from red.activity import Activity
from models.model import Match, Player, Team, Base, initSchema

class Recentmatches(Activity):

    def onCreate(self, data=None):
        self.setLayout("recentmatches")
        self.match = data
        if(self.match == None):
            self.match = Match.getRecent(self.session)
        self.updateLayout()


    def receiveDisplayMessage(self, message):
        if message["head"] == "echo":
            return 
        elif message["head"] == "button_clicked":
            if message["data"] == "back":
                self.back()


    def back(self):
        self.switchActivity("mainmenu")


    def updateLayout(self):
        self.invokeLayoutFunction("updateScoreA",self.match.scorea)
        self.invokeLayoutFunction("updateTeamA", reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.match.teama.players)))

        self.invokeLayoutFunction("updateScoreB",self.match.scoreb)
        self.invokeLayoutFunction("updateTeamB", reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.match.teamb.players)))