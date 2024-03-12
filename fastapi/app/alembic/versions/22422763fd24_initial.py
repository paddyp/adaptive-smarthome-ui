"""initial

Revision ID: 22422763fd24
Revises: 
Create Date: 2024-03-11 15:33:23.206902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22422763fd24'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adaptuirule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('explaination', sa.Text(), nullable=True),
    sa.Column('explaination_level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_adaptuirule_level'), 'adaptuirule', ['level'], unique=False)
    op.create_table('contextofuse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=255), nullable=True),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('type', sa.Enum('INT', 'FLOAT', 'STRING', 'JSON', 'DEVICE', name='typeenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contextofuse_key'), 'contextofuse', ['key'], unique=False)
    op.create_index(op.f('ix_contextofuse_value'), 'contextofuse', ['value'], unique=False)
    op.create_table('metauielement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('uielement', sa.Enum('BUTTON', 'TOGGLEBUTTON', 'SLIDER', 'TRIANGLE', name='uielementenum'), nullable=True),
    sa.Column('current_value', sa.Integer(), nullable=True),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.Column('max', sa.Integer(), nullable=True),
    sa.Column('step', sa.Integer(), nullable=True),
    sa.Column('min_color', sa.String(length=7), nullable=True),
    sa.Column('max_color', sa.String(length=7), nullable=True),
    sa.Column('layoutlevel', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('smarthomedevice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('icon', sa.Enum('LAMP', 'HEATER', 'SHUTTER', name='iconenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adaptuiruleinfluencedcontextvars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.Column('contextofuse_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['contextofuse_id'], ['contextofuse.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adaptuiruleorcondition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('createviewaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metauielement_id', sa.Integer(), nullable=True),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['metauielement_id'], ['metauielement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deleteviewaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metauielement_id', sa.Integer(), nullable=True),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['metauielement_id'], ['metauielement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('layoutchangeaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metauielement_id', sa.Integer(), nullable=True),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(length=100), nullable=True),
    sa.Column('value', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['metauielement_id'], ['metauielement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('metauielemeentvalue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.Column('max', sa.Integer(), nullable=True),
    sa.Column('metauielement_id', sa.Integer(), nullable=True),
    sa.Column('contextofuse_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contextofuse_id'], ['contextofuse.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['metauielement_id'], ['metauielement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('smarthomedevicechannel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('channel_no', sa.Integer(), nullable=True),
    sa.Column('smarthomedevice_id', sa.Integer(), nullable=True),
    sa.Column('contextofuse_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('INT', 'FLOAT', 'COLOR_RED', 'COLOR_GREEN', 'COLOR_BLUE', 'DIMMER', name='smarthomedevicechanneltypeenum'), nullable=True),
    sa.ForeignKeyConstraint(['contextofuse_id'], ['contextofuse.id'], ),
    sa.ForeignKeyConstraint(['smarthomedevice_id'], ['smarthomedevice.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adaptuiruleandcondition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orcondition_id', sa.Integer(), nullable=True),
    sa.Column('contextvar_id', sa.Integer(), nullable=True),
    sa.Column('operator', sa.Enum('EQUAL', 'NOTEQUAL', 'GREATER', 'LOWER', 'GREATEREQUAL', 'LOWEREQUAL', name='operatorenum'), nullable=True),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['contextvar_id'], ['contextofuse.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['orcondition_id'], ['adaptuiruleorcondition.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adjustvalueviewaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('metauielemeentvalue_id', sa.Integer(), nullable=True),
    sa.Column('adaptuirule_id', sa.Integer(), nullable=True),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.Column('max', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adaptuirule_id'], ['adaptuirule.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['metauielemeentvalue_id'], ['metauielemeentvalue.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adjustvalueviewaction')
    op.drop_table('adaptuiruleandcondition')
    op.drop_table('smarthomedevicechannel')
    op.drop_table('metauielemeentvalue')
    op.drop_table('layoutchangeaction')
    op.drop_table('deleteviewaction')
    op.drop_table('createviewaction')
    op.drop_table('adaptuiruleorcondition')
    op.drop_table('adaptuiruleinfluencedcontextvars')
    op.drop_table('smarthomedevice')
    op.drop_table('metauielement')
    op.drop_index(op.f('ix_contextofuse_value'), table_name='contextofuse')
    op.drop_index(op.f('ix_contextofuse_key'), table_name='contextofuse')
    op.drop_table('contextofuse')
    op.drop_index(op.f('ix_adaptuirule_level'), table_name='adaptuirule')
    op.drop_table('adaptuirule')
    # ### end Alembic commands ###
