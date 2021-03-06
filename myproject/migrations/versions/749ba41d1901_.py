"""empty message

Revision ID: 749ba41d1901
Revises: a0ebb7f24a4a
Create Date: 2021-01-11 12:32:03.337263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749ba41d1901'
down_revision = 'a0ebb7f24a4a'
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
    sa.Column('date_time', sa.Float(), nullable=True),
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
