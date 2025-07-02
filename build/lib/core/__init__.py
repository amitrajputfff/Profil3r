from profil3r.modules.email import email
import json

class Core(object):

    from ._menu import menu
    from ._permutations import get_permutations
    from ._results import print_results
    from ._run import run
    from ._report import generate_report, generate_json_report, generate_HTML_report, generate_csv_report
    from ._modules import modules_update, get_report_modules
    from ._logo import print_logo
    from ._argparse import parse_arguments
    
    from .services._social import facebook, twitter, instagram, tiktok, pinterest, linktree, myspace
    from .services._forum import zeroxzerozerosec, jeuxvideo, hackernews, crackedto
    from .services._programming import github, pastebin, replit
    from .services._tchat import skype
    from .services._music import soundcloud, spotify
    from .services._entertainment import dailymotion, vimeo
    from .services._email import email
    from .services._porn import pornhub, redtube, xvideos
    from .services._money import buymeacoffee, patreon
    from .services._domain import domain

    def __init__(self, config_path):
        self.version = "1.3.5"

        with open(config_path, 'r') as f:
            self.CONFIG = json.load(f)

        self.separators = []
        self.result = {}
        self.permutations_list = []
        self.modules = {
            # Emails
            "email":             {"method" : self.email },
            # Social
            "facebook":          {"method" : self.facebook},
            "twitter":           {"method" : self.twitter},
            "tiktok":            {"method" : self.tiktok},
            "instagram":         {"method" : self.instagram},
            "pinterest":         {"method" : self.pinterest},
            "linktree":          {"method" : self.linktree},
            "myspace":           {"method" : self.myspace},
            # Music
            "soundcloud":        {"method" : self.soundcloud},
            "spotify":           {"method" : self.spotify},
            # Programming 
            "github":            {"method" : self.github},
            "pastebin":          {"method" : self.pastebin},
            "replit":            {"method" : self.replit},
            # Forums:
            "0x00sec":           {"method" : self.zeroxzerozerosec},
            "jeuxvideo.com":     {"method" : self.jeuxvideo},
            "hackernews":        {"method" : self.hackernews},
            "crackedto":         {"method" : self.crackedto},
            # Tchat
            "skype":             {"method" : self.skype},
            # Entertainment
            "dailymotion":       {"method" : self.dailymotion},
            "vimeo":             {"method" : self.vimeo},   
            # Porn 
            "pornhub":           {"method" : self.pornhub},
            "redtube":           {"method" : self.redtube},
            "xvideos":           {"method" : self.xvideos},
            # Money
            "buymeacoffee":      {"method" : self.buymeacoffee},
            "patreon":           {"method" : self.patreon},
            # Domain
            "domain":            {"method" : self.domain}
        }