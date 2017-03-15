<?php
$file = fopen("../../../CSV/HistoricalQuotes.csv","r");
print_r(fgetcsv($file));
fclose($file);
?>