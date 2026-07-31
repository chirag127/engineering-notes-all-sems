### Artificial Neuron and its model

An artificial neuron is a mathematical function that models the functioning of a biological neuron. It is the basic unit of an artificial neural network. The artificial neuron receives one or more inputs and sums them to produce an output. The inputs can be weighted, which means that the importance of each input can be adjusted. The output is then calculated by applying an activation function to the weighted sum of the inputs.

The model of an artificial neuron consists of the following components:

1. **Inputs:** These are the values that are fed into the neuron. They can be the raw data or the outputs from other neurons.

2. **Weights:** These are the values that determine the importance of each input. They can be adjusted during the training process to improve the performance of the neural network.

3. **Bias:** This is an additional input that is always set to 1. It allows the neuron to shift the activation function left or right.

4. **Activation function:** This is a mathematical function that is applied to the weighted sum of the inputs. It determines the output of the neuron. Common activation functions include the sigmoid, hyperbolic tangent, and rectified linear unit (ReLU) functions.

5. **Output:** This is the result of applying the activation function to the weighted sum of the inputs. It is the value that is passed on to the next layer of neurons or to the output of the neural network.

In summary, an artificial neuron receives inputs, multiplies them by their respective weights, adds a bias, applies an activation function, and produces an output. This process is often referred to as the forward pass of the neural network. During the training process, the weights and bias are adjusted to improve the performance of the neural network. This is known as the backward pass or backpropagation.