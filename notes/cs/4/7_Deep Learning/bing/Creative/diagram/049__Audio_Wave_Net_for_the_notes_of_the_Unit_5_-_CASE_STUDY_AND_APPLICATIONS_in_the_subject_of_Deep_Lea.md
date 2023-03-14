The following diagram illustrates the basic architecture of a WaveNet, a deep generative model of raw audio waveforms. WaveNet consists of a stack of convolutional layers with various dilation factors that allow its receptive field to grow exponentially with depth and cover thousands of timesteps. Each layer predicts the next sample of the audio signal based on the previous samples and some additional conditioning information, such as the text or speaker identity. The output of the network is a probability distribution over the possible values of the next sample, which can be sampled from to generate new audio.

```
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|  Conditioning   |  |  Conditioning   |  |  Conditioning   |  |  Conditioning   |
|   Information   |  |   Information   |  |   Information   |  |   Information   |
|                 |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       v                 v                 v                 v
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|  Convolutional  |  |  Convolutional  |  |  Convolutional  |  |  Convolutional  |
|     Layer 1     |  |     Layer 2     |  |     Layer 3     |  |     Layer N     |
|                 |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       v                 v                 v                 v
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|  Probability    |  |  Probability    |  |  Probability    |  |  Probability    |
|  Distribution   |  |  Distribution   |  |  Distribution   |  |  Distribution   |
|   for Next      |  |   for Next      |  |   for Next      |  |   for Next      |
|    Sample       |  |    Sample       |  |    Sample       |  |    Sample       |
|                 |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       |                 |                 |                 |
       v                 v                 v                 v
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|    Sampled      |  |    Sampled      |  |    Sampled      |  |    Sampled      |
|     Value       |  |     Value       |  |     Value       |  |     Value       |
|                 |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
       |