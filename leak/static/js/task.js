var website = "http://10.154.194.146:6007/";

$(function () {


	console.log("inside task.js")

  $("#add_btn").on("click", function (e) {
    event.preventDefault();
    $(this).attr("disabled", true).val("Loading..");
    var name = $("#task_name").val();
    var date = $("#task_date").val();
    var status = $("#task_status").val();
    add(name,date,status);
  });
   $("#modify_btn").on("click", function (e) {
    event.preventDefault();
    $(this).attr("disabled", true).val("Loading..");
    var name = $("#task_name").val();
    var date = $("#task_date").val();
    var status = $("#task_status").val();
    modify(name,date,status);
  });
    $("#due_btn").on("click", function (e) {
    event.preventDefault();
    $(this).attr("disabled", true).val("Loading.."); 
    var date = $("#task_due_date").val();
    due(date);
  });
    $("#overdue_btn").on("click", function (e) {
    event.preventDefault();
    $(this).attr("disabled", true).val("Loading.."); 
    overdue();
  });
    $("#finished_btn").on("click", function (e) {
    event.preventDefault();
    $(this).attr("disabled", true).val("Loading.."); 
    finished();
  });
});


function add(name,date,status) {
  var dataString = '{ "name":"' + name + '", "date": "' + date + '","status":"'+status+'"}';
	console.log(dataString);	  
  $.ajax({
    type: 'POST',
    url: website + "add",
    data: dataString,
    success: function (data) {
     if(data['pdf1'] == 'Success'){
		console.log(data);
                console.log("inside success");
                console.log(data['pdf2']);
                $("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-Success');
            }
            else if(data['pdf1'] == 'Failure'){
                console.log("inside Failure");
                $("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');
            }
    },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}


function modify(name,date,status) {

  var dataString = '{ "name":"' + name + '", "date": "' + date + '","status":"'+status+'"}';
  $.ajax({
    type: 'POST',
    url: website + "modify",
    data: dataString,
    success: function (data) {
      if(data['pdf1'] == 'Success'){
                console.log(data);
                console.log("inside success");
                console.log(data['pdf2']);
                $("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-Success');
            }
            else if(data['pdf1'] == 'Failure'){
                console.log("inside Failure");
                $("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');
            }

     },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}



function due(date) {
  
  var dataString = '{ "date": "' + date + '"}';
  $.ajax({
    type: 'POST',
    url: website + "due",
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        $(".add").css("display":"None");
	$(".table").css("display":"block")
        $("#checkmarx-avg-vul-per-scan").html(data['pdf3']);
        $("#checkmarx-total-app-scanned").html(data['pdf4']);
        var i;
        $("#checkmarx-app-list-select").html("");
        console.log(data['pdf5']);
        for (i = 0; i < data['pdf5'].length; i++) {
          $("#checkmarx-app-list-select").append("<option value=" + data['pdf5'][i] + ">" + data['pdf5'][i] + "</option>");
        }
      }
    },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}


function overdue() {
  $.ajax({
    type: 'POST',
    url: website + "overdue",
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        $("#checkmarx-avg-scan-request-per-week").html(data['pdf2']);
        $("#checkmarx-avg-vul-per-scan").html(data['pdf3']);
        $("#checkmarx-total-app-scanned").html(data['pdf4']);
        var i;
        $("#checkmarx-app-list-select").html("");
        console.log(data['pdf5']);
        for (i = 0; i < data['pdf5'].length; i++) {
          $("#checkmarx-app-list-select").append("<option value=" + data['pdf5'][i] + ">" + data['pdf5'][i] + "</option>");
        }
      }
    },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}

function finished() {
 
  $.ajax({
    type: 'POST',
    url: website + "finished",
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        $("#checkmarx-avg-scan-request-per-week").html(data['pdf2']);
        $("#checkmarx-avg-vul-per-scan").html(data['pdf3']);
        $("#checkmarx-total-app-scanned").html(data['pdf4']);
        var i;
        $("#checkmarx-app-list-select").html("");
        console.log(data['pdf5']);
        for (i = 0; i < data['pdf5'].length; i++) {
          $("#checkmarx-app-list-select").append("<option value=" + data['pdf5'][i] + ">" + data['pdf5'][i] + "</option>");
        }
      }
    },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}


