"""columns to be nullable must be set as such

Revision ID: 553c19af3dd5
Revises: 470388e8f005
Create Date: 2013-08-29 21:48:35.268801

"""

# revision identifiers, used by Alembic.
revision = '553c19af3dd5'
down_revision = '470388e8f005'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('affiliate', 'name', nullable=False, existing_type=sa.String(128)),
    op.alter_column('affiliate', 'number', nullable=False, existing_type=sa.String(128)),
    op.alter_column('affiliate', 'email', nullable=False, existing_type=sa.String(128)),
    op.alter_column('affiliate', 'pic', nullable=False, existing_type=sa.String(512))


def downgrade():
    pass
