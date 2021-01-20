var SpeechResult = '';

function Speech() {
    if ('webkitSpeechRecognition' in window) {
        // creating voice capture object
        this.recognition = new webkitSpeechRecognition();

        // settings
        this.recognition.continuous = false; // stop automatically
        this.recognition.interimResults = true;
        this.recognition.lang = 'bn-BD';

        this.startCapture = function () {
            this.recognition.start();
        }

        this.stopCapture = function () {
            this.recognition.stop();
        }

        this.recognition.onresult = function (event) {
            SpeechResult = event.results[0][0].transcript
            $('#output').text(SpeechResult);
        }

        this.recognition.onerror = function (event) {
            console.log(event.error);
        }
    } else {
        console.log("webkitSpeechRecognition is not available.");
    }
}

$(document).ready(function () {
    console.log('Starting SpeechRecognition library.');
    var speech = new Speech();

    speech.recognition.onstart = function () {
        $('#capture').text("Stop");
        $('#capture').val("false");
        $('#status').text("Listening...");
    }

    speech.recognition.onend = function () {
        $('#capture').text("Start");
        $('#capture').val("true");
        $('#status').text("Idle");
        AutoRedirect();
    }

    $('#capture').click(function () {
        if ($('#capture').val() === "true") {
            speech.startCapture();
        } else {
            speech.stopCapture();

        }
    });
});

function redirect() {
    var url = "?search=";
    var inputText = document.getElementById("output").value;
    window.location.href = url + SpeechResult;
}

function AutoRedirect() {
    var url = "/news/?search=";
    window.location.href = url + SpeechResult;
}