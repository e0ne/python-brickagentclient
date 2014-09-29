# Copyright 2014 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from brickclient.tests import utils
from brickclient.tests.v1 import fakes

from brickclient.v1 import connector

cs = fakes.FakeClient()


class TestConnector(utils.TestCase):
    def test_get_connector(self):
        c = cs.connector.get()
        cs.assert_called('GET', '/connector')
        self.assertIsInstance(c, connector.Connector)

