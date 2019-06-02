var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 5;
recognition.start();
recognition.continuous = true;
recognition.interimResults = true;


recognition.onresult = function(event) {
  console.log(event);
  console.log('You said: ', event.results[0][0].transcript);
};

recognition.onstart = function() { 
  console.log('Voice recognition activated. Try speaking into the microphone.');
}

recognition.onspeechend = function() {
  readOutLoud('You were quiet for a while so voice recognition turned itself off.');
}

recognition.onend = function() { console.log("ONEND"); recognition.start(); }


recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    readOutLoud('No speech was detected. Try again.');  
  };
}

function readOutLoud(message) {
  var speech = new SpeechSynthesisUtterance();

  // Set the text and voice attributes.
  speech.text = message;
  speech.volume = 1;
  speech.rate = 1;
  speech.pitch = 1;

  window.speechSynthesis.speak(speech);
}