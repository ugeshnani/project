<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->


<html>

  <head>
  <script>
    $(document).ready(function () {
        getFileNames();
  });

function getFileName(){
    
    console.log("inside getFileNAme function");
    $.ajax({
        type: 'POST',
        url: 'getFileName',
       
        success: function(data){
            for(var i=0;i<data.length;i++){
                var value=data[i]["fileName"]
                $("#fileNames").append('$<option>',{value:value}.text(value));
            }
        },
        error: function(e){
            console.log(e);
        },
        dataType: "json",
        contentType: "application/json; charset=utf-8"
    });
}


function saveESS() {
	console.log("print");
// 	document.addESSForm.action = "saveESS.do";
	
		$.ajax({
			type: "POST",
		    url: './saveESS.do',
		    success: function(result){
		    	alert();
		    // when successfully return from your java  
		    }, error: function(){
		       // when got error
		    }
		}); 
		 

	document.addESSForm.submit();
}
</script>
  <style>
  body#LoginForm{ background-image:url("https://hdwallsource.com/img/2014/9/blur-26347-27038-hd-wallpapers.jpg"); background-repeat:no-repeat; background-position:center; background-size:cover; padding:10px;}

.form-heading { color:#fff; font-size:23px;}
.panel h2{ color:#444444; font-size:18px; margin:0 0 8px 0;}
.panel p { color:#777777; font-size:14px; margin-bottom:30px; line-height:24px;}
.login-form .form-control {
  background: #f7f7f7 none repeat scroll 0 0;
  border: 1px solid #d4d4d4;
  border-radius: 4px;
  font-size: 14px;
  height: 50px;
  line-height: 50px;
}
.main-div {
  background: #ffffff none repeat scroll 0 0;
  border-radius: 2px;
  margin: 10px auto 30px;
  max-width: 38%;
  padding: 50px 70px 70px 71px;
}

.login-form .form-group {
  margin-bottom:10px;
}
.login-form{ text-align:center;}
.forgot a {
  color: #777777;
  font-size: 14px;
  text-decoration: underline;
}
.login-form  .btn.btn-primary {
  background: #f0ad4e none repeat scroll 0 0;
  border-color: #f0ad4e;
  color: #ffffff;
  font-size: 14px;
  width: 100%;
  height: 50px;
  line-height: 50px;
  padding: 0;
}
.forgot {
  text-align: left; margin-bottom:30px;
}
.botto-text {
  color: #ffffff;
  font-size: 14px;
  margin: auto;
}
.login-form .btn.btn-primary.reset {
  background: #ff9900 none repeat scroll 0 0;
}
.back { text-align: left; margin-top:10px;}
.back a {color: #444444; font-size: 13px;text-decoration: none;}
  
  
  </style>
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
	<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!------ Include the above in your HEAD tag ---------->
  </head>
<body id="LoginForm">
<div class="container">
<h1 class="form-heading">login Form</h1>
<div class="login-form">
<div class="main-div">
    <div class="panel">
   <h2>Admin Login</h2>
   <p>Please enter your email and password</p>
   </div>
    <form action="/file" method="post">
    
    <div class="form-group">
            <input type="text" name="employeeid" class="form-control" id="inputEmail" placeholder="Employee Id">
        </div>

        <div class="form-group">
            <input type="email" name="username" class="form-control" id="inputEmail" placeholder="Email Address">
        </div>

       
        <div class="form-group">
            <input type="address" name="address" class="form-control"  placeholder="address">
        </div>
        <div class="form-group">
            <input type="phonenumber" name="phonenumber" class="form-control"  placeholder="phonenumber">
        </div>
        <div class="forgot">
        <a href="/file" method="Get">Forgot password?</a>
        <a href="login.jsp">Get Details</a>
		</div>
        <button type="submit" class="btn btn-primary">Add Details</button>

    </form>
    </div>
<p class="botto-text"> Designed by Ramya Maddi</p>
</div></div></div>


</body>
</html>