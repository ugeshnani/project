
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
<!DOCTYPE html>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>

<title>File Upload</title>
</head>


<script
	src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/js/bootstrap-multiselect.js"></script>
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/css/bootstrap-multiselect.css">
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0s/css/font-awesome.min.css">
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/jquery.sumoselect/3.0.2/sumoselect.min.css">


<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.sumoselect/3.0.2/jquery.sumoselect.min.js"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
	<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
  <script>
  var files = [];
    $(document).ready(function () {
    	
        getFileNames();
        $("#uploadFile").on("click", function(e){
        	e.preventDefault();
        	 var folderName = $("#folderName").val();
       		uploadFile(folderName);
  });
    })
    function uploadFile(folderName){
        
        console.log("inside upoadFile function");
        console.log(files);
        var oMyForm = new FormData();
       
        oMyForm.append("folderName",folderName);
        console.log(oMyForm);
        for (var value of oMyForm.keys()) {
        	   console.log(value); 
        	}
        var inputs = $("#my_form input");
        $.each(inputs, function (obj, v) {
            var file = v.files[1];
            oMyForm.append("file", files);
        })
       $
          .ajax({dataType : 'json',
              url : "fileUpload",
              data : oMyForm,
              type : "POST",
              enctype: 'multipart/form-data',
              processData: false, 
              contentType:false,
              success : function(result) {
                  console.log("inside sucess");
              },
              error : function(result){
                  //...;
            	  console.log("inside error");
              }
          });
    
    }

function getFileNames(){
    
    console.log("inside getFileNAme function");
    $.ajax({
        type: 'POST',
        url: 'getFileName',
       
        success: function(data){
        	console.log("inside sucess");
            for(var i=0;i<data.length;i++){
                var val=data[i]["fileName"];
              $('#folderName').append($('<option>', { 
                  value: val,
                  text : val 
              }));
            };
        },
        error: function(e){
        	console.log("ïnside error");
            console.log(e);
        },
        dataType: "json",
        
    });
}


</script>

<style>
body {
	/* height: 100%; */
	margin: 0;
	background-size: 1366px 768px;
	background-repeat: no-repeat;
	background-color:#daf7f8;
	display: compact;
}
.form-inline .form-control{
	width:100%;
}
.form-inline label{padding-right:10px;}
.form-inline{padding-top:3px;padding-bottom:3px;}
.sumo_responseType {
	width: 270px;
}
div.a {
  font-size: 10px;
}
.select-all {
	height: 35px !important;
}

.btnOk {
	color: blue;
}

.btnCancel {
	color: red;
}

.request_div_width {
	width: 970px !important;
}

.header_color {
	background-color: cornflowerblue !important;
	border-color: #FAEBD7;
}

.header_back_color {
	background-color: lightseagreen !important;
}

.select_box_height {
	height: 30px;
}

.mid_position {
	margin-left: 5%;
}

.option_position {
	margin-left: 5%;
	margin-top: 1%;
}

.footer_position {
	bottom: -5%;
	position: fixed;
	width: 100%;
}

.required:after {
	content: " *";
	color: red;
}

.confirm_content {
	display: inline;
}

.dp_none {
	display: none;
}

.anchor_tag_height {
	margin-top: 6px;
}

.button_bold {
	font-weight: bold;
}

.button_bold_wo_color {
	font-weight: bold;
}

.menu_color {
	background-color: lightblue;
}
.navbar-default{
  background-color: #98AFC7;
 /*  border-color: #425766; */
}
.alert{
	padding: 10px !important;
}
.ui-datepicker-trigger{
	position: absolute;
    right: 20px;
    height: 20px;
    bottom: 5px;
}
.topnav-right {
  float: right;
}

/* Ugesh added */

.col-lg-6 {
    width: 100%;
}
</style>

<body>
	
    <div class ="container">
        <div class ="row">
            <div class="col-lg-12">
            <form id="my_form">
                <div class="row">
                
                    <div class="col-lg-3"  >
                    <label class="control-label" style="float:center;margin-top:50px" >File Names</label>	
                    </div>
                    <div class="col-lg-3">
                    <select  class="form-control input-sm"  id="folderName"  name="folderName"  style="float:center;margin-top:50px" id="fileName">
                        <option value="Choose" label="Choose">Choose</option>
                    </select>
                    </div>  
                </div>
                <div class="row">
                
                    <div class="col-lg-3"  >
                    <label class="control-label" style="float:center;margin-top:50px" >File Upload</label>	
                    </div>
                    <div class="col-lg-3">
                    <input  class="form-control input-sm" type="file" style="float:center;margin-top:50px" name="file" id="fileName"  multiple/><br/><br/>
                     
                    </div>  
                                        <div class="col-lg-3">
                    <input type="submit" id="uploadFile" value="Upload" style="float:center;margin-top:50px"/>
                </div>
                </div>
                </form>
        </div>
      </div>
    </div>
	

	
	
</body>
</html>