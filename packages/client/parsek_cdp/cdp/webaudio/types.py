"""Custom types and enums for the WebAudio domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


type GraphObjectId = str  # An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API


@register("WebAudio.ContextType")
class ContextType(str, Enum):
    """Enum of BaseAudioContext types"""
    REALTIME = 'realtime'
    OFFLINE = 'offline'


@register("WebAudio.ContextState")
class ContextState(str, Enum):
    """Enum of AudioContextState from the spec"""
    SUSPENDED = 'suspended'
    RUNNING = 'running'
    CLOSED = 'closed'
    INTERRUPTED = 'interrupted'


type NodeType = str  # Enum of AudioNode types


@register("WebAudio.ChannelCountMode")
class ChannelCountMode(str, Enum):
    """Enum of AudioNode::ChannelCountMode from the spec"""
    CLAMPED_MAX = 'clamped-max'
    EXPLICIT = 'explicit'
    MAX = 'max'


@register("WebAudio.ChannelInterpretation")
class ChannelInterpretation(str, Enum):
    """Enum of AudioNode::ChannelInterpretation from the spec"""
    DISCRETE = 'discrete'
    SPEAKERS = 'speakers'


type ParamType = str  # Enum of AudioParam types


@register("WebAudio.AutomationRate")
class AutomationRate(str, Enum):
    """Enum of AudioParam::AutomationRate from the spec"""
    A_RATE = 'a-rate'
    K_RATE = 'k-rate'


@register("WebAudio.ContextRealtimeData")
@dataclass
class ContextRealtimeData(DataType):
    """Fields in AudioContext that change in real-time."""
    current_time: float
    render_capacity: float
    callback_interval_mean: float
    callback_interval_variance: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('current_time', 'currentTime', False, 'primitive'),
        FieldMeta('render_capacity', 'renderCapacity', False, 'primitive'),
        FieldMeta('callback_interval_mean', 'callbackIntervalMean', False, 'primitive'),
        FieldMeta('callback_interval_variance', 'callbackIntervalVariance', False, 'primitive'),
    )


@register("WebAudio.BaseAudioContext")
@dataclass
class BaseAudioContext(DataType):
    """Protocol object for BaseAudioContext"""
    context_id: GraphObjectId
    context_type: ContextType
    context_state: ContextState
    callback_buffer_size: float
    max_output_channel_count: float
    sample_rate: float
    realtime_data: Optional[ContextRealtimeData] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('context_type', 'contextType', False, 'enum', ref='WebAudio.ContextType'),
        FieldMeta('context_state', 'contextState', False, 'enum', ref='WebAudio.ContextState'),
        FieldMeta('callback_buffer_size', 'callbackBufferSize', False, 'primitive'),
        FieldMeta('max_output_channel_count', 'maxOutputChannelCount', False, 'primitive'),
        FieldMeta('sample_rate', 'sampleRate', False, 'primitive'),
        FieldMeta('realtime_data', 'realtimeData', True, 'object', ref='WebAudio.ContextRealtimeData'),
    )


@register("WebAudio.AudioListener")
@dataclass
class AudioListener(DataType):
    """Protocol object for AudioListener"""
    listener_id: GraphObjectId
    context_id: GraphObjectId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('listener_id', 'listenerId', False, 'primitive'),
        FieldMeta('context_id', 'contextId', False, 'primitive'),
    )


@register("WebAudio.AudioNode")
@dataclass
class AudioNode(DataType):
    """Protocol object for AudioNode"""
    node_id: GraphObjectId
    context_id: GraphObjectId
    node_type: NodeType
    number_of_inputs: float
    number_of_outputs: float
    channel_count: float
    channel_count_mode: ChannelCountMode
    channel_interpretation: ChannelInterpretation
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('node_type', 'nodeType', False, 'primitive'),
        FieldMeta('number_of_inputs', 'numberOfInputs', False, 'primitive'),
        FieldMeta('number_of_outputs', 'numberOfOutputs', False, 'primitive'),
        FieldMeta('channel_count', 'channelCount', False, 'primitive'),
        FieldMeta('channel_count_mode', 'channelCountMode', False, 'enum', ref='WebAudio.ChannelCountMode'),
        FieldMeta('channel_interpretation', 'channelInterpretation', False, 'enum', ref='WebAudio.ChannelInterpretation'),
    )


@register("WebAudio.AudioParam")
@dataclass
class AudioParam(DataType):
    """Protocol object for AudioParam"""
    param_id: GraphObjectId
    node_id: GraphObjectId
    context_id: GraphObjectId
    param_type: ParamType
    rate: AutomationRate
    default_value: float
    min_value: float
    max_value: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('param_id', 'paramId', False, 'primitive'),
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('context_id', 'contextId', False, 'primitive'),
        FieldMeta('param_type', 'paramType', False, 'primitive'),
        FieldMeta('rate', 'rate', False, 'enum', ref='WebAudio.AutomationRate'),
        FieldMeta('default_value', 'defaultValue', False, 'primitive'),
        FieldMeta('min_value', 'minValue', False, 'primitive'),
        FieldMeta('max_value', 'maxValue', False, 'primitive'),
    )

__all__ = ["AudioListener", "AudioNode", "AudioParam", "AutomationRate", "BaseAudioContext", "ChannelCountMode", "ChannelInterpretation", "ContextRealtimeData", "ContextState", "ContextType", "GraphObjectId", "NodeType", "ParamType"]
