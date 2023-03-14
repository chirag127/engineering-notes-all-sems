### LSTM for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning

- Long Short-Term Memory (LSTM) is a type of Recurrent Neural Network (RNN) that is specifically designed to handle sequential data, such as time series, speech, and text.
- LSTM can learn long-term dependencies and overcome the problems of vanishing and exploding gradients that affect standard RNNs .
- LSTM consists of memory cells that have an internal state and three multiplicative gates: input gate, forget gate, and output gate .
- The input gate decides whether to update the internal state with the current input and the previous hidden state.
- The forget gate decides whether to reset the internal state to zero.
- The output gate decides whether to allow the internal state to impact the cell's output.
- LSTM can be trained with full Backpropagation Through Time (BPTT) using matrix-based batch learning methods.
- LSTM can benefit from advanced optimization algorithms such as L-BFGS and CG methods that are not applicable for SGD methods.
- LSTM can be parallelized with computation architectures like CUDA and MapReduce to accelerate large-scale training.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the three gates of LSTM is **IFO** (input, forget, output), which sounds like **UFO** (unidentified flying object).
- A possible learning trick to understand the role of the gates is to imagine a memory cell as a suitcase that can store and retrieve information. The input gate is like a zipper that can open or close the suitcase. The forget gate is like a trash bin that can empty the suitcase. The output gate is like a lock that can prevent or allow access to the suitcase.