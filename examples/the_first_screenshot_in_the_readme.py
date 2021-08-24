from kivy.app import runTouchApp
from kivy.lang import Builder
import kivyx.uix.behavior.tablikelooks

KV_CODE = '''
<ImageTab@ToggleButtonBehavior+Image>:
    size_hint_min: self.texture.size if self.texture else (1, 1)
    source: r'data/logo/kivy-icon-48.png'
    group: 'test'
<LabelTab@ToggleButtonBehavior+Label>:
    size_hint_min: self.texture_size
    font_size: 24
    group: 'test'
<NotTab@ButtonBehavior+Label>:
    size_hint_min: self.texture_size
    font_size: 24
<Tabs@KXTablikeLooksBehavior+BoxLayout>:
    tab_line_color: '#AAAAFF'
    spacing: 20
    padding: 20

BoxLayout:
    orientation: 'vertical'
    Tabs:
        LabelTab:
            text: 'A'
            on_state:
                if args[1] == 'down': content.text = 'tab A is active'
        LabelTab:
            text: 'B'
            on_state:
                if args[1] == 'down': content.text = 'tab B is active'
        ImageTab:
            on_state:
                if args[1] == 'down': content.text = 'image tab is active'
        NotTab:
            text: 'C'
            on_press:
                content.text = (
                "C does not inherit from ToggleButtonBehavior, \\n "
                "which means it isn't counted as a tab by the KXTablikeLooksBehavior \\n "
                "so pressing it does not affect the line"
                )
    Label:
        id: content
        size_hint_y: 4
'''

root = Builder.load_string(KV_CODE)
runTouchApp(root)
