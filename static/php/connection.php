<?php
$servername="localhost";
$dbusername="root";
$dbpassword="";
$dbname="motorinn";

$conn= new mysqli($servername,$dbusername,$dbpassword,$dbname);
if($conn->connect_error)
{
	die("Connection failed: ". $conn->connect_error);
}
?>