"""empty message

Revision ID: 2d557030e802
Revises: 
Create Date: 2021-08-10 10:24:12.375491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d557030e802'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_name', sa.String(length=64), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_people_email'), 'people', ['email'], unique=True)
    op.create_index(op.f('ix_people_person_name'), 'people', ['person_name'], unique=False)
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza_name', sa.String(length=64), nullable=False),
    sa.Column('ingredients', sa.String(length=240), nullable=False),
    sa.Column('size', sa.Enum('Brotinho', 'Normal', name='pizzasize'), nullable=True),
    sa.Column('stuffed_edge', sa.Boolean(), nullable=True),
    sa.Column('img_link', sa.String(length=240), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pizzas_pizza_name'), 'pizzas', ['pizza_name'], unique=True)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.Column('total', sa.Float(precision=2), nullable=False),
    sa.Column('payment', sa.Enum('Cartão', 'Débito', 'Dinheiro', name='paymenttype'), nullable=True),
    sa.Column('details', sa.String(length=240), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_order_date'), 'orders', ['order_date'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('pessoa_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pessoa_id'], ['people.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_orders_order_date'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_pizzas_pizza_name'), table_name='pizzas')
    op.drop_table('pizzas')
    op.drop_index(op.f('ix_people_person_name'), table_name='people')
    op.drop_index(op.f('ix_people_email'), table_name='people')
    op.drop_table('people')
    # ### end Alembic commands ###
