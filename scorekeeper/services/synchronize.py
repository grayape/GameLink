#synchronize.py

from red.services.base import Service
from threading import Thread

import json
from red.config import config
import requests

class Synchronize(Service, Thread):

    def __init__(self, name, context=None):
        super(Synchronize, self).__init__(name=name, context=context)
        self.serverurl = config.get('Scorekeeper', 'server_url')
        self.location = config.get('Scorekeeper', 'location')



    def processMessage(self, msg):
        if "head" in msg and "data" in msg:
            if msg["head"] == "match":
                self.syncMatch(msg["data"])
                return True


    def syncMatch(self, data):
        data['location'] = self.location
        r = requests.post(self.serverurl + '/match', data=json.dumps(data))


    # def convertData(self, match, location):
    #     result = dict()
    #     print match
    #     result["teama"] =  map(lambda x: x.rfid, match.teama.players)
    #     result["teamb"] =  map(lambda x: x.rfid, match.teamb.players)
    #     result["scorea"] = match.scorea
    #     result["scoreb"] = match.scoreb
    #     result["location"] = location

    #     return result
    #    