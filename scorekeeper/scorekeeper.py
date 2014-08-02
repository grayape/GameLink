#!/usr/bin/python2
from red.app import Red
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Red().start()
