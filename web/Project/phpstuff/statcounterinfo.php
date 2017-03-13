<?php
    require_once 'dbconnector.php';
    date_default_timezone_set('Asia/Kolkata');
    $curr_time = date('h:i:s');
    /*$sql = "INSERT INTO statcounter(ip, startTime) VALUES ('$_SERVER[REMOTE_ADDR]', '$curr_time')";
    if(mysqli_query($conn,$sql)){
        echo "New record created successfully.";
    }
    else{
        echo "Error";
    }*/

    //Point of time where we insert client info from browser
    $touch = $_GET['touch'];
    $os = $_GET['os'];
    $ref = $_GET['ref'];
    $host = $_GET['host'];
    $path = $_GET['path'];
    $width = $_GET['width'];
    $height = $_GET['height'];
    $date = $_GET['date'];

    $queryInfo = "INSERT INTO statcounter(ip, startTime, touch, os, ref, hostname, pathname, width, height, datevar) VALUES ('$_SERVER[REMOTE_ADDR]', '$curr_time', $touch, '$os', '$ref', '$host', '$path', '$width', '$height', STR_TO_DATE('$date', '%b %d %Y'))";
    if(mysqli_query($conn, $queryInfo)){
        echo "New record created successfully.";
    }
    else {
        echo "Error.";
    }
?>
