### Generative Adversarial Networks (GAN)

- Generative Adversarial Networks (GANs) are a type of deep neural network that can generate new data instances that resemble the training data   .
- GANs consist of two sub-models: a generator and a discriminator  .
  - The generator takes a random input (called noise or latent vector) and produces a fake data instance (such as an image)   .
  - The discriminator takes a real or a fake data instance and tries to classify it as real or fake   .
- The generator and the discriminator are trained in an adversarial manner, meaning that they compete against each other   .
  - The generator tries to fool the discriminator by generating realistic data instances   .
  - The discriminator tries to distinguish between real and fake data instances   .
- The training process stops when the generator and the discriminator reach an equilibrium, where the discriminator cannot tell the difference between real and fake data instances   .
- GANs can be used for various applications, such as image synthesis, image editing, image super-resolution, style transfer, text generation, etc.   .
- GANs can be extended and modified in various ways, such as using convolutional layers, adding regularization terms, changing the loss functions, using different architectures, etc.    .