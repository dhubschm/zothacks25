// ACCOUNT
const username = document.querySelector('#userField');
const email = document.querySelector('#emailField');

const loginSubmitBtn = document.querySelector('#loginButton'); //uh... id may change

loginSubmitBtn.addEventListener('click', function () {
    const account = {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({username, email})
    };

    fetch('/users', account);
});

// DRIVER FORM
const carType = document.querySelector('#carType');
const destination = document.querySelector('#destination');
const numOfSeats = document.querySelector('#numOfSeats');
const time = document.querySelector("#timeOfDepart")

const driverSubmitBtn = document.querySelector('#submitEventBtn');  //id probably wont change but be prepared
driverSubmitBtn.addEventListener('click', function () {
    const event = {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({carType, destination, numOfSeats, time})
    };

    fetch('/users', event);
});