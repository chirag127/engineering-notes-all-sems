## Unit 2 - DEEP NETWORKS

Deep networks are artificial neural networks that have multiple hidden layers between the input and output layers. They can learn complex and abstract patterns from data, and are widely used for various tasks such as computer vision, natural language processing, speech recognition, etc.

There are many types of deep networks, each with different architectures and applications. Some of the most common ones are:

- Convolutional Neural Networks (CNNs): These are networks that use convolutional layers to extract features from images or other grid-like data. They are composed of three types of layers: convolutional, pooling, and fully connected. Convolutional layers apply filters to the input data and produce feature maps. Pooling layers reduce the spatial dimensions of the feature maps by applying a function such as max or average. Fully connected layers connect every neuron in one layer to every neuron in the next layer. CNNs are often used for image recognition, object detection, face recognition, etc.

- Recurrent Neural Networks (RNNs): These are networks that have loops in their structure, allowing them to process sequential data such as text, speech, or time series. They have a hidden state that is updated at each time step based on the current input and the previous state. RNNs can learn long-term dependencies in the data, but they also suffer from the problems of vanishing and exploding gradients. To overcome these issues, variants of RNNs such as Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) have been proposed. These networks use gates to control the flow of information in and out of the hidden state, making them more capable of capturing long-term dependencies. RNNs are often used for natural language processing, speech recognition, machine translation, etc.

- Autoencoders (AEs): These are networks that learn to compress and reconstruct the input data, usually in an unsupervised manner. They consist of two parts: an encoder and a decoder. The encoder maps the input data to a lower-dimensional latent space, and the decoder maps the latent space back to the original data. The goal is to minimize the reconstruction error, which forces the network to learn the most salient features of the data. AEs can be used for dimensionality reduction, data compression, denoising, anomaly detection, etc.

- Generative Adversarial Networks (GANs): These are networks that learn to generate realistic and novel data, such as images, text, or audio. They consist of two parts: a generator and a discriminator. The generator tries to produce fake data that looks like the real data, and the discriminator tries to distinguish between the real and fake data. The two networks compete with each other in a minimax game, where the generator tries to fool the discriminator, and the discriminator tries to catch the generator. The goal is to reach a Nash equilibrium, where the generator produces data that the discriminator cannot tell apart from the real data. GANs can be used for image synthesis, image editing, style transfer, text generation, etc.

The following diagram illustrates the basic architecture of a CNN:

```
Input layer
    |
    v
Convolutional layer 1 -> Pooling layer 1 -> Activation layer 1
    |
    v
Convolutional layer 2 -> Pooling layer 2 -> Activation layer 2
    |
    v
...
    |
    v
Convolutional layer N -> Pooling layer N -> Activation layer N
    |
    v
Flatten layer
    |
    v
Fully connected layer 1 -> Activation layer 1
    |
    v
Fully connected layer 2 -> Activation layer 2
    |
    v
...
    |
    v
Fully connected layer M -> Activation layer M
    |
    v
Output layer
```

The following diagram illustrates the basic architecture of an RNN:

```
Input layer
    |
    v
Recurrent layer 1 -> Activation layer 1
    ^                   |
    |                   v
    +-----------------Recurrent layer 2 -> Activation layer 2
                        ^                   |
                        |                   v
                        +-----------------Recurrent layer 3 -> Activation layer 3
                                            ^                   |
                                            |                   v
                                            +-----------------...
                                                                |
                                                                v
Output layer
```

The following diagram illustrates the basic architecture of an AE:

```
Input layer
    |
    v
Encoder layer 1 -> Activation layer 1
    |
    v
Encoder layer 2 -> Activation layer 2
    |
    v
...
    |
    v