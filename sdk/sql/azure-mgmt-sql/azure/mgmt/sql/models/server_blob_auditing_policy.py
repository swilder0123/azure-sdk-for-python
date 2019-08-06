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

from .proxy_resource import ProxyResource


class ServerBlobAuditingPolicy(ProxyResource):
    """A server blob auditing policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param state: Required. Specifies the state of the policy. If state is
     Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required.
     Possible values include: 'Enabled', 'Disabled'
    :type state: str or ~azure.mgmt.sql.models.BlobAuditingPolicyState
    :param storage_endpoint: Specifies the blob storage endpoint (e.g.
     https://MyAccount.blob.core.windows.net). If state is Enabled,
     storageEndpoint is required.
    :type storage_endpoint: str
    :param storage_account_access_key: Specifies the identifier key of the
     auditing storage account. If state is Enabled and storageEndpoint is
     specified, storageAccountAccessKey is required.
    :type storage_account_access_key: str
    :param retention_days: Specifies the number of days to keep in the audit
     logs in the storage account.
    :type retention_days: int
    :param audit_actions_and_groups: Specifies the Actions-Groups and Actions
     to audit.
     The recommended set of action groups to use is the following combination -
     this will audit all the queries and stored procedures executed against the
     database, as well as successful and failed logins:
     BATCH_COMPLETED_GROUP,
     SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,
     FAILED_DATABASE_AUTHENTICATION_GROUP.
     This above combination is also the set that is configured by default when
     enabling auditing from the Azure portal.
     The supported action groups to audit are (note: choose only specific
     groups that cover your auditing needs. Using unnecessary groups could lead
     to very large quantities of audit records):
     APPLICATION_ROLE_CHANGE_PASSWORD_GROUP
     BACKUP_RESTORE_GROUP
     DATABASE_LOGOUT_GROUP
     DATABASE_OBJECT_CHANGE_GROUP
     DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP
     DATABASE_OBJECT_PERMISSION_CHANGE_GROUP
     DATABASE_OPERATION_GROUP
     DATABASE_PERMISSION_CHANGE_GROUP
     DATABASE_PRINCIPAL_CHANGE_GROUP
     DATABASE_PRINCIPAL_IMPERSONATION_GROUP
     DATABASE_ROLE_MEMBER_CHANGE_GROUP
     FAILED_DATABASE_AUTHENTICATION_GROUP
     SCHEMA_OBJECT_ACCESS_GROUP
     SCHEMA_OBJECT_CHANGE_GROUP
     SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP
     SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP
     SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP
     USER_CHANGE_PASSWORD_GROUP
     BATCH_STARTED_GROUP
     BATCH_COMPLETED_GROUP
     These are groups that cover all sql statements and stored procedures
     executed against the database, and should not be used in combination with
     other groups as this will result in duplicate audit logs.
     For more information, see [Database-Level Audit Action
     Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).
     For Database auditing policy, specific Actions can also be specified (note
     that Actions cannot be specified for Server auditing policy). The
     supported actions to audit are:
     SELECT
     UPDATE
     INSERT
     DELETE
     EXECUTE
     RECEIVE
     REFERENCES
     The general form for defining an action to be audited is:
     {action} ON {object} BY {principal}
     Note that <object> in the above format can refer to an object like a
     table, view, or stored procedure, or an entire database or schema. For the
     latter cases, the forms DATABASE::{db_name} and SCHEMA::{schema_name} are
     used, respectively.
     For example:
     SELECT on dbo.myTable by public
     SELECT on DATABASE::myDatabase by public
     SELECT on SCHEMA::mySchema by public
     For more information, see [Database-Level Audit
     Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions)
    :type audit_actions_and_groups: list[str]
    :param storage_account_subscription_id: Specifies the blob storage
     subscription Id.
    :type storage_account_subscription_id: str
    :param is_storage_secondary_key_in_use: Specifies whether
     storageAccountAccessKey value is the storage's secondary key.
    :type is_storage_secondary_key_in_use: bool
    :param is_azure_monitor_target_enabled: Specifies whether audit events are
     sent to Azure Monitor.
     In order to send the events to Azure Monitor, specify 'state' as 'Enabled'
     and 'isAzureMonitorTargetEnabled' as true.
     When using REST API to configure auditing, Diagnostic Settings with
     'SQLSecurityAuditEvents' diagnostic logs category on the database should
     be also created.
     Note that for server level audit you should use the 'master' database as
     {databaseName}.
     Diagnostic Settings URI format:
     PUT
     https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview
     For more information, see [Diagnostic Settings REST
     API](https://go.microsoft.com/fwlink/?linkid=2033207)
     or [Diagnostic Settings
     PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)
    :type is_azure_monitor_target_enabled: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'BlobAuditingPolicyState'},
        'storage_endpoint': {'key': 'properties.storageEndpoint', 'type': 'str'},
        'storage_account_access_key': {'key': 'properties.storageAccountAccessKey', 'type': 'str'},
        'retention_days': {'key': 'properties.retentionDays', 'type': 'int'},
        'audit_actions_and_groups': {'key': 'properties.auditActionsAndGroups', 'type': '[str]'},
        'storage_account_subscription_id': {'key': 'properties.storageAccountSubscriptionId', 'type': 'str'},
        'is_storage_secondary_key_in_use': {'key': 'properties.isStorageSecondaryKeyInUse', 'type': 'bool'},
        'is_azure_monitor_target_enabled': {'key': 'properties.isAzureMonitorTargetEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ServerBlobAuditingPolicy, self).__init__(**kwargs)
        self.state = kwargs.get('state', None)
        self.storage_endpoint = kwargs.get('storage_endpoint', None)
        self.storage_account_access_key = kwargs.get('storage_account_access_key', None)
        self.retention_days = kwargs.get('retention_days', None)
        self.audit_actions_and_groups = kwargs.get('audit_actions_and_groups', None)
        self.storage_account_subscription_id = kwargs.get('storage_account_subscription_id', None)
        self.is_storage_secondary_key_in_use = kwargs.get('is_storage_secondary_key_in_use', None)
        self.is_azure_monitor_target_enabled = kwargs.get('is_azure_monitor_target_enabled', None)
