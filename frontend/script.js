function updateEventPreview(containerElement, data) {
    textElement = containerElement.querySelector('p');
    //text = `Event: ${data.EventName}\nDriver Name: ${data.Host.UserInfo.Username}\nDestination: ${data.Time}\nDeparture Time: ${data.Location}\nNumber of Remaining Seats: ${data.Capacity}\nParticipants:${data.Attendees}`;
    pText = '';
    for (participant of data.Attendees) {
        pText += `${participant.Username}: ${participant.Email};`
    }
    
    text = `
    Event: ${data.EventName}
    Departure Time: ${data.Location}
    Destination: ${data.Time}
    Number of Remaining Seats: ${data.Capacity}
    Participants: ${pText}`;

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
// form issue 
let i = 0;
function displayEvents(event) {
    eventJson = JSON.parse(event.target.response);
    containers = document.querySelectorAll(".eventcontainer");
    for (let i=0; i<Math.min(eventJson.length, containers.length); i++){
        updateEventPreview(containers[i], eventJson[i]);
    }
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
