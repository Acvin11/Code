 <?php  
 //index.php  
 $connect = mysqli_connect('localhost', 'root', '', 'testing');  
 $query = "SELECT * FROM tbl_employee ORDER BY rank asc";  
 $result = mysqli_query($connect, $query);  
 ?>  
 <!DOCTYPE html>  
 <html>  
      <head>  
           <title>Webslesson Tutorial | Ajax Jquery Column Sort with PHP & MySql</title>  
           <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>  
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>  
	   <link rel="stylesheet" href="dp.css" type="text/css">
		<link rel="stylesheet" href="ex.css" type="text/css"> 
	<style>  body{
				margin-left:5px;
				margin-right:5px;
			
			}
		header#header_shop1
			{
				background-image: url("head.jpg");
				margin-right:5px;
				margin-left:-9px;
	
		  }	
	</style>

      </head>  
       <body>
      <div class="main">
<header id="header_shop1">	
<table width=100%>
	
	<tr>
		<td>
			<img src="BMC_logo.png" height=150px width=150px></img>
		<th>	
			<Center>
			<h1> 
				<b>
				<p >
					<font color="white" size="30"style="font-family:'Matura MT Script Capitals'">BMC : Art & Craft Portal
					</font>
				</p>
				</b>
			</h1>
			</center>
		<td align="right">
			<img src="ashoka_pillar.png" height=150px width=100px align="right"></img>
	</tr>
</table>
</header>
</div>

<div class="menu">
     <ul>
            <li><a href="acvin_copy.html" >Home</a></li>
            <li><a href="event.html" class="active">Event</a></li>
           <li><a href="gallery.html">Gallery</a></li>
             <li><a href="about us.html">About us</a></li>
            <li><a href="contact.html" >Contact us</a></li>
     </ul>	
</div>	

	

           <br >            
           <div class="container" style="width:80%;" align="center">  
                <h3 class="text-center">Overall Competition Rankings</h3><br />  
                <div class="table-responsive" id="employee_table">  
                     <table class="table table-bordered">  
                          <tr>  
				<th><a class="column_sort" id="rank" data-order="desc" href="#">Rank</a></th>  
                               <th><a class="column_sort" id="points" data-order="desc" href="#">Total Points</a></th>  
                               <th><a class="column_sort" id="name" data-order="desc" href="#">School Name</a></th>  
                               <th><a class="column_sort" id="compart" data-order="desc" href="#">Competition Participated In</a></th> 
			       <th><a class="column_sort" id="winners" data-order="desc" href="#">Winners</a></th>  
			     
                          </tr> 
			  <?php  
                          while($row = mysqli_fetch_array($result))  
                          {  
                          ?>  
                          <tr>
			       <td><?php echo $row["rank"]; ?></td>   
                               <td><?php echo $row["points"]; ?></td>  
                               <td><?php echo $row["name"]; ?></td>    
	                       	<td><?php echo $row["compart"]; ?></td> 
				<td><?php echo $row["winners"]; ?></td>          
                          </tr>
			  
                          <?php  
                          }  
                          ?>  
                     </table>  
                </div>  
           </div>  
           <br >  
      
<footer>
      <table width="100%">
	<tr>
		<td><font size="4" color="white">Designed By-<b>APPdesigners</font>
		<td align="right">	<a href="#" class="fa fa-facebook"></a>
				        <a href="#" class="fa fa-whatsapp"></a>	
				       <a href="#" class="fa fa-instagram"></a>
	</tr>
         </table>
</footer>
</body>	
</html>  
 <script>  
 $(document).ready(function(){  
      $(document).on('click', '.column_sort', function(){  
           var column_name = $(this).attr("id");  
           var order = $(this).data("order");  
           var arrow = '';  
           //glyphicon glyphicon-arrow-up  
           //glyphicon glyphicon-arrow-down  
           if(order == 'desc')  
           {  
                arrow = '&nbsp;<span class="glyphicon glyphicon-arrow-down"></span>';  
           }  
           else  
           {  
                arrow = '&nbsp;<span class="glyphicon glyphicon-arrow-up"></span>';  
           }  
           $.ajax({  
                url:"sort.php",  
                method:"POST",  
                data:{column_name:column_name, order:order},  
                success:function(data)  
                {  
                     $('#employee_table').html(data);  
                     $('#'+column_name+'').append(arrow);  
                }  
           })  
      });  
 });  
 </script>  
