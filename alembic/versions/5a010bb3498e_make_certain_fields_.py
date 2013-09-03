"""make certain fields not nullable

Revision ID: 5a010bb3498e
Revises: 54989b3dc823
Create Date: 2013-09-02 01:38:58.373842

"""

# revision identifiers, used by Alembic.
revision = '5a010bb3498e'
down_revision = '54989b3dc823'

from alembic import op
import sqlalchemy as sa


def upgrade():
    for column in 'name number email'.split():
        op.alter_column('affiliate', column, nullable=False)


def downgrade():
    pass
