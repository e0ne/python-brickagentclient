# Copyright (c) 2013 OpenStack Foundation
# All Rights Reserved.
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

from brickclient import client
from brickclient.v1 import connector


class Client(object):
    """
    Top-level object to access the OpenStack Volume API.

    Create an instance with your creds::

        >>> client = Client(USERNAME, PASSWORD, PROJECT_ID, AUTH_URL)

    Then call methods on its managers::

        >>> client.volumes.list()
        ...

    """

    def __init__(self, username=None, api_key=None, project_id=None,
                 auth_url='', insecure=False, timeout=None, tenant_id=None,
                 proxy_tenant_id=None, proxy_token=None, region_name=None,
                 endpoint_type='publicURL', extensions=None,
                 service_type='brick', service_name=None,
                 volume_service_name=None, retries=None, http_log_debug=False,
                 cacert=None, auth_system='keystone', auth_plugin=None,
                 session=None, **kwargs):
        # FIXME(comstud): Rename the api_key argument above when we
        # know it's not being used as keyword argument
        password = api_key
        self.connector = connector.LimitsManager(self)

        # extensions

        # Add in any extensions...
        if extensions:
            for extension in extensions:
                if extension.manager_class:
                    setattr(self, extension.name,
                            extension.manager_class(self))

        self.client = client._construct_http_client(
            username=username,
            password=password,
            project_id=project_id,
            auth_url=auth_url,
            insecure=insecure,
            timeout=timeout,
            tenant_id=tenant_id,
            proxy_tenant_id=tenant_id,
            proxy_token=proxy_token,
            region_name=region_name,
            endpoint_type=endpoint_type,
            service_type=service_type,
            service_name=service_name,
            volume_service_name=volume_service_name,
            retries=retries,
            http_log_debug=http_log_debug,
            cacert=cacert,
            auth_system=auth_system,
            auth_plugin=auth_plugin,
            session=session,
            **kwargs)

    def authenticate(self):
        """
        Authenticate against the server.

        Normally this is called automatically when you first access the API,
        but you can call this method to force authentication right now.

        Returns on success; raises :exc:`exceptions.Unauthorized` if the
        credentials are wrong.
        """
        self.client.authenticate()

    def get_volume_api_version_from_endpoint(self):
        return self.client.get_volume_api_version_from_endpoint()
