"""empty message

Revision ID: 1bfb12f7af55
Revises: 8b6ce0ede847
Create Date: 2021-01-11 13:27:34.385640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bfb12f7af55'
down_revision = '8b6ce0ede847'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.String(length=80), nullable=False),
    sa.Column('q_open', sa.Float(), nullable=True),
    sa.Column('q_high', sa.Float(), nullable=True),
    sa.Column('q_low', sa.Float(), nullable=True),
    sa.Column('q_adj_close', sa.Float(), nullable=True),
    sa.Column('q_close', sa.Float(), nullable=True),
    sa.Column('q_volume', sa.Float(), nullable=True),
    sa.Column('q_name_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['q_name_id'], ['quotes_name.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote')
    op.drop_table('quotes_name')
    # ### end Alembic commands ###