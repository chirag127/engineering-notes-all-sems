### Audio Wave Net

- Audio Wave Net is a deep generative model for raw audio waveforms, developed by Google DeepMind  .
- It can generate speech, music, and other sounds that mimic any human voice and sound more natural than the best existing text-to-speech systems.
- It is based on the idea of autoregressive models, which predict the next sample of a sequence given the previous ones.
- It uses dilated causal convolutions, which allow it to capture long-range dependencies and model temporal hierarchies in the audio data .
- It also uses softmax distributions with 256 possible values for each audio sample, which enable it to model complex and diverse sounds.
- It can be conditioned on additional inputs, such as text, speaker identity, or musical notes, to generate specific types of audio .
- It is trained on large datasets of speech or music, using maximum likelihood estimation and gradient-based optimization.
- It can generate high-quality audio samples at 24,000 samples per second, which is comparable to human hearing.
- It is a powerful and flexible model that can be applied to various domains and tasks, such as speech synthesis, music generation, audio enhancement, sound effects, and audio analysis  .