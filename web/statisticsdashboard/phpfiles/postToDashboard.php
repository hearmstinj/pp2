<?php

    $referrer = array();
    $labels = array();
    $pageScanned = fopen("CSV/lastpagescanned.csv", "r");
    $i = 0;
    while(! feof($pageScanned)){
        $val = fgetcsv($pageScanned);
        array_push($referrer, $val[1]);
        array_push($labels, $val[0]);
        $len = count($referrer);
    }

    

    // Echo the json conversion of the array back to the dashboard
    $news = array("aapl" => $referrer[0], "amzn" => $referrer[1], "csco" => $referrer[2], "tsla" => $referrer[3], "msft" => $referrer[4], "ssnlf" => $referrer[5]);
    //print_r($news);
    //$json = json_encode($news);
    //print($json);
    echo json_encode($news);
?>
