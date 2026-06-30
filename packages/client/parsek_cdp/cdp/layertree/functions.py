"""Commands for the LayerTree domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        LayerId,
        PaintProfile,
        PictureTile,
        SnapshotId,
    )
    from ..dom.types import Rect as DOM_Rect

@dataclass
class CompositingReasonsReturn(DataType):
    """Return value of :meth:`LayerTree.compositing_reasons`."""
    compositing_reasons: List[str]
    compositing_reason_ids: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('compositing_reasons', 'compositingReasons', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('compositing_reason_ids', 'compositingReasonIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class LoadSnapshotReturn(DataType):
    """Return value of :meth:`LayerTree.load_snapshot`."""
    snapshot_id: SnapshotId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('snapshot_id', 'snapshotId', False, 'primitive'),
    )


@dataclass
class MakeSnapshotReturn(DataType):
    """Return value of :meth:`LayerTree.make_snapshot`."""
    snapshot_id: SnapshotId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('snapshot_id', 'snapshotId', False, 'primitive'),
    )


@dataclass
class ProfileSnapshotReturn(DataType):
    """Return value of :meth:`LayerTree.profile_snapshot`."""
    timings: List[PaintProfile]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('timings', 'timings', False, 'array', inner=FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive'))),
    )


@dataclass
class ReplaySnapshotReturn(DataType):
    """Return value of :meth:`LayerTree.replay_snapshot`."""
    data_url: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('data_url', 'dataURL', False, 'primitive'),
    )


@dataclass
class SnapshotCommandLogReturn(DataType):
    """Return value of :meth:`LayerTree.snapshot_command_log`."""
    command_log: List[Dict[str, Any]]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('command_log', 'commandLog', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class LayerTree:
    """Commands of the LayerTree domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def compositing_reasons(self, *, layer_id: LayerId) -> CompositingReasonsReturn:
        """
        Provides the reasons why the given layer was composited.
        :param layer_id: The id of the layer for which we want to get the reasons it was composited.
        """
        _params: Dict[str, Any] = {}
        _params['layerId'] = encode(FieldMeta('', '', False, 'primitive'), layer_id)
        _result = await self._target.send('LayerTree.compositingReasons', _params)
        return CompositingReasonsReturn.from_json(_result)

    async def disable(self) -> None:
        """Disables compositing tree inspection."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('LayerTree.disable', _params)
        return None

    async def enable(self) -> None:
        """Enables compositing tree inspection."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('LayerTree.enable', _params)
        return None

    async def load_snapshot(self, *, tiles: List[PictureTile]) -> LoadSnapshotReturn:
        """
        Returns the snapshot identifier.
        :param tiles: An array of tiles composing the snapshot.
        """
        _params: Dict[str, Any] = {}
        _params['tiles'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='LayerTree.PictureTile')), tiles)
        _result = await self._target.send('LayerTree.loadSnapshot', _params)
        return LoadSnapshotReturn.from_json(_result)

    async def make_snapshot(self, *, layer_id: LayerId) -> MakeSnapshotReturn:
        """
        Returns the layer snapshot identifier.
        :param layer_id: The id of the layer.
        """
        _params: Dict[str, Any] = {}
        _params['layerId'] = encode(FieldMeta('', '', False, 'primitive'), layer_id)
        _result = await self._target.send('LayerTree.makeSnapshot', _params)
        return MakeSnapshotReturn.from_json(_result)

    async def profile_snapshot(self, *, snapshot_id: SnapshotId, min_repeat_count: Optional[int] = None, min_duration: Optional[float] = None, clip_rect: Optional[DOM_Rect] = None) -> ProfileSnapshotReturn:
        """
        :param snapshot_id: The id of the layer snapshot.
        :param min_repeat_count: The maximum number of times to replay the snapshot (1, if not specified).
        :param min_duration: The minimum duration (in seconds) to replay the snapshot.
        :param clip_rect: The clip rectangle to apply when replaying the snapshot.
        """
        _params: Dict[str, Any] = {}
        _params['snapshotId'] = encode(FieldMeta('', '', False, 'primitive'), snapshot_id)
        if min_repeat_count is not None:
            _params['minRepeatCount'] = encode(FieldMeta('', '', False, 'primitive'), min_repeat_count)
        if min_duration is not None:
            _params['minDuration'] = encode(FieldMeta('', '', False, 'primitive'), min_duration)
        if clip_rect is not None:
            _params['clipRect'] = encode(FieldMeta('', '', False, 'object', ref='DOM.Rect'), clip_rect)
        _result = await self._target.send('LayerTree.profileSnapshot', _params)
        return ProfileSnapshotReturn.from_json(_result)

    async def release_snapshot(self, *, snapshot_id: SnapshotId) -> None:
        """
        Releases layer snapshot captured by the back-end.
        :param snapshot_id: The id of the layer snapshot.
        """
        _params: Dict[str, Any] = {}
        _params['snapshotId'] = encode(FieldMeta('', '', False, 'primitive'), snapshot_id)
        _result = await self._target.send('LayerTree.releaseSnapshot', _params)
        return None

    async def replay_snapshot(self, *, snapshot_id: SnapshotId, from_step: Optional[int] = None, to_step: Optional[int] = None, scale: Optional[float] = None) -> ReplaySnapshotReturn:
        """
        Replays the layer snapshot and returns the resulting bitmap.
        :param snapshot_id: The id of the layer snapshot.
        :param from_step: The first step to replay from (replay from the very start if not specified).
        :param to_step: The last step to replay to (replay till the end if not specified).
        :param scale: The scale to apply while replaying (defaults to 1).
        """
        _params: Dict[str, Any] = {}
        _params['snapshotId'] = encode(FieldMeta('', '', False, 'primitive'), snapshot_id)
        if from_step is not None:
            _params['fromStep'] = encode(FieldMeta('', '', False, 'primitive'), from_step)
        if to_step is not None:
            _params['toStep'] = encode(FieldMeta('', '', False, 'primitive'), to_step)
        if scale is not None:
            _params['scale'] = encode(FieldMeta('', '', False, 'primitive'), scale)
        _result = await self._target.send('LayerTree.replaySnapshot', _params)
        return ReplaySnapshotReturn.from_json(_result)

    async def snapshot_command_log(self, *, snapshot_id: SnapshotId) -> SnapshotCommandLogReturn:
        """
        Replays the layer snapshot and returns canvas log.
        :param snapshot_id: The id of the layer snapshot.
        """
        _params: Dict[str, Any] = {}
        _params['snapshotId'] = encode(FieldMeta('', '', False, 'primitive'), snapshot_id)
        _result = await self._target.send('LayerTree.snapshotCommandLog', _params)
        return SnapshotCommandLogReturn.from_json(_result)
