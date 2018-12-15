"""create tables

Revision ID: 5941c46d777d
Revises:
Create Date: 2017-08-24 02:58:15.521490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5941c46d777d'
down_revision = None
branch_labels = None
depends_on = None

table_name = 'affiliate'


def upgrade():
    op.create_table(
        table_name,
        sa.Column('kb_id', sa.String(128), primary_key=True, nullable=False),

        sa.Column('gfg', sa.Boolean),
        sa.Column('kbuk_id', sa.Integer),
        sa.Column('lttw_id', sa.String(128)),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('number', sa.String(128), nullable=False),
        sa.Column('email', sa.String(128), nullable=False),
        sa.Column('pic', sa.String(1024), nullable=False),
        sa.Column('skype', sa.String(128))
    )



def downgrade():
    op.drop_table(table_name)
