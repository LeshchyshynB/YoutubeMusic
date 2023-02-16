from typing import Tuple
import math
from music_slot import MusicListSlot
from player import Player

class PlayListSlot(MusicListSlot):
    def on_press(self):
        Player.play(self.music_info[0], self.music_info[2])