"""Custom types and enums for the Accessibility domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register

if TYPE_CHECKING:
    from ..dom.types import BackendNodeId as DOM_BackendNodeId
    from ..page.types import FrameId as Page_FrameId

type AXNodeId = str  # Unique accessibility node identifier.


@register("Accessibility.AXValueType")
class AXValueType(str, Enum):
    """Enum of possible property types."""
    BOOLEAN = 'boolean'
    TRISTATE = 'tristate'
    BOOLEANORUNDEFINED = 'booleanOrUndefined'
    IDREF = 'idref'
    IDREFLIST = 'idrefList'
    INTEGER = 'integer'
    NODE = 'node'
    NODELIST = 'nodeList'
    NUMBER = 'number'
    STRING = 'string'
    COMPUTEDSTRING = 'computedString'
    TOKEN = 'token'
    TOKENLIST = 'tokenList'
    DOMRELATION = 'domRelation'
    ROLE = 'role'
    INTERNALROLE = 'internalRole'
    VALUEUNDEFINED = 'valueUndefined'


@register("Accessibility.AXValueSourceType")
class AXValueSourceType(str, Enum):
    """Enum of possible property sources."""
    ATTRIBUTE = 'attribute'
    IMPLICIT = 'implicit'
    STYLE = 'style'
    CONTENTS = 'contents'
    PLACEHOLDER = 'placeholder'
    RELATEDELEMENT = 'relatedElement'


@register("Accessibility.AXValueNativeSourceType")
class AXValueNativeSourceType(str, Enum):
    """Enum of possible native property sources (as a subtype of a particular AXValueSourceType)."""
    DESCRIPTION = 'description'
    FIGCAPTION = 'figcaption'
    LABEL = 'label'
    LABELFOR = 'labelfor'
    LABELWRAPPED = 'labelwrapped'
    LEGEND = 'legend'
    RUBYANNOTATION = 'rubyannotation'
    TABLECAPTION = 'tablecaption'
    TITLE = 'title'
    OTHER = 'other'


@register("Accessibility.AXValueSource")
@dataclass
class AXValueSource(DataType):
    """A single source for a computed AX property."""
    type_: AXValueSourceType
    value: Optional[AXValue] = None
    attribute: Optional[str] = None
    attribute_value: Optional[AXValue] = None
    superseded: Optional[bool] = None
    native_source: Optional[AXValueNativeSourceType] = None
    native_source_value: Optional[AXValue] = None
    invalid: Optional[bool] = None
    invalid_reason: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Accessibility.AXValueSourceType'),
        FieldMeta('value', 'value', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('attribute', 'attribute', True, 'primitive'),
        FieldMeta('attribute_value', 'attributeValue', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('superseded', 'superseded', True, 'primitive'),
        FieldMeta('native_source', 'nativeSource', True, 'enum', ref='Accessibility.AXValueNativeSourceType'),
        FieldMeta('native_source_value', 'nativeSourceValue', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('invalid', 'invalid', True, 'primitive'),
        FieldMeta('invalid_reason', 'invalidReason', True, 'primitive'),
    )


@register("Accessibility.AXRelatedNode")
@dataclass
class AXRelatedNode(DataType):
    backend_dom_node_id: DOM_BackendNodeId
    idref: Optional[str] = None
    text: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('backend_dom_node_id', 'backendDOMNodeId', False, 'primitive'),
        FieldMeta('idref', 'idref', True, 'primitive'),
        FieldMeta('text', 'text', True, 'primitive'),
    )


@register("Accessibility.AXProperty")
@dataclass
class AXProperty(DataType):
    name: AXPropertyName
    value: AXValue
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('name', 'name', False, 'enum', ref='Accessibility.AXPropertyName'),
        FieldMeta('value', 'value', False, 'object', ref='Accessibility.AXValue'),
    )


@register("Accessibility.AXValue")
@dataclass
class AXValue(DataType):
    """A single computed AX property."""
    type_: AXValueType
    value: Optional[Any] = None
    related_nodes: Optional[List[AXRelatedNode]] = None
    sources: Optional[List[AXValueSource]] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('type_', 'type', False, 'enum', ref='Accessibility.AXValueType'),
        FieldMeta('value', 'value', True, 'primitive'),
        FieldMeta('related_nodes', 'relatedNodes', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXRelatedNode')),
        FieldMeta('sources', 'sources', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXValueSource')),
    )


@register("Accessibility.AXPropertyName")
class AXPropertyName(str, Enum):
    """
    Values of AXProperty name:
    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns': relationships between elements other than parent/child/sibling
    - from 'activeFullscreenElement' to 'uninteresting': reasons why this noode is hidden
    """
    ACTIONS = 'actions'
    BUSY = 'busy'
    DISABLED = 'disabled'
    EDITABLE = 'editable'
    FOCUSABLE = 'focusable'
    FOCUSED = 'focused'
    HIDDEN = 'hidden'
    HIDDENROOT = 'hiddenRoot'
    INVALID = 'invalid'
    KEYSHORTCUTS = 'keyshortcuts'
    SETTABLE = 'settable'
    ROLEDESCRIPTION = 'roledescription'
    LIVE = 'live'
    ATOMIC = 'atomic'
    RELEVANT = 'relevant'
    ROOT = 'root'
    AUTOCOMPLETE = 'autocomplete'
    HASPOPUP = 'hasPopup'
    LEVEL = 'level'
    MULTISELECTABLE = 'multiselectable'
    ORIENTATION = 'orientation'
    MULTILINE = 'multiline'
    READONLY = 'readonly'
    REQUIRED = 'required'
    VALUEMIN = 'valuemin'
    VALUEMAX = 'valuemax'
    VALUETEXT = 'valuetext'
    CHECKED = 'checked'
    EXPANDED = 'expanded'
    MODAL = 'modal'
    PRESSED = 'pressed'
    SELECTED = 'selected'
    ACTIVEDESCENDANT = 'activedescendant'
    CONTROLS = 'controls'
    DESCRIBEDBY = 'describedby'
    DETAILS = 'details'
    ERRORMESSAGE = 'errormessage'
    FLOWTO = 'flowto'
    LABELLEDBY = 'labelledby'
    OWNS = 'owns'
    URL = 'url'
    ACTIVEFULLSCREENELEMENT = 'activeFullscreenElement'
    ACTIVEMODALDIALOG = 'activeModalDialog'
    ACTIVEARIAMODALDIALOG = 'activeAriaModalDialog'
    ARIAHIDDENELEMENT = 'ariaHiddenElement'
    ARIAHIDDENSUBTREE = 'ariaHiddenSubtree'
    EMPTYALT = 'emptyAlt'
    EMPTYTEXT = 'emptyText'
    INERTELEMENT = 'inertElement'
    INERTSUBTREE = 'inertSubtree'
    LABELCONTAINER = 'labelContainer'
    LABELFOR = 'labelFor'
    NOTRENDERED = 'notRendered'
    NOTVISIBLE = 'notVisible'
    PRESENTATIONALROLE = 'presentationalRole'
    PROBABLYPRESENTATIONAL = 'probablyPresentational'
    INACTIVECAROUSELTABCONTENT = 'inactiveCarouselTabContent'
    UNINTERESTING = 'uninteresting'


@register("Accessibility.AXNode")
@dataclass
class AXNode(DataType):
    """A node in the accessibility tree."""
    node_id: AXNodeId
    ignored: bool
    ignored_reasons: Optional[List[AXProperty]] = None
    role: Optional[AXValue] = None
    chrome_role: Optional[AXValue] = None
    name: Optional[AXValue] = None
    description: Optional[AXValue] = None
    value: Optional[AXValue] = None
    properties: Optional[List[AXProperty]] = None
    parent_id: Optional[AXNodeId] = None
    child_ids: Optional[List[AXNodeId]] = None
    backend_dom_node_id: Optional[DOM_BackendNodeId] = None
    frame_id: Optional[Page_FrameId] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('node_id', 'nodeId', False, 'primitive'),
        FieldMeta('ignored', 'ignored', False, 'primitive'),
        FieldMeta('ignored_reasons', 'ignoredReasons', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXProperty')),
        FieldMeta('role', 'role', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('chrome_role', 'chromeRole', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('name', 'name', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('description', 'description', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('value', 'value', True, 'object', ref='Accessibility.AXValue'),
        FieldMeta('properties', 'properties', True, 'array', inner=FieldMeta('', '', False, 'object', ref='Accessibility.AXProperty')),
        FieldMeta('parent_id', 'parentId', True, 'primitive'),
        FieldMeta('child_ids', 'childIds', True, 'array', inner=FieldMeta('', '', False, 'primitive')),
        FieldMeta('backend_dom_node_id', 'backendDOMNodeId', True, 'primitive'),
        FieldMeta('frame_id', 'frameId', True, 'primitive'),
    )

__all__ = ["AXNode", "AXNodeId", "AXProperty", "AXPropertyName", "AXRelatedNode", "AXValue", "AXValueNativeSourceType", "AXValueSource", "AXValueSourceType", "AXValueType"]
