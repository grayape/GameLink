#models.py
# I have collected all models into this file/module because it is easier for SQLAlchemy 
# Feel free to split it up into more files if you can (dare)

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Table, Text, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime
from red.config import config
from red.utils.run_once import run_once
import traceback

Base = declarative_base()
engine = create_engine(config.get("Database","connectionstring"),echo=False)

#################################################################################################################
################################## Table used to connect players and to teams ###################################
#################################################################################################################
player_team = Table('player_team',Base.metadata,
    Column('player_id',Integer,ForeignKey('players.id')),
    Column('team_id',Integer,ForeignKey('teams.id'))
)

#################################################################################################################
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer,Sequence('player_id_seq'),primary_key=True)
    rfid = Column(String,unique=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return "<Player(name='%s')>" % (self.name)

    @staticmethod
    def createOrLoad(rfid,session):
        playerList = session.query(Player).filter(Player.rfid == rfid)
        if playerList.count() <= 0:
            session.add(Player(name=rfid,rfid=rfid))
        return session.query(Player).filter(Player.rfid == rfid).one()

#################################################################################################################
class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer,Sequence('match_id_seq'),primary_key=True)
    scorea = Column(Integer,default = int(0), nullable = False)
    scoreb = Column(Integer,default = int(0), nullable = False)
    teama_id = Column(Integer,ForeignKey('teams.id'))
    teama = relationship('Team', backref=backref('matches_a', order_by=id),foreign_keys=teama_id)
    teamb_id = Column(Integer,ForeignKey('teams.id'))
    teamb = relationship('Team', backref=backref('matches_b', order_by=id),foreign_keys=teamb_id)
    created_at = Column(DateTime, default=func.now())
  

    def asDict(self):
        return {
            "scorea"       : self.scorea    ,
            "scoreb"       : self.scoreb    ,
            "teama"     : map(lambda x: x.rfid , self.teama.players),
            "teamb"     : map(lambda x: x.rfid , self.teamb.players)
        }

    @staticmethod
    def getRecent(session):
        return session.query(Match).order_by(-Match.id).limit(1).first()

#################################################################################################################
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer,Sequence('team_id_seq'),primary_key=True)
    name = Column(String)
    players = relationship('Player',secondary='player_team',backref='teams')
    created_at = Column(DateTime, default=func.now())


    def matches(self):
        return self.matches_a + self.matches_b

    def size(self):
        return len(self.players)

    def __repr__(self):
        return "<Team(name='%s', players='%s')>" % (self.name, self.players)

    @staticmethod
    def createOrLoad(players,session):
        teams = []
        resultTeam = None
        if players == None or len(players) < 1:
            raise Exception("Atleast one player is needed")
        for player in players:
            teams.append(player.teams)
        

        intersectList = reduce(lambda xs,ys: filter(lambda x : x in xs,ys),teams)
        for team in intersectList:
            #team exists, set as local team
            if team.size() == len(teams):
                resultTeam = team
                break

        if resultTeam == None:
            resultTeam = Team(name = " & ".join(map(lambda x: x.name,players)))
            for player in players:
                resultTeam.players.append(player)
            session.add(resultTeam)
        
        if resultTeam == None:
            raise Exception("Result team not set.")

        return resultTeam

def initSchema():
    Base.metadata.create_all(engine)

def dropSchema():
    Base.metadata.drop_all(engine)

def initData():
    session = sessionmaker(bind=engine)()
    p1 =  Player(name='Rasmus',   rfid='1')
    p2 =  Player(name='Kim',   rfid='2')

    try:
        p = [ \
                p1,\
                p2,\
                Player(name='Simon',    rfid='3'),\
                Player(name='Alex',     rfid='4'),\
                Player(name='Mikael',   rfid='5')\
            ]
        session.add_all(p)

        session.commit()

        teamA = Team.createOrLoad([p1],session)
        teamB = Team.createOrLoad([p2],session)
        session.commit()
        match = Match(teama = teamA, teamb = teamB, scorea = 10, scoreb = 0)

        session.add(match)
        session.commit()
    except:
        print(traceback.format_exc())
        session.rollback()
        raise Exception("Rolling back initialize data")

"""
I am considering changing matches such that their not only include the final results, but also "events", such as a scoring.
If we do it like that we will get even more statistics available, and we have discussed having automatic notices of 
goals being scored anyways. Please note that this is not something we need immediately, but it might worth implementing later.
"""

@run_once
def init():
    initSchema();

init()
