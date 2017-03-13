<?php

    include_once 'DBConnect.php';
    session_start();
    $domname = $MySQLi_CON->real_escape_string(trim($_POST['user_name']));
    $uemail = $MySQLi_CON->real_escape_string(trim($_POST['user_email']));
    $upassword = $MySQLi_CON->real_escape_string(trim($_POST['password']));
    $_SESSION["cu"] = $uemail;
    //setcookie("User", $uemail, time() + 600);

    $result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE email = \"$uemail\"");
    if(mysqli_num_rows($result) > 0){
        echo "falseval";
    }
    if(mysqli_num_rows(mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE domain = \"$domname\""))){
        echo "falseval";
    }
    else {
        $sql = "INSERT INTO users(domain, email, password) VALUES ('$domname', '$uemail', '$upassword')";
        mysqli_query($MySQLi_CON, $sql);
    }

 ?>
