from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required, login_manager
from werkzeug.urls import url_parse
from sqlalchemy import desc

from app import app, db
from app.models import User, Person, Pizza
from app.admin.forms import LoginForm, EditProfileForm, NewUserForm, NewPizzaForm

import locale


# Record last user visit
@app.before_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.now()
    db.session.commit()


# Dashboard Route
@app.route('/dashboard')
@login_required
def dashboard():
  title = 'Dashboard'
  return render_template('admin/index.html', title=title)


# Login Route
@app.route('/dashboard/login', methods=['GET', 'POST'])
def dashboardLogin():
  title = 'Login'
  # If user is already authenticated redirect to dashboard
  if current_user.is_authenticated:
    return redirect(url_for('dashboard'))
  # Render login form
  form = LoginForm()
  # Get data from login form
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    # Check username and password
    if user is None or not user.check_password(form.password.data):
      flash('Usuário ou senha inválida')
      return redirect(url_for('dashboardLogin'))
    # Get remember_me value
    login_user(user, remember=form.remember_me.data)
    # Set redirect back from the successful login
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('dashboard')
    return redirect(next_page)
  return render_template('admin/login.html', form=form, title=title)


# Logout
@app.route('/dashboard/logout')
def dashboardLogout():
  logout_user()
  return redirect(url_for('index'))


# User profile
@app.route('/dashboard/user/<username>')
@login_required
def userAdmin(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('admin/user.html', user=user)


# Edit profile form
@app.route('/dashboard/user/edit_profile', methods=['GET', 'POST'])
@login_required
def editUserProfile():
  form = EditProfileForm()
  form_profile = NewUserForm()
  # User Form
  if form.validate_on_submit():
    current_user.username = form.username.data
    if form.password.data:
      current_user.set_password(form.password.data)
    # User personal data
    current_user.person.person_name=form_profile.person_name.data
    current_user.person.lastname=form_profile.lastname.data
    current_user.person.email=form_profile.email.data
    current_user.person.phone=form_profile.phone.data
    current_user.person.address=form_profile.address.data
    current_user.person.is_admin=form_profile.is_admin.data
    
    db.session.commit()
    flash('Alterações realizadas com sucesso!')
    return redirect(url_for('editProfile'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form_profile.person_name.data = current_user.person.person_name
    form_profile.lastname.data = current_user.person.lastname
    form_profile.email.data = current_user.person.email
    form_profile.phone.data = current_user.person.phone
    form_profile.address.data = current_user.person.address
    
  return render_template('admin/edit_profile.html', form=form, form_profile=form_profile)


@app.route('/dashboard/user/new_user', methods=['GET', 'POST'])
@login_required
def newUser():
  form = NewUserForm()
  if request.method == 'POST':
    person = Person(
      person_name=form.person_name.data,
      lastname=form.lastname.data,
      email=form.email.data,
      phone=form.phone.data,
      address=form.address.data,
      is_admin=form.is_admin.data,
      user=form.user.data,
      orders=form.orders.data
    )
    db.session.add(person)
    db.session.commit()
    flash('{} cadastrado(a) com sucesso!'.format(person.name.capitalize()))
    return redirect(url_for('dashboard'))
  return render_template('admin/new_user.html', form=form)

# List pizza
@app.route('/dashboard/pizzas')
@login_required
def pizzas():
  title = 'Lista Pizza'
  pizzas = Pizza.query.order_by(Pizza.id).all()
  # pizzas.order_by(desc(pizzas.id))
  return render_template('admin/list_pizzas.html', title=title, pizzas=pizzas)


# Create a new Pizza
@app.route('/dashboard/pizzas/new', methods=['GET', 'POST'])
@login_required
def newPizza():
  form = NewPizzaForm()
  if request.method == 'POST':
    pizza = Pizza(
      pizza_name=form.pizza_name.data,
      ingredients=form.ingredients.data,
      size=form.size.data,
      stuffed_edge=form.stuffed_edge.data,
      img_link=form.img_link.data,
      price=form.price.data
    )
    db.session.add(pizza)
    db.session.commit()
    flash('Pizza {} adicionada com sucesso!'.format(pizza.pizza_name))
    return redirect(url_for('pizzas'))    
  return render_template('admin/new_pizza.html', form=form)

# Edit a pizza
@app.route('/dashboard/pizzas/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def editPizza(id):
  form = NewPizzaForm()
  pizza = Pizza.query.get(id)
  if form.validate_on_submit():
    pizza.pizza_name=form.pizza_name.data
    pizza.ingredients=form.ingredients.data
    pizza.size=form.size.data
    pizza.stuffed_edge=form.stuffed_edge.data
    pizza.img_link=form.img_link.data
    pizza.price=form.price.data
    db.session.commit()
    flash('Alterações realizadas com sucesso!')
    return redirect(url_for('pizzas'))
  elif request.method == 'GET':
    form.pizza_name.data = pizza.pizza_name
    form.ingredients.data = pizza.ingredients
    form.size.data = pizza.size
    form.stuffed_edge.data = pizza.stuffed_edge
    form.img_link.data = pizza.img_link
    form.price.data = pizza.price
  return render_template('admin/new_pizza.html', form=form)

@app.route('/dashboard/pizzas/<int:id>')
@login_required
def modalDelete(id):
  pizza = Pizza.query.filter_by(id = id).first()
  return render_template('admin/list_pizzas.html', pizza = pizza)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
  pizza = Pizza.query.filter_by(id = id).first()
  db.session.delete(pizza)
  db.session.commit()
  return redirect(url_for('pizzas'))