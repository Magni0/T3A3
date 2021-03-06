"""empty message

Revision ID: ef839c6b5434
Revises: 07de3b72777f
Create Date: 2020-12-28 19:20:44.450380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef839c6b5434'
down_revision = '07de3b72777f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('moods', 'amusement',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'annoyance',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'anxiety',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'beauty',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'defiance',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'dreaminess',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'feelingpumped',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'joy',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'relaxation',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'sadness',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'scariness',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('moods', 'triumph',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('moods', 'triumph',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'scariness',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'sadness',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'relaxation',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'joy',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'feelingpumped',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'dreaminess',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'defiance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'beauty',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'anxiety',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'annoyance',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('moods', 'amusement',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
