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

import logging

import fixtures

import brickclient.client
import brickclient.v1.client
from brickclient.tests import utils


class ClientTest(utils.TestCase):

    def test_get_client_class_v1(self):
        output = brickclient.client.get_client_class('1')
        self.assertEqual(brickclient.v1.client.Client, output)

    def test_get_client_class_unknown(self):
        self.assertRaises(brickclient.exceptions.UnsupportedVersion,
                          brickclient.client.get_client_class, '0')

    def test_log_req(self):
        self.logger = self.useFixture(
            fixtures.FakeLogger(
                format="%(message)s",
                level=logging.DEBUG,
                nuke_handlers=True
            )
        )

        kwargs = {}
        kwargs['headers'] = {"X-Foo": "bar"}
        kwargs['data'] = ('{"auth": {"tenantName": "fakeService",'
                          ' "passwordCredentials": {"username": "fakeUser",'
                          ' "password": "fakePassword"}}}')

        cs = brickclient.client.HTTPClient("user", None, None,
                                            "http://127.0.0.1:5000")
        cs.http_log_debug = True
        cs.http_log_req('PUT', kwargs)

        output = self.logger.output.split('\n')

        print("JSBRYANT: output is", output)

        self.assertNotIn("fakePassword", output[1])
        self.assertIn("fakeUser", output[1])
