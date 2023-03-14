### Generative Adversarial Networks (GAN) for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- A generative adversarial network (GAN) is a deep neural network framework which is able to learn from a set of training data and generate new data with the same characteristics as the training data.
- For example, a GAN trained on photographs of human faces can generate realistic-looking faces which are entirely fictitious.
- GANs consist of two neural networks, the generator and the discriminator, which compete against each other in a zero-sum game .
- The generator is trained to produce fake data, and the discriminator is trained to distinguish the generator’s fake data from real examples .
- If the generator produces fake data that the discriminator can easily recognize as implausible, such as an image that is clearly not a face, the generator is penalized .
- Over time, the generator learns to generate more plausible examples .
- The discriminator is a binary classifier, which outputs the probability of the input being real or fake .
- The discriminator’s input may come from two sources: the training set, such as real photos of faces, or real audio recordings; or the generator, such as generated synthetic faces, or fake audio recordings .
- The generator and the discriminator are trained alternately, using the backpropagation algorithm through the whole system .
- The training process stops when the generator’s outputs are so realistic, that the discriminator is unable to distinguish them from the real examples .

- A possible mnemonic to remember the components of a GAN is: **G**AN = **G**enerator + **A**dversary + **N**etwork.
- A possible learning trick to understand the concept of a GAN is to imagine a forger and a detective playing a game of deception.
- The forger tries to create fake paintings that look like the originals, and the detective tries to spot the fakes among the real ones.
- The forger and the detective both improve their skills over time, until the forger can produce perfect replicas that the detective cannot tell apart from the originals.
- The forger is analogous to the generator, and the detective is analogous to the discriminator.

- A possible ascii diagram to illustrate the architecture of a GAN is:

```
  +----------------+     +----------------+     +----------------+
  |                |     |                |     |                |
  |  Random noise  |---->|   Generator    |---->|  Discriminator |
  |                |     |                |     |                |
  +----------------+     +----------------+     +----------------+
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
                                        |     |
  +----------------+     +----------------+     |
  |                |     |                |     |
  |  Real data     |---->|  Training set  |-----+
  |                |     |                |
  +----------------+     +----------------+
```

- A possible code snippet to implement a simple GAN in MATLAB is:

```matlab
% Define the generator network
layersGenerator = [
    imageInputLayer([1 1 100],'Normalization','none','Name','in')
    transposedConv2dLayer(4,20,'Stride',1,'Name','tconv1')
    batchNormalizationLayer('Name','bn1')
    reluLayer('Name','relu1')
    transposedConv2dLayer(3,20,'Stride',2,'Cropping',1,'Name','tconv2')
    batchNormalizationLayer('Name','bn2')
    reluLayer('Name','relu2')
    transposedConv2dLayer(5,1,'Stride',2,'Cropping',2,'Name','tconv3')
    tanhLayer('Name','tanh1')];
lgraphGenerator = layerGraph(layersGenerator);