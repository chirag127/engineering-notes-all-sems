 Here is the content in markdown format for the topic ### batch normalization for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### Batch Normalization

- Batch Normalization is a technique to normalize the input layer of a neural network.
- It scales and shifts the activations of the previous layer at each batch, i.e. at each training step.
- This has the effect of reducing internal covariate shift, which is a problem encountered during training of deep neural networks.
- Internal covariate shift refers to the change in the distribution of network activations due to the change in network parameters during training. This slows down the training process.
- Batch Normalization reduces internal covariate shift by making the activation distributions similar at the start of each batch. This speeds up the training process and makes the network more robust to variations in the input data.
- The benefits of Batch Normalization are:

- Faster training due to reduced need for careful parameter initialization and scaling of the inputs/activations.
- Higher accuracy due to less reliance on initialization.
- Acts as a regularizer, leading to less overfitting.
- Makes the network more robust to input variations and hence leads to better performance on unseen data.

- The outputs of the Batch Normalization layer are the normalized activations along with the parameters for scaling and shifting. These outputs are then used as inputs to the next layer in the network.
- During testing, we use the stored parameters to normalize and scale the activations. We don't recompute parameters at each batch during testing.
- Some potential disadvantages are:

- Additional hyperparameter tuning may be required to choose the decay rates for the exponential moving averages of parameters.
- The storage requirements are increased due to the parameters being stored. However, this is typically not a significant increase.
- The assumption that the activations are Gaussian may not always hold true.

- Overall, Batch Normalization is a very useful technique and is commonly used in modern deep neural networks to speed up training and improve performance.