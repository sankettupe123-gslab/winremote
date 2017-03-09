function validate() {
    var ip = document.getElementById("ip").value;
    if (ip == "") {
        alert("Please Enter IP Address");
        return false;
    }

    var user = document.getElementById("user").value;
    if (user == "") {
        alert("Please Enter User Name");
        return false;
     }

    var pass = document.getElementById("pass").value;
    if (pass == "") {
        alert("Please Enter Password");
        return false;
          }

    var cmd = document.getElementById("cmd").value;
    if (cmd == "") {
        alert("Please Enter Command");
        return false;
       }
    showbar();
}

    function showbar(){
var x = document.getElementById('bar');
document.getElementById('bar').style.display = 'block';
    }
