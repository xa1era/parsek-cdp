"""Commands for the CSS domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        CSSAnimationStyle,
        CSSAtRule,
        CSSComputedStyleProperty,
        CSSContainerQuery,
        CSSFunctionRule,
        CSSKeyframesRule,
        CSSLayerData,
        CSSMedia,
        CSSPositionTryRule,
        CSSProperty,
        CSSPropertyRegistration,
        CSSPropertyRule,
        CSSRule,
        CSSScope,
        CSSStyle,
        CSSSupports,
        ComputedStyleExtraFields,
        InheritedAnimatedStyleEntry,
        InheritedPseudoElementMatches,
        InheritedStyleEntry,
        PlatformFontUsage,
        PseudoElementMatches,
        RuleMatch,
        RuleUsage,
        SelectorList,
        SourceRange,
        StyleDeclarationEdit,
        Value,
    )
    from ..dom.types import NodeId as DOM_NodeId
    from ..dom.types import PseudoType as DOM_PseudoType
    from ..dom.types import StyleSheetId as DOM_StyleSheetId
    from ..page.types import FrameId as Page_FrameId

@dataclass
class AddRuleReturn(DataType):
    """Return value of :meth:`CSS.add_rule`."""
    rule: CSSRule
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule', 'rule', False, 'object', ref='CSS.CSSRule'),
    )


@dataclass
class CollectClassNamesReturn(DataType):
    """Return value of :meth:`CSS.collect_class_names`."""
    class_names: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('class_names', 'classNames', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class CreateStyleSheetReturn(DataType):
    """Return value of :meth:`CSS.create_style_sheet`."""
    style_sheet_id: DOM_StyleSheetId
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
    )


@dataclass
class GetBackgroundColorsReturn(DataType):
    """Return value of :meth:`CSS.get_background_colors`."""
    background_colors: Optional[List[str]] = None
    computed_font_size: Optional[str] = None
    computed_font_weight: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('background_colors', 'backgroundColors', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('computed_font_size', 'computedFontSize', True, 'primitive'),
        FieldMeta('computed_font_weight', 'computedFontWeight', True, 'primitive'),
    )


@dataclass
class GetComputedStyleForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_computed_style_for_node`."""
    computed_style: List[CSSComputedStyleProperty]
    extra_fields: ComputedStyleExtraFields
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('computed_style', 'computedStyle', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSComputedStyleProperty')),
        FieldMeta('extra_fields', 'extraFields', False, 'object', ref='CSS.ComputedStyleExtraFields'),
    )


@dataclass
class ResolveValuesReturn(DataType):
    """Return value of :meth:`CSS.resolve_values`."""
    results: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('results', 'results', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class GetLonghandPropertiesReturn(DataType):
    """Return value of :meth:`CSS.get_longhand_properties`."""
    longhand_properties: List[CSSProperty]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('longhand_properties', 'longhandProperties', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSProperty')),
    )


@dataclass
class GetInlineStylesForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_inline_styles_for_node`."""
    inline_style: Optional[CSSStyle] = None
    attributes_style: Optional[CSSStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('inline_style', 'inlineStyle', True, 'object', ref='CSS.CSSStyle'),
        FieldMeta('attributes_style', 'attributesStyle', True, 'object', ref='CSS.CSSStyle'),
    )


@dataclass
class GetAnimatedStylesForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_animated_styles_for_node`."""
    animation_styles: Optional[List[CSSAnimationStyle]] = None
    transitions_style: Optional[CSSStyle] = None
    inherited: Optional[List[InheritedAnimatedStyleEntry]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('animation_styles', 'animationStyles', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSAnimationStyle')),
        FieldMeta('transitions_style', 'transitionsStyle', True, 'object', ref='CSS.CSSStyle'),
        FieldMeta('inherited', 'inherited', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.InheritedAnimatedStyleEntry')),
    )


@dataclass
class GetMatchedStylesForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_matched_styles_for_node`."""
    inline_style: Optional[CSSStyle] = None
    attributes_style: Optional[CSSStyle] = None
    matched_css_rules: Optional[List[RuleMatch]] = None
    pseudo_elements: Optional[List[PseudoElementMatches]] = None
    inherited: Optional[List[InheritedStyleEntry]] = None
    inherited_pseudo_elements: Optional[List[InheritedPseudoElementMatches]] = None
    css_keyframes_rules: Optional[List[CSSKeyframesRule]] = None
    css_position_try_rules: Optional[List[CSSPositionTryRule]] = None
    active_position_fallback_index: Optional[int] = None
    css_property_rules: Optional[List[CSSPropertyRule]] = None
    css_property_registrations: Optional[List[CSSPropertyRegistration]] = None
    css_at_rules: Optional[List[CSSAtRule]] = None
    parent_layout_node_id: Optional[DOM_NodeId] = None
    css_function_rules: Optional[List[CSSFunctionRule]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('inline_style', 'inlineStyle', True, 'object', ref='CSS.CSSStyle'),
        FieldMeta('attributes_style', 'attributesStyle', True, 'object', ref='CSS.CSSStyle'),
        FieldMeta('matched_css_rules', 'matchedCSSRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.RuleMatch')),
        FieldMeta('pseudo_elements', 'pseudoElements', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.PseudoElementMatches')),
        FieldMeta('inherited', 'inherited', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.InheritedStyleEntry')),
        FieldMeta('inherited_pseudo_elements', 'inheritedPseudoElements', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.InheritedPseudoElementMatches')),
        FieldMeta('css_keyframes_rules', 'cssKeyframesRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSKeyframesRule')),
        FieldMeta('css_position_try_rules', 'cssPositionTryRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSPositionTryRule')),
        FieldMeta('active_position_fallback_index', 'activePositionFallbackIndex', True, 'primitive'),
        FieldMeta('css_property_rules', 'cssPropertyRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSPropertyRule')),
        FieldMeta('css_property_registrations', 'cssPropertyRegistrations', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSPropertyRegistration')),
        FieldMeta('css_at_rules', 'cssAtRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSAtRule')),
        FieldMeta('parent_layout_node_id', 'parentLayoutNodeId', True, 'primitive'),
        FieldMeta('css_function_rules', 'cssFunctionRules', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSFunctionRule')),
    )


@dataclass
class GetEnvironmentVariablesReturn(DataType):
    """Return value of :meth:`CSS.get_environment_variables`."""
    environment_variables: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('environment_variables', 'environmentVariables', False, 'primitive'),
    )


@dataclass
class GetMediaQueriesReturn(DataType):
    """Return value of :meth:`CSS.get_media_queries`."""
    medias: List[CSSMedia]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('medias', 'medias', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSMedia')),
    )


@dataclass
class GetPlatformFontsForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_platform_fonts_for_node`."""
    fonts: List[PlatformFontUsage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('fonts', 'fonts', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.PlatformFontUsage')),
    )


@dataclass
class GetStyleSheetTextReturn(DataType):
    """Return value of :meth:`CSS.get_style_sheet_text`."""
    text: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
    )


@dataclass
class GetLayersForNodeReturn(DataType):
    """Return value of :meth:`CSS.get_layers_for_node`."""
    root_layer: CSSLayerData
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('root_layer', 'rootLayer', False, 'object', ref='CSS.CSSLayerData'),
    )


@dataclass
class GetLocationForSelectorReturn(DataType):
    """Return value of :meth:`CSS.get_location_for_selector`."""
    ranges: List[SourceRange]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('ranges', 'ranges', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.SourceRange')),
    )


@dataclass
class TakeComputedStyleUpdatesReturn(DataType):
    """Return value of :meth:`CSS.take_computed_style_updates`."""
    node_ids: List[DOM_NodeId]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_ids', 'nodeIds', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class SetPropertyRulePropertyNameReturn(DataType):
    """Return value of :meth:`CSS.set_property_rule_property_name`."""
    property_name: Value
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('property_name', 'propertyName', False, 'object', ref='CSS.Value'),
    )


@dataclass
class SetKeyframeKeyReturn(DataType):
    """Return value of :meth:`CSS.set_keyframe_key`."""
    key_text: Value
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('key_text', 'keyText', False, 'object', ref='CSS.Value'),
    )


@dataclass
class SetMediaTextReturn(DataType):
    """Return value of :meth:`CSS.set_media_text`."""
    media: CSSMedia
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('media', 'media', False, 'object', ref='CSS.CSSMedia'),
    )


@dataclass
class SetContainerQueryTextReturn(DataType):
    """Return value of :meth:`CSS.set_container_query_text`."""
    container_query: CSSContainerQuery
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('container_query', 'containerQuery', False, 'object', ref='CSS.CSSContainerQuery'),
    )


@dataclass
class SetSupportsTextReturn(DataType):
    """Return value of :meth:`CSS.set_supports_text`."""
    supports: CSSSupports
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('supports', 'supports', False, 'object', ref='CSS.CSSSupports'),
    )


@dataclass
class SetScopeTextReturn(DataType):
    """Return value of :meth:`CSS.set_scope_text`."""
    scope: CSSScope
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('scope', 'scope', False, 'object', ref='CSS.CSSScope'),
    )


@dataclass
class SetRuleSelectorReturn(DataType):
    """Return value of :meth:`CSS.set_rule_selector`."""
    selector_list: SelectorList
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('selector_list', 'selectorList', False, 'object', ref='CSS.SelectorList'),
    )


@dataclass
class SetStyleSheetTextReturn(DataType):
    """Return value of :meth:`CSS.set_style_sheet_text`."""
    source_map_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('source_map_url', 'sourceMapURL', True, 'primitive'),
    )


@dataclass
class SetStyleTextsReturn(DataType):
    """Return value of :meth:`CSS.set_style_texts`."""
    styles: List[CSSStyle]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('styles', 'styles', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSStyle')),
    )


@dataclass
class StopRuleUsageTrackingReturn(DataType):
    """Return value of :meth:`CSS.stop_rule_usage_tracking`."""
    rule_usage: List[RuleUsage]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule_usage', 'ruleUsage', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.RuleUsage')),
    )


@dataclass
class TakeCoverageDeltaReturn(DataType):
    """Return value of :meth:`CSS.take_coverage_delta`."""
    coverage: List[RuleUsage]
    timestamp: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('coverage', 'coverage', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.RuleUsage')),
        FieldMeta('timestamp', 'timestamp', False, 'primitive'),
    )


class CSS:
    """Commands of the CSS domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def add_rule(self, *, style_sheet_id: DOM_StyleSheetId, rule_text: str, location: SourceRange, node_for_property_syntax_validation: Optional[DOM_NodeId] = None) -> AddRuleReturn:
        """
        Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
        position specified by `location`.
        :param style_sheet_id: The css style sheet identifier where a new rule should be inserted.
        :param rule_text: The text of a new rule.
        :param location: Text position of a new rule in the target style sheet.
        :param node_for_property_syntax_validation: NodeId for the DOM node in whose context custom property declarations for registered properties should be
        validated. If omitted, declarations in the new rule text can only be validated statically, which may produce
        incorrect results if the declaration contains a var() for example.
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['ruleText'] = encode(FieldMeta('', '', False, 'primitive'), rule_text)
        _params['location'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), location)
        if node_for_property_syntax_validation is not None:
            _params['nodeForPropertySyntaxValidation'] = encode(FieldMeta('', '', False, 'primitive'), node_for_property_syntax_validation)
        _result = await self._target.send('CSS.addRule', _params)
        return AddRuleReturn.from_json(_result)

    async def collect_class_names(self, *, style_sheet_id: DOM_StyleSheetId) -> CollectClassNamesReturn:
        """
        Returns all class names from specified stylesheet.
        :param style_sheet_id:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _result = await self._target.send('CSS.collectClassNames', _params)
        return CollectClassNamesReturn.from_json(_result)

    async def create_style_sheet(self, *, frame_id: Page_FrameId, force: Optional[bool] = None) -> CreateStyleSheetReturn:
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.
        :param frame_id: Identifier of the frame where "via-inspector" stylesheet should be created.
        :param force: If true, creates a new stylesheet for every call. If false,
        returns a stylesheet previously created by a call with force=false
        for the frame's document if it exists or creates a new stylesheet
        (default: false).
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        if force is not None:
            _params['force'] = encode(FieldMeta('', '', False, 'primitive'), force)
        _result = await self._target.send('CSS.createStyleSheet', _params)
        return CreateStyleSheetReturn.from_json(_result)

    async def disable(self) -> None:
        """Disables the CSS agent for the given page."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.disable', _params)
        return None

    async def enable(self) -> None:
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
        enabled until the result of this command is received.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.enable', _params)
        return None

    async def force_pseudo_state(self, *, node_id: DOM_NodeId, forced_pseudo_classes: List[str]) -> None:
        """
        Ensures that the given node will have specified pseudo-classes whenever its style is computed by
        the browser.
        :param node_id: The element id for which to force the pseudo state.
        :param forced_pseudo_classes: Element pseudo classes to force when computing the element's style.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['forcedPseudoClasses'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), forced_pseudo_classes)
        _result = await self._target.send('CSS.forcePseudoState', _params)
        return None

    async def force_starting_style(self, *, node_id: DOM_NodeId, forced: bool) -> None:
        """
        Ensures that the given node is in its starting-style state.
        :param node_id: The element id for which to force the starting-style state.
        :param forced: Boolean indicating if this is on or off.
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['forced'] = encode(FieldMeta('', '', False, 'primitive'), forced)
        _result = await self._target.send('CSS.forceStartingStyle', _params)
        return None

    async def get_background_colors(self, *, node_id: DOM_NodeId) -> GetBackgroundColorsReturn:
        """:param node_id: Id of the node to get background colors for."""
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getBackgroundColors', _params)
        return GetBackgroundColorsReturn.from_json(_result)

    async def get_computed_style_for_node(self, *, node_id: DOM_NodeId) -> GetComputedStyleForNodeReturn:
        """
        Returns the computed style for a DOM node identified by `nodeId`.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getComputedStyleForNode', _params)
        return GetComputedStyleForNodeReturn.from_json(_result)

    async def resolve_values(self, *, values: List[str], node_id: DOM_NodeId, property_name: Optional[str] = None, pseudo_type: Optional[DOM_PseudoType] = None, pseudo_identifier: Optional[str] = None) -> ResolveValuesReturn:
        """
        Resolve the specified values in the context of the provided element.
        For example, a value of '1em' is evaluated according to the computed
        'font-size' of the element and a value 'calc(1px + 2px)' will be
        resolved to '3px'.
        If the `propertyName` was specified the `values` are resolved as if
        they were property's declaration. If a value cannot be parsed according
        to the provided property syntax, the value is parsed using combined
        syntax as if null `propertyName` was provided. If the value cannot be
        resolved even then, return the provided value without any changes.
        :param values: Cascade-dependent keywords (revert/revert-layer) do not work.
        :param node_id: Id of the node in whose context the expression is evaluated
        :param property_name: Only longhands and custom property names are accepted.
        :param pseudo_type: Pseudo element type, only works for pseudo elements that generate
        elements in the tree, such as ::before and ::after.
        :param pseudo_identifier: Pseudo element custom ident.
        """
        _params: Dict[str, Any] = {}
        _params['values'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), values)
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        if property_name is not None:
            _params['propertyName'] = encode(FieldMeta('', '', False, 'primitive'), property_name)
        if pseudo_type is not None:
            _params['pseudoType'] = encode(FieldMeta('', '', False, 'enum', ref='DOM.PseudoType'), pseudo_type)
        if pseudo_identifier is not None:
            _params['pseudoIdentifier'] = encode(FieldMeta('', '', False, 'primitive'), pseudo_identifier)
        _result = await self._target.send('CSS.resolveValues', _params)
        return ResolveValuesReturn.from_json(_result)

    async def get_longhand_properties(self, *, shorthand_name: str, value: str) -> GetLonghandPropertiesReturn:
        """
        :param shorthand_name:
        :param value:
        """
        _params: Dict[str, Any] = {}
        _params['shorthandName'] = encode(FieldMeta('', '', False, 'primitive'), shorthand_name)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('CSS.getLonghandProperties', _params)
        return GetLonghandPropertiesReturn.from_json(_result)

    async def get_inline_styles_for_node(self, *, node_id: DOM_NodeId) -> GetInlineStylesForNodeReturn:
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
        attributes) for a DOM node identified by `nodeId`.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getInlineStylesForNode', _params)
        return GetInlineStylesForNodeReturn.from_json(_result)

    async def get_animated_styles_for_node(self, *, node_id: DOM_NodeId) -> GetAnimatedStylesForNodeReturn:
        """
        Returns the styles coming from animations & transitions
        including the animation & transition styles coming from inheritance chain.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getAnimatedStylesForNode', _params)
        return GetAnimatedStylesForNodeReturn.from_json(_result)

    async def get_matched_styles_for_node(self, *, node_id: DOM_NodeId) -> GetMatchedStylesForNodeReturn:
        """
        Returns requested styles for a DOM node identified by `nodeId`.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getMatchedStylesForNode', _params)
        return GetMatchedStylesForNodeReturn.from_json(_result)

    async def get_environment_variables(self) -> GetEnvironmentVariablesReturn:
        """Returns the values of the default UA-defined environment variables used in env()"""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.getEnvironmentVariables', _params)
        return GetEnvironmentVariablesReturn.from_json(_result)

    async def get_media_queries(self) -> GetMediaQueriesReturn:
        """Returns all media queries parsed by the rendering engine."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.getMediaQueries', _params)
        return GetMediaQueriesReturn.from_json(_result)

    async def get_platform_fonts_for_node(self, *, node_id: DOM_NodeId) -> GetPlatformFontsForNodeReturn:
        """
        Requests information about platform fonts which we used to render child TextNodes in the given
        node.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getPlatformFontsForNode', _params)
        return GetPlatformFontsForNodeReturn.from_json(_result)

    async def get_style_sheet_text(self, *, style_sheet_id: DOM_StyleSheetId) -> GetStyleSheetTextReturn:
        """
        Returns the current textual content for a stylesheet.
        :param style_sheet_id:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _result = await self._target.send('CSS.getStyleSheetText', _params)
        return GetStyleSheetTextReturn.from_json(_result)

    async def get_layers_for_node(self, *, node_id: DOM_NodeId) -> GetLayersForNodeReturn:
        """
        Returns all layers parsed by the rendering engine for the tree scope of a node.
        Given a DOM element identified by nodeId, getLayersForNode returns the root
        layer for the nearest ancestor document or shadow root. The layer root contains
        the full layer tree for the tree scope and their ordering.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.getLayersForNode', _params)
        return GetLayersForNodeReturn.from_json(_result)

    async def get_location_for_selector(self, *, style_sheet_id: DOM_StyleSheetId, selector_text: str) -> GetLocationForSelectorReturn:
        """
        Given a CSS selector text and a style sheet ID, getLocationForSelector
        returns an array of locations of the CSS selector in the style sheet.
        :param style_sheet_id:
        :param selector_text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['selectorText'] = encode(FieldMeta('', '', False, 'primitive'), selector_text)
        _result = await self._target.send('CSS.getLocationForSelector', _params)
        return GetLocationForSelectorReturn.from_json(_result)

    async def track_computed_style_updates_for_node(self, *, node_id: Optional[DOM_NodeId] = None) -> None:
        """
        Starts tracking the given node for the computed style updates
        and whenever the computed style is updated for node, it queues
        a `computedStyleUpdated` event with throttling.
        There can only be 1 node tracked for computed style updates
        so passing a new node id removes tracking from the previous node.
        Pass `undefined` to disable tracking.
        :param node_id:
        """
        _params: Dict[str, Any] = {}
        if node_id is not None:
            _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _result = await self._target.send('CSS.trackComputedStyleUpdatesForNode', _params)
        return None

    async def track_computed_style_updates(self, *, properties_to_track: List[CSSComputedStyleProperty]) -> None:
        """
        Starts tracking the given computed styles for updates. The specified array of properties
        replaces the one previously specified. Pass empty array to disable tracking.
        Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
        The changes to computed style properties are only tracked for nodes pushed to the front-end
        by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
        to the front-end, no updates will be issued for the node.
        :param properties_to_track:
        """
        _params: Dict[str, Any] = {}
        _params['propertiesToTrack'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSComputedStyleProperty')), properties_to_track)
        _result = await self._target.send('CSS.trackComputedStyleUpdates', _params)
        return None

    async def take_computed_style_updates(self) -> TakeComputedStyleUpdatesReturn:
        """Polls the next batch of computed style updates."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.takeComputedStyleUpdates', _params)
        return TakeComputedStyleUpdatesReturn.from_json(_result)

    async def set_effective_property_value_for_node(self, *, node_id: DOM_NodeId, property_name: str, value: str) -> None:
        """
        Find a rule with the given active property for the given node and set the new value for this
        property
        :param node_id: The element id for which to set property.
        :param property_name:
        :param value:
        """
        _params: Dict[str, Any] = {}
        _params['nodeId'] = encode(FieldMeta('', '', False, 'primitive'), node_id)
        _params['propertyName'] = encode(FieldMeta('', '', False, 'primitive'), property_name)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        _result = await self._target.send('CSS.setEffectivePropertyValueForNode', _params)
        return None

    async def set_property_rule_property_name(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, property_name: str) -> SetPropertyRulePropertyNameReturn:
        """
        Modifies the property rule property name.
        :param style_sheet_id:
        :param range:
        :param property_name:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['propertyName'] = encode(FieldMeta('', '', False, 'primitive'), property_name)
        _result = await self._target.send('CSS.setPropertyRulePropertyName', _params)
        return SetPropertyRulePropertyNameReturn.from_json(_result)

    async def set_keyframe_key(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, key_text: str) -> SetKeyframeKeyReturn:
        """
        Modifies the keyframe rule key text.
        :param style_sheet_id:
        :param range:
        :param key_text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['keyText'] = encode(FieldMeta('', '', False, 'primitive'), key_text)
        _result = await self._target.send('CSS.setKeyframeKey', _params)
        return SetKeyframeKeyReturn.from_json(_result)

    async def set_media_text(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, text: str) -> SetMediaTextReturn:
        """
        Modifies the rule selector.
        :param style_sheet_id:
        :param range:
        :param text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        _result = await self._target.send('CSS.setMediaText', _params)
        return SetMediaTextReturn.from_json(_result)

    async def set_container_query_text(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, text: str) -> SetContainerQueryTextReturn:
        """
        Modifies the expression of a container query.
        :param style_sheet_id:
        :param range:
        :param text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        _result = await self._target.send('CSS.setContainerQueryText', _params)
        return SetContainerQueryTextReturn.from_json(_result)

    async def set_supports_text(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, text: str) -> SetSupportsTextReturn:
        """
        Modifies the expression of a supports at-rule.
        :param style_sheet_id:
        :param range:
        :param text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        _result = await self._target.send('CSS.setSupportsText', _params)
        return SetSupportsTextReturn.from_json(_result)

    async def set_scope_text(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, text: str) -> SetScopeTextReturn:
        """
        Modifies the expression of a scope at-rule.
        :param style_sheet_id:
        :param range:
        :param text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        _result = await self._target.send('CSS.setScopeText', _params)
        return SetScopeTextReturn.from_json(_result)

    async def set_rule_selector(self, *, style_sheet_id: DOM_StyleSheetId, range: SourceRange, selector: str) -> SetRuleSelectorReturn:
        """
        Modifies the rule selector.
        :param style_sheet_id:
        :param range:
        :param selector:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['range'] = encode(FieldMeta('', '', False, 'object', ref='CSS.SourceRange'), range)
        _params['selector'] = encode(FieldMeta('', '', False, 'primitive'), selector)
        _result = await self._target.send('CSS.setRuleSelector', _params)
        return SetRuleSelectorReturn.from_json(_result)

    async def set_style_sheet_text(self, *, style_sheet_id: DOM_StyleSheetId, text: str) -> SetStyleSheetTextReturn:
        """
        Sets the new stylesheet text.
        :param style_sheet_id:
        :param text:
        """
        _params: Dict[str, Any] = {}
        _params['styleSheetId'] = encode(FieldMeta('', '', False, 'primitive'), style_sheet_id)
        _params['text'] = encode(FieldMeta('', '', False, 'primitive'), text)
        _result = await self._target.send('CSS.setStyleSheetText', _params)
        return SetStyleSheetTextReturn.from_json(_result)

    async def set_style_texts(self, *, edits: List[StyleDeclarationEdit], node_for_property_syntax_validation: Optional[DOM_NodeId] = None) -> SetStyleTextsReturn:
        """
        Applies specified style edits one after another in the given order.
        :param edits:
        :param node_for_property_syntax_validation: NodeId for the DOM node in whose context custom property declarations for registered properties should be
        validated. If omitted, declarations in the new rule text can only be validated statically, which may produce
        incorrect results if the declaration contains a var() for example.
        """
        _params: Dict[str, Any] = {}
        _params['edits'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.StyleDeclarationEdit')), edits)
        if node_for_property_syntax_validation is not None:
            _params['nodeForPropertySyntaxValidation'] = encode(FieldMeta('', '', False, 'primitive'), node_for_property_syntax_validation)
        _result = await self._target.send('CSS.setStyleTexts', _params)
        return SetStyleTextsReturn.from_json(_result)

    async def start_rule_usage_tracking(self) -> None:
        """Enables the selector recording."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.startRuleUsageTracking', _params)
        return None

    async def stop_rule_usage_tracking(self) -> StopRuleUsageTrackingReturn:
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
        `takeCoverageDelta` (or since start of coverage instrumentation).
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.stopRuleUsageTracking', _params)
        return StopRuleUsageTrackingReturn.from_json(_result)

    async def take_coverage_delta(self) -> TakeCoverageDeltaReturn:
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
        instrumentation).
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('CSS.takeCoverageDelta', _params)
        return TakeCoverageDeltaReturn.from_json(_result)

    async def set_local_fonts_enabled(self, *, enabled: bool) -> None:
        """
        Enables/disables rendering of local CSS fonts (enabled by default).
        :param enabled: Whether rendering of local fonts is enabled.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('CSS.setLocalFontsEnabled', _params)
        return None
