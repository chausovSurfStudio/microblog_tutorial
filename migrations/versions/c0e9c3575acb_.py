"""empty message

Revision ID: c0e9c3575acb
Revises: None
Create Date: 2016-02-20 21:54:38.208584

"""

# revision identifiers, used by Alembic.
revision = 'c0e9c3575acb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
