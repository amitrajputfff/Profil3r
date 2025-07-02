from profil3r.core.colors import Colors

def print_results(self, element):
    if element in self.result:
        element_results = self.result[element]
        
        # Section title

        # No results
        if not element_results["accounts"]:
            print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " {} ❌".format(element.upper()) + Colors.ENDC + Colors.FAIL + " (No results)" + Colors.ENDC)
            return 
        # Results
        else: 
            print("\n" + Colors.BOLD + "└──" + Colors.ENDC + Colors.OKGREEN + " {} ✔️".format(element.upper()) + Colors.ENDC)

        # General case
        if element != "email":
    
            for account in element_results["accounts"]:
                print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + account["value"] + Colors.ENDC)
        
        # Emails case
        else:
            possible_emails_list = [account["value"] for account in element_results["accounts"]]
            
            for account in element_results["accounts"]:
                    # We pad the emails with spaces for better visibility
                longest_email_length = len(max(possible_emails_list))
                email = account["value"].ljust(longest_email_length + 5)

                # Breached account
                if account["breached"]:
                    print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + email + Colors.FAIL + "[BREACHED]" + Colors.ENDC)
                # Safe account
                else:
                    print(Colors.BOLD + "   ├──" + Colors.ENDC + Colors.HEADER + email + Colors.OKGREEN + "[SAFE]" + Colors.ENDC)