#!/usr/bin/python2
import sys
import os
sys.path.insert(1,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.model import dropSchema


dropSchema()