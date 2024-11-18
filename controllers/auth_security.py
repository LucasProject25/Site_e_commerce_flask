#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import Flask, request, render_template, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from connexion_db import get_db

auth_security = Blueprint('auth_security', __name__,
                        template_folder='templates')

@auth_security.route('/login')
def auth_login():
    return render_template('auth/login.html')


@auth_security.route('/login', methods=['POST'])
def auth_login_post():
    mycursor = get_db().cursor()
    login = request.form.get('login')
    password = request.form.get('password')
    tuple_select = (login)
    sql = '''SELECT  * 
             FROM utilisateur 
             WHERE login = %s'''
    retour = mycursor.execute(sql, tuple_select)
    user = mycursor.fetchone()
    if user:
        mdp_ok = check_password_hash(user['password'], password)
        if not mdp_ok:
            flash(u'Vérifier votre mot de passe et essayer encore.', 'alert-warning')
            return redirect('/login')
        else:
            session['login'] = user['login']
            session['role'] = user['role']
            session['id_user'] = user['id_utilisateur']
            print(user['login'], user['role'])
            if user['role'] == 'ROLE_admin':
                return redirect('/admin/commande/index')
            else:
                return redirect('/client/boisson/show')
    else:
        flash(u'Vérifier votre login et essayer encore.', 'alert-warning')
        return redirect('/login')

@auth_security.route('/signup')
def auth_signup():
    return render_template('auth/signup.html')


@auth_security.route('/signup', methods=['POST'])
def auth_signup_post():
    mycursor = get_db().cursor()
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')
    tuple_select = (login, email)
    sql = '''SELECT id_utilisateur
             FROM utilisateur
             WHERE login = %s AND email = %s;   '''
    retour = mycursor.execute(sql, tuple_select)
    user = mycursor.fetchone()
    if user:
        flash(u'votre adresse Email ou  votre Login existe déjà', 'alert-warning')
        return redirect('/signup')

    # ajouter un nouveau user
    password = generate_password_hash(password, method='sha256')
    tuple_insert = (login, email, password, 'ROLE_client', login)
    sql = ''' INSERT INTO utilisateur(login,email,password,role,nom) VALUES
              (%s,%s,%s,%s,%s)'''
    mycursor.execute(sql, tuple_insert)
    get_db().commit()

    sql = """ SELECT LAST_INSERT_ID() AS last_insert_id
              FROM utilisateur;  """
    mycursor.execute(sql)
    info_last_id = mycursor.fetchone()
    id_user = info_last_id['last_insert_id']
    print('last_insert_id', id_user)
    session.pop('login', None)
    session.pop('role', None)
    session.pop('id_user', None)
    session['login'] = login
    session['role'] = 'ROLE_client'
    session['id_user'] = id_user
    return redirect('/client/boisson/show')


@auth_security.route('/logout')
def auth_logout():
    session.pop('login', None)
    session.pop('role', None)
    session.pop('id_user', None)
    if 'filter_word' in session:
        session.pop('filter_word')
    if 'filter_prix_min' in session:
        session.pop('filter_prix_min')
    if 'filter_prix_max' in session:
        session.pop('filter_prix_max')
    if 'filter_types' in session:
        session.pop('filter_types')
    return redirect('/')

@auth_security.route('/forget-password', methods=['GET'])
def forget_password():
    return render_template('auth/forget_password.html')
