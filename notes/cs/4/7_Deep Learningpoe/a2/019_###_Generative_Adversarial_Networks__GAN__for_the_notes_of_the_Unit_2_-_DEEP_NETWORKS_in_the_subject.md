 Here is the content in markdown format for the topic ### Generative Adversarial Networks (GAN) for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Generative Adversarial Networks (GAN)

GANs are a class of neural networks that pit two networks against each other to generate synthetic yet realistic images. They consist of two networks:

1. Generator network: Generates new images instance by instance. The goal is to generate images that match the real distribution.
2. Discriminator network: Evaluates the generated instances and classifies them as real or fake. The goal is to classify real and fake images correctly.

The training process involves an adversarial game, where the generator is learning to produce more and more realistic images, while the discriminator is learning to get better at distinguishing real and fake images. This adversarial process allows the generator to learn how to capture the underlying data distribution and generate sharp, varied images.

Advantages:

- Can generate photo-realistic images
- Generate images in a unsupervised manner without the need for large amounts of labeled data
- Have been applied to various applications like image generation, video generation, speech synthesis, etc.

Disadvantages:

- Training can be unstable and requires careful tuning of hyperparameters
- Does not have an explicit learning objective and hard to analyze why models fail
- Generated samples can be overly smooth or lack diversity

**Examples:**

- DCGAN: Deep Convolutional GAN. Uses CNNs for both generator and discriminator.
- CycleGAN: Transfers styles from one image to another (e.g. horse -> zebra)
- Pix2Pix: Translates input sketches to photo-realistic images

**Applications:**

- Generating images for data augmentation
- Synthesizing medical images
- Video generation and editing
- Text-to-image synthesis
- Super-resolution
- etc.