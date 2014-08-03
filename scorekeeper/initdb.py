#!/usr/bin/python2
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from red.config      import config, initConfig

configFile='meta.conf'
initConfig(configFile)

from models.model import initSchema,initData

initSchema()
initData()