
from red.activity import Activity


class Confirmresult (Activity):

    def onCreate(self, data=None):
        """ onCreate"""
        self.setLayout("confirm")
        self.match = data
        self.invokeLayoutFunction("updateMatchResult",str(self.match.scorea) + " - " + str(self.match.scoreb))

    def receiveDisplayMessage(self,message):
        if message["head"] == "button_clicked":          
            if message["data"] == "confirm":
                self.saveMatch()
            elif message["data"] == "cancel":
                self.cancel()
        else:
            self.logger.critical("We " + __file__ +" received something (message), but we are unsure what it is")
      
    def saveMatch(self):
        self.session.commit()
        self.send("synchronize", head= "match", data=self.match.asDict())
        self.switchActivity("mainmenu")

    def cancel(self):
        self.switchActivity("match", data=self.match)
        