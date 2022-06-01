// Setting the height of the Body
let navbarHeight = document.getElementById('navbar').offsetHeight;
let elementHeight = window.innerHeight - navbarHeight;
document.getElementById('main-body').setAttribute('style', `height: ${elementHeight}px`);


// Getting Chat-Log and room name
const chatLog = document.getElementById('chat-log');
const room_name = document.getElementById('room-name').textContent;

// Getting Username of the User
let username;
if (document.getElementById('username') != undefined) {
  username = document.getElementById('username').textContent;
}

// URL and Socket Variables
const url = `ws://${window.location.host}/ws/chat/${room_name}/`;
const chatSocket = new WebSocket(url);
const chatSend = document.getElementById('message-form');


// Function to Capitalize UserName
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}


// Function to Notify User Joined
function notifyUserJoined(USERNAME, message) {
  const msgHTML = `
  <div class="alert alert-warning mx-5 p-2">
    ${USERNAME} ${message}
  </div>
  `;

  chatLog.insertAdjacentHTML("beforeend", msgHTML);
  chatLog.scrollTop += 500;
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

    // Loading Last Few Messages
    recievedMessage.last_messages.forEach(msg => {
      let side;
      if (USERNAME === msg.username) {
        side = "right";
      } else {
        side = "left";
      }
      console.log(msg.time);
      appendMessage(capitalizeFirstLetter(msg.username), side, msg.message, msg.time * 1000);
    });

  }

  // Notification Received
  if (recievedMessage.type === 'notify') {
    notifyUserJoined(capitalizeFirstLetter(recievedMessage.username), recievedMessage.message);
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
function appendMessage(name, side, text, timestamp = Date.now()) {
  console.log(timestamp);
  const msgHTML = `
    <div class="msg ${side}-msg">

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date(timestamp))}</div>
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


  const day = date.getDate();
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
  const month = months[date.getMonth()];
  const hours = "0" + date.getHours();
  const minutes = "0" + date.getMinutes();

  return `${day} ${month} ${hours.slice(-2)}:${minutes.slice(-2)}`;
}