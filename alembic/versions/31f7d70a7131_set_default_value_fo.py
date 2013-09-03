"""set default value for skype id

Revision ID: 31f7d70a7131
Revises: 23815eddec3d
Create Date: 2013-09-02 08:58:33.521965

"""

# revision identifiers, used by Alembic.
revision = '31f7d70a7131'
down_revision = '23815eddec3d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'skype', server_default='metaperl')


def downgrade():
    pass
