### Audio Wave Net for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- WaveNet is a **deep generative model** of raw audio waveforms that can produce natural-sounding speech and music .
- WaveNet is based on a **fully convolutional neural network** with **dilated causal convolutions** that allow it to model long-range dependencies in the audio signal .
- WaveNet generates audio samples one by one, conditioning each sample on the previous ones and optionally on some additional inputs (such as text or speaker identity) .
- WaveNet uses a **softmax output layer** with 256 possible values for each sample, corresponding to 8-bit quantization of the waveform .
- WaveNet can be trained on any kind of audio, such as speech, music, or environmental sounds .
- WaveNet can also be used as a **conditional generative model**, where the audio generation is guided by some external information, such as text (for text-to-speech synthesis), speaker identity (for voice conversion), or musical score (for music synthesis)  .
- WaveNet can produce high-quality audio that is close to human performance, and can also capture the characteristics of different speakers, languages, and emotions .
- WaveNet is currently used to power the voices of Google Assistant and other Google products.

Some possible mnemonics and learning tricks for WaveNet are:

- WaveNet is a **wave** of **net**works that can generate **raw audio**.
- WaveNet uses **dilated** convolutions to **dilate** the receptive field and capture long-range dependencies.
- WaveNet is **causal**, meaning it only looks at the past and not the future samples.
- WaveNet is **generative**, meaning it can create new audio samples from scratch or based on some conditions.
- WaveNet is **convolutional**, meaning it uses filters to learn features from the audio signal.