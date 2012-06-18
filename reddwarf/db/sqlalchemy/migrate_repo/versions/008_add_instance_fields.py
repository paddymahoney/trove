# Copyright 2012 OpenStack LLC.
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

from sqlalchemy.schema import Column
from sqlalchemy.schema import ColumnDefault
from sqlalchemy.schema import MetaData

from reddwarf.db.sqlalchemy.migrate_repo.schema import Integer
from reddwarf.db.sqlalchemy.migrate_repo.schema import String
from reddwarf.db.sqlalchemy.migrate_repo.schema import Table


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    # add column:
    instances = Table('instances', meta, autoload=True)
    instances.create_column(Column('tenant_id', String(36), nullable=True))
    instances.create_column(Column('server_status', String(64)))


def downgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    # drop column:
    instances = Table('instances', meta, autoload=True)

    instances.drop_column('tenant_id')
    instances.drop_column('server_status')