"""create owners table

Revision ID: c019c05149f4
Revises: 106d25864014
Create Date: 2021-11-06 00:42:21.261763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c019c05149f4'
down_revision = '106d25864014'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('about', sa.String(), nullable=True))
    op.add_column('users', sa.Column('profile_photo', sa.String(), nullable=True))
    op.add_column('users', sa.Column('private', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'private')
    op.drop_column('users', 'profile_photo')
    op.drop_column('users', 'about')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###