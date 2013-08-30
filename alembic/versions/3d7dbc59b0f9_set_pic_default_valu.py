"""set pic default value

Revision ID: 3d7dbc59b0f9
Revises: 553c19af3dd5
Create Date: 2013-08-29 21:59:35.563799

"""

# revision identifiers, used by Alembic.
revision = '3d7dbc59b0f9'
down_revision = '553c19af3dd5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'pic', server_default='https://www.evernote.com/shard/s309/sh/ff96d662-fe19-45b0-b845-9173abc1aa58/309fd4d7c62dcbea928682bc9ef5fbed/deep/0/Screenshot%208/24/13%201:33%20PM.jpg', existing_type=sa.String(512))



def downgrade():
    pass
