from app import app, db
from app.models import Person, User, Pizza, Order

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'Person': Person, 'User': User, 'Pizza': Pizza, 'Order': Order}