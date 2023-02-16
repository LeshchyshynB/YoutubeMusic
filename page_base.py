from kivy.uix.layout import Layout

class PageBase:
    def build(self) -> Layout:
        ...

    def clear_page(self):
        ...