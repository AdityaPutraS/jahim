"""users table

Revision ID: 1eed6b4550cb
Revises: 
Create Date: 2018-08-09 23:23:04.461128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eed6b4550cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('displayName', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_displayName'), 'user', ['displayName'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('inventori',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namaBarang', sa.String(length=120), nullable=True),
    sa.Column('jumlahBarang', sa.Integer(), nullable=True),
    sa.Column('namaHimpunan', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['namaHimpunan'], ['user.displayName'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventori_jumlahBarang'), 'inventori', ['jumlahBarang'], unique=False)
    op.create_index(op.f('ix_inventori_namaBarang'), 'inventori', ['namaBarang'], unique=True)
    op.create_table('pinjam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namaPeminjam', sa.String(length=120), nullable=True),
    sa.Column('namaBarang', sa.String(length=120), nullable=True),
    sa.Column('namaPemilik', sa.String(length=120), nullable=True),
    sa.Column('jumlahPinjam', sa.Integer(), nullable=True),
    sa.Column('awalPinjam', sa.Integer(), nullable=True),
    sa.Column('akhirPinjam', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['namaPeminjam'], ['user.displayName'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pinjam_jumlahPinjam'), 'pinjam', ['jumlahPinjam'], unique=False)
    op.create_index(op.f('ix_pinjam_namaBarang'), 'pinjam', ['namaBarang'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pinjam_namaBarang'), table_name='pinjam')
    op.drop_index(op.f('ix_pinjam_jumlahPinjam'), table_name='pinjam')
    op.drop_table('pinjam')
    op.drop_index(op.f('ix_inventori_namaBarang'), table_name='inventori')
    op.drop_index(op.f('ix_inventori_jumlahBarang'), table_name='inventori')
    op.drop_table('inventori')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_displayName'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
