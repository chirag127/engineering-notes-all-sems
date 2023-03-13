One of the common architectures for dimensionality reduction in deep learning is the autoencoder. An autoencoder is a type of neural network that learns to encode the input data into a lower-dimensional representation and then decode it back to the original data. The goal is to minimize the reconstruction error between the input and the output. The lower-dimensional representation can capture the essential features of the data and reduce the noise and redundancy.

The following diagram illustrates the basic architecture of an autoencoder:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|     Input      |    |    Encoder     |    |    Decoder     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  x1 x2 x3 x4  | -> |  h1 h2 h3 h4   | -> |  x1 x2 x3 x4   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The encoder is a function that maps the input data x to a hidden representation h, which has a lower dimensionality than x. The decoder is a function that maps the hidden representation h back to the input data x. The encoder and decoder can be implemented as feedforward neural networks, convolutional neural networks, recurrent neural networks, or other types of deep learning models.

There are different types of autoencoders, such as sparse autoencoders, denoising autoencoders, variational autoencoders, and generative adversarial autoencoders, that have different objectives and applications. Autoencoders can be used for data compression, noise reduction, feature extraction, anomaly detection, image generation, and more.