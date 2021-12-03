from profil3r.modules.email.email import Email

# Emails
def email(self):
    self.result["email"] = Email(self.CONFIG, self.permutations_list).search()
    # print results
    self.print_results("email")