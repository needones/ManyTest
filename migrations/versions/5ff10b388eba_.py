"""empty message

Revision ID: 5ff10b388eba
Revises: d2a94b509d79
Create Date: 2018-10-11 11:02:02.950740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ff10b388eba'
down_revision = 'd2a94b509d79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('m_name', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_name', sa.String(length=16), nullable=True),
    sa.Column('u_age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collect',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user', sa.Integer(), nullable=True),
    sa.Column('c_movie', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_movie'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['c_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collect')
    op.drop_table('user')
    op.drop_table('movie')
    # ### end Alembic commands ###
