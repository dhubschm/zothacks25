// ACCOUNT
const username = document.querySelector('#userField');
const email = document.querySelector('#emailField');

const loginSubmitBtn = document.querySelector('#loginButton');

loginSubmitBtn.addEventListener('click', async function () {
    const account = {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({username, email})
    };

    await fetch('/users', account);
});

// DRIVER FORM
const carType = document.querySelector('#carType');
const destination = document.querySelector('#destination');
const numOfSeats = document.querySelector('#numOfSeats');
const time = document.querySelector("#timeOfDepart")

const driverSubmitBtn = document.querySelector('#submitEventBtn');
driverSubmitBtn.addEventListener('click', async function () {
    const event = {
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify({carType, destination, numOfSeats, time})
    };

    await fetch('/users', event);
});

// GET PREV EVENTS (in progress)

/*
async function updateEvents() {
    const events = (await fetch('/users/events')).json();
}
    */

// For each class="eventcontainer", need to change eventnameX, eventdestX, departtimeX, seatsremX
// Fetch event list from FastAPI in route "/users/events" (it has limit parameter)

// Can also get specific event