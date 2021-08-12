from enum import Enum
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, Length

# Login Form
class LoginForm(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired()])
  password = PasswordField('Senha', validators=[DataRequired()])
  remember_me = BooleanField('Lembrar de mim')
  submit = SubmitField('Entrar')

# Edit Profile Form
class EditProfileForm(FlaskForm):
  username = StringField('Nome de usuário', validators=[DataRequired()])
  password = PasswordField('Nova senha')
  submit = SubmitField('Salvar')


# New/Edit User Form
class NewUserForm(FlaskForm):
  person_name = StringField('Nome', validators=[DataRequired()])
  lastname = StringField('Sobrenome')
  email = EmailField('E-mail', validators=[DataRequired()])
  phone = TelField('Fone', validators=[DataRequired()])
  address = StringField('Endereço', validators=[DataRequired()])
  is_admin = BooleanField('Usuário do Sistema')
  submit = SubmitField('Finalizar Compra')


# New/Edit Pizza Form
# Size list
class PizzaSize(Enum):
  Brotinho = 'Brotinho'
  Normal = 'Normal'


# Pizza Form
class NewPizzaForm(FlaskForm):
  pizza_name = StringField('Sabor', validators=[DataRequired()])
  ingredients = TextAreaField('Ingredientes', validators=[DataRequired()])
  size = SelectField("Tamanho", choices=[(choice.name, choice.value) for choice in PizzaSize])
  stuffed_edge = BooleanField('Borda Recheada')
  img_link = StringField('Link da Imagem', validators=[DataRequired()])
  price = FloatField('Preço', )
  submit = SubmitField('Salvar')
 