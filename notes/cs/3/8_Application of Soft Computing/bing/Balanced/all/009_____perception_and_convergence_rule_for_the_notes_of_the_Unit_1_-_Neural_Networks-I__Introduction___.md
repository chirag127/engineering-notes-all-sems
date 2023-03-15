# Perception and Convergence Rule

- A perceptron is a kind of a single-layer artificial neural network with only one neuron.
- A perceptron is a simplified model of the biological neurons in our brain.
- A perceptron calculates the linear combination of its real-valued or boolean inputs and passes it through a threshold activation function.
- A perceptron can be used for binary classification tasks, such as determining whether an input belongs to one class or another.
- The perceptron learning rule is an algorithm that updates the weights of the perceptron based on the errors made on the training data.
- The perceptron convergence theorem states that for any data set which is linearly separable, the perceptron learning rule is guaranteed to find a solution in a finite number of steps.
- The perceptron convergence theorem can be proved by showing that the squared distance between the optimal weight vector and the current weight vector decreases monotonically after each update.
- The perceptron convergence theorem does not hold if the data set is not linearly separable, in which case the perceptron learning rule may never converge or oscillate indefinitely.
- A common variant of the basic perceptron algorithm is the averaged perceptron, which uses the average of the weight vectors over all the updates instead of the final weight vector.
- The averaged perceptron has better generalization performance and can be verified using a similar proof technique as the basic perceptron.
- A recent extension of the perceptron is the deep neural network with controllable rule representations (DeepCTRL), which incorporates a rule encoder into the model coupled with a rule-based objective, enabling a shared representation for decision making.
- DeepCTRL is agnostic to data type and model architecture, and can be applied to any kind of rule defined for inputs and outputs.
- DeepCTRL can learn from both rule-based and data-driven supervision, and can control the trade-off between rule compliance and data fit.