'''
A situation where 'tab_line_stays_inside' needs to be False.

* tab_line_stays_inside が True だと各MyTabsの線同士の末端が繋が
  らなくなり、見た目が悪くなってしまう。
'''

from kivy.app import runTouchApp
from kivy.lang import Builder
import kivyx.uix.behavior.tablikelooks

KV_CODE = '''
#:set LINE_WIDTH 2

<MyTab@ToggleButtonBehavior+Image>:
    size_hint_min: self.texture.size if self.texture else (1, 1)
    source: r'data/logo/kivy-icon-48.png'
    group: 'test'
<MyTabs@KXTablikeLooksBehavior+BoxLayout>:
    tab_line_color: '#AAAAFF'
    tab_line_stays_inside: False
    tab_line_width: LINE_WIDTH
    spacing: 20
    padding: 20
    size_hint_min: self.minimum_size

GridLayout:
    cols: 3
    rows: 3
    padding: LINE_WIDTH
    Widget:
    MyTabs:
        orientation: 'horizontal'
        tab_style_h: 'top'
        MyTab:
        MyTab:
        MyTab:
        MyTab:
    Widget:
    MyTabs:
        orientation: 'vertical'
        tab_style_v: 'left'
        MyTab:
        MyTab:
        MyTab:
    Widget:
        size_hint: 1000, 1000
    MyTabs:
        orientation: 'vertical'
        tab_style_v: 'right'
        MyTab:
        MyTab:
    Widget:
    MyTabs:
        orientation: 'horizontal'
        tab_style_h: 'bottom'
        MyTab:
        MyTab:
        MyTab:
        MyTab:
        MyTab:
    Widget:
'''

root = Builder.load_string(KV_CODE)
runTouchApp(root)
