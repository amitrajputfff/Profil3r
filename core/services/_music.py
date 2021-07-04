from profil3r.modules.music.soundcloud import Soundcloud
from profil3r.modules.music.spotify import Spotify
from profil3r.modules.music.smule import Smule

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

# Smule
def smule(self):
    self.result["smule"] = Smule(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("smule")