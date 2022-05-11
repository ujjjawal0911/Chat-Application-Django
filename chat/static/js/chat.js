// Getting Chat-Log and room name
const chatLog = document.getElementById('chat-log');
const room_name = document.getElementById('room-name').textContent;

// Getting Username of the Us
const username = document.getElementById('username').textContent;

// URL and Socket Variables
const url = `ws://${window.location.host}/ws/chat/${room_name}/`;
const chatSocket = new WebSocket(url);
const chatSend = document.getElementById('message-form');


// Function to Capitalize UserName
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

// Variable to Set Username
let USERNAME;

// When Socket Recieved
chatSocket.onmessage = function (event) {

  // Converting Received Message to JSON Format
  const recievedMessage = JSON.parse(event.data);

  // Connection Made - set Username - important for Anonymous Users
  console.log(recievedMessage);
  if (recievedMessage.type === 'connection_made') {
    USERNAME = recievedMessage.username;
  }


  // On recieivng normal messages
  if (recievedMessage.type === 'chat_message') {
    let side;
    if (USERNAME === recievedMessage.username) {
      side = "right";
    } else {
      side = "left";
    }
    appendMessage(capitalizeFirstLetter(recievedMessage.username), side, recievedMessage.message);
  }
}

chatSend.onsubmit = (event) => {
  // Preventing Default Submit Option
  event.preventDefault();

  // Getting Message Element
  const messageInput = document.getElementById('message');

  // Extracting the message and sending back to server
  let message = messageInput.value;
  chatSocket.send(JSON.stringify({
    'message': message,
    'username': USERNAME,
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

// Function to Format Date
function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}