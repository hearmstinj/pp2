<?php
    include 'init.php';
    session_start();

    $uName = $_POST['name'];
    $pWord = $_POST['pwd'];
    $qry = "SELECT user_id,username FROM login WHERE username='".$uName."' AND password='".$pWord."'" ;
    $res = mysql_query($qry);
    $num_row = mysql_num_rows($res);
    $row=mysql_fetch_assoc($res);
    if( $num_row == 1)
    {
        $_SESSION['username'] = $row['username'];
    }
    else {
        echo 'false';
    }

?>
