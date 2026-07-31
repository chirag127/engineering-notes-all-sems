### Audio Wave Net

- Audio Wave Net is a deep generative model for raw audio waveforms, developed by Google DeepMind  .
- It can generate speech that mimics any human voice and sounds more natural than the best existing text-to-speech systems.
- It can also generate music and other types of audio signals.
- It is based on the idea of predicting the next audio sample given the previous ones, using a convolutional neural network with dilated causal convolutions.
- It can model complex and diverse distributions of audio data, such as speech and music, by using a softmax output layer with 256 possible values for each 8-bit audio sample.
- It can capture long-range dependencies in audio data, such as prosody and rhythm, by using a large receptive field of up to 16,000 samples (0.64 seconds of audio at 24 kHz sampling rate).
- It can generate high-fidelity audio samples at 24 kHz, with up to 16 times faster than real time on a GPU.
- It can be conditioned on additional inputs, such as speaker identity, text, or musical score, to generate audio with specific characteristics or content .