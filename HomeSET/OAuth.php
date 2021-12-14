<?php
// Contient les fonctions nécessaire à l'authentification

    function httpPost($url, $data){
        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($curl);

        $parsed_json = json_decode($response);
                            
        $_SESSION['CurrentToken']   = $parsed_json->{'access_token'};
        $_SESSION['Refresh_token']  = $parsed_json->{'refresh_token'};
        
        $TokenTimeStampTTL = $parsed_json->{'expires_in'};
        // S'il reste moins de 10 secondes de vie à un Token, on le refresh
        $_SESSION['TokenMaxTimeStamp'] = (time() + $TokenTimeStampTTL) - 10;

        return $response;
    }

    function getProperties($ficProp){
        $data = file_get_contents($ficProp); 
        // décoder le flux JSON
        $obj = json_decode($data); 

        $_SESSION['client_id']      = $obj[0]->client_id;
        $_SESSION['client_secret']  = $obj[0]->client_secret;
        $_SESSION['$authorize_url'] = $obj[0]->authorize_url;
        $_SESSION['netatmo_user']   = $obj[0]->netatmo_user;
        $_SESSION['netatmo_pass']   = $obj[0]->netatmo_pass;

        return true;    
    }
?>