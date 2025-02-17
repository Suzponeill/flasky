"""added cyclist model

Revision ID: 8ac1f0fa94f9
Revises: 1d06c651046f
Create Date: 2022-11-07 11:03:57.153344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ac1f0fa94f9'
down_revision = '1d06c651046f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cyclist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cyclist')
    # ### end Alembic commands ###
