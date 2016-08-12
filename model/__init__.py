# -*-coding: utf-8 -*-

import os
import sys

MAIN_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def init_path():
    if not MAIN_PATH == sys.path[0]:
        sys.path.insert(0, MAIN_PATH)


init_path()
