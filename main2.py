from kivy.uix.floatlayout import FloatLayout
import config
from kivy.core.window import Window
from kivymd.app import MDApp
from pages import Pages
from kivy.lang.builder import Builder
from kivy.config import Config
Config.set('graphics', 'resizable', False)

KV = '''
#:import pages pages

AnchorLayout:
	anchor_x: 'center'
	anchor_y: 'bottom'

	BoxLayout:
		size_hint: (1, 0.1)
		orientation: 'horizontal'

		Button:
			text: 'Search'
			on_press: pages.Pages.load_page('SearchPage')

		Button:
			text: 'PlayList'
			on_press: pages.Pages.load_page('PlayList')

'''

class FreeMusicApp(MDApp):
	def build(self):
		Window.size = (450, 500)
		layout = FloatLayout(size=(100, 100))
		Pages.init(layout)
		Pages.load_page("SearchPage")
		layout.add_widget(Builder.load_string(KV))

		return layout

	def delete_movies(self, instance):
		try:
			config.Parser.delt()
		except:
			pass






if __name__ == '__main__':
	FreeMusicApp().run()
