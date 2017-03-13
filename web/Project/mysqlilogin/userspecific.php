<?php


    require_once 'DBConnect.php';
    session_start();

    if(!isset($_GET["logvar"]) && !isset($_GET["display"]) & isset($_GET["regvar"])){

        $domname = $MySQLi_CON->real_escape_string(trim($_GET['user_name']));
        $uemail = $MySQLi_CON->real_escape_string(trim($_GET['user_email']));
        $upassword = $MySQLi_CON->real_escape_string(trim($_GET['password']));
        $_SESSION["cu"] = $uemail;
        $_SESSION["displayuser"] = $uemail;
        //setcookie("User", $uemail, time() + 600);

        $result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE email = \"$uemail\"");
        if(mysqli_num_rows($result) > 0){
            echo "falseval";
            session_destroy();
        }
        else if(mysqli_num_rows(mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE domain = \"$domname\""))){
            echo "falseval";
            session_destroy();
        }
        else {
            $sql = "INSERT INTO users(domain, email, password) VALUES ('$domname', '$uemail', '$upassword')";
            mysqli_query($MySQLi_CON, $sql);
            echo true;
        }

    }


    else if(!isset($_GET["logvar"]) && !isset($_GET["display"])){
        if(isset($_SESSION["cu"])){
            echo $_SESSION["displayuser"];
        }
        else
            echo false;
    }



    else if(!isset($_SESSION["cu"])){
        $userLoginName = $_GET["loginName"];
        $userLoginPass = $_GET["loginPass"];
        $_SESSION["cu"] = $userLoginName;
        $_SESSION["displayuser"] = $userLoginName;
        //setcookie("User", $userLoginName, time() + 600);

        $result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE email = '$userLoginName' AND password = '$userLoginPass'");
        //$result = mysqli_query($MySQLi_CON, "SELECT * FROM users WHERE username = $userLoginName");
        if(mysqli_num_rows($result)>0){
            echo true;
        }
        else {
            echo false;
            session_destroy();
        }
    }

else if(isset($_SESSION["cu"])){




    $alldata = array();
    $dc = 0;
    $host = "17abcxyz";
    $cvar = 0;
    $current_user = $_SESSION["cu"];
    //$current_user = $_COOKIE["User"];
    $limitcount = 0; $lolval = array();
    $result = mysqli_query($MySQLi_CON, "SELECT domain FROM users WHERE email LIKE '%$current_user%'");
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $host = $row[0];
            $lolval[0] = $row;
        }
    }
    else $lolval[0] = "no execution of $result";

    $sql = "SELECT hostname FROM statcounter WHERE hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) == 0){
        $cvar = 1;
    }

    $sql="SELECT count(*) FROM statcounter WHERE hostname LIKE \"%$host%\"";
    $result=mysqli_query($MySQLi_CON, $sql);

    if (mysqli_num_rows($result) > 0) {
    // output data of each row
        while($row = mysqli_fetch_array($result)) {
            $alldata[$dc] = $row[0];
        }
    }
    $dc+=1;
    $sql = "SELECT count(DISTINCT ip) FROM statcounter WHERE hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[$dc] = $row[0];
        }
    }

    $sql = "SELECT AVG(TIMESTAMPDIFF(second, startTime, endTime)) FROM statcounter WHERE endTime >= 0 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)){
            $alldata[++$dc] = round($row[0]/60, 2);
        }
    }

    $sql = "SELECT COUNT(ip), COUNT(DISTINCT datevar) FROM statcounter WHERE 1 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result)>0){
        while($row = mysqli_fetch_array($result)){
            if($row[1]!=0){
                $alldata[++$dc] = $row[0]/$row[1];
            }
            else {
                $alldata[++$dc] = 0;
            }
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE touch>0 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE touch=0 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT ref FROM statcounter WHERE ref!='' AND hostname LIKE \"%$host%\" group by ref ORDER BY count(ref) DESC LIMIT 3";
    $result = mysqli_query($MySQLi_CON, $sql);
    $tempvar = 0;
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    while($dc < 8){
        $alldata[++$dc] = 0;
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%WINDOWS NT%\" AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%X11%\" AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    if($dc < 10){
        $alldata[++$dc] = 0;
    }

    $sql = "SELECT count(os) FROM `statcounter` WHERE os LIKE \"%Android%\" AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    if($dc < 11){
        $alldata[++$dc] = 0;
    }

    $others = $alldata[9] + $alldata[10] + $alldata[11];
    $sql = "SELECT count(os) FROM `statcounter` WHERE 1 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0] - $others;
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width < 640 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >=640 AND width<1024 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >=1024 AND width<=1366 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT COUNT(*) FROM statcounter WHERE width >1366 AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT DISTINCT datevar FROM statcounter WHERE 1 AND hostname LIKE \"%$host%\" GROUP BY datevar ORDER BY datevar DESC limit 0,5";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }

    $sql = "SELECT count(os) FROM statcounter where os LIKE \"%WINDOWS%\" AND hostname LIKE \"%$host%\" group by datevar order by datevar desc limit 0,5";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
            //$alldata[++$dc] = $row[0]? $row[0] : 0;
            //$cvar++;
        }
    }

    $sql = "SELECT count(os) FROM statcounter where os LIKE \"%Android%\" AND hostname LIKE \"%$host%\" group by datevar order by datevar desc limit 0,5";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    while($dc < 31){
        $alldata[++$dc] = 0;
    }

    $sql = "SELECT count(os) FROM statcounter WHERE os LIKE \"%Chrome%\" AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    while($dc < 32){
        $alldata[++$dc] = 0;
    }

    $sql = "SELECT count(os) FROM statcounter WHERE os LIKE \"%.NET%\" AND hostname LIKE \"%$host%\"";
    $result = mysqli_query($MySQLi_CON, $sql);
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)) {
            $alldata[++$dc] = $row[0];
        }
    }
    while($dc < 33){
        $alldata[++$dc] = 0;
    }

    $thedata = array("total" => $alldata[0], "unique" => $alldata[1], "avgsession" => $alldata[2], "dau" => $alldata[3], "touch" => $alldata[4], "ntouch" => $alldata[5], "ref1" => $alldata[6], "ref2" => $alldata[7], "ref3" => $alldata[8], "windowsc" => $alldata[9], "linc" => $alldata[10], "androidc" => $alldata[11], "otherosc" => $alldata[12], "xsmall" => $alldata[13], "small" => $alldata[14], "medium" => $alldata[15], "large" => $alldata[16], "date5" => $alldata[17], "oswin5" => $alldata[22], "date4" => $alldata[18], "oswin4" => $alldata[23], "date3" => $alldata[19], "oswin3" => $alldata[24], "date2" => $alldata[20], "oswin2" => $alldata[25], "date1" => $alldata[21], "oswin1" => $alldata[26], "osand5" => $alldata[27], "osand4" => $alldata[28], "osand3" => $alldata[29], "osand2" => $alldata[30], "osand1" => $alldata[31], "whoisthere" => $_SESSION["cu"], "thehost" => $host, "current_user" => $current_user, "cu" => $_SESSION["cu"], "limitcount" => $limitcount, "istheredata" => $cvar, "chromeusers" => $alldata[32], "slowpokes" => $alldata[33]);

    #header("Content-Type: application/json");
    echo json_encode($thedata);
    //unset($_SESSION["cu"]);
    //session_destroy();

}
 ?>
