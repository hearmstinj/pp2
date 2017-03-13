<?php

    include_once "DBConnect.php";
    require_once "userspecific.php";
    
    if(isset($_SESSION["cu"])){

        echo $_SESSION["cu"];
    }
    else {
        echo false;
    }

 ?>
