from modules.music.soundcloud import SoundCloud
from modules.music.spotify import Spotify

# Soundcloud
def soundcloud(self):
    self.result["soundcloud"] = Soundcloud(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("soundcloud")

# Soundcloud
def spotify(self):
    self.result["spotify"] = Spotify(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("spotify")