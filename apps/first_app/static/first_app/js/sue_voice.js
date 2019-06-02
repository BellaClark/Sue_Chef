
console.log("sue says hello")
var sue = new p5.Speech(); // speech synthesis object
sue.speak('sue says hi there'); // say something 

var foo = new p5.SpeechRec(); // speech recognition object (will prompt for mic access)
foo.start(); // start listening
foo.onResult = showResult; // bind callback function to trigger when speech is recognized

function showResult() {
    console.log(foo.resultString); // log the result
}