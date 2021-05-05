function login(id) {
    loginId = id
    if (!id) {
        loginId = document.getElementById("loginId").value;
    }
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        console.log(this.readyState)
        if (this.readyState == 4 && this.status == 200) {
            document.cookie = "employee=" + this.responseText
            if (!id) window.location.href = "index.html"
        } else if (this.readyState == 4) {
            document.getElementById("message").innerHTML = "Unable to login with that Id"
        }
    }

    url = "http://127.0.0.1:5000/employees/"

    xhr.open("POST", url, true)

    let login = {
        loginId: loginId
    }

    //May not be required - needs further testing
    //Add Headers to our requests
    xhr.setRequestHeader('Content-Type', 'application/json')

    xhr.send(JSON.stringify(login));

}
function betterDate(intDate) {
    date = new Date(intDate)
    dd = date.getDate()
    mm = date.getMonth()
    yyyy = date.getFullYear()
    if (parseInt(dd) < 10){
        dd = "0" + dd
    }
    if (parseInt(mm) < 10){
        mm = "0" + mm
    }
    return yyyy + "-" + mm + "-" + dd
    
}