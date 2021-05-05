function login(id) {
    loginId = id
    if (!id) {
        loginId = document.getElementById("loginId").value;
    }
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.cookie = "employee=" + this.responseText
            if (!id) window.location.href = "index.html"
        } else if (this.readyState == 4) {
            document.getElementById("message").innerHTML = "Unable to login with that Id"
        }
    }

    url = "http://127.0.0.1:5000/employees/"

    xhr.open("POST", url, false)

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
    dd = date.getUTCDate()
    mm = date.getUTCMonth() + 1
    yyyy = date.getUTCFullYear()
    if (parseInt(dd) < 10) {
        dd = "0" + dd
    }
    if (parseInt(mm) < 10) {
        mm = "0" + mm
    }
    return yyyy + "-" + mm + "-" + dd

}
function patchRequest(id, reimbursement, statusId, amount) {

    reimbursement = employee.reimbursements.find(x => x.id == id)
    statusId = parseInt(reimbursement.status.id) + 1
    message = document.getElementById(`message${id}`).value
    amount = document.getElementById(`amount${id}`).value

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            login(employee.loginId)
            window.location.reload()
        } else if (this.readyState == 4) {
            console.log("Something is wrong")
        }
    }

    url = `http://127.0.0.1:5000/reimbursement/${id}`

    xhr.open("PATCH", url, true)

    let patch = {
        statusId: statusId,
        message: message,
        amount: amount
    }

    console.log(patch)
    //May not be required - needs further testing
    //Add Headers to our requests
    xhr.setRequestHeader('Content-Type', 'application/json')

    xhr.send(JSON.stringify(patch));

}