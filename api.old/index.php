<?php
require 'flight/Flight.php'; //https://github.com/mikecao/flight
require_once 'VDO.php';
require_once("dbhelper.php");

date_default_timezone_set("Europe/Copenhagen");
//$location, $teama, $teamb, $scorea, $scoreb
//sytax:
 //{
     //"teama": [
         //1,
         //2,
         //3
     //],
     //"teamb": [
         //1,
         //2, 
         //3
     //],
     //"scorea": 123,
     //"scoreb": 123,
     //"location": 123
 //}
function match(){
    $inputData = Flight::request();
    
    $obj = json_decode($inputData->body);
    
    //TODO:CHECK UP AGAINST JSON SCHEMA
    
    //CHECK IF TEAMS EXIST ETC
    $teamaId = getTeamId($obj->teama);
    $teambId = getTeamId($obj->teamb);
    
    //Flight::json(array('yolo' => $teamaId)); // this is how to debug bro
    
    //INSERT MATCH INTO DB
    global $DB;
    $result = $DB->prepareAndExecute("INSERT INTO matches 
                          (location,teamA,teamB,teamAScore,teamBScore) VALUES 
                          (?,?,?,?,?)",array($obj->location,$teamaId,$teambId,$obj->scorea,$obj->scoreb));
}

function register($rfid, $name){
    global $DB;
    $result = $DB->prepareAndExecute("INSERT INTO players
                          (rfid,name) VALUES
                          ('?','?')",array($rfid,$name));
}

function team(){
    //list of players
}



Flight::route('POST|GET /match', 'match');
Flight::route('/register/@rfid/@name', 'register');

Flight::start();
