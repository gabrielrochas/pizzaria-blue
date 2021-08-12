from flask import render_template, request

from app import app, db
from app.models import Pizza, Person
from app.admin.forms import NewUserForm


@app.route('/')
def index():
  pizzas = Pizza.query.order_by(Pizza.price).all()
  return render_template('index.html', pizzas=pizzas)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/members')
def members():
  return render_template('members.html')

@app.route('/fale-conosco')
def faleConosco():
  return render_template('fale-conosco.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
  form = NewUserForm()
  if request.method == 'POST':
    person = Person(
      person_name=form.person_name.data,
      lastname=form.lastname.data,
      email=form.email.data,
      phone=form.phone.data,
      address=form.address.data,
    )
    db.session.add(person)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('checkout.html', form = form)