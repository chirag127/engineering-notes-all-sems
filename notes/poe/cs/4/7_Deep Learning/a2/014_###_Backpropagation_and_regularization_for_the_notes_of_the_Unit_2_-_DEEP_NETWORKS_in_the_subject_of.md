 Here is the content in markdown format for the topic ### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning:

### Backpropagation and regularization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Backpropagation is a method used in training artificial neural networks for supervised learning. It involves propagating the error from the output layer back to the inner layers and updating the weights to minimise the loss function.
- It calculates the gradient of the loss function with respect to the weights and uses gradient descent to update the weights and minimise the loss.
- Regularization is a technique to prevent overfitting in neural networks. It adds a penalty term to the loss function to constrain the complexity of the model. Some common regularization techniques are:
-- L1 regularization: Adds absolute value of magnitude of weights to the loss. Results in sparse weights (many weights become zero).
-- L2 regularization: Adds square of magnitude of weights to the loss. Results in smaller weights spread out.
-- Dropout: Randomly drops out (sets to zero) a number of output features of the layer during training. This prevents co-adaptation of features.

**Mnemonics:**
- "Backprop calculates gradients and updates weights to minimise loss."
- "Reg prevents overfitting by constraining complexity (L1, L2, Dropout)."

**Advantages:**
- Backpropagation is efficient and enables training of multilayer neural networks.
- Regularization improves generalisation and reduces overfitting.

**Disadvantages:**
- Backpropagation can be unstable and lead to exploding/vanishing gradients.
- Regularization hyperparameters need to be tuned and can lead to underfitting if chosen incorrectly.

**Applications:**
- Backpropagation is fundamental to training all modern deep neural networks.
- Regularization is applied in almost all practical deep learning implementations to improve performance.

Does this help? Let me know if you would like me to explain or add anything further.