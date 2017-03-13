<?php
session_start();
if(isset($_SESSION['userSession'])!="")
{
 header("Location: ../FrontEnd/RandomHTML/timepass_next_page.html");
}
include_once 'DBConnect.php';

if(isset($_POST['btn-signup']))
{
 $uname = $MySQLi_CON->real_escape_string(trim($_POST['user_name']));
 $email = $MySQLi_CON->real_escape_string(trim($_POST['user_email']));
 $upass = $MySQLi_CON->real_escape_string(trim($_POST['password']));

 $new_password = password_hash($upass, PASSWORD_DEFAULT);

 $check_email = $MySQLi_CON->query("SELECT email FROM users WHERE email='$email'");
 $count=$check_email->num_rows;

 if($count==0){


  $query = "INSERT INTO users(username,email,password) VALUES('$uname','$email','$new_password')";


  if($MySQLi_CON->query($query))
  {
   $msg = "<div class='alert alert-success'>
      <span class='glyphicon glyphicon-info-sign'></span> &nbsp; successfully registered !
     </div>";
  }
  else
  {
   $msg = "<div class='alert alert-danger'>
      <span class='glyphicon glyphicon-info-sign'></span> &nbsp; error while registering !
     </div>";
  }
 }
 else{


  $msg = "<div class='alert alert-danger'>
     <span class='glyphicon glyphicon-info-sign'></span> &nbsp; sorry email already taken !
    </div>";

 }

 $MySQLi_CON->close();
}
?>
