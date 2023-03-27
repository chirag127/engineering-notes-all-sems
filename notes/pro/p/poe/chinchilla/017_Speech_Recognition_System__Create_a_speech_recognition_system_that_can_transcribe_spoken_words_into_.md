# Speech Recognition System

A Speech Recognition System is a technology that can transcribe spoken words into text. It is used in many applications such as voice assistants, automated customer service, and dictation software. In this project, we will create a speech recognition system using libraries like SpeechRecognition, PyAudio and PocketSphinx.

## Libraries

### SpeechRecognition

SpeechRecognition is a Python library for performing speech recognition. It supports several speech recognition engines and APIs such as Google Speech Recognition, Microsoft Bing Voice Recognition, and CMU Sphinx. The library can be installed using pip.

### PyAudio

PyAudio is a Python library for working with audio. It can be used to record and play audio files, as well as for processing audio data. It can be installed using pip.

### PocketSphinx

PocketSphinx is a speech recognition engine developed by Carnegie Mellon University. It is designed to work on low-resource devices and is suitable for embedded systems. It can be used with SpeechRecognition library to perform speech recognition.

## Creating a Speech Recognition System

To create a speech recognition system, we will follow these steps:

1. Install the required libraries: SpeechRecognition, PyAudio, and PocketSphinx.
2. Record audio using PyAudio and save it as a WAV file.
3. Use SpeechRecognition library to transcribe the audio file into text.
4. Print the transcribed text.

```python
import speech_recognition as sr
import pyaudio

# create an instance of the SpeechRecognition class
r = sr.Recognizer()

# record audio using PyAudio
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# save audio as WAV file
with open("audio.wav", "wb") as f:
    f.write(audio.get_wav_data())

# transcribe audio using SpeechRecognition
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)
    text = r.recognize_sphinx(audio)

# print transcribed text
print("Transcribed Text: ", text)
```

## Conclusion

In this project, we created a speech recognition system using libraries such as SpeechRecognition, PyAudio, and PocketSphinx. We recorded audio using PyAudio, transcribed it into text using SpeechRecognition, and printed the transcribed text. This project can be extended by integrating it with other applications such as voice assistants or automated customer service.