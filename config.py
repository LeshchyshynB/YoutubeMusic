from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import os

class Parser:
	@classmethod
	def delt(cls):
		allfiles = os.listdir('music/')
		files = [ fname for fname in allfiles if fname.endswith('.mp4')]
		for i in files:
			os.remove("music/"+i)		

	@classmethod
	def extract(cls, i: str):
		video_sourse = YouTube(i).streams.filter(file_extension='mp4').first().download("music/")
		video_clip = mp.VideoFileClip(video_sourse)
		video_clip.audio.write_audiofile("music/"+YouTube(i).title+".mp3")

	@classmethod
	def parse(cls, url: str):
		content = cls.get_content(url)

		if(content):
			for i in cls.get_content(url):
				cls.extract(i[0])

	@classmethod
	def get_content(cls, url : str):
		result = []
		if len(url) > 60:
			try:
				for i in Playlist(url):
					source = YouTube(i)
					result.append((i, source.title, source.length))
				return result

			except:
				pass
		elif len(url) < 60 and len(url) > 1:
			try:
				source = YouTube(url)
				result.append((url, source.title, source.length))
				return result
			except:
				pass
			
		else:
			return []

		return result
