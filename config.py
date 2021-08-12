import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  # SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nunca-vai-adivinhar!'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgresql://ekyovyji:RLdcObC5xJqb-b1hUmoa8d1VVcXUfEzX@kesavan.db.elephantsql.com/ekyovyji'
  SQLALCHEMY_TRACK_MODIFICATIONS = False