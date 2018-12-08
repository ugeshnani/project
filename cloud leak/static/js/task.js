var website = "http://127.0.0.1:6007/";

$(function () {
var user_role = check_session();
console.log("returned username is: "+user_role);
/*if(user_role == "user"){
$(".add").css("display", "none");
$(".table_div").css("display", "block");
}
else if(user_role =="admin"){
$(".add").css("display", "block");
$(".table_div").css("display", "block");
}*/

  $("#add_btn").on("click", function (e) {
    event.preventDefault();
    $(".table_div").css("display", "none");
    var name = $("#task_name").val();
    var date = $("#task_date").val();
    var status = $("#task_status").val();
    add(name, date, status);
  });

  $("#modify_btn").on("click", function (e) {
    event.preventDefault();
    $(".table_div").css("display", "none");
    var name = $("#task_name").val();
    var date = $("#task_date").val();
    var status = $("#task_status").val();
    modify(name, date, status);
  });

  $("#due_btn").on("click", function (e) {
    event.preventDefault();
    $(".table_div").css("display", "block");
    var date = $("#due_date").val();
    console.log(date);
    due(date);
  });

  $("#overdue_btn").on("click", function (e) {
    event.preventDefault();
    $(".table_div").css("display", "block");
    overdue();
  });

  $("#finished_btn").on("click", function (e) {
    event.preventDefault();
    $(".table_div").css("display", "block");
    finished();
  });

  $("#signout_btn").on("click", function (e) {
    event.preventDefault();
    signout();
  });
});

function check_session(){
    var ret = "";
    console.log("inside checksession function");
    $.ajax({
       async: false,
	type: 'POST',
        url: website+'check_session',
        success: function(data){
            if(data['pdf1'] == 'Success'){
		ret = data['pdf2']+"";
		console.log("in success printing ret: "+ret);
		console.log("in success printing data['pdf2']: "+data['pdf2']);
            }
        },
	error: function(e){
            console.log(e);
        },
        dataType: "json",
        contentType: "application/json; charset=utf-8"
    });
    console.log("printing return :"+ret);
    return ret+"";
}

function add(name, date, status) {
  var dataString = '{ "name":"' + name + '", "date": "' + date + '","status":"' + status + '"}';
  console.log(dataString);
  $.ajax({
    type: 'POST',
    url: website + "add",
    data: dataString,
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        console.log(data);
        console.log("inside success");
        console.log(data['pdf2']);
        //$("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-Success');
 $("#task_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-success');
      
}
      else if (data['pdf1'] == 'Failure') {
        console.log("inside Failure");
        //$("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');
$("#task_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');      
}
    },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}


function modify(name, date, status) {

  var dataString = '{ "name":"' + name + '", "date": "' + date + '","status":"' + status + '"}';
  $.ajax({
    type: 'POST',
    url: website + "modify",
    data: dataString,
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        console.log(data);
        console.log("inside success");
        console.log(data['pdf2']);
       // $("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-Success');
$("#task_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-success');      
}
      else if (data['pdf1'] == 'Failure') {
        console.log("inside Failure");
$("#task_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');        
//$("#add_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown alert-danger');
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
  console.log(dataString);
  $.ajax({
    type: 'POST',
    url: website + "due",
    data: dataString,
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        $(".table").css("display", "block");
        var s = $('#task_table').DataTable();
        s.clear().draw();
        for (var i = 0; i < data['pdf2'].length; i++) {
          s.row.add([
            data.pdf2[i][0],
            data.pdf2[i][1],
            data.pdf2[i][2]
          ]).draw(false);
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
        $(".table").css("display", "block");
        var s = $('#task_table').DataTable();
        s.clear().draw();
        for (var i = 0; i < data['pdf2'].length; i++) {
          s.row.add([
            data.pdf2[i][0],
            data.pdf2[i][1],
            data.pdf2[i][2]
          ]).draw(false);
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
        $(".table").css("display", "block");
        var s = $('#task_table').DataTable();
        s.clear().draw();
        for (var i = 0; i < data['pdf2'].length; i++) {
          s.row.add([
            data.pdf2[i][0],
            data.pdf2[i][1],
            data.pdf2[i][2]
          ]).draw(false);
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

function signout() {

  $.ajax({
    type: 'POST',
    url: website + "signout",
    success: function (data) {
      if (data['pdf1'] == 'Success') {
        window.location.replace(website);
	console.log("signout clicked");
      }
 },
    error: function (e) {
      console.log(e);
    },
    dataType: "json",
    contentType: "application/json; charset=utf-8"
  });
}


