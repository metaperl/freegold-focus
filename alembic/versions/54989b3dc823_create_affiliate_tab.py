"""create affiliate table

Revision ID: 54989b3dc823
Revises: None
Create Date: 2013-09-02 01:26:31.467760

"""

# revision identifiers, used by Alembic.
revision = '54989b3dc823'
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
        sa.Column('pic', sa.String(512), default="http://j.mp/17y4bFj"),
        sa.Column('kbuk_id', sa.Integer, nullable=True)
    )


def downgrade():
    op.drop_table('affiliate')
