"""Custom types and enums for the CSS domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..dom.types import LogicalAxes as DOM_LogicalAxes
    from ..dom.types import PhysicalAxes as DOM_PhysicalAxes
    from ..dom.types import PseudoType as DOM_PseudoType
    from ..dom.types import StyleSheetId as DOM_StyleSheetId
    from ..page.types import FrameId as Page_FrameId

@register("CSS.StyleSheetOrigin")
class StyleSheetOrigin(str, Enum):
    """
    Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent
    stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via
    inspector" rules), "regular" for regular stylesheets.
    """
    INJECTED = 'injected'
    USER_AGENT = 'user-agent'
    INSPECTOR = 'inspector'
    REGULAR = 'regular'


@register("CSS.PseudoElementMatches")
@dataclass
class PseudoElementMatches(DataType):
    """CSS rule collection for a single pseudo style."""
    pseudo_type: DOM_PseudoType
    matches: List[RuleMatch]
    pseudo_identifier: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('pseudo_type', 'pseudoType', False, 'enum', ref='DOM.PseudoType'),
        FieldMeta('matches', 'matches', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.RuleMatch')),
        FieldMeta('pseudo_identifier', 'pseudoIdentifier', True, 'primitive'),
    )


@register("CSS.CSSAnimationStyle")
@dataclass
class CSSAnimationStyle(DataType):
    """CSS style coming from animations with the name of the animation."""
    style: CSSStyle
    name: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('name', 'name', True, 'primitive'),
    )


@register("CSS.InheritedStyleEntry")
@dataclass
class InheritedStyleEntry(DataType):
    """Inherited CSS rule collection from ancestor node."""
    matched_css_rules: List[RuleMatch]
    inline_style: Optional[CSSStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('matched_css_rules', 'matchedCSSRules', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.RuleMatch')),
        FieldMeta('inline_style', 'inlineStyle', True, 'object', ref='CSS.CSSStyle'),
    )


@register("CSS.InheritedAnimatedStyleEntry")
@dataclass
class InheritedAnimatedStyleEntry(DataType):
    """Inherited CSS style collection for animated styles from ancestor node."""
    animation_styles: Optional[List[CSSAnimationStyle]] = None
    transitions_style: Optional[CSSStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('animation_styles', 'animationStyles', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSAnimationStyle')),
        FieldMeta('transitions_style', 'transitionsStyle', True, 'object', ref='CSS.CSSStyle'),
    )


@register("CSS.InheritedPseudoElementMatches")
@dataclass
class InheritedPseudoElementMatches(DataType):
    """Inherited pseudo element matches from pseudos of an ancestor node."""
    pseudo_elements: List[PseudoElementMatches]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('pseudo_elements', 'pseudoElements', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.PseudoElementMatches')),
    )


@register("CSS.RuleMatch")
@dataclass
class RuleMatch(DataType):
    """Match data for a CSS rule."""
    rule: CSSRule
    matching_selectors: List[int]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('rule', 'rule', False, 'object', ref='CSS.CSSRule'),
        FieldMeta('matching_selectors', 'matchingSelectors', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@register("CSS.Value")
@dataclass
class Value(DataType):
    """Data for a simple selector (these are delimited by commas in a selector list)."""
    text: str
    range: Optional[SourceRange] = None
    specificity: Optional[Specificity] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('specificity', 'specificity', True, 'object', ref='CSS.Specificity'),
    )


@register("CSS.Specificity")
@dataclass
class Specificity(DataType):
    """
    Specificity:
    https://drafts.csswg.org/selectors/#specificity-rules
    """
    a: int
    b: int
    c: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('a', 'a', False, 'primitive'),
        FieldMeta('b', 'b', False, 'primitive'),
        FieldMeta('c', 'c', False, 'primitive'),
    )


@register("CSS.SelectorList")
@dataclass
class SelectorList(DataType):
    """Selector list data."""
    selectors: List[Value]
    text: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('selectors', 'selectors', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.Value')),
        FieldMeta('text', 'text', False, 'primitive'),
    )


@register("CSS.CSSStyleSheetHeader")
@dataclass
class CSSStyleSheetHeader(DataType):
    """CSS stylesheet metainformation."""
    style_sheet_id: DOM_StyleSheetId
    frame_id: Page_FrameId
    source_url: str
    origin: StyleSheetOrigin
    title: str
    disabled: bool
    is_inline: bool
    is_mutable: bool
    is_constructed: bool
    start_line: float
    start_column: float
    length: float
    end_line: float
    end_column: float
    source_map_url: Optional[str] = None
    owner_node: Optional[DOM_BackendNodeId] = None
    has_source_url: Optional[bool] = None
    loading_failed: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
        FieldMeta('frame_id', 'frameId', False, 'primitive'),
        FieldMeta('source_url', 'sourceURL', False, 'primitive'),
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('title', 'title', False, 'primitive'),
        FieldMeta('disabled', 'disabled', False, 'primitive'),
        FieldMeta('is_inline', 'isInline', False, 'primitive'),
        FieldMeta('is_mutable', 'isMutable', False, 'primitive'),
        FieldMeta('is_constructed', 'isConstructed', False, 'primitive'),
        FieldMeta('start_line', 'startLine', False, 'primitive'),
        FieldMeta('start_column', 'startColumn', False, 'primitive'),
        FieldMeta('length', 'length', False, 'primitive'),
        FieldMeta('end_line', 'endLine', False, 'primitive'),
        FieldMeta('end_column', 'endColumn', False, 'primitive'),
        FieldMeta('source_map_url', 'sourceMapURL', True, 'primitive'),
        FieldMeta('owner_node', 'ownerNode', True, 'primitive'),
        FieldMeta('has_source_url', 'hasSourceURL', True, 'primitive'),
        FieldMeta('loading_failed', 'loadingFailed', True, 'primitive'),
    )


@register("CSS.CSSRule")
@dataclass
class CSSRule(DataType):
    """CSS rule representation."""
    selector_list: SelectorList
    origin: StyleSheetOrigin
    style: CSSStyle
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    nesting_selectors: Optional[List[str]] = None
    origin_tree_scope_node_id: Optional[DOM_BackendNodeId] = None
    media: Optional[List[CSSMedia]] = None
    container_queries: Optional[List[CSSContainerQuery]] = None
    supports: Optional[List[CSSSupports]] = None
    layers: Optional[List[CSSLayer]] = None
    scopes: Optional[List[CSSScope]] = None
    rule_types: Optional[List[CSSRuleType]] = None
    starting_styles: Optional[List[CSSStartingStyle]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('selector_list', 'selectorList', False, 'object', ref='CSS.SelectorList'),
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
        FieldMeta('nesting_selectors', 'nestingSelectors', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('origin_tree_scope_node_id', 'originTreeScopeNodeId', True, 'primitive'),
        FieldMeta('media', 'media', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSMedia')),
        FieldMeta('container_queries', 'containerQueries', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSContainerQuery')),
        FieldMeta('supports', 'supports', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSSupports')),
        FieldMeta('layers', 'layers', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSLayer')),
        FieldMeta('scopes', 'scopes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSScope')),
        FieldMeta('rule_types', 'ruleTypes', True, 'array', inner=FieldMeta('', '', False, 'enum', ref='CSS.CSSRuleType')),
        FieldMeta('starting_styles', 'startingStyles', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSStartingStyle')),
    )


@register("CSS.CSSRuleType")
class CSSRuleType(str, Enum):
    """
    Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors.
    This list only contains rule types that are collected during the ancestor rule collection.
    """
    MEDIARULE = 'MediaRule'
    SUPPORTSRULE = 'SupportsRule'
    CONTAINERRULE = 'ContainerRule'
    LAYERRULE = 'LayerRule'
    SCOPERULE = 'ScopeRule'
    STYLERULE = 'StyleRule'
    STARTINGSTYLERULE = 'StartingStyleRule'


@register("CSS.RuleUsage")
@dataclass
class RuleUsage(DataType):
    """CSS coverage information."""
    style_sheet_id: DOM_StyleSheetId
    start_offset: float
    end_offset: float
    used: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
        FieldMeta('start_offset', 'startOffset', False, 'primitive'),
        FieldMeta('end_offset', 'endOffset', False, 'primitive'),
        FieldMeta('used', 'used', False, 'primitive'),
    )


@register("CSS.SourceRange")
@dataclass
class SourceRange(DataType):
    """Text range within a resource. All numbers are zero-based."""
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('start_line', 'startLine', False, 'primitive'),
        FieldMeta('start_column', 'startColumn', False, 'primitive'),
        FieldMeta('end_line', 'endLine', False, 'primitive'),
        FieldMeta('end_column', 'endColumn', False, 'primitive'),
    )


@register("CSS.ShorthandEntry")
@dataclass
class ShorthandEntry(DataType):
    name: str
    value: str
    important: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('important', 'important', True, 'primitive'),
    )


@register("CSS.CSSComputedStyleProperty")
@dataclass
class CSSComputedStyleProperty(DataType):
    name: str
    value: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
    )


@register("CSS.ComputedStyleExtraFields")
@dataclass
class ComputedStyleExtraFields(DataType):
    is_appearance_base: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('is_appearance_base', 'isAppearanceBase', False, 'primitive'),
    )


@register("CSS.CSSStyle")
@dataclass
class CSSStyle(DataType):
    """CSS style representation."""
    css_properties: List[CSSProperty]
    shorthand_entries: List[ShorthandEntry]
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    css_text: Optional[str] = None
    range: Optional[SourceRange] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('css_properties', 'cssProperties', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSProperty')),
        FieldMeta('shorthand_entries', 'shorthandEntries', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.ShorthandEntry')),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
        FieldMeta('css_text', 'cssText', True, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
    )


@register("CSS.CSSProperty")
@dataclass
class CSSProperty(DataType):
    """CSS property declaration data."""
    name: str
    value: str
    important: Optional[bool] = None
    implicit: Optional[bool] = None
    text: Optional[str] = None
    parsed_ok: Optional[bool] = None
    disabled: Optional[bool] = None
    range: Optional[SourceRange] = None
    longhand_properties: Optional[List[CSSProperty]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('important', 'important', True, 'primitive'),
        FieldMeta('implicit', 'implicit', True, 'primitive'),
        FieldMeta('text', 'text', True, 'primitive'),
        FieldMeta('parsed_ok', 'parsedOk', True, 'primitive'),
        FieldMeta('disabled', 'disabled', True, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('longhand_properties', 'longhandProperties', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSProperty')),
    )


@register("CSS.CSSMedia")
@dataclass
class CSSMedia(DataType):
    """CSS media rule descriptor."""
    text: str
    source: Literal['mediaRule', 'importRule', 'linkedSheet', 'inlineSheet']
    source_url: Optional[str] = None
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    media_list: Optional[List[MediaQuery]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('source', 'source', False, 'primitive'),
        FieldMeta('source_url', 'sourceURL', True, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
        FieldMeta('media_list', 'mediaList', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.MediaQuery')),
    )


@register("CSS.MediaQuery")
@dataclass
class MediaQuery(DataType):
    """Media query descriptor."""
    expressions: List[MediaQueryExpression]
    active: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('expressions', 'expressions', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.MediaQueryExpression')),
        FieldMeta('active', 'active', False, 'primitive'),
    )


@register("CSS.MediaQueryExpression")
@dataclass
class MediaQueryExpression(DataType):
    """Media query expression descriptor."""
    value: float
    unit: str
    feature: str
    value_range: Optional[SourceRange] = None
    computed_length: Optional[float] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('value', 'value', False, 'primitive'),
        FieldMeta('unit', 'unit', False, 'primitive'),
        FieldMeta('feature', 'feature', False, 'primitive'),
        FieldMeta('value_range', 'valueRange', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('computed_length', 'computedLength', True, 'primitive'),
    )


@register("CSS.CSSContainerQuery")
@dataclass
class CSSContainerQuery(DataType):
    """CSS container query rule descriptor."""
    text: str
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    name: Optional[str] = None
    physical_axes: Optional[DOM_PhysicalAxes] = None
    logical_axes: Optional[DOM_LogicalAxes] = None
    queries_scroll_state: Optional[bool] = None
    queries_anchored: Optional[bool] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
        FieldMeta('name', 'name', True, 'primitive'),
        FieldMeta('physical_axes', 'physicalAxes', True, 'enum', ref='DOM.PhysicalAxes'),
        FieldMeta('logical_axes', 'logicalAxes', True, 'enum', ref='DOM.LogicalAxes'),
        FieldMeta('queries_scroll_state', 'queriesScrollState', True, 'primitive'),
        FieldMeta('queries_anchored', 'queriesAnchored', True, 'primitive'),
    )


@register("CSS.CSSSupports")
@dataclass
class CSSSupports(DataType):
    """CSS Supports at-rule descriptor."""
    text: str
    active: bool
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('active', 'active', False, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSScope")
@dataclass
class CSSScope(DataType):
    """CSS Scope at-rule descriptor."""
    text: str
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSLayer")
@dataclass
class CSSLayer(DataType):
    """CSS Layer at-rule descriptor."""
    text: str
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('text', 'text', False, 'primitive'),
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSStartingStyle")
@dataclass
class CSSStartingStyle(DataType):
    """CSS Starting Style at-rule descriptor."""
    range: Optional[SourceRange] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('range', 'range', True, 'object', ref='CSS.SourceRange'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSLayerData")
@dataclass
class CSSLayerData(DataType):
    """CSS Layer data."""
    name: str
    order: float
    sub_layers: Optional[List[CSSLayerData]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('order', 'order', False, 'primitive'),
        FieldMeta('sub_layers', 'subLayers', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSLayerData')),
    )


@register("CSS.PlatformFontUsage")
@dataclass
class PlatformFontUsage(DataType):
    """Information about amount of glyphs that were rendered with given font."""
    family_name: str
    post_script_name: str
    is_custom_font: bool
    glyph_count: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('family_name', 'familyName', False, 'primitive'),
        FieldMeta('post_script_name', 'postScriptName', False, 'primitive'),
        FieldMeta('is_custom_font', 'isCustomFont', False, 'primitive'),
        FieldMeta('glyph_count', 'glyphCount', False, 'primitive'),
    )


@register("CSS.FontVariationAxis")
@dataclass
class FontVariationAxis(DataType):
    """Information about font variation axes for variable fonts"""
    tag: str
    name: str
    min_value: float
    max_value: float
    default_value: float
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('tag', 'tag', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('min_value', 'minValue', False, 'primitive'),
        FieldMeta('max_value', 'maxValue', False, 'primitive'),
        FieldMeta('default_value', 'defaultValue', False, 'primitive'),
    )


@register("CSS.FontFace")
@dataclass
class FontFace(DataType):
    """
    Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
    and additional information such as platformFontFamily and fontVariationAxes.
    """
    font_family: str
    font_style: str
    font_variant: str
    font_weight: str
    font_stretch: str
    font_display: str
    unicode_range: str
    src: str
    platform_font_family: str
    font_variation_axes: Optional[List[FontVariationAxis]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('font_family', 'fontFamily', False, 'primitive'),
        FieldMeta('font_style', 'fontStyle', False, 'primitive'),
        FieldMeta('font_variant', 'fontVariant', False, 'primitive'),
        FieldMeta('font_weight', 'fontWeight', False, 'primitive'),
        FieldMeta('font_stretch', 'fontStretch', False, 'primitive'),
        FieldMeta('font_display', 'fontDisplay', False, 'primitive'),
        FieldMeta('unicode_range', 'unicodeRange', False, 'primitive'),
        FieldMeta('src', 'src', False, 'primitive'),
        FieldMeta('platform_font_family', 'platformFontFamily', False, 'primitive'),
        FieldMeta('font_variation_axes', 'fontVariationAxes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.FontVariationAxis')),
    )


@register("CSS.CSSTryRule")
@dataclass
class CSSTryRule(DataType):
    """CSS try rule representation."""
    origin: StyleSheetOrigin
    style: CSSStyle
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSPositionTryRule")
@dataclass
class CSSPositionTryRule(DataType):
    """CSS @position-try rule representation."""
    name: Value
    origin: StyleSheetOrigin
    style: CSSStyle
    active: bool
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'object', ref='CSS.Value'),
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('active', 'active', False, 'primitive'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSKeyframesRule")
@dataclass
class CSSKeyframesRule(DataType):
    """CSS keyframes rule representation."""
    animation_name: Value
    keyframes: List[CSSKeyframeRule]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('animation_name', 'animationName', False, 'object', ref='CSS.Value'),
        FieldMeta('keyframes', 'keyframes', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSKeyframeRule')),
    )


@register("CSS.CSSPropertyRegistration")
@dataclass
class CSSPropertyRegistration(DataType):
    """Representation of a custom property registration through CSS.registerProperty"""
    property_name: str
    inherits: bool
    syntax: str
    initial_value: Optional[Value] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('property_name', 'propertyName', False, 'primitive'),
        FieldMeta('inherits', 'inherits', False, 'primitive'),
        FieldMeta('syntax', 'syntax', False, 'primitive'),
        FieldMeta('initial_value', 'initialValue', True, 'object', ref='CSS.Value'),
    )


@register("CSS.CSSAtRule")
@dataclass
class CSSAtRule(DataType):
    """CSS generic @rule representation."""
    type_: Literal['font-face', 'font-feature-values', 'font-palette-values']
    origin: StyleSheetOrigin
    style: CSSStyle
    subsection: Optional[Literal['swash', 'annotation', 'ornaments', 'stylistic', 'styleset', 'character-variant']] = None
    name: Optional[Value] = None
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'primitive'),
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('subsection', 'subsection', True, 'primitive'),
        FieldMeta('name', 'name', True, 'object', ref='CSS.Value'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSPropertyRule")
@dataclass
class CSSPropertyRule(DataType):
    """CSS property at-rule representation."""
    origin: StyleSheetOrigin
    property_name: Value
    style: CSSStyle
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('property_name', 'propertyName', False, 'object', ref='CSS.Value'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSFunctionParameter")
@dataclass
class CSSFunctionParameter(DataType):
    """CSS function argument representation."""
    name: str
    type_: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('type_', 'type', False, 'primitive'),
    )


@register("CSS.CSSFunctionConditionNode")
@dataclass
class CSSFunctionConditionNode(DataType):
    """CSS function conditional block representation."""
    children: List[CSSFunctionNode]
    condition_text: str
    media: Optional[CSSMedia] = None
    container_queries: Optional[CSSContainerQuery] = None
    supports: Optional[CSSSupports] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('children', 'children', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSFunctionNode')),
        FieldMeta('condition_text', 'conditionText', False, 'primitive'),
        FieldMeta('media', 'media', True, 'object', ref='CSS.CSSMedia'),
        FieldMeta('container_queries', 'containerQueries', True, 'object', ref='CSS.CSSContainerQuery'),
        FieldMeta('supports', 'supports', True, 'object', ref='CSS.CSSSupports'),
    )


@register("CSS.CSSFunctionNode")
@dataclass
class CSSFunctionNode(DataType):
    """Section of the body of a CSS function rule."""
    condition: Optional[CSSFunctionConditionNode] = None
    style: Optional[CSSStyle] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('condition', 'condition', True, 'object', ref='CSS.CSSFunctionConditionNode'),
        FieldMeta('style', 'style', True, 'object', ref='CSS.CSSStyle'),
    )


@register("CSS.CSSFunctionRule")
@dataclass
class CSSFunctionRule(DataType):
    """CSS function at-rule representation."""
    name: Value
    origin: StyleSheetOrigin
    parameters: List[CSSFunctionParameter]
    children: List[CSSFunctionNode]
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'object', ref='CSS.Value'),
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('parameters', 'parameters', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSFunctionParameter')),
        FieldMeta('children', 'children', False, 'array', inner=FieldMeta('', '', False, 'object', ref='CSS.CSSFunctionNode')),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.CSSKeyframeRule")
@dataclass
class CSSKeyframeRule(DataType):
    """CSS keyframe rule representation."""
    origin: StyleSheetOrigin
    key_text: Value
    style: CSSStyle
    style_sheet_id: Optional[DOM_StyleSheetId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('origin', 'origin', False, 'enum', ref='CSS.StyleSheetOrigin'),
        FieldMeta('key_text', 'keyText', False, 'object', ref='CSS.Value'),
        FieldMeta('style', 'style', False, 'object', ref='CSS.CSSStyle'),
        FieldMeta('style_sheet_id', 'styleSheetId', True, 'primitive'),
    )


@register("CSS.StyleDeclarationEdit")
@dataclass
class StyleDeclarationEdit(DataType):
    """A descriptor of operation to mutate style declaration text."""
    style_sheet_id: DOM_StyleSheetId
    range: SourceRange
    text: str
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('style_sheet_id', 'styleSheetId', False, 'primitive'),
        FieldMeta('range', 'range', False, 'object', ref='CSS.SourceRange'),
        FieldMeta('text', 'text', False, 'primitive'),
    )

__all__ = ["CSSAnimationStyle", "CSSAtRule", "CSSComputedStyleProperty", "CSSContainerQuery", "CSSFunctionConditionNode", "CSSFunctionNode", "CSSFunctionParameter", "CSSFunctionRule", "CSSKeyframeRule", "CSSKeyframesRule", "CSSLayer", "CSSLayerData", "CSSMedia", "CSSPositionTryRule", "CSSProperty", "CSSPropertyRegistration", "CSSPropertyRule", "CSSRule", "CSSRuleType", "CSSScope", "CSSStartingStyle", "CSSStyle", "CSSStyleSheetHeader", "CSSSupports", "CSSTryRule", "ComputedStyleExtraFields", "FontFace", "FontVariationAxis", "InheritedAnimatedStyleEntry", "InheritedPseudoElementMatches", "InheritedStyleEntry", "MediaQuery", "MediaQueryExpression", "PlatformFontUsage", "PseudoElementMatches", "RuleMatch", "RuleUsage", "SelectorList", "ShorthandEntry", "SourceRange", "Specificity", "StyleDeclarationEdit", "StyleSheetOrigin", "Value"]
