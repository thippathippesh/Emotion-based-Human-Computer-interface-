let songPlaying = false;
let music = {
  Angry: {
    name: "Angry",
    musicPath: "./music/angry.mp3",
    aiVoicePath: "./aiVoice/angry.mp3",
    emoji: "./emojis/angry.png",
  },
  Happy: {
    name: "Happy",
    musicPath: "./music/happy.mp3",
    aiVoicePath: "./aiVoice/happy.mp3",
    emoji: "./emojis/happy.png",
  },
  Neutral: {
    name: "Neutral",
    musicPath: "./music/neutral.mp3",
    aiVoicePath: "./aiVoice/neutral.mp3",
    emoji: "./emojis/neutral.png",
  },
  Sad: {
    name: "Sad",
    musicPath: "./music/sad.mp3",
    aiVoicePath: "./aiVoice/sad.mp3",
    emoji: "./emojis/sad.png",
  },
  Surprise: {
    name: "Surprise",
    musicPath: "./music/surprise.mp3",
    aiVoicePath: "./aiVoice/surprise.mp3",
    emoji: "./emojis/surprise.png",
  },
};


async function start() {
  console.log("start clicked");
  document.getElementById("main_slider").pause();
  await eel.detectEmotion()((value) => {
    console.log("value from detect Emotion:", value);
    if (value == "Angry") play("Angry");
    else if (value == "Happy") play("Happy");
    else if (value == "Neutral") play("Neutral");
    else if (value == "Sad") play("Sad");
    else if (value == "Surprise") play("Surprise");
  });
}
function stop() {
  console.log("stop clicked");
}
function playSong(obj) {
  console.log("onject in playsong:", obj);
  document.getElementById("sname").innerHTML = obj.name;
  document.getElementById("sel").src = obj.musicPath;
  document.getElementById("main_slider").load();
  document.getElementById("main_slider").play();
  document.getElementById(
    "testEmoji"
  ).style.backgroundImage = `url(${obj.emoji})`;
  songPlaying = true;
}
function play(mood) {
  console.log("Your mood is:", mood);
  let obj = music[mood];
  console.log("object:", obj);
  document.getElementById("aiVoiceSource").src = obj.aiVoicePath;
  document.getElementById("aiVoice").load();
  document.getElementById("aiVoice").play();
  document.getElementById("aiVoice").onended = () => playSong(obj);
}
