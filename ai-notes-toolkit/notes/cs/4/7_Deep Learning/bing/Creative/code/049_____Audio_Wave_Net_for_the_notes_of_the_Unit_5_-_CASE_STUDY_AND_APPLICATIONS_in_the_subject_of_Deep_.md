# Audio Wave Net

Audio Wave Net is a deep learning-based generative model for raw audio waveforms. It was developed by Google DeepMind and can be used for applications such as speech synthesis, music generation, and audio enhancement. Some of the main features of Audio Wave Net are:

- It is a fully probabilistic and autoregressive model, meaning that it predicts each audio sample based on all the previous ones, using a conditional distribution.
- It uses dilated causal convolutions, which allow it to capture long-range dependencies and temporal patterns in the audio data, without increasing the computational complexity or the receptive field size.
- It employs a softmax output layer with 256 possible values for each sample, which enables it to model the complex and noisy nature of raw audio signals.
- It can be conditioned on additional inputs, such as text, speaker identity, or musical notes, to generate audio in a specific style or domain.
- It can generate high-quality and natural-sounding audio, outperforming the state-of-the-art text-to-speech and music generation systems.

The following diagram illustrates the architecture of Audio Wave Net:

![Audio Wave Net architecture](https://www.deepmind.com/images/wavenet-architecture.png)

The input of the model is a sequence of audio samples, represented as discrete values in the range of [-128, 127]. The output is a probability distribution over the same range, indicating the likelihood of each possible value for the next sample. The model consists of several layers of dilated causal convolutions, each with a different dilation factor, which determines how far apart the inputs are in each convolution. The dilation factor increases exponentially with the depth of the layer, allowing the model to capture longer and longer dependencies as it goes deeper. The outputs of the convolution layers are summed with residual and skip connections, which help the model learn faster and avoid vanishing gradients. The final output is obtained by applying a 1x1 convolution and a softmax activation to the skip connections.

The model can also take additional inputs, such as text, speaker identity, or musical notes, to condition the audio generation. These inputs are encoded by separate networks, such as recurrent neural networks (RNNs) or convolutional neural networks (CNNs), and then fed into the Audio Wave Net model as auxiliary inputs. The auxiliary inputs are added to the outputs of the convolution layers, before the residual and skip connections, to modulate the audio generation according to the desired attributes.

The model is trained by minimizing the cross-entropy loss between the predicted distribution and the true value of the next sample, using stochastic gradient descent (SGD) or its variants. The model can generate new audio samples by sampling from the output distribution, starting from a given seed or silence. The generation process is sequential and autoregressive, meaning that each sample depends on all the previous ones. This makes the generation slow, but also ensures the coherence and quality of the audio.

Audio Wave Net is a powerful and versatile generative model for raw audio, which can produce realistic and natural-sounding audio for various applications. It is based on deep learning techniques that exploit the temporal structure and the probabilistic nature of audio data. It can also be conditioned on additional inputs, to generate audio in a specific style or domain. Audio Wave Net is a breakthrough in audio synthesis and generation, and a promising direction for future research and development.