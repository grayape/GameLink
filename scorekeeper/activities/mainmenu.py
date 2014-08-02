from red.activity import Activity


class Mainmenu(Activity):
    """ MainMenu """

    def onCreate(self, data=None):
        """ onCreate"""
        self.setLayout("mainmenu")
        self.send("lpc",{"head":'get_tag'})
       
    def receiveDisplayMessage(self, message):

        """ Receives stuff """
        if message["head"] == "button_clicked":          
            if message["data"] == "new_match":
                self.switchActivity("creatematch")
            elif message["data"] == "recent_matches":
                self.switchActivity("recentmatches")
            elif message["data"] == "get_serial":
                self.switchActivity("serial")
        else:
            self.logger.critical("We " + __file__ +" received something (message), but we are unsure what it is. It Was: " + str(message))

    def receiveLpcMessage(self,message):
        if message["head"]=="tag":
            if len(message["data"]) > 0:
                self.switchActivity("creatematch",[message["data"]]) #it expects a list of rfids
            else:
                self.send("lpc",{"head":'get_tag'})

    def receiveSynchronizeMessage(self, message):
        print message