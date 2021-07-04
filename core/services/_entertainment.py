from profil3r.modules.entertainment.dailymotion import Dailymotion
from profil3r.modules.entertainment.vimeo import Vimeo
from profil3r.modules.entertainment.deviantart import DeviantArt

# Dailymotion
def dailymotion(self):
    self.result["dailymotion"] = Dailymotion(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("dailymotion")

# Vimeo
def vimeo(self):
    self.result["vimeo"] = Vimeo(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("vimeo")

# DeviantArt
def deviantart(self):
    self.result["deviantart"] = DeviantArt(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("deviantart")