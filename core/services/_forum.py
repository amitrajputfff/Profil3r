from profil3r.modules.forum.zeroxzerozerosec import ZeroxZeroZeroSec
from profil3r.modules.forum.jeuxvideo import JeuxVideo
from profil3r.modules.forum.hackernews import Hackernews
from profil3r.modules.forum.crackedto import CrackedTo

# 0x00sec
def zeroxzerozerosec(self):
    self.result["0x00sec"] = ZeroxZeroZeroSec(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("0x00sec")

# jeuxvideo.com
def jeuxvideo(self):
    self.result["jeuxvideo.com"] = JeuxVideo(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("jeuxvideo.com")

# Hackernews
def hackernews(self):
    self.result["hackernews"] = Hackernews(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("hackernews")

# Cracked.to
def crackedto(self):
    self.result["crackedto"] = CrackedTo(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("crackedto")