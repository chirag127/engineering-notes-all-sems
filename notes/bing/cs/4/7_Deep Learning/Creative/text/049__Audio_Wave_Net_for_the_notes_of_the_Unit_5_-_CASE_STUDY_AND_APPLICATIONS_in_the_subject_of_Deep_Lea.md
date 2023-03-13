### Audio Wave Net

- Audio Wave Net is a deep generative model for raw audio waveforms .
- It can generate speech that mimics any human voice and sounds more natural than the best existing Text-to-Speech systems.
- It can also model any kind of audio, including music.
- It works by directly modelling the raw waveform of the audio signal, one sample at a time, with up to 24,000 samples per second of sound .
- It uses a convolutional neural network with dilated causal convolutions to capture long-range dependencies in the audio signal.
- It also uses a softmax output layer with 256 possible values for each sample, representing the possible amplitudes of the waveform.
- It can be conditioned on additional inputs, such as speaker identity, text, or linguistic features, to generate specific types of audio.
- It can be trained on speech samples from different languages and domains, and can generate speech in any of them.
- It can also generate novel sounds that are not present in the training data, such as animal noises or musical instruments.
- It can be used for various applications, such as speech synthesis, speech recognition, music generation, audio enhancement, and audio analysis .

: WaveNet: A generative model for raw audio - DeepMind
: WaveNet - DeepMind