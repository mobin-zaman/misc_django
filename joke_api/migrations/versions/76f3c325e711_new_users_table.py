"""new users table

Revision ID: 76f3c325e711
Revises: 40246ea4b5e1
Create Date: 2019-05-11 12:14:22.688521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76f3c325e711'
down_revision = '40246ea4b5e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('joined_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'joined_on')
    # ### end Alembic commands ###
