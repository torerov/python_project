"""empty message

Revision ID: bf62f99e6e
Revises: 2e39de817df
Create Date: 2016-01-06 21:15:59.975970

"""

# revision identifiers, used by Alembic.
revision = 'bf62f99e6e'
down_revision = '2e39de817df'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('password', sa.VARCHAR(length=20), nullable=False),
    sa.Column('role', sa.VARCHAR(length=20), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
