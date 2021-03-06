--
-- Table structure for matches
--
CREATE TABLE `matches` (
  `matchId` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(128) NOT NULL,
  `timeCreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `teamA` int(11) NOT NULL,
  `teamB` int(11) NOT NULL,
  `teamAScore` int(3) NOT NULL,
  `teamBScore` int(3) NOT NULL,
  `points` int(11) DEFAULT NULL,
  PRIMARY KEY (`matchId`)
);

--
-- Table structure for players
--
CREATE TABLE `players` (
  `playerId` int(11) NOT NULL AUTO_INCREMENT,
  `rfid` varchar(8) NOT NULL,
  `name` varchar(50) NOT NULL,
  `timeCreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`playerId`)
);

--
-- Table structure for teams
--
CREATE TABLE `teams` (
  `teamId` int(11) NOT NULL AUTO_INCREMENT,
  `timeCreated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(50) NOT NULL,
  `rating` int(11) NOT NULL DEFAULT '1200',
  `wins` int(11) NOT NULL,
  `losses` int(11) NOT NULL,
  PRIMARY KEY (`teamId`)
);

--
-- Table structure for memberof
--
CREATE TABLE `memberof` (
  `playerId` int(11) NOT NULL,
  `teamId` int(11) NOT NULL,
  PRIMARY KEY (`playerId`, `teamId`)
);