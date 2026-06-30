"""Custom types and enums for the Preload domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..network.types import LoaderId as Network_LoaderId
    from ..network.types import RequestId as Network_RequestId

type RuleSetId = str  # Unique id


@register("Preload.RuleSet")
@dataclass
class RuleSet(DataType):
    """Corresponds to SpeculationRuleSet"""
    id: RuleSetId
    loader_id: Network_LoaderId
    source_text: str
    backend_node_id: Optional[DOM_BackendNodeId] = None
    url: Optional[str] = None
    request_id: Optional[Network_RequestId] = None
    error_type: Optional[RuleSetErrorType] = None
    error_message: Optional[str] = None
    tag: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('source_text', 'sourceText', False, 'primitive'),
        FieldMeta('backend_node_id', 'backendNodeId', True, 'primitive'),
        FieldMeta('url', 'url', True, 'primitive'),
        FieldMeta('request_id', 'requestId', True, 'primitive'),
        FieldMeta('error_type', 'errorType', True, 'enum', ref='Preload.RuleSetErrorType'),
        FieldMeta('error_message', 'errorMessage', True, 'primitive'),
        FieldMeta('tag', 'tag', True, 'primitive'),
    )


@register("Preload.RuleSetErrorType")
class RuleSetErrorType(str, Enum):
    SOURCEISNOTJSONOBJECT = 'SourceIsNotJsonObject'
    INVALIDRULESSKIPPED = 'InvalidRulesSkipped'
    INVALIDRULESETLEVELTAG = 'InvalidRulesetLevelTag'


@register("Preload.SpeculationAction")
class SpeculationAction(str, Enum):
    """
    The type of preloading attempted. It corresponds to
    mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it
    isn't being used by clients).
    """
    PREFETCH = 'Prefetch'
    PRERENDER = 'Prerender'
    PRERENDERUNTILSCRIPT = 'PrerenderUntilScript'


@register("Preload.SpeculationTargetHint")
class SpeculationTargetHint(str, Enum):
    """
    Corresponds to mojom::SpeculationTargetHint.
    See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
    """
    BLANK = 'Blank'
    SELF = 'Self'


@register("Preload.PreloadingAttemptKey")
@dataclass
class PreloadingAttemptKey(DataType):
    """
    A key that identifies a preloading attempt.
    
    The url used is the url specified by the trigger (i.e. the initial URL), and
    not the final url that is navigated to. For example, prerendering allows
    same-origin main frame navigations during the attempt, but the attempt is
    still keyed with the initial URL.
    """
    loader_id: Network_LoaderId
    action: SpeculationAction
    url: str
    target_hint: Optional[SpeculationTargetHint] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('action', 'action', False, 'enum', ref='Preload.SpeculationAction'),
        FieldMeta('url', 'url', False, 'primitive'),
        FieldMeta('target_hint', 'targetHint', True, 'enum', ref='Preload.SpeculationTargetHint'),
    )


@register("Preload.PreloadingAttemptSource")
@dataclass
class PreloadingAttemptSource(DataType):
    """
    Lists sources for a preloading attempt, specifically the ids of rule sets
    that had a speculation rule that triggered the attempt, and the
    BackendNodeIds of <a href> or <area href> elements that triggered the
    attempt (in the case of attempts triggered by a document rule). It is
    possible for multiple rule sets and links to trigger a single attempt.
    """
    key: PreloadingAttemptKey
    rule_set_ids: List[RuleSetId]
    node_ids: List[DOM_BackendNodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'object', ref='Preload.PreloadingAttemptKey'),
        FieldMeta('rule_set_ids', 'ruleSetIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


type PreloadPipelineId = str  # Chrome manages different types of preloads together using a


@register("Preload.PrerenderFinalStatus")
class PrerenderFinalStatus(str, Enum):
    """List of FinalStatus reasons for Prerender2."""
    ACTIVATED = 'Activated'
    DESTROYED = 'Destroyed'
    LOWENDDEVICE = 'LowEndDevice'
    INVALIDSCHEMEREDIRECT = 'InvalidSchemeRedirect'
    INVALIDSCHEMENAVIGATION = 'InvalidSchemeNavigation'
    NAVIGATIONREQUESTBLOCKEDBYCSP = 'NavigationRequestBlockedByCsp'
    MOJOBINDERPOLICY = 'MojoBinderPolicy'
    RENDERERPROCESSCRASHED = 'RendererProcessCrashed'
    RENDERERPROCESSKILLED = 'RendererProcessKilled'
    DOWNLOAD = 'Download'
    TRIGGERDESTROYED = 'TriggerDestroyed'
    NAVIGATIONNOTCOMMITTED = 'NavigationNotCommitted'
    NAVIGATIONBADHTTPSTATUS = 'NavigationBadHttpStatus'
    CLIENTCERTREQUESTED = 'ClientCertRequested'
    NAVIGATIONREQUESTNETWORKERROR = 'NavigationRequestNetworkError'
    CANCELALLHOSTSFORTESTING = 'CancelAllHostsForTesting'
    DIDFAILLOAD = 'DidFailLoad'
    STOP = 'Stop'
    SSLCERTIFICATEERROR = 'SslCertificateError'
    LOGINAUTHREQUESTED = 'LoginAuthRequested'
    UACHANGEREQUIRESRELOAD = 'UaChangeRequiresReload'
    BLOCKEDBYCLIENT = 'BlockedByClient'
    AUDIOOUTPUTDEVICEREQUESTED = 'AudioOutputDeviceRequested'
    MIXEDCONTENT = 'MixedContent'
    TRIGGERBACKGROUNDED = 'TriggerBackgrounded'
    MEMORYLIMITEXCEEDED = 'MemoryLimitExceeded'
    DATASAVERENABLED = 'DataSaverEnabled'
    TRIGGERURLHASEFFECTIVEURL = 'TriggerUrlHasEffectiveUrl'
    ACTIVATEDBEFORESTARTED = 'ActivatedBeforeStarted'
    INACTIVEPAGERESTRICTION = 'InactivePageRestriction'
    STARTFAILED = 'StartFailed'
    TIMEOUTBACKGROUNDED = 'TimeoutBackgrounded'
    CROSSSITEREDIRECTININITIALNAVIGATION = 'CrossSiteRedirectInInitialNavigation'
    CROSSSITENAVIGATIONININITIALNAVIGATION = 'CrossSiteNavigationInInitialNavigation'
    SAMESITECROSSORIGINREDIRECTNOTOPTINININITIALNAVIGATION = 'SameSiteCrossOriginRedirectNotOptInInInitialNavigation'
    SAMESITECROSSORIGINNAVIGATIONNOTOPTINININITIALNAVIGATION = 'SameSiteCrossOriginNavigationNotOptInInInitialNavigation'
    ACTIVATIONNAVIGATIONPARAMETERMISMATCH = 'ActivationNavigationParameterMismatch'
    ACTIVATEDINBACKGROUND = 'ActivatedInBackground'
    EMBEDDERHOSTDISALLOWED = 'EmbedderHostDisallowed'
    ACTIVATIONNAVIGATIONDESTROYEDBEFORESUCCESS = 'ActivationNavigationDestroyedBeforeSuccess'
    TABCLOSEDBYUSERGESTURE = 'TabClosedByUserGesture'
    TABCLOSEDWITHOUTUSERGESTURE = 'TabClosedWithoutUserGesture'
    PRIMARYMAINFRAMERENDERERPROCESSCRASHED = 'PrimaryMainFrameRendererProcessCrashed'
    PRIMARYMAINFRAMERENDERERPROCESSKILLED = 'PrimaryMainFrameRendererProcessKilled'
    ACTIVATIONFRAMEPOLICYNOTCOMPATIBLE = 'ActivationFramePolicyNotCompatible'
    PRELOADINGDISABLED = 'PreloadingDisabled'
    BATTERYSAVERENABLED = 'BatterySaverEnabled'
    ACTIVATEDDURINGMAINFRAMENAVIGATION = 'ActivatedDuringMainFrameNavigation'
    PRELOADINGUNSUPPORTEDBYWEBCONTENTS = 'PreloadingUnsupportedByWebContents'
    CROSSSITEREDIRECTINMAINFRAMENAVIGATION = 'CrossSiteRedirectInMainFrameNavigation'
    CROSSSITENAVIGATIONINMAINFRAMENAVIGATION = 'CrossSiteNavigationInMainFrameNavigation'
    SAMESITECROSSORIGINREDIRECTNOTOPTININMAINFRAMENAVIGATION = 'SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation'
    SAMESITECROSSORIGINNAVIGATIONNOTOPTININMAINFRAMENAVIGATION = 'SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation'
    MEMORYPRESSUREONTRIGGER = 'MemoryPressureOnTrigger'
    MEMORYPRESSUREAFTERTRIGGERED = 'MemoryPressureAfterTriggered'
    PRERENDERINGDISABLEDBYDEVTOOLS = 'PrerenderingDisabledByDevTools'
    SPECULATIONRULEREMOVED = 'SpeculationRuleRemoved'
    ACTIVATEDWITHAUXILIARYBROWSINGCONTEXTS = 'ActivatedWithAuxiliaryBrowsingContexts'
    MAXNUMOFRUNNINGEAGERPRERENDERSEXCEEDED = 'MaxNumOfRunningEagerPrerendersExceeded'
    MAXNUMOFRUNNINGNONEAGERPRERENDERSEXCEEDED = 'MaxNumOfRunningNonEagerPrerendersExceeded'
    MAXNUMOFRUNNINGEMBEDDERPRERENDERSEXCEEDED = 'MaxNumOfRunningEmbedderPrerendersExceeded'
    PRERENDERINGURLHASEFFECTIVEURL = 'PrerenderingUrlHasEffectiveUrl'
    REDIRECTEDPRERENDERINGURLHASEFFECTIVEURL = 'RedirectedPrerenderingUrlHasEffectiveUrl'
    ACTIVATIONURLHASEFFECTIVEURL = 'ActivationUrlHasEffectiveUrl'
    JAVASCRIPTINTERFACEADDED = 'JavaScriptInterfaceAdded'
    JAVASCRIPTINTERFACEREMOVED = 'JavaScriptInterfaceRemoved'
    ALLPRERENDERINGCANCELED = 'AllPrerenderingCanceled'
    WINDOWCLOSED = 'WindowClosed'
    SLOWNETWORK = 'SlowNetwork'
    OTHERPRERENDEREDPAGEACTIVATED = 'OtherPrerenderedPageActivated'
    V8OPTIMIZERDISABLED = 'V8OptimizerDisabled'
    PRERENDERFAILEDDURINGPREFETCH = 'PrerenderFailedDuringPrefetch'
    BROWSINGDATAREMOVED = 'BrowsingDataRemoved'
    PRERENDERHOSTREUSED = 'PrerenderHostReused'


@register("Preload.PreloadingStatus")
class PreloadingStatus(str, Enum):
    """
    Preloading status values, see also PreloadingTriggeringOutcome. This
    status is shared by prefetchStatusUpdated and prerenderStatusUpdated.
    """
    PENDING = 'Pending'
    RUNNING = 'Running'
    READY = 'Ready'
    SUCCESS = 'Success'
    FAILURE = 'Failure'
    NOTSUPPORTED = 'NotSupported'


@register("Preload.PrefetchStatus")
class PrefetchStatus(str, Enum):
    """
    TODO(https://crbug.com/1384419): revisit the list of PrefetchStatus and
    filter out the ones that aren't necessary to the developers.
    """
    PREFETCHALLOWED = 'PrefetchAllowed'
    PREFETCHFAILEDINELIGIBLEREDIRECT = 'PrefetchFailedIneligibleRedirect'
    PREFETCHFAILEDINVALIDREDIRECT = 'PrefetchFailedInvalidRedirect'
    PREFETCHFAILEDMIMENOTSUPPORTED = 'PrefetchFailedMIMENotSupported'
    PREFETCHFAILEDNETERROR = 'PrefetchFailedNetError'
    PREFETCHFAILEDNON2XX = 'PrefetchFailedNon2XX'
    PREFETCHEVICTEDAFTERBROWSINGDATAREMOVED = 'PrefetchEvictedAfterBrowsingDataRemoved'
    PREFETCHEVICTEDAFTERCANDIDATEREMOVED = 'PrefetchEvictedAfterCandidateRemoved'
    PREFETCHEVICTEDFORNEWERPREFETCH = 'PrefetchEvictedForNewerPrefetch'
    PREFETCHHELDBACK = 'PrefetchHeldback'
    PREFETCHINELIGIBLERETRYAFTER = 'PrefetchIneligibleRetryAfter'
    PREFETCHISPRIVACYDECOY = 'PrefetchIsPrivacyDecoy'
    PREFETCHISSTALE = 'PrefetchIsStale'
    PREFETCHNOTELIGIBLEBROWSERCONTEXTOFFTHERECORD = 'PrefetchNotEligibleBrowserContextOffTheRecord'
    PREFETCHNOTELIGIBLEDATASAVERENABLED = 'PrefetchNotEligibleDataSaverEnabled'
    PREFETCHNOTELIGIBLEEXISTINGPROXY = 'PrefetchNotEligibleExistingProxy'
    PREFETCHNOTELIGIBLEHOSTISNONUNIQUE = 'PrefetchNotEligibleHostIsNonUnique'
    PREFETCHNOTELIGIBLENONDEFAULTSTORAGEPARTITION = 'PrefetchNotEligibleNonDefaultStoragePartition'
    PREFETCHNOTELIGIBLESAMESITECROSSORIGINPREFETCHREQUIREDPROXY = 'PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy'
    PREFETCHNOTELIGIBLESCHEMEISNOTHTTPS = 'PrefetchNotEligibleSchemeIsNotHttps'
    PREFETCHNOTELIGIBLEUSERHASCOOKIES = 'PrefetchNotEligibleUserHasCookies'
    PREFETCHNOTELIGIBLEUSERHASSERVICEWORKER = 'PrefetchNotEligibleUserHasServiceWorker'
    PREFETCHNOTELIGIBLEUSERHASSERVICEWORKERNOFETCHHANDLER = 'PrefetchNotEligibleUserHasServiceWorkerNoFetchHandler'
    PREFETCHNOTELIGIBLEREDIRECTFROMSERVICEWORKER = 'PrefetchNotEligibleRedirectFromServiceWorker'
    PREFETCHNOTELIGIBLEREDIRECTTOSERVICEWORKER = 'PrefetchNotEligibleRedirectToServiceWorker'
    PREFETCHNOTELIGIBLEBATTERYSAVERENABLED = 'PrefetchNotEligibleBatterySaverEnabled'
    PREFETCHNOTELIGIBLEPRELOADINGDISABLED = 'PrefetchNotEligiblePreloadingDisabled'
    PREFETCHNOTFINISHEDINTIME = 'PrefetchNotFinishedInTime'
    PREFETCHNOTSTARTED = 'PrefetchNotStarted'
    PREFETCHNOTUSEDCOOKIESCHANGED = 'PrefetchNotUsedCookiesChanged'
    PREFETCHPROXYNOTAVAILABLE = 'PrefetchProxyNotAvailable'
    PREFETCHRESPONSEUSED = 'PrefetchResponseUsed'
    PREFETCHSUCCESSFULBUTNOTUSED = 'PrefetchSuccessfulButNotUsed'
    PREFETCHNOTUSEDPROBEFAILED = 'PrefetchNotUsedProbeFailed'


@register("Preload.PrerenderMismatchedHeaders")
@dataclass
class PrerenderMismatchedHeaders(DataType):
    """Information of headers to be displayed when the header mismatch occurred."""
    header_name: str
    initial_value: Optional[str] = None
    activation_value: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('header_name', 'headerName', False, 'primitive'),
        FieldMeta('initial_value', 'initialValue', True, 'primitive'),
        FieldMeta('activation_value', 'activationValue', True, 'primitive'),
    )

__all__ = ["PrefetchStatus", "PreloadPipelineId", "PreloadingAttemptKey", "PreloadingAttemptSource", "PreloadingStatus", "PrerenderFinalStatus", "PrerenderMismatchedHeaders", "RuleSet", "RuleSetErrorType", "RuleSetId", "SpeculationAction", "SpeculationTargetHint"]
