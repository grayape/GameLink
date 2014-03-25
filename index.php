<?php
require 'flight/Flight.php';
require_once 'DB.php';

function match($location, $teama, $teamb, $scorea, $scoreb){
    global $DB;
    $draw = FALSE;
    $aiswinner = FALSE;
    echo "inserts match<br/>";
    echo "$teama $scorea - $scoreb $teamb<br/>";
    $result = $DB->query("INSERT INTO matches 
                              (location,teamA,teamB,teamAScore,teamBScore) VALUES 
                              ($location,$teama,$teamb,$scorea,$scoreb)");
}

function register($rfid, $name){
    echo "registers player<br/>";
    echo "Player with RFID $rfid registered as $name<br/>";
}

Flight::route('/match/@location/@teama/@teamb/@scorea/@scoreb', 'match');
Flight::route('/register/@rfid/@name', 'register');

Flight::start();
?>
