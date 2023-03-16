### Audio Wave Net

- Audio Wave Net is a deep generative model for raw audio waveforms, developed by Google DeepMind  .
- It can generate speech that mimics any human voice and sounds more natural than the best existing text-to-speech systems.
- It can also generate music by learning from a large corpus of musical pieces.
- It is based on the idea of autoregressive models, which predict the next sample in a sequence given the previous ones .
- It uses a stack of convolutional layers with dilated causal filters, which allow it to capture long-range dependencies in the audio data .
- It also uses residual and skip connections, gated activations, and softmax outputs to improve the training and generation process .
- It can be conditioned on additional inputs, such as speaker identity, text, or musical genre, to generate diverse and controllable audio outputs .
- It is trained using maximum likelihood estimation, which minimizes the negative log-likelihood of the data given the model .
- It is evaluated using subjective and objective metrics, such as mean opinion score, log-likelihood, and signal-to-noise ratio .
- It has achieved state-of-the-art results on speech synthesis, music generation, and audio super-resolution .