#!/usr/bin/python2
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from red.app import Red

Red().start()
