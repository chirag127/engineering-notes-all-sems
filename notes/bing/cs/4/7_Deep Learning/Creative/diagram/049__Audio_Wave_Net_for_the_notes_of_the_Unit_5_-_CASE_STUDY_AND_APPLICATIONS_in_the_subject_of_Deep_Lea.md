A WaveNet is a deep generative model of raw audio waveforms that can produce realistic speech and music. It is based on a convolutional neural network that operates directly on the audio samples, one at a time. It uses dilated causal convolutions to capture long-range dependencies in the audio signal, and a softmax output layer to predict the next sample from a discrete set of possible values. The WaveNet model can be conditioned on additional inputs, such as text or speaker identity, to generate different kinds of audio.

The following diagram illustrates the basic architecture of a WaveNet:

```
    Input audio samples
    |
    V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Dilated causal convolutions
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |       |           |                   |
    V       V           V                   V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Gated activation units
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |       |           |                   |
    V       V           V                   V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Residual and skip connections
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |       |           |                   |
    V       V           V                   V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Receptive field
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |       |           |                   |
    V       V           V                   V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Output distribution
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
    |       |           |                   |
    V       V           V                   V
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  Predicted audio samples
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
```