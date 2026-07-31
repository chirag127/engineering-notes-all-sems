### Audio Wave Net

- Audio Wave Net is a deep generative model for raw audio waveforms, developed by Google DeepMind  .
- It can generate speech that mimics any human voice and sounds more natural than the best existing text-to-speech systems.
- It can also generate music and other types of audio signals.
- It is based on the idea of autoregressive models, which predict the next sample of a sequence given the previous ones.
- It uses dilated causal convolutions to capture long-range dependencies in the audio data.
- It also uses gated activation units and residual connections to improve the learning capacity and gradient flow of the network.
- It can be conditioned on additional inputs, such as text or speaker identity, to generate specific types of audio.
- It is trained on large datasets of speech or music, using maximum likelihood estimation.
- It generates audio samples one by one, with up to 24,000 samples per second of sound.
- It is a powerful and flexible model that can learn from any kind of raw audio and generate realistic and diverse sounds  .

: https://towardsdatascience.com/how-wavenet-works-12e2420ef386
: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/
: https://www.deepmind.com/blog/wavenet-a-generative-model-for-raw-audio
: https://www.deepmind.com/research/highlighted-research/wavenet
: https://arxiv.org/abs/1609.03499