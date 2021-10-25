'''
KXTablikeLooksBehavior
======================

A mix-in class that adds tab-like graphical representation to BoxLayout.
'''

__all__ = ('KXTablikeLooksBehavior', )

from kivy.clock import Clock
from kivy.factory import Factory
from kivy.properties import (
    ColorProperty, NumericProperty, ObjectProperty, OptionProperty,
    BooleanProperty,
)
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior


class KXTablikeLooksBehavior:
    tab_style_h = OptionProperty('top', options=('top', 'bottom', ))
    tab_style_v = OptionProperty('left', options=('left', 'right'))
    tab_line_stays_inside = BooleanProperty(True)
    tab_line_color = ColorProperty("#FFFFFF")
    tab_line_width = NumericProperty(2)
    _tab_next_highlight = ObjectProperty(None, allownone=True)

    @property
    def _is_horizontal(self):
        return self.orientation in ('horizontal', 'lr', 'rl')

    def __init__(self, **kwargs):
        from kivy.graphics import InstructionGroup, Color, Line
        self._tab_inst_color = Color()
        self._tab_inst_line = Line(joint='bevel', cap='square', width=2)
        self._tab_current_highlight = None
        self._tab_actual_update_canvas = self._tab_update_canvas_ver_inside
        super().__init__(**kwargs)
        inst_group = InstructionGroup()
        inst_group.add(self._tab_inst_color)
        inst_group.add(self._tab_inst_line)
        self.canvas.after.add(inst_group)
        self._tab_trigger_update_canvas = trigger_update_canvas = \
            Clock.create_trigger(self._tab_update_canvas, 0)
        self._tab_trigger_rebind = trigger_rebind = \
            Clock.create_trigger(self._tab_rebind, 0)
        f = self.fbind
        f('pos', trigger_update_canvas)
        f('size', trigger_update_canvas)
        f('tab_line_width', trigger_update_canvas)
        f('spacing', trigger_update_canvas)
        f('padding', trigger_update_canvas)
        f('orientation', trigger_rebind)
        f('tab_style_h', trigger_rebind)
        f('tab_style_v', trigger_rebind)
        f('tab_line_stays_inside', trigger_update_canvas)
        f('_tab_next_highlight', trigger_rebind)
        trigger_rebind()

    def on_tab_line_stays_inside(self, __, tab_line_stays_inside):
        self._tab_actual_update_canvas = self._tab_update_canvas_ver_inside \
            if tab_line_stays_inside else self._tab_update_canvas_ver_normal

    def on_tab_line_color(self, __, color):
        self._tab_inst_color.rgba = color

    def on_tab_line_width(self, __, width):
        self._tab_inst_line.width = width

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, ToggleButtonBehavior):
            widget.bind(state=self._on_child_state)
        return super().add_widget(widget, *args, **kwargs)

    def remove_widget(self, widget, *args, **kwargs):
        if widget.__self__ is self._tab_current_highlight:
            self._tab_next_highlight = None
        if isinstance(widget, ToggleButtonBehavior):
            widget.unbind(state=self._on_child_state)
        return super().remove_widget(widget, *args, **kwargs)

    def _on_child_state(self, widget, state):
        self._tab_next_highlight = widget if state == 'down' else None

    def _tab_rebind(self, *args):
        trigger = self._tab_trigger_update_canvas
        current = self._tab_current_highlight
        next = self._tab_next_highlight
        trigger()
        if current is not None:
            current.unbind(pos=trigger, size=trigger)
        self._tab_current_highlight = next
        if next is not None:
            next.bind(pos=trigger, size=trigger)

    def _tab_update_canvas(self, *args):
        self._tab_actual_update_canvas()

    def _tab_update_canvas_ver_normal(self):
        spacing = self.spacing
        cur = self._tab_current_highlight
        inst_line = self._tab_inst_line
        is_horizontal = self._is_horizontal
        y1 = self_y = self.y
        y2 = self_top = self.top
        x1 = self_x = self.x
        x2 = self_right = self.right
        if is_horizontal:
            if self.tab_style_h == 'bottom':
                y1, y2 = y2, y1
        else:
            if self.tab_style_v == 'left':
                x1, x2 = x2, x1
        if cur is None:
            inst_line.points = (self_x, y1, self_right, y1, ) if \
                is_horizontal else (x1, self_y, x1, self_top, )
        elif is_horizontal:
            cur_x = cur.x
            cur_right = cur.right
            inst_line.points = (
                self_x, y1,
                max(cur_x - spacing, self_x), y1,
                cur_x, y2,
                cur_right, y2,
                min(cur_right + spacing, self_right), y1,
                self_right, y1,
            )
        else:
            cur_y = cur.y
            cur_top = cur.top
            inst_line.points = (
                x1, self_y,
                x1, max(cur_y - spacing, self_y),
                x2, cur_y,
                x2, cur_top,
                x1, min(cur_top + spacing, self_top),
                x1, self_top,
            )

    def _tab_update_canvas_ver_inside(self):
        spacing = self.spacing
        cur = self._tab_current_highlight
        inst_line = self._tab_inst_line
        is_horizontal = self._is_horizontal
        lw = self.tab_line_width
        self_y = self.y + lw
        self_top = self.top - lw
        self_x = self.x + lw
        self_right = self.right - lw
        y1 = self_y
        y2 = self_top
        x1 = self_x
        x2 = self_right
        if is_horizontal:
            if self.tab_style_h == 'bottom':
                y1, y2 = y2, y1
        else:
            if self.tab_style_v == 'left':
                x1, x2 = x2, x1
        if cur is None:
            inst_line.points = (self_x, y1, self_right, y1, ) if \
                is_horizontal else (x1, self_y, x1, self_top, )
        elif is_horizontal:
            cur_x = cur.x + lw
            cur_right = cur.right - lw
            inst_line.points = (
                self_x, y1,
                max(cur_x - spacing, x1), y1,
                cur_x, y2,
                cur_right, y2,
                min(cur_right + spacing, x2), y1,
                self_right, y1,
            )
        else:
            cur_y = cur.y + lw
            cur_top = cur.top - lw
            inst_line.points = (
                x1, self_y,
                x1, max(cur_y - spacing, y1),
                x2, cur_y,
                x2, cur_top,
                x1, min(cur_top + spacing, y2),
                x1, self_top,
            )


Factory.register('KXTablikeLooksBehavior', cls=KXTablikeLooksBehavior)
