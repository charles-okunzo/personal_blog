"""empty message

Revision ID: 5b75d05aab40
Revises: 56cbe75bd5ab
Create Date: 2022-05-17 12:00:53.597397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b75d05aab40'
down_revision = '56cbe75bd5ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_blogpost_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'blogpost_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blogpost_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_blogpost_id_fkey', 'comments', 'blogposts', ['blogpost_id'], ['id'])
    # ### end Alembic commands ###
