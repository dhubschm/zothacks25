//import React from "react";

// ACCOUNT

function updateEventPreview(containerElement, data) {
    textElement = containerElement.querySelector('p');
    //text = `Event: ${data.EventName}\nDriver Name: ${data.Host.UserInfo.Username}\nDestination: ${data.Time}\nDeparture Time: ${data.Location}\nNumber of Remaining Seats: ${data.Capacity}\nParticipants:${data.Attendees}`;
    text = `
    Event: ${data.EventName}
    Driver Name: ${data.Host.UserInfo.Username}
    Destination: ${data.Time}\nDeparture Time: ${data.Location}
    Number of Remaining Seats: ${data.Capacity}
    Participants:${data.Attendees}`;

    textElement.textContent = text;
    buttonElement = containerElement.querySelector('button');
    enableButton(buttonElement);
}

function enableButton(btn) {
    btn.textContent = 'Join!';
    btn.disabled = false;
}

function getEvents() {
    const req = new XMLHttpRequest();
    req.open("GET", "/events/");
    req.addEventListener("load", displayEvents);
    req.send(); 
    return req;
}

let i = 0;
function displayEvents(event) {
    eventJson = JSON.parse(event.target.response);
    containers = document.querySelectorAll(".eventcontainer");
    // contains.length()
    /*if (numEvent == 10) {
        numEvent == 1;
    }*/
    updateEventPreview(containers[i], eventJson);
    i++;
    /*
    for (container of containers) {
        updateEventPreview(container, eventJson);
    }*/
}

const loginSubmitBtn = document.querySelector("#submitEventBtn");
loginSubmitBtn.addEventListener("click", function () {
    // loginSubmitBtn = 0;
});

const driverSubmitBtn = document.querySelector("#submitEventBtn");
driverSubmitBtn.addEventListener("click", function () {
    getEvents();
});

window.onload = getEvents;
/*
const username = document.querySelector("#userField");
const email = document.querySelector("#emailField");

const loginSubmitBtn = document.querySelector("#loginButton");

loginSubmitBtn.addEventListener("click", function () {
    loginSubmitBtn.textContent = "Logout";
});

// DRIVER FORM
const carType = document.querySelector("#carType");
const destination = document.querySelector("#destination");
const numOfSeats = document.querySelector("#numOfSeats");
const time = document.querySelector("#timeOfDepart");

const driverSubmitBtn = document.querySelector("#submitEventBtn");
driverSubmitBtn.addEventListener("click", function () {
    driverSubmitBtn.textContent = "Exit trip";
});

// GET PREV EVENTS (in progress)
*/
/*


function createEventPreview() {
    pass;
}
    */

// For each class="eventcontainer", need to change eventnameX, eventdestX, departtimeX, seatsremX
// Fetch event list from FastAPI in route "/users/events" (it has limit parameter)

// Can also get specific event