"""empty message

Revision ID: 4cb05808a316
Revises: 
Create Date: 2021-02-08 16:29:07.783343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb05808a316'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=64), nullable=True),
    sa.Column('user_password', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name'),
    sa.UniqueConstraint('user_password')
    )
    op.create_table('freezer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('shelf_name', sa.String(length=200), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('freezer')
    op.drop_table('user')
    # ### end Alembic commands ###