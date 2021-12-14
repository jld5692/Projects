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

                    include 'OAuth.php';    // Fonction et éléments nécessaire à l'authentification
                    
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
                        $resPro = getProperties('properties.json');

                        if (isset($_SESSION['CurrentToken']) and ($_SESSION['CurrentToken'] !== "")) {
                            if ($_SESSION['TokenMaxTimeStamp'] < time()) {
                                // echo ("<BR><B>On a besoin de rafraichir le Token </B><BR>");
                                $dataRefresh = [
                                    'grant_type'    => 'refresh_token',
                                    'refresh_token' => $_SESSION['Refresh_token'],
                                    'client_id'     => $_SESSION['client_id'],
                                    'client_secret' => $_SESSION['client_secret']
                                ];
    
                                $resRefresh = httpPost($_SESSION['$authorize_url'], $dataRefresh);

                                // echo("<h1>SESSION TOKEN</h1>");
                                // echo ($_SESSION['CurrentToken']);
                                // echo("<BR><HR>");

                            } else {
                                // Le Token est toujours valide --> on n'a rien à faire
                                // echo ("<BR><B>Token valide - rien à faire </B><BR>");
                                // echo ($_SESSION['CurrentToken']);
                                // echo ("<HR>");
                                // echo ($_SESSION['TokenMaxTimeStamp']);
                            }
                        } else {
                            // echo ("<BR><B>Nouvelle demande - init du Token </B><BR>");
                            $dataInit = [
                                'grant_type'    => 'password',
                                'client_id'     => $_SESSION['client_id'],
                                'client_secret' => $_SESSION['client_secret'],
                                'username'      => $_SESSION['netatmo_user'],
                                'password'      => $_SESSION['netatmo_pass'],
                                'scope'         => 'read_station'
                            ];

                            $resInit = httpPost($_SESSION['$authorize_url'], $dataInit);
                           
                            // echo("<h1>SESSION TOKEN</h1>");
                            // echo ($_SESSION['CurrentToken']);
                            // echo("<BR><HR>");
                        }
                        // ----------------------------------------------------------- 

                        // ----------------------------------------------------------- 
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