from profil3r.modules.porn.pornhub import Pornhub
from profil3r.modules.porn.redtube import Redtube
from profil3r.modules.porn.xvideos import XVideos

# Pornhub
def pornhub(self):
    self.result["pornhub"] = Pornhub(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("pornhub")

# Redtube
def redtube(self):
    self.result["redtube"] = Redtube(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("redtube")

# XVideos
def xvideos(self):
    self.result["xvideos"] = XVideos(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("xvideos")