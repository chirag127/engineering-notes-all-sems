 Here is the content in markdown format:

### ResNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- ResNet (Residual Network) is a type of feed-forward neural network used in deep learning that solves the degradation problem.
- The degradation problem refers to the accuracy of a network decreasing as we increase the depth of the network. This happens due to the vanishing gradient problem.
- ResNet solves this by introducing skip connections that bypass some layers. These skipped layers are called residual blocks.
- A residual block has two paths -

1. The activation path - containing a few convolutional layers
2. The identity shortcut path - directly connecting the input to the output

- The output of the two paths is added together and fed as input to the next layer.
- This allows the gradient to flow even through the deeper layers and prevents overfitting, thereby increasing the accuracy even for very deep networks (100+ layers).
- Some tips to remember ResNet:

Mnemonics: Skip the layers, Sum the paths
Shortcut the identity
Bypass the vanish

- Advantages: Solves degradation problem, can train very deep networks, state-of-the-art accuracy.
- Disadvantages: Complex architecture, requires more training time and parameters.
- Applications: Image classification, Object detection, Semantic segmentation, etc.

[Detailed diagrams and codes can be added here for better understanding]

Hope this helps! Let me know if you would like me to explain anything in more detail.