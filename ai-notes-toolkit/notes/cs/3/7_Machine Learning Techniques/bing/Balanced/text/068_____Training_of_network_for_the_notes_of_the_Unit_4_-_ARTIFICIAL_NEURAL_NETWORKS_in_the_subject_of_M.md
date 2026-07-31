### Training of network for the notes of the Unit 4 - ARTIFICIAL NEURAL NETWORKS in the subject of Machine Learning Techniques

- Artificial neural networks (ANNs) are computational models inspired by the structure and function of biological neurons.
- ANNs consist of interconnected units called artificial neurons, which process information and transmit signals to other neurons.
- ANNs can learn from data and perform tasks such as classification, regression, clustering, pattern recognition, etc.
- Training an ANN involves adjusting the weights of the connections between neurons, so that the network can produce the desired output for a given input.
- Training an ANN requires the following steps :
  - First, an ANN will require a random weight initialization.
  - Split the dataset in batches (batch size).
  - Send the batches one by one to the GPU.
  - Calculate the forward pass (what would be the output with the current weights).
  - Compare the calculated output to the expected output (loss).
  - Adjust the weights (using the learning rate increment or decrement) according to the backward pass (backward gradient propagation).
  - Repeat the process until the loss is minimized or a certain number of iterations (epochs) is reached.
- There are different types of ANNs, such as feedforward neural networks, recurrent neural networks, convolutional neural networks, etc., which have different architectures and applications.
- ANNs are used in various domains, such as computer vision, natural language processing, speech recognition, bioinformatics, etc. 
- ANNs are also the basis of deep learning, which is a subfield of machine learning that uses multiple layers of neurons to learn complex and abstract features from data.