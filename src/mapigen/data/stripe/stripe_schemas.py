import msgspec
from typing import Optional, List, Any, Dict

class GetAccount_params(msgspec.Struct):
    expand: Optional[List[str]] = None

class PostAccountLinks_params(msgspec.Struct):
    account: Optional[Any] = None
    collect: Optional[Any] = None
    collection_options: Optional[Any] = None
    expand: Optional[Any] = None
    refresh_url: Optional[Any] = None
    return_url: Optional[Any] = None
    type: Optional[Any] = None

class PostAccountSessions_params(msgspec.Struct):
    account: Optional[Any] = None
    components: Optional[Any] = None
    expand: Optional[Any] = None

class GetAccounts_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostAccounts_params(msgspec.Struct):
    account_token: Optional[Any] = None
    bank_account: Optional[Any] = None
    business_profile: Optional[Any] = None
    business_type: Optional[Any] = None
    capabilities: Optional[Any] = None
    company: Optional[Any] = None
    controller: Optional[Any] = None
    country: Optional[Any] = None
    default_currency: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    external_account: Optional[Any] = None
    groups: Optional[Any] = None
    individual: Optional[Any] = None
    metadata: Optional[Any] = None
    settings: Optional[Any] = None
    tos_acceptance: Optional[Any] = None
    type: Optional[Any] = None

class DeleteAccountsAccount_params(msgspec.Struct):
    account: Optional[str] = None

class GetAccountsAccount_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None

class PostAccountsAccount_params(msgspec.Struct):
    account: Optional[str] = None
    account_token: Optional[Any] = None
    business_profile: Optional[Any] = None
    business_type: Optional[Any] = None
    capabilities: Optional[Any] = None
    company: Optional[Any] = None
    default_currency: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    external_account: Optional[Any] = None
    groups: Optional[Any] = None
    individual: Optional[Any] = None
    metadata: Optional[Any] = None
    settings: Optional[Any] = None
    tos_acceptance: Optional[Any] = None

class PostAccountsAccountBankAccounts_params(msgspec.Struct):
    account: Optional[str] = None
    bank_account: Optional[Any] = None
    default_for_currency: Optional[Any] = None
    expand: Optional[Any] = None
    external_account: Optional[Any] = None
    metadata: Optional[Any] = None

class DeleteAccountsAccountBankAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    id: Optional[str] = None

class GetAccountsAccountBankAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostAccountsAccountBankAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    account_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    default_for_currency: Optional[Any] = None
    documents: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetAccountsAccountCapabilities_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None

class GetAccountsAccountCapabilitiesCapability_params(msgspec.Struct):
    account: Optional[str] = None
    capability: Optional[str] = None
    expand: Optional[List[str]] = None

class PostAccountsAccountCapabilitiesCapability_params(msgspec.Struct):
    account: Optional[str] = None
    capability: Optional[str] = None
    expand: Optional[Any] = None
    requested: Optional[Any] = None

class GetAccountsAccountExternalAccounts_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    object: Optional[str] = None
    starting_after: Optional[str] = None

class PostAccountsAccountExternalAccounts_params(msgspec.Struct):
    account: Optional[str] = None
    bank_account: Optional[Any] = None
    default_for_currency: Optional[Any] = None
    expand: Optional[Any] = None
    external_account: Optional[Any] = None
    metadata: Optional[Any] = None

class DeleteAccountsAccountExternalAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    id: Optional[str] = None

class GetAccountsAccountExternalAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostAccountsAccountExternalAccountsId_params(msgspec.Struct):
    account: Optional[str] = None
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    account_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    default_for_currency: Optional[Any] = None
    documents: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class PostAccountsAccountLoginLinks_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None

class GetAccountsAccountPeople_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    relationship: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None

class PostAccountsAccountPeople_params(msgspec.Struct):
    account: Optional[str] = None
    additional_tos_acceptances: Optional[Any] = None
    address: Optional[Any] = None
    address_kana: Optional[Any] = None
    address_kanji: Optional[Any] = None
    dob: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    first_name: Optional[Any] = None
    first_name_kana: Optional[Any] = None
    first_name_kanji: Optional[Any] = None
    full_name_aliases: Optional[Any] = None
    gender: Optional[Any] = None
    id_number: Optional[Any] = None
    id_number_secondary: Optional[Any] = None
    last_name: Optional[Any] = None
    last_name_kana: Optional[Any] = None
    last_name_kanji: Optional[Any] = None
    maiden_name: Optional[Any] = None
    metadata: Optional[Any] = None
    nationality: Optional[Any] = None
    person_token: Optional[Any] = None
    phone: Optional[Any] = None
    political_exposure: Optional[Any] = None
    registered_address: Optional[Any] = None
    relationship: Optional[Any] = None
    ssn_last_4: Optional[Any] = None
    us_cfpb_data: Optional[Any] = None
    verification: Optional[Any] = None

class DeleteAccountsAccountPeoplePerson_params(msgspec.Struct):
    account: Optional[str] = None
    person: Optional[str] = None

class GetAccountsAccountPeoplePerson_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None
    person: Optional[str] = None

class PostAccountsAccountPeoplePerson_params(msgspec.Struct):
    account: Optional[str] = None
    person: Optional[str] = None
    additional_tos_acceptances: Optional[Any] = None
    address: Optional[Any] = None
    address_kana: Optional[Any] = None
    address_kanji: Optional[Any] = None
    dob: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    first_name: Optional[Any] = None
    first_name_kana: Optional[Any] = None
    first_name_kanji: Optional[Any] = None
    full_name_aliases: Optional[Any] = None
    gender: Optional[Any] = None
    id_number: Optional[Any] = None
    id_number_secondary: Optional[Any] = None
    last_name: Optional[Any] = None
    last_name_kana: Optional[Any] = None
    last_name_kanji: Optional[Any] = None
    maiden_name: Optional[Any] = None
    metadata: Optional[Any] = None
    nationality: Optional[Any] = None
    person_token: Optional[Any] = None
    phone: Optional[Any] = None
    political_exposure: Optional[Any] = None
    registered_address: Optional[Any] = None
    relationship: Optional[Any] = None
    ssn_last_4: Optional[Any] = None
    us_cfpb_data: Optional[Any] = None
    verification: Optional[Any] = None

class GetAccountsAccountPersons_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    relationship: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None

class PostAccountsAccountPersons_params(msgspec.Struct):
    account: Optional[str] = None
    additional_tos_acceptances: Optional[Any] = None
    address: Optional[Any] = None
    address_kana: Optional[Any] = None
    address_kanji: Optional[Any] = None
    dob: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    first_name: Optional[Any] = None
    first_name_kana: Optional[Any] = None
    first_name_kanji: Optional[Any] = None
    full_name_aliases: Optional[Any] = None
    gender: Optional[Any] = None
    id_number: Optional[Any] = None
    id_number_secondary: Optional[Any] = None
    last_name: Optional[Any] = None
    last_name_kana: Optional[Any] = None
    last_name_kanji: Optional[Any] = None
    maiden_name: Optional[Any] = None
    metadata: Optional[Any] = None
    nationality: Optional[Any] = None
    person_token: Optional[Any] = None
    phone: Optional[Any] = None
    political_exposure: Optional[Any] = None
    registered_address: Optional[Any] = None
    relationship: Optional[Any] = None
    ssn_last_4: Optional[Any] = None
    us_cfpb_data: Optional[Any] = None
    verification: Optional[Any] = None

class DeleteAccountsAccountPersonsPerson_params(msgspec.Struct):
    account: Optional[str] = None
    person: Optional[str] = None

class GetAccountsAccountPersonsPerson_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None
    person: Optional[str] = None

class PostAccountsAccountPersonsPerson_params(msgspec.Struct):
    account: Optional[str] = None
    person: Optional[str] = None
    additional_tos_acceptances: Optional[Any] = None
    address: Optional[Any] = None
    address_kana: Optional[Any] = None
    address_kanji: Optional[Any] = None
    dob: Optional[Any] = None
    documents: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    first_name: Optional[Any] = None
    first_name_kana: Optional[Any] = None
    first_name_kanji: Optional[Any] = None
    full_name_aliases: Optional[Any] = None
    gender: Optional[Any] = None
    id_number: Optional[Any] = None
    id_number_secondary: Optional[Any] = None
    last_name: Optional[Any] = None
    last_name_kana: Optional[Any] = None
    last_name_kanji: Optional[Any] = None
    maiden_name: Optional[Any] = None
    metadata: Optional[Any] = None
    nationality: Optional[Any] = None
    person_token: Optional[Any] = None
    phone: Optional[Any] = None
    political_exposure: Optional[Any] = None
    registered_address: Optional[Any] = None
    relationship: Optional[Any] = None
    ssn_last_4: Optional[Any] = None
    us_cfpb_data: Optional[Any] = None
    verification: Optional[Any] = None

class PostAccountsAccountReject_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None
    reason: Optional[Any] = None

class GetApplePayDomains_params(msgspec.Struct):
    domain_name: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostApplePayDomains_params(msgspec.Struct):
    domain_name: Optional[Any] = None
    expand: Optional[Any] = None

class DeleteApplePayDomainsDomain_params(msgspec.Struct):
    domain: Optional[str] = None

class GetApplePayDomainsDomain_params(msgspec.Struct):
    domain: Optional[str] = None
    expand: Optional[List[str]] = None

class GetApplicationFees_params(msgspec.Struct):
    charge: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetApplicationFeesFeeRefundsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    fee: Optional[str] = None
    id: Optional[str] = None

class PostApplicationFeesFeeRefundsId_params(msgspec.Struct):
    fee: Optional[str] = None
    id: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetApplicationFeesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostApplicationFeesIdRefund_params(msgspec.Struct):
    id: Optional[str] = None
    amount: Optional[Any] = None
    directive: Optional[Any] = None
    expand: Optional[Any] = None

class GetApplicationFeesIdRefunds_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostApplicationFeesIdRefunds_params(msgspec.Struct):
    id: Optional[str] = None
    amount: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetAppsSecrets_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    scope: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None

class PostAppsSecrets_params(msgspec.Struct):
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    name: Optional[Any] = None
    payload: Optional[Any] = None
    scope: Optional[Any] = None

class PostAppsSecretsDelete_params(msgspec.Struct):
    expand: Optional[Any] = None
    name: Optional[Any] = None
    scope: Optional[Any] = None

class GetAppsSecretsFind_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    name: Optional[str] = None
    scope: Optional[Dict[str, Any]] = None

class GetBalance_params(msgspec.Struct):
    expand: Optional[List[str]] = None

class GetBalanceHistory_params(msgspec.Struct):
    created: Optional[Any] = None
    currency: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payout: Optional[str] = None
    source: Optional[str] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class GetBalanceHistoryId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetBalanceTransactions_params(msgspec.Struct):
    created: Optional[Any] = None
    currency: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payout: Optional[str] = None
    source: Optional[str] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class GetBalanceTransactionsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetBillingAlerts_params(msgspec.Struct):
    alert_type: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    meter: Optional[str] = None
    starting_after: Optional[str] = None

class PostBillingAlerts_params(msgspec.Struct):
    alert_type: Optional[Any] = None
    expand: Optional[Any] = None
    title: Optional[Any] = None
    usage_threshold: Optional[Any] = None

class GetBillingAlertsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostBillingAlertsIdActivate_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostBillingAlertsIdArchive_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostBillingAlertsIdDeactivate_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetBillingCreditBalanceSummary_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    filter: Optional[Dict[str, Any]] = None

class GetBillingCreditBalanceTransactions_params(msgspec.Struct):
    credit_grant: Optional[str] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetBillingCreditBalanceTransactionsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetBillingCreditGrants_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostBillingCreditGrants_params(msgspec.Struct):
    amount: Optional[Any] = None
    applicability_config: Optional[Any] = None
    category: Optional[Any] = None
    customer: Optional[Any] = None
    effective_at: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    priority: Optional[Any] = None

class GetBillingCreditGrantsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostBillingCreditGrantsId_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    metadata: Optional[Any] = None

class PostBillingCreditGrantsIdExpire_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostBillingCreditGrantsIdVoid_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostBillingMeterEventAdjustments_params(msgspec.Struct):
    cancel: Optional[Any] = None
    event_name: Optional[Any] = None
    expand: Optional[Any] = None
    type: Optional[Any] = None

class PostBillingMeterEvents_params(msgspec.Struct):
    event_name: Optional[Any] = None
    expand: Optional[Any] = None
    identifier: Optional[Any] = None
    payload: Optional[Any] = None
    timestamp: Optional[Any] = None

class GetBillingMeters_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostBillingMeters_params(msgspec.Struct):
    customer_mapping: Optional[Any] = None
    default_aggregation: Optional[Any] = None
    display_name: Optional[Any] = None
    event_name: Optional[Any] = None
    event_time_window: Optional[Any] = None
    expand: Optional[Any] = None
    value_settings: Optional[Any] = None

class GetBillingMetersId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostBillingMetersId_params(msgspec.Struct):
    id: Optional[str] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None

class PostBillingMetersIdDeactivate_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetBillingMetersIdEventSummaries_params(msgspec.Struct):
    customer: Optional[str] = None
    end_time: Optional[int] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None
    limit: Optional[int] = None
    start_time: Optional[int] = None
    starting_after: Optional[str] = None
    value_grouping_window: Optional[str] = None

class PostBillingMetersIdReactivate_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetBillingPortalConfigurations_params(msgspec.Struct):
    active: Optional[bool] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    is_default: Optional[bool] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostBillingPortalConfigurations_params(msgspec.Struct):
    business_profile: Optional[Any] = None
    default_return_url: Optional[Any] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None
    login_page: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetBillingPortalConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    expand: Optional[List[str]] = None

class PostBillingPortalConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    active: Optional[Any] = None
    business_profile: Optional[Any] = None
    default_return_url: Optional[Any] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None
    login_page: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class PostBillingPortalSessions_params(msgspec.Struct):
    configuration: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    flow_data: Optional[Any] = None
    locale: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    return_url: Optional[Any] = None

class GetCharges_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_intent: Optional[str] = None
    starting_after: Optional[str] = None
    transfer_group: Optional[str] = None

class PostCharges_params(msgspec.Struct):
    amount: Optional[Any] = None
    application_fee: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    capture: Optional[Any] = None
    card: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    destination: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    radar_options: Optional[Any] = None
    receipt_email: Optional[Any] = None
    shipping: Optional[Any] = None
    source: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    statement_descriptor_suffix: Optional[Any] = None
    transfer_data: Optional[Any] = None
    transfer_group: Optional[Any] = None

class GetChargesSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class GetChargesCharge_params(msgspec.Struct):
    charge: Optional[str] = None
    expand: Optional[List[str]] = None

class PostChargesCharge_params(msgspec.Struct):
    charge: Optional[str] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    fraud_details: Optional[Any] = None
    metadata: Optional[Any] = None
    receipt_email: Optional[Any] = None
    shipping: Optional[Any] = None
    transfer_group: Optional[Any] = None

class PostChargesChargeCapture_params(msgspec.Struct):
    charge: Optional[str] = None
    amount: Optional[Any] = None
    application_fee: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    expand: Optional[Any] = None
    receipt_email: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    statement_descriptor_suffix: Optional[Any] = None
    transfer_data: Optional[Any] = None
    transfer_group: Optional[Any] = None

class GetChargesChargeDispute_params(msgspec.Struct):
    charge: Optional[str] = None
    expand: Optional[List[str]] = None

class PostChargesChargeDispute_params(msgspec.Struct):
    charge: Optional[str] = None
    evidence: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    submit: Optional[Any] = None

class PostChargesChargeDisputeClose_params(msgspec.Struct):
    charge: Optional[str] = None
    expand: Optional[Any] = None

class PostChargesChargeRefund_params(msgspec.Struct):
    charge: Optional[str] = None
    amount: Optional[Any] = None
    expand: Optional[Any] = None
    instructions_email: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_intent: Optional[Any] = None
    reason: Optional[Any] = None
    refund_application_fee: Optional[Any] = None
    reverse_transfer: Optional[Any] = None

class GetChargesChargeRefunds_params(msgspec.Struct):
    charge: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostChargesChargeRefunds_params(msgspec.Struct):
    charge: Optional[str] = None
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    instructions_email: Optional[Any] = None
    metadata: Optional[Any] = None
    origin: Optional[Any] = None
    payment_intent: Optional[Any] = None
    reason: Optional[Any] = None
    refund_application_fee: Optional[Any] = None
    reverse_transfer: Optional[Any] = None

class GetChargesChargeRefundsRefund_params(msgspec.Struct):
    charge: Optional[str] = None
    expand: Optional[List[str]] = None
    refund: Optional[str] = None

class PostChargesChargeRefundsRefund_params(msgspec.Struct):
    charge: Optional[str] = None
    refund: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetCheckoutSessions_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    customer_details: Optional[Dict[str, Any]] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_intent: Optional[str] = None
    payment_link: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    subscription: Optional[str] = None

class PostCheckoutSessions_params(msgspec.Struct):
    adaptive_pricing: Optional[Any] = None
    after_expiration: Optional[Any] = None
    allow_promotion_codes: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    billing_address_collection: Optional[Any] = None
    cancel_url: Optional[Any] = None
    client_reference_id: Optional[Any] = None
    consent_collection: Optional[Any] = None
    currency: Optional[Any] = None
    custom_fields: Optional[Any] = None
    custom_text: Optional[Any] = None
    customer: Optional[Any] = None
    customer_creation: Optional[Any] = None
    customer_email: Optional[Any] = None
    customer_update: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    invoice_creation: Optional[Any] = None
    line_items: Optional[Any] = None
    locale: Optional[Any] = None
    metadata: Optional[Any] = None
    mode: Optional[Any] = None
    optional_items: Optional[Any] = None
    origin_context: Optional[Any] = None
    payment_intent_data: Optional[Any] = None
    payment_method_collection: Optional[Any] = None
    payment_method_configuration: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    permissions: Optional[Any] = None
    phone_number_collection: Optional[Any] = None
    redirect_on_completion: Optional[Any] = None
    return_url: Optional[Any] = None
    saved_payment_method_options: Optional[Any] = None
    setup_intent_data: Optional[Any] = None
    shipping_address_collection: Optional[Any] = None
    shipping_options: Optional[Any] = None
    submit_type: Optional[Any] = None
    subscription_data: Optional[Any] = None
    success_url: Optional[Any] = None
    tax_id_collection: Optional[Any] = None
    ui_mode: Optional[Any] = None
    wallet_options: Optional[Any] = None

class GetCheckoutSessionsSession_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    session: Optional[str] = None

class PostCheckoutSessionsSession_params(msgspec.Struct):
    session: Optional[str] = None
    collected_information: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    shipping_options: Optional[Any] = None

class PostCheckoutSessionsSessionExpire_params(msgspec.Struct):
    session: Optional[str] = None
    expand: Optional[Any] = None

class GetCheckoutSessionsSessionLineItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    session: Optional[str] = None
    starting_after: Optional[str] = None

class GetClimateOrders_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostClimateOrders_params(msgspec.Struct):
    amount: Optional[Any] = None
    beneficiary: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    metric_tons: Optional[Any] = None
    product: Optional[Any] = None

class GetClimateOrdersOrder_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    order: Optional[str] = None

class PostClimateOrdersOrder_params(msgspec.Struct):
    order: Optional[str] = None
    beneficiary: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostClimateOrdersOrderCancel_params(msgspec.Struct):
    order: Optional[str] = None
    expand: Optional[Any] = None

class GetClimateProducts_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetClimateProductsProduct_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    product: Optional[str] = None

class GetClimateSuppliers_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetClimateSuppliersSupplier_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    supplier: Optional[str] = None

class GetConfirmationTokensConfirmationToken_params(msgspec.Struct):
    confirmation_token: Optional[str] = None
    expand: Optional[List[str]] = None

class GetCountrySpecs_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetCountrySpecsCountry_params(msgspec.Struct):
    country: Optional[str] = None
    expand: Optional[List[str]] = None

class GetCoupons_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCoupons_params(msgspec.Struct):
    amount_off: Optional[Any] = None
    applies_to: Optional[Any] = None
    currency: Optional[Any] = None
    currency_options: Optional[Any] = None
    duration: Optional[Any] = None
    duration_in_months: Optional[Any] = None
    expand: Optional[Any] = None
    id: Optional[Any] = None
    max_redemptions: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    percent_off: Optional[Any] = None
    redeem_by: Optional[Any] = None

class DeleteCouponsCoupon_params(msgspec.Struct):
    coupon: Optional[str] = None

class GetCouponsCoupon_params(msgspec.Struct):
    coupon: Optional[str] = None
    expand: Optional[List[str]] = None

class PostCouponsCoupon_params(msgspec.Struct):
    coupon: Optional[str] = None
    currency_options: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetCreditNotes_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCreditNotes_params(msgspec.Struct):
    amount: Optional[Any] = None
    credit_amount: Optional[Any] = None
    effective_at: Optional[Any] = None
    email_type: Optional[Any] = None
    expand: Optional[Any] = None
    invoice: Optional[Any] = None
    lines: Optional[Any] = None
    memo: Optional[Any] = None
    metadata: Optional[Any] = None
    out_of_band_amount: Optional[Any] = None
    reason: Optional[Any] = None
    refund_amount: Optional[Any] = None
    refunds: Optional[Any] = None
    shipping_cost: Optional[Any] = None

class GetCreditNotesPreview_params(msgspec.Struct):
    amount: Optional[int] = None
    credit_amount: Optional[int] = None
    effective_at: Optional[int] = None
    email_type: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    lines: Optional[List[Dict[str, Any]]] = None
    memo: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    out_of_band_amount: Optional[int] = None
    reason: Optional[str] = None
    refund_amount: Optional[int] = None
    refunds: Optional[List[Dict[str, Any]]] = None
    shipping_cost: Optional[Dict[str, Any]] = None

class GetCreditNotesPreviewLines_params(msgspec.Struct):
    amount: Optional[int] = None
    credit_amount: Optional[int] = None
    effective_at: Optional[int] = None
    email_type: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    limit: Optional[int] = None
    lines: Optional[List[Dict[str, Any]]] = None
    memo: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    out_of_band_amount: Optional[int] = None
    reason: Optional[str] = None
    refund_amount: Optional[int] = None
    refunds: Optional[List[Dict[str, Any]]] = None
    shipping_cost: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None

class GetCreditNotesCreditNoteLines_params(msgspec.Struct):
    credit_note: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetCreditNotesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostCreditNotesId_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    memo: Optional[Any] = None
    metadata: Optional[Any] = None

class PostCreditNotesIdVoid_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostCustomerSessions_params(msgspec.Struct):
    components: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None

class GetCustomers_params(msgspec.Struct):
    created: Optional[Any] = None
    email: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    test_clock: Optional[str] = None

class PostCustomers_params(msgspec.Struct):
    address: Optional[Any] = None
    balance: Optional[Any] = None
    cash_balance: Optional[Any] = None
    description: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_prefix: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    next_invoice_sequence: Optional[Any] = None
    payment_method: Optional[Any] = None
    phone: Optional[Any] = None
    preferred_locales: Optional[Any] = None
    shipping: Optional[Any] = None
    source: Optional[Any] = None
    tax: Optional[Any] = None
    tax_exempt: Optional[Any] = None
    tax_id_data: Optional[Any] = None
    test_clock: Optional[Any] = None

class GetCustomersSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class DeleteCustomersCustomer_params(msgspec.Struct):
    customer: Optional[str] = None

class GetCustomersCustomer_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None

class PostCustomersCustomer_params(msgspec.Struct):
    customer: Optional[str] = None
    address: Optional[Any] = None
    balance: Optional[Any] = None
    bank_account: Optional[Any] = None
    card: Optional[Any] = None
    cash_balance: Optional[Any] = None
    default_alipay_account: Optional[Any] = None
    default_bank_account: Optional[Any] = None
    default_card: Optional[Any] = None
    default_source: Optional[Any] = None
    description: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_prefix: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    next_invoice_sequence: Optional[Any] = None
    phone: Optional[Any] = None
    preferred_locales: Optional[Any] = None
    shipping: Optional[Any] = None
    source: Optional[Any] = None
    tax: Optional[Any] = None
    tax_exempt: Optional[Any] = None

class GetCustomersCustomerBalanceTransactions_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerBalanceTransactions_params(msgspec.Struct):
    customer: Optional[str] = None
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetCustomersCustomerBalanceTransactionsTransaction_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    transaction: Optional[str] = None

class PostCustomersCustomerBalanceTransactionsTransaction_params(msgspec.Struct):
    customer: Optional[str] = None
    transaction: Optional[str] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetCustomersCustomerBankAccounts_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerBankAccounts_params(msgspec.Struct):
    customer: Optional[str] = None
    alipay_account: Optional[Any] = None
    bank_account: Optional[Any] = None
    card: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    source: Optional[Any] = None

class DeleteCustomersCustomerBankAccountsId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetCustomersCustomerBankAccountsId_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostCustomersCustomerBankAccountsId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    owner: Optional[Any] = None

class PostCustomersCustomerBankAccountsIdVerify_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    amounts: Optional[Any] = None
    expand: Optional[Any] = None

class GetCustomersCustomerCards_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerCards_params(msgspec.Struct):
    customer: Optional[str] = None
    alipay_account: Optional[Any] = None
    bank_account: Optional[Any] = None
    card: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    source: Optional[Any] = None

class DeleteCustomersCustomerCardsId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetCustomersCustomerCardsId_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostCustomersCustomerCardsId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    owner: Optional[Any] = None

class GetCustomersCustomerCashBalance_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None

class PostCustomersCustomerCashBalance_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[Any] = None
    settings: Optional[Any] = None

class GetCustomersCustomerCashBalanceTransactions_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetCustomersCustomerCashBalanceTransactionsTransaction_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    transaction: Optional[str] = None

class DeleteCustomersCustomerDiscount_params(msgspec.Struct):
    customer: Optional[str] = None

class GetCustomersCustomerDiscount_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None

class PostCustomersCustomerFundingInstructions_params(msgspec.Struct):
    customer: Optional[str] = None
    bank_transfer: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    funding_type: Optional[Any] = None

class GetCustomersCustomerPaymentMethods_params(msgspec.Struct):
    allow_redisplay: Optional[str] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class GetCustomersCustomerPaymentMethodsPaymentMethod_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    payment_method: Optional[str] = None

class GetCustomersCustomerSources_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    object: Optional[str] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerSources_params(msgspec.Struct):
    customer: Optional[str] = None
    alipay_account: Optional[Any] = None
    bank_account: Optional[Any] = None
    card: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    source: Optional[Any] = None

class DeleteCustomersCustomerSourcesId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetCustomersCustomerSourcesId_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostCustomersCustomerSourcesId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    owner: Optional[Any] = None

class PostCustomersCustomerSourcesIdVerify_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None
    amounts: Optional[Any] = None
    expand: Optional[Any] = None

class GetCustomersCustomerSubscriptions_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerSubscriptions_params(msgspec.Struct):
    customer: Optional[str] = None
    add_invoice_items: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    backdate_start_date: Optional[Any] = None
    billing_cycle_anchor: Optional[Any] = None
    billing_thresholds: Optional[Any] = None
    cancel_at: Optional[Any] = None
    cancel_at_period_end: Optional[Any] = None
    collection_method: Optional[Any] = None
    currency: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    items: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    payment_settings: Optional[Any] = None
    pending_invoice_item_interval: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    transfer_data: Optional[Any] = None
    trial_end: Optional[Any] = None
    trial_from_plan: Optional[Any] = None
    trial_period_days: Optional[Any] = None
    trial_settings: Optional[Any] = None

class DeleteCustomersCustomerSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    customer: Optional[str] = None
    subscription_exposed_id: Optional[str] = None
    expand: Optional[Any] = None
    invoice_now: Optional[Any] = None
    prorate: Optional[Any] = None

class GetCustomersCustomerSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    subscription_exposed_id: Optional[str] = None

class PostCustomersCustomerSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    customer: Optional[str] = None
    subscription_exposed_id: Optional[str] = None
    add_invoice_items: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    billing_cycle_anchor: Optional[Any] = None
    billing_thresholds: Optional[Any] = None
    cancel_at: Optional[Any] = None
    cancel_at_period_end: Optional[Any] = None
    cancellation_details: Optional[Any] = None
    collection_method: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    items: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    pause_collection: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    payment_settings: Optional[Any] = None
    pending_invoice_item_interval: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None
    transfer_data: Optional[Any] = None
    trial_end: Optional[Any] = None
    trial_from_plan: Optional[Any] = None
    trial_settings: Optional[Any] = None

class DeleteCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount_params(msgspec.Struct):
    customer: Optional[str] = None
    subscription_exposed_id: Optional[str] = None

class GetCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    subscription_exposed_id: Optional[str] = None

class GetCustomersCustomerTaxIds_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostCustomersCustomerTaxIds_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[Any] = None
    type: Optional[Any] = None
    value: Optional[Any] = None

class DeleteCustomersCustomerTaxIdsId_params(msgspec.Struct):
    customer: Optional[str] = None
    id: Optional[str] = None

class GetCustomersCustomerTaxIdsId_params(msgspec.Struct):
    customer: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetDisputes_params(msgspec.Struct):
    charge: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_intent: Optional[str] = None
    starting_after: Optional[str] = None

class GetDisputesDispute_params(msgspec.Struct):
    dispute: Optional[str] = None
    expand: Optional[List[str]] = None

class PostDisputesDispute_params(msgspec.Struct):
    dispute: Optional[str] = None
    evidence: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    submit: Optional[Any] = None

class PostDisputesDisputeClose_params(msgspec.Struct):
    dispute: Optional[str] = None
    expand: Optional[Any] = None

class GetEntitlementsActiveEntitlements_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetEntitlementsActiveEntitlementsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetEntitlementsFeatures_params(msgspec.Struct):
    archived: Optional[bool] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    lookup_key: Optional[str] = None
    starting_after: Optional[str] = None

class PostEntitlementsFeatures_params(msgspec.Struct):
    expand: Optional[Any] = None
    lookup_key: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetEntitlementsFeaturesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostEntitlementsFeaturesId_params(msgspec.Struct):
    id: Optional[str] = None
    active: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class PostEphemeralKeys_params(msgspec.Struct):
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    issuing_card: Optional[Any] = None
    nonce: Optional[Any] = None
    verification_session: Optional[Any] = None

class DeleteEphemeralKeysKey_params(msgspec.Struct):
    key: Optional[str] = None
    expand: Optional[Any] = None

class GetEvents_params(msgspec.Struct):
    created: Optional[Any] = None
    delivery_success: Optional[bool] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None
    types: Optional[List[str]] = None

class GetEventsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetExchangeRates_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetExchangeRatesRateId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    rate_id: Optional[str] = None

class PostExternalAccountsId_params(msgspec.Struct):
    id: Optional[str] = None
    account_holder_name: Optional[Any] = None
    account_holder_type: Optional[Any] = None
    account_type: Optional[Any] = None
    address_city: Optional[Any] = None
    address_country: Optional[Any] = None
    address_line1: Optional[Any] = None
    address_line2: Optional[Any] = None
    address_state: Optional[Any] = None
    address_zip: Optional[Any] = None
    default_for_currency: Optional[Any] = None
    documents: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetFileLinks_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    expired: Optional[bool] = None
    file: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostFileLinks_params(msgspec.Struct):
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    file: Optional[Any] = None
    metadata: Optional[Any] = None

class GetFileLinksLink_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    link: Optional[str] = None

class PostFileLinksLink_params(msgspec.Struct):
    link: Optional[str] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    metadata: Optional[Any] = None

class GetFiles_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    purpose: Optional[str] = None
    starting_after: Optional[str] = None

class PostFiles_params(msgspec.Struct):
    expand: Optional[Any] = None
    file: Optional[Any] = None
    file_link_data: Optional[Any] = None
    purpose: Optional[Any] = None

class GetFilesFile_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    file: Optional[str] = None

class GetFinancialConnectionsAccounts_params(msgspec.Struct):
    account_holder: Optional[Dict[str, Any]] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    session: Optional[str] = None
    starting_after: Optional[str] = None

class GetFinancialConnectionsAccountsAccount_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None

class PostFinancialConnectionsAccountsAccountDisconnect_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None

class GetFinancialConnectionsAccountsAccountOwners_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    ownership: Optional[str] = None
    starting_after: Optional[str] = None

class PostFinancialConnectionsAccountsAccountRefresh_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None

class PostFinancialConnectionsAccountsAccountSubscribe_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None

class PostFinancialConnectionsAccountsAccountUnsubscribe_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None

class PostFinancialConnectionsSessions_params(msgspec.Struct):
    account_holder: Optional[Any] = None
    expand: Optional[Any] = None
    filters: Optional[Any] = None
    permissions: Optional[Any] = None
    prefetch: Optional[Any] = None
    return_url: Optional[Any] = None

class GetFinancialConnectionsSessionsSession_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    session: Optional[str] = None

class GetFinancialConnectionsTransactions_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    transacted_at: Optional[Any] = None
    transaction_refresh: Optional[Dict[str, Any]] = None

class GetFinancialConnectionsTransactionsTransaction_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    transaction: Optional[str] = None

class GetForwardingRequests_params(msgspec.Struct):
    created: Optional[Dict[str, Any]] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostForwardingRequests_params(msgspec.Struct):
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_method: Optional[Any] = None
    replacements: Optional[Any] = None
    request: Optional[Any] = None
    url: Optional[Any] = None

class GetForwardingRequestsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetIdentityVerificationReports_params(msgspec.Struct):
    client_reference_id: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None
    verification_session: Optional[str] = None

class GetIdentityVerificationReportsReport_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    report: Optional[str] = None

class GetIdentityVerificationSessions_params(msgspec.Struct):
    client_reference_id: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    related_customer: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostIdentityVerificationSessions_params(msgspec.Struct):
    client_reference_id: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    options: Optional[Any] = None
    provided_details: Optional[Any] = None
    related_customer: Optional[Any] = None
    related_person: Optional[Any] = None
    return_url: Optional[Any] = None
    type: Optional[Any] = None
    verification_flow: Optional[Any] = None

class GetIdentityVerificationSessionsSession_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    session: Optional[str] = None

class PostIdentityVerificationSessionsSession_params(msgspec.Struct):
    session: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    options: Optional[Any] = None
    provided_details: Optional[Any] = None
    type: Optional[Any] = None

class PostIdentityVerificationSessionsSessionCancel_params(msgspec.Struct):
    session: Optional[str] = None
    expand: Optional[Any] = None

class PostIdentityVerificationSessionsSessionRedact_params(msgspec.Struct):
    session: Optional[str] = None
    expand: Optional[Any] = None

class GetInvoicePayments_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    limit: Optional[int] = None
    payment: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetInvoicePaymentsInvoicePayment_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    invoice_payment: Optional[str] = None

class GetInvoiceRenderingTemplates_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetInvoiceRenderingTemplatesTemplate_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    template: Optional[str] = None
    version: Optional[int] = None

class PostInvoiceRenderingTemplatesTemplateArchive_params(msgspec.Struct):
    template: Optional[str] = None
    expand: Optional[Any] = None

class PostInvoiceRenderingTemplatesTemplateUnarchive_params(msgspec.Struct):
    template: Optional[str] = None
    expand: Optional[Any] = None

class GetInvoiceitems_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    limit: Optional[int] = None
    pending: Optional[bool] = None
    starting_after: Optional[str] = None

class PostInvoiceitems_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    discountable: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice: Optional[Any] = None
    metadata: Optional[Any] = None
    period: Optional[Any] = None
    price_data: Optional[Any] = None
    pricing: Optional[Any] = None
    quantity: Optional[Any] = None
    subscription: Optional[Any] = None
    tax_behavior: Optional[Any] = None
    tax_code: Optional[Any] = None
    tax_rates: Optional[Any] = None
    unit_amount_decimal: Optional[Any] = None

class DeleteInvoiceitemsInvoiceitem_params(msgspec.Struct):
    invoiceitem: Optional[str] = None

class GetInvoiceitemsInvoiceitem_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    invoiceitem: Optional[str] = None

class PostInvoiceitemsInvoiceitem_params(msgspec.Struct):
    invoiceitem: Optional[str] = None
    amount: Optional[Any] = None
    description: Optional[Any] = None
    discountable: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    period: Optional[Any] = None
    price_data: Optional[Any] = None
    pricing: Optional[Any] = None
    quantity: Optional[Any] = None
    tax_behavior: Optional[Any] = None
    tax_code: Optional[Any] = None
    tax_rates: Optional[Any] = None
    unit_amount_decimal: Optional[Any] = None

class GetInvoices_params(msgspec.Struct):
    collection_method: Optional[str] = None
    created: Optional[Any] = None
    customer: Optional[str] = None
    due_date: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    subscription: Optional[str] = None

class PostInvoices_params(msgspec.Struct):
    account_tax_ids: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    auto_advance: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    automatically_finalizes_at: Optional[Any] = None
    collection_method: Optional[Any] = None
    currency: Optional[Any] = None
    custom_fields: Optional[Any] = None
    customer: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    due_date: Optional[Any] = None
    effective_at: Optional[Any] = None
    expand: Optional[Any] = None
    footer: Optional[Any] = None
    from_invoice: Optional[Any] = None
    issuer: Optional[Any] = None
    metadata: Optional[Any] = None
    number: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    payment_settings: Optional[Any] = None
    pending_invoice_items_behavior: Optional[Any] = None
    rendering: Optional[Any] = None
    shipping_cost: Optional[Any] = None
    shipping_details: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    subscription: Optional[Any] = None
    transfer_data: Optional[Any] = None

class PostInvoicesCreatePreview_params(msgspec.Struct):
    automatic_tax: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    customer_details: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_items: Optional[Any] = None
    issuer: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    preview_mode: Optional[Any] = None
    schedule: Optional[Any] = None
    schedule_details: Optional[Any] = None
    subscription: Optional[Any] = None
    subscription_details: Optional[Any] = None

class GetInvoicesSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class DeleteInvoicesInvoice_params(msgspec.Struct):
    invoice: Optional[str] = None

class GetInvoicesInvoice_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None

class PostInvoicesInvoice_params(msgspec.Struct):
    invoice: Optional[str] = None
    account_tax_ids: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    auto_advance: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    automatically_finalizes_at: Optional[Any] = None
    collection_method: Optional[Any] = None
    custom_fields: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    due_date: Optional[Any] = None
    effective_at: Optional[Any] = None
    expand: Optional[Any] = None
    footer: Optional[Any] = None
    issuer: Optional[Any] = None
    metadata: Optional[Any] = None
    number: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    payment_settings: Optional[Any] = None
    rendering: Optional[Any] = None
    shipping_cost: Optional[Any] = None
    shipping_details: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    transfer_data: Optional[Any] = None

class PostInvoicesInvoiceAddLines_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None
    invoice_metadata: Optional[Any] = None
    lines: Optional[Any] = None

class PostInvoicesInvoiceAttachPayment_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None
    payment_intent: Optional[Any] = None

class PostInvoicesInvoiceFinalize_params(msgspec.Struct):
    invoice: Optional[str] = None
    auto_advance: Optional[Any] = None
    expand: Optional[Any] = None

class GetInvoicesInvoiceLines_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    invoice: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostInvoicesInvoiceLinesLineItemId_params(msgspec.Struct):
    invoice: Optional[str] = None
    line_item_id: Optional[str] = None
    amount: Optional[Any] = None
    description: Optional[Any] = None
    discountable: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    period: Optional[Any] = None
    price_data: Optional[Any] = None
    pricing: Optional[Any] = None
    quantity: Optional[Any] = None
    tax_amounts: Optional[Any] = None
    tax_rates: Optional[Any] = None

class PostInvoicesInvoiceMarkUncollectible_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None

class PostInvoicesInvoicePay_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None
    forgive: Optional[Any] = None
    mandate: Optional[Any] = None
    off_session: Optional[Any] = None
    paid_out_of_band: Optional[Any] = None
    payment_method: Optional[Any] = None
    source: Optional[Any] = None

class PostInvoicesInvoiceRemoveLines_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None
    invoice_metadata: Optional[Any] = None
    lines: Optional[Any] = None

class PostInvoicesInvoiceSend_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None

class PostInvoicesInvoiceUpdateLines_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None
    invoice_metadata: Optional[Any] = None
    lines: Optional[Any] = None

class PostInvoicesInvoiceVoid_params(msgspec.Struct):
    invoice: Optional[str] = None
    expand: Optional[Any] = None

class GetIssuingAuthorizations_params(msgspec.Struct):
    card: Optional[str] = None
    cardholder: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetIssuingAuthorizationsAuthorization_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[List[str]] = None

class PostIssuingAuthorizationsAuthorization_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostIssuingAuthorizationsAuthorizationApprove_params(msgspec.Struct):
    authorization: Optional[str] = None
    amount: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostIssuingAuthorizationsAuthorizationDecline_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetIssuingCardholders_params(msgspec.Struct):
    created: Optional[Any] = None
    email: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    phone_number: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None

class PostIssuingCardholders_params(msgspec.Struct):
    billing: Optional[Any] = None
    company: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    individual: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    phone_number: Optional[Any] = None
    preferred_locales: Optional[Any] = None
    spending_controls: Optional[Any] = None
    status: Optional[Any] = None
    type: Optional[Any] = None

class GetIssuingCardholdersCardholder_params(msgspec.Struct):
    cardholder: Optional[str] = None
    expand: Optional[List[str]] = None

class PostIssuingCardholdersCardholder_params(msgspec.Struct):
    cardholder: Optional[str] = None
    billing: Optional[Any] = None
    company: Optional[Any] = None
    email: Optional[Any] = None
    expand: Optional[Any] = None
    individual: Optional[Any] = None
    metadata: Optional[Any] = None
    phone_number: Optional[Any] = None
    preferred_locales: Optional[Any] = None
    spending_controls: Optional[Any] = None
    status: Optional[Any] = None

class GetIssuingCards_params(msgspec.Struct):
    cardholder: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    expand: Optional[List[str]] = None
    last4: Optional[str] = None
    limit: Optional[int] = None
    personalization_design: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None

class PostIssuingCards_params(msgspec.Struct):
    cardholder: Optional[Any] = None
    currency: Optional[Any] = None
    exp_month: Optional[Any] = None
    exp_year: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    metadata: Optional[Any] = None
    personalization_design: Optional[Any] = None
    pin: Optional[Any] = None
    replacement_for: Optional[Any] = None
    replacement_reason: Optional[Any] = None
    second_line: Optional[Any] = None
    shipping: Optional[Any] = None
    spending_controls: Optional[Any] = None
    status: Optional[Any] = None
    type: Optional[Any] = None

class GetIssuingCardsCard_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[List[str]] = None

class PostIssuingCardsCard_params(msgspec.Struct):
    card: Optional[str] = None
    cancellation_reason: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    personalization_design: Optional[Any] = None
    pin: Optional[Any] = None
    shipping: Optional[Any] = None
    spending_controls: Optional[Any] = None
    status: Optional[Any] = None

class GetIssuingDisputes_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    transaction: Optional[str] = None

class PostIssuingDisputes_params(msgspec.Struct):
    amount: Optional[Any] = None
    evidence: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    transaction: Optional[Any] = None
    treasury: Optional[Any] = None

class GetIssuingDisputesDispute_params(msgspec.Struct):
    dispute: Optional[str] = None
    expand: Optional[List[str]] = None

class PostIssuingDisputesDispute_params(msgspec.Struct):
    dispute: Optional[str] = None
    amount: Optional[Any] = None
    evidence: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostIssuingDisputesDisputeSubmit_params(msgspec.Struct):
    dispute: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetIssuingPersonalizationDesigns_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    lookup_keys: Optional[List[str]] = None
    preferences: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostIssuingPersonalizationDesigns_params(msgspec.Struct):
    card_logo: Optional[Any] = None
    carrier_text: Optional[Any] = None
    expand: Optional[Any] = None
    lookup_key: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    physical_bundle: Optional[Any] = None
    preferences: Optional[Any] = None
    transfer_lookup_key: Optional[Any] = None

class GetIssuingPersonalizationDesignsPersonalizationDesign_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    personalization_design: Optional[str] = None

class PostIssuingPersonalizationDesignsPersonalizationDesign_params(msgspec.Struct):
    personalization_design: Optional[str] = None
    card_logo: Optional[Any] = None
    carrier_text: Optional[Any] = None
    expand: Optional[Any] = None
    lookup_key: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    physical_bundle: Optional[Any] = None
    preferences: Optional[Any] = None
    transfer_lookup_key: Optional[Any] = None

class GetIssuingPhysicalBundles_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None

class GetIssuingPhysicalBundlesPhysicalBundle_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    physical_bundle: Optional[str] = None

class GetIssuingSettlementsSettlement_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    settlement: Optional[str] = None

class PostIssuingSettlementsSettlement_params(msgspec.Struct):
    settlement: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetIssuingTokens_params(msgspec.Struct):
    card: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetIssuingTokensToken_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    token: Optional[str] = None

class PostIssuingTokensToken_params(msgspec.Struct):
    token: Optional[str] = None
    expand: Optional[Any] = None
    status: Optional[Any] = None

class GetIssuingTransactions_params(msgspec.Struct):
    card: Optional[str] = None
    cardholder: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class GetIssuingTransactionsTransaction_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    transaction: Optional[str] = None

class PostIssuingTransactionsTransaction_params(msgspec.Struct):
    transaction: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostLinkAccountSessions_params(msgspec.Struct):
    account_holder: Optional[Any] = None
    expand: Optional[Any] = None
    filters: Optional[Any] = None
    permissions: Optional[Any] = None
    prefetch: Optional[Any] = None
    return_url: Optional[Any] = None

class GetLinkAccountSessionsSession_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    session: Optional[str] = None

class GetLinkedAccounts_params(msgspec.Struct):
    account_holder: Optional[Dict[str, Any]] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    session: Optional[str] = None
    starting_after: Optional[str] = None

class GetLinkedAccountsAccount_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[List[str]] = None

class PostLinkedAccountsAccountDisconnect_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None

class GetLinkedAccountsAccountOwners_params(msgspec.Struct):
    account: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    ownership: Optional[str] = None
    starting_after: Optional[str] = None

class PostLinkedAccountsAccountRefresh_params(msgspec.Struct):
    account: Optional[str] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None

class GetMandatesMandate_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    mandate: Optional[str] = None

class GetPaymentIntents_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostPaymentIntents_params(msgspec.Struct):
    amount: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    automatic_payment_methods: Optional[Any] = None
    capture_method: Optional[Any] = None
    confirm: Optional[Any] = None
    confirmation_method: Optional[Any] = None
    confirmation_token: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    error_on_requires_action: Optional[Any] = None
    excluded_payment_method_types: Optional[Any] = None
    expand: Optional[Any] = None
    mandate: Optional[Any] = None
    mandate_data: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_configuration: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    radar_options: Optional[Any] = None
    receipt_email: Optional[Any] = None
    return_url: Optional[Any] = None
    setup_future_usage: Optional[Any] = None
    shipping: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    statement_descriptor_suffix: Optional[Any] = None
    transfer_data: Optional[Any] = None
    transfer_group: Optional[Any] = None
    use_stripe_sdk: Optional[Any] = None

class GetPaymentIntentsSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class GetPaymentIntentsIntent_params(msgspec.Struct):
    client_secret: Optional[str] = None
    expand: Optional[List[str]] = None
    intent: Optional[str] = None

class PostPaymentIntentsIntent_params(msgspec.Struct):
    intent: Optional[str] = None
    amount: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    capture_method: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_configuration: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    receipt_email: Optional[Any] = None
    setup_future_usage: Optional[Any] = None
    shipping: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    statement_descriptor_suffix: Optional[Any] = None
    transfer_data: Optional[Any] = None
    transfer_group: Optional[Any] = None

class PostPaymentIntentsIntentApplyCustomerBalance_params(msgspec.Struct):
    intent: Optional[str] = None
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None

class PostPaymentIntentsIntentCancel_params(msgspec.Struct):
    intent: Optional[str] = None
    cancellation_reason: Optional[Any] = None
    expand: Optional[Any] = None

class PostPaymentIntentsIntentCapture_params(msgspec.Struct):
    intent: Optional[str] = None
    amount_to_capture: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    expand: Optional[Any] = None
    final_capture: Optional[Any] = None
    metadata: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    statement_descriptor_suffix: Optional[Any] = None
    transfer_data: Optional[Any] = None

class PostPaymentIntentsIntentConfirm_params(msgspec.Struct):
    intent: Optional[str] = None
    capture_method: Optional[Any] = None
    client_secret: Optional[Any] = None
    confirmation_token: Optional[Any] = None
    error_on_requires_action: Optional[Any] = None
    expand: Optional[Any] = None
    mandate: Optional[Any] = None
    mandate_data: Optional[Any] = None
    off_session: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    radar_options: Optional[Any] = None
    receipt_email: Optional[Any] = None
    return_url: Optional[Any] = None
    setup_future_usage: Optional[Any] = None
    shipping: Optional[Any] = None
    use_stripe_sdk: Optional[Any] = None

class PostPaymentIntentsIntentIncrementAuthorization_params(msgspec.Struct):
    intent: Optional[str] = None
    amount: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    transfer_data: Optional[Any] = None

class PostPaymentIntentsIntentVerifyMicrodeposits_params(msgspec.Struct):
    intent: Optional[str] = None
    amounts: Optional[Any] = None
    client_secret: Optional[Any] = None
    descriptor_code: Optional[Any] = None
    expand: Optional[Any] = None

class GetPaymentLinks_params(msgspec.Struct):
    active: Optional[bool] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostPaymentLinks_params(msgspec.Struct):
    after_completion: Optional[Any] = None
    allow_promotion_codes: Optional[Any] = None
    application_fee_amount: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    billing_address_collection: Optional[Any] = None
    consent_collection: Optional[Any] = None
    currency: Optional[Any] = None
    custom_fields: Optional[Any] = None
    custom_text: Optional[Any] = None
    customer_creation: Optional[Any] = None
    expand: Optional[Any] = None
    inactive_message: Optional[Any] = None
    invoice_creation: Optional[Any] = None
    line_items: Optional[Any] = None
    metadata: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    optional_items: Optional[Any] = None
    payment_intent_data: Optional[Any] = None
    payment_method_collection: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    phone_number_collection: Optional[Any] = None
    restrictions: Optional[Any] = None
    shipping_address_collection: Optional[Any] = None
    shipping_options: Optional[Any] = None
    submit_type: Optional[Any] = None
    subscription_data: Optional[Any] = None
    tax_id_collection: Optional[Any] = None
    transfer_data: Optional[Any] = None

class GetPaymentLinksPaymentLink_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    payment_link: Optional[str] = None

class PostPaymentLinksPaymentLink_params(msgspec.Struct):
    payment_link: Optional[str] = None
    active: Optional[Any] = None
    after_completion: Optional[Any] = None
    allow_promotion_codes: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    billing_address_collection: Optional[Any] = None
    custom_fields: Optional[Any] = None
    custom_text: Optional[Any] = None
    customer_creation: Optional[Any] = None
    expand: Optional[Any] = None
    inactive_message: Optional[Any] = None
    invoice_creation: Optional[Any] = None
    line_items: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_intent_data: Optional[Any] = None
    payment_method_collection: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    phone_number_collection: Optional[Any] = None
    restrictions: Optional[Any] = None
    shipping_address_collection: Optional[Any] = None
    submit_type: Optional[Any] = None
    subscription_data: Optional[Any] = None
    tax_id_collection: Optional[Any] = None

class GetPaymentLinksPaymentLinkLineItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_link: Optional[str] = None
    starting_after: Optional[str] = None

class GetPaymentMethodConfigurations_params(msgspec.Struct):
    application: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostPaymentMethodConfigurations_params(msgspec.Struct):
    acss_debit: Optional[Any] = None
    affirm: Optional[Any] = None
    afterpay_clearpay: Optional[Any] = None
    alipay: Optional[Any] = None
    alma: Optional[Any] = None
    amazon_pay: Optional[Any] = None
    apple_pay: Optional[Any] = None
    apple_pay_later: Optional[Any] = None
    au_becs_debit: Optional[Any] = None
    bacs_debit: Optional[Any] = None
    bancontact: Optional[Any] = None
    billie: Optional[Any] = None
    blik: Optional[Any] = None
    boleto: Optional[Any] = None
    card: Optional[Any] = None
    cartes_bancaires: Optional[Any] = None
    cashapp: Optional[Any] = None
    customer_balance: Optional[Any] = None
    eps: Optional[Any] = None
    expand: Optional[Any] = None
    fpx: Optional[Any] = None
    giropay: Optional[Any] = None
    google_pay: Optional[Any] = None
    grabpay: Optional[Any] = None
    ideal: Optional[Any] = None
    jcb: Optional[Any] = None
    kakao_pay: Optional[Any] = None
    klarna: Optional[Any] = None
    konbini: Optional[Any] = None
    kr_card: Optional[Any] = None
    link: Optional[Any] = None
    mobilepay: Optional[Any] = None
    multibanco: Optional[Any] = None
    name: Optional[Any] = None
    naver_pay: Optional[Any] = None
    nz_bank_account: Optional[Any] = None
    oxxo: Optional[Any] = None
    p24: Optional[Any] = None
    parent: Optional[Any] = None
    pay_by_bank: Optional[Any] = None
    payco: Optional[Any] = None
    paynow: Optional[Any] = None
    paypal: Optional[Any] = None
    pix: Optional[Any] = None
    promptpay: Optional[Any] = None
    revolut_pay: Optional[Any] = None
    samsung_pay: Optional[Any] = None
    satispay: Optional[Any] = None
    sepa_debit: Optional[Any] = None
    sofort: Optional[Any] = None
    swish: Optional[Any] = None
    twint: Optional[Any] = None
    us_bank_account: Optional[Any] = None
    wechat_pay: Optional[Any] = None
    zip: Optional[Any] = None

class GetPaymentMethodConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    expand: Optional[List[str]] = None

class PostPaymentMethodConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    acss_debit: Optional[Any] = None
    active: Optional[Any] = None
    affirm: Optional[Any] = None
    afterpay_clearpay: Optional[Any] = None
    alipay: Optional[Any] = None
    alma: Optional[Any] = None
    amazon_pay: Optional[Any] = None
    apple_pay: Optional[Any] = None
    apple_pay_later: Optional[Any] = None
    au_becs_debit: Optional[Any] = None
    bacs_debit: Optional[Any] = None
    bancontact: Optional[Any] = None
    billie: Optional[Any] = None
    blik: Optional[Any] = None
    boleto: Optional[Any] = None
    card: Optional[Any] = None
    cartes_bancaires: Optional[Any] = None
    cashapp: Optional[Any] = None
    customer_balance: Optional[Any] = None
    eps: Optional[Any] = None
    expand: Optional[Any] = None
    fpx: Optional[Any] = None
    giropay: Optional[Any] = None
    google_pay: Optional[Any] = None
    grabpay: Optional[Any] = None
    ideal: Optional[Any] = None
    jcb: Optional[Any] = None
    kakao_pay: Optional[Any] = None
    klarna: Optional[Any] = None
    konbini: Optional[Any] = None
    kr_card: Optional[Any] = None
    link: Optional[Any] = None
    mobilepay: Optional[Any] = None
    multibanco: Optional[Any] = None
    name: Optional[Any] = None
    naver_pay: Optional[Any] = None
    nz_bank_account: Optional[Any] = None
    oxxo: Optional[Any] = None
    p24: Optional[Any] = None
    pay_by_bank: Optional[Any] = None
    payco: Optional[Any] = None
    paynow: Optional[Any] = None
    paypal: Optional[Any] = None
    pix: Optional[Any] = None
    promptpay: Optional[Any] = None
    revolut_pay: Optional[Any] = None
    samsung_pay: Optional[Any] = None
    satispay: Optional[Any] = None
    sepa_debit: Optional[Any] = None
    sofort: Optional[Any] = None
    swish: Optional[Any] = None
    twint: Optional[Any] = None
    us_bank_account: Optional[Any] = None
    wechat_pay: Optional[Any] = None
    zip: Optional[Any] = None

class GetPaymentMethodDomains_params(msgspec.Struct):
    domain_name: Optional[str] = None
    enabled: Optional[bool] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostPaymentMethodDomains_params(msgspec.Struct):
    domain_name: Optional[Any] = None
    enabled: Optional[Any] = None
    expand: Optional[Any] = None

class GetPaymentMethodDomainsPaymentMethodDomain_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    payment_method_domain: Optional[str] = None

class PostPaymentMethodDomainsPaymentMethodDomain_params(msgspec.Struct):
    payment_method_domain: Optional[str] = None
    enabled: Optional[Any] = None
    expand: Optional[Any] = None

class PostPaymentMethodDomainsPaymentMethodDomainValidate_params(msgspec.Struct):
    payment_method_domain: Optional[str] = None
    expand: Optional[Any] = None

class GetPaymentMethods_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class PostPaymentMethods_params(msgspec.Struct):
    acss_debit: Optional[Any] = None
    affirm: Optional[Any] = None
    afterpay_clearpay: Optional[Any] = None
    alipay: Optional[Any] = None
    allow_redisplay: Optional[Any] = None
    alma: Optional[Any] = None
    amazon_pay: Optional[Any] = None
    au_becs_debit: Optional[Any] = None
    bacs_debit: Optional[Any] = None
    bancontact: Optional[Any] = None
    billie: Optional[Any] = None
    billing_details: Optional[Any] = None
    blik: Optional[Any] = None
    boleto: Optional[Any] = None
    card: Optional[Any] = None
    cashapp: Optional[Any] = None
    crypto: Optional[Any] = None
    customer: Optional[Any] = None
    customer_balance: Optional[Any] = None
    eps: Optional[Any] = None
    expand: Optional[Any] = None
    fpx: Optional[Any] = None
    giropay: Optional[Any] = None
    grabpay: Optional[Any] = None
    ideal: Optional[Any] = None
    interac_present: Optional[Any] = None
    kakao_pay: Optional[Any] = None
    klarna: Optional[Any] = None
    konbini: Optional[Any] = None
    kr_card: Optional[Any] = None
    link: Optional[Any] = None
    metadata: Optional[Any] = None
    mobilepay: Optional[Any] = None
    multibanco: Optional[Any] = None
    naver_pay: Optional[Any] = None
    nz_bank_account: Optional[Any] = None
    oxxo: Optional[Any] = None
    p24: Optional[Any] = None
    pay_by_bank: Optional[Any] = None
    payco: Optional[Any] = None
    payment_method: Optional[Any] = None
    paynow: Optional[Any] = None
    paypal: Optional[Any] = None
    pix: Optional[Any] = None
    promptpay: Optional[Any] = None
    radar_options: Optional[Any] = None
    revolut_pay: Optional[Any] = None
    samsung_pay: Optional[Any] = None
    satispay: Optional[Any] = None
    sepa_debit: Optional[Any] = None
    sofort: Optional[Any] = None
    swish: Optional[Any] = None
    twint: Optional[Any] = None
    type: Optional[Any] = None
    us_bank_account: Optional[Any] = None
    wechat_pay: Optional[Any] = None
    zip: Optional[Any] = None

class GetPaymentMethodsPaymentMethod_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    payment_method: Optional[str] = None

class PostPaymentMethodsPaymentMethod_params(msgspec.Struct):
    payment_method: Optional[str] = None
    allow_redisplay: Optional[Any] = None
    billing_details: Optional[Any] = None
    card: Optional[Any] = None
    expand: Optional[Any] = None
    link: Optional[Any] = None
    metadata: Optional[Any] = None
    pay_by_bank: Optional[Any] = None
    us_bank_account: Optional[Any] = None

class PostPaymentMethodsPaymentMethodAttach_params(msgspec.Struct):
    payment_method: Optional[str] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None

class PostPaymentMethodsPaymentMethodDetach_params(msgspec.Struct):
    payment_method: Optional[str] = None
    expand: Optional[Any] = None

class GetPayouts_params(msgspec.Struct):
    arrival_date: Optional[Any] = None
    created: Optional[Any] = None
    destination: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostPayouts_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    destination: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    method: Optional[Any] = None
    payout_method: Optional[Any] = None
    source_type: Optional[Any] = None
    statement_descriptor: Optional[Any] = None

class GetPayoutsPayout_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    payout: Optional[str] = None

class PostPayoutsPayout_params(msgspec.Struct):
    payout: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostPayoutsPayoutCancel_params(msgspec.Struct):
    payout: Optional[str] = None
    expand: Optional[Any] = None

class PostPayoutsPayoutReverse_params(msgspec.Struct):
    payout: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetPlans_params(msgspec.Struct):
    active: Optional[bool] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    product: Optional[str] = None
    starting_after: Optional[str] = None

class PostPlans_params(msgspec.Struct):
    active: Optional[Any] = None
    amount: Optional[Any] = None
    amount_decimal: Optional[Any] = None
    billing_scheme: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    id: Optional[Any] = None
    interval: Optional[Any] = None
    interval_count: Optional[Any] = None
    metadata: Optional[Any] = None
    meter: Optional[Any] = None
    nickname: Optional[Any] = None
    product: Optional[Any] = None
    tiers: Optional[Any] = None
    tiers_mode: Optional[Any] = None
    transform_usage: Optional[Any] = None
    trial_period_days: Optional[Any] = None
    usage_type: Optional[Any] = None

class DeletePlansPlan_params(msgspec.Struct):
    plan: Optional[str] = None

class GetPlansPlan_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    plan: Optional[str] = None

class PostPlansPlan_params(msgspec.Struct):
    plan: Optional[str] = None
    active: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    nickname: Optional[Any] = None
    product: Optional[Any] = None
    trial_period_days: Optional[Any] = None

class GetPrices_params(msgspec.Struct):
    active: Optional[bool] = None
    created: Optional[Any] = None
    currency: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    lookup_keys: Optional[List[str]] = None
    product: Optional[str] = None
    recurring: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None
    type: Optional[str] = None

class PostPrices_params(msgspec.Struct):
    active: Optional[Any] = None
    billing_scheme: Optional[Any] = None
    currency: Optional[Any] = None
    currency_options: Optional[Any] = None
    custom_unit_amount: Optional[Any] = None
    expand: Optional[Any] = None
    lookup_key: Optional[Any] = None
    metadata: Optional[Any] = None
    nickname: Optional[Any] = None
    product: Optional[Any] = None
    product_data: Optional[Any] = None
    recurring: Optional[Any] = None
    tax_behavior: Optional[Any] = None
    tiers: Optional[Any] = None
    tiers_mode: Optional[Any] = None
    transfer_lookup_key: Optional[Any] = None
    transform_quantity: Optional[Any] = None
    unit_amount: Optional[Any] = None
    unit_amount_decimal: Optional[Any] = None

class GetPricesSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class GetPricesPrice_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    price: Optional[str] = None

class PostPricesPrice_params(msgspec.Struct):
    price: Optional[str] = None
    active: Optional[Any] = None
    currency_options: Optional[Any] = None
    expand: Optional[Any] = None
    lookup_key: Optional[Any] = None
    metadata: Optional[Any] = None
    nickname: Optional[Any] = None
    tax_behavior: Optional[Any] = None
    transfer_lookup_key: Optional[Any] = None

class GetProducts_params(msgspec.Struct):
    active: Optional[bool] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    ids: Optional[List[str]] = None
    limit: Optional[int] = None
    shippable: Optional[bool] = None
    starting_after: Optional[str] = None
    url: Optional[str] = None

class PostProducts_params(msgspec.Struct):
    active: Optional[Any] = None
    default_price_data: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    id: Optional[Any] = None
    images: Optional[Any] = None
    marketing_features: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    package_dimensions: Optional[Any] = None
    shippable: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    tax_code: Optional[Any] = None
    unit_label: Optional[Any] = None
    url: Optional[Any] = None

class GetProductsSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class DeleteProductsId_params(msgspec.Struct):
    id: Optional[str] = None

class GetProductsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostProductsId_params(msgspec.Struct):
    id: Optional[str] = None
    active: Optional[Any] = None
    default_price: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    images: Optional[Any] = None
    marketing_features: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None
    package_dimensions: Optional[Any] = None
    shippable: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    tax_code: Optional[Any] = None
    unit_label: Optional[Any] = None
    url: Optional[Any] = None

class GetProductsProductFeatures_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    product: Optional[str] = None
    starting_after: Optional[str] = None

class PostProductsProductFeatures_params(msgspec.Struct):
    product: Optional[str] = None
    entitlement_feature: Optional[Any] = None
    expand: Optional[Any] = None

class DeleteProductsProductFeaturesId_params(msgspec.Struct):
    id: Optional[str] = None
    product: Optional[str] = None

class GetProductsProductFeaturesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None
    product: Optional[str] = None

class GetPromotionCodes_params(msgspec.Struct):
    active: Optional[bool] = None
    code: Optional[str] = None
    coupon: Optional[str] = None
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostPromotionCodes_params(msgspec.Struct):
    active: Optional[Any] = None
    code: Optional[Any] = None
    coupon: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    max_redemptions: Optional[Any] = None
    metadata: Optional[Any] = None
    restrictions: Optional[Any] = None

class GetPromotionCodesPromotionCode_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    promotion_code: Optional[str] = None

class PostPromotionCodesPromotionCode_params(msgspec.Struct):
    promotion_code: Optional[str] = None
    active: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    restrictions: Optional[Any] = None

class GetQuotes_params(msgspec.Struct):
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    test_clock: Optional[str] = None

class PostQuotes_params(msgspec.Struct):
    application_fee_amount: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    collection_method: Optional[Any] = None
    customer: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    footer: Optional[Any] = None
    from_quote: Optional[Any] = None
    header: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    line_items: Optional[Any] = None
    metadata: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    subscription_data: Optional[Any] = None
    test_clock: Optional[Any] = None
    transfer_data: Optional[Any] = None

class GetQuotesQuote_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    quote: Optional[str] = None

class PostQuotesQuote_params(msgspec.Struct):
    quote: Optional[str] = None
    application_fee_amount: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    collection_method: Optional[Any] = None
    customer: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None
    footer: Optional[Any] = None
    header: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    line_items: Optional[Any] = None
    metadata: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    subscription_data: Optional[Any] = None
    transfer_data: Optional[Any] = None

class PostQuotesQuoteAccept_params(msgspec.Struct):
    quote: Optional[str] = None
    expand: Optional[Any] = None

class PostQuotesQuoteCancel_params(msgspec.Struct):
    quote: Optional[str] = None
    expand: Optional[Any] = None

class GetQuotesQuoteComputedUpfrontLineItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    quote: Optional[str] = None
    starting_after: Optional[str] = None

class PostQuotesQuoteFinalize_params(msgspec.Struct):
    quote: Optional[str] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None

class GetQuotesQuoteLineItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    quote: Optional[str] = None
    starting_after: Optional[str] = None

class GetQuotesQuotePdf_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    quote: Optional[str] = None

class GetRadarEarlyFraudWarnings_params(msgspec.Struct):
    charge: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_intent: Optional[str] = None
    starting_after: Optional[str] = None

class GetRadarEarlyFraudWarningsEarlyFraudWarning_params(msgspec.Struct):
    early_fraud_warning: Optional[str] = None
    expand: Optional[List[str]] = None

class GetRadarValueListItems_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    value: Optional[str] = None
    value_list: Optional[str] = None

class PostRadarValueListItems_params(msgspec.Struct):
    expand: Optional[Any] = None
    value: Optional[Any] = None
    value_list: Optional[Any] = None

class DeleteRadarValueListItemsItem_params(msgspec.Struct):
    item: Optional[str] = None

class GetRadarValueListItemsItem_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    item: Optional[str] = None

class GetRadarValueLists_params(msgspec.Struct):
    alias: Optional[str] = None
    contains: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostRadarValueLists_params(msgspec.Struct):
    alias: Optional[Any] = None
    expand: Optional[Any] = None
    item_type: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class DeleteRadarValueListsValueList_params(msgspec.Struct):
    value_list: Optional[str] = None

class GetRadarValueListsValueList_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    value_list: Optional[str] = None

class PostRadarValueListsValueList_params(msgspec.Struct):
    value_list: Optional[str] = None
    alias: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    name: Optional[Any] = None

class GetRefunds_params(msgspec.Struct):
    charge: Optional[str] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_intent: Optional[str] = None
    starting_after: Optional[str] = None

class PostRefunds_params(msgspec.Struct):
    amount: Optional[Any] = None
    charge: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    instructions_email: Optional[Any] = None
    metadata: Optional[Any] = None
    origin: Optional[Any] = None
    payment_intent: Optional[Any] = None
    reason: Optional[Any] = None
    refund_application_fee: Optional[Any] = None
    reverse_transfer: Optional[Any] = None

class GetRefundsRefund_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    refund: Optional[str] = None

class PostRefundsRefund_params(msgspec.Struct):
    refund: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostRefundsRefundCancel_params(msgspec.Struct):
    refund: Optional[str] = None
    expand: Optional[Any] = None

class GetReportingReportRuns_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostReportingReportRuns_params(msgspec.Struct):
    expand: Optional[Any] = None
    parameters: Optional[Any] = None
    report_type: Optional[Any] = None

class GetReportingReportRunsReportRun_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    report_run: Optional[str] = None

class GetReportingReportTypes_params(msgspec.Struct):
    expand: Optional[List[str]] = None

class GetReportingReportTypesReportType_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    report_type: Optional[str] = None

class GetReviews_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetReviewsReview_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    review: Optional[str] = None

class PostReviewsReviewApprove_params(msgspec.Struct):
    review: Optional[str] = None
    expand: Optional[Any] = None

class GetSetupAttempts_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    setup_intent: Optional[str] = None
    starting_after: Optional[str] = None

class GetSetupIntents_params(msgspec.Struct):
    attach_to_self: Optional[bool] = None
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    payment_method: Optional[str] = None
    starting_after: Optional[str] = None

class PostSetupIntents_params(msgspec.Struct):
    attach_to_self: Optional[Any] = None
    automatic_payment_methods: Optional[Any] = None
    confirm: Optional[Any] = None
    confirmation_token: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    flow_directions: Optional[Any] = None
    mandate_data: Optional[Any] = None
    metadata: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_configuration: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None
    return_url: Optional[Any] = None
    single_use: Optional[Any] = None
    usage: Optional[Any] = None
    use_stripe_sdk: Optional[Any] = None

class GetSetupIntentsIntent_params(msgspec.Struct):
    client_secret: Optional[str] = None
    expand: Optional[List[str]] = None
    intent: Optional[str] = None

class PostSetupIntentsIntent_params(msgspec.Struct):
    intent: Optional[str] = None
    attach_to_self: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    flow_directions: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_configuration: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    payment_method_types: Optional[Any] = None

class PostSetupIntentsIntentCancel_params(msgspec.Struct):
    intent: Optional[str] = None
    cancellation_reason: Optional[Any] = None
    expand: Optional[Any] = None

class PostSetupIntentsIntentConfirm_params(msgspec.Struct):
    intent: Optional[str] = None
    client_secret: Optional[Any] = None
    confirmation_token: Optional[Any] = None
    expand: Optional[Any] = None
    mandate_data: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    return_url: Optional[Any] = None
    use_stripe_sdk: Optional[Any] = None

class PostSetupIntentsIntentVerifyMicrodeposits_params(msgspec.Struct):
    intent: Optional[str] = None
    amounts: Optional[Any] = None
    client_secret: Optional[Any] = None
    descriptor_code: Optional[Any] = None
    expand: Optional[Any] = None

class GetShippingRates_params(msgspec.Struct):
    active: Optional[bool] = None
    created: Optional[Any] = None
    currency: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostShippingRates_params(msgspec.Struct):
    delivery_estimate: Optional[Any] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None
    fixed_amount: Optional[Any] = None
    metadata: Optional[Any] = None
    tax_behavior: Optional[Any] = None
    tax_code: Optional[Any] = None
    type: Optional[Any] = None

class GetShippingRatesShippingRateToken_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    shipping_rate_token: Optional[str] = None

class PostShippingRatesShippingRateToken_params(msgspec.Struct):
    shipping_rate_token: Optional[str] = None
    active: Optional[Any] = None
    expand: Optional[Any] = None
    fixed_amount: Optional[Any] = None
    metadata: Optional[Any] = None
    tax_behavior: Optional[Any] = None

class PostSigmaSavedQueriesId_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    name: Optional[Any] = None
    sql: Optional[Any] = None

class GetSigmaScheduledQueryRuns_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetSigmaScheduledQueryRunsScheduledQueryRun_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    scheduled_query_run: Optional[str] = None

class PostSources_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    expand: Optional[Any] = None
    flow: Optional[Any] = None
    mandate: Optional[Any] = None
    metadata: Optional[Any] = None
    original_source: Optional[Any] = None
    owner: Optional[Any] = None
    receiver: Optional[Any] = None
    redirect: Optional[Any] = None
    source_order: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    token: Optional[Any] = None
    type: Optional[Any] = None
    usage: Optional[Any] = None

class GetSourcesSource_params(msgspec.Struct):
    client_secret: Optional[str] = None
    expand: Optional[List[str]] = None
    source: Optional[str] = None

class PostSourcesSource_params(msgspec.Struct):
    source: Optional[str] = None
    amount: Optional[Any] = None
    expand: Optional[Any] = None
    mandate: Optional[Any] = None
    metadata: Optional[Any] = None
    owner: Optional[Any] = None
    source_order: Optional[Any] = None

class GetSourcesSourceMandateNotificationsMandateNotification_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    mandate_notification: Optional[str] = None
    source: Optional[str] = None

class GetSourcesSourceSourceTransactions_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    source: Optional[str] = None
    starting_after: Optional[str] = None

class GetSourcesSourceSourceTransactionsSourceTransaction_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    source: Optional[str] = None
    source_transaction: Optional[str] = None

class PostSourcesSourceVerify_params(msgspec.Struct):
    source: Optional[str] = None
    expand: Optional[Any] = None
    values: Optional[Any] = None

class GetSubscriptionItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    subscription: Optional[str] = None

class PostSubscriptionItems_params(msgspec.Struct):
    billing_thresholds: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    price: Optional[Any] = None
    price_data: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None
    quantity: Optional[Any] = None
    subscription: Optional[Any] = None
    tax_rates: Optional[Any] = None

class DeleteSubscriptionItemsItem_params(msgspec.Struct):
    item: Optional[str] = None
    clear_usage: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None

class GetSubscriptionItemsItem_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    item: Optional[str] = None

class PostSubscriptionItemsItem_params(msgspec.Struct):
    item: Optional[str] = None
    billing_thresholds: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    price: Optional[Any] = None
    price_data: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None
    quantity: Optional[Any] = None
    tax_rates: Optional[Any] = None

class GetSubscriptionSchedules_params(msgspec.Struct):
    canceled_at: Optional[Any] = None
    completed_at: Optional[Any] = None
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    released_at: Optional[Any] = None
    scheduled: Optional[bool] = None
    starting_after: Optional[str] = None

class PostSubscriptionSchedules_params(msgspec.Struct):
    billing_mode: Optional[Any] = None
    customer: Optional[Any] = None
    default_settings: Optional[Any] = None
    end_behavior: Optional[Any] = None
    expand: Optional[Any] = None
    from_subscription: Optional[Any] = None
    metadata: Optional[Any] = None
    phases: Optional[Any] = None
    start_date: Optional[Any] = None

class GetSubscriptionSchedulesSchedule_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    schedule: Optional[str] = None

class PostSubscriptionSchedulesSchedule_params(msgspec.Struct):
    schedule: Optional[str] = None
    default_settings: Optional[Any] = None
    end_behavior: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    phases: Optional[Any] = None
    proration_behavior: Optional[Any] = None

class PostSubscriptionSchedulesScheduleCancel_params(msgspec.Struct):
    schedule: Optional[str] = None
    expand: Optional[Any] = None
    invoice_now: Optional[Any] = None
    prorate: Optional[Any] = None

class PostSubscriptionSchedulesScheduleRelease_params(msgspec.Struct):
    schedule: Optional[str] = None
    expand: Optional[Any] = None
    preserve_cancel_date: Optional[Any] = None

class GetSubscriptions_params(msgspec.Struct):
    automatic_tax: Optional[Dict[str, Any]] = None
    collection_method: Optional[str] = None
    created: Optional[Any] = None
    current_period_end: Optional[Any] = None
    current_period_start: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    price: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    test_clock: Optional[str] = None

class PostSubscriptions_params(msgspec.Struct):
    add_invoice_items: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    backdate_start_date: Optional[Any] = None
    billing_cycle_anchor: Optional[Any] = None
    billing_cycle_anchor_config: Optional[Any] = None
    billing_mode: Optional[Any] = None
    billing_thresholds: Optional[Any] = None
    cancel_at: Optional[Any] = None
    cancel_at_period_end: Optional[Any] = None
    collection_method: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    items: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    payment_settings: Optional[Any] = None
    pending_invoice_item_interval: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    transfer_data: Optional[Any] = None
    trial_end: Optional[Any] = None
    trial_from_plan: Optional[Any] = None
    trial_period_days: Optional[Any] = None
    trial_settings: Optional[Any] = None

class GetSubscriptionsSearch_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    page: Optional[str] = None
    query: Optional[str] = None

class DeleteSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    subscription_exposed_id: Optional[str] = None
    cancellation_details: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_now: Optional[Any] = None
    prorate: Optional[Any] = None

class GetSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    subscription_exposed_id: Optional[str] = None

class PostSubscriptionsSubscriptionExposedId_params(msgspec.Struct):
    subscription_exposed_id: Optional[str] = None
    add_invoice_items: Optional[Any] = None
    application_fee_percent: Optional[Any] = None
    automatic_tax: Optional[Any] = None
    billing_cycle_anchor: Optional[Any] = None
    billing_thresholds: Optional[Any] = None
    cancel_at: Optional[Any] = None
    cancel_at_period_end: Optional[Any] = None
    cancellation_details: Optional[Any] = None
    collection_method: Optional[Any] = None
    days_until_due: Optional[Any] = None
    default_payment_method: Optional[Any] = None
    default_source: Optional[Any] = None
    default_tax_rates: Optional[Any] = None
    description: Optional[Any] = None
    discounts: Optional[Any] = None
    expand: Optional[Any] = None
    invoice_settings: Optional[Any] = None
    items: Optional[Any] = None
    metadata: Optional[Any] = None
    off_session: Optional[Any] = None
    on_behalf_of: Optional[Any] = None
    pause_collection: Optional[Any] = None
    payment_behavior: Optional[Any] = None
    payment_settings: Optional[Any] = None
    pending_invoice_item_interval: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None
    transfer_data: Optional[Any] = None
    trial_end: Optional[Any] = None
    trial_from_plan: Optional[Any] = None
    trial_settings: Optional[Any] = None

class DeleteSubscriptionsSubscriptionExposedIdDiscount_params(msgspec.Struct):
    subscription_exposed_id: Optional[str] = None

class PostSubscriptionsSubscriptionMigrate_params(msgspec.Struct):
    subscription: Optional[str] = None
    billing_mode: Optional[Any] = None
    expand: Optional[Any] = None

class PostSubscriptionsSubscriptionResume_params(msgspec.Struct):
    subscription: Optional[str] = None
    billing_cycle_anchor: Optional[Any] = None
    expand: Optional[Any] = None
    proration_behavior: Optional[Any] = None
    proration_date: Optional[Any] = None

class PostTaxCalculations_params(msgspec.Struct):
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    customer_details: Optional[Any] = None
    expand: Optional[Any] = None
    line_items: Optional[Any] = None
    ship_from_details: Optional[Any] = None
    shipping_cost: Optional[Any] = None
    tax_date: Optional[Any] = None

class GetTaxCalculationsCalculation_params(msgspec.Struct):
    calculation: Optional[str] = None
    expand: Optional[List[str]] = None

class GetTaxCalculationsCalculationLineItems_params(msgspec.Struct):
    calculation: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetTaxRegistrations_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTaxRegistrations_params(msgspec.Struct):
    active_from: Optional[Any] = None
    country: Optional[Any] = None
    country_options: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None

class GetTaxRegistrationsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostTaxRegistrationsId_params(msgspec.Struct):
    id: Optional[str] = None
    active_from: Optional[Any] = None
    expand: Optional[Any] = None
    expires_at: Optional[Any] = None

class GetTaxSettings_params(msgspec.Struct):
    expand: Optional[List[str]] = None

class PostTaxSettings_params(msgspec.Struct):
    defaults: Optional[Any] = None
    expand: Optional[Any] = None
    head_office: Optional[Any] = None

class PostTaxTransactionsCreateFromCalculation_params(msgspec.Struct):
    calculation: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    posted_at: Optional[Any] = None
    reference: Optional[Any] = None

class PostTaxTransactionsCreateReversal_params(msgspec.Struct):
    expand: Optional[Any] = None
    flat_amount: Optional[Any] = None
    line_items: Optional[Any] = None
    metadata: Optional[Any] = None
    mode: Optional[Any] = None
    original_transaction: Optional[Any] = None
    reference: Optional[Any] = None
    shipping_cost: Optional[Any] = None

class GetTaxTransactionsTransaction_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    transaction: Optional[str] = None

class GetTaxTransactionsTransactionLineItems_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    transaction: Optional[str] = None

class GetTaxCodes_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class GetTaxCodesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetTaxIds_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    owner: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None

class PostTaxIds_params(msgspec.Struct):
    expand: Optional[Any] = None
    owner: Optional[Any] = None
    type: Optional[Any] = None
    value: Optional[Any] = None

class DeleteTaxIdsId_params(msgspec.Struct):
    id: Optional[str] = None

class GetTaxIdsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetTaxRates_params(msgspec.Struct):
    active: Optional[bool] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    inclusive: Optional[bool] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostTaxRates_params(msgspec.Struct):
    active: Optional[Any] = None
    country: Optional[Any] = None
    description: Optional[Any] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None
    inclusive: Optional[Any] = None
    jurisdiction: Optional[Any] = None
    metadata: Optional[Any] = None
    percentage: Optional[Any] = None
    state: Optional[Any] = None
    tax_type: Optional[Any] = None

class GetTaxRatesTaxRate_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    tax_rate: Optional[str] = None

class PostTaxRatesTaxRate_params(msgspec.Struct):
    tax_rate: Optional[str] = None
    active: Optional[Any] = None
    country: Optional[Any] = None
    description: Optional[Any] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None
    jurisdiction: Optional[Any] = None
    metadata: Optional[Any] = None
    state: Optional[Any] = None
    tax_type: Optional[Any] = None

class GetTerminalConfigurations_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    is_account_default: Optional[bool] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostTerminalConfigurations_params(msgspec.Struct):
    bbpos_wisepos_e: Optional[Any] = None
    expand: Optional[Any] = None
    name: Optional[Any] = None
    offline: Optional[Any] = None
    reboot_window: Optional[Any] = None
    stripe_s700: Optional[Any] = None
    tipping: Optional[Any] = None
    verifone_p400: Optional[Any] = None
    wifi: Optional[Any] = None

class DeleteTerminalConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None

class GetTerminalConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    expand: Optional[List[str]] = None

class PostTerminalConfigurationsConfiguration_params(msgspec.Struct):
    configuration: Optional[str] = None
    bbpos_wisepos_e: Optional[Any] = None
    expand: Optional[Any] = None
    name: Optional[Any] = None
    offline: Optional[Any] = None
    reboot_window: Optional[Any] = None
    stripe_s700: Optional[Any] = None
    tipping: Optional[Any] = None
    verifone_p400: Optional[Any] = None
    wifi: Optional[Any] = None

class PostTerminalConnectionTokens_params(msgspec.Struct):
    expand: Optional[Any] = None
    location: Optional[Any] = None

class GetTerminalLocations_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostTerminalLocations_params(msgspec.Struct):
    address: Optional[Any] = None
    configuration_overrides: Optional[Any] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class DeleteTerminalLocationsLocation_params(msgspec.Struct):
    location: Optional[str] = None

class GetTerminalLocationsLocation_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    location: Optional[str] = None

class PostTerminalLocationsLocation_params(msgspec.Struct):
    location: Optional[str] = None
    address: Optional[Any] = None
    configuration_overrides: Optional[Any] = None
    display_name: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetTerminalReaders_params(msgspec.Struct):
    device_type: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    location: Optional[str] = None
    serial_number: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTerminalReaders_params(msgspec.Struct):
    expand: Optional[Any] = None
    label: Optional[Any] = None
    location: Optional[Any] = None
    metadata: Optional[Any] = None
    registration_code: Optional[Any] = None

class DeleteTerminalReadersReader_params(msgspec.Struct):
    reader: Optional[str] = None

class GetTerminalReadersReader_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    reader: Optional[str] = None

class PostTerminalReadersReader_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None
    label: Optional[Any] = None
    metadata: Optional[Any] = None

class PostTerminalReadersReaderCancelAction_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None

class PostTerminalReadersReaderCollectInputs_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None
    inputs: Optional[Any] = None
    metadata: Optional[Any] = None

class PostTerminalReadersReaderCollectPaymentMethod_params(msgspec.Struct):
    reader: Optional[str] = None
    collect_config: Optional[Any] = None
    expand: Optional[Any] = None
    payment_intent: Optional[Any] = None

class PostTerminalReadersReaderConfirmPaymentIntent_params(msgspec.Struct):
    reader: Optional[str] = None
    confirm_config: Optional[Any] = None
    expand: Optional[Any] = None
    payment_intent: Optional[Any] = None

class PostTerminalReadersReaderProcessPaymentIntent_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None
    payment_intent: Optional[Any] = None
    process_config: Optional[Any] = None

class PostTerminalReadersReaderProcessSetupIntent_params(msgspec.Struct):
    reader: Optional[str] = None
    allow_redisplay: Optional[Any] = None
    expand: Optional[Any] = None
    process_config: Optional[Any] = None
    setup_intent: Optional[Any] = None

class PostTerminalReadersReaderRefundPayment_params(msgspec.Struct):
    reader: Optional[str] = None
    amount: Optional[Any] = None
    charge: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    payment_intent: Optional[Any] = None
    refund_application_fee: Optional[Any] = None
    refund_payment_config: Optional[Any] = None
    reverse_transfer: Optional[Any] = None

class PostTerminalReadersReaderSetReaderDisplay_params(msgspec.Struct):
    reader: Optional[str] = None
    cart: Optional[Any] = None
    expand: Optional[Any] = None
    type: Optional[Any] = None

class PostTestHelpersConfirmationTokens_params(msgspec.Struct):
    expand: Optional[Any] = None
    payment_method: Optional[Any] = None
    payment_method_data: Optional[Any] = None
    payment_method_options: Optional[Any] = None
    return_url: Optional[Any] = None
    setup_future_usage: Optional[Any] = None
    shipping: Optional[Any] = None

class PostTestHelpersCustomersCustomerFundCashBalance_params(msgspec.Struct):
    customer: Optional[str] = None
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    reference: Optional[Any] = None

class PostTestHelpersIssuingAuthorizations_params(msgspec.Struct):
    amount: Optional[Any] = None
    amount_details: Optional[Any] = None
    authorization_method: Optional[Any] = None
    card: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    fleet: Optional[Any] = None
    fuel: Optional[Any] = None
    is_amount_controllable: Optional[Any] = None
    merchant_amount: Optional[Any] = None
    merchant_currency: Optional[Any] = None
    merchant_data: Optional[Any] = None
    network_data: Optional[Any] = None
    verification_data: Optional[Any] = None
    wallet: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationCapture_params(msgspec.Struct):
    authorization: Optional[str] = None
    capture_amount: Optional[Any] = None
    close_authorization: Optional[Any] = None
    expand: Optional[Any] = None
    purchase_details: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationExpire_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationFinalizeAmount_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None
    final_amount: Optional[Any] = None
    fleet: Optional[Any] = None
    fuel: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationFraudChallengesRespond_params(msgspec.Struct):
    authorization: Optional[str] = None
    confirmed: Optional[Any] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationIncrement_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None
    increment_amount: Optional[Any] = None
    is_amount_controllable: Optional[Any] = None

class PostTestHelpersIssuingAuthorizationsAuthorizationReverse_params(msgspec.Struct):
    authorization: Optional[str] = None
    expand: Optional[Any] = None
    reverse_amount: Optional[Any] = None

class PostTestHelpersIssuingCardsCardShippingDeliver_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingCardsCardShippingFail_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingCardsCardShippingReturn_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingCardsCardShippingShip_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingCardsCardShippingSubmit_params(msgspec.Struct):
    card: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignActivate_params(msgspec.Struct):
    personalization_design: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignDeactivate_params(msgspec.Struct):
    personalization_design: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignReject_params(msgspec.Struct):
    personalization_design: Optional[str] = None
    expand: Optional[Any] = None
    rejection_reasons: Optional[Any] = None

class PostTestHelpersIssuingSettlements_params(msgspec.Struct):
    bin: Optional[Any] = None
    clearing_date: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    interchange_fees_amount: Optional[Any] = None
    net_total_amount: Optional[Any] = None
    network: Optional[Any] = None
    network_settlement_identifier: Optional[Any] = None
    transaction_amount: Optional[Any] = None
    transaction_count: Optional[Any] = None

class PostTestHelpersIssuingSettlementsSettlementComplete_params(msgspec.Struct):
    settlement: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersIssuingTransactionsCreateForceCapture_params(msgspec.Struct):
    amount: Optional[Any] = None
    card: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    merchant_data: Optional[Any] = None
    purchase_details: Optional[Any] = None

class PostTestHelpersIssuingTransactionsCreateUnlinkedRefund_params(msgspec.Struct):
    amount: Optional[Any] = None
    card: Optional[Any] = None
    currency: Optional[Any] = None
    expand: Optional[Any] = None
    merchant_data: Optional[Any] = None
    purchase_details: Optional[Any] = None

class PostTestHelpersIssuingTransactionsTransactionRefund_params(msgspec.Struct):
    transaction: Optional[str] = None
    expand: Optional[Any] = None
    refund_amount: Optional[Any] = None

class PostTestHelpersRefundsRefundExpire_params(msgspec.Struct):
    refund: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTerminalReadersReaderPresentPaymentMethod_params(msgspec.Struct):
    reader: Optional[str] = None
    amount_tip: Optional[Any] = None
    card: Optional[Any] = None
    card_present: Optional[Any] = None
    expand: Optional[Any] = None
    interac_present: Optional[Any] = None
    type: Optional[Any] = None

class PostTestHelpersTerminalReadersReaderSucceedInputCollection_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None
    skip_non_required_inputs: Optional[Any] = None

class PostTestHelpersTerminalReadersReaderTimeoutInputCollection_params(msgspec.Struct):
    reader: Optional[str] = None
    expand: Optional[Any] = None

class GetTestHelpersTestClocks_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostTestHelpersTestClocks_params(msgspec.Struct):
    expand: Optional[Any] = None
    frozen_time: Optional[Any] = None
    name: Optional[Any] = None

class DeleteTestHelpersTestClocksTestClock_params(msgspec.Struct):
    test_clock: Optional[str] = None

class GetTestHelpersTestClocksTestClock_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    test_clock: Optional[str] = None

class PostTestHelpersTestClocksTestClockAdvance_params(msgspec.Struct):
    test_clock: Optional[str] = None
    expand: Optional[Any] = None
    frozen_time: Optional[Any] = None

class PostTestHelpersTreasuryInboundTransfersIdFail_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    failure_details: Optional[Any] = None

class PostTestHelpersTreasuryInboundTransfersIdReturn_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryInboundTransfersIdSucceed_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryOutboundPaymentsId_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    tracking_details: Optional[Any] = None

class PostTestHelpersTreasuryOutboundPaymentsIdFail_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryOutboundPaymentsIdPost_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryOutboundPaymentsIdReturn_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None
    returned_details: Optional[Any] = None

class PostTestHelpersTreasuryOutboundTransfersOutboundTransfer_params(msgspec.Struct):
    outbound_transfer: Optional[str] = None
    expand: Optional[Any] = None
    tracking_details: Optional[Any] = None

class PostTestHelpersTreasuryOutboundTransfersOutboundTransferFail_params(msgspec.Struct):
    outbound_transfer: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryOutboundTransfersOutboundTransferPost_params(msgspec.Struct):
    outbound_transfer: Optional[str] = None
    expand: Optional[Any] = None

class PostTestHelpersTreasuryOutboundTransfersOutboundTransferReturn_params(msgspec.Struct):
    outbound_transfer: Optional[str] = None
    expand: Optional[Any] = None
    returned_details: Optional[Any] = None

class PostTestHelpersTreasuryReceivedCredits_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    initiating_payment_method_details: Optional[Any] = None
    network: Optional[Any] = None

class PostTestHelpersTreasuryReceivedDebits_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    initiating_payment_method_details: Optional[Any] = None
    network: Optional[Any] = None

class PostTokens_params(msgspec.Struct):
    account: Optional[Any] = None
    bank_account: Optional[Any] = None
    card: Optional[Any] = None
    customer: Optional[Any] = None
    cvc_update: Optional[Any] = None
    expand: Optional[Any] = None
    person: Optional[Any] = None
    pii: Optional[Any] = None

class GetTokensToken_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    token: Optional[str] = None

class GetTopups_params(msgspec.Struct):
    amount: Optional[Any] = None
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTopups_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    source: Optional[Any] = None
    statement_descriptor: Optional[Any] = None
    transfer_group: Optional[Any] = None

class GetTopupsTopup_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    topup: Optional[str] = None

class PostTopupsTopup_params(msgspec.Struct):
    topup: Optional[str] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class PostTopupsTopupCancel_params(msgspec.Struct):
    topup: Optional[str] = None
    expand: Optional[Any] = None

class GetTransfers_params(msgspec.Struct):
    created: Optional[Any] = None
    destination: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    transfer_group: Optional[str] = None

class PostTransfers_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    destination: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    source_transaction: Optional[Any] = None
    source_type: Optional[Any] = None
    transfer_group: Optional[Any] = None

class GetTransfersIdReversals_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    id: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostTransfersIdReversals_params(msgspec.Struct):
    id: Optional[str] = None
    amount: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    refund_application_fee: Optional[Any] = None

class GetTransfersTransfer_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    transfer: Optional[str] = None

class PostTransfersTransfer_params(msgspec.Struct):
    transfer: Optional[str] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetTransfersTransferReversalsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None
    transfer: Optional[str] = None

class PostTransfersTransferReversalsId_params(msgspec.Struct):
    id: Optional[str] = None
    transfer: Optional[str] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None

class GetTreasuryCreditReversals_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    received_credit: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryCreditReversals_params(msgspec.Struct):
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    received_credit: Optional[Any] = None

class GetTreasuryCreditReversalsCreditReversal_params(msgspec.Struct):
    credit_reversal: Optional[str] = None
    expand: Optional[List[str]] = None

class GetTreasuryDebitReversals_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    received_debit: Optional[str] = None
    resolution: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryDebitReversals_params(msgspec.Struct):
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    received_debit: Optional[Any] = None

class GetTreasuryDebitReversalsDebitReversal_params(msgspec.Struct):
    debit_reversal: Optional[str] = None
    expand: Optional[List[str]] = None

class GetTreasuryFinancialAccounts_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryFinancialAccounts_params(msgspec.Struct):
    expand: Optional[Any] = None
    features: Optional[Any] = None
    metadata: Optional[Any] = None
    nickname: Optional[Any] = None
    platform_restrictions: Optional[Any] = None
    supported_currencies: Optional[Any] = None

class GetTreasuryFinancialAccountsFinancialAccount_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None

class PostTreasuryFinancialAccountsFinancialAccount_params(msgspec.Struct):
    financial_account: Optional[str] = None
    expand: Optional[Any] = None
    features: Optional[Any] = None
    forwarding_settings: Optional[Any] = None
    metadata: Optional[Any] = None
    nickname: Optional[Any] = None
    platform_restrictions: Optional[Any] = None

class PostTreasuryFinancialAccountsFinancialAccountClose_params(msgspec.Struct):
    financial_account: Optional[str] = None
    expand: Optional[Any] = None
    forwarding_settings: Optional[Any] = None

class GetTreasuryFinancialAccountsFinancialAccountFeatures_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None

class PostTreasuryFinancialAccountsFinancialAccountFeatures_params(msgspec.Struct):
    financial_account: Optional[str] = None
    card_issuing: Optional[Any] = None
    deposit_insurance: Optional[Any] = None
    expand: Optional[Any] = None
    financial_addresses: Optional[Any] = None
    inbound_transfers: Optional[Any] = None
    intra_stripe_flows: Optional[Any] = None
    outbound_payments: Optional[Any] = None
    outbound_transfers: Optional[Any] = None

class GetTreasuryInboundTransfers_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryInboundTransfers_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    metadata: Optional[Any] = None
    origin_payment_method: Optional[Any] = None
    statement_descriptor: Optional[Any] = None

class GetTreasuryInboundTransfersId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostTreasuryInboundTransfersInboundTransferCancel_params(msgspec.Struct):
    inbound_transfer: Optional[str] = None
    expand: Optional[Any] = None

class GetTreasuryOutboundPayments_params(msgspec.Struct):
    created: Optional[Any] = None
    customer: Optional[str] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryOutboundPayments_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    customer: Optional[Any] = None
    description: Optional[Any] = None
    destination_payment_method: Optional[Any] = None
    destination_payment_method_data: Optional[Any] = None
    destination_payment_method_options: Optional[Any] = None
    end_user_details: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    metadata: Optional[Any] = None
    statement_descriptor: Optional[Any] = None

class GetTreasuryOutboundPaymentsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class PostTreasuryOutboundPaymentsIdCancel_params(msgspec.Struct):
    id: Optional[str] = None
    expand: Optional[Any] = None

class GetTreasuryOutboundTransfers_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class PostTreasuryOutboundTransfers_params(msgspec.Struct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    description: Optional[Any] = None
    destination_payment_method: Optional[Any] = None
    destination_payment_method_data: Optional[Any] = None
    destination_payment_method_options: Optional[Any] = None
    expand: Optional[Any] = None
    financial_account: Optional[Any] = None
    metadata: Optional[Any] = None
    statement_descriptor: Optional[Any] = None

class GetTreasuryOutboundTransfersOutboundTransfer_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    outbound_transfer: Optional[str] = None

class PostTreasuryOutboundTransfersOutboundTransferCancel_params(msgspec.Struct):
    outbound_transfer: Optional[str] = None
    expand: Optional[Any] = None

class GetTreasuryReceivedCredits_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    linked_flows: Optional[Dict[str, Any]] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetTreasuryReceivedCreditsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetTreasuryReceivedDebits_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None

class GetTreasuryReceivedDebitsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetTreasuryTransactionEntries_params(msgspec.Struct):
    created: Optional[Any] = None
    effective_at: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    order_by: Optional[str] = None
    starting_after: Optional[str] = None
    transaction: Optional[str] = None

class GetTreasuryTransactionEntriesId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetTreasuryTransactions_params(msgspec.Struct):
    created: Optional[Any] = None
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    financial_account: Optional[str] = None
    limit: Optional[int] = None
    order_by: Optional[str] = None
    starting_after: Optional[str] = None
    status: Optional[str] = None
    status_transitions: Optional[Dict[str, Any]] = None

class GetTreasuryTransactionsId_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    id: Optional[str] = None

class GetWebhookEndpoints_params(msgspec.Struct):
    ending_before: Optional[str] = None
    expand: Optional[List[str]] = None
    limit: Optional[int] = None
    starting_after: Optional[str] = None

class PostWebhookEndpoints_params(msgspec.Struct):
    api_version: Optional[Any] = None
    connect: Optional[Any] = None
    description: Optional[Any] = None
    enabled_events: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    url: Optional[Any] = None

class DeleteWebhookEndpointsWebhookEndpoint_params(msgspec.Struct):
    webhook_endpoint: Optional[str] = None

class GetWebhookEndpointsWebhookEndpoint_params(msgspec.Struct):
    expand: Optional[List[str]] = None
    webhook_endpoint: Optional[str] = None

class PostWebhookEndpointsWebhookEndpoint_params(msgspec.Struct):
    webhook_endpoint: Optional[str] = None
    description: Optional[Any] = None
    disabled: Optional[Any] = None
    enabled_events: Optional[Any] = None
    expand: Optional[Any] = None
    metadata: Optional[Any] = None
    url: Optional[Any] = None
