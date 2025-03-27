"""Stub file for reflex/components/base/error_boundary.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Mapping, Optional, Sequence, overload

from reflex.components.component import Component
from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.vars.base import Var
from reflex.vars.object import ObjectVar

def on_error_spec(
    error: ObjectVar[dict[str, str]], info: ObjectVar[dict[str, str]]
) -> tuple[Var[str], Var[str]]: ...

class ErrorBoundary(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        fallback_render: Component | Var[Component] | None = None,
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
        on_error: Optional[EventType[()] | EventType[str] | EventType[str, str]] = None,
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
    ) -> "ErrorBoundary":
        """Create an ErrorBoundary component.

        Args:
            *children: The children of the component.
            on_error: Fired when the boundary catches an error.
            fallback_render: Rendered instead of the children when an error is caught.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The ErrorBoundary component.
        """
        ...

error_boundary = ErrorBoundary.create
