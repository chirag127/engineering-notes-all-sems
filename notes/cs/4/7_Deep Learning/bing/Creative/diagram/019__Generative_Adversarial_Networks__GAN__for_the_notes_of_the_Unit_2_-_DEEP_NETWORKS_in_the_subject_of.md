A generative adversarial network (GAN) is a deep learning architecture that consists of two neural networks competing against each other in a zero-sum game framework. The goal of GANs is to generate new, synthetic data that resembles some known data distribution.

A GAN has two main components: the generator and the discriminator.

- The generator learns to produce realistic fake data from a random seed. The fake examples produced by the generator are used as negative examples for training the discriminator.
- The discriminator learns to distinguish the generator's fake data from real data. The discriminator penalizes the generator for producing implausible results.

The following diagram illustrates the basic architecture of a GAN using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Random seed   +---->+   Generator    +---->+   Fake data    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 |
                                                 v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Real data    +---->+  Discriminator +<----+  Fake data     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         v
+----------------+
|                |
|  Loss signal  |
|                |
+----------------+
```

The generator output is connected directly to the discriminator input. Through backpropagation, the discriminator's classification provides a signal that the generator uses to update its weights.

There are many variations of GANs that use different architectures, loss functions, and training strategies. Some examples are DCGAN, StyleGAN, CycleGAN, and WGAN.