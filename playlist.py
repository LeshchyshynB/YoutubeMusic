from typing import List, Tuple
from typing import Dict
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from playlist_slot import PlayListSlot
from kivy.lang import Builder
import os
from moviepy.editor import VideoFileClip
from page_base import PageBase
from mutagen.mp3 import MP3
import config

KV = '''
ScrollView:
    size_hint: 1, 0.5
    MDList:
        id: container
'''

class PlayList(PageBase):
    def __init__(self):
        self.layout : BoxLayout
        self.music_slots : List[PlayListSlot] = []
        self.cache_music : List[ Tuple[str, VideoFileClip] ] = []

    def build(self) -> BoxLayout:
        self.box = Builder.load_string(KV)
        self.layout = BoxLayout(size=(100, 100), orientation="vertical")

        self.reload_button = Button(text="Reload", size_hint=(1, .05), on_press=self.update_search_list)
        self.delete_movie_button = Button(text="Clear music cache", size_hint=(1, .05), on_press=self.delete_movies)
        self.layout.add_widget(self.reload_button)
        self.layout.add_widget(self.delete_movie_button)
        self.layout.add_widget(self.box)

        if len(self.music_slots)==0:
            self.update_search_list(None)

        return self.layout

    def clear_page(self):
        self.layout.clear_widgets()
        
    def clear_list(self):
        self.box.ids.container.clear_widgets()
        self.music_slots.clear()

    def update_search_list(self, instance):
        self.clear_list()
        files = [fname for fname in os.listdir('music/') if fname.endswith('.mp3')]
           
        if len(files) != len(self.cache_music):
            self.cache_music.clear()
            for file_name in files:
                self.__add_music_slot(self.__register_music(file_name)) 
        else:
            for music in self.cache_music:
                self.__add_music_slot(music)

    def __add_music_slot(self, music : Tuple[str, str, MP3]):
        path, name, video_clip = music
        self.box.ids.container.add_widget(PlayListSlot(music_info=(path, name, video_clip.info.length)))

    def __register_music(self, file_name : str) -> Tuple[str, str, MP3]:
        path = '\\'.join(__file__.split('\\')[0:-1])+"\\music\\"+file_name
        video_clip = MP3(path)
        self.cache_music.append(music := (path, file_name, video_clip))

        return music

    def delete_movies(self, instance):
        try:
            config.Parser().delt()
        except:
            pass
