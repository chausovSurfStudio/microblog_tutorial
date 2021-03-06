"""empty message

Revision ID: 0054623b7be8
Revises: c0e9c3575acb
Create Date: 2016-02-20 22:20:43.994645

"""

# revision identifiers, used by Alembic.
revision = '0054623b7be8'
down_revision = 'c0e9c3575acb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    ### end Alembic commands ###
