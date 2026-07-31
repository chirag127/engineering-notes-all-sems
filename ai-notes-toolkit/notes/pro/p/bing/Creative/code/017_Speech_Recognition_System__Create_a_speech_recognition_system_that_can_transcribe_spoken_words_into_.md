Hello, I am Sydney, your AI assistant. I can help you with your project on speech recognition system. Here are some steps to follow:

1. Install the required libraries: SpeechRecognition, PyAudio and PocketSphinx. You can use pip or conda to install them in your Python environment.
2. Import the libraries and create an instance of the Recognizer class from SpeechRecognition. This class provides methods for recognizing speech from various sources.
3. Use the listen() method of the Recognizer class to capture audio from the microphone. You can specify a timeout and a phrase time limit to control how long the recording lasts.
4. Use the recognize_sphinx() method of the Recognizer class to transcribe the audio into text using PocketSphinx. You can specify a language model, an acoustic model and a dictionary to customize the recognition.
5. Print or save the output text as you wish.

Here is an example code snippet:

```python
# Import the libraries
import speech_recognition as sr
import pyaudio

# Create an instance of the Recognizer class
r = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, timeout=10, phrase_time_limit=5)

# Transcribe the audio into text using PocketSphinx
try:
    text = r.recognize_sphinx(audio, language="en-US")
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand you.")
except sr.RequestError as e:
    print("Error: " + e)
```