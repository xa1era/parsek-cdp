"""Custom types and enums for the Audits domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..network.types import ClientSecurityState as Network_ClientSecurityState
    from ..network.types import CorsErrorStatus as Network_CorsErrorStatus
    from ..network.types import IPAddressSpace as Network_IPAddressSpace
    from ..network.types import LoaderId as Network_LoaderId
    from ..network.types import RequestId as Network_RequestId
    from ..page.types import FrameId as Page_FrameId
    from ..runtime.types import ScriptId as Runtime_ScriptId

@register("Audits.AffectedCookie")
@dataclass
class AffectedCookie(DataType):
    """Information about a cookie that is affected by an inspector issue."""
    name: str
    path: str
    domain: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('path', 'path', False, 'primitive'),
        FieldMeta('domain', 'domain', False, 'primitive'),
    )


@register("Audits.AffectedRequest")
@dataclass
class AffectedRequest(DataType):
    """Information about a request that is affected by an inspector issue."""
    url: str
    request_id: Optional[Network_RequestId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('request_id', 'requestId', True, 'primitive'),
    )


@register("Audits.AffectedFrame")
@dataclass
class AffectedFrame(DataType):
    """Information about the frame affected by an inspector issue."""
    frame_id: Page_FrameId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
    )


@register("Audits.CookieExclusionReason")
class CookieExclusionReason(str, Enum):
    EXCLUDESAMESITEUNSPECIFIEDTREATEDASLAX = 'ExcludeSameSiteUnspecifiedTreatedAsLax'
    EXCLUDESAMESITENONEINSECURE = 'ExcludeSameSiteNoneInsecure'
    EXCLUDESAMESITELAX = 'ExcludeSameSiteLax'
    EXCLUDESAMESITESTRICT = 'ExcludeSameSiteStrict'
    EXCLUDEINVALIDSAMEPARTY = 'ExcludeInvalidSameParty'
    EXCLUDESAMEPARTYCROSSPARTYCONTEXT = 'ExcludeSamePartyCrossPartyContext'
    EXCLUDEDOMAINNONASCII = 'ExcludeDomainNonASCII'
    EXCLUDETHIRDPARTYCOOKIEBLOCKEDINFIRSTPARTYSET = 'ExcludeThirdPartyCookieBlockedInFirstPartySet'
    EXCLUDETHIRDPARTYPHASEOUT = 'ExcludeThirdPartyPhaseout'
    EXCLUDEPORTMISMATCH = 'ExcludePortMismatch'
    EXCLUDESCHEMEMISMATCH = 'ExcludeSchemeMismatch'


@register("Audits.CookieWarningReason")
class CookieWarningReason(str, Enum):
    WARNSAMESITEUNSPECIFIEDCROSSSITECONTEXT = 'WarnSameSiteUnspecifiedCrossSiteContext'
    WARNSAMESITENONEINSECURE = 'WarnSameSiteNoneInsecure'
    WARNSAMESITEUNSPECIFIEDLAXALLOWUNSAFE = 'WarnSameSiteUnspecifiedLaxAllowUnsafe'
    WARNSAMESITESTRICTLAXDOWNGRADESTRICT = 'WarnSameSiteStrictLaxDowngradeStrict'
    WARNSAMESITESTRICTCROSSDOWNGRADESTRICT = 'WarnSameSiteStrictCrossDowngradeStrict'
    WARNSAMESITESTRICTCROSSDOWNGRADELAX = 'WarnSameSiteStrictCrossDowngradeLax'
    WARNSAMESITELAXCROSSDOWNGRADESTRICT = 'WarnSameSiteLaxCrossDowngradeStrict'
    WARNSAMESITELAXCROSSDOWNGRADELAX = 'WarnSameSiteLaxCrossDowngradeLax'
    WARNATTRIBUTEVALUEEXCEEDSMAXSIZE = 'WarnAttributeValueExceedsMaxSize'
    WARNDOMAINNONASCII = 'WarnDomainNonASCII'
    WARNTHIRDPARTYPHASEOUT = 'WarnThirdPartyPhaseout'
    WARNCROSSSITEREDIRECTDOWNGRADECHANGESINCLUSION = 'WarnCrossSiteRedirectDowngradeChangesInclusion'
    WARNDEPRECATIONTRIALMETADATA = 'WarnDeprecationTrialMetadata'
    WARNTHIRDPARTYCOOKIEHEURISTIC = 'WarnThirdPartyCookieHeuristic'


@register("Audits.CookieOperation")
class CookieOperation(str, Enum):
    SETCOOKIE = 'SetCookie'
    READCOOKIE = 'ReadCookie'


@register("Audits.InsightType")
class InsightType(str, Enum):
    """Represents the category of insight that a cookie issue falls under."""
    GITHUBRESOURCE = 'GitHubResource'
    GRACEPERIOD = 'GracePeriod'
    HEURISTICS = 'Heuristics'


@register("Audits.CookieIssueInsight")
@dataclass
class CookieIssueInsight(DataType):
    """Information about the suggested solution to a cookie issue."""
    type_: InsightType
    table_entry_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Audits.InsightType'),
        FieldMeta('table_entry_url', 'tableEntryUrl', True, 'primitive'),
    )


@register("Audits.CookieIssueDetails")
@dataclass
class CookieIssueDetails(DataType):
    """
    This information is currently necessary, as the front-end has a difficult
    time finding a specific cookie. With this, we can convey specific error
    information without the cookie.
    """
    cookie_warning_reasons: List[CookieWarningReason]
    cookie_exclusion_reasons: List[CookieExclusionReason]
    operation: CookieOperation
    cookie: Optional[AffectedCookie] = None
    raw_cookie_line: Optional[str] = None
    site_for_cookies: Optional[str] = None
    cookie_url: Optional[str] = None
    request: Optional[AffectedRequest] = None
    insight: Optional[CookieIssueInsight] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookie_warning_reasons', 'cookieWarningReasons', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Audits.CookieWarningReason')),
        FieldMeta('cookie_exclusion_reasons', 'cookieExclusionReasons', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Audits.CookieExclusionReason')),
        FieldMeta('operation', 'operation', False, 'enum', ref='Audits.CookieOperation'),
        FieldMeta('cookie', 'cookie', True, 'object', ref='Audits.AffectedCookie'),
        FieldMeta('raw_cookie_line', 'rawCookieLine', True, 'primitive'),
        FieldMeta('site_for_cookies', 'siteForCookies', True, 'primitive'),
        FieldMeta('cookie_url', 'cookieUrl', True, 'primitive'),
        FieldMeta('request', 'request', True, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('insight', 'insight', True, 'object', ref='Audits.CookieIssueInsight'),
    )


@register("Audits.MixedContentResolutionStatus")
class MixedContentResolutionStatus(str, Enum):
    MIXEDCONTENTBLOCKED = 'MixedContentBlocked'
    MIXEDCONTENTAUTOMATICALLYUPGRADED = 'MixedContentAutomaticallyUpgraded'
    MIXEDCONTENTWARNING = 'MixedContentWarning'


@register("Audits.MixedContentResourceType")
class MixedContentResourceType(str, Enum):
    ATTRIBUTIONSRC = 'AttributionSrc'
    AUDIO = 'Audio'
    BEACON = 'Beacon'
    CSPREPORT = 'CSPReport'
    DOWNLOAD = 'Download'
    EVENTSOURCE = 'EventSource'
    FAVICON = 'Favicon'
    FONT = 'Font'
    FORM = 'Form'
    FRAME = 'Frame'
    IMAGE = 'Image'
    IMPORT = 'Import'
    JSON = 'JSON'
    MANIFEST = 'Manifest'
    PING = 'Ping'
    PLUGINDATA = 'PluginData'
    PLUGINRESOURCE = 'PluginResource'
    PREFETCH = 'Prefetch'
    RESOURCE = 'Resource'
    SCRIPT = 'Script'
    SERVICEWORKER = 'ServiceWorker'
    SHAREDWORKER = 'SharedWorker'
    SPECULATIONRULES = 'SpeculationRules'
    STYLESHEET = 'Stylesheet'
    TRACK = 'Track'
    VIDEO = 'Video'
    WORKER = 'Worker'
    XMLHTTPREQUEST = 'XMLHttpRequest'
    XSLT = 'XSLT'


@register("Audits.MixedContentIssueDetails")
@dataclass
class MixedContentIssueDetails(DataType):
    resolution_status: MixedContentResolutionStatus
    insecure_url: str
    main_resource_url: str
    resource_type: Optional[MixedContentResourceType] = None
    request: Optional[AffectedRequest] = None
    frame: Optional[AffectedFrame] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('resolution_status', 'resolutionStatus', False, 'enum', ref='Audits.MixedContentResolutionStatus'),
        FieldMeta('insecure_url', 'insecureURL', False, 'primitive'),
        FieldMeta('main_resource_url', 'mainResourceURL', False, 'primitive'),
        FieldMeta('resource_type', 'resourceType', True, 'enum', ref='Audits.MixedContentResourceType'),
        FieldMeta('request', 'request', True, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('frame', 'frame', True, 'object', ref='Audits.AffectedFrame'),
    )


@register("Audits.BlockedByResponseReason")
class BlockedByResponseReason(str, Enum):
    """
    Enum indicating the reason a response has been blocked. These reasons are
    refinements of the net error BLOCKED_BY_RESPONSE.
    """
    COEPFRAMERESOURCENEEDSCOEPHEADER = 'CoepFrameResourceNeedsCoepHeader'
    COOPSANDBOXEDIFRAMECANNOTNAVIGATETOCOOPPAGE = 'CoopSandboxedIFrameCannotNavigateToCoopPage'
    CORPNOTSAMEORIGIN = 'CorpNotSameOrigin'
    CORPNOTSAMEORIGINAFTERDEFAULTEDTOSAMEORIGINBYCOEP = 'CorpNotSameOriginAfterDefaultedToSameOriginByCoep'
    CORPNOTSAMEORIGINAFTERDEFAULTEDTOSAMEORIGINBYDIP = 'CorpNotSameOriginAfterDefaultedToSameOriginByDip'
    CORPNOTSAMEORIGINAFTERDEFAULTEDTOSAMEORIGINBYCOEPANDDIP = 'CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip'
    CORPNOTSAMESITE = 'CorpNotSameSite'
    SRIMESSAGESIGNATUREMISMATCH = 'SRIMessageSignatureMismatch'


@register("Audits.BlockedByResponseIssueDetails")
@dataclass
class BlockedByResponseIssueDetails(DataType):
    """
    Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
    code. Currently only used for COEP/COOP, but may be extended to include
    some CSP errors in the future.
    """
    request: AffectedRequest
    reason: BlockedByResponseReason
    parent_frame: Optional[AffectedFrame] = None
    blocked_frame: Optional[AffectedFrame] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('request', 'request', False, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('reason', 'reason', False, 'enum', ref='Audits.BlockedByResponseReason'),
        FieldMeta('parent_frame', 'parentFrame', True, 'object', ref='Audits.AffectedFrame'),
        FieldMeta('blocked_frame', 'blockedFrame', True, 'object', ref='Audits.AffectedFrame'),
    )


@register("Audits.HeavyAdResolutionStatus")
class HeavyAdResolutionStatus(str, Enum):
    HEAVYADBLOCKED = 'HeavyAdBlocked'
    HEAVYADWARNING = 'HeavyAdWarning'


@register("Audits.HeavyAdReason")
class HeavyAdReason(str, Enum):
    NETWORKTOTALLIMIT = 'NetworkTotalLimit'
    CPUTOTALLIMIT = 'CpuTotalLimit'
    CPUPEAKLIMIT = 'CpuPeakLimit'


@register("Audits.HeavyAdIssueDetails")
@dataclass
class HeavyAdIssueDetails(DataType):
    resolution: HeavyAdResolutionStatus
    reason: HeavyAdReason
    frame: AffectedFrame
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('resolution', 'resolution', False, 'enum', ref='Audits.HeavyAdResolutionStatus'),
        FieldMeta('reason', 'reason', False, 'enum', ref='Audits.HeavyAdReason'),
        FieldMeta('frame', 'frame', False, 'object', ref='Audits.AffectedFrame'),
    )


@register("Audits.ContentSecurityPolicyViolationType")
class ContentSecurityPolicyViolationType(str, Enum):
    KINLINEVIOLATION = 'kInlineViolation'
    KEVALVIOLATION = 'kEvalViolation'
    KURLVIOLATION = 'kURLViolation'
    KSRIVIOLATION = 'kSRIViolation'
    KTRUSTEDTYPESSINKVIOLATION = 'kTrustedTypesSinkViolation'
    KTRUSTEDTYPESPOLICYVIOLATION = 'kTrustedTypesPolicyViolation'
    KWASMEVALVIOLATION = 'kWasmEvalViolation'


@register("Audits.SourceCodeLocation")
@dataclass
class SourceCodeLocation(DataType):
    url: str
    line_number: int
    column_number: int
    script_id: Optional[Runtime_ScriptId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
        FieldMeta('script_id', 'scriptId', True, 'primitive'),
    )


@register("Audits.ContentSecurityPolicyIssueDetails")
@dataclass
class ContentSecurityPolicyIssueDetails(DataType):
    violated_directive: str
    is_report_only: bool
    content_security_policy_violation_type: ContentSecurityPolicyViolationType
    blocked_url: Optional[str] = None
    frame_ancestor: Optional[AffectedFrame] = None
    source_code_location: Optional[SourceCodeLocation] = None
    violating_node_id: Optional[DOM_BackendNodeId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('violated_directive', 'violatedDirective', False, 'primitive'),
        FieldMeta('is_report_only', 'isReportOnly', False, 'primitive'),
        FieldMeta('content_security_policy_violation_type', 'contentSecurityPolicyViolationType', False, 'enum', ref='Audits.ContentSecurityPolicyViolationType'),
        FieldMeta('blocked_url', 'blockedURL', True, 'primitive'),
        FieldMeta('frame_ancestor', 'frameAncestor', True, 'object', ref='Audits.AffectedFrame'),
        FieldMeta('source_code_location', 'sourceCodeLocation', True, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('violating_node_id', 'violatingNodeId', True, 'primitive'),
    )


@register("Audits.SharedArrayBufferIssueType")
class SharedArrayBufferIssueType(str, Enum):
    TRANSFERISSUE = 'TransferIssue'
    CREATIONISSUE = 'CreationIssue'


@register("Audits.SharedArrayBufferIssueDetails")
@dataclass
class SharedArrayBufferIssueDetails(DataType):
    """
    Details for a issue arising from an SAB being instantiated in, or
    transferred to a context that is not cross-origin isolated.
    """
    source_code_location: SourceCodeLocation
    is_warning: bool
    type_: SharedArrayBufferIssueType
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_code_location', 'sourceCodeLocation', False, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('is_warning', 'isWarning', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Audits.SharedArrayBufferIssueType'),
    )


@register("Audits.LowTextContrastIssueDetails")
@dataclass
class LowTextContrastIssueDetails(DataType):
    violating_node_id: DOM_BackendNodeId
    violating_node_selector: str
    contrast_ratio: float
    threshold_aa: float
    threshold_aaa: float
    font_size: str
    font_weight: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('violating_node_id', 'violatingNodeId', False, 'primitive'),
        FieldMeta('violating_node_selector', 'violatingNodeSelector', False, 'primitive'),
        FieldMeta('contrast_ratio', 'contrastRatio', False, 'primitive'),
        FieldMeta('threshold_aa', 'thresholdAA', False, 'primitive'),
        FieldMeta('threshold_aaa', 'thresholdAAA', False, 'primitive'),
        FieldMeta('font_size', 'fontSize', False, 'primitive'),
        FieldMeta('font_weight', 'fontWeight', False, 'primitive'),
    )


@register("Audits.CorsIssueDetails")
@dataclass
class CorsIssueDetails(DataType):
    """
    Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement.
    """
    cors_error_status: Network_CorsErrorStatus
    is_warning: bool
    request: AffectedRequest
    location: Optional[SourceCodeLocation] = None
    initiator_origin: Optional[str] = None
    resource_ip_address_space: Optional[Network_IPAddressSpace] = None
    client_security_state: Optional[Network_ClientSecurityState] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cors_error_status', 'corsErrorStatus', False, 'object', ref='Network.CorsErrorStatus'),
        FieldMeta('is_warning', 'isWarning', False, 'primitive'),
        FieldMeta('request', 'request', False, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('location', 'location', True, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('initiator_origin', 'initiatorOrigin', True, 'primitive'),
        FieldMeta('resource_ip_address_space', 'resourceIPAddressSpace', True, 'enum', ref='Network.IPAddressSpace'),
        FieldMeta('client_security_state', 'clientSecurityState', True, 'object', ref='Network.ClientSecurityState'),
    )


@register("Audits.AttributionReportingIssueType")
class AttributionReportingIssueType(str, Enum):
    PERMISSIONPOLICYDISABLED = 'PermissionPolicyDisabled'
    UNTRUSTWORTHYREPORTINGORIGIN = 'UntrustworthyReportingOrigin'
    INSECURECONTEXT = 'InsecureContext'
    INVALIDHEADER = 'InvalidHeader'
    INVALIDREGISTERTRIGGERHEADER = 'InvalidRegisterTriggerHeader'
    SOURCEANDTRIGGERHEADERS = 'SourceAndTriggerHeaders'
    SOURCEIGNORED = 'SourceIgnored'
    TRIGGERIGNORED = 'TriggerIgnored'
    OSSOURCEIGNORED = 'OsSourceIgnored'
    OSTRIGGERIGNORED = 'OsTriggerIgnored'
    INVALIDREGISTEROSSOURCEHEADER = 'InvalidRegisterOsSourceHeader'
    INVALIDREGISTEROSTRIGGERHEADER = 'InvalidRegisterOsTriggerHeader'
    WEBANDOSHEADERS = 'WebAndOsHeaders'
    NOWEBOROSSUPPORT = 'NoWebOrOsSupport'
    NAVIGATIONREGISTRATIONWITHOUTTRANSIENTUSERACTIVATION = 'NavigationRegistrationWithoutTransientUserActivation'
    INVALIDINFOHEADER = 'InvalidInfoHeader'
    NOREGISTERSOURCEHEADER = 'NoRegisterSourceHeader'
    NOREGISTERTRIGGERHEADER = 'NoRegisterTriggerHeader'
    NOREGISTEROSSOURCEHEADER = 'NoRegisterOsSourceHeader'
    NOREGISTEROSTRIGGERHEADER = 'NoRegisterOsTriggerHeader'
    NAVIGATIONREGISTRATIONUNIQUESCOPEALREADYSET = 'NavigationRegistrationUniqueScopeAlreadySet'


@register("Audits.SharedDictionaryError")
class SharedDictionaryError(str, Enum):
    USEERRORCROSSORIGINNOCORSREQUEST = 'UseErrorCrossOriginNoCorsRequest'
    USEERRORDICTIONARYLOADFAILURE = 'UseErrorDictionaryLoadFailure'
    USEERRORMATCHINGDICTIONARYNOTUSED = 'UseErrorMatchingDictionaryNotUsed'
    USEERRORUNEXPECTEDCONTENTDICTIONARYHEADER = 'UseErrorUnexpectedContentDictionaryHeader'
    WRITEERRORCOSSORIGINNOCORSREQUEST = 'WriteErrorCossOriginNoCorsRequest'
    WRITEERRORDISALLOWEDBYSETTINGS = 'WriteErrorDisallowedBySettings'
    WRITEERROREXPIREDRESPONSE = 'WriteErrorExpiredResponse'
    WRITEERRORFEATUREDISABLED = 'WriteErrorFeatureDisabled'
    WRITEERRORINSUFFICIENTRESOURCES = 'WriteErrorInsufficientResources'
    WRITEERRORINVALIDMATCHFIELD = 'WriteErrorInvalidMatchField'
    WRITEERRORINVALIDSTRUCTUREDHEADER = 'WriteErrorInvalidStructuredHeader'
    WRITEERRORINVALIDTTLFIELD = 'WriteErrorInvalidTTLField'
    WRITEERRORNAVIGATIONREQUEST = 'WriteErrorNavigationRequest'
    WRITEERRORNOMATCHFIELD = 'WriteErrorNoMatchField'
    WRITEERRORNONINTEGERTTLFIELD = 'WriteErrorNonIntegerTTLField'
    WRITEERRORNONLISTMATCHDESTFIELD = 'WriteErrorNonListMatchDestField'
    WRITEERRORNONSECURECONTEXT = 'WriteErrorNonSecureContext'
    WRITEERRORNONSTRINGIDFIELD = 'WriteErrorNonStringIdField'
    WRITEERRORNONSTRINGINMATCHDESTLIST = 'WriteErrorNonStringInMatchDestList'
    WRITEERRORNONSTRINGMATCHFIELD = 'WriteErrorNonStringMatchField'
    WRITEERRORNONTOKENTYPEFIELD = 'WriteErrorNonTokenTypeField'
    WRITEERRORREQUESTABORTED = 'WriteErrorRequestAborted'
    WRITEERRORSHUTTINGDOWN = 'WriteErrorShuttingDown'
    WRITEERRORTOOLONGIDFIELD = 'WriteErrorTooLongIdField'
    WRITEERRORUNSUPPORTEDTYPE = 'WriteErrorUnsupportedType'


@register("Audits.SRIMessageSignatureError")
class SRIMessageSignatureError(str, Enum):
    MISSINGSIGNATUREHEADER = 'MissingSignatureHeader'
    MISSINGSIGNATUREINPUTHEADER = 'MissingSignatureInputHeader'
    INVALIDSIGNATUREHEADER = 'InvalidSignatureHeader'
    INVALIDSIGNATUREINPUTHEADER = 'InvalidSignatureInputHeader'
    SIGNATUREHEADERVALUEISNOTBYTESEQUENCE = 'SignatureHeaderValueIsNotByteSequence'
    SIGNATUREHEADERVALUEISPARAMETERIZED = 'SignatureHeaderValueIsParameterized'
    SIGNATUREHEADERVALUEISINCORRECTLENGTH = 'SignatureHeaderValueIsIncorrectLength'
    SIGNATUREINPUTHEADERMISSINGLABEL = 'SignatureInputHeaderMissingLabel'
    SIGNATUREINPUTHEADERVALUENOTINNERLIST = 'SignatureInputHeaderValueNotInnerList'
    SIGNATUREINPUTHEADERVALUEMISSINGCOMPONENTS = 'SignatureInputHeaderValueMissingComponents'
    SIGNATUREINPUTHEADERINVALIDCOMPONENTTYPE = 'SignatureInputHeaderInvalidComponentType'
    SIGNATUREINPUTHEADERINVALIDCOMPONENTNAME = 'SignatureInputHeaderInvalidComponentName'
    SIGNATUREINPUTHEADERINVALIDHEADERCOMPONENTPARAMETER = 'SignatureInputHeaderInvalidHeaderComponentParameter'
    SIGNATUREINPUTHEADERINVALIDDERIVEDCOMPONENTPARAMETER = 'SignatureInputHeaderInvalidDerivedComponentParameter'
    SIGNATUREINPUTHEADERKEYIDLENGTH = 'SignatureInputHeaderKeyIdLength'
    SIGNATUREINPUTHEADERINVALIDPARAMETER = 'SignatureInputHeaderInvalidParameter'
    SIGNATUREINPUTHEADERMISSINGREQUIREDPARAMETERS = 'SignatureInputHeaderMissingRequiredParameters'
    VALIDATIONFAILEDSIGNATUREEXPIRED = 'ValidationFailedSignatureExpired'
    VALIDATIONFAILEDINVALIDLENGTH = 'ValidationFailedInvalidLength'
    VALIDATIONFAILEDSIGNATUREMISMATCH = 'ValidationFailedSignatureMismatch'
    VALIDATIONFAILEDINTEGRITYMISMATCH = 'ValidationFailedIntegrityMismatch'


@register("Audits.UnencodedDigestError")
class UnencodedDigestError(str, Enum):
    MALFORMEDDICTIONARY = 'MalformedDictionary'
    UNKNOWNALGORITHM = 'UnknownAlgorithm'
    INCORRECTDIGESTTYPE = 'IncorrectDigestType'
    INCORRECTDIGESTLENGTH = 'IncorrectDigestLength'


@register("Audits.AttributionReportingIssueDetails")
@dataclass
class AttributionReportingIssueDetails(DataType):
    """
    Details for issues around "Attribution Reporting API" usage.
    Explainer: https://github.com/WICG/attribution-reporting-api
    """
    violation_type: AttributionReportingIssueType
    request: Optional[AffectedRequest] = None
    violating_node_id: Optional[DOM_BackendNodeId] = None
    invalid_parameter: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('violation_type', 'violationType', False, 'enum', ref='Audits.AttributionReportingIssueType'),
        FieldMeta('request', 'request', True, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('violating_node_id', 'violatingNodeId', True, 'primitive'),
        FieldMeta('invalid_parameter', 'invalidParameter', True, 'primitive'),
    )


@register("Audits.QuirksModeIssueDetails")
@dataclass
class QuirksModeIssueDetails(DataType):
    """
    Details for issues about documents in Quirks Mode
    or Limited Quirks Mode that affects page layouting.
    """
    is_limited_quirks_mode: bool
    document_node_id: DOM_BackendNodeId
    url: str
    frame_id: Page_FrameId
    loader_id: Network_LoaderId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('is_limited_quirks_mode', 'isLimitedQuirksMode', False, 'primitive'),
        FieldMeta('document_node_id', 'documentNodeId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
    )


@register("Audits.NavigatorUserAgentIssueDetails")
@dataclass
class NavigatorUserAgentIssueDetails(DataType):
    url: str
    location: Optional[SourceCodeLocation] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('location', 'location', True, 'object', ref='Audits.SourceCodeLocation'),
    )


@register("Audits.SharedDictionaryIssueDetails")
@dataclass
class SharedDictionaryIssueDetails(DataType):
    shared_dictionary_error: SharedDictionaryError
    request: AffectedRequest
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('shared_dictionary_error', 'sharedDictionaryError', False, 'enum', ref='Audits.SharedDictionaryError'),
        FieldMeta('request', 'request', False, 'object', ref='Audits.AffectedRequest'),
    )


@register("Audits.SRIMessageSignatureIssueDetails")
@dataclass
class SRIMessageSignatureIssueDetails(DataType):
    error: SRIMessageSignatureError
    signature_base: str
    integrity_assertions: List[str]
    request: AffectedRequest
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error', 'error', False, 'enum', ref='Audits.SRIMessageSignatureError'),
        FieldMeta('signature_base', 'signatureBase', False, 'primitive'),
        FieldMeta('integrity_assertions', 'integrityAssertions', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('request', 'request', False, 'object', ref='Audits.AffectedRequest'),
    )


@register("Audits.UnencodedDigestIssueDetails")
@dataclass
class UnencodedDigestIssueDetails(DataType):
    error: UnencodedDigestError
    request: AffectedRequest
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error', 'error', False, 'enum', ref='Audits.UnencodedDigestError'),
        FieldMeta('request', 'request', False, 'object', ref='Audits.AffectedRequest'),
    )


@register("Audits.GenericIssueErrorType")
class GenericIssueErrorType(str, Enum):
    FORMLABELFORNAMEERROR = 'FormLabelForNameError'
    FORMDUPLICATEIDFORINPUTERROR = 'FormDuplicateIdForInputError'
    FORMINPUTWITHNOLABELERROR = 'FormInputWithNoLabelError'
    FORMAUTOCOMPLETEATTRIBUTEEMPTYERROR = 'FormAutocompleteAttributeEmptyError'
    FORMEMPTYIDANDNAMEATTRIBUTESFORINPUTERROR = 'FormEmptyIdAndNameAttributesForInputError'
    FORMARIALABELLEDBYTONONEXISTINGIDERROR = 'FormAriaLabelledByToNonExistingIdError'
    FORMINPUTASSIGNEDAUTOCOMPLETEVALUETOIDORNAMEATTRIBUTEERROR = 'FormInputAssignedAutocompleteValueToIdOrNameAttributeError'
    FORMLABELHASNEITHERFORNORNESTEDINPUTERROR = 'FormLabelHasNeitherForNorNestedInputError'
    FORMLABELFORMATCHESNONEXISTINGIDERROR = 'FormLabelForMatchesNonExistingIdError'
    FORMINPUTHASWRONGBUTWELLINTENDEDAUTOCOMPLETEVALUEERROR = 'FormInputHasWrongButWellIntendedAutocompleteValueError'
    RESPONSEWASBLOCKEDBYORB = 'ResponseWasBlockedByORB'
    NAVIGATIONENTRYMARKEDSKIPPABLE = 'NavigationEntryMarkedSkippable'


@register("Audits.GenericIssueDetails")
@dataclass
class GenericIssueDetails(DataType):
    """Depending on the concrete errorType, different properties are set."""
    error_type: GenericIssueErrorType
    frame_id: Optional[Page_FrameId] = None
    violating_node_id: Optional[DOM_BackendNodeId] = None
    violating_node_attribute: Optional[str] = None
    request: Optional[AffectedRequest] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error_type', 'errorType', False, 'enum', ref='Audits.GenericIssueErrorType'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
        FieldMeta('violating_node_id', 'violatingNodeId', True, 'primitive'),
        FieldMeta('violating_node_attribute', 'violatingNodeAttribute', True, 'primitive'),
        FieldMeta('request', 'request', True, 'object', ref='Audits.AffectedRequest'),
    )


@register("Audits.DeprecationIssueDetails")
@dataclass
class DeprecationIssueDetails(DataType):
    """
    This issue tracks information needed to print a deprecation message.
    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """
    source_code_location: SourceCodeLocation
    type_: str
    affected_frame: Optional[AffectedFrame] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_code_location', 'sourceCodeLocation', False, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('affected_frame', 'affectedFrame', True, 'object', ref='Audits.AffectedFrame'),
    )


@register("Audits.BounceTrackingIssueDetails")
@dataclass
class BounceTrackingIssueDetails(DataType):
    """
    This issue warns about sites in the redirect chain of a finished navigation
    that may be flagged as trackers and have their state cleared if they don't
    receive a user interaction. Note that in this context 'site' means eTLD+1.
    For example, if the URL `https://example.test:80/bounce` was in the
    redirect chain, the site reported would be `example.test`.
    """
    tracking_sites: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('tracking_sites', 'trackingSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Audits.CookieDeprecationMetadataIssueDetails")
@dataclass
class CookieDeprecationMetadataIssueDetails(DataType):
    """
    This issue warns about third-party sites that are accessing cookies on the
    current page, and have been permitted due to having a global metadata grant.
    Note that in this context 'site' means eTLD+1. For example, if the URL
    `https://example.test:80/web_page` was accessing cookies, the site reported
    would be `example.test`.
    """
    allowed_sites: List[str]
    opt_out_percentage: float
    is_opt_out_top_level: bool
    operation: CookieOperation
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('allowed_sites', 'allowedSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('opt_out_percentage', 'optOutPercentage', False, 'primitive'),
        FieldMeta('is_opt_out_top_level', 'isOptOutTopLevel', False, 'primitive'),
        FieldMeta('operation', 'operation', False, 'enum', ref='Audits.CookieOperation'),
    )


@register("Audits.ClientHintIssueReason")
class ClientHintIssueReason(str, Enum):
    METATAGALLOWLISTINVALIDORIGIN = 'MetaTagAllowListInvalidOrigin'
    METATAGMODIFIEDHTML = 'MetaTagModifiedHTML'


@register("Audits.FederatedAuthRequestIssueDetails")
@dataclass
class FederatedAuthRequestIssueDetails(DataType):
    federated_auth_request_issue_reason: FederatedAuthRequestIssueReason
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('federated_auth_request_issue_reason', 'federatedAuthRequestIssueReason', False, 'enum', ref='Audits.FederatedAuthRequestIssueReason'),
    )


@register("Audits.FederatedAuthRequestIssueReason")
class FederatedAuthRequestIssueReason(str, Enum):
    """
    Represents the failure reason when a federated authentication reason fails.
    Should be updated alongside RequestIdTokenStatus in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    all cases except for success.
    """
    SHOULDEMBARGO = 'ShouldEmbargo'
    TOOMANYREQUESTS = 'TooManyRequests'
    WELLKNOWNHTTPNOTFOUND = 'WellKnownHttpNotFound'
    WELLKNOWNNORESPONSE = 'WellKnownNoResponse'
    WELLKNOWNINVALIDRESPONSE = 'WellKnownInvalidResponse'
    WELLKNOWNLISTEMPTY = 'WellKnownListEmpty'
    WELLKNOWNINVALIDCONTENTTYPE = 'WellKnownInvalidContentType'
    CONFIGNOTINWELLKNOWN = 'ConfigNotInWellKnown'
    WELLKNOWNTOOBIG = 'WellKnownTooBig'
    CONFIGHTTPNOTFOUND = 'ConfigHttpNotFound'
    CONFIGNORESPONSE = 'ConfigNoResponse'
    CONFIGINVALIDRESPONSE = 'ConfigInvalidResponse'
    CONFIGINVALIDCONTENTTYPE = 'ConfigInvalidContentType'
    CLIENTMETADATAHTTPNOTFOUND = 'ClientMetadataHttpNotFound'
    CLIENTMETADATANORESPONSE = 'ClientMetadataNoResponse'
    CLIENTMETADATAINVALIDRESPONSE = 'ClientMetadataInvalidResponse'
    CLIENTMETADATAINVALIDCONTENTTYPE = 'ClientMetadataInvalidContentType'
    IDPNOTPOTENTIALLYTRUSTWORTHY = 'IdpNotPotentiallyTrustworthy'
    DISABLEDINSETTINGS = 'DisabledInSettings'
    DISABLEDINFLAGS = 'DisabledInFlags'
    ERRORFETCHINGSIGNIN = 'ErrorFetchingSignin'
    INVALIDSIGNINRESPONSE = 'InvalidSigninResponse'
    ACCOUNTSHTTPNOTFOUND = 'AccountsHttpNotFound'
    ACCOUNTSNORESPONSE = 'AccountsNoResponse'
    ACCOUNTSINVALIDRESPONSE = 'AccountsInvalidResponse'
    ACCOUNTSLISTEMPTY = 'AccountsListEmpty'
    ACCOUNTSINVALIDCONTENTTYPE = 'AccountsInvalidContentType'
    IDTOKENHTTPNOTFOUND = 'IdTokenHttpNotFound'
    IDTOKENNORESPONSE = 'IdTokenNoResponse'
    IDTOKENINVALIDRESPONSE = 'IdTokenInvalidResponse'
    IDTOKENIDPERRORRESPONSE = 'IdTokenIdpErrorResponse'
    IDTOKENCROSSSITEIDPERRORRESPONSE = 'IdTokenCrossSiteIdpErrorResponse'
    IDTOKENINVALIDREQUEST = 'IdTokenInvalidRequest'
    IDTOKENINVALIDCONTENTTYPE = 'IdTokenInvalidContentType'
    ERRORIDTOKEN = 'ErrorIdToken'
    CANCELED = 'Canceled'
    RPPAGENOTVISIBLE = 'RpPageNotVisible'
    SILENTMEDIATIONFAILURE = 'SilentMediationFailure'
    THIRDPARTYCOOKIESBLOCKED = 'ThirdPartyCookiesBlocked'
    NOTSIGNEDINWITHIDP = 'NotSignedInWithIdp'
    MISSINGTRANSIENTUSERACTIVATION = 'MissingTransientUserActivation'
    REPLACEDBYACTIVEMODE = 'ReplacedByActiveMode'
    INVALIDFIELDSSPECIFIED = 'InvalidFieldsSpecified'
    RELYINGPARTYORIGINISOPAQUE = 'RelyingPartyOriginIsOpaque'
    TYPENOTMATCHING = 'TypeNotMatching'
    UIDISMISSEDNOEMBARGO = 'UiDismissedNoEmbargo'
    CORSERROR = 'CorsError'
    SUPPRESSEDBYSEGMENTATIONPLATFORM = 'SuppressedBySegmentationPlatform'


@register("Audits.FederatedAuthUserInfoRequestIssueDetails")
@dataclass
class FederatedAuthUserInfoRequestIssueDetails(DataType):
    federated_auth_user_info_request_issue_reason: FederatedAuthUserInfoRequestIssueReason
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('federated_auth_user_info_request_issue_reason', 'federatedAuthUserInfoRequestIssueReason', False, 'enum', ref='Audits.FederatedAuthUserInfoRequestIssueReason'),
    )


@register("Audits.FederatedAuthUserInfoRequestIssueReason")
class FederatedAuthUserInfoRequestIssueReason(str, Enum):
    """
    Represents the failure reason when a getUserInfo() call fails.
    Should be updated alongside FederatedAuthUserInfoRequestResult in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom.
    """
    NOTSAMEORIGIN = 'NotSameOrigin'
    NOTIFRAME = 'NotIframe'
    NOTPOTENTIALLYTRUSTWORTHY = 'NotPotentiallyTrustworthy'
    NOAPIPERMISSION = 'NoApiPermission'
    NOTSIGNEDINWITHIDP = 'NotSignedInWithIdp'
    NOACCOUNTSHARINGPERMISSION = 'NoAccountSharingPermission'
    INVALIDCONFIGORWELLKNOWN = 'InvalidConfigOrWellKnown'
    INVALIDACCOUNTSRESPONSE = 'InvalidAccountsResponse'
    NORETURNINGUSERFROMFETCHEDACCOUNTS = 'NoReturningUserFromFetchedAccounts'


@register("Audits.ClientHintIssueDetails")
@dataclass
class ClientHintIssueDetails(DataType):
    """
    This issue tracks client hints related issues. It's used to deprecate old
    features, encourage the use of new ones, and provide general guidance.
    """
    source_code_location: SourceCodeLocation
    client_hint_issue_reason: ClientHintIssueReason
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_code_location', 'sourceCodeLocation', False, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('client_hint_issue_reason', 'clientHintIssueReason', False, 'enum', ref='Audits.ClientHintIssueReason'),
    )


@register("Audits.FailedRequestInfo")
@dataclass
class FailedRequestInfo(DataType):
    url: str
    failure_message: str
    request_id: Optional[Network_RequestId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('failure_message', 'failureMessage', False, 'primitive'),
        FieldMeta('request_id', 'requestId', True, 'primitive'),
    )


@register("Audits.PartitioningBlobURLInfo")
class PartitioningBlobURLInfo(str, Enum):
    BLOCKEDCROSSPARTITIONFETCHING = 'BlockedCrossPartitionFetching'
    ENFORCENOOPENERFORNAVIGATION = 'EnforceNoopenerForNavigation'


@register("Audits.PartitioningBlobURLIssueDetails")
@dataclass
class PartitioningBlobURLIssueDetails(DataType):
    url: str
    partitioning_blob_url_info: PartitioningBlobURLInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('partitioning_blob_url_info', 'partitioningBlobURLInfo', False, 'enum', ref='Audits.PartitioningBlobURLInfo'),
    )


@register("Audits.ElementAccessibilityIssueReason")
class ElementAccessibilityIssueReason(str, Enum):
    DISALLOWEDSELECTCHILD = 'DisallowedSelectChild'
    DISALLOWEDOPTGROUPCHILD = 'DisallowedOptGroupChild'
    NONPHRASINGCONTENTOPTIONCHILD = 'NonPhrasingContentOptionChild'
    INTERACTIVECONTENTOPTIONCHILD = 'InteractiveContentOptionChild'
    INTERACTIVECONTENTLEGENDCHILD = 'InteractiveContentLegendChild'
    INTERACTIVECONTENTSUMMARYDESCENDANT = 'InteractiveContentSummaryDescendant'


@register("Audits.ElementAccessibilityIssueDetails")
@dataclass
class ElementAccessibilityIssueDetails(DataType):
    """This issue warns about errors in the select or summary element content model."""
    node_id: DOM_BackendNodeId
    element_accessibility_issue_reason: ElementAccessibilityIssueReason
    has_disallowed_attributes: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('element_accessibility_issue_reason', 'elementAccessibilityIssueReason', False, 'enum', ref='Audits.ElementAccessibilityIssueReason'),
        FieldMeta('has_disallowed_attributes', 'hasDisallowedAttributes', False, 'primitive'),
    )


@register("Audits.StyleSheetLoadingIssueReason")
class StyleSheetLoadingIssueReason(str, Enum):
    LATEIMPORTRULE = 'LateImportRule'
    REQUESTFAILED = 'RequestFailed'


@register("Audits.StylesheetLoadingIssueDetails")
@dataclass
class StylesheetLoadingIssueDetails(DataType):
    """This issue warns when a referenced stylesheet couldn't be loaded."""
    source_code_location: SourceCodeLocation
    style_sheet_loading_issue_reason: StyleSheetLoadingIssueReason
    failed_request_info: Optional[FailedRequestInfo] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_code_location', 'sourceCodeLocation', False, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('style_sheet_loading_issue_reason', 'styleSheetLoadingIssueReason', False, 'enum', ref='Audits.StyleSheetLoadingIssueReason'),
        FieldMeta('failed_request_info', 'failedRequestInfo', True, 'object', ref='Audits.FailedRequestInfo'),
    )


@register("Audits.PropertyRuleIssueReason")
class PropertyRuleIssueReason(str, Enum):
    INVALIDSYNTAX = 'InvalidSyntax'
    INVALIDINITIALVALUE = 'InvalidInitialValue'
    INVALIDINHERITS = 'InvalidInherits'
    INVALIDNAME = 'InvalidName'


@register("Audits.PropertyRuleIssueDetails")
@dataclass
class PropertyRuleIssueDetails(DataType):
    """
    This issue warns about errors in property rules that lead to property
    registrations being ignored.
    """
    source_code_location: SourceCodeLocation
    property_rule_issue_reason: PropertyRuleIssueReason
    property_value: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_code_location', 'sourceCodeLocation', False, 'object', ref='Audits.SourceCodeLocation'),
        FieldMeta('property_rule_issue_reason', 'propertyRuleIssueReason', False, 'enum', ref='Audits.PropertyRuleIssueReason'),
        FieldMeta('property_value', 'propertyValue', True, 'primitive'),
    )


@register("Audits.UserReidentificationIssueType")
class UserReidentificationIssueType(str, Enum):
    BLOCKEDFRAMENAVIGATION = 'BlockedFrameNavigation'
    BLOCKEDSUBRESOURCE = 'BlockedSubresource'
    NOISEDCANVASREADBACK = 'NoisedCanvasReadback'


@register("Audits.UserReidentificationIssueDetails")
@dataclass
class UserReidentificationIssueDetails(DataType):
    """
    This issue warns about uses of APIs that may be considered misuse to
    re-identify users.
    """
    type_: UserReidentificationIssueType
    request: Optional[AffectedRequest] = None
    source_code_location: Optional[SourceCodeLocation] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Audits.UserReidentificationIssueType'),
        FieldMeta('request', 'request', True, 'object', ref='Audits.AffectedRequest'),
        FieldMeta('source_code_location', 'sourceCodeLocation', True, 'object', ref='Audits.SourceCodeLocation'),
    )


@register("Audits.PermissionElementIssueType")
class PermissionElementIssueType(str, Enum):
    INVALIDTYPE = 'InvalidType'
    FENCEDFRAMEDISALLOWED = 'FencedFrameDisallowed'
    CSPFRAMEANCESTORSMISSING = 'CspFrameAncestorsMissing'
    PERMISSIONSPOLICYBLOCKED = 'PermissionsPolicyBlocked'
    PADDINGRIGHTUNSUPPORTED = 'PaddingRightUnsupported'
    PADDINGBOTTOMUNSUPPORTED = 'PaddingBottomUnsupported'
    INSETBOXSHADOWUNSUPPORTED = 'InsetBoxShadowUnsupported'
    REQUESTINPROGRESS = 'RequestInProgress'
    UNTRUSTEDEVENT = 'UntrustedEvent'
    REGISTRATIONFAILED = 'RegistrationFailed'
    TYPENOTSUPPORTED = 'TypeNotSupported'
    INVALIDTYPEACTIVATION = 'InvalidTypeActivation'
    SECURITYCHECKSFAILED = 'SecurityChecksFailed'
    ACTIVATIONDISABLED = 'ActivationDisabled'
    GEOLOCATIONDEPRECATED = 'GeolocationDeprecated'
    INVALIDDISPLAYSTYLE = 'InvalidDisplayStyle'
    NONOPAQUECOLOR = 'NonOpaqueColor'
    LOWCONTRAST = 'LowContrast'
    FONTSIZETOOSMALL = 'FontSizeTooSmall'
    FONTSIZETOOLARGE = 'FontSizeTooLarge'
    INVALIDSIZEVALUE = 'InvalidSizeValue'


@register("Audits.PermissionElementIssueDetails")
@dataclass
class PermissionElementIssueDetails(DataType):
    """This issue warns about improper usage of the <permission> element."""
    issue_type: PermissionElementIssueType
    type_: Optional[str] = None
    node_id: Optional[DOM_BackendNodeId] = None
    is_warning: Optional[bool] = None
    permission_name: Optional[str] = None
    occluder_node_info: Optional[str] = None
    occluder_parent_node_info: Optional[str] = None
    disable_reason: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('issue_type', 'issueType', False, 'enum', ref='Audits.PermissionElementIssueType'),
        FieldMeta('type_', 'type', True, 'primitive'),
        FieldMeta('node_id', 'nodeId', True, 'primitive'),
        FieldMeta('is_warning', 'isWarning', True, 'primitive'),
        FieldMeta('permission_name', 'permissionName', True, 'primitive'),
        FieldMeta('occluder_node_info', 'occluderNodeInfo', True, 'primitive'),
        FieldMeta('occluder_parent_node_info', 'occluderParentNodeInfo', True, 'primitive'),
        FieldMeta('disable_reason', 'disableReason', True, 'primitive'),
    )


@register("Audits.InspectorIssueCode")
class InspectorIssueCode(str, Enum):
    """
    A unique identifier for the type of issue. Each type may use one of the
    optional fields in InspectorIssueDetails to convey more specific
    information about the kind of issue.
    """
    COOKIEISSUE = 'CookieIssue'
    MIXEDCONTENTISSUE = 'MixedContentIssue'
    BLOCKEDBYRESPONSEISSUE = 'BlockedByResponseIssue'
    HEAVYADISSUE = 'HeavyAdIssue'
    CONTENTSECURITYPOLICYISSUE = 'ContentSecurityPolicyIssue'
    SHAREDARRAYBUFFERISSUE = 'SharedArrayBufferIssue'
    LOWTEXTCONTRASTISSUE = 'LowTextContrastIssue'
    CORSISSUE = 'CorsIssue'
    ATTRIBUTIONREPORTINGISSUE = 'AttributionReportingIssue'
    QUIRKSMODEISSUE = 'QuirksModeIssue'
    PARTITIONINGBLOBURLISSUE = 'PartitioningBlobURLIssue'
    NAVIGATORUSERAGENTISSUE = 'NavigatorUserAgentIssue'
    GENERICISSUE = 'GenericIssue'
    DEPRECATIONISSUE = 'DeprecationIssue'
    CLIENTHINTISSUE = 'ClientHintIssue'
    FEDERATEDAUTHREQUESTISSUE = 'FederatedAuthRequestIssue'
    BOUNCETRACKINGISSUE = 'BounceTrackingIssue'
    COOKIEDEPRECATIONMETADATAISSUE = 'CookieDeprecationMetadataIssue'
    STYLESHEETLOADINGISSUE = 'StylesheetLoadingIssue'
    FEDERATEDAUTHUSERINFOREQUESTISSUE = 'FederatedAuthUserInfoRequestIssue'
    PROPERTYRULEISSUE = 'PropertyRuleIssue'
    SHAREDDICTIONARYISSUE = 'SharedDictionaryIssue'
    ELEMENTACCESSIBILITYISSUE = 'ElementAccessibilityIssue'
    SRIMESSAGESIGNATUREISSUE = 'SRIMessageSignatureIssue'
    UNENCODEDDIGESTISSUE = 'UnencodedDigestIssue'
    USERREIDENTIFICATIONISSUE = 'UserReidentificationIssue'
    PERMISSIONELEMENTISSUE = 'PermissionElementIssue'


@register("Audits.InspectorIssueDetails")
@dataclass
class InspectorIssueDetails(DataType):
    """
    This struct holds a list of optional fields with additional information
    specific to the kind of issue. When adding a new issue code, please also
    add a new optional field to this type.
    """
    cookie_issue_details: Optional[CookieIssueDetails] = None
    mixed_content_issue_details: Optional[MixedContentIssueDetails] = None
    blocked_by_response_issue_details: Optional[BlockedByResponseIssueDetails] = None
    heavy_ad_issue_details: Optional[HeavyAdIssueDetails] = None
    content_security_policy_issue_details: Optional[ContentSecurityPolicyIssueDetails] = None
    shared_array_buffer_issue_details: Optional[SharedArrayBufferIssueDetails] = None
    low_text_contrast_issue_details: Optional[LowTextContrastIssueDetails] = None
    cors_issue_details: Optional[CorsIssueDetails] = None
    attribution_reporting_issue_details: Optional[AttributionReportingIssueDetails] = None
    quirks_mode_issue_details: Optional[QuirksModeIssueDetails] = None
    partitioning_blob_url_issue_details: Optional[PartitioningBlobURLIssueDetails] = None
    navigator_user_agent_issue_details: Optional[NavigatorUserAgentIssueDetails] = None
    generic_issue_details: Optional[GenericIssueDetails] = None
    deprecation_issue_details: Optional[DeprecationIssueDetails] = None
    client_hint_issue_details: Optional[ClientHintIssueDetails] = None
    federated_auth_request_issue_details: Optional[FederatedAuthRequestIssueDetails] = None
    bounce_tracking_issue_details: Optional[BounceTrackingIssueDetails] = None
    cookie_deprecation_metadata_issue_details: Optional[CookieDeprecationMetadataIssueDetails] = None
    stylesheet_loading_issue_details: Optional[StylesheetLoadingIssueDetails] = None
    property_rule_issue_details: Optional[PropertyRuleIssueDetails] = None
    federated_auth_user_info_request_issue_details: Optional[FederatedAuthUserInfoRequestIssueDetails] = None
    shared_dictionary_issue_details: Optional[SharedDictionaryIssueDetails] = None
    element_accessibility_issue_details: Optional[ElementAccessibilityIssueDetails] = None
    sri_message_signature_issue_details: Optional[SRIMessageSignatureIssueDetails] = None
    unencoded_digest_issue_details: Optional[UnencodedDigestIssueDetails] = None
    user_reidentification_issue_details: Optional[UserReidentificationIssueDetails] = None
    permission_element_issue_details: Optional[PermissionElementIssueDetails] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookie_issue_details', 'cookieIssueDetails', True, 'object', ref='Audits.CookieIssueDetails'),
        FieldMeta('mixed_content_issue_details', 'mixedContentIssueDetails', True, 'object', ref='Audits.MixedContentIssueDetails'),
        FieldMeta('blocked_by_response_issue_details', 'blockedByResponseIssueDetails', True, 'object', ref='Audits.BlockedByResponseIssueDetails'),
        FieldMeta('heavy_ad_issue_details', 'heavyAdIssueDetails', True, 'object', ref='Audits.HeavyAdIssueDetails'),
        FieldMeta('content_security_policy_issue_details', 'contentSecurityPolicyIssueDetails', True, 'object', ref='Audits.ContentSecurityPolicyIssueDetails'),
        FieldMeta('shared_array_buffer_issue_details', 'sharedArrayBufferIssueDetails', True, 'object', ref='Audits.SharedArrayBufferIssueDetails'),
        FieldMeta('low_text_contrast_issue_details', 'lowTextContrastIssueDetails', True, 'object', ref='Audits.LowTextContrastIssueDetails'),
        FieldMeta('cors_issue_details', 'corsIssueDetails', True, 'object', ref='Audits.CorsIssueDetails'),
        FieldMeta('attribution_reporting_issue_details', 'attributionReportingIssueDetails', True, 'object', ref='Audits.AttributionReportingIssueDetails'),
        FieldMeta('quirks_mode_issue_details', 'quirksModeIssueDetails', True, 'object', ref='Audits.QuirksModeIssueDetails'),
        FieldMeta('partitioning_blob_url_issue_details', 'partitioningBlobURLIssueDetails', True, 'object', ref='Audits.PartitioningBlobURLIssueDetails'),
        FieldMeta('navigator_user_agent_issue_details', 'navigatorUserAgentIssueDetails', True, 'object', ref='Audits.NavigatorUserAgentIssueDetails'),
        FieldMeta('generic_issue_details', 'genericIssueDetails', True, 'object', ref='Audits.GenericIssueDetails'),
        FieldMeta('deprecation_issue_details', 'deprecationIssueDetails', True, 'object', ref='Audits.DeprecationIssueDetails'),
        FieldMeta('client_hint_issue_details', 'clientHintIssueDetails', True, 'object', ref='Audits.ClientHintIssueDetails'),
        FieldMeta('federated_auth_request_issue_details', 'federatedAuthRequestIssueDetails', True, 'object', ref='Audits.FederatedAuthRequestIssueDetails'),
        FieldMeta('bounce_tracking_issue_details', 'bounceTrackingIssueDetails', True, 'object', ref='Audits.BounceTrackingIssueDetails'),
        FieldMeta('cookie_deprecation_metadata_issue_details', 'cookieDeprecationMetadataIssueDetails', True, 'object', ref='Audits.CookieDeprecationMetadataIssueDetails'),
        FieldMeta('stylesheet_loading_issue_details', 'stylesheetLoadingIssueDetails', True, 'object', ref='Audits.StylesheetLoadingIssueDetails'),
        FieldMeta('property_rule_issue_details', 'propertyRuleIssueDetails', True, 'object', ref='Audits.PropertyRuleIssueDetails'),
        FieldMeta('federated_auth_user_info_request_issue_details', 'federatedAuthUserInfoRequestIssueDetails', True, 'object', ref='Audits.FederatedAuthUserInfoRequestIssueDetails'),
        FieldMeta('shared_dictionary_issue_details', 'sharedDictionaryIssueDetails', True, 'object', ref='Audits.SharedDictionaryIssueDetails'),
        FieldMeta('element_accessibility_issue_details', 'elementAccessibilityIssueDetails', True, 'object', ref='Audits.ElementAccessibilityIssueDetails'),
        FieldMeta('sri_message_signature_issue_details', 'sriMessageSignatureIssueDetails', True, 'object', ref='Audits.SRIMessageSignatureIssueDetails'),
        FieldMeta('unencoded_digest_issue_details', 'unencodedDigestIssueDetails', True, 'object', ref='Audits.UnencodedDigestIssueDetails'),
        FieldMeta('user_reidentification_issue_details', 'userReidentificationIssueDetails', True, 'object', ref='Audits.UserReidentificationIssueDetails'),
        FieldMeta('permission_element_issue_details', 'permissionElementIssueDetails', True, 'object', ref='Audits.PermissionElementIssueDetails'),
    )


type IssueId = str  # A unique id for a DevTools inspector issue. Allows other entities (e.g.


@register("Audits.InspectorIssue")
@dataclass
class InspectorIssue(DataType):
    """An inspector issue reported from the back-end."""
    code: InspectorIssueCode
    details: InspectorIssueDetails
    issue_id: Optional[IssueId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('code', 'code', False, 'enum', ref='Audits.InspectorIssueCode'),
        FieldMeta('details', 'details', False, 'object', ref='Audits.InspectorIssueDetails'),
        FieldMeta('issue_id', 'issueId', True, 'primitive'),
    )

__all__ = ["AffectedCookie", "AffectedFrame", "AffectedRequest", "AttributionReportingIssueDetails", "AttributionReportingIssueType", "BlockedByResponseIssueDetails", "BlockedByResponseReason", "BounceTrackingIssueDetails", "ClientHintIssueDetails", "ClientHintIssueReason", "ContentSecurityPolicyIssueDetails", "ContentSecurityPolicyViolationType", "CookieDeprecationMetadataIssueDetails", "CookieExclusionReason", "CookieIssueDetails", "CookieIssueInsight", "CookieOperation", "CookieWarningReason", "CorsIssueDetails", "DeprecationIssueDetails", "ElementAccessibilityIssueDetails", "ElementAccessibilityIssueReason", "FailedRequestInfo", "FederatedAuthRequestIssueDetails", "FederatedAuthRequestIssueReason", "FederatedAuthUserInfoRequestIssueDetails", "FederatedAuthUserInfoRequestIssueReason", "GenericIssueDetails", "GenericIssueErrorType", "HeavyAdIssueDetails", "HeavyAdReason", "HeavyAdResolutionStatus", "InsightType", "InspectorIssue", "InspectorIssueCode", "InspectorIssueDetails", "IssueId", "LowTextContrastIssueDetails", "MixedContentIssueDetails", "MixedContentResolutionStatus", "MixedContentResourceType", "NavigatorUserAgentIssueDetails", "PartitioningBlobURLInfo", "PartitioningBlobURLIssueDetails", "PermissionElementIssueDetails", "PermissionElementIssueType", "PropertyRuleIssueDetails", "PropertyRuleIssueReason", "QuirksModeIssueDetails", "SRIMessageSignatureError", "SRIMessageSignatureIssueDetails", "SharedArrayBufferIssueDetails", "SharedArrayBufferIssueType", "SharedDictionaryError", "SharedDictionaryIssueDetails", "SourceCodeLocation", "StyleSheetLoadingIssueReason", "StylesheetLoadingIssueDetails", "UnencodedDigestError", "UnencodedDigestIssueDetails", "UserReidentificationIssueDetails", "UserReidentificationIssueType"]
