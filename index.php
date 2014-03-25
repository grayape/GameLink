<?php
require 'flight/Flight.php';
require_once 'DB.php';

date_default_timezone_set("Europe/Copenhagen");

function match($location, $teama, $teamb, $scorea, $scoreb){
    global $DB;
    $result = $DB->query("INSERT INTO matches 
                          (location,teamA,teamB,teamAScore,teamBScore) VALUES 
                          ($location,$teama,$teamb,$scorea,$scoreb)");
}

function register($rfid, $name){
    global $DB;
    echo "registers player<br/>";
    echo "Player with RFID $rfid registered as $name<br/>";
    $result = $DB->query("INSERT INTO players
                          (rfid,name) VALUES
                          ('$rfid','$name')");
}

Flight::route('/match/@location/@teama/@teamb/@scorea/@scoreb', 'match');
Flight::route('/register/@rfid/@name', 'register');

Flight::start();
?>
