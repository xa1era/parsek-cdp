"""Commands for the HeadlessExperimental domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import ScreenshotParams

@dataclass
class BeginFrameReturn(DataType):
    """Return value of :meth:`HeadlessExperimental.begin_frame`."""
    has_damage: bool
    screenshot_data: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('has_damage', 'hasDamage', False, 'primitive'),
        FieldMeta('screenshot_data', 'screenshotData', True, 'primitive'),
    )


class HeadlessExperimental:
    """Commands of the HeadlessExperimental domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def begin_frame(self, *, frame_time_ticks: Optional[float] = None, interval: Optional[float] = None, no_display_updates: Optional[bool] = None, screenshot: Optional[ScreenshotParams] = None) -> BeginFrameReturn:
        """
        Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
        screenshot from the resulting frame. Requires that the target was created with enabled
        BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
        https://goo.gle/chrome-headless-rendering for more background.
        :param frame_time_ticks: Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
        the current time will be used.
        :param interval: The interval between BeginFrames that is reported to the compositor, in milliseconds.
        Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        :param no_display_updates: Whether updates should not be committed and drawn onto the display. False by default. If
        true, only side effects of the BeginFrame will be run, such as layout and animations, but
        any visual updates may not be visible on the display or in screenshots.
        :param screenshot: If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
        no screenshot will be captured. Note that capturing a screenshot can fail, for example,
        during renderer initialization. In such a case, no screenshot data will be returned.
        """
        _params: Dict[str, Any] = {}
        if frame_time_ticks is not None:
            _params['frameTimeTicks'] = encode(FieldMeta('', '', False, 'primitive'), frame_time_ticks)
        if interval is not None:
            _params['interval'] = encode(FieldMeta('', '', False, 'primitive'), interval)
        if no_display_updates is not None:
            _params['noDisplayUpdates'] = encode(FieldMeta('', '', False, 'primitive'), no_display_updates)
        if screenshot is not None:
            _params['screenshot'] = encode(FieldMeta('', '', False, 'object', ref='HeadlessExperimental.ScreenshotParams'), screenshot)
        _result = await self._target.send('HeadlessExperimental.beginFrame', _params)
        return BeginFrameReturn.from_json(_result)

    async def disable(self) -> None:
        """
        Disables headless events for the target.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeadlessExperimental.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables headless events for the target.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('HeadlessExperimental.enable', _params)
        return None
