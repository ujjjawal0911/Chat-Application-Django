
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

// When Socket Closed
chatSocket.onmessage = function (event) {
    const recievedMessage = JSON.parse(event.data);
    chatLog.innerHTML += `<div>${recievedMessage.message}</div>`;
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