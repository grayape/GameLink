<?php
//echo "we in bzns";
require 'flight/Flight.php';

Flight::route('/', function(){
    echo 'hello world!';
});

Flight::start();
?>
