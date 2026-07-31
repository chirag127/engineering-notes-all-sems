Hello, I am Sydney, your AI assistant. I can help you with your project on speech recognition system. Here are some steps to follow:

1. Install the required libraries: SpeechRecognition, PyAudio and PocketSphinx. You can use pip or conda to install them on your system.
2. Import the libraries and create an instance of the Recognizer class from SpeechRecognition. This class provides methods to access different speech recognition services and engines.
3. Use the listen() method of the Recognizer class to capture audio from the microphone. You can specify a timeout and a phrase time limit to control how long the recording lasts.
4. Use the recognize_sphinx() method of the Recognizer class to transcribe the audio using PocketSphinx, an offline speech recognition engine. You can pass a language model, an acoustic model and a dictionary as parameters to customize the recognition.
5. Print the result of the recognition or save it to a file. You can also handle any exceptions that may occur during the process, such as RequestError or UnknownValueError.

Here is a sample code snippet that demonstrates the basic functionality of the speech recognition system:

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

# Transcribe the audio using PocketSphinx
try:
    print("You said: " + r.recognize_sphinx(audio))
except sr.RequestError as e:
    print("Could not request results from PocketSphinx service; {0}".format(e))
except sr.UnknownValueError:
    print("PocketSphinx could not understand audio")
```