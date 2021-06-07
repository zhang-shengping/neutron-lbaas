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

Revision ID: 8b0c72bb5c98
Revises: d2cd4adbe61f
Create Date: 2020-12-23 23:32:25.425252

"""

# revision identifiers, used by Alembic.
revision = '8b0c72bb5c98'
down_revision = 'd2cd4adbe61f'

from alembic import op
import sqlalchemy as sa

INSERT_CLIENT_IP = "insert_client_ip"

def upgrade():
    op.add_column(
            'lbaas_listeners',
            sa.Column(INSERT_CLIENT_IP, sa.String(16), nullable=True)
    )
