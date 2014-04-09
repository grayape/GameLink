<?php
require_once("DB.php");

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
    $result = $DB->query("SELECT teamId FROM memberof WHERE playerId IN ($commaArray)
                          HAVING COUNT(playerId) = $playerCount;");
    $teamObj = mysql_fetch_object($result);
    
    //Team exists
    //Return Team Id 
    if($teamObj){
        return $teamObj->teamId;
    }
    
    //Team does not exist
    //Create new team
    $result = $DB->query("INSERT INTO teams (name, rating, wins, losses) VALUES ('',1200,0,0);");
    $teamId = mysqli_insert_id();
    
    //Add players to team
    foreach($array as $playerId){
        $result = $DB->query("INSERT INTO memberof (playerId,teamId) VALUES ($playerId,$teamId)");
    }
    //return the teamId of the new team
    return $teamId;

}
