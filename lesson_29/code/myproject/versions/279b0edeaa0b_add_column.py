"""add column

Revision ID: 279b0edeaa0b
Revises: bfa797c2f29f
Create Date: 2024-12-09 21:43:24.718035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '279b0edeaa0b'
down_revision = 'bfa797c2f29f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('email_', sa.String(255)))
    pass


def downgrade():
    pass
