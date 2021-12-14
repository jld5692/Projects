<?php
session_start();

if(isset($_POST['username']) && isset($_POST['password']))
{
   // récupération des données du fichier de properties
   $data = file_get_contents('properties.json'); 
   // décoder le flux JSON
   $obj = json_decode($data); 

      // connexion à la base de données
   $db_username = $obj[0]->username;
   $db_password = $obj[0]->db_password;
   $db_name     = $obj[0]->db_name;
   $db_host     = $obj[0]->db_host;

   echo("<h1>IN</h1>");
   echo ("<HR>");
   
   //fclose($data); // on ferme le fichier pour rester propre

   $db = mysqli_connect($db_host, $db_username, $db_password,$db_name)
         or die('could not connect to database');
    
   // on applique les deux fonctions mysqli_real_escape_string et htmlspecialchars
   // pour éliminer toute attaque de type injection SQL et XSS
   $username = mysqli_real_escape_string($db,htmlspecialchars($_POST['username'])); 
   $password = mysqli_real_escape_string($db,htmlspecialchars($_POST['password']));

   echo ($username);
   echo ("<HR>");

   if($username !== "" && $password !== "")
   {
      $requete = "SELECT password_user FROM users where name_user = '".$username."' ";
      $exec_requete = mysqli_query($db,$requete);
      $reponse      = mysqli_fetch_array($exec_requete);
      $pass = $reponse['password_user'];
      
      if(password_verify($password, $pass))
      {
         $_SESSION['username'] = $username;
         header('Location: accueil.php');
      }
      else
      {
         header('Location: login.php?erreur=1'); // utilisateur ou mot de passe incorrect
      }
   }
   else
   {
      header('Location: login.php?erreur=2'); // utilisateur ou mot de passe vide
   }
}
else
{
   header('Location: login.php');
}
mysqli_close($db); // fermer la connexion
?>