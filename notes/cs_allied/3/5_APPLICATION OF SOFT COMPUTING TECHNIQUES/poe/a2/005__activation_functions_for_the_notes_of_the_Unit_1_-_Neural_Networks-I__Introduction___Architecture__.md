 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Activation Functions

- Sigmoid Function: It is an S-shaped function that squashes the output between 0 and 1. It is defined as 1/(1+e^(-x)). It is differentiable everywhere and hence used in the hidden layers of a neural network. However, it suffers from the saturation problem as the gradient becomes very small near the extremes.
- Hyperbolic Tangent Function: It is similar to the sigmoid function but the output range is from -1 to 1. It is defined as (e^x - e^-x)/(e^x + e^-x). It avoids the saturation problem but is computationally more expensive than the sigmoid function.
- ReLU Function: It is the Rectified Linear Unit which returns 0 if the input is negative and the input as it is if the input is positive. It is defined as max(0,x). It is non-saturating and computationally efficient. However, it is not differentiable at 0 and can result in the problem of dying ReLU if the weights are not initialized properly.
- Leaky ReLU: It is a modified form of the ReLU function that has a small negative slope for negative input. It is defined as max(ax,x) where a < 1. It fixes the non-differentiability problem of ReLU and avoids the dying ReLU problem. It performs better than ReLU for training deep neural networks.

The points are written in a formal style with no feelings or friendliness shown as required. The content is written inside the specified header for the given topic which is activation functions for the notes of Unit 1 - Neural Networks-I. Let me know if you would like me to modify or expand the content.