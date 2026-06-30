"""Commands for the Animation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from ..runtime.types import RemoteObject as Runtime_RemoteObject

@dataclass
class GetCurrentTimeReturn(DataType):
    """Return value of :meth:`Animation.get_current_time`."""
    current_time: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('current_time', 'currentTime', False, 'primitive'),
    )


@dataclass
class GetPlaybackRateReturn(DataType):
    """Return value of :meth:`Animation.get_playback_rate`."""
    playback_rate: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('playback_rate', 'playbackRate', False, 'primitive'),
    )


@dataclass
class ResolveAnimationReturn(DataType):
    """Return value of :meth:`Animation.resolve_animation`."""
    remote_object: Runtime_RemoteObject
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('remote_object', 'remoteObject', False, 'object', ref='Runtime.RemoteObject'),
    )


class Animation:
    """Commands of the Animation domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def disable(self) -> None:
        """Disables animation domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Animation.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables animation domain notifications."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Animation.enable', _params)
        return None

    async def get_current_time(self, *, id: str) -> GetCurrentTimeReturn:
        """
        Returns the current time of the an animation.
        :param id: Id of animation.
        """
        _params: Dict[str, Any] = {}
        _params['id'] = encode(FieldMeta('', '', False, 'primitive'), id)
        _result = await self._target.send('Animation.getCurrentTime', _params)
        return GetCurrentTimeReturn.from_json(_result)

    async def get_playback_rate(self) -> GetPlaybackRateReturn:
        """Gets the playback rate of the document timeline."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Animation.getPlaybackRate', _params)
        return GetPlaybackRateReturn.from_json(_result)

    async def release_animations(self, *, animations: List[str]) -> None:
        """
        Releases a set of animations to no longer be manipulated.
        :param animations: List of animation ids to seek.
        """
        _params: Dict[str, Any] = {}
        _params['animations'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), animations)
        _result = await self._target.send('Animation.releaseAnimations', _params)
        return None

    async def resolve_animation(self, *, animation_id: str) -> ResolveAnimationReturn:
        """
        Gets the remote object of the Animation.
        :param animation_id: Animation id.
        """
        _params: Dict[str, Any] = {}
        _params['animationId'] = encode(FieldMeta('', '', False, 'primitive'), animation_id)
        _result = await self._target.send('Animation.resolveAnimation', _params)
        return ResolveAnimationReturn.from_json(_result)

    async def seek_animations(self, *, animations: List[str], current_time: float) -> None:
        """
        Seek a set of animations to a particular time within each animation.
        :param animations: List of animation ids to seek.
        :param current_time: Set the current time of each animation.
        """
        _params: Dict[str, Any] = {}
        _params['animations'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), animations)
        _params['currentTime'] = encode(FieldMeta('', '', False, 'primitive'), current_time)
        _result = await self._target.send('Animation.seekAnimations', _params)
        return None

    async def set_paused(self, *, animations: List[str], paused: bool) -> None:
        """
        Sets the paused state of a set of animations.
        :param animations: Animations to set the pause state of.
        :param paused: Paused state to set to.
        """
        _params: Dict[str, Any] = {}
        _params['animations'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), animations)
        _params['paused'] = encode(FieldMeta('', '', False, 'primitive'), paused)
        _result = await self._target.send('Animation.setPaused', _params)
        return None

    async def set_playback_rate(self, *, playback_rate: float) -> None:
        """
        Sets the playback rate of the document timeline.
        :param playback_rate: Playback rate for animations on page
        """
        _params: Dict[str, Any] = {}
        _params['playbackRate'] = encode(FieldMeta('', '', False, 'primitive'), playback_rate)
        _result = await self._target.send('Animation.setPlaybackRate', _params)
        return None

    async def set_timing(self, *, animation_id: str, duration: float, delay: float) -> None:
        """
        Sets the timing of an animation node.
        :param animation_id: Animation id.
        :param duration: Duration of the animation.
        :param delay: Delay of the animation.
        """
        _params: Dict[str, Any] = {}
        _params['animationId'] = encode(FieldMeta('', '', False, 'primitive'), animation_id)
        _params['duration'] = encode(FieldMeta('', '', False, 'primitive'), duration)
        _params['delay'] = encode(FieldMeta('', '', False, 'primitive'), delay)
        _result = await self._target.send('Animation.setTiming', _params)
        return None
