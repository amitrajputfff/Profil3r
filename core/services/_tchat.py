from profil3r.modules.tchat.skype import Skype

# Skype
def skype(self):
    self.result["skype"] = Skype(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("skype")