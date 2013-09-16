"""try adding column once again

Revision ID: 3759b016c863
Revises: 4db81d992590
Create Date: 2013-09-15 19:57:28.343940

"""

# revision identifiers, used by Alembic.
revision = '3759b016c863'
down_revision = '4db81d992590'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('affiliate', sa.Column('lttw_id', sa.String(), default='thequietcenter'))


def downgrade():
    op.drop_column('affiliate', 'lttw_id')
