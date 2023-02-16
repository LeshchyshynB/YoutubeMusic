from threading import Thread
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from typing import Tuple
from config import Parser
from music_slot import MusicListSlot


class SearchListSlot(MusicListSlot):
    def on_press(self):
        download_button = MDFlatButton(text="Download", on_press=self.on_download)
        cancel_button = MDFlatButton(text="Cancel", on_press=self.cancel_dialog)

        self.download_dialog = MDDialog(text=self.music_info[1], title="Download", size_hint=(0.7, 1), buttons=[
            download_button,
            cancel_button
        ])

        self.download_dialog.open()


    def on_download(self, instance):
        download_tread = Thread(target=Parser.extract, args=(self.music_info[0],))
        download_tread.start()
        self.download_dialog.dismiss()

    def cancel_dialog(self, instance):
        self.download_dialog.dismiss()
