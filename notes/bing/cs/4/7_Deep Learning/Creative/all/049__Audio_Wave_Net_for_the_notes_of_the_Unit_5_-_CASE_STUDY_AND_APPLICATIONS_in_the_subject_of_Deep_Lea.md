### Audio Wave Net for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- WaveNet is a deep neural network for generating raw audio waveforms  .
- The main objective of WaveNet is to generate new samples from the original distribution of the data. Hence, it is known as a generative model .
- The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones .
- WaveNet creates the waveforms of speech patterns by predicting which sounds likely follow each other. Each waveform is built one sample at a time, with up to 24,000 samples per second of sound.
- WaveNet can generate speech which mimics any human voice and which sounds more natural than the best existing Text-to-Speech systems. It can also generate music and other types of audio .
- WaveNet consists of a stack of convolutional layers, where each layer has a larger receptive field than the previous one . This allows the model to capture long-range dependencies in the audio data .
- WaveNet uses dilated convolutions, which are convolutions with holes, to increase the receptive field without increasing the number of parameters or the computation time .
- WaveNet also uses residual and skip connections, which are connections that bypass some layers, to improve the gradient flow and the modeling capacity of the network .
- WaveNet can be conditioned on additional inputs, such as speaker identity, text, or linguistic features, to generate audio with specific characteristics or content .
- WaveNet is trained on speech samples using a cross-entropy loss function, which measures the difference between the predicted and the actual distributions of the audio samples .
- WaveNet is evaluated on various datasets and metrics, such as mean opinion score, log-likelihood, and signal-to-noise ratio, and it outperforms the state-of-the-art methods in terms of naturalness and quality of the generated audio .

Some possible mnemonics and learning tricks for Audio Wave Net are:

- WaveNet: WAVeform gEneration using Neural neTwork
- Generative model: Generates new samples from the original data
- Autoregressive model: Auto (self) + regressive (backward) = predicts each sample based on previous ones
- Dilated convolutions: DILated = Dots In Layers = convolutions with holes
- Residual and skip connections: RESidual = REuse Some outputs = add outputs of previous layers to current layer
- Skip connections: SKIP = Skip some layers = connect outputs of some layers directly to the final layer
- Conditioned on additional inputs: CONditioned = CONtrol the output = use extra information to influence the generated audio