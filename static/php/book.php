<?php
$query = "SELECT * FROM `ultradeluxe` where available=1;";
include('connection.php');
 $search_result  = mysqli_query($conn, $query);
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Motor Inn</title>
<link href='..\css\book.css' rel='stylesheet'>
 <script src="..\javascript\jquery.js"></script>
<script type="text/javascript">
    
    function master() 
         { 
            
            
               $(document).ready(function()
               {
                alert(document.getElementById('roomid').value);
                  var name=document.getElementById('roomid').value;
                  $.ajax({
                     type:"POST",
                     url:'http://localhost/motorinn/php/boo.php',
                     data:{'name':name},
                     cache:false,
                     success:function(html)
                     {
                        $("#clk").html(html);   
                     }
                  }); 
               });
            }
</script>
</head>
<body>

<nav>
<a href=""><b>Home</b></a>
<a href=""><b>Book Room</b></a>
<a href=""><b>Hire Vehicle</b></a>
<a href=""><b>Order Food</b></a>
<a href=""><b>Entertainment</b></a>
</nav>
<div >
<a href="">Ultra Deluxe</a>
<a href="">Deluxe</a>
<a href="">Non Deluxe</a>
</div>
<form action="" method="POST">
<input type="text" placeholder="Enter RoomNo">
<button type="submit">Book
	</button>
</form>
<center></br></br>
    <table border="1" width="90%">
    <tr>
        <th>Room No</th>
         <th>Cost</th>
         <th>Description</th>
    </tr>
<?php while($row = mysqli_fetch_array($search_result)):?>
	
<tr onclick="window.location=master()">
    <td id="roomno"><center><?php echo $row['roomno'];?></center></td>
    <td><center><?php echo $row['cost'];?></center></td>
     <td><center><?php echo $row['description'];?></center></td>
</tr>
    <?php endwhile;mysqli_close($conn);?>
    </table></center>
</body>
</html>