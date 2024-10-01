"""initial

Revision ID: e0972cef1617
Revises: 
Create Date: 2024-10-01 19:04:20.061466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0972cef1617'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manufacturers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer_name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('row', sa.Integer(), nullable=False),
    sa.Column('cell', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('manufacturer_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('expiration_date', sa.Date(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=False),
    sa.Column('stock_location', sa.Integer(), nullable=False),
    sa.Column('stock_quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['product_categories.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturers.id'], ),
    sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_feature_association',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('feature_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feature_id'], ['product_features.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'feature_id')
    )
    op.create_table('shipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('shipment_date', sa.Date(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('supplier_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

  


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procedure_appointment',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('procedure_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('staff_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], name='procedure_appointment_client_id_fkey'),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='procedure_appointment_procedure_id_fkey'),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], name='procedure_appointment_staff_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='procedure_appointment_pkey')
    )
    op.create_table('clients',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('clients_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='clients_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('accommodations_usage',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('accommodations_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('room_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('start_data', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('end_data', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['accommodations_id'], ['accommodations.id'], name='accommodations_usage_accommodations_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='accommodations_usage_pkey')
    )
    op.create_table('bookings',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('bookings_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('accommodation_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('check_in_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('check_out_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodations.id'], name='bookings_accommodation_id_fkey'),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], name='bookings_client_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='bookings_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('room_usage',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('procedure_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('staff_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='room_usage_procedure_id_fkey'),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name='room_usage_room_id_fkey'),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], name='room_usage_staff_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='room_usage_pkey')
    )
    op.create_table('procedures',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('procedure_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='procedures_pkey')
    )
    op.create_table('accommodations',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('accommodations_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('room_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('daily_rate', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='accommodations_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('staff',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='staff_pkey')
    )
    op.create_table('room_status',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('booking_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['booking_id'], ['bookings.id'], name='room_status_booking_id_fkey'),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name='room_status_room_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='room_status_pkey')
    )
    op.create_table('rooms',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('purpose', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='rooms_pkey')
    )
    op.drop_table('shipments')
    op.drop_table('product_feature_association')
    op.drop_table('products')
    op.drop_table('stock')
    op.drop_table('product_features')
    op.drop_table('product_categories')
    op.drop_table('manufacturers')
    # ### end Alembic commands ###
