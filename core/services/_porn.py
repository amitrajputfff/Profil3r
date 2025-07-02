from modules.porn.pornhub import PornHub
from modules.porn.redtube import RedTube
from modules.porn.xvideos import XVideos

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