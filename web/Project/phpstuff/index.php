<?php
    require_once 'dbconnector.php';
    $sql = "SELECT * FROM iptime";
    $result =  mysqli_query($conn, $sql);
    //$row = mysqli_fetch_assoc($result);
    //echo $row["ip"];
    if (mysqli_num_rows($result) > 0) {
    // output data of each row
        while($row = mysqli_fetch_assoc($result)) {
            echo "IP:" . $row["ip"]. " - Time" . $row["time"]. "<br>";
        }
    } else {
        echo "0 results";
    }
?>
