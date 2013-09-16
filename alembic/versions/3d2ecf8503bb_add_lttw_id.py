"""add lttw id

Revision ID: 3d2ecf8503bb
Revises: 31f7d70a7131
Create Date: 2013-09-15 13:41:25.872782

"""

# revision identifiers, used by Alembic.
revision = '3d2ecf8503bb'
down_revision = '31f7d70a7131'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('affiliate', sa.Column('lttw_id', sa.String()))

def downgrade():
    op.drop_column('affiliate', 'lttw_id')
