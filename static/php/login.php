<?php 
    session_start();
    if ((isset($_SESSION['Username']) && $_SESSION['Username'] != '')) 
    {	
        header("Location:home.php");
    }
    include('connection.php');
    $msg = "";
    if ($_SERVER['REQUEST_METHOD'] == 'POST') 
    {
        $name = $_POST["userid"];
        $password = md5($_POST["password"]);
	       if ($name == '' || $password == '') 
           {
                $msg = "You must enter all fields";
            }
            else
            {
                $sql = "SELECT * FROM users WHERE userid = '$_POST[userid]' AND password = '$_POST[password]'";
                $query = mysqli_query($conn,$sql);
                if ($query === false) 
                {
                    echo "Could not successfully run query ($sql) from DB: " . mysqli_error($conn);
                    exit;
                }
		      if (mysqli_num_rows($query) > 0) 
                {
                    $_SESSION['Username'] = $_POST['userid'];
                    header('Location: home.php');
                    exit;
                }
                $msg=  "Username and password do not match";
            }
    }
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href='..\css\login.css' rel='stylesheet' >
</head>
<body>
<div id="im"></div>
<po></po>

<div id="pos"></div>
<img src="../images/user.png" id="pic")>

<form action="..\php\login.php" method="POST">
<input id="pos1" type="text" placeholder="Enter id" name="userid">
<input id="pos2" type="password" placeholder="Enter password" name="password">
<a href=""><b>Forgot Passowrd</b></a>
<div style="color:red;">
    <p>
                <?php echo $msg; ?>
                    
    </p>
</div>
<div id="poss" ><button type="submit">Login</button></div>

</form>
</iframe>
</body>
</html>


</body>
</html>
