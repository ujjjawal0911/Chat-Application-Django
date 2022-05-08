const url = 'ws://' + window.location.host + '/ws/chat/';
const chatSocket = new WebSocket(url);
const chatSend = document.getElementById('message-form');


// When Socket Open
chatSocket.onopen = function (event) {
    console.log(event.data);
}

// When Socket Closed
chatSocket.onmessage = function (event) {
    console.log(event.data);
}

chatSend.onsubmit = (event) => {
    // Preventing Default Submit Option
    event.preventDefault();

    // Getting Message Element
    const messageInput = document.getElementById('message');

    // Extracting the message and sending back to server
    let message = messageInput.value;
    chatSocket.send(message);

    // Resetting and setting back to focus
    chatSend.reset();
    chatSend.focus();
}