<?php
    require_once 'dbconnector.php';
    $sql="SELECT count(*) FROM statcounter WHERE touch>0";
    $result=mysqli_query($conn, $sql);
    $alldata = array();
    $dc = 0;
    $sql="SELECT count(*) FROM statcounter WHERE width<640";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result)>0)
    {
      while($row=mysqli_fetch_array($result))
      {
        $alldata[$dc]=$row[0];
      }
    }
    $dc+=1;
    $sql="SELECT count(*) FROM statcounter WHERE width>=640 and width<1024";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result)>0)
    {
      while($row=mysqli_fetch_array($result))
      {
        $alldata[$dc]=$row[0];
      }
    }
    $dc+=1;
    $sql="SELECT count(*) FROM statcounter WHERE width>=1024 and width<=1366";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result)>0)
    {
      while($row=mysqli_fetch_array($result))
      {
        $alldata[$dc]=$row[0];
      }
    }
    $dc+=1;
    $sql="SELECT count(*) FROM statcounter WHERE width>1366";
    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result)>0)
    {
      while($row=mysqli_fetch_array($result))
      {
        $alldata[$dc]=$row[0];
      }
    }
    $thedata = array("xsmall" => $alldata[0], "small"=>$alldata[1],"medium"=>$alldata[2],"large"=>$alldata[3]);
    #header("Content-Type: application/json");
    echo json_encode($thedata);
?>
