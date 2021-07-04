from profil3r.core.colors import Colors

def print_logo(self):
    print(Colors.OKGREEN + Colors.BOLD + '''
    ____             _____ _______     
   / __ \_________  / __(_) /__  /_____
  / /_/ / ___/ __ \/ /_/ / / /_ </ ___/
 / ____/ /  / /_/ / __/ / /___/ / /    
/_/   /_/   \____/_/ /_/_//____/_/     
                                       
''' + Colors.ENDC)

    print(Colors.HEADER + "Version {version} - Developped by Rog3rSm1th".format(version=self.version))
    print("You can buy me a coffee at : https://www.buymeacoffee.com/givocefo\n" + Colors.ENDC)