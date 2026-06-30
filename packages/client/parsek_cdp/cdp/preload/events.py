"""Events for the Preload domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        PrefetchStatus,
        PreloadPipelineId,
        PreloadingAttemptKey,
        PreloadingAttemptSource,
        PreloadingStatus,
        PrerenderFinalStatus,
        PrerenderMismatchedHeaders,
        RuleSet,
        RuleSetId,
    )
    from ..network.types import LoaderId as Network_LoaderId
    from ..network.types import RequestId as Network_RequestId
    from ..page.types import FrameId as Page_FrameId

@register_event("Preload.ruleSetUpdated")
@dataclass
class RuleSetUpdated(Event):
    """Upsert. Currently, it is only emitted when a rule set added."""
    rule_set: RuleSet
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule_set', 'ruleSet', False, 'object', ref='Preload.RuleSet'),
    )


@register_event("Preload.ruleSetRemoved")
@dataclass
class RuleSetRemoved(Event):
    id: RuleSetId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('id', 'id', False, 'primitive'),
    )


@register_event("Preload.preloadEnabledStateUpdated")
@dataclass
class PreloadEnabledStateUpdated(Event):
    """Fired when a preload enabled state is updated."""
    disabled_by_preference: bool
    disabled_by_data_saver: bool
    disabled_by_battery_saver: bool
    disabled_by_holdback_prefetch_speculation_rules: bool
    disabled_by_holdback_prerender_speculation_rules: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('disabled_by_preference', 'disabledByPreference', False, 'primitive'),
        FieldMeta('disabled_by_data_saver', 'disabledByDataSaver', False, 'primitive'),
        FieldMeta('disabled_by_battery_saver', 'disabledByBatterySaver', False, 'primitive'),
        FieldMeta('disabled_by_holdback_prefetch_speculation_rules', 'disabledByHoldbackPrefetchSpeculationRules', False, 'primitive'),
        FieldMeta('disabled_by_holdback_prerender_speculation_rules', 'disabledByHoldbackPrerenderSpeculationRules', False, 'primitive'),
    )


@register_event("Preload.prefetchStatusUpdated")
@dataclass
class PrefetchStatusUpdated(Event):
    """Fired when a prefetch attempt is updated."""
    key: PreloadingAttemptKey
    pipeline_id: PreloadPipelineId
    initiating_frame_id: Page_FrameId
    prefetch_url: str
    status: PreloadingStatus
    prefetch_status: PrefetchStatus
    request_id: Network_RequestId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'object', ref='Preload.PreloadingAttemptKey'),
        FieldMeta('pipeline_id', 'pipelineId', False, 'primitive'),
        FieldMeta('initiating_frame_id', 'initiatingFrameId', False, 'primitive'),
        FieldMeta('prefetch_url', 'prefetchUrl', False, 'primitive'),
        FieldMeta('status', 'status', False, 'enum', ref='Preload.PreloadingStatus'),
        FieldMeta('prefetch_status', 'prefetchStatus', False, 'enum', ref='Preload.PrefetchStatus'),
        FieldMeta('request_id', 'requestId', False, 'primitive'),
    )


@register_event("Preload.prerenderStatusUpdated")
@dataclass
class PrerenderStatusUpdated(Event):
    """Fired when a prerender attempt is updated."""
    key: PreloadingAttemptKey
    pipeline_id: PreloadPipelineId
    status: PreloadingStatus
    prerender_status: Optional[PrerenderFinalStatus] = None
    disallowed_mojo_interface: Optional[str] = None
    mismatched_headers: Optional[List[PrerenderMismatchedHeaders]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key', 'key', False, 'object', ref='Preload.PreloadingAttemptKey'),
        FieldMeta('pipeline_id', 'pipelineId', False, 'primitive'),
        FieldMeta('status', 'status', False, 'enum', ref='Preload.PreloadingStatus'),
        FieldMeta('prerender_status', 'prerenderStatus', True, 'enum', ref='Preload.PrerenderFinalStatus'),
        FieldMeta('disallowed_mojo_interface', 'disallowedMojoInterface', True, 'primitive'),
        FieldMeta('mismatched_headers', 'mismatchedHeaders', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Preload.PrerenderMismatchedHeaders')),
    )


@register_event("Preload.preloadingAttemptSourcesUpdated")
@dataclass
class PreloadingAttemptSourcesUpdated(Event):
    """Send a list of sources for all preloading attempts in a document."""
    loader_id: Network_LoaderId
    preloading_attempt_sources: List[PreloadingAttemptSource]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('loader_id', 'loaderId', False, 'primitive'),
        FieldMeta('preloading_attempt_sources', 'preloadingAttemptSources', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Preload.PreloadingAttemptSource')),
    )

__all__ = ["PrefetchStatusUpdated", "PreloadEnabledStateUpdated", "PreloadingAttemptSourcesUpdated", "PrerenderStatusUpdated", "RuleSetRemoved", "RuleSetUpdated"]
