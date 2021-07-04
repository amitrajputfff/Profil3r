from profil3r.modules.programming.github import Github
from profil3r.modules.programming.pastebin import Pastebin
from profil3r.modules.programming.replit import Replit

# Github
def github(self):
    self.result["github"] = Github(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("github")

# Pastebin
def pastebin(self):
    self.result["pastebin"] = Pastebin(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("pastebin")

# Repl.it
def replit(self):
    self.result["replit"] = Replit(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("replit")