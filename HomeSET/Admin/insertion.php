<?php
session_start();

// on contrôle que les données minimales sont bien saisies
if(isset($_POST['username']) && isset($_POST['password']))
{
    // récupération des données du fichier de properties
    $data = file_get_contents('../properties.json'); 
    // décoder le flux JSON
    $obj = json_decode($data); 

    // connexion à la base de données
    $db_username = $obj[0]->username;
    $db_password = $obj[0]->db_password;
    $db_name     = $obj[0]->db_name;
    $db_host     = $obj[0]->db_host;

    //fclose($data); // on ferme le fichier pour rester propre

    $db = mysqli_connect($db_host, $db_username, $db_password,$db_name)
            or die('could not connect to database');

    // on vérifie que le username n'est pas déjà attribué à quelqu'un
    $req_checkuser = "SELECT COUNT(*) AS nbr FROM users WHERE name_user = '".$_POST['username']."'";
    $exec_req_checkuser = mysqli_query($db,$req_checkuser);
    $reponse_checkuser = mysqli_fetch_array($exec_req_checkuser);
    
    if ($reponse_checkuser['nbr'] != 0) {
        header('Location: ../login.php?erreur=3'); // utilisateur ou mot de passe vide
    } else {
        // L'utilisateur n'existe pas encore
        // on applique les deux fonctions mysqli_real_escape_string et htmlspecialchars
        // pour éliminer toute attaque de type injection SQL et XSS
        $username = mysqli_real_escape_string($db,htmlspecialchars($_POST['username'])); 
        $password = mysqli_real_escape_string($db,htmlspecialchars($_POST['password']));

        if($username !== "" && $password !== "")
        {
            $password_hash = password_hash(strval($password), PASSWORD_DEFAULT);    // on hash le mot de passe avant enregistrement
            $requete = "INSERT INTO users (`name_user`, `password_user`) VALUES ('".$username."', '".$password_hash."' )";
            $exec_requete = mysqli_query($db,$requete);
            $reponse      = mysqli_fetch_array($exec_requete);
            $_SESSION['username'] = $username;
            header('Location: confirmation.php');
        }
        else
        {
            header('Location: ../login.php?erreur=2'); // utilisateur ou mot de passe vide
        }
    }
}
else
{
    header('Location: login.php');
}
mysqli_close($db); // fermer la connexion
?>