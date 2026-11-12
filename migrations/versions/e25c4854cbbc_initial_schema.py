from alembic import op
import sqlalchemy as sa


revision = 'e25c4854cbbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'user_table',

        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('hash_password', sa.String(), nullable=False),
        sa.Column('email', sa.String()),
        sa.Column('mobile_no', sa.String(15), nullable=False)
    )

    op.create_table(
        'user_tasks',

        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('is_completed', sa.Boolean()),
        sa.Column('user_id', sa.Integer()),

        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user_table.id'],
            ondelete='CASCADE'
        )
    )


def downgrade():

    op.drop_table('user_tasks')
    op.drop_table('user_table')