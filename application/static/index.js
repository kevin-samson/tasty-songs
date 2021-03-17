const timer = ms => new Promise(res => setTimeout(res, ms))
function add_messages(msg) {
    var content =
      '<div class="container">' +
      '<h4 style="color:#000" align="center">' +
      msg +
      "</h4></div>";
    // update div
    var messageDiv = document.getElementById("messages");
    messageDiv.innerHTML += content;
     scrollSmoothToBottom("messages");

}

function scrollSmoothToBottom(id) {
  var div = document.getElementById(id);
  $("#" + id).animate(
    {
      scrollTop: div.scrollHeight - div.clientHeight,
    },
    250
  );
}

async function test () {
    for (let i = 0;i<20;i++){
        add_messages(i);
        await timer(1000);
    }
}




var socket = io.connect("http://" + document.domain + ":" + location.port);
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on("message response", function (msg) {
  add_messages(msg);
});