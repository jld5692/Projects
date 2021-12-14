<?php
// Contient les différents endPoint accessible coté partenaite



function getPublicData(){
}

function getStationData(){
}

function getMeasuree(){
    $url = "https://api.netatmo.com/api/getmeasure";

    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    $headers = array(
    "Accept: application/json",
    "Authorization: Bearer {$_SESSION['CurrentToken']}",
    "Content-Type: application/json",
    );

    //echo("<br><hr>");

    curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

    $data = <<<DATA
    {
    "device_id":"70:ee:50:12:9f:18", 
    "scale":"1hour",
    "type":"temperature", 
    "limit":"12", 
    "optimize":"false", 
    "real_time": "false"}
    DATA;

    curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

    //for debug only!
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

    $resp = curl_exec($curl);
    $resp_json1 = json_decode($resp, true);
    // echo("<hr>");

    $bouhbou = $resp_json1['time_exec'];
   
    // echo("TEST : {$bouhbou}");      
    // echo("<hr>");
    // curl_close($curl);
    // var_dump($resp);


}



?>