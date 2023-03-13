The following diagram illustrates the basic architecture of a probabilistic deep learning model, based on the paper [A Probabilistic Theory of Deep Learning](^4^) by Patel, Nguyen and Baraniuk. The diagram is drawn using ASCII characters.

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Data space    |     |  Feature space |     |  Label space   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  x: data point |     |  z: feature    |     |  y: label      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  p(x)          |     |  p(z|x)        |     |  p(y|z)        |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Data          |     |  Encoder       |     |  Decoder       |
|  distribution  |     |  network       |     |  network       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  x ~ p(x)      | --> |  z ~ p(z|x)    | --> |  y ~ p(y|z)    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The diagram shows how a data point x is mapped to a feature z by an encoder network, and then to a label y by a decoder network. The encoder and decoder networks are deep neural networks that learn to approximate the conditional distributions p(z|x) and p(y|z), respectively. The data distribution p(x) is assumed to be given or known. The goal of probabilistic deep learning is to account for the uncertainty in both the data and the model, and to infer the posterior distributions of the latent variables and the model parameters.