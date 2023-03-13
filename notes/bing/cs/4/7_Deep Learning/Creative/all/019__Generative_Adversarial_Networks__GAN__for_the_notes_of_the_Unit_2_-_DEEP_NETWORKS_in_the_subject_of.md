### Generative Adversarial Networks (GAN) for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- A generative adversarial network (GAN) is a class of machine learning frameworks designed by Ian Goodfellow and his colleagues in June 2014.
- A GAN consists of two neural networks: a generator and a discriminator, that compete with each other in a zero-sum game, where one agent's gain is another agent's loss.
- The generator tries to create new data instances that resemble the training data, while the discriminator tries to distinguish between real and fake data.
- The generator and the discriminator are trained simultaneously using a minimax game, where the generator tries to minimize the discriminator's accuracy, and the discriminator tries to maximize it.
- The training process stops when the generator and the discriminator reach a Nash equilibrium, where neither agent can improve its strategy by changing its parameters.
- GANs are generative models, meaning they can learn the probability distribution that generated the training data, and use it to sample new data.
- GANs can generate realistic and diverse data, such as images, text, audio, and video, from a random noise input.
- GANs have many applications, such as image synthesis, image editing, image super-resolution, image inpainting, style transfer, text generation, speech synthesis, video generation, and anomaly detection.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the names and roles of the two neural networks in a GAN is: **G**enerator **G**enerates, **D**iscriminator **D**etects.
- A possible learning trick to understand the minimax game between the generator and the discriminator is to imagine a counterfeiter and a police officer. The counterfeiter tries to make fake money that looks like real money, and the police officer tries to catch the fake money. The counterfeiter wants to fool the police officer, and the police officer wants to catch the counterfeiter. The game ends when the counterfeiter makes perfect money, or the police officer gives up.