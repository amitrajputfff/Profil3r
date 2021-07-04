from profil3r.modules.domain.domain import Domain

# Domain
def domain(self):
    self.result["domain"] = Domain(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("domain")