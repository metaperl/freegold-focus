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
        'affiliate',
        sa.Column('id', sa.String(128), primary_key=True),
        sa.Column('name', sa.String(128)),
        sa.Column('number', sa.String(128)),
        sa.Column('email', sa.String(128)),
        sa.Column('skype', sa.String(128), nullable=True),
        sa.Column(
            'pic', sa.String(512),
            default="https://www.evernote.com/shard/s309/sh/ff96d662-fe19-45b0-b845-9173abc1aa58/309fd4d7c62dcbea928682bc9ef5fbed/deep/0/Screenshot%208/24/13%201:33%20PM.jpg"
        ),
        sa.Column('kbuk_id', sa.Integer, nullable=True)

    )


def downgrade():
    op.drop_table('affiliate')
