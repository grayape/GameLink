from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Serial(Activity):
    
    def onCreate(self, data=None):
        self.setLayout("serial")
        self.send("lpc",{"head":'get_tag'})
        
    def receiveLpcMessage(self, message):
        if message["head"]=="tag":
            self.invokeLayoutFunction("updateSerial",message["data"])
            self.send("lpc",{"head":'get_tag'})
            
    def receiveDisplayMessage(self, message):
        if message["head"]=="button_clicked" and message["data"] == "okay":
            self.send("lpc",{'head':'stop_operations'})
            self.switchActivity("mainmenu")
            
  
