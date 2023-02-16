import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import threading
import os
from music_slot import MusicListSlot
import time

class Player(MusicListSlot):
	current_sound = None
	current_sound_play = False
	@classmethod
	def play(cls, path, sec):
		if cls.current_sound:
			cls.current_sound.stop()
		cls.current_sound = SoundLoader.load(path)
		cls.current_sound.play()
		cls.current_sound_play = True
		cls.sec = sec
		

	@classmethod
	def pause(cls, obj):
		if cls.current_sound_play == True:
			cls.second_pause = cls.current_sound.get_pos()
			cls.current_sound_play = False
			cls.current_sound.stop()
			obj.background_down="materials/play.png" 
			obj.background_normal="materials/play.png"
		else:
			cls.current_sound.play()
			cls.current_sound.seek(cls.second_pause)
			cls.current_sound_play = True
			obj.background_down="materials/pause.png"
			obj.background_normal="materials/pause.png"

	@classmethod
	def stop(cls, obj):
		cls.current_sound.stop()
				
	@classmethod
	def next(cls, obj):
		...

	@classmethod
	def previous(cls, obj):
		...

	@classmethod
	def mute(cls, obj):
		try:
			if cls.current_sound.volume == 1.0:
				cls.current_sound.volume = 0.0
				obj.background_down="materials/mute.png"
				obj.background_normal="materials/mute.png"
				obj.pos=(450/2-18+70,70)
			else:
				cls.current_sound.volume = 1.0
				obj.background_down="materials/volume.png"
				obj.background_normal="materials/volume.png"
				obj.pos=(450/2-18+80,70)
		except:
			pass