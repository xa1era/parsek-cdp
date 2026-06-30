"""Custom types and enums for the Page domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..network.types import LoaderId as Network_LoaderId
    from ..network.types import ResourceType as Network_ResourceType
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..runtime.types import ScriptId as Runtime_ScriptId
    from ..runtime.types import UniqueDebuggerId as Runtime_UniqueDebuggerId

type FrameId = str  # Unique frame identifier.


@register("Page.AdFrameType")
class AdFrameType(str, Enum):
    """Indicates whether a frame has been identified as an ad."""
    NONE = 'none'
    CHILD = 'child'
    ROOT = 'root'


@register("Page.AdFrameExplanation")
class AdFrameExplanation(str, Enum):
    PARENTISAD = 'ParentIsAd'
    CREATEDBYADSCRIPT = 'CreatedByAdScript'
    MATCHEDBLOCKINGRULE = 'MatchedBlockingRule'


@register("Page.AdFrameStatus")
@dataclass
class AdFrameStatus(DataType):
    """Indicates whether a frame has been identified as an ad and why."""
    ad_frame_type: AdFrameType
    explanations: Optional[List[AdFrameExplanation]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('ad_frame_type', 'adFrameType', False, 'enum', ref='Page.AdFrameType'),
        FieldMeta('explanations', 'explanations', True, 'array', inner=FieldMeta('', '', False, 'enum', ref='Page.AdFrameExplanation')),
    )


@register("Page.AdScriptId")
@dataclass
class AdScriptId(DataType):
    """
    Identifies the script which caused a script or frame to be labelled as an
    ad.
    """
    script_id: Runtime_ScriptId
    debugger_id: Runtime_UniqueDebuggerId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script_id', 'scriptId', False, 'primitive'),
        FieldMeta('debugger_id', 'debuggerId', False, 'primitive'),
    )


@register("Page.AdScriptAncestry")
@dataclass
class AdScriptAncestry(DataType):
    """
    Encapsulates the script ancestry and the root script filterlist rule that
    caused the frame to be labelled as an ad. Only created when `ancestryChain`
    is not empty.
    """
    ancestry_chain: List[AdScriptId]
    root_script_filterlist_rule: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('ancestry_chain', 'ancestryChain', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.AdScriptId')),
        FieldMeta('root_script_filterlist_rule', 'rootScriptFilterlistRule', True, 'primitive'),
    )


@register("Page.SecureContextType")
class SecureContextType(str, Enum):
    """Indicates whether the frame is a secure context and why it is the case."""
    SECURE = 'Secure'
    SECURELOCALHOST = 'SecureLocalhost'
    INSECURESCHEME = 'InsecureScheme'
    INSECUREANCESTOR = 'InsecureAncestor'


@register("Page.CrossOriginIsolatedContextType")
class CrossOriginIsolatedContextType(str, Enum):
    """Indicates whether the frame is cross-origin isolated and why it is the case."""
    ISOLATED = 'Isolated'
    NOTISOLATED = 'NotIsolated'
    NOTISOLATEDFEATUREDISABLED = 'NotIsolatedFeatureDisabled'


@register("Page.GatedAPIFeatures")
class GatedAPIFeatures(str, Enum):
    SHAREDARRAYBUFFERS = 'SharedArrayBuffers'
    SHAREDARRAYBUFFERSTRANSFERALLOWED = 'SharedArrayBuffersTransferAllowed'
    PERFORMANCEMEASUREMEMORY = 'PerformanceMeasureMemory'
    PERFORMANCEPROFILE = 'PerformanceProfile'


@register("Page.PermissionsPolicyFeature")
class PermissionsPolicyFeature(str, Enum):
    """
    All Permissions Policy features. This enum should match the one defined
    in services/network/public/cpp/permissions_policy/permissions_policy_features.json5.
    LINT.IfChange(PermissionsPolicyFeature)
    """
    ACCELEROMETER = 'accelerometer'
    ALL_SCREENS_CAPTURE = 'all-screens-capture'
    AMBIENT_LIGHT_SENSOR = 'ambient-light-sensor'
    ARIA_NOTIFY = 'aria-notify'
    ATTRIBUTION_REPORTING = 'attribution-reporting'
    AUTOFILL = 'autofill'
    AUTOPLAY = 'autoplay'
    BLUETOOTH = 'bluetooth'
    BROWSING_TOPICS = 'browsing-topics'
    CAMERA = 'camera'
    CAPTURED_SURFACE_CONTROL = 'captured-surface-control'
    CH_DPR = 'ch-dpr'
    CH_DEVICE_MEMORY = 'ch-device-memory'
    CH_DOWNLINK = 'ch-downlink'
    CH_ECT = 'ch-ect'
    CH_PREFERS_COLOR_SCHEME = 'ch-prefers-color-scheme'
    CH_PREFERS_REDUCED_MOTION = 'ch-prefers-reduced-motion'
    CH_PREFERS_REDUCED_TRANSPARENCY = 'ch-prefers-reduced-transparency'
    CH_RTT = 'ch-rtt'
    CH_SAVE_DATA = 'ch-save-data'
    CH_UA = 'ch-ua'
    CH_UA_ARCH = 'ch-ua-arch'
    CH_UA_BITNESS = 'ch-ua-bitness'
    CH_UA_HIGH_ENTROPY_VALUES = 'ch-ua-high-entropy-values'
    CH_UA_PLATFORM = 'ch-ua-platform'
    CH_UA_MODEL = 'ch-ua-model'
    CH_UA_MOBILE = 'ch-ua-mobile'
    CH_UA_FORM_FACTORS = 'ch-ua-form-factors'
    CH_UA_FULL_VERSION = 'ch-ua-full-version'
    CH_UA_FULL_VERSION_LIST = 'ch-ua-full-version-list'
    CH_UA_PLATFORM_VERSION = 'ch-ua-platform-version'
    CH_UA_WOW64 = 'ch-ua-wow64'
    CH_VIEWPORT_HEIGHT = 'ch-viewport-height'
    CH_VIEWPORT_WIDTH = 'ch-viewport-width'
    CH_WIDTH = 'ch-width'
    CLIPBOARD_READ = 'clipboard-read'
    CLIPBOARD_WRITE = 'clipboard-write'
    COMPUTE_PRESSURE = 'compute-pressure'
    CONTROLLED_FRAME = 'controlled-frame'
    CROSS_ORIGIN_ISOLATED = 'cross-origin-isolated'
    DEFERRED_FETCH = 'deferred-fetch'
    DEFERRED_FETCH_MINIMAL = 'deferred-fetch-minimal'
    DEVICE_ATTRIBUTES = 'device-attributes'
    DIGITAL_CREDENTIALS_CREATE = 'digital-credentials-create'
    DIGITAL_CREDENTIALS_GET = 'digital-credentials-get'
    DIRECT_SOCKETS = 'direct-sockets'
    DIRECT_SOCKETS_MULTICAST = 'direct-sockets-multicast'
    DIRECT_SOCKETS_PRIVATE = 'direct-sockets-private'
    DISPLAY_CAPTURE = 'display-capture'
    DOCUMENT_DOMAIN = 'document-domain'
    ENCRYPTED_MEDIA = 'encrypted-media'
    EXECUTION_WHILE_OUT_OF_VIEWPORT = 'execution-while-out-of-viewport'
    EXECUTION_WHILE_NOT_RENDERED = 'execution-while-not-rendered'
    FENCED_UNPARTITIONED_STORAGE_READ = 'fenced-unpartitioned-storage-read'
    FOCUS_WITHOUT_USER_ACTIVATION = 'focus-without-user-activation'
    FULLSCREEN = 'fullscreen'
    FROBULATE = 'frobulate'
    GAMEPAD = 'gamepad'
    GEOLOCATION = 'geolocation'
    GYROSCOPE = 'gyroscope'
    HID = 'hid'
    IDENTITY_CREDENTIALS_GET = 'identity-credentials-get'
    IDLE_DETECTION = 'idle-detection'
    INTEREST_COHORT = 'interest-cohort'
    JOIN_AD_INTEREST_GROUP = 'join-ad-interest-group'
    KEYBOARD_MAP = 'keyboard-map'
    LANGUAGE_DETECTOR = 'language-detector'
    LANGUAGE_MODEL = 'language-model'
    LOCAL_FONTS = 'local-fonts'
    LOCAL_NETWORK_ACCESS = 'local-network-access'
    MAGNETOMETER = 'magnetometer'
    MANUAL_TEXT = 'manual-text'
    MEDIA_PLAYBACK_WHILE_NOT_VISIBLE = 'media-playback-while-not-visible'
    MICROPHONE = 'microphone'
    MIDI = 'midi'
    ON_DEVICE_SPEECH_RECOGNITION = 'on-device-speech-recognition'
    OTP_CREDENTIALS = 'otp-credentials'
    PAYMENT = 'payment'
    PICTURE_IN_PICTURE = 'picture-in-picture'
    PRIVATE_AGGREGATION = 'private-aggregation'
    PRIVATE_STATE_TOKEN_ISSUANCE = 'private-state-token-issuance'
    PRIVATE_STATE_TOKEN_REDEMPTION = 'private-state-token-redemption'
    PUBLICKEY_CREDENTIALS_CREATE = 'publickey-credentials-create'
    PUBLICKEY_CREDENTIALS_GET = 'publickey-credentials-get'
    RECORD_AD_AUCTION_EVENTS = 'record-ad-auction-events'
    REWRITER = 'rewriter'
    RUN_AD_AUCTION = 'run-ad-auction'
    SCREEN_WAKE_LOCK = 'screen-wake-lock'
    SERIAL = 'serial'
    SHARED_STORAGE = 'shared-storage'
    SHARED_STORAGE_SELECT_URL = 'shared-storage-select-url'
    SMART_CARD = 'smart-card'
    SPEAKER_SELECTION = 'speaker-selection'
    STORAGE_ACCESS = 'storage-access'
    SUB_APPS = 'sub-apps'
    SUMMARIZER = 'summarizer'
    SYNC_XHR = 'sync-xhr'
    TRANSLATOR = 'translator'
    UNLOAD = 'unload'
    USB = 'usb'
    USB_UNRESTRICTED = 'usb-unrestricted'
    VERTICAL_SCROLL = 'vertical-scroll'
    WEB_APP_INSTALLATION = 'web-app-installation'
    WEB_PRINTING = 'web-printing'
    WEB_SHARE = 'web-share'
    WINDOW_MANAGEMENT = 'window-management'
    WRITER = 'writer'
    XR_SPATIAL_TRACKING = 'xr-spatial-tracking'


@register("Page.PermissionsPolicyBlockReason")
class PermissionsPolicyBlockReason(str, Enum):
    """Reason for a permissions policy feature to be disabled."""
    HEADER = 'Header'
    IFRAMEATTRIBUTE = 'IframeAttribute'
    INFENCEDFRAMETREE = 'InFencedFrameTree'
    INISOLATEDAPP = 'InIsolatedApp'


@register("Page.PermissionsPolicyBlockLocator")
@dataclass
class PermissionsPolicyBlockLocator(DataType):
    frame_id: FrameId
    block_reason: PermissionsPolicyBlockReason
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('block_reason', 'blockReason', False, 'enum', ref='Page.PermissionsPolicyBlockReason'),
    )


@register("Page.PermissionsPolicyFeatureState")
@dataclass
class PermissionsPolicyFeatureState(DataType):
    feature: PermissionsPolicyFeature
    allowed: bool
    locator: Optional[PermissionsPolicyBlockLocator] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('feature', 'feature', False, 'enum', ref='Page.PermissionsPolicyFeature'),
        FieldMeta('allowed', 'allowed', False, 'primitive'),
        FieldMeta('locator', 'locator', True, 'object', ref='Page.PermissionsPolicyBlockLocator'),
    )


@register("Page.OriginTrialTokenStatus")
class OriginTrialTokenStatus(str, Enum):
    """
    Origin Trial(https://www.chromium.org/blink/origin-trials) support.
    Status for an Origin Trial token.
    """
    SUCCESS = 'Success'
    NOTSUPPORTED = 'NotSupported'
    INSECURE = 'Insecure'
    EXPIRED = 'Expired'
    WRONGORIGIN = 'WrongOrigin'
    INVALIDSIGNATURE = 'InvalidSignature'
    MALFORMED = 'Malformed'
    WRONGVERSION = 'WrongVersion'
    FEATUREDISABLED = 'FeatureDisabled'
    TOKENDISABLED = 'TokenDisabled'
    FEATUREDISABLEDFORUSER = 'FeatureDisabledForUser'
    UNKNOWNTRIAL = 'UnknownTrial'


@register("Page.OriginTrialStatus")
class OriginTrialStatus(str, Enum):
    """Status for an Origin Trial."""
    ENABLED = 'Enabled'
    VALIDTOKENNOTPROVIDED = 'ValidTokenNotProvided'
    OSNOTSUPPORTED = 'OSNotSupported'
    TRIALNOTALLOWED = 'TrialNotAllowed'


@register("Page.OriginTrialUsageRestriction")
class OriginTrialUsageRestriction(str, Enum):
    NONE = 'None'
    SUBSET = 'Subset'


@register("Page.OriginTrialToken")
@dataclass
class OriginTrialToken(DataType):
    origin: str
    match_sub_domains: bool
    trial_name: str
    expiry_time: Network_TimeSinceEpoch
    is_third_party: bool
    usage_restriction: OriginTrialUsageRestriction
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('match_sub_domains', 'matchSubDomains', False, 'primitive'),
        FieldMeta('trial_name', 'trialName', False, 'primitive'),
        FieldMeta('expiry_time', 'expiryTime', False, 'primitive'),
        FieldMeta('is_third_party', 'isThirdParty', False, 'primitive'),
        FieldMeta('usage_restriction', 'usageRestriction', False, 'enum', ref='Page.OriginTrialUsageRestriction'),
    )


@register("Page.OriginTrialTokenWithStatus")
@dataclass
class OriginTrialTokenWithStatus(DataType):
    raw_token_text: str
    status: OriginTrialTokenStatus
    parsed_token: Optional[OriginTrialToken] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('raw_token_text', 'rawTokenText', False, 'primitive'),
        FieldMeta('status', 'status', False, 'enum', ref='Page.OriginTrialTokenStatus'),
        FieldMeta('parsed_token', 'parsedToken', True, 'object', ref='Page.OriginTrialToken'),
    )


@register("Page.OriginTrial")
@dataclass
class OriginTrial(DataType):
    trial_name: str
    status: OriginTrialStatus
    tokens_with_status: List[OriginTrialTokenWithStatus]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('trial_name', 'trialName', False, 'primitive'),
        FieldMeta('status', 'status', False, 'enum', ref='Page.OriginTrialStatus'),
        FieldMeta('tokens_with_status', 'tokensWithStatus', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.OriginTrialTokenWithStatus')),
    )


@register("Page.SecurityOriginDetails")
@dataclass
class SecurityOriginDetails(DataType):
    """Additional information about the frame document's security origin."""
    is_localhost: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('is_localhost', 'isLocalhost', False, 'primitive'),
    )


@register("Page.Frame")
@dataclass
class Frame(DataType):
    """Information about the Frame on the page."""
    id: FrameId
    loader_id: Network_LoaderId
    url: str
    domain_and_registry: str
    security_origin: str
    mime_type: str
    secure_context_type: SecureContextType
    cross_origin_isolated_context_type: CrossOriginIsolatedContextType
    gated_api_features: List[GatedAPIFeatures]
    parent_id: Optional[FrameId] = None
    name: Optional[str] = None
    url_fragment: Optional[str] = None
    security_origin_details: Optional[SecurityOriginDetails] = None
    unreachable_url: Optional[str] = None
    ad_frame_status: Optional[AdFrameStatus] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('domain_and_registry', 'domainAndRegistry', False, 'primitive'),
        FieldMeta('security_origin', 'securityOrigin', False, 'primitive'),
        FieldMeta('mime_type', 'mimeType', False, 'primitive'),
        FieldMeta('secure_context_type', 'secureContextType', False, 'enum', ref='Page.SecureContextType'),
        FieldMeta('cross_origin_isolated_context_type', 'crossOriginIsolatedContextType', False, 'enum', ref='Page.CrossOriginIsolatedContextType'),
        FieldMeta('gated_api_features', 'gatedAPIFeatures', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Page.GatedAPIFeatures')),
        FieldMeta('parent_id', 'parentId', True, 'primitive'),
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('url_fragment', 'urlFragment', True, 'primitive'),
        FieldMeta('security_origin_details', 'securityOriginDetails', True, 'object', ref='Page.SecurityOriginDetails'),
        FieldMeta('unreachable_url', 'unreachableUrl', True, 'primitive'),
        FieldMeta('ad_frame_status', 'adFrameStatus', True, 'object', ref='Page.AdFrameStatus'),
    )


@register("Page.FrameResource")
@dataclass
class FrameResource(DataType):
    """Information about the Resource on the page."""
    url: str
    type_: Network_ResourceType
    mime_type: str
    last_modified: Optional[Network_TimeSinceEpoch] = None
    content_size: Optional[float] = None
    failed: Optional[bool] = None
    canceled: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'enum', ref='Network.ResourceType'),
        FieldMeta('mime_type', 'mimeType', False, 'primitive'),
        FieldMeta('last_modified', 'lastModified', True, 'primitive'),
        FieldMeta('content_size', 'contentSize', True, 'primitive'),
        FieldMeta('failed', 'failed', True, 'primitive'),
        FieldMeta('canceled', 'canceled', True, 'primitive'),
    )


@register("Page.FrameResourceTree")
@dataclass
class FrameResourceTree(DataType):
    """Information about the Frame hierarchy along with their cached resources."""
    frame: Frame
    resources: List[FrameResource]
    child_frames: Optional[List[FrameResourceTree]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame', 'frame', False, 'object', ref='Page.Frame'),
        FieldMeta('resources', 'resources', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FrameResource')),
        FieldMeta('child_frames', 'childFrames', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FrameResourceTree')),
    )


@register("Page.FrameTree")
@dataclass
class FrameTree(DataType):
    """Information about the Frame hierarchy."""
    frame: Frame
    child_frames: Optional[List[FrameTree]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('frame', 'frame', False, 'object', ref='Page.Frame'),
        FieldMeta('child_frames', 'childFrames', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FrameTree')),
    )


type ScriptIdentifier = str  # Unique script identifier.


@register("Page.TransitionType")
class TransitionType(str, Enum):
    """Transition type."""
    LINK = 'link'
    TYPED = 'typed'
    ADDRESS_BAR = 'address_bar'
    AUTO_BOOKMARK = 'auto_bookmark'
    AUTO_SUBFRAME = 'auto_subframe'
    MANUAL_SUBFRAME = 'manual_subframe'
    GENERATED = 'generated'
    AUTO_TOPLEVEL = 'auto_toplevel'
    FORM_SUBMIT = 'form_submit'
    RELOAD = 'reload'
    KEYWORD = 'keyword'
    KEYWORD_GENERATED = 'keyword_generated'
    OTHER = 'other'


@register("Page.NavigationEntry")
@dataclass
class NavigationEntry(DataType):
    """Navigation history entry."""
    id: int
    url: str
    user_typed_url: str
    title: str
    transition_type: TransitionType
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('user_typed_url', 'userTypedURL', False, 'primitive'),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('transition_type', 'transitionType', False, 'enum', ref='Page.TransitionType'),
    )


@register("Page.ScreencastFrameMetadata")
@dataclass
class ScreencastFrameMetadata(DataType):
    """Screencast frame metadata."""
    offset_top: float
    page_scale_factor: float
    device_width: float
    device_height: float
    scroll_offset_x: float
    scroll_offset_y: float
    timestamp: Optional[Network_TimeSinceEpoch] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('offset_top', 'offsetTop', False, 'primitive'),
        FieldMeta('page_scale_factor', 'pageScaleFactor', False, 'primitive'),
        FieldMeta('device_width', 'deviceWidth', False, 'primitive'),
        FieldMeta('device_height', 'deviceHeight', False, 'primitive'),
        FieldMeta('scroll_offset_x', 'scrollOffsetX', False, 'primitive'),
        FieldMeta('scroll_offset_y', 'scrollOffsetY', False, 'primitive'),
        FieldMeta('timestamp', 'timestamp', True, 'primitive'),
    )


@register("Page.DialogType")
class DialogType(str, Enum):
    """Javascript dialog type."""
    ALERT = 'alert'
    CONFIRM = 'confirm'
    PROMPT = 'prompt'
    BEFOREUNLOAD = 'beforeunload'


@register("Page.AppManifestError")
@dataclass
class AppManifestError(DataType):
    """Error while paring app manifest."""
    message: str
    critical: int
    line: int
    column: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('message', 'message', False, 'primitive'),
        FieldMeta('critical', 'critical', False, 'primitive'),
        FieldMeta('line', 'line', False, 'primitive'),
        FieldMeta('column', 'column', False, 'primitive'),
    )


@register("Page.AppManifestParsedProperties")
@dataclass
class AppManifestParsedProperties(DataType):
    """Parsed app manifest properties."""
    scope: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('scope', 'scope', False, 'primitive'),
    )


@register("Page.LayoutViewport")
@dataclass
class LayoutViewport(DataType):
    """Layout viewport position and dimensions."""
    page_x: int
    page_y: int
    client_width: int
    client_height: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('page_x', 'pageX', False, 'primitive'),
        FieldMeta('page_y', 'pageY', False, 'primitive'),
        FieldMeta('client_width', 'clientWidth', False, 'primitive'),
        FieldMeta('client_height', 'clientHeight', False, 'primitive'),
    )


@register("Page.VisualViewport")
@dataclass
class VisualViewport(DataType):
    """Visual viewport position, dimensions, and scale."""
    offset_x: float
    offset_y: float
    page_x: float
    page_y: float
    client_width: float
    client_height: float
    scale: float
    zoom: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('offset_x', 'offsetX', False, 'primitive'),
        FieldMeta('offset_y', 'offsetY', False, 'primitive'),
        FieldMeta('page_x', 'pageX', False, 'primitive'),
        FieldMeta('page_y', 'pageY', False, 'primitive'),
        FieldMeta('client_width', 'clientWidth', False, 'primitive'),
        FieldMeta('client_height', 'clientHeight', False, 'primitive'),
        FieldMeta('scale', 'scale', False, 'primitive'),
        FieldMeta('zoom', 'zoom', True, 'primitive'),
    )


@register("Page.Viewport")
@dataclass
class Viewport(DataType):
    """Viewport for capturing screenshot."""
    x: float
    y: float
    width: float
    height: float
    scale: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('x', 'x', False, 'primitive'),
        FieldMeta('y', 'y', False, 'primitive'),
        FieldMeta('width', 'width', False, 'primitive'),
        FieldMeta('height', 'height', False, 'primitive'),
        FieldMeta('scale', 'scale', False, 'primitive'),
    )


@register("Page.FontFamilies")
@dataclass
class FontFamilies(DataType):
    """Generic font families collection."""
    standard: Optional[str] = None
    fixed: Optional[str] = None
    serif: Optional[str] = None
    sans_serif: Optional[str] = None
    cursive: Optional[str] = None
    fantasy: Optional[str] = None
    math: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('standard', 'standard', True, 'primitive'),
        FieldMeta('fixed', 'fixed', True, 'primitive'),
        FieldMeta('serif', 'serif', True, 'primitive'),
        FieldMeta('sans_serif', 'sansSerif', True, 'primitive'),
        FieldMeta('cursive', 'cursive', True, 'primitive'),
        FieldMeta('fantasy', 'fantasy', True, 'primitive'),
        FieldMeta('math', 'math', True, 'primitive'),
    )


@register("Page.ScriptFontFamilies")
@dataclass
class ScriptFontFamilies(DataType):
    """Font families collection for a script."""
    script: str
    font_families: FontFamilies
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('script', 'script', False, 'primitive'),
        FieldMeta('font_families', 'fontFamilies', False, 'object', ref='Page.FontFamilies'),
    )


@register("Page.FontSizes")
@dataclass
class FontSizes(DataType):
    """Default font sizes."""
    standard: Optional[int] = None
    fixed: Optional[int] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('standard', 'standard', True, 'primitive'),
        FieldMeta('fixed', 'fixed', True, 'primitive'),
    )


@register("Page.ClientNavigationReason")
class ClientNavigationReason(str, Enum):
    ANCHORCLICK = 'anchorClick'
    FORMSUBMISSIONGET = 'formSubmissionGet'
    FORMSUBMISSIONPOST = 'formSubmissionPost'
    HTTPHEADERREFRESH = 'httpHeaderRefresh'
    INITIALFRAMENAVIGATION = 'initialFrameNavigation'
    METATAGREFRESH = 'metaTagRefresh'
    OTHER = 'other'
    PAGEBLOCKINTERSTITIAL = 'pageBlockInterstitial'
    RELOAD = 'reload'
    SCRIPTINITIATED = 'scriptInitiated'


@register("Page.ClientNavigationDisposition")
class ClientNavigationDisposition(str, Enum):
    CURRENTTAB = 'currentTab'
    NEWTAB = 'newTab'
    NEWWINDOW = 'newWindow'
    DOWNLOAD = 'download'


@register("Page.InstallabilityErrorArgument")
@dataclass
class InstallabilityErrorArgument(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("Page.InstallabilityError")
@dataclass
class InstallabilityError(DataType):
    """The installability error"""
    error_id: str
    error_arguments: List[InstallabilityErrorArgument]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('error_id', 'errorId', False, 'primitive'),
        FieldMeta('error_arguments', 'errorArguments', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.InstallabilityErrorArgument')),
    )


@register("Page.ReferrerPolicy")
class ReferrerPolicy(str, Enum):
    """The referring-policy used for the navigation."""
    NOREFERRER = 'noReferrer'
    NOREFERRERWHENDOWNGRADE = 'noReferrerWhenDowngrade'
    ORIGIN = 'origin'
    ORIGINWHENCROSSORIGIN = 'originWhenCrossOrigin'
    SAMEORIGIN = 'sameOrigin'
    STRICTORIGIN = 'strictOrigin'
    STRICTORIGINWHENCROSSORIGIN = 'strictOriginWhenCrossOrigin'
    UNSAFEURL = 'unsafeUrl'


@register("Page.CompilationCacheParams")
@dataclass
class CompilationCacheParams(DataType):
    """Per-script compilation cache parameters for `Page.produceCompilationCache`"""
    url: str
    eager: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('eager', 'eager', True, 'primitive'),
    )


@register("Page.FileFilter")
@dataclass
class FileFilter(DataType):
    name: Optional[str] = None
    accepts: Optional[List[str]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('accepts', 'accepts', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("Page.FileHandler")
@dataclass
class FileHandler(DataType):
    action: str
    name: str
    launch_type: str
    icons: Optional[List[ImageResource]] = None
    accepts: Optional[List[FileFilter]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('action', 'action', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('launch_type', 'launchType', False, 'primitive'),
        FieldMeta('icons', 'icons', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.ImageResource')),
        FieldMeta('accepts', 'accepts', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FileFilter')),
    )


@register("Page.ImageResource")
@dataclass
class ImageResource(DataType):
    """The image definition used in both icon and screenshot."""
    url: str
    sizes: Optional[str] = None
    type_: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('sizes', 'sizes', True, 'primitive'),
        FieldMeta('type_', 'type', True, 'primitive'),
    )


@register("Page.LaunchHandler")
@dataclass
class LaunchHandler(DataType):
    client_mode: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('client_mode', 'clientMode', False, 'primitive'),
    )


@register("Page.ProtocolHandler")
@dataclass
class ProtocolHandler(DataType):
    protocol: str
    url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('protocol', 'protocol', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
    )


@register("Page.RelatedApplication")
@dataclass
class RelatedApplication(DataType):
    url: str
    id: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('id', 'id', True, 'primitive'),
    )


@register("Page.ScopeExtension")
@dataclass
class ScopeExtension(DataType):
    origin: str
    has_origin_wildcard: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'primitive'),
        FieldMeta('has_origin_wildcard', 'hasOriginWildcard', False, 'primitive'),
    )


@register("Page.Screenshot")
@dataclass
class Screenshot(DataType):
    image: ImageResource
    form_factor: str
    label: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('image', 'image', False, 'object', ref='Page.ImageResource'),
        FieldMeta('form_factor', 'formFactor', False, 'primitive'),
        FieldMeta('label', 'label', True, 'primitive'),
    )


@register("Page.ShareTarget")
@dataclass
class ShareTarget(DataType):
    action: str
    method: str
    enctype: str
    title: Optional[str] = None
    text: Optional[str] = None
    url: Optional[str] = None
    files: Optional[List[FileFilter]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('action', 'action', False, 'primitive'),
        FieldMeta('method', 'method', False, 'primitive'),
        FieldMeta('enctype', 'enctype', False, 'primitive'),
        FieldMeta('title', 'title', True, 'primitive'),
        FieldMeta('text', 'text', True, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('files', 'files', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FileFilter')),
    )


@register("Page.Shortcut")
@dataclass
class Shortcut(DataType):
    name: str
    url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('url', 'url', False, 'primitive'),
    )


@register("Page.WebAppManifest")
@dataclass
class WebAppManifest(DataType):
    background_color: Optional[str] = None
    description: Optional[str] = None
    dir: Optional[str] = None
    display: Optional[str] = None
    display_overrides: Optional[List[str]] = None
    file_handlers: Optional[List[FileHandler]] = None
    icons: Optional[List[ImageResource]] = None
    id: Optional[str] = None
    lang: Optional[str] = None
    launch_handler: Optional[LaunchHandler] = None
    name: Optional[str] = None
    orientation: Optional[str] = None
    prefer_related_applications: Optional[bool] = None
    protocol_handlers: Optional[List[ProtocolHandler]] = None
    related_applications: Optional[List[RelatedApplication]] = None
    scope: Optional[str] = None
    scope_extensions: Optional[List[ScopeExtension]] = None
    screenshots: Optional[List[Screenshot]] = None
    share_target: Optional[ShareTarget] = None
    short_name: Optional[str] = None
    shortcuts: Optional[List[Shortcut]] = None
    start_url: Optional[str] = None
    theme_color: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('background_color', 'backgroundColor', True, 'primitive'),
        FieldMeta('description', 'description', True, 'primitive'),
        FieldMeta('dir', 'dir', True, 'primitive'),
        FieldMeta('display', 'display', True, 'primitive'),
        FieldMeta('display_overrides', 'displayOverrides', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('file_handlers', 'fileHandlers', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.FileHandler')),
        FieldMeta('icons', 'icons', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.ImageResource')),
        FieldMeta('id', 'id', True, 'primitive'),
        FieldMeta('lang', 'lang', True, 'primitive'),
        FieldMeta('launch_handler', 'launchHandler', True, 'object', ref='Page.LaunchHandler'),
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('orientation', 'orientation', True, 'primitive'),
        FieldMeta('prefer_related_applications', 'preferRelatedApplications', True, 'primitive'),
        FieldMeta('protocol_handlers', 'protocolHandlers', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.ProtocolHandler')),
        FieldMeta('related_applications', 'relatedApplications', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.RelatedApplication')),
        FieldMeta('scope', 'scope', True, 'primitive'),
        FieldMeta('scope_extensions', 'scopeExtensions', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.ScopeExtension')),
        FieldMeta('screenshots', 'screenshots', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.Screenshot')),
        FieldMeta('share_target', 'shareTarget', True, 'object', ref='Page.ShareTarget'),
        FieldMeta('short_name', 'shortName', True, 'primitive'),
        FieldMeta('shortcuts', 'shortcuts', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.Shortcut')),
        FieldMeta('start_url', 'startUrl', True, 'primitive'),
        FieldMeta('theme_color', 'themeColor', True, 'primitive'),
    )


@register("Page.NavigationType")
class NavigationType(str, Enum):
    """The type of a frameNavigated event."""
    NAVIGATION = 'Navigation'
    BACKFORWARDCACHERESTORE = 'BackForwardCacheRestore'


@register("Page.BackForwardCacheNotRestoredReason")
class BackForwardCacheNotRestoredReason(str, Enum):
    """List of not restored reasons for back-forward cache."""
    NOTPRIMARYMAINFRAME = 'NotPrimaryMainFrame'
    BACKFORWARDCACHEDISABLED = 'BackForwardCacheDisabled'
    RELATEDACTIVECONTENTSEXIST = 'RelatedActiveContentsExist'
    HTTPSTATUSNOTOK = 'HTTPStatusNotOK'
    SCHEMENOTHTTPORHTTPS = 'SchemeNotHTTPOrHTTPS'
    LOADING = 'Loading'
    WASGRANTEDMEDIAACCESS = 'WasGrantedMediaAccess'
    DISABLEFORRENDERFRAMEHOSTCALLED = 'DisableForRenderFrameHostCalled'
    DOMAINNOTALLOWED = 'DomainNotAllowed'
    HTTPMETHODNOTGET = 'HTTPMethodNotGET'
    SUBFRAMEISNAVIGATING = 'SubframeIsNavigating'
    TIMEOUT = 'Timeout'
    CACHELIMIT = 'CacheLimit'
    JAVASCRIPTEXECUTION = 'JavaScriptExecution'
    RENDERERPROCESSKILLED = 'RendererProcessKilled'
    RENDERERPROCESSCRASHED = 'RendererProcessCrashed'
    SCHEDULERTRACKEDFEATUREUSED = 'SchedulerTrackedFeatureUsed'
    CONFLICTINGBROWSINGINSTANCE = 'ConflictingBrowsingInstance'
    CACHEFLUSHED = 'CacheFlushed'
    SERVICEWORKERVERSIONACTIVATION = 'ServiceWorkerVersionActivation'
    SESSIONRESTORED = 'SessionRestored'
    SERVICEWORKERPOSTMESSAGE = 'ServiceWorkerPostMessage'
    ENTEREDBACKFORWARDCACHEBEFORESERVICEWORKERHOSTADDED = 'EnteredBackForwardCacheBeforeServiceWorkerHostAdded'
    RENDERFRAMEHOSTREUSED_SAMESITE = 'RenderFrameHostReused_SameSite'
    RENDERFRAMEHOSTREUSED_CROSSSITE = 'RenderFrameHostReused_CrossSite'
    SERVICEWORKERCLAIM = 'ServiceWorkerClaim'
    IGNOREEVENTANDEVICT = 'IgnoreEventAndEvict'
    HAVEINNERCONTENTS = 'HaveInnerContents'
    TIMEOUTPUTTINGINCACHE = 'TimeoutPuttingInCache'
    BACKFORWARDCACHEDISABLEDBYLOWMEMORY = 'BackForwardCacheDisabledByLowMemory'
    BACKFORWARDCACHEDISABLEDBYCOMMANDLINE = 'BackForwardCacheDisabledByCommandLine'
    NETWORKREQUESTDATAPIPEDRAINEDASBYTESCONSUMER = 'NetworkRequestDatapipeDrainedAsBytesConsumer'
    NETWORKREQUESTREDIRECTED = 'NetworkRequestRedirected'
    NETWORKREQUESTTIMEOUT = 'NetworkRequestTimeout'
    NETWORKEXCEEDSBUFFERLIMIT = 'NetworkExceedsBufferLimit'
    NAVIGATIONCANCELLEDWHILERESTORING = 'NavigationCancelledWhileRestoring'
    NOTMOSTRECENTNAVIGATIONENTRY = 'NotMostRecentNavigationEntry'
    BACKFORWARDCACHEDISABLEDFORPRERENDER = 'BackForwardCacheDisabledForPrerender'
    USERAGENTOVERRIDEDIFFERS = 'UserAgentOverrideDiffers'
    FOREGROUNDCACHELIMIT = 'ForegroundCacheLimit'
    BROWSINGINSTANCENOTSWAPPED = 'BrowsingInstanceNotSwapped'
    BACKFORWARDCACHEDISABLEDFORDELEGATE = 'BackForwardCacheDisabledForDelegate'
    UNLOADHANDLEREXISTSINMAINFRAME = 'UnloadHandlerExistsInMainFrame'
    UNLOADHANDLEREXISTSINSUBFRAME = 'UnloadHandlerExistsInSubFrame'
    SERVICEWORKERUNREGISTRATION = 'ServiceWorkerUnregistration'
    CACHECONTROLNOSTORE = 'CacheControlNoStore'
    CACHECONTROLNOSTORECOOKIEMODIFIED = 'CacheControlNoStoreCookieModified'
    CACHECONTROLNOSTOREHTTPONLYCOOKIEMODIFIED = 'CacheControlNoStoreHTTPOnlyCookieModified'
    NORESPONSEHEAD = 'NoResponseHead'
    UNKNOWN = 'Unknown'
    ACTIVATIONNAVIGATIONSDISALLOWEDFORBUG1234857 = 'ActivationNavigationsDisallowedForBug1234857'
    ERRORDOCUMENT = 'ErrorDocument'
    FENCEDFRAMESEMBEDDER = 'FencedFramesEmbedder'
    COOKIEDISABLED = 'CookieDisabled'
    HTTPAUTHREQUIRED = 'HTTPAuthRequired'
    COOKIEFLUSHED = 'CookieFlushed'
    BROADCASTCHANNELONMESSAGE = 'BroadcastChannelOnMessage'
    WEBVIEWSETTINGSCHANGED = 'WebViewSettingsChanged'
    WEBVIEWJAVASCRIPTOBJECTCHANGED = 'WebViewJavaScriptObjectChanged'
    WEBVIEWMESSAGELISTENERINJECTED = 'WebViewMessageListenerInjected'
    WEBVIEWSAFEBROWSINGALLOWLISTCHANGED = 'WebViewSafeBrowsingAllowlistChanged'
    WEBVIEWDOCUMENTSTARTJAVASCRIPTCHANGED = 'WebViewDocumentStartJavascriptChanged'
    WEBSOCKET = 'WebSocket'
    WEBTRANSPORT = 'WebTransport'
    WEBRTC = 'WebRTC'
    MAINRESOURCEHASCACHECONTROLNOSTORE = 'MainResourceHasCacheControlNoStore'
    MAINRESOURCEHASCACHECONTROLNOCACHE = 'MainResourceHasCacheControlNoCache'
    SUBRESOURCEHASCACHECONTROLNOSTORE = 'SubresourceHasCacheControlNoStore'
    SUBRESOURCEHASCACHECONTROLNOCACHE = 'SubresourceHasCacheControlNoCache'
    CONTAINSPLUGINS = 'ContainsPlugins'
    DOCUMENTLOADED = 'DocumentLoaded'
    OUTSTANDINGNETWORKREQUESTOTHERS = 'OutstandingNetworkRequestOthers'
    REQUESTEDMIDIPERMISSION = 'RequestedMIDIPermission'
    REQUESTEDAUDIOCAPTUREPERMISSION = 'RequestedAudioCapturePermission'
    REQUESTEDVIDEOCAPTUREPERMISSION = 'RequestedVideoCapturePermission'
    REQUESTEDBACKFORWARDCACHEBLOCKEDSENSORS = 'RequestedBackForwardCacheBlockedSensors'
    REQUESTEDBACKGROUNDWORKPERMISSION = 'RequestedBackgroundWorkPermission'
    BROADCASTCHANNEL = 'BroadcastChannel'
    WEBXR = 'WebXR'
    SHAREDWORKER = 'SharedWorker'
    SHAREDWORKERMESSAGE = 'SharedWorkerMessage'
    SHAREDWORKERWITHNOACTIVECLIENT = 'SharedWorkerWithNoActiveClient'
    WEBLOCKS = 'WebLocks'
    WEBHID = 'WebHID'
    WEBBLUETOOTH = 'WebBluetooth'
    WEBSHARE = 'WebShare'
    REQUESTEDSTORAGEACCESSGRANT = 'RequestedStorageAccessGrant'
    WEBNFC = 'WebNfc'
    OUTSTANDINGNETWORKREQUESTFETCH = 'OutstandingNetworkRequestFetch'
    OUTSTANDINGNETWORKREQUESTXHR = 'OutstandingNetworkRequestXHR'
    APPBANNER = 'AppBanner'
    PRINTING = 'Printing'
    WEBDATABASE = 'WebDatabase'
    PICTUREINPICTURE = 'PictureInPicture'
    SPEECHRECOGNIZER = 'SpeechRecognizer'
    IDLEMANAGER = 'IdleManager'
    PAYMENTMANAGER = 'PaymentManager'
    SPEECHSYNTHESIS = 'SpeechSynthesis'
    KEYBOARDLOCK = 'KeyboardLock'
    WEBOTPSERVICE = 'WebOTPService'
    OUTSTANDINGNETWORKREQUESTDIRECTSOCKET = 'OutstandingNetworkRequestDirectSocket'
    INJECTEDJAVASCRIPT = 'InjectedJavascript'
    INJECTEDSTYLESHEET = 'InjectedStyleSheet'
    KEEPALIVEREQUEST = 'KeepaliveRequest'
    INDEXEDDBEVENT = 'IndexedDBEvent'
    DUMMY = 'Dummy'
    JSNETWORKREQUESTRECEIVEDCACHECONTROLNOSTORERESOURCE = 'JsNetworkRequestReceivedCacheControlNoStoreResource'
    WEBRTCUSEDWITHCCNS = 'WebRTCUsedWithCCNS'
    WEBTRANSPORTUSEDWITHCCNS = 'WebTransportUsedWithCCNS'
    WEBSOCKETUSEDWITHCCNS = 'WebSocketUsedWithCCNS'
    SMARTCARD = 'SmartCard'
    LIVEMEDIASTREAMTRACK = 'LiveMediaStreamTrack'
    UNLOADHANDLER = 'UnloadHandler'
    PARSERABORTED = 'ParserAborted'
    CONTENTSECURITYHANDLER = 'ContentSecurityHandler'
    CONTENTWEBAUTHENTICATIONAPI = 'ContentWebAuthenticationAPI'
    CONTENTFILECHOOSER = 'ContentFileChooser'
    CONTENTSERIAL = 'ContentSerial'
    CONTENTFILESYSTEMACCESS = 'ContentFileSystemAccess'
    CONTENTMEDIADEVICESDISPATCHERHOST = 'ContentMediaDevicesDispatcherHost'
    CONTENTWEBBLUETOOTH = 'ContentWebBluetooth'
    CONTENTWEBUSB = 'ContentWebUSB'
    CONTENTMEDIASESSIONSERVICE = 'ContentMediaSessionService'
    CONTENTSCREENREADER = 'ContentScreenReader'
    CONTENTDISCARDED = 'ContentDiscarded'
    EMBEDDERPOPUPBLOCKERTABHELPER = 'EmbedderPopupBlockerTabHelper'
    EMBEDDERSAFEBROWSINGTRIGGEREDPOPUPBLOCKER = 'EmbedderSafeBrowsingTriggeredPopupBlocker'
    EMBEDDERSAFEBROWSINGTHREATDETAILS = 'EmbedderSafeBrowsingThreatDetails'
    EMBEDDERAPPBANNERMANAGER = 'EmbedderAppBannerManager'
    EMBEDDERDOMDISTILLERVIEWERSOURCE = 'EmbedderDomDistillerViewerSource'
    EMBEDDERDOMDISTILLERSELFDELETINGREQUESTDELEGATE = 'EmbedderDomDistillerSelfDeletingRequestDelegate'
    EMBEDDEROOMINTERVENTIONTABHELPER = 'EmbedderOomInterventionTabHelper'
    EMBEDDEROFFLINEPAGE = 'EmbedderOfflinePage'
    EMBEDDERCHROMEPASSWORDMANAGERCLIENTBINDCREDENTIALMANAGER = 'EmbedderChromePasswordManagerClientBindCredentialManager'
    EMBEDDERPERMISSIONREQUESTMANAGER = 'EmbedderPermissionRequestManager'
    EMBEDDERMODALDIALOG = 'EmbedderModalDialog'
    EMBEDDEREXTENSIONS = 'EmbedderExtensions'
    EMBEDDEREXTENSIONMESSAGING = 'EmbedderExtensionMessaging'
    EMBEDDEREXTENSIONMESSAGINGFOROPENPORT = 'EmbedderExtensionMessagingForOpenPort'
    EMBEDDEREXTENSIONSENTMESSAGETOCACHEDFRAME = 'EmbedderExtensionSentMessageToCachedFrame'
    REQUESTEDBYWEBVIEWCLIENT = 'RequestedByWebViewClient'
    POSTMESSAGEBYWEBVIEWCLIENT = 'PostMessageByWebViewClient'
    CACHECONTROLNOSTOREDEVICEBOUNDSESSIONTERMINATED = 'CacheControlNoStoreDeviceBoundSessionTerminated'
    CACHELIMITPRUNEDONMODERATEMEMORYPRESSURE = 'CacheLimitPrunedOnModerateMemoryPressure'
    CACHELIMITPRUNEDONCRITICALMEMORYPRESSURE = 'CacheLimitPrunedOnCriticalMemoryPressure'


@register("Page.BackForwardCacheNotRestoredReasonType")
class BackForwardCacheNotRestoredReasonType(str, Enum):
    """Types of not restored reasons for back-forward cache."""
    SUPPORTPENDING = 'SupportPending'
    PAGESUPPORTNEEDED = 'PageSupportNeeded'
    CIRCUMSTANTIAL = 'Circumstantial'


@register("Page.BackForwardCacheBlockingDetails")
@dataclass
class BackForwardCacheBlockingDetails(DataType):
    line_number: int
    column_number: int
    url: Optional[str] = None
    function: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('line_number', 'lineNumber', False, 'primitive'),
        FieldMeta('column_number', 'columnNumber', False, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('function', 'function', True, 'primitive'),
    )


@register("Page.BackForwardCacheNotRestoredExplanation")
@dataclass
class BackForwardCacheNotRestoredExplanation(DataType):
    type_: BackForwardCacheNotRestoredReasonType
    reason: BackForwardCacheNotRestoredReason
    context: Optional[str] = None
    details: Optional[List[BackForwardCacheBlockingDetails]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Page.BackForwardCacheNotRestoredReasonType'),
        FieldMeta('reason', 'reason', False, 'enum', ref='Page.BackForwardCacheNotRestoredReason'),
        FieldMeta('context', 'context', True, 'primitive'),
        FieldMeta('details', 'details', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.BackForwardCacheBlockingDetails')),
    )


@register("Page.BackForwardCacheNotRestoredExplanationTree")
@dataclass
class BackForwardCacheNotRestoredExplanationTree(DataType):
    url: str
    explanations: List[BackForwardCacheNotRestoredExplanation]
    children: List[BackForwardCacheNotRestoredExplanationTree]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('explanations', 'explanations', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.BackForwardCacheNotRestoredExplanation')),
        FieldMeta('children', 'children', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Page.BackForwardCacheNotRestoredExplanationTree')),
    )

__all__ = ["AdFrameExplanation", "AdFrameStatus", "AdFrameType", "AdScriptAncestry", "AdScriptId", "AppManifestError", "AppManifestParsedProperties", "BackForwardCacheBlockingDetails", "BackForwardCacheNotRestoredExplanation", "BackForwardCacheNotRestoredExplanationTree", "BackForwardCacheNotRestoredReason", "BackForwardCacheNotRestoredReasonType", "ClientNavigationDisposition", "ClientNavigationReason", "CompilationCacheParams", "CrossOriginIsolatedContextType", "DialogType", "FileFilter", "FileHandler", "FontFamilies", "FontSizes", "Frame", "FrameId", "FrameResource", "FrameResourceTree", "FrameTree", "GatedAPIFeatures", "ImageResource", "InstallabilityError", "InstallabilityErrorArgument", "LaunchHandler", "LayoutViewport", "NavigationEntry", "NavigationType", "OriginTrial", "OriginTrialStatus", "OriginTrialToken", "OriginTrialTokenStatus", "OriginTrialTokenWithStatus", "OriginTrialUsageRestriction", "PermissionsPolicyBlockLocator", "PermissionsPolicyBlockReason", "PermissionsPolicyFeature", "PermissionsPolicyFeatureState", "ProtocolHandler", "ReferrerPolicy", "RelatedApplication", "ScopeExtension", "ScreencastFrameMetadata", "Screenshot", "ScriptFontFamilies", "ScriptIdentifier", "SecureContextType", "SecurityOriginDetails", "ShareTarget", "Shortcut", "TransitionType", "Viewport", "VisualViewport", "WebAppManifest"]
