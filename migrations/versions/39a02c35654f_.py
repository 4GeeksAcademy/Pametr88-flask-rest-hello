"""empty message

Revision ID: 39a02c35654f
Revises: 
Create Date: 2023-11-24 21:08:43.009172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a02c35654f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.String(length=120), nullable=False),
    sa.Column('hair_color', sa.String(length=120), nullable=False),
    sa.Column('skin_color', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('eye_color'),
    sa.UniqueConstraint('hair_color'),
    sa.UniqueConstraint('height'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('skin_color')
    )
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created', sa.String(length=120), nullable=False),
    sa.Column('edited', sa.String(length=120), nullable=False),
    sa.Column('producer', sa.String(length=120), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('director', sa.String(length=120), nullable=False),
    sa.Column('release_date', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('created'),
    sa.UniqueConstraint('director'),
    sa.UniqueConstraint('edited'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('producer'),
    sa.UniqueConstraint('release_date'),
    sa.UniqueConstraint('title')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.String(length=120), nullable=False),
    sa.Column('orbital_period', sa.String(length=120), nullable=False),
    sa.Column('gravity', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('diameter'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('orbital_period'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('rotation_period')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('classification', sa.String(length=120), nullable=False),
    sa.Column('designation', sa.String(length=120), nullable=False),
    sa.Column('average_height', sa.String(length=120), nullable=False),
    sa.Column('average_lifespan', sa.String(length=120), nullable=False),
    sa.Column('hair_colors', sa.String(length=120), nullable=False),
    sa.Column('skin_colors', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('average_height'),
    sa.UniqueConstraint('average_lifespan'),
    sa.UniqueConstraint('classification'),
    sa.UniqueConstraint('designation'),
    sa.UniqueConstraint('hair_colors'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('skin_colors')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.Column('films_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['films_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('species')
    op.drop_table('planets')
    op.drop_table('films')
    op.drop_table('character')
    # ### end Alembic commands ###