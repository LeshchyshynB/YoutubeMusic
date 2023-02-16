from kivymd.uix.list import TwoLineListItem
from typing import Tuple
import math

class MusicListSlot(TwoLineListItem):
    def __init__(self, music_info : Tuple[str, str, int] = None, **kwargs):
        super().__init__(**kwargs)

        self.music_info = music_info
        self.text = music_info[1]
        self.secondary_text = self.__format_time(music_info[2])

    def __format_time(self, seconds=1):
        mins, sec = divmod(math.floor(seconds), 60)

        if(sec < 10):
            return f"{mins}:0{sec}" 
        return f"{mins}:{sec}" 