let video = document.getElementById("video-player");
let play_btn = document.getElementById("play-btn");
let mute_btn = document.getElementById("mute-btn");
let fullscreen_btn = document.getElementById("fullscreen-btn");
let body = document.getElementById("body");
let duration = video.duration;

function playPause() {
  if (video.paused) {
    video.play();
    play_btn.innerHTML = '<i class="fa-solid fa-pause"></i>';
  } else {
    video.pause();
    play_btn.innerHTML = '<i class="fa-solid fa-play"></i>';
  }
}

function toggleMute() {
  if (video.muted) {
    video.muted = false;
    mute_btn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
  } else {
    video.muted = true;
    mute_btn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
  }
}

function back() {
  prev = document.referrer;
  console.log(prev);
  console.log(prev.split("/"));

  // TODO replace this with a more robust check
  if (prev.split("/")[3] == "browse") {
    history.back();
  } else {
    // TODO replace this with prod addr, -- pull from env var instead of hard-coding when CI ready
    window.location.replace("http://127.0.0.1:8000/browse");
  }
}

function fullscreen() {
  if (document.fullscreen) {
    document.exitFullscreen();
  } else {
    body.requestFullscreen();
  }
}
