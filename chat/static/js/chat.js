const url = 'ws://' + window.location.host + '/ws/chat/';
const chatSocket = new WebSocket(url);

chatSocket.onopen = function (event) {
    console.log(event.data);
}

chatSocket.onmessage = function (event) {
    console.log(event.data);
}