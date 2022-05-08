const url = 'ws://' + window.location.host + '/ws/chat/';
const chatSocket = new WebSocket(url);
const chatSend = document.getElementById('message-form');

// Getting Chat Log
const chatLog = document.getElementById('chat-log');


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
    chatLog.innerHTML += `<div>${message}</div>`;
    chatSocket.send(message);

    // Resetting and setting back to focus
    chatSend.reset();
    chatSend.focus();
}