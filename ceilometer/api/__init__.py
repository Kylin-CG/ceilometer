# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Doug Hellmann <doug.hellmann@dreamhost.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import flask.helpers

from ceilometer.openstack.common import cfg
from ceilometer.openstack.common import jsonutils

# Replace the json module used by flask with the one from
# openstack.common so we can take advantage of the fact that it knows
# how to serialize more complex objects.
flask.helpers.json = jsonutils

# Register options for the service
API_SERVICE_OPTS = [
    cfg.IntOpt('metering_api_port',
               default=9000,
               help='The port for the ceilometer API server',
               ),
    ]
cfg.CONF.register_opts(API_SERVICE_OPTS)
