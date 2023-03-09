 Here are the notes on Recurrent Neural Networks for the topic Neural Networks - I (Introduction & Architecture) in the given format:

### Recurrent Neural Networks

- Recurrent Neural Networks are a type of neural networks wherein the output from previous timesteps are fed as inputs to the current timestep. This creates a loop and enables the network to retain 'memory' of previous inputs and influence the current output.
- The recurrent connections between timesteps allow the network to process sequential data and learn temporal patterns. This makes RNNs suitable for tasks like time series forecasting, speech recognition, machine translation, etc.
- The basic architecture of an RNN consists of an input layer, a hidden layer and an output layer. The hidden layer has a recurrent connection where the output is fed back as input. The error from the current timestep is backpropagated through this loop to update the weights and learn the temporal patterns.
- Training RNNs is difficult due to the problem of vanishing and exploding gradients. As the gradient is backpropagated through many timesteps, it can either exponentially decay or explode making training unstable. Solutions to address this include LSTM, GRU units and gradient clipping.
- LSTM (Long Short Term Memory) units are a type of recurrent units that have a more complex structure with cell states and gates to regulate the flow of information. This helps preserve the gradient for longer periods and makes training deep RNNs feasible. LSTMs have achieved state-of-the-art results in many sequence modeling problems.
- Some advantages of RNNs are:
    - Able to retain memory and process sequential data
    - Can learn complex temporal dependencies and patterns
- Some disadvantages are:
    - Difficult to train due to exploding/vanishing gradient problem
    - Require large amounts of training data
- RNNs have a wide range of applications like time series forecasting, machine translation, speech recognition, sentiment analysis, etc. Due to their sequential nature, they are best suited for sequence modeling problems.

[Diagrams and code snippets can be added here for visualization and clarity]