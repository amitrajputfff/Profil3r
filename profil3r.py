import sys
from itertools import chain, combinations
from core import Core
from core.colors import Colors
from multiprocessing import Process

CONFIG = './config.json'

profil3r = Core(CONFIG).run()