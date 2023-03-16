### Batch Normalization

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch  .
- It affects the output of the previous activation layer by subtracting the batch mean and dividing by the batch standard deviation .
- It reduces the internal covariate shift, which is the change in the distribution of layer inputs during training due to the change in parameters of previous layers.
- It has several advantages, such as:
  - It accelerates the training process by allowing higher learning rates and less careful initialization  .
  - It provides some regularization effect by adding noise to the layer inputs .
  - It makes the network less sensitive to the scale and shift of the input features .
- It has some drawbacks, such as:
  - It adds computational complexity and memory overhead to the network .
  - It introduces a dependence on the batch size and may not work well for small or variable batches .
  - It may not be compatible with some network architectures or optimization methods .