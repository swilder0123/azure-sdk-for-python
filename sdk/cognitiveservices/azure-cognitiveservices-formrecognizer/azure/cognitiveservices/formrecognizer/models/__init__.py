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

try:
    from ._models_py3 import AnalyzeOperationResult
    from ._models_py3 import AnalyzeResult
    from ._models_py3 import DataTable
    from ._models_py3 import DataTableCell
    from ._models_py3 import DocumentResult
    from ._models_py3 import ErrorInformation
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import FieldValue
    from ._models_py3 import FormFieldsReport
    from ._models_py3 import FormOperationError
    from ._models_py3 import KeysResult
    from ._models_py3 import KeyValueElement
    from ._models_py3 import KeyValuePair
    from ._models_py3 import Model
    from ._models_py3 import ModelInfo
    from ._models_py3 import ModelsModel
    from ._models_py3 import ModelsSummary
    from ._models_py3 import PageResult
    from ._models_py3 import ReadResult
    from ._models_py3 import SourcePath
    from ._models_py3 import TextLine
    from ._models_py3 import TextWord
    from ._models_py3 import TrainingDocumentInfo
    from ._models_py3 import TrainRequest
    from ._models_py3 import TrainResult
    from ._models_py3 import TrainSourceFilter
except (SyntaxError, ImportError):
    from ._models import AnalyzeOperationResult
    from ._models import AnalyzeResult
    from ._models import DataTable
    from ._models import DataTableCell
    from ._models import DocumentResult
    from ._models import ErrorInformation
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import FieldValue
    from ._models import FormFieldsReport
    from ._models import FormOperationError
    from ._models import KeysResult
    from ._models import KeyValueElement
    from ._models import KeyValuePair
    from ._models import Model
    from ._models import ModelInfo
    from ._models import ModelsModel
    from ._models import ModelsSummary
    from ._models import PageResult
    from ._models import ReadResult
    from ._models import SourcePath
    from ._models import TextLine
    from ._models import TextWord
    from ._models import TrainingDocumentInfo
    from ._models import TrainRequest
    from ._models import TrainResult
    from ._models import TrainSourceFilter
from ._form_recognizer_client_enums import (
    FieldValueType,
    Language,
    LengthUnit,
    ModelStatus,
    OperationStatus,
    TrainStatus,
)

__all__ = [
    'AnalyzeOperationResult',
    'AnalyzeResult',
    'DataTable',
    'DataTableCell',
    'DocumentResult',
    'ErrorInformation',
    'ErrorResponse', 'ErrorResponseException',
    'FieldValue',
    'FormFieldsReport',
    'FormOperationError',
    'KeysResult',
    'KeyValueElement',
    'KeyValuePair',
    'Model',
    'ModelInfo',
    'ModelsModel',
    'ModelsSummary',
    'PageResult',
    'ReadResult',
    'SourcePath',
    'TextLine',
    'TextWord',
    'TrainingDocumentInfo',
    'TrainRequest',
    'TrainResult',
    'TrainSourceFilter',
    'OperationStatus',
    'LengthUnit',
    'Language',
    'FieldValueType',
    'TrainStatus',
    'ModelStatus',
]
