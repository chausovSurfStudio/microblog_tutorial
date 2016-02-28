"""empty message

Revision ID: 2d8259287862
Revises: df5f62d8f093
Create Date: 2016-02-28 20:04:18.676387

"""

# revision identifiers, used by Alembic.
revision = '2d8259287862'
down_revision = 'df5f62d8f093'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
