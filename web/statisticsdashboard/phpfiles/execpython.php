<?php
$start_date = $_GET["start"];
$end_date = $_GET["end"];
$capital = $_GET["capital"];
$read = exec("python trial.py " . $start_date . " " . $end_date . " " . $capital);
$text = fopen("graph.txt", "r");
echo fread($text, filesize("graph.txt"));


?>
