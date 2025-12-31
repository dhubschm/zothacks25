function updateEventPreview(containerElement, data) {
    const wrapper = containerElement.querySelector('.event-info-wrapper');
    if (!wrapper) return;

    let pText = data.Attendees.length > 0 
        ? data.Attendees.map(p => p.Username).join(", ") 
        : "No one joined yet";

    // This template keeps everything in neat rows
    wrapper.innerHTML = `
        <div style="margin-bottom: 10px;">
            <b class="detail-label">🚙Car Description:</b><br>
            <span style="font-size:15px; font-family: Arial;color:#3a3a3a;">${data.Car_description || 'N/A'}</span>
        </div>
        <div style="margin-bottom: 10px;">
            <b class="detail-label">🗺️Destination:</b><br>
            <span style="font-size:15px; font-family: Arial;color:#3a3a3a;">${data.Location}</span>
        </div>
        <div style="margin-bottom: 10px;">
            <b class="detail-label">🕒Departure Time:</b><br>
            <span style="font-size:15px; font-family: Arial;color:#3a3a3a;">${data.Time}</span>
        </div>
        <div style="margin-bottom: 10px;">
            <b class="detail-label">💺Remaining Seats:</b><br>
            <span style="font-size:15px; font-family: Arial;color:#3a3a3a;">${data.Capacity} Left</span>
        </div>
        <div class="participants-box"
            <b>Participants:</b> ${pText}
        </div>
    `;
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
