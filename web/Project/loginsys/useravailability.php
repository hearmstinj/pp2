<?php
include 'init.php';

if(isset($_POST['username']))
{
$username = $_POST['username'];
$username = mysql_real_escape_string($username);
$sql_check = mysql_query("SELECT user_id FROM login WHERE username='$username'");
if(mysql_num_rows($sql_check))
{
echo 'not available';
}
else
{
echo 'available';
}
}

?>
