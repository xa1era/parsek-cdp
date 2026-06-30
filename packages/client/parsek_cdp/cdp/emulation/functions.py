"""Commands for the Emulation domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        DevicePosture,
        DisabledImageType,
        DisplayFeature,
        MediaFeature,
        PressureMetadata,
        PressureSource,
        PressureState,
        SafeAreaInsets,
        ScreenId,
        ScreenInfo,
        ScreenOrientation,
        SensorMetadata,
        SensorReading,
        SensorType,
        UserAgentMetadata,
        VirtualTimePolicy,
        WorkAreaInsets,
    )
    from ..dom.types import RGBA as DOM_RGBA
    from ..network.types import TimeSinceEpoch as Network_TimeSinceEpoch
    from ..page.types import Viewport as Page_Viewport

@dataclass
class CanEmulateReturn(DataType):
    """Return value of :meth:`Emulation.can_emulate`."""
    result: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('result', 'result', False, 'primitive'),
    )


@dataclass
class GetOverriddenSensorInformationReturn(DataType):
    """Return value of :meth:`Emulation.get_overridden_sensor_information`."""
    requested_sampling_frequency: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('requested_sampling_frequency', 'requestedSamplingFrequency', False, 'primitive'),
    )


@dataclass
class SetVirtualTimePolicyReturn(DataType):
    """Return value of :meth:`Emulation.set_virtual_time_policy`."""
    virtual_time_ticks_base: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('virtual_time_ticks_base', 'virtualTimeTicksBase', False, 'primitive'),
    )


@dataclass
class GetScreenInfosReturn(DataType):
    """Return value of :meth:`Emulation.get_screen_infos`."""
    screen_infos: List[ScreenInfo]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('screen_infos', 'screenInfos', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Emulation.ScreenInfo')),
    )


@dataclass
class AddScreenReturn(DataType):
    """Return value of :meth:`Emulation.add_screen`."""
    screen_info: ScreenInfo
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('screen_info', 'screenInfo', False, 'object', ref='Emulation.ScreenInfo'),
    )


class Emulation:
    """Commands of the Emulation domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def can_emulate(self) -> CanEmulateReturn:
        """
        Tells whether emulation is supported.
        
        .. deprecated::
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.canEmulate', _params)
        return CanEmulateReturn.from_json(_result)

    async def clear_device_metrics_override(self) -> None:
        """Clears the overridden device metrics."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.clearDeviceMetricsOverride', _params)
        return None

    async def clear_geolocation_override(self) -> None:
        """Clears the overridden Geolocation Position and Error."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.clearGeolocationOverride', _params)
        return None

    async def reset_page_scale_factor(self) -> None:
        """Requests that page scale factor is reset to initial values."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.resetPageScaleFactor', _params)
        return None

    async def set_focus_emulation_enabled(self, *, enabled: bool) -> None:
        """
        Enables or disables simulating a focused and active page.
        :param enabled: Whether to enable to disable focus emulation.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Emulation.setFocusEmulationEnabled', _params)
        return None

    async def set_auto_dark_mode_override(self, *, enabled: Optional[bool] = None) -> None:
        """
        Automatically render all web contents using a dark theme.
        :param enabled: Whether to enable or disable automatic dark mode.
        If not specified, any existing override will be cleared.
        """
        _params: Dict[str, Any] = {}
        if enabled is not None:
            _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Emulation.setAutoDarkModeOverride', _params)
        return None

    async def set_cpu_throttling_rate(self, *, rate: float) -> None:
        """
        Enables CPU throttling to emulate slow CPUs.
        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        """
        _params: Dict[str, Any] = {}
        _params['rate'] = encode(FieldMeta('', '', False, 'primitive'), rate)
        _result = await self._target.send('Emulation.setCPUThrottlingRate', _params)
        return None

    async def set_default_background_color_override(self, *, color: Optional[DOM_RGBA] = None) -> None:
        """
        Sets or clears an override of the default background color of the frame. This override is used
        if the content does not specify one.
        :param color: RGBA of the default background color. If not specified, any existing override will be
        cleared.
        """
        _params: Dict[str, Any] = {}
        if color is not None:
            _params['color'] = encode(FieldMeta('', '', False, 'object', ref='DOM.RGBA'), color)
        _result = await self._target.send('Emulation.setDefaultBackgroundColorOverride', _params)
        return None

    async def set_safe_area_insets_override(self, *, insets: SafeAreaInsets) -> None:
        """
        Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
        respective variables to be undefined, even if previously overridden.
        :param insets:
        """
        _params: Dict[str, Any] = {}
        _params['insets'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.SafeAreaInsets'), insets)
        _result = await self._target.send('Emulation.setSafeAreaInsetsOverride', _params)
        return None

    async def set_device_metrics_override(self, *, width: int, height: int, device_scale_factor: float, mobile: bool, scale: Optional[float] = None, screen_width: Optional[int] = None, screen_height: Optional[int] = None, position_x: Optional[int] = None, position_y: Optional[int] = None, dont_set_visible_size: Optional[bool] = None, screen_orientation: Optional[ScreenOrientation] = None, viewport: Optional[Page_Viewport] = None, display_feature: Optional[DisplayFeature] = None, device_posture: Optional[DevicePosture] = None) -> None:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
        window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
        query results).
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param device_scale_factor: Overriding device scale factor value. 0 disables the override.
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
        autosizing and more.
        :param scale: Scale to apply to resulting view image.
        :param screen_width: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :param screen_height: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :param position_x: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :param position_y: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :param dont_set_visible_size: Do not set visible view size, rely upon explicit setVisibleSize call.
        :param screen_orientation: Screen orientation override.
        :param viewport: If set, the visible area of the page will be overridden to this viewport. This viewport
        change is not observed by the page, e.g. viewport-relative elements do not change positions.
        :param display_feature: If set, the display feature of a multi-segment screen. If not set, multi-segment support
        is turned-off.
        Deprecated, use Emulation.setDisplayFeaturesOverride.
        :param device_posture: If set, the posture of a foldable device. If not set the posture is set
        to continuous.
        Deprecated, use Emulation.setDevicePostureOverride.
        """
        _params: Dict[str, Any] = {}
        _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        _params['deviceScaleFactor'] = encode(FieldMeta('', '', False, 'primitive'), device_scale_factor)
        _params['mobile'] = encode(FieldMeta('', '', False, 'primitive'), mobile)
        if scale is not None:
            _params['scale'] = encode(FieldMeta('', '', False, 'primitive'), scale)
        if screen_width is not None:
            _params['screenWidth'] = encode(FieldMeta('', '', False, 'primitive'), screen_width)
        if screen_height is not None:
            _params['screenHeight'] = encode(FieldMeta('', '', False, 'primitive'), screen_height)
        if position_x is not None:
            _params['positionX'] = encode(FieldMeta('', '', False, 'primitive'), position_x)
        if position_y is not None:
            _params['positionY'] = encode(FieldMeta('', '', False, 'primitive'), position_y)
        if dont_set_visible_size is not None:
            _params['dontSetVisibleSize'] = encode(FieldMeta('', '', False, 'primitive'), dont_set_visible_size)
        if screen_orientation is not None:
            _params['screenOrientation'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.ScreenOrientation'), screen_orientation)
        if viewport is not None:
            _params['viewport'] = encode(FieldMeta('', '', False, 'object', ref='Page.Viewport'), viewport)
        if display_feature is not None:
            _params['displayFeature'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.DisplayFeature'), display_feature)
        if device_posture is not None:
            _params['devicePosture'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.DevicePosture'), device_posture)
        _result = await self._target.send('Emulation.setDeviceMetricsOverride', _params)
        return None

    async def set_device_posture_override(self, *, posture: DevicePosture) -> None:
        """
        Start reporting the given posture value to the Device Posture API.
        This override can also be set in setDeviceMetricsOverride().
        :param posture:
        """
        _params: Dict[str, Any] = {}
        _params['posture'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.DevicePosture'), posture)
        _result = await self._target.send('Emulation.setDevicePostureOverride', _params)
        return None

    async def clear_device_posture_override(self) -> None:
        """
        Clears a device posture override set with either setDeviceMetricsOverride()
        or setDevicePostureOverride() and starts using posture information from the
        platform again.
        Does nothing if no override is set.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.clearDevicePostureOverride', _params)
        return None

    async def set_display_features_override(self, *, features: List[DisplayFeature]) -> None:
        """
        Start using the given display features to pupulate the Viewport Segments API.
        This override can also be set in setDeviceMetricsOverride().
        :param features:
        """
        _params: Dict[str, Any] = {}
        _params['features'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Emulation.DisplayFeature')), features)
        _result = await self._target.send('Emulation.setDisplayFeaturesOverride', _params)
        return None

    async def clear_display_features_override(self) -> None:
        """
        Clears the display features override set with either setDeviceMetricsOverride()
        or setDisplayFeaturesOverride() and starts using display features from the
        platform again.
        Does nothing if no override is set.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.clearDisplayFeaturesOverride', _params)
        return None

    async def set_scrollbars_hidden(self, *, hidden: bool) -> None:
        """:param hidden: Whether scrollbars should be always hidden."""
        _params: Dict[str, Any] = {}
        _params['hidden'] = encode(FieldMeta('', '', False, 'primitive'), hidden)
        _result = await self._target.send('Emulation.setScrollbarsHidden', _params)
        return None

    async def set_document_cookie_disabled(self, *, disabled: bool) -> None:
        """:param disabled: Whether document.coookie API should be disabled."""
        _params: Dict[str, Any] = {}
        _params['disabled'] = encode(FieldMeta('', '', False, 'primitive'), disabled)
        _result = await self._target.send('Emulation.setDocumentCookieDisabled', _params)
        return None

    async def set_emit_touch_events_for_mouse(self, *, enabled: bool, configuration: Optional[Literal['mobile', 'desktop']] = None) -> None:
        """
        :param enabled: Whether touch emulation based on mouse input should be enabled.
        :param configuration: Touch/gesture events configuration. Default: current platform.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        if configuration is not None:
            _params['configuration'] = encode(FieldMeta('', '', False, 'primitive'), configuration)
        _result = await self._target.send('Emulation.setEmitTouchEventsForMouse', _params)
        return None

    async def set_emulated_media(self, *, media: Optional[str] = None, features: Optional[List[MediaFeature]] = None) -> None:
        """
        Emulates the given media type or media feature for CSS media queries.
        :param media: Media type to emulate. Empty string disables the override.
        :param features: Media features to emulate.
        """
        _params: Dict[str, Any] = {}
        if media is not None:
            _params['media'] = encode(FieldMeta('', '', False, 'primitive'), media)
        if features is not None:
            _params['features'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Emulation.MediaFeature')), features)
        _result = await self._target.send('Emulation.setEmulatedMedia', _params)
        return None

    async def set_emulated_vision_deficiency(self, *, type_: Literal['none', 'blurredVision', 'reducedContrast', 'achromatopsia', 'deuteranopia', 'protanopia', 'tritanopia']) -> None:
        """
        Emulates the given vision deficiency.
        :param type_: Vision deficiency to emulate. Order: best-effort emulations come first, followed by any
        physiologically accurate emulations for medically recognized color vision deficiencies.
        """
        _params: Dict[str, Any] = {}
        _params['type'] = encode(FieldMeta('', '', False, 'primitive'), type_)
        _result = await self._target.send('Emulation.setEmulatedVisionDeficiency', _params)
        return None

    async def set_emulated_os_text_scale(self, *, scale: Optional[float] = None) -> None:
        """
        Emulates the given OS text scale.
        :param scale:
        """
        _params: Dict[str, Any] = {}
        if scale is not None:
            _params['scale'] = encode(FieldMeta('', '', False, 'primitive'), scale)
        _result = await self._target.send('Emulation.setEmulatedOSTextScale', _params)
        return None

    async def set_geolocation_override(self, *, latitude: Optional[float] = None, longitude: Optional[float] = None, accuracy: Optional[float] = None, altitude: Optional[float] = None, altitude_accuracy: Optional[float] = None, heading: Optional[float] = None, speed: Optional[float] = None) -> None:
        """
        Overrides the Geolocation Position or Error. Omitting latitude, longitude or
        accuracy emulates position unavailable.
        :param latitude: Mock latitude
        :param longitude: Mock longitude
        :param accuracy: Mock accuracy
        :param altitude: Mock altitude
        :param altitude_accuracy: Mock altitudeAccuracy
        :param heading: Mock heading
        :param speed: Mock speed
        """
        _params: Dict[str, Any] = {}
        if latitude is not None:
            _params['latitude'] = encode(FieldMeta('', '', False, 'primitive'), latitude)
        if longitude is not None:
            _params['longitude'] = encode(FieldMeta('', '', False, 'primitive'), longitude)
        if accuracy is not None:
            _params['accuracy'] = encode(FieldMeta('', '', False, 'primitive'), accuracy)
        if altitude is not None:
            _params['altitude'] = encode(FieldMeta('', '', False, 'primitive'), altitude)
        if altitude_accuracy is not None:
            _params['altitudeAccuracy'] = encode(FieldMeta('', '', False, 'primitive'), altitude_accuracy)
        if heading is not None:
            _params['heading'] = encode(FieldMeta('', '', False, 'primitive'), heading)
        if speed is not None:
            _params['speed'] = encode(FieldMeta('', '', False, 'primitive'), speed)
        _result = await self._target.send('Emulation.setGeolocationOverride', _params)
        return None

    async def get_overridden_sensor_information(self, *, type_: SensorType) -> GetOverriddenSensorInformationReturn:
        """:param type_:"""
        _params: Dict[str, Any] = {}
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.SensorType'), type_)
        _result = await self._target.send('Emulation.getOverriddenSensorInformation', _params)
        return GetOverriddenSensorInformationReturn.from_json(_result)

    async def set_sensor_override_enabled(self, *, enabled: bool, type_: SensorType, metadata: Optional[SensorMetadata] = None) -> None:
        """
        Overrides a platform sensor of a given type. If |enabled| is true, calls to
        Sensor.start() will use a virtual sensor as backend rather than fetching
        data from a real hardware sensor. Otherwise, existing virtual
        sensor-backend Sensor objects will fire an error event and new calls to
        Sensor.start() will attempt to use a real sensor instead.
        :param enabled:
        :param type_:
        :param metadata:
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.SensorType'), type_)
        if metadata is not None:
            _params['metadata'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.SensorMetadata'), metadata)
        _result = await self._target.send('Emulation.setSensorOverrideEnabled', _params)
        return None

    async def set_sensor_override_readings(self, *, type_: SensorType, reading: SensorReading) -> None:
        """
        Updates the sensor readings reported by a sensor type previously overridden
        by setSensorOverrideEnabled.
        :param type_:
        :param reading:
        """
        _params: Dict[str, Any] = {}
        _params['type'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.SensorType'), type_)
        _params['reading'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.SensorReading'), reading)
        _result = await self._target.send('Emulation.setSensorOverrideReadings', _params)
        return None

    async def set_pressure_source_override_enabled(self, *, enabled: bool, source: PressureSource, metadata: Optional[PressureMetadata] = None) -> None:
        """
        Overrides a pressure source of a given type, as used by the Compute
        Pressure API, so that updates to PressureObserver.observe() are provided
        via setPressureStateOverride instead of being retrieved from
        platform-provided telemetry data.
        :param enabled:
        :param source:
        :param metadata:
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _params['source'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.PressureSource'), source)
        if metadata is not None:
            _params['metadata'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.PressureMetadata'), metadata)
        _result = await self._target.send('Emulation.setPressureSourceOverrideEnabled', _params)
        return None

    async def set_pressure_state_override(self, *, source: PressureSource, state: PressureState) -> None:
        """
        TODO: OBSOLETE: To remove when setPressureDataOverride is merged.
        Provides a given pressure state that will be processed and eventually be
        delivered to PressureObserver users. |source| must have been previously
        overridden by setPressureSourceOverrideEnabled.
        :param source:
        :param state:
        """
        _params: Dict[str, Any] = {}
        _params['source'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.PressureSource'), source)
        _params['state'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.PressureState'), state)
        _result = await self._target.send('Emulation.setPressureStateOverride', _params)
        return None

    async def set_pressure_data_override(self, *, source: PressureSource, state: PressureState, own_contribution_estimate: Optional[float] = None) -> None:
        """
        Provides a given pressure data set that will be processed and eventually be
        delivered to PressureObserver users. |source| must have been previously
        overridden by setPressureSourceOverrideEnabled.
        :param source:
        :param state:
        :param own_contribution_estimate:
        """
        _params: Dict[str, Any] = {}
        _params['source'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.PressureSource'), source)
        _params['state'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.PressureState'), state)
        if own_contribution_estimate is not None:
            _params['ownContributionEstimate'] = encode(FieldMeta('', '', False, 'primitive'), own_contribution_estimate)
        _result = await self._target.send('Emulation.setPressureDataOverride', _params)
        return None

    async def set_idle_override(self, *, is_user_active: bool, is_screen_unlocked: bool) -> None:
        """
        Overrides the Idle state.
        :param is_user_active: Mock isUserActive
        :param is_screen_unlocked: Mock isScreenUnlocked
        """
        _params: Dict[str, Any] = {}
        _params['isUserActive'] = encode(FieldMeta('', '', False, 'primitive'), is_user_active)
        _params['isScreenUnlocked'] = encode(FieldMeta('', '', False, 'primitive'), is_screen_unlocked)
        _result = await self._target.send('Emulation.setIdleOverride', _params)
        return None

    async def clear_idle_override(self) -> None:
        """Clears Idle state overrides."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.clearIdleOverride', _params)
        return None

    async def set_navigator_overrides(self, *, platform: str) -> None:
        """
        Overrides value returned by the javascript navigator object.
        
        .. deprecated::
        :param platform: The platform navigator.platform should return.
        """
        _params: Dict[str, Any] = {}
        _params['platform'] = encode(FieldMeta('', '', False, 'primitive'), platform)
        _result = await self._target.send('Emulation.setNavigatorOverrides', _params)
        return None

    async def set_page_scale_factor(self, *, page_scale_factor: float) -> None:
        """
        Sets a specified page scale factor.
        :param page_scale_factor: Page scale factor.
        """
        _params: Dict[str, Any] = {}
        _params['pageScaleFactor'] = encode(FieldMeta('', '', False, 'primitive'), page_scale_factor)
        _result = await self._target.send('Emulation.setPageScaleFactor', _params)
        return None

    async def set_script_execution_disabled(self, *, value: bool) -> None:
        """
        Switches script execution in the page.
        :param value: Whether script execution should be disabled in the page.
        """
        _params: Dict[str, Any] = {}
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('Emulation.setScriptExecutionDisabled', _params)
        return None

    async def set_touch_emulation_enabled(self, *, enabled: bool, max_touch_points: Optional[int] = None) -> None:
        """
        Enables touch on platforms which do not support them.
        :param enabled: Whether the touch event emulation should be enabled.
        :param max_touch_points: Maximum touch points supported. Defaults to one.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        if max_touch_points is not None:
            _params['maxTouchPoints'] = encode(FieldMeta('', '', False, 'primitive'), max_touch_points)
        _result = await self._target.send('Emulation.setTouchEmulationEnabled', _params)
        return None

    async def set_virtual_time_policy(self, *, policy: VirtualTimePolicy, budget: Optional[float] = None, max_virtual_time_task_starvation_count: Optional[int] = None, initial_virtual_time: Optional[Network_TimeSinceEpoch] = None) -> SetVirtualTimePolicyReturn:
        """
        Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
        the current virtual time policy.  Note this supersedes any previous time budget.
        :param policy:
        :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
        virtualTimeBudgetExpired event is sent.
        :param max_virtual_time_task_starvation_count: If set this specifies the maximum number of tasks that can be run before virtual is forced
        forwards to prevent deadlock.
        :param initial_virtual_time: If set, base::Time::Now will be overridden to initially return this value.
        """
        _params: Dict[str, Any] = {}
        _params['policy'] = encode(FieldMeta('', '', False, 'enum', ref='Emulation.VirtualTimePolicy'), policy)
        if budget is not None:
            _params['budget'] = encode(FieldMeta('', '', False, 'primitive'), budget)
        if max_virtual_time_task_starvation_count is not None:
            _params['maxVirtualTimeTaskStarvationCount'] = encode(FieldMeta('', '', False, 'primitive'), max_virtual_time_task_starvation_count)
        if initial_virtual_time is not None:
            _params['initialVirtualTime'] = encode(FieldMeta('', '', False, 'primitive'), initial_virtual_time)
        _result = await self._target.send('Emulation.setVirtualTimePolicy', _params)
        return SetVirtualTimePolicyReturn.from_json(_result)

    async def set_locale_override(self, *, locale: Optional[str] = None) -> None:
        """
        Overrides default host system locale with the specified one.
        :param locale: ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and
        restores default host system locale.
        """
        _params: Dict[str, Any] = {}
        if locale is not None:
            _params['locale'] = encode(FieldMeta('', '', False, 'primitive'), locale)
        _result = await self._target.send('Emulation.setLocaleOverride', _params)
        return None

    async def set_timezone_override(self, *, timezone_id: str) -> None:
        """
        Overrides default host system timezone with the specified one.
        :param timezone_id: The timezone identifier. List of supported timezones:
        https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt
        If empty, disables the override and restores default host system timezone.
        """
        _params: Dict[str, Any] = {}
        _params['timezoneId'] = encode(FieldMeta('', '', False, 'primitive'), timezone_id)
        _result = await self._target.send('Emulation.setTimezoneOverride', _params)
        return None

    async def set_visible_size(self, *, width: int, height: int) -> None:
        """
        Resizes the frame/viewport of the page. Note that this does not affect the frame's container
        (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
        on Android.
        
        .. deprecated::
        :param width: Frame width (DIP).
        :param height: Frame height (DIP).
        """
        _params: Dict[str, Any] = {}
        _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        _result = await self._target.send('Emulation.setVisibleSize', _params)
        return None

    async def set_disabled_image_types(self, *, image_types: List[DisabledImageType]) -> None:
        """:param image_types: Image types to disable."""
        _params: Dict[str, Any] = {}
        _params['imageTypes'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'enum', ref='Emulation.DisabledImageType')), image_types)
        _result = await self._target.send('Emulation.setDisabledImageTypes', _params)
        return None

    async def set_data_saver_override(self, *, data_saver_enabled: Optional[bool] = None) -> None:
        """
        Override the value of navigator.connection.saveData
        :param data_saver_enabled: Override value. Omitting the parameter disables the override.
        """
        _params: Dict[str, Any] = {}
        if data_saver_enabled is not None:
            _params['dataSaverEnabled'] = encode(FieldMeta('', '', False, 'primitive'), data_saver_enabled)
        _result = await self._target.send('Emulation.setDataSaverOverride', _params)
        return None

    async def set_hardware_concurrency_override(self, *, hardware_concurrency: int) -> None:
        """:param hardware_concurrency: Hardware concurrency to report"""
        _params: Dict[str, Any] = {}
        _params['hardwareConcurrency'] = encode(FieldMeta('', '', False, 'primitive'), hardware_concurrency)
        _result = await self._target.send('Emulation.setHardwareConcurrencyOverride', _params)
        return None

    async def set_user_agent_override(self, *, user_agent: str, accept_language: Optional[str] = None, platform: Optional[str] = None, user_agent_metadata: Optional[UserAgentMetadata] = None) -> None:
        """
        Allows overriding user agent with the given string.
        `userAgentMetadata` must be set for Client Hint headers to be sent.
        :param user_agent: User agent to use.
        :param accept_language: Browser language to emulate.
        :param platform: The platform navigator.platform should return.
        :param user_agent_metadata: To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
        """
        _params: Dict[str, Any] = {}
        _params['userAgent'] = encode(FieldMeta('', '', False, 'primitive'), user_agent)
        if accept_language is not None:
            _params['acceptLanguage'] = encode(FieldMeta('', '', False, 'primitive'), accept_language)
        if platform is not None:
            _params['platform'] = encode(FieldMeta('', '', False, 'primitive'), platform)
        if user_agent_metadata is not None:
            _params['userAgentMetadata'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.UserAgentMetadata'), user_agent_metadata)
        _result = await self._target.send('Emulation.setUserAgentOverride', _params)
        return None

    async def set_automation_override(self, *, enabled: bool) -> None:
        """
        Allows overriding the automation flag.
        :param enabled: Whether the override should be enabled.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Emulation.setAutomationOverride', _params)
        return None

    async def set_small_viewport_height_difference_override(self, *, difference: int) -> None:
        """
        Allows overriding the difference between the small and large viewport sizes, which determine the
        value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.
        :param difference: This will cause an element of size 100svh to be `difference` pixels smaller than an element
        of size 100lvh.
        """
        _params: Dict[str, Any] = {}
        _params['difference'] = encode(FieldMeta('', '', False, 'primitive'), difference)
        _result = await self._target.send('Emulation.setSmallViewportHeightDifferenceOverride', _params)
        return None

    async def get_screen_infos(self) -> GetScreenInfosReturn:
        """Returns device's screen configuration."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Emulation.getScreenInfos', _params)
        return GetScreenInfosReturn.from_json(_result)

    async def add_screen(self, *, left: int, top: int, width: int, height: int, work_area_insets: Optional[WorkAreaInsets] = None, device_pixel_ratio: Optional[float] = None, rotation: Optional[int] = None, color_depth: Optional[int] = None, label: Optional[str] = None, is_internal: Optional[bool] = None) -> AddScreenReturn:
        """
        Add a new screen to the device. Only supported in headless mode.
        :param left: Offset of the left edge of the screen in pixels.
        :param top: Offset of the top edge of the screen in pixels.
        :param width: The width of the screen in pixels.
        :param height: The height of the screen in pixels.
        :param work_area_insets: Specifies the screen's work area. Default is entire screen.
        :param device_pixel_ratio: Specifies the screen's device pixel ratio. Default is 1.
        :param rotation: Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0.
        :param color_depth: Specifies the screen's color depth in bits. Default is 24.
        :param label: Specifies the descriptive label for the screen. Default is none.
        :param is_internal: Indicates whether the screen is internal to the device or external, attached to the device. Default is false.
        """
        _params: Dict[str, Any] = {}
        _params['left'] = encode(FieldMeta('', '', False, 'primitive'), left)
        _params['top'] = encode(FieldMeta('', '', False, 'primitive'), top)
        _params['width'] = encode(FieldMeta('', '', False, 'primitive'), width)
        _params['height'] = encode(FieldMeta('', '', False, 'primitive'), height)
        if work_area_insets is not None:
            _params['workAreaInsets'] = encode(FieldMeta('', '', False, 'object', ref='Emulation.WorkAreaInsets'), work_area_insets)
        if device_pixel_ratio is not None:
            _params['devicePixelRatio'] = encode(FieldMeta('', '', False, 'primitive'), device_pixel_ratio)
        if rotation is not None:
            _params['rotation'] = encode(FieldMeta('', '', False, 'primitive'), rotation)
        if color_depth is not None:
            _params['colorDepth'] = encode(FieldMeta('', '', False, 'primitive'), color_depth)
        if label is not None:
            _params['label'] = encode(FieldMeta('', '', False, 'primitive'), label)
        if is_internal is not None:
            _params['isInternal'] = encode(FieldMeta('', '', False, 'primitive'), is_internal)
        _result = await self._target.send('Emulation.addScreen', _params)
        return AddScreenReturn.from_json(_result)

    async def remove_screen(self, *, screen_id: ScreenId) -> None:
        """
        Remove screen from the device. Only supported in headless mode.
        :param screen_id:
        """
        _params: Dict[str, Any] = {}
        _params['screenId'] = encode(FieldMeta('', '', False, 'primitive'), screen_id)
        _result = await self._target.send('Emulation.removeScreen', _params)
        return None
