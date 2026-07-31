# Fully Connected Neural Network

- A fully connected neural network consists of a series of fully connected layers that connect every neuron in one layer to every neuron in another layer .
- A fully connected layer is a function from ℝ m to ℝ n that applies a linear transformation to the input vector through a weights matrix.
- The output of a fully connected layer is given by:

$$
\mathbf{y} = \mathbf{Wx} + \mathbf{b}
$$

where $\mathbf{x}$ is the input vector, $\mathbf{W}$ is the weights matrix, $\mathbf{b}$ is the bias vector, and $\mathbf{y}$ is the output vector.

- The major advantage of fully connected networks is that they are “structure agnostic” i.e. there are no special assumptions about the input data, such as spatial or temporal relationships.
- Fully connected networks can be used for any type of data that can be represented as a vector, such as images, text, audio, etc.
- The major disadvantage of fully connected networks is that they are prone to overfitting, especially when the input dimension is large, as they have a large number of parameters to learn.
- Fully connected networks also do not exploit any local features or patterns in the input data, such as edges or shapes in images, or words or phrases in text.
- Fully connected networks are often used as the final layer of a neural network, after applying other types of layers, such as convolutional or recurrent layers, that can extract more meaningful features from the input data .
- To define a fully connected neural network in PyTorch, we can use the `torch.nn.Linear` module, which implements a fully connected layer, and the `torch.nn.Sequential` module, which creates a container for a sequence of layers.
- For example, the following code defines a fully connected neural network with two hidden layers and one output layer:

```python
import torch
import torch.nn as nn

# Define the input size, hidden layer sizes, and output size
input_size = 784 # 28 x 28 pixels for MNIST images
hidden_sizes = [128, 64]
output_size = 10 # 10 classes for MNIST digits

# Define the network using torch.nn.Sequential
model = nn.Sequential(
    nn.Linear(input_size, hidden_sizes[0]), # First hidden layer
    nn.ReLU(), # Activation function
    nn.Linear(hidden_sizes[0], hidden_sizes[1]), # Second hidden layer
    nn.ReLU(), # Activation function
    nn.Linear(hidden_sizes[1], output_size) # Output layer
)

# Print the model
print(model)
```

- The output of the code is:

```python
Sequential(
  (0): Linear(in_features=784, out_features=128, bias=True)
  (1): ReLU()
  (2): Linear(in_features=128, out_features=64, bias=True)
  (3): ReLU()
  (4): Linear(in_features=64, out_features=10, bias=True)
)
```

- To train and test the model, we need to provide the input data, the target labels, the loss function, and the optimizer. We can use the `torch.nn.CrossEntropyLoss` module for the loss function, and the `torch.optim.SGD` module for the optimizer.
- For example, the following code trains the model for one epoch on the MNIST dataset, and evaluates its accuracy on the test set:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Define the batch size and the number of epochs
batch_size = 64
epochs = 1

# Define the data loaders for the train and test sets
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('data', train=True, download=True,
                   transform=transforms.ToTensor()),
    batch_size=batch_size, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('data', train=False, transform=transforms.ToTensor()),
    batch_size=batch_size, shuffle=True)

# Define the loss function and the optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Train the model for one epoch
for epoch in range(epochs):
    running_loss = 0.

```
