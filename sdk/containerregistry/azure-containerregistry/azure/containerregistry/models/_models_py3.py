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
from msrest.exceptions import HttpOperationError


class AccessToken(Model):
    """AccessToken.

    :param access_token: The access token for performing authenticated
     requests
    :type access_token: str
    """

    _attribute_map = {
        'access_token': {'key': 'access_token', 'type': 'str'},
    }

    def __init__(self, *, access_token: str=None, **kwargs) -> None:
        super(AccessToken, self).__init__(**kwargs)
        self.access_token = access_token


class AcrErrorInfo(Model):
    """Error information.

    :param code: Error code
    :type code: str
    :param message: Error message
    :type message: str
    :param detail: Error details
    :type detail: object
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'detail': {'key': 'detail', 'type': 'object'},
    }

    def __init__(self, *, code: str=None, message: str=None, detail=None, **kwargs) -> None:
        super(AcrErrorInfo, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.detail = detail


class AcrErrors(Model):
    """Acr error response describing why the operation failed.

    :param errors: Array of detailed error
    :type errors: list[~azure.containerregistry.models.AcrErrorInfo]
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[AcrErrorInfo]'},
    }

    def __init__(self, *, errors=None, **kwargs) -> None:
        super(AcrErrors, self).__init__(**kwargs)
        self.errors = errors


class AcrErrorsException(HttpOperationError):
    """Server responsed with exception of type: 'AcrErrors'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(AcrErrorsException, self).__init__(deserialize, response, 'AcrErrors', *args)


class AcrManifests(Model):
    """Manifest attributes.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param manifests_attributes: List of manifests
    :type manifests_attributes:
     list[~azure.containerregistry.models.ManifestAttributesBase]
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'manifests_attributes': {'key': 'manifests', 'type': '[ManifestAttributesBase]'},
    }

    def __init__(self, *, registry: str=None, image_name: str=None, manifests_attributes=None, **kwargs) -> None:
        super(AcrManifests, self).__init__(**kwargs)
        self.registry = registry
        self.image_name = image_name
        self.manifests_attributes = manifests_attributes


class Annotations(Model):
    """Additional information provided through arbitrary metadata.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param created: Date and time on which the image was built (string,
     date-time as defined by https://tools.ietf.org/html/rfc3339#section-5.6)
    :type created: datetime
    :param authors: Contact details of the people or organization responsible
     for the image.
    :type authors: str
    :param url: URL to find more information on the image.
    :type url: str
    :param documentation: URL to get documentation on the image.
    :type documentation: str
    :param source: URL to get source code for building the image.
    :type source: str
    :param version: Version of the packaged software. The version MAY match a
     label or tag in the source code repository, may also be Semantic
     versioning-compatible
    :type version: str
    :param revision: Source control revision identifier for the packaged
     software.
    :type revision: str
    :param vendor: Name of the distributing entity, organization or
     individual.
    :type vendor: str
    :param licenses: License(s) under which contained software is distributed
     as an SPDX License Expression.
    :type licenses: str
    :param name: Name of the reference for a target.
    :type name: str
    :param title: Human-readable title of the image
    :type title: str
    :param description: Human-readable description of the software packaged in
     the image
    :type description: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'created': {'key': 'org\\.opencontainers\\.image\\.created', 'type': 'iso-8601'},
        'authors': {'key': 'org\\.opencontainers\\.image\\.authors', 'type': 'str'},
        'url': {'key': 'org\\.opencontainers\\.image\\.url', 'type': 'str'},
        'documentation': {'key': 'org\\.opencontainers\\.image\\.documentation', 'type': 'str'},
        'source': {'key': 'org\\.opencontainers\\.image\\.source', 'type': 'str'},
        'version': {'key': 'org\\.opencontainers\\.image\\.version', 'type': 'str'},
        'revision': {'key': 'org\\.opencontainers\\.image\\.revision', 'type': 'str'},
        'vendor': {'key': 'org\\.opencontainers\\.image\\.vendor', 'type': 'str'},
        'licenses': {'key': 'org\\.opencontainers\\.image\\.licenses', 'type': 'str'},
        'name': {'key': 'org\\.opencontainers\\.image\\.ref\\.name', 'type': 'str'},
        'title': {'key': 'org\\.opencontainers\\.image\\.title', 'type': 'str'},
        'description': {'key': 'org\\.opencontainers\\.image\\.description', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, created=None, authors: str=None, url: str=None, documentation: str=None, source: str=None, version: str=None, revision: str=None, vendor: str=None, licenses: str=None, name: str=None, title: str=None, description: str=None, **kwargs) -> None:
        super(Annotations, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.created = created
        self.authors = authors
        self.url = url
        self.documentation = documentation
        self.source = source
        self.version = version
        self.revision = revision
        self.vendor = vendor
        self.licenses = licenses
        self.name = name
        self.title = title
        self.description = description


class ChangeableAttributes(Model):
    """ChangeableAttributes.

    :param delete_enabled: Delete enabled
    :type delete_enabled: bool
    :param write_enabled: Write enabled
    :type write_enabled: bool
    :param list_enabled: List enabled
    :type list_enabled: bool
    :param read_enabled: Read enabled
    :type read_enabled: bool
    """

    _attribute_map = {
        'delete_enabled': {'key': 'deleteEnabled', 'type': 'bool'},
        'write_enabled': {'key': 'writeEnabled', 'type': 'bool'},
        'list_enabled': {'key': 'listEnabled', 'type': 'bool'},
        'read_enabled': {'key': 'readEnabled', 'type': 'bool'},
    }

    def __init__(self, *, delete_enabled: bool=None, write_enabled: bool=None, list_enabled: bool=None, read_enabled: bool=None, **kwargs) -> None:
        super(ChangeableAttributes, self).__init__(**kwargs)
        self.delete_enabled = delete_enabled
        self.write_enabled = write_enabled
        self.list_enabled = list_enabled
        self.read_enabled = read_enabled


class DeletedRepository(Model):
    """Deleted repository.

    :param manifests_deleted: SHA of the deleted image
    :type manifests_deleted: list[str]
    :param tags_deleted: Tag of the deleted image
    :type tags_deleted: list[str]
    """

    _attribute_map = {
        'manifests_deleted': {'key': 'manifestsDeleted', 'type': '[str]'},
        'tags_deleted': {'key': 'tagsDeleted', 'type': '[str]'},
    }

    def __init__(self, *, manifests_deleted=None, tags_deleted=None, **kwargs) -> None:
        super(DeletedRepository, self).__init__(**kwargs)
        self.manifests_deleted = manifests_deleted
        self.tags_deleted = tags_deleted


class Descriptor(Model):
    """Docker V2 image layer descriptor including config and layers.

    :param media_type: Layer media type
    :type media_type: str
    :param size: Layer size
    :type size: long
    :param digest: Layer digest
    :type digest: str
    :param urls: Specifies a list of URIs from which this object may be
     downloaded.
    :type urls: list[str]
    :param annotations:
    :type annotations: ~azure.containerregistry.models.Annotations
    """

    _attribute_map = {
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'digest': {'key': 'digest', 'type': 'str'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'annotations': {'key': 'annotations', 'type': 'Annotations'},
    }

    def __init__(self, *, media_type: str=None, size: int=None, digest: str=None, urls=None, annotations=None, **kwargs) -> None:
        super(Descriptor, self).__init__(**kwargs)
        self.media_type = media_type
        self.size = size
        self.digest = digest
        self.urls = urls
        self.annotations = annotations


class FsLayer(Model):
    """Image layer information.

    :param blob_sum: SHA of an image layer
    :type blob_sum: str
    """

    _attribute_map = {
        'blob_sum': {'key': 'blobSum', 'type': 'str'},
    }

    def __init__(self, *, blob_sum: str=None, **kwargs) -> None:
        super(FsLayer, self).__init__(**kwargs)
        self.blob_sum = blob_sum


class History(Model):
    """A list of unstructured historical data for v1 compatibility.

    :param v1_compatibility: The raw v1 compatibility information
    :type v1_compatibility: str
    """

    _attribute_map = {
        'v1_compatibility': {'key': 'v1Compatibility', 'type': 'str'},
    }

    def __init__(self, *, v1_compatibility: str=None, **kwargs) -> None:
        super(History, self).__init__(**kwargs)
        self.v1_compatibility = v1_compatibility


class ImageSignature(Model):
    """Signature of a signed manifest.

    :param header: A JSON web signature
    :type header: ~azure.containerregistry.models.JWK
    :param signature: A signature for the image manifest, signed by a libtrust
     private key
    :type signature: str
    :param protected: The signed protected header
    :type protected: str
    """

    _attribute_map = {
        'header': {'key': 'header', 'type': 'JWK'},
        'signature': {'key': 'signature', 'type': 'str'},
        'protected': {'key': 'protected', 'type': 'str'},
    }

    def __init__(self, *, header=None, signature: str=None, protected: str=None, **kwargs) -> None:
        super(ImageSignature, self).__init__(**kwargs)
        self.header = header
        self.signature = signature
        self.protected = protected


class JWK(Model):
    """A JSON web signature.

    :param jwk:
    :type jwk: ~azure.containerregistry.models.JWKHeader
    :param alg: The algorithm used to sign or encrypt the JWT
    :type alg: str
    """

    _attribute_map = {
        'jwk': {'key': 'jwk', 'type': 'JWKHeader'},
        'alg': {'key': 'alg', 'type': 'str'},
    }

    def __init__(self, *, jwk=None, alg: str=None, **kwargs) -> None:
        super(JWK, self).__init__(**kwargs)
        self.jwk = jwk
        self.alg = alg


class JWKHeader(Model):
    """JSON web key parameter.

    :param crv: crv value
    :type crv: str
    :param kid: kid value
    :type kid: str
    :param kty: kty value
    :type kty: str
    :param x: x value
    :type x: str
    :param y: y value
    :type y: str
    """

    _attribute_map = {
        'crv': {'key': 'crv', 'type': 'str'},
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'x': {'key': 'x', 'type': 'str'},
        'y': {'key': 'y', 'type': 'str'},
    }

    def __init__(self, *, crv: str=None, kid: str=None, kty: str=None, x: str=None, y: str=None, **kwargs) -> None:
        super(JWKHeader, self).__init__(**kwargs)
        self.crv = crv
        self.kid = kid
        self.kty = kty
        self.x = x
        self.y = y


class Manifest(Model):
    """Returns the requested manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
    }

    def __init__(self, *, schema_version: int=None, **kwargs) -> None:
        super(Manifest, self).__init__(**kwargs)
        self.schema_version = schema_version


class ManifestAttributes(Model):
    """Manifest attributes details.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param attributes: Manifest attributes
    :type attributes: ~azure.containerregistry.models.ManifestAttributesBase
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'attributes': {'key': 'manifest', 'type': 'ManifestAttributesBase'},
    }

    def __init__(self, *, registry: str=None, image_name: str=None, attributes=None, **kwargs) -> None:
        super(ManifestAttributes, self).__init__(**kwargs)
        self.registry = registry
        self.image_name = image_name
        self.attributes = attributes


class ManifestAttributesBase(Model):
    """Manifest details.

    :param digest: Manifest
    :type digest: str
    :param image_size: Image size
    :type image_size: long
    :param created_time: Created time
    :type created_time: str
    :param last_update_time: Last update time
    :type last_update_time: str
    :param architecture: CPU architecture
    :type architecture: str
    :param os: Operating system
    :type os: str
    :param media_type: Media type
    :type media_type: str
    :param config_media_type: Config blob media type
    :type config_media_type: str
    :param tags: List of tags
    :type tags: list[str]
    :param changeable_attributes: Changeable attributes
    :type changeable_attributes:
     ~azure.containerregistry.models.ChangeableAttributes
    """

    _attribute_map = {
        'digest': {'key': 'digest', 'type': 'str'},
        'image_size': {'key': 'imageSize', 'type': 'long'},
        'created_time': {'key': 'createdTime', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'str'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'os': {'key': 'os', 'type': 'str'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'config_media_type': {'key': 'configMediaType', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'changeable_attributes': {'key': 'changeableAttributes', 'type': 'ChangeableAttributes'},
    }

    def __init__(self, *, digest: str=None, image_size: int=None, created_time: str=None, last_update_time: str=None, architecture: str=None, os: str=None, media_type: str=None, config_media_type: str=None, tags=None, changeable_attributes=None, **kwargs) -> None:
        super(ManifestAttributesBase, self).__init__(**kwargs)
        self.digest = digest
        self.image_size = image_size
        self.created_time = created_time
        self.last_update_time = last_update_time
        self.architecture = architecture
        self.os = os
        self.media_type = media_type
        self.config_media_type = config_media_type
        self.tags = tags
        self.changeable_attributes = changeable_attributes


class ManifestAttributesManifest(Model):
    """List of manifest attributes.

    :param references: List of manifest attributes details
    :type references:
     list[~azure.containerregistry.models.ManifestAttributesManifestReferences]
    :param quarantine_tag: Quarantine tag name
    :type quarantine_tag: str
    """

    _attribute_map = {
        'references': {'key': 'references', 'type': '[ManifestAttributesManifestReferences]'},
        'quarantine_tag': {'key': 'quarantineTag', 'type': 'str'},
    }

    def __init__(self, *, references=None, quarantine_tag: str=None, **kwargs) -> None:
        super(ManifestAttributesManifest, self).__init__(**kwargs)
        self.references = references
        self.quarantine_tag = quarantine_tag


class ManifestAttributesManifestReferences(Model):
    """Manifest attributes details.

    :param digest: Manifest digest
    :type digest: str
    :param architecture: CPU architecture
    :type architecture: str
    :param os: Operating system
    :type os: str
    """

    _attribute_map = {
        'digest': {'key': 'digest', 'type': 'str'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'os': {'key': 'os', 'type': 'str'},
    }

    def __init__(self, *, digest: str=None, architecture: str=None, os: str=None, **kwargs) -> None:
        super(ManifestAttributesManifestReferences, self).__init__(**kwargs)
        self.digest = digest
        self.architecture = architecture
        self.os = os


class ManifestChangeableAttributes(Model):
    """Changeable attributes.

    :param delete_enabled: Delete enabled
    :type delete_enabled: bool
    :param write_enabled: Write enabled
    :type write_enabled: bool
    :param list_enabled: List enabled
    :type list_enabled: bool
    :param read_enabled: Read enabled
    :type read_enabled: bool
    :param quarantine_state: Quarantine state
    :type quarantine_state: str
    :param quarantine_details: Quarantine details
    :type quarantine_details: str
    """

    _attribute_map = {
        'delete_enabled': {'key': 'deleteEnabled', 'type': 'bool'},
        'write_enabled': {'key': 'writeEnabled', 'type': 'bool'},
        'list_enabled': {'key': 'listEnabled', 'type': 'bool'},
        'read_enabled': {'key': 'readEnabled', 'type': 'bool'},
        'quarantine_state': {'key': 'quarantineState', 'type': 'str'},
        'quarantine_details': {'key': 'quarantineDetails', 'type': 'str'},
    }

    def __init__(self, *, delete_enabled: bool=None, write_enabled: bool=None, list_enabled: bool=None, read_enabled: bool=None, quarantine_state: str=None, quarantine_details: str=None, **kwargs) -> None:
        super(ManifestChangeableAttributes, self).__init__(**kwargs)
        self.delete_enabled = delete_enabled
        self.write_enabled = write_enabled
        self.list_enabled = list_enabled
        self.read_enabled = read_enabled
        self.quarantine_state = quarantine_state
        self.quarantine_details = quarantine_details


class ManifestList(Manifest):
    """Returns the requested Docker multi-arch-manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param media_type: Media type for this Manifest
    :type media_type: str
    :param manifests: List of V2 image layer information
    :type manifests:
     list[~azure.containerregistry.models.ManifestListAttributes]
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'manifests': {'key': 'manifests', 'type': '[ManifestListAttributes]'},
    }

    def __init__(self, *, schema_version: int=None, media_type: str=None, manifests=None, **kwargs) -> None:
        super(ManifestList, self).__init__(schema_version=schema_version, **kwargs)
        self.media_type = media_type
        self.manifests = manifests


class ManifestListAttributes(Model):
    """ManifestListAttributes.

    :param media_type: The MIME type of the referenced object. This will
     generally be application/vnd.docker.image.manifest.v2+json, but it could
     also be application/vnd.docker.image.manifest.v1+json
    :type media_type: str
    :param size: The size in bytes of the object
    :type size: long
    :param digest: The digest of the content, as defined by the Registry V2
     HTTP API Specification
    :type digest: str
    :param platform:
    :type platform: ~azure.containerregistry.models.Platform
    """

    _attribute_map = {
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'digest': {'key': 'digest', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'Platform'},
    }

    def __init__(self, *, media_type: str=None, size: int=None, digest: str=None, platform=None, **kwargs) -> None:
        super(ManifestListAttributes, self).__init__(**kwargs)
        self.media_type = media_type
        self.size = size
        self.digest = digest
        self.platform = platform


class ManifestWrapper(Manifest):
    """Returns the requested manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param media_type: Media type for this Manifest
    :type media_type: str
    :param manifests: (ManifestList, OCIIndex) List of V2 image layer
     information
    :type manifests:
     list[~azure.containerregistry.models.ManifestListAttributes]
    :param config: (V2, OCI) Image config descriptor
    :type config: ~azure.containerregistry.models.Descriptor
    :param layers: (V2, OCI) List of V2 image layer information
    :type layers: list[~azure.containerregistry.models.Descriptor]
    :param annotations: (OCI, OCIIndex) Additional metadata
    :type annotations: ~azure.containerregistry.models.Annotations
    :param architecture: (V1) CPU architecture
    :type architecture: str
    :param name: (V1) Image name
    :type name: str
    :param tag: (V1) Image tag
    :type tag: str
    :param fs_layers: (V1) List of layer information
    :type fs_layers: list[~azure.containerregistry.models.FsLayer]
    :param history: (V1) Image history
    :type history: list[~azure.containerregistry.models.History]
    :param signatures: (V1) Image signature
    :type signatures: list[~azure.containerregistry.models.ImageSignature]
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'manifests': {'key': 'manifests', 'type': '[ManifestListAttributes]'},
        'config': {'key': 'config', 'type': 'Descriptor'},
        'layers': {'key': 'layers', 'type': '[Descriptor]'},
        'annotations': {'key': 'annotations', 'type': 'Annotations'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'fs_layers': {'key': 'fsLayers', 'type': '[FsLayer]'},
        'history': {'key': 'history', 'type': '[History]'},
        'signatures': {'key': 'signatures', 'type': '[ImageSignature]'},
    }

    def __init__(self, *, schema_version: int=None, media_type: str=None, manifests=None, config=None, layers=None, annotations=None, architecture: str=None, name: str=None, tag: str=None, fs_layers=None, history=None, signatures=None, **kwargs) -> None:
        super(ManifestWrapper, self).__init__(schema_version=schema_version, **kwargs)
        self.media_type = media_type
        self.manifests = manifests
        self.config = config
        self.layers = layers
        self.annotations = annotations
        self.architecture = architecture
        self.name = name
        self.tag = tag
        self.fs_layers = fs_layers
        self.history = history
        self.signatures = signatures


class OCIIndex(Manifest):
    """Returns the requested OCI index file.

    :param schema_version: Schema version
    :type schema_version: int
    :param manifests: List of OCI image layer information
    :type manifests:
     list[~azure.containerregistry.models.ManifestListAttributes]
    :param annotations:
    :type annotations: ~azure.containerregistry.models.Annotations
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'manifests': {'key': 'manifests', 'type': '[ManifestListAttributes]'},
        'annotations': {'key': 'annotations', 'type': 'Annotations'},
    }

    def __init__(self, *, schema_version: int=None, manifests=None, annotations=None, **kwargs) -> None:
        super(OCIIndex, self).__init__(schema_version=schema_version, **kwargs)
        self.manifests = manifests
        self.annotations = annotations


class OCIManifest(Manifest):
    """Returns the requested OCI Manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param config: V2 image config descriptor
    :type config: ~azure.containerregistry.models.Descriptor
    :param layers: List of V2 image layer information
    :type layers: list[~azure.containerregistry.models.Descriptor]
    :param annotations:
    :type annotations: ~azure.containerregistry.models.Annotations
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'config': {'key': 'config', 'type': 'Descriptor'},
        'layers': {'key': 'layers', 'type': '[Descriptor]'},
        'annotations': {'key': 'annotations', 'type': 'Annotations'},
    }

    def __init__(self, *, schema_version: int=None, config=None, layers=None, annotations=None, **kwargs) -> None:
        super(OCIManifest, self).__init__(schema_version=schema_version, **kwargs)
        self.config = config
        self.layers = layers
        self.annotations = annotations


class Platform(Model):
    """The platform object describes the platform which the image in the manifest
    runs on. A full list of valid operating system and architecture values are
    listed in the Go language documentation for $GOOS and $GOARCH.

    :param architecture: Specifies the CPU architecture, for example amd64 or
     ppc64le.
    :type architecture: str
    :param os: The os field specifies the operating system, for example linux
     or windows.
    :type os: str
    :param osversion: The optional os.version field specifies the operating
     system version, for example 10.0.10586.
    :type osversion: str
    :param osfeatures: The optional os.features field specifies an array of
     strings, each listing a required OS feature (for example on Windows win32k
    :type osfeatures: list[str]
    :param variant: The optional variant field specifies a variant of the CPU,
     for example armv6l to specify a particular CPU variant of the ARM CPU.
    :type variant: str
    :param features: The optional features field specifies an array of
     strings, each listing a required CPU feature (for example sse4 or aes
    :type features: list[str]
    """

    _attribute_map = {
        'architecture': {'key': 'architecture', 'type': 'str'},
        'os': {'key': 'os', 'type': 'str'},
        'osversion': {'key': 'os\\.version', 'type': 'str'},
        'osfeatures': {'key': 'os\\.features', 'type': '[str]'},
        'variant': {'key': 'variant', 'type': 'str'},
        'features': {'key': 'features', 'type': '[str]'},
    }

    def __init__(self, *, architecture: str=None, os: str=None, osversion: str=None, osfeatures=None, variant: str=None, features=None, **kwargs) -> None:
        super(Platform, self).__init__(**kwargs)
        self.architecture = architecture
        self.os = os
        self.osversion = osversion
        self.osfeatures = osfeatures
        self.variant = variant
        self.features = features


class RefreshToken(Model):
    """RefreshToken.

    :param refresh_token: The refresh token to be used for generating access
     tokens
    :type refresh_token: str
    """

    _attribute_map = {
        'refresh_token': {'key': 'refresh_token', 'type': 'str'},
    }

    def __init__(self, *, refresh_token: str=None, **kwargs) -> None:
        super(RefreshToken, self).__init__(**kwargs)
        self.refresh_token = refresh_token


class Repositories(Model):
    """List of repositories.

    :param names: Repository names
    :type names: list[str]
    """

    _attribute_map = {
        'names': {'key': 'repositories', 'type': '[str]'},
    }

    def __init__(self, *, names=None, **kwargs) -> None:
        super(Repositories, self).__init__(**kwargs)
        self.names = names


class RepositoryAttributes(Model):
    """Repository attributes.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param created_time: Image created time
    :type created_time: str
    :param last_update_time: Image last update time
    :type last_update_time: str
    :param manifest_count: Number of the manifests
    :type manifest_count: int
    :param tag_count: Number of the tags
    :type tag_count: int
    :param changeable_attributes: Changeable attributes
    :type changeable_attributes:
     ~azure.containerregistry.models.ChangeableAttributes
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'str'},
        'manifest_count': {'key': 'manifestCount', 'type': 'int'},
        'tag_count': {'key': 'tagCount', 'type': 'int'},
        'changeable_attributes': {'key': 'changeableAttributes', 'type': 'ChangeableAttributes'},
    }

    def __init__(self, *, registry: str=None, image_name: str=None, created_time: str=None, last_update_time: str=None, manifest_count: int=None, tag_count: int=None, changeable_attributes=None, **kwargs) -> None:
        super(RepositoryAttributes, self).__init__(**kwargs)
        self.registry = registry
        self.image_name = image_name
        self.created_time = created_time
        self.last_update_time = last_update_time
        self.manifest_count = manifest_count
        self.tag_count = tag_count
        self.changeable_attributes = changeable_attributes


class RepositoryTags(Model):
    """Result of the request to list tags of the image.

    :param name: Name of the image
    :type name: str
    :param tags: List of tags
    :type tags: list[str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
    }

    def __init__(self, *, name: str=None, tags=None, **kwargs) -> None:
        super(RepositoryTags, self).__init__(**kwargs)
        self.name = name
        self.tags = tags


class TagAttributes(Model):
    """Tag attributes.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param attributes: List of tag attribute details
    :type attributes: ~azure.containerregistry.models.TagAttributesBase
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'attributes': {'key': 'tag', 'type': 'TagAttributesBase'},
    }

    def __init__(self, *, registry: str=None, image_name: str=None, attributes=None, **kwargs) -> None:
        super(TagAttributes, self).__init__(**kwargs)
        self.registry = registry
        self.image_name = image_name
        self.attributes = attributes


class TagAttributesBase(Model):
    """Tag attribute details.

    :param name: Tag name
    :type name: str
    :param digest: Tag digest
    :type digest: str
    :param created_time: Tag created time
    :type created_time: str
    :param last_update_time: Tag last update time
    :type last_update_time: str
    :param signed: Is signed
    :type signed: bool
    :param changeable_attributes: Changeable attributes
    :type changeable_attributes:
     ~azure.containerregistry.models.ChangeableAttributes
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'digest': {'key': 'digest', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'str'},
        'signed': {'key': 'signed', 'type': 'bool'},
        'changeable_attributes': {'key': 'changeableAttributes', 'type': 'ChangeableAttributes'},
    }

    def __init__(self, *, name: str=None, digest: str=None, created_time: str=None, last_update_time: str=None, signed: bool=None, changeable_attributes=None, **kwargs) -> None:
        super(TagAttributesBase, self).__init__(**kwargs)
        self.name = name
        self.digest = digest
        self.created_time = created_time
        self.last_update_time = last_update_time
        self.signed = signed
        self.changeable_attributes = changeable_attributes


class TagAttributesTag(Model):
    """Tag.

    :param signature_record: SignatureRecord value
    :type signature_record: str
    """

    _attribute_map = {
        'signature_record': {'key': 'signatureRecord', 'type': 'str'},
    }

    def __init__(self, *, signature_record: str=None, **kwargs) -> None:
        super(TagAttributesTag, self).__init__(**kwargs)
        self.signature_record = signature_record


class TagList(Model):
    """List of tag details.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param tags: List of tag attribute details
    :type tags: list[~azure.containerregistry.models.TagAttributesBase]
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[TagAttributesBase]'},
    }

    def __init__(self, *, registry: str=None, image_name: str=None, tags=None, **kwargs) -> None:
        super(TagList, self).__init__(**kwargs)
        self.registry = registry
        self.image_name = image_name
        self.tags = tags


class V1Manifest(Manifest):
    """Returns the requested V1 manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param architecture: CPU architecture
    :type architecture: str
    :param name: Image name
    :type name: str
    :param tag: Image tag
    :type tag: str
    :param fs_layers: List of layer information
    :type fs_layers: list[~azure.containerregistry.models.FsLayer]
    :param history: Image history
    :type history: list[~azure.containerregistry.models.History]
    :param signatures: Image signature
    :type signatures: list[~azure.containerregistry.models.ImageSignature]
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'fs_layers': {'key': 'fsLayers', 'type': '[FsLayer]'},
        'history': {'key': 'history', 'type': '[History]'},
        'signatures': {'key': 'signatures', 'type': '[ImageSignature]'},
    }

    def __init__(self, *, schema_version: int=None, architecture: str=None, name: str=None, tag: str=None, fs_layers=None, history=None, signatures=None, **kwargs) -> None:
        super(V1Manifest, self).__init__(schema_version=schema_version, **kwargs)
        self.architecture = architecture
        self.name = name
        self.tag = tag
        self.fs_layers = fs_layers
        self.history = history
        self.signatures = signatures


class V2Manifest(Manifest):
    """Returns the requested Docker V2 Manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param media_type: Media type for this Manifest
    :type media_type: str
    :param config: V2 image config descriptor
    :type config: ~azure.containerregistry.models.Descriptor
    :param layers: List of V2 image layer information
    :type layers: list[~azure.containerregistry.models.Descriptor]
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'config': {'key': 'config', 'type': 'Descriptor'},
        'layers': {'key': 'layers', 'type': '[Descriptor]'},
    }

    def __init__(self, *, schema_version: int=None, media_type: str=None, config=None, layers=None, **kwargs) -> None:
        super(V2Manifest, self).__init__(schema_version=schema_version, **kwargs)
        self.media_type = media_type
        self.config = config
        self.layers = layers