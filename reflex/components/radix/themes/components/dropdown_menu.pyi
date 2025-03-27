"""Stub file for reflex/components/radix/themes/components/dropdown_menu.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Literal, Mapping, Optional, Sequence, overload

from reflex.components.component import ComponentNamespace
from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.vars.base import Var

from ..base import RadixThemesComponent, RadixThemesTriggerComponent

LiteralDirType = Literal["ltr", "rtl"]
LiteralSizeType = Literal["1", "2"]
LiteralVariantType = Literal["solid", "soft"]
LiteralSideType = Literal["top", "right", "bottom", "left"]
LiteralAlignType = Literal["start", "center", "end"]
LiteralStickyType = Literal["partial", "always"]

class DropdownMenuRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        default_open: Var[bool] | bool | None = None,
        open: Var[bool] | bool | None = None,
        modal: Var[bool] | bool | None = None,
        dir: Literal["ltr", "rtl"] | Var[Literal["ltr", "rtl"]] | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_open_change: Optional[EventType[()] | EventType[bool]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "DropdownMenuRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            default_open: The open state of the dropdown menu when it is initially rendered. Use when you do not need to control its open state.
            open: The controlled open state of the dropdown menu. Must be used in conjunction with onOpenChange.
            modal: The modality of the dropdown menu. When set to true, interaction with outside elements will be disabled and only menu content will be visible to screen readers. Defaults to True.
            dir: The reading direction of submenus when applicable. If omitted, inherits globally from DirectionProvider or assumes LTR (left-to-right) reading mode.
            on_open_change: Fired when the open state changes.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenuTrigger(RadixThemesTriggerComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Var[bool] | bool | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
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
    ) -> "DropdownMenuTrigger":
        """Create a new RadixThemesTriggerComponent instance.

        Args:
            children: The children of the component.
            props: The properties of the component.

        Returns:
            The new RadixThemesTriggerComponent instance.
        """
        ...

class DropdownMenuContent(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Breakpoints[str, Literal["1", "2"]]
        | Literal["1", "2"]
        | Var[Breakpoints[str, Literal["1", "2"]] | Literal["1", "2"]]
        | None = None,
        variant: Literal["soft", "solid"] | Var[Literal["soft", "solid"]] | None = None,
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
        high_contrast: Var[bool] | bool | None = None,
        as_child: Var[bool] | bool | None = None,
        loop: Var[bool] | bool | None = None,
        force_mount: Var[bool] | bool | None = None,
        side: Literal["bottom", "left", "right", "top"]
        | Var[Literal["bottom", "left", "right", "top"]]
        | None = None,
        side_offset: Var[float | int] | float | int | None = None,
        align: Literal["center", "end", "start"]
        | Var[Literal["center", "end", "start"]]
        | None = None,
        align_offset: Var[float | int] | float | int | None = None,
        avoid_collisions: Var[bool] | bool | None = None,
        collision_padding: Var[dict[str, float | int] | float | int]
        | dict[str, float | int]
        | float
        | int
        | None = None,
        sticky: Literal["always", "partial"]
        | Var[Literal["always", "partial"]]
        | None = None,
        hide_when_detached: Var[bool] | bool | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_close_auto_focus: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_escape_key_down: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_focus_outside: Optional[EventType[()]] = None,
        on_interact_outside: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_pointer_down_outside: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "DropdownMenuContent":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: Dropdown Menu Content size "1" - "2"
            variant: Variant of Dropdown Menu Content: "solid" | "soft"
            color_scheme: Override theme color for Dropdown Menu Content
            high_contrast: Renders the Dropdown Menu Content in higher contrast
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
            loop: When True, keyboard navigation will loop from last item to first, and vice versa. Defaults to False.
            force_mount: Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries.
            side: The preferred side of the trigger to render against when open. Will be reversed when collisions occur and `avoid_collisions` is enabled.The position of the tooltip. Defaults to "top".
            side_offset: The distance in pixels from the trigger. Defaults to 0.
            align: The preferred alignment against the trigger. May change when collisions occur. Defaults to "center".
            align_offset: An offset in pixels from the "start" or "end" alignment options.
            avoid_collisions: When true, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to True.
            collision_padding: The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
            sticky: The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
            hide_when_detached: Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
            on_close_auto_focus: Fired when the dialog is closed.
            on_escape_key_down: Fired when the escape key is pressed.
            on_pointer_down_outside: Fired when the pointer is down outside the dialog.
            on_focus_outside: Fired when focus moves outside the dialog.
            on_interact_outside: Fired when the pointer interacts outside the dialog.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenuSubTrigger(RadixThemesTriggerComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Var[bool] | bool | None = None,
        disabled: Var[bool] | bool | None = None,
        text_value: Var[str] | str | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
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
    ) -> "DropdownMenuSubTrigger":
        """Create a new RadixThemesTriggerComponent instance.

        Args:
            children: The children of the component.
            props: The properties of the component.

        Returns:
            The new RadixThemesTriggerComponent instance.
        """
        ...

class DropdownMenuSub(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        open: Var[bool] | bool | None = None,
        default_open: Var[bool] | bool | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_open_change: Optional[EventType[()] | EventType[bool]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "DropdownMenuSub":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            open: The controlled open state of the submenu. Must be used in conjunction with `on_open_change`.
            default_open: The open state of the submenu when it is initially rendered. Use when you do not need to control its open state.
            on_open_change: Fired when the open state changes.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenuSubContent(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Var[bool] | bool | None = None,
        loop: Var[bool] | bool | None = None,
        force_mount: Var[bool] | bool | None = None,
        side_offset: Var[float | int] | float | int | None = None,
        align_offset: Var[float | int] | float | int | None = None,
        avoid_collisions: Var[bool] | bool | None = None,
        collision_padding: Var[dict[str, float | int] | float | int]
        | dict[str, float | int]
        | float
        | int
        | None = None,
        sticky: Literal["always", "partial"]
        | Var[Literal["always", "partial"]]
        | None = None,
        hide_when_detached: Var[bool] | bool | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_escape_key_down: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_focus_outside: Optional[EventType[()]] = None,
        on_interact_outside: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_pointer_down_outside: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "DropdownMenuSubContent":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
            loop: When True, keyboard navigation will loop from last item to first, and vice versa. Defaults to False.
            force_mount: Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries.
            side_offset: The distance in pixels from the trigger. Defaults to 0.
            align_offset: An offset in pixels from the "start" or "end" alignment options.
            avoid_collisions: When true, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to True.
            collision_padding: The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
            sticky: The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
            hide_when_detached: Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
            on_escape_key_down: Fired when the escape key is pressed.
            on_pointer_down_outside: Fired when the pointer is down outside the dialog.
            on_focus_outside: Fired when focus moves outside the dialog.
            on_interact_outside: Fired when the pointer interacts outside the dialog.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenuItem(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
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
        shortcut: Var[str] | str | None = None,
        as_child: Var[bool] | bool | None = None,
        disabled: Var[bool] | bool | None = None,
        text_value: Var[str] | str | None = None,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_select: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "DropdownMenuItem":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color_scheme: Override theme color for Dropdown Menu Item
            shortcut: Shortcut to render a menu item as a link
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
            disabled: When true, prevents the user from interacting with the item.
            text_value: Optional text used for typeahead purposes. By default the typeahead behavior will use the .textContent of the item. Use this when the content is complex, or you have non-textual content inside.
            on_select: Fired when the item is selected.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenuSeparator(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
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
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
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
    ) -> "DropdownMenuSeparator":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class DropdownMenu(ComponentNamespace):
    root = staticmethod(DropdownMenuRoot.create)
    trigger = staticmethod(DropdownMenuTrigger.create)
    content = staticmethod(DropdownMenuContent.create)
    sub_trigger = staticmethod(DropdownMenuSubTrigger.create)
    sub = staticmethod(DropdownMenuSub.create)
    sub_content = staticmethod(DropdownMenuSubContent.create)
    item = staticmethod(DropdownMenuItem.create)
    separator = staticmethod(DropdownMenuSeparator.create)

menu = dropdown_menu = DropdownMenu()
