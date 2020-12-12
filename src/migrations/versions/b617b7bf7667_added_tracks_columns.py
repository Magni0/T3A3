"""added Tracks columns

Revision ID: b617b7bf7667
Revises: 
Create Date: 2020-12-12 15:23:08.587235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b617b7bf7667'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userprofile',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('displayname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userprofile')
    # ### end Alembic commands ###