<?php

    include_once 'DBConnect.php';
    session_start();
    $userLoginName = $_GET["loginName"];
    $userLoginPass = $_GET["loginPass"];
    $_SESSION["cu"] = $userLoginName;
    //setcookie("User", $userLoginName, time() + 600);

    $result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE email = '$userLoginName' AND password = '$userLoginPass'");
    //$result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE username = $userLoginName");
    if(mysqli_num_rows($result)>0){
        echo true;
    }
    else {
        echo false;
    }

?>
