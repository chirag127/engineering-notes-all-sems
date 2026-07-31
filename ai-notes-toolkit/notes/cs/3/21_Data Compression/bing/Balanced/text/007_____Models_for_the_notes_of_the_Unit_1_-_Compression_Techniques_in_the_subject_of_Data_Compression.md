### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques discard some information that is deemed less important or perceptually irrelevant.
- Data compression can be achieved by using different models and coders.
- A model is a component that captures the probability distribution of the data by knowing or discovering something about the structure of the input.
- A coder is a component that encodes the data based on the model, using fewer bits for more probable symbols and more bits for less probable symbols.
- Some of the popular model compression techniques are:

  - Pruning: Pruning is a technique that reduces the number of parameters in a deep neural network by removing redundant and inconsequential connections, neurons, channels, or layers . Pruning can improve the efficiency and generalization of the network, as well as reduce the risk of overfitting.
  - Quantization: Quantization is a technique that reduces the precision of the weights and activations in a deep neural network by using fewer bits to represent them, such as 8-bit or 16-bit integers instead of 32-bit floating point numbers . Quantization can reduce the memory and computational requirements of the network, as well as the energy consumption and latency.
  - Knowledge distillation: Knowledge distillation is a technique that transfers the knowledge from a large, complex model (teacher) to a smaller, simpler model (student) by training the student to mimic the output of the teacher . Knowledge distillation can preserve the accuracy of the network while reducing the size and complexity.
  - Low-rank factorization: Low-rank factorization is a technique that decomposes a large, dense matrix (such as a weight matrix or a convolutional kernel) into a product of two smaller, sparse matrices with lower rank . Low-rank factorization can reduce the number of parameters and operations in the network, as well as the storage and bandwidth requirements.