# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BgpSession(Model):
    """The properties that define a BGP session.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param session_prefix_v4: The IPv4 prefix that contains both ends' IPv4
     addresses.
    :type session_prefix_v4: str
    :param session_prefix_v6: The IPv6 prefix that contains both ends' IPv6
     addresses.
    :type session_prefix_v6: str
    :ivar microsoft_session_ipv4_address: The IPv4 session address on
     Microsoft's end.
    :vartype microsoft_session_ipv4_address: str
    :ivar microsoft_session_ipv6_address: The IPv6 session address on
     Microsoft's end.
    :vartype microsoft_session_ipv6_address: str
    :param peer_session_ipv4_address: The IPv4 session address on peer's end.
    :type peer_session_ipv4_address: str
    :param peer_session_ipv6_address: The IPv6 session address on peer's end.
    :type peer_session_ipv6_address: str
    :ivar session_state_v4: The state of the IPv4 session. Possible values
     include: 'None', 'Idle', 'Connect', 'Active', 'OpenSent', 'OpenConfirm',
     'OpenReceived', 'Established', 'PendingAdd', 'PendingUpdate',
     'PendingRemove'
    :vartype session_state_v4: str or
     ~azure.mgmt.peering.models.SessionStateV4
    :ivar session_state_v6: The state of the IPv6 session. Possible values
     include: 'None', 'Idle', 'Connect', 'Active', 'OpenSent', 'OpenConfirm',
     'OpenReceived', 'Established', 'PendingAdd', 'PendingUpdate',
     'PendingRemove'
    :vartype session_state_v6: str or
     ~azure.mgmt.peering.models.SessionStateV6
    :param max_prefixes_advertised_v4: The maximum number of prefixes
     advertised over the IPv4 session.
    :type max_prefixes_advertised_v4: int
    :param max_prefixes_advertised_v6: The maximum number of prefixes
     advertised over the IPv6 session.
    :type max_prefixes_advertised_v6: int
    :param md5_authentication_key: The MD5 authentication key of the session.
    :type md5_authentication_key: str
    """

    _validation = {
        'microsoft_session_ipv4_address': {'readonly': True},
        'microsoft_session_ipv6_address': {'readonly': True},
        'session_state_v4': {'readonly': True},
        'session_state_v6': {'readonly': True},
    }

    _attribute_map = {
        'session_prefix_v4': {'key': 'sessionPrefixV4', 'type': 'str'},
        'session_prefix_v6': {'key': 'sessionPrefixV6', 'type': 'str'},
        'microsoft_session_ipv4_address': {'key': 'microsoftSessionIPv4Address', 'type': 'str'},
        'microsoft_session_ipv6_address': {'key': 'microsoftSessionIPv6Address', 'type': 'str'},
        'peer_session_ipv4_address': {'key': 'peerSessionIPv4Address', 'type': 'str'},
        'peer_session_ipv6_address': {'key': 'peerSessionIPv6Address', 'type': 'str'},
        'session_state_v4': {'key': 'sessionStateV4', 'type': 'str'},
        'session_state_v6': {'key': 'sessionStateV6', 'type': 'str'},
        'max_prefixes_advertised_v4': {'key': 'maxPrefixesAdvertisedV4', 'type': 'int'},
        'max_prefixes_advertised_v6': {'key': 'maxPrefixesAdvertisedV6', 'type': 'int'},
        'md5_authentication_key': {'key': 'md5AuthenticationKey', 'type': 'str'},
    }

    def __init__(self, *, session_prefix_v4: str=None, session_prefix_v6: str=None, peer_session_ipv4_address: str=None, peer_session_ipv6_address: str=None, max_prefixes_advertised_v4: int=None, max_prefixes_advertised_v6: int=None, md5_authentication_key: str=None, **kwargs) -> None:
        super(BgpSession, self).__init__(**kwargs)
        self.session_prefix_v4 = session_prefix_v4
        self.session_prefix_v6 = session_prefix_v6
        self.microsoft_session_ipv4_address = None
        self.microsoft_session_ipv6_address = None
        self.peer_session_ipv4_address = peer_session_ipv4_address
        self.peer_session_ipv6_address = peer_session_ipv6_address
        self.session_state_v4 = None
        self.session_state_v6 = None
        self.max_prefixes_advertised_v4 = max_prefixes_advertised_v4
        self.max_prefixes_advertised_v6 = max_prefixes_advertised_v6
        self.md5_authentication_key = md5_authentication_key