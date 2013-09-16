"""add lttw default id

Revision ID: 4db81d992590
Revises: 3d2ecf8503bb
Create Date: 2013-09-15 13:48:40.504590

"""

# revision identifiers, used by Alembic.
revision = '4db81d992590'
down_revision = '3d2ecf8503bb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'lttw_id', server_default='thequietcenter')


def downgrade():
    pass
