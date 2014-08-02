#!/usr/bin/python2
from red.config      import config, initConfig

configFile='meta.conf'
initConfig(configFile)

from models.model import initSchema,initData

initSchema()
initData()