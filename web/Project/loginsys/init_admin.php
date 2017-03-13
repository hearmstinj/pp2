<?php
error_reporting(0);
include_once('config_admin.php');

mysql_connect(DB_HOST,DB_USER,DB_PASS);
mysql_select_db(DB_NAME);
//file_uploads = On;

include_once('blog.php');
?>
