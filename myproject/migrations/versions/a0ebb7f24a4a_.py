"""empty message

Revision ID: a0ebb7f24a4a
Revises: 
Create Date: 2021-01-11 12:15:20.641934

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a0ebb7f24a4a'
down_revision = None
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