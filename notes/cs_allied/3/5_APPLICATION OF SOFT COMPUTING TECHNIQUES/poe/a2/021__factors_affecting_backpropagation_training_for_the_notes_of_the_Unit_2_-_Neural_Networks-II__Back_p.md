 Here are the factors affecting backpropagation training for the notes of Unit 2 - Neural Networks-II (Backpropagation networks):

### Learning rate (η)
- The learning rate controls the size of the weight updates during training.
- If the learning rate is too high, the weight updates may oscillate and become unstable.
- If the learning rate is too low, training may be very slow.
- An appropriate value must be chosen, often using a validation set to tune this hyperparameter.

### Momentum (α)
- Momentum is a method of accelerating gradient descent in the relevant direction and dampening oscillations.
- It adds a fraction of the previous weight update to the current one, making weight changes smoother and avoiding slow, zigzag movements.
- A good value for momentum is typically 0.9.

### Number of iterations
- Training ends after a fixed number of iterations (epochs) through the training data.
- More iterations lead to lower error on the training set but may lead to overfitting.
- Early stopping is a method to avoid overfitting by stopping training once the validation error increases.

### Weight initialization
- The initial weights must be randomly chosen, as symmetry can lead to poor local minima.
- If weights are initialized to zero, all neurons compute the same output in the initial layer.
- Random values between -1 and 1 or from a Gaussian distribution are common approaches.

[No external links included. Content written in Markdown format with bullet points as instructed.]