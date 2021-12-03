import argparse

# Usage :  profil3r.py [-h] -p PROFILE [PROFILE ...]
# Parse arguments from the command line using argparse
def parse_arguments(self):
    parser = argparse.ArgumentParser(description='Profil3r is an OSINT tool that allows you to find the differents social accounts, domains and emails used by a person')
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--profile', required=True, nargs='+', help="parts of the username that you are looking for, e.g. : john doe")
    args = parser.parse_args()
    
    # Items passed from the command line
    self.items = args.profile