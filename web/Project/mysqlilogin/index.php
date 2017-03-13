<?php
session_start();
include_once 'DBConnect.php';

if(isset($_SESSION['userSession'])!="")
{
 header("Location: ../FrontEnd/RandomHTML/timepass_next_page.html");
 exit;
}

if(isset($_POST['btn-login']))
{
 $email = $MySQLi_CON->real_escape_string(trim($_POST['user_email']));
 $upass = $MySQLi_CON->real_escape_string(trim($_POST['password']));

 $query = $MySQLi_CON->query("SELECT * FROM users WHERE email='$email'");
 $row=$query->fetch_array();

 if(password_verify($upass, $row['password']))
 {
  $_SESSION['userSession'] = $row['user_id'];
  header("Location: home.php");
 }
 else
 {
  $msg = "
        email or password does not exists !
    ";
 }

 $MySQLi_CON->close();

}
?>
