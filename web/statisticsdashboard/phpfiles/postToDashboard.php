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
    $symbols = array("aapl", "amzn", "csco", "googl", "msft", "tsla");
    $differences = array();
    foreach ($symbols as $symbol) {
        $current_file = fopen("CSV/" . $symbol . "_HistoricalQuotes.csv", "r");
        $current_value = fgetcsv($current_file);
        $previous_value = fgetcsv($current_file);
        array_push($differences, $current_value[1] - $previous_value[1]);
        fclose($current_file);
    }
    $change = array("aapl" => $differences[0], "amzn" => $differences[1], "msft" => $differences[3], "googl" => $differences[4]);

    // ============================================================================================
    //Generate the historical quotes graph for the past 10 days and print close values for each day

    $daily_close = array();
    $file_handlers = array();
    foreach ($symbols as $symbol) {
        array_push($file_handlers, fopen("CSV/" . $symbol . "_HistoricalQuotes.csv", "r"));
    }

    for ($i = 0; $i < 10; $i++) {
        $day = array();
        array_push($day, "date");
        for ($j = 0; $j < 6; $j++) {
            $row = fgetcsv($file_handlers[$j]);
            $day_split = explode("/", $row[0]);
            $day[0] = $day_split[0] . "-" . $day_split[1] . "-" . $day_split[2];
            array_push($day, $row[1]);
        }
        array_push($daily_close, $day);
    }
    // ============================================================================================

    // ============================================================================================
    // Generate the bar graph showing accuracies of each stock

    $accuracies = array();
    foreach ($symbols as $symbol) {
        if($symbol == 'csco') {
            continue;
        }
        $file_handler = fopen("CSV/FinalResult.csv", "r");
        for ($i = 0; $i < 5; $i++) {
            $row = fgetcsv($file_handler);
            array_push($accuracies, $row[2]);
        }
    }
    // ============================================================================================

    $final = array("news" => $news, "quotes" => $change, "history" => $daily_close, "accuracy" => $accuracies);

    echo json_encode($final);
?>
