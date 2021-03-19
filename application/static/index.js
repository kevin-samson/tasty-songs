//const timer = ms => new Promise(res => setTimeout(res, ms))
var socket = io.connect("http://" + document.domain + ":" + location.port);

function add_messages(track) {
    var content =
      '<a href='+track.url+'>'+
      '<div'+
        ' class="d-flex m-2 align-items-center song-player"'+
        ' style="cursor: pointer;">'+
        '<img src='+ track.album +'></img>'+
        '<div class="ml-3">'+
        '<div>'+track.title+'</div>'+
        '<div class="text-muted">'+track.artist+'</div>'+
        '</div>'+
        "</div></a>";
    // update div
    var messageDiv = document.getElementById("messages");
    messageDiv.innerHTML += content;

}


function clear_all() {
    var messageDiv = document.getElementById("messages");
    messageDiv.innerHTML = ''
}

function scrollSmoothToBottom(id) {
  var div = document.getElementById(id);
  $("#" + id).animate(
    {
      scrollTop: div.scrollHeight - div.clientHeight,
    },
    500
  );
}

async function test () {
    for (let i = 0;i<20;i++){
        add_messages(i);
    }
    scrollSmoothToBottom("messages");
}



/*document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === 'visible'){
        socket.emit('my event', {data:"Looking at screen"})
    }else{
        socket.emit('my event', {data:"Not looking at screen"})
    }
});*/

socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on("message response", function (msg) {
  add_messages(msg);
});

socket.on('song data', (data) => {
    let tracks = data.tracks.items
    console.log(tracks)
    for (let i=0; i<tracks.length; i++){
        add_messages({title:tracks[i].name,
                      artist:tracks[i].artists[0].name,
                      album:tracks[i].album.images[2].url,
                      url:tracks[i].external_urls.spotify})
    }
    let SongPlayer = document.querySelectorAll(".song-player")
    console.log(SongPlayer)

})

let box = document.getElementById('msg')
box.addEventListener('keyup',() => {
    clear_all()
    console.log(box.value)
    if (box.value !== '') {
        socket.emit('search song', {data: box.value});
    }
})


/*'<div'+
'className="d-flex m-2 align-items-center"'+
'style="cursor: pointer;"'+
'onClick='+track.url+'>'+
'<img src='+ {track.albumUrl} +'/>'+
'<div className="ml-3">'+
'<div>'+track.title+'</div>'+
'<div className="text-muted">'+track.artist+'</div>'+
'</div>'+
'</div>'*/

/*var content =
      '<div class="container">' +
      '<b style="color:#000" class="right">' +
      track.artist +
      "</b><p>" +
      track.title +
      '</p>'+
      '<img src='+track.album+'></img>'+
      "</div>";*/