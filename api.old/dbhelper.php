<?php
require_once("VDO.php");

//returns FALSE on failure and teamId on success
/**
 * Returns team id if team exists, or creates new team and returns the id of the new team 
 *
 * @param  Array    $array  array of player ids
 * @return TeamId
 */ 
function getTeamId($array){
    if(!is_array($array)){
        return FALSE;
    }
    global $DB;
    
    //check if team exists
    $playerCount = count($array);
    $commaArray = implode(",",$array);
    $result = $DB->prepareAndExecute("SELECT teamId FROM memberof WHERE playerId IN (?)
                          HAVING COUNT(playerId) = ?",array($commaArray,$playerCount));
    $teamObj = $result->fetchObject();
    
    //Team exists
    //Return Team Id 
    if($teamObj){
        return $teamObj->teamId;
    }
    
    //Team does not exist
    //Create new team
    $DB->prepareAndExecute("INSERT INTO teams (name, rating, wins, losses) VALUES ('',1200,0,0)");
    $teamId = $DB->lastInsertId();
    
    //Add players to team
    foreach($array as $playerId){
        $DB->prepareAndExecute("INSERT INTO memberof (playerId,teamId) VALUES (?,?)",array($playerId,$teamId));
    }
    //return the teamId of the new team
    return $teamId;

}
