"""empty message

Revision ID: de65e56818e4
Revises: d1aa6d291037
Create Date: 2020-09-09 13:55:25.274814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de65e56818e4'
down_revision = 'd1aa6d291037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('log_counter', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'log_counter')
    # ### end Alembic commands ###
