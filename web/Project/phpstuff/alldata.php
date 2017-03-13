<?php
    require_once 'dbconnector.php';
    $sql="SELECT count(*) FROM statcounter";
    $result=mysqli_query($conn, $sql);
    $alldata = array();
    $dc = 0;
    if (mysqli_num_rows($result) > 0) {
    // output data of each row
        while($row = mysqli_fetch_array($result)) {
            $alldata[$dc] = $row[0];
        }
    }
    $dc+=1;
    $sql = "SELECT count(DISTINCT ip) FROM statcounter";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[$dc] = $row[0];
        }
    }

    $sql = "SELECT AVG(TIMESTAMPDIFF(second, startTime, endTime)) FROM statcounter WHERE endTime >= 0";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)){
            $alldata[++$dc] = round($row[0]/60, 2);
        }
    }

    $sql = "SELECT COUNT(ip), COUNT(DISTINCT datevar) FROM statcounter";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result)>0){
        while($row = mysqli_fetch_array($result)){
            $alldata[++$dc] = $row[0]/$row[1];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE touch>0";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE touch=0";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT ref FROM statcounter WHERE ref!='' group by ref ORDER BY count(ref) DESC LIMIT 3";
    $result = mysqli_query($conn, $sql);
    $tempvar = 0;
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%WINDOWS NT%\"";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%X11%\"";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%Android%\"";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $others = $alldata[9] + $alldata[10] + $alldata[11];
    $sql = "SELECT count(os) FROM `statcounter` WHERE 1";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0] - $others;
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width < 640";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >=640 AND width<1024";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >=1024 AND width<=1366";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >1366";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT DISTINCT datevar FROM statcounter WHERE 1 GROUP BY datevar ORDER BY datevar DESC limit 0,5";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM statcounter where os LIKE \"%WINDOWS%\" group by datevar order by datevar desc limit 0,5";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM statcounter where os LIKE \"%Android%\" group by datevar order by datevar desc limit 0,5";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }



    $thedata = array("total" => $alldata[0], "unique" => $alldata[1], "avgsession" => $alldata[2], "dau" => $alldata[3], "touch" => $alldata[4], "ntouch" => $alldata[5], "ref1" => $alldata[6], "ref2" => $alldata[7], "ref3" => $alldata[8], "windowsc" => $alldata[9], "linc" => $alldata[10], "androidc" => $alldata[11], "otherosc" => $alldata[12], "xsmall" => $alldata[13], "small" => $alldata[14], "medium" => $alldata[15], "large" => $alldata[16], "date5" => $alldata[17], "oswin5" => $alldata[22], "date4" => $alldata[18], "oswin4" => $alldata[23], "date3" => $alldata[19], "oswin3" => $alldata[24], "date2" => $alldata[20], "oswin2" => $alldata[25], "date1" => $alldata[21], "oswin1" => $alldata[26], "osand5" => $alldata[27], "osand4" => $alldata[28], "osand3" => $alldata[29], "osand2" => $alldata[30], "osand1" => $alldata[31]);

    #header("Content-Type: application/json");
    echo json_encode($thedata);
 ?>
