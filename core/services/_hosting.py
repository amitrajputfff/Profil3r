from profil3r.modules.hosting.aboutme import AboutMe
from profil3r.modules.hosting.wordpress import WordPress
from profil3r.modules.hosting.slideshare import SlideShare

# AboutMe
def aboutme(self):
    self.result["aboutme"] = AboutMe(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("aboutme")

# WordPress
def wordpress(self):
    self.result["wordpress"] = WordPress(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("wordpress")

# SlideShare
def slideshare(self):
    self.result["slideshare"] = SlideShare(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("slideshare")