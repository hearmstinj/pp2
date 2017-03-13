<?php
    require_once 'dbconnector.php';
    date_default_timezone_set('Asia/Kolkata');
    $curr_time = date('h:i:s');

    $theip = $_SERVER[REMOTE_ADDR];

    $sql = "UPDATE statcounter SET endTime = '$curr_time' WHERE ip = '$theip' AND endTime = '-06:55:35'";

    if(mysqli_query($conn,$sql)){
        echo "New record created successfully.";
    }
    else{
        echo "Error";
    }
?>
