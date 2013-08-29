"""create person table

Revision ID: 470388e8f005
Revises: None
Create Date: 2013-08-29 16:50:42.020026

"""

# revision identifiers, used by Alembic.
revision = '470388e8f005'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'person',
        sa.Column('karatbars_id', sa.String(128), primary_key=True),
        sa.Column('name', sa.String(128)),
        sa.Column('number', sa.String(128)),
        sa.Column('email', sa.String(128)),
        sa.Column('skype', sa.String(128)),
        sa.Column('pic', sa.String(512))
    )


def downgrade():
    op.drop_table('account')
