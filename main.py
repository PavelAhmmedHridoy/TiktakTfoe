from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# Background color (dark modern theme)
Window.clearcolor = (0.08, 0.09, 0.12, 1)

class StylishApp(App):
    def build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        # Title Card
        title = Label(
            text="🚀 GitHub APK Builder",
            font_size=28,
            bold=True,
            color=(0.2, 0.8, 1, 1),
            size_hint=(1, 0.2)
        )

        # Subtitle
        subtitle = Label(
            text="Stylish Kivy Demo App 😎",
            font_size=18,
            color=(0.8, 0.8, 0.8, 1),
            size_hint=(1, 0.2)
        )

        # Status label
        self.status = Label(
            text="Ready to run APK build system ⚡",
            font_size=16,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )

        # Button
        btn = Button(
            text="CLICK ME 🔥",
            font_size=20,
            bold=True,
            size_hint=(1, 0.3),
            background_normal="",
            background_color=(0.1, 0.6, 1, 1)
        )

        btn.bind(on_press=self.on_click)

        root.add_widget(title)
        root.add_widget(subtitle)
        root.add_widget(self.status)
        root.add_widget(btn)

        return root

    def on_click(self, instance):
        self.status.text = "💥 Button clicked! App is alive & stylish 😎"
        instance.background_color = (0.2, 1, 0.5, 1)

StylishApp().run()
