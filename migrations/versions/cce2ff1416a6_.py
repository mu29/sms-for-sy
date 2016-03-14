"""empty message

Revision ID: cce2ff1416a6
Revises: None
Create Date: 2016-03-14 23:39:41.360111

"""

# revision identifiers, used by Alembic.
revision = 'cce2ff1416a6'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('age', sa.String(), nullable=True),
    sa.Column('school', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('contact', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    ### end Alembic commands ###
