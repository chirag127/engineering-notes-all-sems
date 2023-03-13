A Generative Adversarial Network (GAN) is a deep learning architecture that consists of two neural networks competing against each other in a zero-sum game framework. The goal of GANs is to generate new, synthetic data that resembles some known data distribution.

The following diagram illustrates the basic architecture of a GAN:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|    Real Data   |     |    Generator   |     |   Discriminator|
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +--------------------->+                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      +--------------------->+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +--------------------->+                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +<---------------------+<---------------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |

```

The GAN has two components: the generator and the discriminator  .

- The generator learns to produce realistic fake data from a random seed. The fake examples produced by the generator are used as negative examples for training the discriminator.
- The discriminator learns to distinguish between real and fake data. The discriminator is trained on both real data (positive examples) and fake data (negative examples) generated by the generator. The discriminator tries to maximize the probability of correctly classifying the data, while the generator tries to minimize that probability (or equivalently, maximize the probability of fooling the discriminator) .

The generator and the discriminator are trained alternately in a minimax game, where the generator tries to minimize the objective function and the discriminator tries to maximize it . The objective function can be written as:

```
min_G max_D V(D, G) = E_x~p_data(x)[log D(x)] + E_z~p_z(z)[log(1 - D(G(z)))]
```

where `x` is the real data, `z` is the random seed, `p_data` is the data distribution, `p_z` is the seed distribution, `D` is the discriminator, `G` is the generator, and `E` is the expectation operator