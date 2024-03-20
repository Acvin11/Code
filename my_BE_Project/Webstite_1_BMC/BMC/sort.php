<?php  
 //sort.php  
 $connect = mysqli_connect("localhost", "root", "", "testing");  
 $output = '';  
 $order = $_POST["order"];  
 if($order == 'desc')  
 {  
      $order = 'asc';  
 }  
 else  
 {  
      $order = 'desc';  
 }  
 $query = "SELECT * FROM tbl_employee ORDER BY ".$_POST["column_name"]." ".$_POST["order"]."";  
 $result = mysqli_query($connect, $query);  
 $output .= '  
 	<table class="table table-bordered">  
 	     <tr> 
	          <th><a class="column_sort" id="rank" data-order="'.$order.'" href="#">Rank</a></th>   
        	   <th><a class="column_sort" id="points" data-order="'.$order.'" href="#">Total Points</a></th>  
          	   <th><a class="column_sort" id="name" data-order="'.$order.'" href="#">School Name</a></th>  
		    <th><a class="column_sort" id="compart" data-order="'.$order.'" href="#">Competition Participated In</a></th>    
           	   <th><a class="column_sort" id="winners" data-order="'.$order.'" href="#">Winners</a></th>  
           	
      	     </tr>  
 		';  
 while($row = mysqli_fetch_array($result))  
 {      $output .= '  
      <tr>  
	 
           <td>' . $row["rank"] . '</td>  
           <td>' . $row["points"] . '</td>  
           <td>' . $row["name"] . '</td>  
           <td>' . $row["compart"] . '</td>  
           <td>' . $row["winners"] . '</td>  
      </tr>  
      ';  
 }
 echo $output;  
 ?>  