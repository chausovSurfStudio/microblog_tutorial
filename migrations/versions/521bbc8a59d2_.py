"""empty message

Revision ID: 521bbc8a59d2
Revises: 0054623b7be8
Create Date: 2016-02-22 12:47:46.112127

"""

# revision identifiers, used by Alembic.
revision = '521bbc8a59d2'
down_revision = '0054623b7be8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
