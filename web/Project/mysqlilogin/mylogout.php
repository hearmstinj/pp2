<?php

    include_once "DBConnect.php";
    require_once "userspecific.php";
    session_start();
    if(isset($_SESSION["cu"])){
        unset($_SESSION["cu"]);
        session_destroy();
        echo true;
    }
    else {
        echo false;
    }

 ?>
