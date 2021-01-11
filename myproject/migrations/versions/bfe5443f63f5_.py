"""empty message

Revision ID: bfe5443f63f5
Revises: 749ba41d1901
Create Date: 2021-01-11 13:07:45.924176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bfe5443f63f5'
down_revision = '749ba41d1901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade_quote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade_quote',
    sa.Column('date_time', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('q_open', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('q_high', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('q_low', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('q_close', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('q_adj_close', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('q_volume', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('q_name_id', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###