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

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class BlobOperations(object):
    """BlobOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get(
            self, name, digest, custom_headers=None, raw=False, callback=None, **operation_config):
        """Retrieve the blob from the registry identified by digest.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param digest: Digest of a BLOB
        :type digest: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=True, **operation_config)

        if response.status_code not in [200, 307]:
            raise HttpOperationError(self._deserialize, response)

        header_dict = {}
        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/v2/{name}/blobs/{digest}'}

    def check(
            self, name, digest, custom_headers=None, raw=False, **operation_config):
        """Same as GET, except only the headers are returned.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param digest: Digest of a BLOB
        :type digest: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.check.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 307]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Content-Length': 'long',
                'Docker-Content-Digest': 'str',
                'Location': 'str',
            })
            return client_raw_response
    check.metadata = {'url': '/v2/{name}/blobs/{digest}'}

    def delete(
            self, name, digest, custom_headers=None, raw=False, callback=None, **operation_config):
        """Removes an already uploaded blob.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param digest: Digest of a BLOB
        :type digest: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=True, **operation_config)

        if response.status_code not in [202]:
            raise HttpOperationError(self._deserialize, response)

        header_dict = {}
        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    delete.metadata = {'url': '/v2/{name}/blobs/{digest}'}

    def mount(
            self, name, from_parameter, mount, custom_headers=None, raw=False, **operation_config):
        """Mount a blob identified by the `mount` parameter from another
        repository.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param from_parameter: Name of the source repository.
        :type from_parameter: str
        :param mount: Digest of blob to mount from the source repository.
        :type mount: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.mount.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['from'] = self._serialize.query("from_parameter", from_parameter, 'str')
        query_parameters['mount'] = self._serialize.query("mount", mount, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
                'Docker-Upload-UUID': 'str',
                'Docker-Content-Digest': 'str',
            })
            return client_raw_response
    mount.metadata = {'url': '/v2/{name}/blobs/uploads/'}

    def get_status(
            self, location, custom_headers=None, raw=False, **operation_config):
        """Retrieve status of upload identified by uuid. The primary purpose of
        this endpoint is to resolve the current status of a resumable upload.

        :param location: Link acquired from upload start or previous chunk.
         Note, do not include initial / (must do substring(1) )
        :type location: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.get_status.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Range': 'str',
                'Docker-Upload-UUID': 'str',
            })
            return client_raw_response
    get_status.metadata = {'url': '/{nextBlobUuidLink}'}

    def upload(
            self, value, location, custom_headers=None, raw=False, callback=None, **operation_config):
        """Upload a stream of data without completing the upload.

        :param value: Raw data of blob
        :type value: Generator
        :param location: Link acquired from upload start or previous chunk.
         Note, do not include initial / (must do substring(1) )
        :type location: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.upload.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(value, callback)

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
                'Range': 'str',
                'Docker-Upload-UUID': 'str',
            })
            return client_raw_response
    upload.metadata = {'url': '/{nextBlobUuidLink}'}

    def end_upload(
            self, digest, location, value=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Complete the upload, providing all the data in the body, if necessary.
        A request without a body will just complete the upload with previously
        uploaded content.

        :param digest: Digest of a BLOB
        :type digest: str
        :param location: Link acquired from upload start or previous chunk.
         Note, do not include initial / (must do substring(1) )
        :type location: str
        :param value: Optional raw data of blob
        :type value: Generator
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.end_upload.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['digest'] = self._serialize.query("digest", digest, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(value, callback)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
                'Range': 'str',
                'Docker-Content-Digest': 'str',
            })
            return client_raw_response
    end_upload.metadata = {'url': '/{nextBlobUuidLink}'}

    def cancel_upload(
            self, location, custom_headers=None, raw=False, **operation_config):
        """Cancel outstanding upload processes, releasing associated resources. If
        this is not called, the unfinished uploads will eventually timeout.

        :param location: Link acquired from upload start or previous chunk.
         Note, do not include initial / (must do substring(1) )
        :type location: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.cancel_upload.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    cancel_upload.metadata = {'url': '/{nextBlobUuidLink}'}

    def start_upload(
            self, name, custom_headers=None, raw=False, **operation_config):
        """Initiate a resumable blob upload with an empty request body.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.start_upload.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
                'Range': 'str',
                'Docker-Upload-UUID': 'str',
            })
            return client_raw_response
    start_upload.metadata = {'url': '/v2/{name}/blobs/uploads/'}

    def get_chunk(
            self, name, digest, range, custom_headers=None, raw=False, callback=None, **operation_config):
        """Retrieve the blob from the registry identified by `digest`. This
        endpoint may also support RFC7233 compliant range requests. Support can
        be detected by issuing a HEAD request. If the header `Accept-Range:
        bytes` is returned, range requests can be used to fetch partial
        content.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param digest: Digest of a BLOB
        :type digest: str
        :param range: Format : bytes=<start>-<end>,  HTTP Range header
         specifying blob chunk.
        :type range: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_chunk.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Range'] = self._serialize.header("range", range, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=True, **operation_config)

        if response.status_code not in [206]:
            raise HttpOperationError(self._deserialize, response)

        header_dict = {}
        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get_chunk.metadata = {'url': '/v2/{name}/blobs/{digest}'}

    def check_chunk(
            self, name, digest, range, custom_headers=None, raw=False, **operation_config):
        """Same as GET, except only the headers are returned.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param digest: Digest of a BLOB
        :type digest: str
        :param range: Format : bytes=<start>-<end>,  HTTP Range header
         specifying blob chunk.
        :type range: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.check_chunk.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Range'] = self._serialize.header("range", range, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Content-Length': 'long',
                'Content-Range': 'str',
            })
            return client_raw_response
    check_chunk.metadata = {'url': '/v2/{name}/blobs/{digest}'}