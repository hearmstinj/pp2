<?php

	if(isset($_GET['title'])){ $title = $_GET['title']; }
	if(isset($_GET['date'])){ $date = $_GET['date']; }
	if(isset($_GET['fromtime'])){ $fromt = $_GET['fromtime']; }
	if(isset($_GET['totime'])){ $tot = $_GET['totime']; }
	if(isset($_GET['priority'])){ $priority = $_GET['priority']; }

	$db=mysqli_connect("localhost","root","","test")or die("Cannot connect to DATABASE");

	$sql = "INSERT INTO `taskdata`(`Title`, `Date`, `FromTime`, `ToTime`, `Priority`) VALUES ('$title', '$date', '$fromt', '$tot', '$priority');";

	$result = mysqli_query($db, $sql) or die("Cannot QUERY");

?>
