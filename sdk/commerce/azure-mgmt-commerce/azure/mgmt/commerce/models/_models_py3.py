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


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class InfoField(Model):
    """Key-value pairs of instance details in the legacy format.

    :param project: Identifies the name of the instance provisioned by the
     user.
    :type project: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
    }

    def __init__(self, *, project: str=None, **kwargs) -> None:
        super(InfoField, self).__init__(**kwargs)
        self.project = project


class MeterInfo(Model):
    """Detailed information about the meter.

    :param meter_id: The unique identifier of the resource.
    :type meter_id: str
    :param meter_name: The name of the meter, within the given meter category
    :type meter_name: str
    :param meter_category: The category of the meter, e.g., 'Cloud services',
     'Networking', etc..
    :type meter_category: str
    :param meter_sub_category: The subcategory of the meter, e.g., 'A6 Cloud
     services', 'ExpressRoute (IXP)', etc..
    :type meter_sub_category: str
    :param unit: The unit in which the meter consumption is charged, e.g.,
     'Hours', 'GB', etc.
    :type unit: str
    :param meter_tags: Provides additional meter data. 'Third Party' indicates
     a meter with no discount. Blanks indicate First Party.
    :type meter_tags: list[str]
    :param meter_region: The region in which the Azure service is available.
    :type meter_region: str
    :param meter_rates: The list of key/value pairs for the meter rates, in
     the format 'key':'value' where key = the meter quantity, and value = the
     corresponding price
    :type meter_rates: dict[str, float]
    :param effective_date: Indicates the date from which the meter rate is
     effective.
    :type effective_date: datetime
    :param included_quantity: The resource quantity that is included in the
     offer at no cost. Consumption beyond this quantity will be charged.
    :type included_quantity: float
    """

    _attribute_map = {
        'meter_id': {'key': 'MeterId', 'type': 'str'},
        'meter_name': {'key': 'MeterName', 'type': 'str'},
        'meter_category': {'key': 'MeterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'MeterSubCategory', 'type': 'str'},
        'unit': {'key': 'Unit', 'type': 'str'},
        'meter_tags': {'key': 'MeterTags', 'type': '[str]'},
        'meter_region': {'key': 'MeterRegion', 'type': 'str'},
        'meter_rates': {'key': 'MeterRates', 'type': '{float}'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'included_quantity': {'key': 'IncludedQuantity', 'type': 'float'},
    }

    def __init__(self, *, meter_id: str=None, meter_name: str=None, meter_category: str=None, meter_sub_category: str=None, unit: str=None, meter_tags=None, meter_region: str=None, meter_rates=None, effective_date=None, included_quantity: float=None, **kwargs) -> None:
        super(MeterInfo, self).__init__(**kwargs)
        self.meter_id = meter_id
        self.meter_name = meter_name
        self.meter_category = meter_category
        self.meter_sub_category = meter_sub_category
        self.unit = unit
        self.meter_tags = meter_tags
        self.meter_region = meter_region
        self.meter_rates = meter_rates
        self.effective_date = effective_date
        self.included_quantity = included_quantity


class OfferTermInfo(Model):
    """Describes the offer term.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MonetaryCredit, MonetaryCommitment, RecurringCharge

    All required parameters must be populated in order to send to Azure.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Required. Constant filled by server.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
    }

    _subtype_map = {
        'name': {'Monetary Credit': 'MonetaryCredit', 'Monetary Commitment': 'MonetaryCommitment', 'Recurring Charge': 'RecurringCharge'}
    }

    def __init__(self, *, effective_date=None, **kwargs) -> None:
        super(OfferTermInfo, self).__init__(**kwargs)
        self.effective_date = effective_date
        self.name = None


class MonetaryCommitment(OfferTermInfo):
    """Indicates that a monetary commitment is required for this offer.

    All required parameters must be populated in order to send to Azure.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Required. Constant filled by server.
    :type name: str
    :param tiered_discount: The list of key/value pairs for the tiered meter
     rates, in the format 'key':'value' where key = price, and value = the
     corresponding discount percentage. This field is used only by offer terms
     of type 'Monetary Commitment'.
    :type tiered_discount: dict[str, decimal.Decimal]
    :param excluded_meter_ids: An array of meter ids that are excluded from
     the given offer terms.
    :type excluded_meter_ids: list[str]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
        'tiered_discount': {'key': 'TieredDiscount', 'type': '{decimal}'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
    }

    def __init__(self, *, effective_date=None, tiered_discount=None, excluded_meter_ids=None, **kwargs) -> None:
        super(MonetaryCommitment, self).__init__(effective_date=effective_date, **kwargs)
        self.tiered_discount = tiered_discount
        self.excluded_meter_ids = excluded_meter_ids
        self.name = 'Monetary Commitment'


class MonetaryCredit(OfferTermInfo):
    """Indicates that this is a monetary credit offer.

    All required parameters must be populated in order to send to Azure.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Required. Constant filled by server.
    :type name: str
    :param credit: The amount of credit provided under the terms of the given
     offer level.
    :type credit: decimal.Decimal
    :param excluded_meter_ids: An array of meter ids that are excluded from
     the given offer terms.
    :type excluded_meter_ids: list[str]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
        'credit': {'key': 'Credit', 'type': 'decimal'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
    }

    def __init__(self, *, effective_date=None, credit=None, excluded_meter_ids=None, **kwargs) -> None:
        super(MonetaryCredit, self).__init__(effective_date=effective_date, **kwargs)
        self.credit = credit
        self.excluded_meter_ids = excluded_meter_ids
        self.name = 'Monetary Credit'


class RateCardQueryParameters(Model):
    """Parameters that are used in the odata $filter query parameter for providing
    RateCard information.

    All required parameters must be populated in order to send to Azure.

    :param offer_durable_id: Required. The Offer ID parameter consists of the
     'MS-AZR-' prefix, plus the Offer ID number (e.g., MS-AZR-0026P). See
     https://azure.microsoft.com/en-us/support/legal/offer-details/ for more
     information on the list of available Offer IDs, country/region
     availability, and billing currency.
    :type offer_durable_id: str
    :param currency: Required. The currency in which the rates need to be
     provided.
    :type currency: str
    :param locale: Required. The culture in which the resource metadata needs
     to be localized.
    :type locale: str
    :param region_info: Required. 2 letter ISO code where the offer was
     purchased.
    :type region_info: str
    """

    _validation = {
        'offer_durable_id': {'required': True, 'pattern': r'^MS-AZR-\d{4}P(-\d{4}P)*$'},
        'currency': {'required': True},
        'locale': {'required': True},
        'region_info': {'required': True},
    }

    _attribute_map = {
        'offer_durable_id': {'key': 'OfferDurableId', 'type': 'str'},
        'currency': {'key': 'Currency', 'type': 'str'},
        'locale': {'key': 'Locale', 'type': 'str'},
        'region_info': {'key': 'RegionInfo', 'type': 'str'},
    }

    def __init__(self, *, offer_durable_id: str, currency: str, locale: str, region_info: str, **kwargs) -> None:
        super(RateCardQueryParameters, self).__init__(**kwargs)
        self.offer_durable_id = offer_durable_id
        self.currency = currency
        self.locale = locale
        self.region_info = region_info


class RecurringCharge(OfferTermInfo):
    """Indicates a recurring charge is present for this offer.

    All required parameters must be populated in order to send to Azure.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Required. Constant filled by server.
    :type name: str
    :param recurring_charge: The amount of recurring charge as per the offer
     term.
    :type recurring_charge: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
        'recurring_charge': {'key': 'RecurringCharge', 'type': 'int'},
    }

    def __init__(self, *, effective_date=None, recurring_charge: int=None, **kwargs) -> None:
        super(RecurringCharge, self).__init__(effective_date=effective_date, **kwargs)
        self.recurring_charge = recurring_charge
        self.name = 'Recurring Charge'


class ResourceRateCardInfo(Model):
    """Price and Metadata information for resources.

    :param currency: The currency in which the rates are provided.
    :type currency: str
    :param locale: The culture in which the resource information is localized.
    :type locale: str
    :param is_tax_included: All rates are pretax, so this will always be
     returned as 'false'.
    :type is_tax_included: bool
    :param offer_terms: A list of offer terms.
    :type offer_terms: list[~azure.mgmt.commerce.models.OfferTermInfo]
    :param meters: A list of meters.
    :type meters: list[~azure.mgmt.commerce.models.MeterInfo]
    """

    _attribute_map = {
        'currency': {'key': 'Currency', 'type': 'str'},
        'locale': {'key': 'Locale', 'type': 'str'},
        'is_tax_included': {'key': 'IsTaxIncluded', 'type': 'bool'},
        'offer_terms': {'key': 'OfferTerms', 'type': '[OfferTermInfo]'},
        'meters': {'key': 'Meters', 'type': '[MeterInfo]'},
    }

    def __init__(self, *, currency: str=None, locale: str=None, is_tax_included: bool=None, offer_terms=None, meters=None, **kwargs) -> None:
        super(ResourceRateCardInfo, self).__init__(**kwargs)
        self.currency = currency
        self.locale = locale
        self.is_tax_included = is_tax_included
        self.offer_terms = offer_terms
        self.meters = meters


class UsageAggregation(Model):
    """Describes the usageAggregation.

    :param id: Unique Id for the usage aggregate.
    :type id: str
    :param name: Name of the usage aggregate.
    :type name: str
    :param type: Type of the resource being returned.
    :type type: str
    :param subscription_id: The subscription identifier for the Azure user.
    :type subscription_id: str
    :param meter_id: Unique ID for the resource that was consumed (aka
     ResourceID).
    :type meter_id: str
    :param usage_start_time: UTC start time for the usage bucket to which this
     usage aggregate belongs.
    :type usage_start_time: datetime
    :param usage_end_time: UTC end time for the usage bucket to which this
     usage aggregate belongs.
    :type usage_end_time: datetime
    :param quantity: The amount of the resource consumption that occurred in
     this time frame.
    :type quantity: float
    :param unit: The unit in which the usage for this resource is being
     counted, e.g. Hours, GB.
    :type unit: str
    :param meter_name: Friendly name of the resource being consumed.
    :type meter_name: str
    :param meter_category: Category of the consumed resource.
    :type meter_category: str
    :param meter_sub_category: Sub-category of the consumed resource.
    :type meter_sub_category: str
    :param meter_region: Region of the meterId used for billing purposes
    :type meter_region: str
    :param info_fields: Key-value pairs of instance details (legacy format).
    :type info_fields: ~azure.mgmt.commerce.models.InfoField
    :param instance_data: Key-value pairs of instance details represented as a
     string.
    :type instance_data: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'usage_start_time': {'key': 'properties.usageStartTime', 'type': 'iso-8601'},
        'usage_end_time': {'key': 'properties.usageEndTime', 'type': 'iso-8601'},
        'quantity': {'key': 'properties.quantity', 'type': 'float'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'meter_name': {'key': 'properties.meterName', 'type': 'str'},
        'meter_category': {'key': 'properties.meterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'properties.meterSubCategory', 'type': 'str'},
        'meter_region': {'key': 'properties.meterRegion', 'type': 'str'},
        'info_fields': {'key': 'properties.infoFields', 'type': 'InfoField'},
        'instance_data': {'key': 'properties.instanceData', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, type: str=None, subscription_id: str=None, meter_id: str=None, usage_start_time=None, usage_end_time=None, quantity: float=None, unit: str=None, meter_name: str=None, meter_category: str=None, meter_sub_category: str=None, meter_region: str=None, info_fields=None, instance_data: str=None, **kwargs) -> None:
        super(UsageAggregation, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.subscription_id = subscription_id
        self.meter_id = meter_id
        self.usage_start_time = usage_start_time
        self.usage_end_time = usage_end_time
        self.quantity = quantity
        self.unit = unit
        self.meter_name = meter_name
        self.meter_category = meter_category
        self.meter_sub_category = meter_sub_category
        self.meter_region = meter_region
        self.info_fields = info_fields
        self.instance_data = instance_data
