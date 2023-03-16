### Recurrent networks

- Recurrent networks are a type of artificial neural networks that can process sequential data or time series data, such as natural language, speech, or video .
- Recurrent networks have a "memory" that allows them to store information from previous inputs and use it to influence the current input and output .
- Recurrent networks can be unfolded in time to form a feedforward network with multiple layers, one for each time step .
- Recurrent networks can be trained using backpropagation through time (BPTT), which is a variant of backpropagation that updates the weights of the network based on the error gradients from all time steps .
- Recurrent networks can suffer from the vanishing or exploding gradient problem, which means that the error gradients can become very small or very large as they propagate through time, making the learning unstable or ineffective .
- Recurrent networks can be improved by using different architectures or variants, such as:
  - Long short-term memory (LSTM), which uses gated units to control the flow of information and avoid the vanishing gradient problem .
  - Gated recurrent unit (GRU), which is a simplified version of LSTM that uses fewer gates and parameters .
  - Bidirectional recurrent neural network (BRNN), which processes the input sequence from both directions and combines the outputs to enhance the representation .
  - Echo state network (ESN), which uses a large and randomly initialized recurrent layer that is not trained, and only trains the output layer .
  - Neural Turing machine (NTM), which uses an external memory and a controller to perform complex tasks that require reasoning and manipulation of symbols .