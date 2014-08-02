#!/usr/bin/python2
from red.config      import config, initConfig
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

configFile='meta.conf'
initConfig(configFile)

from models.model import initSchema,initData

initSchema()
initData()