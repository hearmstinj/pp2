<?php

    //Code used to obtain the latest news article links
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

    //Generate the news articles mapped array
    $news = array("aapl" => $referrer[0], "amzn" => $referrer[1], "csco" => $referrer[2], "tsla" => $referrer[3], "msft" => $referrer[4], "ssnlf" => $referrer[5], "googl" => $referrer[6]);

    //Obtain the daily price change metrics for AAPL, AMZN, MSFT and GOOGL
    $symbols = array("aapl", "amzn", "msft", "googl");
    $differences = array();
    foreach ($symbols as $symbol) {
        $current_file = fopen("CSV/" . $symbol . "_HistoricalQuotes.csv", "r");
        $current_value = fgetcsv($current_file);
        $previous_value = fgetcsv($current_file);
        array_push($differences, $current_value[1] - $previous_value[1]);
        fclose($current_file);
    }
    $change = array("aapl" => $differences[0], "amzn" => $differences[1], "msft" => $differences[2], "googl" => $differences[3]);

    //Generate the historical quotes graph for the past 10 days and print close values for each day

    $daily_close = array();
    foreach ($symbols as $symbol) {
        $current_file = fopen("CSV/" . $symbol . "_HistoricalQuotes.csv", "r");
        // Get the last 10 days quotes
        $day = array();
        for ($i = 0; $i < 10; $i++) {
            $row = fgetcsv($current_file);
            array_push($day, $row[0]);
            array_push()
        }
    }

    $final = array("news" => $news, "quotes" => $change);

    echo json_encode($final);
?>
