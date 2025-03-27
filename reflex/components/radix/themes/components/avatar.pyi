"""Stub file for reflex/components/radix/themes/components/avatar.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Literal, Mapping, Optional, Sequence, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.vars.base import Var

from ..base import RadixThemesComponent

LiteralSize = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]

class Avatar(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        variant: Literal["soft", "solid"] | Var[Literal["soft", "solid"]] | None = None,
        size: Breakpoints[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        | Var[
            Breakpoints[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
            | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
        high_contrast: Var[bool] | bool | None = None,
        radius: Literal["full", "large", "medium", "none", "small"]
        | Var[Literal["full", "large", "medium", "none", "small"]]
        | None = None,
        src: Var[str] | str | None = None,
        fallback: Var[str] | str | None = None,
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
    ) -> "Avatar":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            variant: The variant of the avatar
            size: The size of the avatar: "1" - "9"
            color_scheme: Color theme of the avatar
            high_contrast: Whether to render the avatar with higher contrast color against background
            radius: Override theme radius for avatar: "none" | "small" | "medium" | "large" | "full"
            src: The src of the avatar image
            fallback: The rendered fallback text
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

avatar = Avatar.create
