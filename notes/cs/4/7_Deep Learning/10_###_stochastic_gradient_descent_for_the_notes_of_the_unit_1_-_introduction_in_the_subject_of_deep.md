### stochastic gradient descent for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning

Stochastic Gradient Descent (SGD) is a optimization algorithm used in deep learning to update the parameters of a model in an iterative manner. It is a form of gradient descent, which is a optimization technique that involves computing the gradient of the loss function with respect to the model parameters and updating the parameters in the direction of the negative gradient.

In SGD, the gradient is computed for a single training example at a time, rather than for the entire training set. This makes the algorithm computationally efficient and allows it to be used for large datasets.

The update rule for SGD is given by:

θ = θ - η * ∇θL(θ)

where θ is the model parameters, η is the learning rate, and L(θ) is the loss function for the model.

SGD has several variants, including Mini-batch SGD, where the gradient is computed for a small batch of training examples at a time, and Momentum SGD, where the update rule is modified to include a momentum term that helps the algorithm converge faster.

SGD is widely used in deep learning and has been shown to be effective for training deep neural networks on a variety of tasks, such as image classification, natural language processing, and reinforcement learning.

It is important to choose an appropriate learning rate and to monitor the convergence of the algorithm to ensure that the model parameters are updated in an effective manner.
