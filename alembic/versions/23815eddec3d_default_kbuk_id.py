"""default kbuk id

Revision ID: 23815eddec3d
Revises: bbef259f4d3
Create Date: 2013-09-02 01:58:34.642504

"""

# revision identifiers, used by Alembic.
revision = '23815eddec3d'
down_revision = 'bbef259f4d3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'kbuk_id', server_default='80')



def downgrade():
    pass
