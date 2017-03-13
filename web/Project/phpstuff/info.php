<?php
    require_once 'dbconnector.php';
    date_default_timezone_set('Asia/Kolkata');
    $curr_time = date('h:i:s');
    $sql = "INSERT INTO iptime(ip, time) VALUES ('$_SERVER[REMOTE_ADDR]', '$curr_time')";
    if(mysqli_query($conn,$sql)){
        echo "New record created successfully.";
    }
    else{
        echo "Error";
    }

    //Point of time where we insert client info from browser
    $touch = $_GET['touch'];
    $os = $_GET['os'];
    $ref = $_GET['ref'];
    $host = $_GET['host'];
    $path = $_GET['path'];

    $queryInfo = "INSERT INTO client(Touch, OS, Referrer, Host, Pathname) VALUES ($touch, '$os', '$ref', '$host', '$path')";
    if(mysqli_query($conn, $queryInfo)){
        echo "New record created successfully.";
    }
    else {
        echo "Error.";
    }
?>
