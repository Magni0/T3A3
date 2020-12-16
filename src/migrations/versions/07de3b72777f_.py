"""empty message

Revision ID: 07de3b72777f
Revises: 5e7c1125e285
Create Date: 2020-12-16 18:38:53.939025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07de3b72777f'
down_revision = '5e7c1125e285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracks', sa.Column('moods_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tracks', 'moods', ['moods_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tracks', type_='foreignkey')
    op.drop_column('tracks', 'moods_id')
    # ### end Alembic commands ###
