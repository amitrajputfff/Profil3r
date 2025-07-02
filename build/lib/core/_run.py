from profil3r.core.colors import Colors
import threading

def run(self):
    self.print_logo()
    # Get arguments from the command line
    self.parse_arguments()

    self.menu()
    self.get_permutations()

    # Number of permutations to test per service
    print(Colors.BOLD + "[+]" + Colors.ENDC + " {} permutations to test for each service, you can reduce this number by selecting less options if it takes too long".format(len(self.permutations_list)))

    modules = self.get_report_modules()

    print("\n" + "Profil3r will search : \n " + Colors.BOLD + "[+] " + Colors.ENDC +  "{} \n".format(str('\n ' + Colors.BOLD + "[+] " + Colors.ENDC).join(modules)))

    for module in modules:
        thread = threading.Thread(target=self.modules[module]["method"])
        thread.start()
        thread.join()
    self.generate_report()