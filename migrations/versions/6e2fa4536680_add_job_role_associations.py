"""add_job_role_associations

Revision ID: 6e2fa4536680
Revises:
Create Date: 2026-11-19 14:22:28.131219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e2fa4536680'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'job_role_associations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('job_id', sa.Integer(), nullable=False),
        sa.Column('canonical_role_id', sa.String(), nullable=False),
        sa.Column('professional_field_id', sa.String(), nullable=False),
        sa.Column('subfield_id', sa.String(), nullable=True),
        sa.Column('match_type', sa.String(), nullable=False),
        sa.Column('matched_term', sa.String(), nullable=True),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True
        ),
        sa.ForeignKeyConstraint(
            ['job_id'],
            ['jobs.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'job_id',
            'canonical_role_id',
            name='uq_job_role_association'
        )
    )

    op.create_index(
        'ix_job_role_associations_id',
        'job_role_associations',
        ['id'],
        unique=False
    )
    op.create_index(
        'ix_job_role_associations_job_id',
        'job_role_associations',
        ['job_id'],
        unique=False
    )
    op.create_index(
        'ix_job_role_associations_canonical_role_id',
        'job_role_associations',
        ['canonical_role_id'],
        unique=False
    )
    op.create_index(
        'ix_job_role_associations_professional_field_id',
        'job_role_associations',
        ['professional_field_id'],
        unique=False
    )
    op.create_index(
        'ix_job_role_associations_subfield_id',
        'job_role_associations',
        ['subfield_id'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        'ix_job_role_associations_subfield_id',
        table_name='job_role_associations'
    )
    op.drop_index(
        'ix_job_role_associations_professional_field_id',
        table_name='job_role_associations'
    )
    op.drop_index(
        'ix_job_role_associations_canonical_role_id',
        table_name='job_role_associations'
    )
    op.drop_index(
        'ix_job_role_associations_job_id',
        table_name='job_role_associations'
    )
    op.drop_index(
        'ix_job_role_associations_id',
        table_name='job_role_associations'
    )
    op.drop_table('job_role_associations')
