"""Stub file for reflex/components/radix/themes/components/text_area.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Literal, Mapping, Optional, Sequence, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventType, KeyInputInfo
from reflex.vars.base import Var

from ..base import RadixThemesComponent

LiteralTextAreaSize = Literal["1", "2", "3"]
LiteralTextAreaResize = Literal["none", "vertical", "horizontal", "both"]

class TextArea(RadixThemesComponent, elements.Textarea):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Breakpoints[str, Literal["1", "2", "3"]]
        | Literal["1", "2", "3"]
        | Var[Breakpoints[str, Literal["1", "2", "3"]] | Literal["1", "2", "3"]]
        | None = None,
        variant: Literal["classic", "soft", "surface"]
        | Var[Literal["classic", "soft", "surface"]]
        | None = None,
        resize: Breakpoints[str, Literal["both", "horizontal", "none", "vertical"]]
        | Literal["both", "horizontal", "none", "vertical"]
        | Var[
            Breakpoints[str, Literal["both", "horizontal", "none", "vertical"]]
            | Literal["both", "horizontal", "none", "vertical"]
        ]
        | None = None,
        color_scheme: Literal[
            "amber",
            "blue",
            "bronze",
            "brown",
            "crimson",
            "cyan",
            "gold",
            "grass",
            "gray",
            "green",
            "indigo",
            "iris",
            "jade",
            "lime",
            "mint",
            "orange",
            "pink",
            "plum",
            "purple",
            "red",
            "ruby",
            "sky",
            "teal",
            "tomato",
            "violet",
            "yellow",
        ]
        | Var[
            Literal[
                "amber",
                "blue",
                "bronze",
                "brown",
                "crimson",
                "cyan",
                "gold",
                "grass",
                "gray",
                "green",
                "indigo",
                "iris",
                "jade",
                "lime",
                "mint",
                "orange",
                "pink",
                "plum",
                "purple",
                "red",
                "ruby",
                "sky",
                "teal",
                "tomato",
                "violet",
                "yellow",
            ]
        ]
        | None = None,
        radius: Literal["full", "large", "medium", "none", "small"]
        | Var[Literal["full", "large", "medium", "none", "small"]]
        | None = None,
        auto_complete: Var[bool] | bool | None = None,
        auto_focus: Var[bool] | bool | None = None,
        default_value: Var[str] | str | None = None,
        dirname: Var[str] | str | None = None,
        disabled: Var[bool] | bool | None = None,
        form: Var[str] | str | None = None,
        max_length: Var[int] | int | None = None,
        min_length: Var[int] | int | None = None,
        name: Var[str] | str | None = None,
        placeholder: Var[str] | str | None = None,
        read_only: Var[bool] | bool | None = None,
        required: Var[bool] | bool | None = None,
        rows: Var[str] | str | None = None,
        value: Var[str] | str | None = None,
        wrap: Var[str] | str | None = None,
        auto_height: Var[bool] | bool | None = None,
        cols: Var[int] | int | None = None,
        enter_key_submit: Var[bool] | bool | None = None,
        access_key: Var[str] | str | None = None,
        auto_capitalize: Literal[
            "characters", "none", "off", "on", "sentences", "words"
        ]
        | Var[Literal["characters", "none", "off", "on", "sentences", "words"]]
        | None = None,
        content_editable: Literal["inherit", "plaintext-only", False, True]
        | Var[Literal["inherit", "plaintext-only", False, True]]
        | None = None,
        context_menu: Var[str] | str | None = None,
        dir: Var[str] | str | None = None,
        draggable: Var[bool] | bool | None = None,
        enter_key_hint: Literal[
            "done", "enter", "go", "next", "previous", "search", "send"
        ]
        | Var[Literal["done", "enter", "go", "next", "previous", "search", "send"]]
        | None = None,
        hidden: Var[bool] | bool | None = None,
        input_mode: Literal[
            "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
        ]
        | Var[
            Literal[
                "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
            ]
        ]
        | None = None,
        item_prop: Var[str] | str | None = None,
        lang: Var[str] | str | None = None,
        role: Literal[
            "alert",
            "alertdialog",
            "application",
            "article",
            "banner",
            "button",
            "cell",
            "checkbox",
            "columnheader",
            "combobox",
            "complementary",
            "contentinfo",
            "definition",
            "dialog",
            "directory",
            "document",
            "feed",
            "figure",
            "form",
            "grid",
            "gridcell",
            "group",
            "heading",
            "img",
            "link",
            "list",
            "listbox",
            "listitem",
            "log",
            "main",
            "marquee",
            "math",
            "menu",
            "menubar",
            "menuitem",
            "menuitemcheckbox",
            "menuitemradio",
            "navigation",
            "none",
            "note",
            "option",
            "presentation",
            "progressbar",
            "radio",
            "radiogroup",
            "region",
            "row",
            "rowgroup",
            "rowheader",
            "scrollbar",
            "search",
            "searchbox",
            "separator",
            "slider",
            "spinbutton",
            "status",
            "switch",
            "tab",
            "table",
            "tablist",
            "tabpanel",
            "term",
            "textbox",
            "timer",
            "toolbar",
            "tooltip",
            "tree",
            "treegrid",
            "treeitem",
        ]
        | Var[
            Literal[
                "alert",
                "alertdialog",
                "application",
                "article",
                "banner",
                "button",
                "cell",
                "checkbox",
                "columnheader",
                "combobox",
                "complementary",
                "contentinfo",
                "definition",
                "dialog",
                "directory",
                "document",
                "feed",
                "figure",
                "form",
                "grid",
                "gridcell",
                "group",
                "heading",
                "img",
                "link",
                "list",
                "listbox",
                "listitem",
                "log",
                "main",
                "marquee",
                "math",
                "menu",
                "menubar",
                "menuitem",
                "menuitemcheckbox",
                "menuitemradio",
                "navigation",
                "none",
                "note",
                "option",
                "presentation",
                "progressbar",
                "radio",
                "radiogroup",
                "region",
                "row",
                "rowgroup",
                "rowheader",
                "scrollbar",
                "search",
                "searchbox",
                "separator",
                "slider",
                "spinbutton",
                "status",
                "switch",
                "tab",
                "table",
                "tablist",
                "tabpanel",
                "term",
                "textbox",
                "timer",
                "toolbar",
                "tooltip",
                "tree",
                "treegrid",
                "treeitem",
            ]
        ]
        | None = None,
        slot: Var[str] | str | None = None,
        spell_check: Var[bool] | bool | None = None,
        tab_index: Var[int] | int | None = None,
        title: Var[str] | str | None = None,
        style: Sequence[Mapping[str, Any]]
        | Mapping[str, Any]
        | Var[Mapping[str, Any]]
        | Breakpoints
        | None = None,
        key: Any | None = None,
        id: Any | None = None,
        class_name: Any | None = None,
        autofocus: bool | None = None,
        custom_attrs: dict[str, Var | Any] | None = None,
        on_blur: Optional[EventType[()] | EventType[str]] = None,
        on_change: Optional[EventType[()] | EventType[str]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()] | EventType[str]] = None,
        on_key_down: Optional[
            EventType[()] | EventType[str] | EventType[str, KeyInputInfo]
        ] = None,
        on_key_up: Optional[
            EventType[()] | EventType[str] | EventType[str, KeyInputInfo]
        ] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "TextArea":
        """Create an Input component.

        Args:
            *children: The children of the component.
            size: The size of the text area: "1" | "2" | "3"
            variant: The variant of the text area
            resize: The resize behavior of the text area: "none" | "vertical" | "horizontal" | "both"
            color_scheme: The color of the text area
            radius: The radius of the text area: "none" | "small" | "medium" | "large" | "full"
            auto_complete: Whether the form control should have autocomplete enabled
            auto_focus: Automatically focuses the textarea when the page loads
            default_value: The default value of the textarea when initially rendered
            dirname: Name part of the textarea to submit in 'dir' and 'name' pair when form is submitted
            disabled: Disables the textarea
            form: Associates the textarea with a form (by id)
            max_length: Maximum number of characters allowed in the textarea
            min_length: Minimum number of characters required in the textarea
            name: Name of the textarea, used when submitting the form
            placeholder: Placeholder text in the textarea
            read_only: Indicates whether the textarea is read-only
            required: Indicates that the textarea is required
            rows: Visible number of lines in the text control
            value: The controlled value of the textarea, read only unless used with on_change
            wrap: How the text in the textarea is to be wrapped when submitting the form
            auto_height: Automatically fit the content height to the text (use min-height with this prop)
            cols: Visible width of the text control, in average character widths
            enter_key_submit: Enter key submits form (shift-enter adds new line)
            on_change: Fired when the input value changes
            on_focus: Fired when the input gains focus
            on_blur: Fired when the input loses focus
            on_key_down: Fired when a key is pressed down
            on_key_up: Fired when a key is released
            access_key: Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The component.
        """
        ...

    def add_style(self): ...

text_area = TextArea.create
