from red.activity import Activity
from models.model import Match, Player, Team, Base, initSchema

class Match(Activity):
   
    def onCreate(self,data=None):
        self.setLayout("match")
        self.match = data
        self.updateLayout()
     

    def receiveDisplayMessage(self,message):
        if message["head"] == "button_clicked":          
            if message["data"] == "a_scored":
                self.team_scored("a");
            elif message["data"] == "b_scored":
                self.team_scored("b");
            elif message["data"] == "end_match":
                self.end_match()
        else:
            print("We (match) received something (message), but we are unsure what it is")
      

    def end_match(self):
        self.switchActivity("confirmresult", data=self.match)
        
        
    def team_scored(self, team):
        if team == 'a':
            scoring_team = self.match.teama;
            self.match.scorea = self.match.scorea + 1
        elif team == 'b':
            scoring_team = self.match.teamb;
            self.match.scoreb = self.match.scoreb + 1
        else:
            print ("Who the hell scored")
        
        print("Some scored it was team: " + scoring_team.name)
        print("Score is now: %s - %s" % (self.match.scorea  ,self.match.scoreb))
        # Broadcast to display
        self.updateLayout()


    def updateLayout(self):
        self.invokeLayoutFunction("updateScoreA",self.match.scorea)
        self.invokeLayoutFunction("updateScoreB",self.match.scoreb)
            

    
