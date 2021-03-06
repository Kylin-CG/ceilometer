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
"""Tests for ceilometer.compute.instance
"""

import unittest

import mock

from ceilometer.compute import instance
from ceilometer.compute import manager


class FauxInstance(object):

    def __init__(self, **kwds):
        for name, value in kwds.items():
            setattr(self, name, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default):
        try:
            return getattr(self, key)
        except AttributeError:
            return default


class TestLocationMetadata(unittest.TestCase):

    INSTANCE_PROPERTIES = {'display_name': 'display name',
                           'reservation_id': 'reservation id',
                           'architecture': 'x86_64',
                           'availability_zone': 'zone1',
                           'image_ref': 'image ref',
                           'image_ref_url': 'image ref url',
                           'kernel_id': 'kernel id',
                           'os_type': 'linux',
                           'ramdisk_id': 'ramdisk id',
                           'disk_gb': 10,
                           'ephemeral_gb': 7,
                           'memory_mb': 2048,
                           'root_gb': 3,
                           'vcpus': 1,
                           }

    def setUp(self):
        self.manager = manager.AgentManager()
        super(TestLocationMetadata, self).setUp()
        self.instance = FauxInstance(**self.INSTANCE_PROPERTIES)
        self.instance.host = 'made-up-hostname'
        m = mock.MagicMock()
        m.flavorid = 1
        self.instance.instance_type = m

    def test_metadata(self):
        md = instance.get_metadata_from_dbobject(self.instance)
        for name in self.INSTANCE_PROPERTIES.keys():
            actual = md[name]
            print 'checking', name, actual
            expected = self.INSTANCE_PROPERTIES[name]
            assert actual == expected
