
// Getting Chat Log and room name
const chatLog = document.getElementById('chat-log');
const room_name = document.getElementById('room-name').textContent;

// URL and Socket Variables
const url = `ws://${window.location.host}/ws/chat/${room_name}/`;
const chatSocket = new WebSocket(url);
const chatSend = document.getElementById('message-form');


// When Socket Open
chatSocket.onopen = function (event) {
    console.log(event.data);
}

// Test Variables
const USERNAME = "Harvey";
const RECEIVER = "Adam";

// When Socket Closed
chatSocket.onmessage = function (event) {
    const recievedMessage = JSON.parse(event.data);
    appendMessage(USERNAME, "left", recievedMessage.message);
    // appendMessage(PERSON_NAME, PERSON_IMG, "right", recievedMessage);
    // chatLog.innerHTML += `<div>${recievedMessage.message}</div>`;
}

chatSend.onsubmit = (event) => {
    // Preventing Default Submit Option
    event.preventDefault();

    // Getting Message Element
    const messageInput = document.getElementById('message');

    // Extracting the message and sending back to server
    let message = messageInput.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    // Resetting and setting back to focus
    chatSend.reset();
    chatSend.focus();
}

// Append Message
function appendMessage(name, side, text) {
    const msgHTML = `
    <div class="msg ${side}-msg">

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

    chatLog.insertAdjacentHTML("beforeend", msgHTML);
    chatLog.scrollTop += 500;
}