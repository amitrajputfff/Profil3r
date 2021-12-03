import sys
from itertools import chain, combinations
from profil3r.core import Core
from profil3r.core.colors import Colors
from multiprocessing import Process

CONFIG = './config.json'

profil3r = Core(CONFIG).run()