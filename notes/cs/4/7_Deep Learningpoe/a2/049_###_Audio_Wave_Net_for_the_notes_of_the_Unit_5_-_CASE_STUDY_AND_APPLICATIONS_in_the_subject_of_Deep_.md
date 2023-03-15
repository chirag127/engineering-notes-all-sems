 Here is the markdown content for ### Audio Wave Net for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning:

### Audio Wave Net

- Audio Wave Net is a neural network architecture designed for generating raw audio waveforms.
- It is a type of autoregressive model that predicts the next sample in a sequence based on previous samples.
- It uses dilated convolutions to enlarge the receptive field and capture long-range dependencies in the audio signal.
- The architecture is made up of stacks of residual blocks containing dilated convolutions and gated linear units.
- Sample-by-sample generation allows high quality audio to be synthesized since errors do not accumulate over long sequences.
- However, this also makes Audio Wave Net computationally expensive to train and generate audio with.
- Audio Wave Net has been used to generate piano melodies, speech, and other types of raw audio.

Advantages:

- Can generate high quality raw audio waveforms.
- Allows sample-by-sample generation avoiding error accumulation.
- Uses dilated convolutions to capture long-range dependencies.

Disadvantages:

- Computationally expensive to train and generate audio.
- Generates audio sample-by-sample making it slow.
- Difficult to control properties of generated audio like rhythm or tone.

Examples:

- Generating piano melodies: https://deepmind.com/blog/wavenet-generative-model-raw-audio/
- Speech synthesis: https://arxiv.org/abs/1609.03499

Applications:

- Audio compression by learning to predict future samples.
- Synthesizing and manipulating audio.
- Adding missing frequencies or instruments to audio.
- Speech synthesis.