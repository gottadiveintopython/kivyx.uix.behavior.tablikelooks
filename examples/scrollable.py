'''
A situation where 'tab_line_stays_inside' needs to be True.

* tab_line_stays_inside が False だとScrolViewによって線が切り取ら
  れてしまい、線の幅が半分になってしまう。
'''

from kivy.app import runTouchApp
from kivy.factory import Factory
from kivy.lang import Builder

import kivyx.uix.behavior.tablikelooks

KV_CODE = '''
<Spacer@Widget>:
    size_hint_x: None
    width: 20
    canvas:
        Color:
            rgba: .2, .2, .2, 1
        Rectangle:
            pos: self.pos
            size: self.size
<LabelTab@ToggleButtonBehavior+Label>:
    font_size: 30
    size_hint_min_x: self.texture_size[0]
    group: 'test'
<ImageTab@ToggleButtonBehavior+Image>:
    size_hint_min_x: self.texture.size[0] if self.texture else 1
    group: 'test'
<MyTabs@KXTablikeLooksBehavior+BoxLayout>:

BoxLayout:
    orientation: 'vertical'
    ScrollView:
        size_hint_y: None
        height: 80
        MyTabs:
            id: tabs
            tab_style_h: 'top'
            tab_line_color: '#AAAAFF'
            padding: 20, 0
            spacing: 20
            size_hint: None, 1
            width: max(self.minimum_width, self.parent.width)
    Widget:
'''

root = Builder.load_string(KV_CODE)
add_widget = root.ids.tabs.add_widget
Spacer = Factory.Spacer
LabelTab = Factory.LabelTab
ImageTab = Factory.ImageTab
for __ in range(5):
    add_widget(LabelTab(text='first'))
    add_widget(LabelTab(text='second'))
    add_widget(ImageTab(source=r'data/logo/kivy-icon-48.png'))
    add_widget(LabelTab(text='third'))
    add_widget(Spacer())
runTouchApp(root)
