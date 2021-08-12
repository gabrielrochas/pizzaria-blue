from datetime import datetime
from enum import Enum
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(id):
  return User.query.get(int(id))


class Person(db.Model):
  __tablename__ = 'people'

  id = db.Column(db.Integer, primary_key=True)
  person_name = db.Column(db.String(64), index=True, nullable=False)
  lastname = db.Column(db.String(120))
  email = db.Column(db.String(128), index=True, unique=True, nullable=False)
  phone = db.Column(db.String(15), unique=True, nullable=False)
  address = db.Column(db.String(200), nullable=False)
  is_admin = db.Column(db.Boolean, default=False)
  user = db.relationship('User', backref='person', uselist=False)
  orders = db.relationship('Order', backref='customer', lazy='dynamic')


  def __repr__(self):
    return '<Nome {}>'.format(self.person_name)
  
  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, nullable=False, unique=True)
  password = db.Column(db.String(128))
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)
  person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

  def __repr__(self):
    return '<Usuário {}>'.format(self.username)


  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)


# class PizzaSize(Enum):
#   Brotinho = 'Brotinho'
#   Normal = 'Normal'


class Pizza(db.Model):
  __tablename__ = 'pizzas'

  id = db.Column(db.Integer, primary_key=True)
  pizza_name = db.Column(db.String(64), index=True, unique=True, nullable=False)
  ingredients = db.Column(db.String(240), nullable=False)
  # size = db.Column(db.Enum(PizzaSize))
  size = db.Column(db.String(50), default='Normal')
  stuffed_edge = db.Column(db.Boolean, default=False)
  img_link = db.Column(db.String(240), nullable=False)
  price = db.Column(db.Float(precision=2), nullable=False)
  order = db.relationship('Order', backref='pizza', lazy='dynamic')

  def __repr__(self):
    return '<Pizza: {} Tamanho: {}>'.format(self.pizza_name, self.size)

class PaymentType(Enum):
  Cartão = 'cartao'
  Débito = 'debito'
  Dinheiro = 'dinheiro'

class Order(db.Model):
  __tablename__ = 'orders'

  id = db.Column(db.Integer, primary_key=True)
  person_id = db.Column(db.Integer, db.ForeignKey('people.id'))
  pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
  total = db.Column(db.Float(precision=2), nullable=False)
  payment = db.Column(db.Enum(PaymentType))
  details = db.Column(db.String(240))
  order_date = db.Column(db.DateTime, index=True,default=datetime.utcnow)