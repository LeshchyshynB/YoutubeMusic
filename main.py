import kivy
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import config
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
import threading
import os
from pages import Pages
from kivy.config import Config
from search_page import SearchPage
from player import Player

class FreeMusicApp(MDApp):
	def build(self):
		Window.size = (450, 600)
		Config.set('graphics', 'resizable', False)
		Window.clearcolor = (1, 1, 1, 1)
		self.content = FloatLayout(size=(100, 100))
		self.nav_download = Button(background_down="materials/download.png", background_normal="materials/download.png", on_press=self.change_to_download, pos=(50,10), size_hint=(.11, .08))
		self.nav_player = Button(background_down="materials/player.png", background_normal="materials/player.png", on_press=self.change_to_player, pos=(450/2-18,10), size_hint=(.12, .09))
		self.nav_list = Button(background_down="materials/list.png", background_normal="materials/list.png", on_press=self.change_to_list, pos=(450-50-36,10), size_hint=(.11, .08))
		self.nav_play = Button(text='',background_down="materials/play.png", background_normal="materials/play.png", on_press=Player.pause, pos=(450/2-18,70), size_hint=(.12, .09))
		self.nav_stop = Button(text='',background_down="materials/stop.png", background_normal="materials/stop.png", on_press=Player.stop, pos=(450/2-18-80,70), size_hint=(.11, .08))
		self.nav_next = Button(text='',background_down="materials/next.png", background_normal="materials/next.png", on_press=Player.next, pos=(450/2-18+150,110), size_hint=(.11, .08))
		self.nav_previous = Button(text='',background_down="materials/previous.png", background_normal="materials/previous.png", on_press=Player.previous, pos=(450/2-18-150,110), size_hint=(.11, .08))
		self.nav_mute = Button(text='',background_down="materials/volume.png", background_normal="materials/volume.png", on_press=Player.mute, pos=(450/2-18+80,70), size_hint=(.11, .08))
		self.content.add_widget(self.nav_download)
		self.content.add_widget(self.nav_player)
		self.content.add_widget(self.nav_list)
		Pages.init(self.content)
		self.change_to_player("")
		return self.content

	def change_to_download(self, instance):
		self.content.clear_widgets()
		self.content.add_widget(self.nav_download)
		self.content.add_widget(self.nav_player)
		self.content.add_widget(self.nav_list)
		Pages.load_page('SearchPage')

	def change_to_player(self, instance):
		self.content.clear_widgets()
		self.content.add_widget(self.nav_download)
		self.content.add_widget(self.nav_player)
		self.content.add_widget(self.nav_list)
		self.content.add_widget(self.nav_play)
		self.content.add_widget(self.nav_stop)
		self.content.add_widget(self.nav_next)
		self.content.add_widget(self.nav_previous)
		self.content.add_widget(self.nav_mute)

	def change_to_list(self, instance):
		self.content.clear_widgets()
		self.content.add_widget(self.nav_download)
		self.content.add_widget(self.nav_player)
		self.content.add_widget(self.nav_list)
		Pages.load_page('PlayList')


if __name__ == '__main__':
	FreeMusicApp().run()