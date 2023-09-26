<?php

$hostname = "192.168.1.212";
$username = "root";
$password = "pencil1!";
$db = "Scores";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

if(isset($_POST['submit'])) {
  echo "line 15";
  $Team_Name=$_POST['Team_Name'];
  $Mobility=$_POST['Mobility'];
  $Balance=$_POST['Balance'];
  $AmountOfAuto=$_POST['AmountOfAuto'];
  $ConeTop=$_POST['ConeTop'];
  $ConeMiddle=$_POST['ConeMiddle'];
  $ConeBottom=$_POST['ConeBottom'];
  $CubeTop=$_POST['CubeTop'];
  $CubeMiddle=$_POST['CubeMiddle'];
  $CubeBottom=$_POST['CubeBottom'];
  echo "line 26";
  $query = "INSERT INTO ScoreTable (Team_Name, Mobility, Balance, AmountOfAuto, ConeTop, ConeMiddle, ConeBottom, CubeTop, CubeMiddle, CubeBottom)
  VALUES ('$Team_Name', '$Mobility', '$Balance', '$AmountOfAuto', '$ConeTop', '$ConeMiddle', '$ConeBottom', '$CubeTop', '$CubeMiddle', '$CubeBottom')";
  drecho "line 29";
    if (!mysqli_query($dbconnect, $query)) {
        die('An error occurred. Your scouting data has not been submitted.');
    } else {
      echo "Thanks for your help.";
    }

}
?>
