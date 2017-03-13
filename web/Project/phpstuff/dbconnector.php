<?php
    $con_error="Could not connect";
    $mysql_host="localhost";
    $mysql_user="root";
    $mysql_pass="";
    $mysql_db="csv_db";
    $conn= @mysqli_connect($mysql_host, $mysql_user, $mysql_pass) or die($con_error);
    @mysqli_select_db($conn, $mysql_db) or die($con_error);
?>
