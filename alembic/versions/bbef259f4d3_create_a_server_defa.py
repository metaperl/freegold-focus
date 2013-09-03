"""create a server_default for pic

Revision ID: bbef259f4d3
Revises: 5a010bb3498e
Create Date: 2013-09-02 01:54:37.827316

"""

# revision identifiers, used by Alembic.
revision = 'bbef259f4d3'
down_revision = '5a010bb3498e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'pic', server_default="http://j.mp/17y4bFj")

def downgrade():
    pass
