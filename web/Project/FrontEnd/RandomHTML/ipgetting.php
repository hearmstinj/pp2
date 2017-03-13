<!DOCTYPE html>
<html>
<head>
    <title>IP and time</title>
</head>
<body>
    <?php
        require_once '../../phpstuff/dbconnector.php';
        date_default_timezone_set('Asia/Kolkata');
        $curr_time = date('h:i:s');
        $sql = "INSERT INTO iptime(ip, time) VALUES ('$_SERVER[REMOTE_ADDR]', '$curr_time')";
        if(mysqli_query($conn,$sql)){
            echo "New record created successfully.";
        }
        else{
            echo "Error";
        }
    ?>
</body>
</html>
