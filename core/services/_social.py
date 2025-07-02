from modules.social.facebook import Facebook
from modules.social.twitter import Twitter
from modules.social.instagram import Instagram
from modules.social.tiktok import TikTok
from modules.social.pinterest import Pinterest
from modules.social.linktree import Linktree
from modules.social.myspace import MySpace

# Facebook
def facebook(self):
    self.result["facebook"] = Facebook(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("facebook")

# Twitter
def twitter(self):
    self.result["twitter"] = Twitter(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("twitter")

# TikTok
def tiktok(self):
    self.result["tiktok"] = TikTok(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("tiktok")

# Instagram
def instagram(self):
    self.result["instagram"] = Instagram(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("instagram")

# Pinterest
def pinterest(self):
    self.result["pinterest"] = Pinterest(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("pinterest")

# LinkTree
def linktree(self):
    self.result["linktree"] = LinkTree(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("linktree")

# MySpace
def myspace(self):
    self.result["myspace"] = MySpace(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("myspace")