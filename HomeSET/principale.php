<html>

<head>
    <meta charset="utf-8">
    <!-- importer le fichier de style -->
    <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
</head>

<body style='background:#fff;'>
    <header>
    </header>

    <main>
        <div id="content">

            <!-- tester si l'utilisateur est connecté -->
            <?php
                    session_start();
                    if(isset($_GET['deconnexion']))
                    { 
                        if($_GET['deconnexion']==true)
                        {  
                            session_unset();
                            header("location:login.php");
                        }
                    }
                    else if($_SESSION['username'] !== ""){
                        $user = $_SESSION['username'];
                        // afficher un message
                        echo("<br>Bonjour $user, vous êtes connectés<hr>");
                        
                        // -----------------------------------------------------------
                        // récupération du token auprès de netatmo
                        //	client (application) credentials - located at apim.byu.edu
                        // récupération des données du fichier de properties
                        $data = file_get_contents('properties.json'); 
                        // décoder le flux JSON
                        $obj = json_decode($data); 

                        $client_id      = $obj[0]->client_id;
                        $client_secret  = $obj[0]->client_secret;
                        $authorize_url  = $obj[0]->authorize_url;
                        $netatmo_user   = $obj[0]->netatmo_user;
                        $netatmo_pass   = $obj[0]->netatmo_pass;

                        function httpPost($url, $data){
                            $curl = curl_init($url);
                            curl_setopt($curl, CURLOPT_POST, true);
                            curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
                            curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                            $response = curl_exec($curl);
                            return $response;
                        }

                        $data = [
                            'grant_type' => 'password',
                            'client_id' => $client_id,
                            'client_secret' => $client_secret,
                            'username' => $netatmo_user,
                            'password' => $netatmo_pass,
                            'scope' => 'read_station'
                        ];

                        $res = httpPost($authorize_url, $data);

                        //echo("<hr> Passé");

                        $parsed_json = json_decode($res);
                        //$TokTok = $parsed_json->{'access_token'}->{'features'}->{'date'};
                        $TokTok = $parsed_json->{'access_token'};
                        //echo("<hr>");
                        //echo($TokTok);
                        // ----------------------------------------------------------- 
                        $url = "https://api.netatmo.com/api/getmeasure";

                        $curl = curl_init($url);
                        curl_setopt($curl, CURLOPT_URL, $url);
                        curl_setopt($curl, CURLOPT_POST, true);
                        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

                        $headers = array(
                        "Accept: application/json",
                        "Authorization: Bearer {$TokTok}",
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
                        echo("<hr>");

                        $bouhbou = $resp_json1['time_exec'];
                       
                        echo("TEST : {$bouhbou}");      
                        echo("<hr>");
                        curl_close($curl);
                        var_dump($resp);
                        // ----------------------------------------------------------- 
                    }
                ?>
        </div>
    </main>

    <footer>
        <a href='principale.php?deconnexion=true'><span>Déconnexion</span></a>
    </footer>
</body>

</html>