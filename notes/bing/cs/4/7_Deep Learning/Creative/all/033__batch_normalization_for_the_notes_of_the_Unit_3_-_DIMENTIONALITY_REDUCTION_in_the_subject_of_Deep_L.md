### Batch Normalization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly.
- Batch normalization involves two steps:
  - Calculating the mean and standard deviation of the inputs for each mini-batch.
  - Using the mean and standard deviation to normalize the inputs and adding two learnable parameters: a scale factor and an offset factor.
- Batch normalization can be implemented in Keras and TensorFlow 2 using the `BatchNormalization` layer.
- Batch normalization has some advantages and disadvantages:
  - Advantages:
    - It accelerates the training process by reducing the internal covariate shift, which is the change in the distribution of the inputs to a layer due to the updates of the previous layers.
    - It allows the use of higher learning rates and less careful initialization, as it reduces the sensitivity to the initial weights.
    - It reduces the need for other regularization techniques, such as dropout, weight decay, or L2 regularization, as it adds some noise to the inputs.
    - It improves the generalization performance of the model, as it reduces the overfitting to the training data.
  - Disadvantages:
    - It adds some computational complexity and runtime overhead to the model, as it requires extra calculations and parameters for each layer.
    - It may reduce the representational power of the network, as it constrains the inputs to a fixed distribution.
    - It may not work well with some activation functions, such as sigmoid or tanh, as they may saturate the inputs and make the normalization ineffective.
    - It may not be compatible with some architectures or tasks, such as recurrent neural networks or generative models, as they may require different normalization schemes or none at all.

- A possible mnemonic to remember the steps of batch normalization is: **M**ean and **S**tandard deviation, **N**ormalize and **S**cale, **O**ffset and **L**earn.
- A possible learning trick to understand the effect of batch normalization is to imagine a classroom of students taking a test. Without batch normalization, the test scores may vary widely depending on the difficulty of the test, the preparation of the students, and the grading of the teacher. With batch normalization, the test scores are standardized to have a mean of zero and a standard deviation of one, and then adjusted by a scale and an offset factor that are learned by the teacher. This way, the test scores are more comparable and consistent across different tests, students, and teachers.