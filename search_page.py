from typing import List
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextFieldRect
from search_page_slot import SearchListSlot
from kivy.lang import Builder
from config import Parser
from page_base import PageBase
from typing import Tuple

KV = '''
ScrollView:
    size_hint: 1, 0.5
    MDList:
        id: container
'''

class SearchPage(PageBase):
    def __init__(self):
        self.source_music : List
        self.layout : BoxLayout
        self.search_results : BoxLayout
        self.cache_music : List[Tuple[str, str, int]] = []
        self.music_slots : List[SearchListSlot] = []

    def build(self) -> BoxLayout:
        self.box = Builder.load_string(KV)
        self.layout = BoxLayout(size=(100, 100), orientation="vertical")
        self.text_input = MDTextFieldRect(size_hint=(2, 1))
        self.search_panel = BoxLayout(size_hint=(1, 0.04), pos_hint={"top": -1 })
        self.search_button = Button(text="Search", on_press=self.refresh_search_list, size_hint=(1, 1))

        self.search_panel.add_widget(self.text_input)
        self.search_panel.add_widget(self.search_button)
        self.layout.add_widget(self.search_panel)
        self.layout.add_widget(self.box)

        if len(self.cache_music) > 1:
            for music in self.cache_music:
                self.__add_music_slot(music)

        return self.layout

    def clear_page(self):
        self.layout.clear_widgets()

    def clear_list(self):
        self.box.ids.container.clear_widgets()
        self.music_slots.clear()

    def refresh_search_list(self, instance):
        if len(self.text_input.text) > 0:
            self.clear_list()
            self.__register_music()

    def __add_music_slot(self, music : Tuple[str, str, int]):
        url, name, duration = music
        self.box.ids.container.add_widget(SearchListSlot(music_info=(url, name, duration)))

    def __register_music(self):
        for i in Parser.get_content(self.text_input.text):
            slot = SearchListSlot(music_info=i)
            self.cache_music.append(i)
            self.music_slots.append(slot)
            self.box.ids.container.add_widget(slot)

    