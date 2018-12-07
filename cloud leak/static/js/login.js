var website = 'http://10.154.194.146:6007/'
$(document).ready(function () {
    $("#login_submit").on("click", function(e){
        e.preventDefault();
        var user_id= $("#userid").val();
        var password= $("#password").val();
        login(user_id, password);
    });
});

function login(user_id, password){
    var dataString = '{"username":"'+user_id+'", "password":"'+password+'"}';
    console.log(dataString);
    $.ajax({
        type: 'POST',
        url: website+'login',
        data: dataString,
        success: function(data){
            if(data['pdf1'] == 'Success'){
                console.log("inside success");
                console.log(data['pdf2']);
                window.location.replace(website+"static/task.html");
            }
            else if(data['pdf1'] == 'Failure'){
                console.log("inside Failure");
                $("#login_alert").html(data['pdf2']).css("display", "block").addClass('animated fadeInDown');
            }
        },
        error: function(e){
            console.log(e);
        },
        dataType: "json",
        contentType: "application/json; charset=utf-8"
    });
}

