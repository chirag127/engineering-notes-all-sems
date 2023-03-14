### Generative Adversarial Networks (GAN) for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

Generative Adversarial Networks (GAN) is a powerful deep learning technique that is used to generate new data based on a given dataset. It is a type of unsupervised learning and was introduced by Ian Goodfellow and his colleagues in 2014. GANs have gained a lot of popularity in recent years due to their ability to generate realistic synthetic data.

#### How GAN works?

GAN consists of two neural networks, a generator and a discriminator, that work together in a competitive manner. The generator network takes a random noise vector as input and generates a new data sample that is similar to the training data. The discriminator network takes both real and generated data as input and tries to distinguish between them.

During the training process, the generator tries to generate data that can fool the discriminator, while the discriminator tries to correctly identify real and fake data. The generator and discriminator network are trained together using backpropagation and gradient descent. The goal is to find a balance between the generator generating realistic samples and the discriminator being able to correctly distinguish between real and fake samples.

#### Advantages of GAN

- GAN can generate new data that is similar to the training data, which can be used for data augmentation and improve the performance of other machine learning models.
- GAN can be used to generate synthetic data for domains where collecting real data is difficult or expensive, such as medical imaging or satellite imagery.
- GAN can be used for image and video synthesis, such as generating realistic images of faces, landscapes, and objects.

#### Disadvantages of GAN

- GAN can be difficult to train, and finding the right balance between the generator and discriminator networks can be challenging.
- GAN can suffer from mode collapse, where the generator produces a limited set of outputs that do not represent the full diversity of the training data.
- GAN can produce synthetic data that is biased or contains artifacts, which can affect the performance of downstream machine learning models.

#### Mnemonics and Learning Tricks

- Remember that the generator tries to generate data that can fool the discriminator, while the discriminator tries to correctly identify real and fake data.
- Think of GAN as a game between two players, where the generator and discriminator are playing against each other to improve their performance.
- Visualize the training process as a dance between the generator and discriminator, where they are constantly trying to outsmart each other.