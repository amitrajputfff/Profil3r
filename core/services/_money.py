from profil3r.modules.money.buymeacoffee import BuyMeACoffee
from profil3r.modules.money.patreon import Patreon

# BuyMeACoffee
def buymeacoffee(self):
    self.result["buymeacoffee"] = BuyMeACoffee(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("buymeacoffee")

# Patreon
def patreon(self):
    self.result["patreon"] = Patreon(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("patreon")