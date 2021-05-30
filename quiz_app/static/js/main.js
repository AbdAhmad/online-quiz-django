window.load = initAll();
var saveAnsButton;
function initAll(){
    alert('alert')
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick = saveAns();
}

function saveAns(){
    var ans = $('input:radio[name=name]:checked').val();
    var req = new XMLHttpRequest();
    var url = '/save_ans?ans=' + ans;
    alert(ans)
    req.open('GET', url, true);
    req.send();
}


function signupPasswordOneVisibilityToggle() {
    let passwordOne = document.getElementById("passwordOne");
        if (passwordOne.type === "password") {
            passwordOne.type = "text";
        } else {
            passwordOne.type = "password";
        }
    }

function signupPasswordTwoVisibilityToggle() {
    let passwordTwo = document.getElementById("passwordTwo");
    if (passwordTwo.type === "password") {
        passwordTwo.type = "text";
    } else {
        passwordTwo.type = "password";
    }
}

function loginPasswordVisibilityToggle() {
    let myInput = document.getElementById("myInput");
        if (myInput.type === "password") {
            myInput.type = "text";
        } else {
            myInput.type = "password";
        }
}

function setTimer(){
    var message_ele = document.getElementById("message_container");
    setTimeout(function(){ 
    message_ele.style.display = "none"; 
    }, 3000);
}
