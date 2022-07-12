"""edit column

Revision ID: 9e8956c3d2dc
Revises: 4e614956af39
Create Date: 2022-07-12 17:58:27.687393

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9e8956c3d2dc'
down_revision = '4e614956af39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('demo', 'description',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=60),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('demo', 'description',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    # ### end Alembic commands ###
