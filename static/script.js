const startBtn = document.getElementById('startBtn');
const statusDiv = document.getElementById('status');
const transcriptDiv = document.getElementById('transcript');

// Check browser support
if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    alert("Your browser does not support Web Speech API. Please use Chrome or Edge.");
}

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

startBtn.addEventListener('click', () => {
    try {
        recognition.start();
        statusDiv.textContent = "Listening...";
        startBtn.textContent = "Listening...";
        startBtn.classList.add('listening');
        startBtn.disabled = true;
    } catch (e) {
        console.error(e);
        statusDiv.textContent = "Error starting recognition.";
    }
});

recognition.onresult = async (event) => {
    const text = event.results[0][0].transcript;
    statusDiv.textContent = "Processing...";
    startBtn.textContent = "Processing...";
    startBtn.classList.remove('listening');

    displayTranscript(`You: "${text}"`);
    
    // Send to backend logic
    await sendTextToBackend(text);
};

recognition.onspeechend = () => {
    recognition.stop();
    startBtn.disabled = false;
    startBtn.textContent = "Start Listening";
    startBtn.classList.remove('listening');
};

recognition.onerror = (event) => {
    statusDiv.textContent = 'Error occurred in recognition: ' + event.error;
    startBtn.disabled = false;
    startBtn.textContent = "Start Listening";
    startBtn.classList.remove('listening');
};

async function sendTextToBackend(text) {
    try {
        const response = await fetch('/api/process_text', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });
        const data = await response.json();
        
        if (data.error) {
            displayTranscript(`Error: ${data.error}`);
            speak("I'm sorry, I encountered an error.");
        } else {
            const botResponse = data.text_response;
            displayTranscript(`Bot: "${botResponse}"`, true);
            speak(botResponse);
        }
    } catch (error) {
        console.error("Backend Error:", error);
        displayTranscript("Error connecting to server.");
        speak("I cannot connect to the brain right now.");
    }
}

function speak(text) {
    statusDiv.textContent = "Speaking...";
    const utterance = new SpeechSynthesisUtterance(text);
    
    // Try to find a good voice
    const voices = window.speechSynthesis.getVoices();
    // Prefer "Google US English" or safe fallback
    const preferredVoice = voices.find(v => v.name.includes("Google US English")) || voices[0];
    if (preferredVoice) utterance.voice = preferredVoice;

    utterance.rate = 0.9; // Slightly slower
    utterance.pitch = 1;

    utterance.onend = () => {
        statusDiv.textContent = "Click 'Start Listening'";
    };

    window.speechSynthesis.speak(utterance);
}

function displayTranscript(msg, append = false) {
    transcriptDiv.style.display = 'block';
    if (append) {
        transcriptDiv.innerHTML += `<br><br>${msg}`;
    } else {
        transcriptDiv.innerHTML = msg;
    }
}
