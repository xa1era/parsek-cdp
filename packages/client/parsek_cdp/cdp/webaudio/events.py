"""Events for the WebAudio domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import FieldMeta
from ..mixins.event import Event, register_event

if TYPE_CHECKING:
    from .types import (
        AudioListener,
        AudioNode,
        AudioParam,
        BaseAudioContext,
        GraphObjectId,
    )

@register_event("WebAudio.contextCreated")
@dataclass
class ContextCreated(Event):
    """Notifies that a new BaseAudioContext has been created."""
    context: BaseAudioContext
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context', 'context', False, 'object', ref='WebAudio.BaseAudioContext'),
    )


@register_event("WebAudio.contextWillBeDestroyed")
@dataclass
class ContextWillBeDestroyed(Event):
    """Notifies that an existing BaseAudioContext will be destroyed."""
    context_id: GraphObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
    )


@register_event("WebAudio.contextChanged")
@dataclass
class ContextChanged(Event):
    """Notifies that existing BaseAudioContext has changed some properties (id stays the same).."""
    context: BaseAudioContext
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context', 'context', False, 'object', ref='WebAudio.BaseAudioContext'),
    )


@register_event("WebAudio.audioListenerCreated")
@dataclass
class AudioListenerCreated(Event):
    """Notifies that the construction of an AudioListener has finished."""
    listener: AudioListener
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('listener', 'listener', False, 'object', ref='WebAudio.AudioListener'),
    )


@register_event("WebAudio.audioListenerWillBeDestroyed")
@dataclass
class AudioListenerWillBeDestroyed(Event):
    """Notifies that a new AudioListener has been created."""
    context_id: GraphObjectId
    listener_id: GraphObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('listener_id', 'listenerId', False, 'primitive'),
    )


@register_event("WebAudio.audioNodeCreated")
@dataclass
class AudioNodeCreated(Event):
    """Notifies that a new AudioNode has been created."""
    node: AudioNode
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node', 'node', False, 'object', ref='WebAudio.AudioNode'),
    )


@register_event("WebAudio.audioNodeWillBeDestroyed")
@dataclass
class AudioNodeWillBeDestroyed(Event):
    """Notifies that an existing AudioNode has been destroyed."""
    context_id: GraphObjectId
    node_id: GraphObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
    )


@register_event("WebAudio.audioParamCreated")
@dataclass
class AudioParamCreated(Event):
    """Notifies that a new AudioParam has been created."""
    param: AudioParam
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('param', 'param', False, 'object', ref='WebAudio.AudioParam'),
    )


@register_event("WebAudio.audioParamWillBeDestroyed")
@dataclass
class AudioParamWillBeDestroyed(Event):
    """Notifies that an existing AudioParam has been destroyed."""
    context_id: GraphObjectId
    node_id: GraphObjectId
    param_id: GraphObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('param_id', 'paramId', False, 'primitive'),
    )


@register_event("WebAudio.nodesConnected")
@dataclass
class NodesConnected(Event):
    """Notifies that two AudioNodes are connected."""
    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: Optional[float] = None
    destination_input_index: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('source_id', 'sourceId', False, 'primitive'),
        FieldMeta('destination_id', 'destinationId', False, 'primitive'),
        FieldMeta('source_output_index', 'sourceOutputIndex', True, 'primitive'),
        FieldMeta('destination_input_index', 'destinationInputIndex', True, 'primitive'),
    )


@register_event("WebAudio.nodesDisconnected")
@dataclass
class NodesDisconnected(Event):
    """Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected."""
    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: Optional[float] = None
    destination_input_index: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('source_id', 'sourceId', False, 'primitive'),
        FieldMeta('destination_id', 'destinationId', False, 'primitive'),
        FieldMeta('source_output_index', 'sourceOutputIndex', True, 'primitive'),
        FieldMeta('destination_input_index', 'destinationInputIndex', True, 'primitive'),
    )


@register_event("WebAudio.nodeParamConnected")
@dataclass
class NodeParamConnected(Event):
    """Notifies that an AudioNode is connected to an AudioParam."""
    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('source_id', 'sourceId', False, 'primitive'),
        FieldMeta('destination_id', 'destinationId', False, 'primitive'),
        FieldMeta('source_output_index', 'sourceOutputIndex', True, 'primitive'),
    )


@register_event("WebAudio.nodeParamDisconnected")
@dataclass
class NodeParamDisconnected(Event):
    """Notifies that an AudioNode is disconnected to an AudioParam."""
    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('source_id', 'sourceId', False, 'primitive'),
        FieldMeta('destination_id', 'destinationId', False, 'primitive'),
        FieldMeta('source_output_index', 'sourceOutputIndex', True, 'primitive'),
    )

__all__ = ["AudioListenerCreated", "AudioListenerWillBeDestroyed", "AudioNodeCreated", "AudioNodeWillBeDestroyed", "AudioParamCreated", "AudioParamWillBeDestroyed", "ContextChanged", "ContextCreated", "ContextWillBeDestroyed", "NodeParamConnected", "NodeParamDisconnected", "NodesConnected", "NodesDisconnected"]
