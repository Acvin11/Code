<?php
session_start();
if(isset($_SESSION["uid"])){
	header("location:profile.php");
}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>BMC Store</title>
		
		<link rel="stylesheet" href="css/bootstrap.min.css"/>
		<link rel="stylesheet" href="dp.css" type="text/css">
		<link rel="stylesheet" href="ex.css" type="text/css">
		<script src="js/jquery2.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="main.js"></script>
		<link rel="stylesheet" type="text/css" href="style.css">
		<style>
		.navbar .nav > li > a {
						line-height: 1px;	
					}			
		   body{
				margin-left:5px;
				margin-right:5px;
			
			}
		header#header_shop1
			{
				background-image: url("head.jpg");
				margin-right:6px;
				margin-left:-3px;
	
		  }	
		header#header_shop2
			{
		
				background-color:  #fff3e6;
				margin-left:95px;
				margin-right:65px;
			
			}
		header#header_shop3
			{
		
				background-image: url("5.png");
				margin-left:5px;
				margin-right:5px;
			
			}

		ul#acvin{
				margin-right:6%;
			}
	div#panel-heading{
				font-size:20px;
				background-color:#337ab7;
				color:white;
				
			}
		
	div.get_product{
				font-size:17px;
				background-color:black;
			}
		
	h1#Shopping{
				font-family:Matura MT Script Capitals;
				color:#337ab7;
		   }
	div#menu{
			margin-right:5px;
				
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
				<p style="font-family:'Old English Text MT'">
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
  <div class="menu" id="menu">
     <ul>
            <li><a href="acvin_copy.html" class="active">Home</a></li>
            <li><a href="event.html">Event</a></li>
           <li><a href="gallery.html">Gallery</a></li>
             <li><a href="about us.html">About us</a></li>
            <li><a href="contact.html" >Contact us</a></li>
     </ul>	
</div>
</div>	
<header id="header_shop3">
<center>
 <h1 id="Shopping">Shopping Cart</h1>
</center>

<header id="header_shop2">
   <div class="collapse navbar-collapse" id="collapse">
			<ul class="nav navbar-nav navbar-right" id="acvin">
				<li ><a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-shopping-cart"></span>Cart<span class="badge">0</span></a>
					<div class="dropdown-menu" style="width:400px;">
						<div class="panel panel-success">
							<div class="panel-heading">
								<div class="row">
									<div class="col-md-3">Sl.No</div>
									<div class="col-md-3">Product Image</div>
									<div class="col-md-3">Product Name</div>
									<div class="col-md-3">Price in Rs.</div>
								</div>
							</div>
							<div class="panel-body">
								<div id="cart_product">
								<!--<div class="row">
									<div class="col-md-3">Sl.No</div>
									<div class="col-md-3">Product Image</div>
									<div class="col-md-3">Product Name</div>
									<div class="col-md-3">Price in Rs.</div>
								</div>-->
								</div>
							</div>
							<div class="panel-footer"></div>
						</div>
					</div>
				</li>
				<li><a href="http://localhost/KhanStore/login_form.php" class="btn btn-Info" ><span class="glyphicon glyphicon-pencil"></span>Description</a>
				</li>
				<li><a href="http://localhost/KhanStore/login_form.php" class="btn btn-Info" ><span class="glyphicon glyphicon-user"></span>SignIn</a>
				</li>
			</ul>
		
	</div>
			
		<div class="row">
			<div class="col-md-1"></div>
			<div class="col-md-2 col-xs-12">
				<div id="get_category" >
				</div>
				<div id="get_brand">
				</div>
				
			</div>
			<div class="col-md-8 col-xs-12" >
				<div class="row">
					<div class="col-md-12 col-xs-12" id="product_msg">
					</div>
				</div>
				<div class="panel panel-info">
					<div class="panel-heading" id="panel-heading">Products</div>
					<div class="panel-body">
						<div id="get_product" class="get_product">
							<!--Here we get product jquery Ajax Request-->
						</div>
						</div>
					<div class="panel-footer">&copy; BMC</div>
				</div>
			</div>
			<div class="col-md-1"></div>
		</div>
	
<br>
</header>
<br>
</header>
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
















































