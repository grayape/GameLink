#!/usr/bin/python2
#server.py

from flask import Flask, request
import json
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from red.config import initConfig
initConfig('meta.conf')
from models.model import Player
from util import crossdomain

class Server(object):
    
    def start(self):

 
        app = Flask(__name__)
        
        @app.route("/", methods=['GET', 'POST'])
        def hello():
            return "Hello World!"

        @app.route("/players", methods=['GET'])
        @crossdomain(origin='*')
        def getPlayers():
            return json.dumps([{"name":'Rasmus',"id":1,"matches_played":2},{"name":'Kim',"id":2,"matches_played":2}])
            h = resp.headers
            h['Access-Control-Allow-Origin'] = '*'
        
        # from OpenSSL import SSL
        # context = SSL.Context(SSL.SSLv23_METHOD)
        # context.use_privatekey_file('new.cert.key')

        # app.run(host='77.66.51.6',port=2323, debug=True) #, ssl_context=context)  
        # app.run(host='192.168.1.100',port=12346, debug=True) #, ssl_context=context)  
        app.run(host='127.0.0.1',port=12345, debug=True) #, ssl_context=context)  
          

 
# from server.server import Server

Server().start()