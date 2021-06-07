# Copyright 2020 <PUT YOUR NAME/COMPANY HERE>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""empty message

Revision ID: d2cd4adbe61f
Revises: ad2795681549
Create Date: 2020-12-01 22:43:08.461021

"""

# revision identifiers, used by Alembic.
revision = 'd2cd4adbe61f'
down_revision = 'ad2795681549'

from alembic import op
import sqlalchemy as sa

from neutron.db import migration

old_pool_protocols = sa.Enum("HTTP", "HTTPS", "TCP",
                             name="pool_protocolsv2")

new_pool_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "FTP",
                             name="pool_protocolsv2")

def upgrade():
    migration.alter_enum(
        'lbaas_pools',
        'protocol',
        new_pool_protocols,
        nullable=False
    )
