 Here is the content in markdown format:

### ResNet for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

ResNet (Residual Network) is a type of neural network architecture proposed by Kaiming He et al. in 2015. It solves the problem of degradation in deep neural networks by introducing skip connections that bypass some layers. The key insight is that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping.

**Architecture:** ResNet contains shortcut connections that skip one or more layers. These shortcuts help to combat the vanishing gradient problem by strengthening the gradient flow. The architecture allows for considerably deeper networks that can achieve higher accuracy.

**Identity mapping:** The identity shortcut connections simply perform identity mapping y = x, which passes the input directly to the output without any parameter changes. This serves as a baseline or control case for the neural network to check against. If the stack of layers cannot improve on the identity mapping, it collapses to this simple baseline. This makes training more stable and robust.

**Difference shortcut:** The difference shortcut connections project the input into a different space before adding to the output of the stack of layers. This allows the network to learn more complex mappings that cannot be modeled by the identity function. The projection may change the dimensionality or number of channels before adding to the output of the layers.

**Benefits:**
- Allows considerably deeper networks to be trained which improves accuracy.
- Identity mapping provides a baseline for optimization and more stable training.
- Overcomes vanishing gradient problem through strengthened gradient flow via skip connections.
- Outperforms plain stacked networks on image classification tasks.

**Disadvantages:**
- Additional parameters and complexity from the shortcut connections.
- Identity mapping may be overused and restrict representational power.
- Challenging to train due to instability from fast gradient flow. Requires careful tuning of hyperparameters and optimization.

**Applications:** Image classification, Object detection, Segmentation, Super-resolution, etc. ResNet has become a foundation for many modern computer vision models due to its excellent performance and adaptability.