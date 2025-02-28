"""modifed task model

Revision ID: 1f58e4a53c1b
Revises: 63fd0e87bb52
Create Date: 2023-05-10 10:23:43.645763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f58e4a53c1b'
down_revision = '63fd0e87bb52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('description', sa.String(), nullable=True))
    op.add_column('task', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('task', 'task_description')
    op.drop_column('task', 'task_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('task_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('task', sa.Column('task_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('task', 'title')
    op.drop_column('task', 'description')
    # ### end Alembic commands ###
