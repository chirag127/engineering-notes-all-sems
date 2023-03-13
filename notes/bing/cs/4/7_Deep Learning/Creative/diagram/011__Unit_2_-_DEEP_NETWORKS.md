## Unit 2 - DEEP NETWORKS

Deep networks are neural networks that have multiple hidden layers between the input and output layers. They can learn complex and abstract features from the data, and are widely used for various tasks such as computer vision, natural language processing, speech recognition, etc.

There are different types of deep networks, each with its own architecture and principles. Some of the common ones are:

- Convolutional Neural Networks (CNNs): These are networks that use convolutional layers to extract features from images or other types of data that have a spatial structure. Convolutional layers apply filters to the input data and produce feature maps that capture the local patterns in the data. CNNs can also use pooling layers to reduce the dimensionality of the feature maps, and fully connected layers to perform classification or regression tasks. CNNs are very effective for image recognition, object detection, face recognition, etc.

- Recurrent Neural Networks (RNNs): These are networks that use recurrent layers to process sequential data, such as text, speech, or time series. Recurrent layers have a hidden state that can store information from previous inputs, and use it to influence the current output. RNNs can learn long-term dependencies and temporal patterns in the data, and are suitable for natural language processing, machine translation, speech recognition, etc.

- Autoencoders: These are networks that learn to encode the input data into a lower-dimensional representation, and then decode it back to the original data. Autoencoders can be used for dimensionality reduction, data compression, denoising, anomaly detection, etc. Autoencoders can also have different variants, such as sparse autoencoders, variational autoencoders, or generative adversarial networks.

- Generative Adversarial Networks (GANs): These are networks that consist of two components: a generator and a discriminator. The generator tries to produce realistic data that can fool the discriminator, while the discriminator tries to distinguish between real and fake data. GANs can learn to generate new data that resembles the training data, such as images, text, or audio.

- Residual Networks (ResNets): These are networks that use residual connections to overcome the problem of vanishing gradients in very deep networks. Residual connections are shortcuts that allow the input of a layer to be added to the output of a later layer, bypassing some intermediate layers. ResNets can learn very deep and complex features, and are widely used for image recognition, object detection, etc.

The following diagram illustrates the basic architecture of a CNN:

```
Input image
    |
    V
Convolutional layer 1
    |
    V
Pooling layer 1
    |
    V
Convolutional layer 2
    |
    V
Pooling layer 2
    |
    V
Fully connected layer 1
    |
    V
Fully connected layer 2
    |
    V
Output layer
```

The following diagram illustrates the basic architecture of an RNN:

```
Input sequence
    |
    V
Recurrent layer 1
    |
    V
Recurrent layer 2
    |
    V
Output layer
```

The following diagram illustrates the basic architecture of an autoencoder:

```
Input data
    |
    V
Encoder layer 1
    |
    V
Encoder layer 2
    |
    V
Latent representation
    |
    V
Decoder layer 1
    |
    V
Decoder layer 2
    |
    V
Output data
```

The following diagram illustrates the basic architecture of a GAN:

```
Noise vector
    |
    V
Generator
    |
    V
Fake data
    |       |
    V       V
Discriminator
    |       |
    V       V
Fake score  Real data
                |
                V
            Real score
```

The following diagram illustrates the basic architecture of a ResNet:

```
Input data
    |
    V
Layer 1
    |
    V
Layer 2
    |
    V
Layer 3
    |       |
    V       |
Layer 4    |
    |       |
    V       |
Layer 5    |
    |       |
    V       V
    +----->+
    |
    V
Output layer
```