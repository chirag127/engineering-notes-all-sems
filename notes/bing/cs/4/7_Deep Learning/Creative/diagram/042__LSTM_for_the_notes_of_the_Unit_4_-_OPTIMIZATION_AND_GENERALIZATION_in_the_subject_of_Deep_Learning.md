The following text and diagram illustrate the basic architecture of a LSTM unit for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning.

A LSTM unit is composed of a cell, an input gate, an output gate and a forget gate. The cell stores the long-term memory of the unit, while the gates control the flow of information into and out of the cell. The gates are implemented as sigmoid neural network layers and pointwise multiplication operations.

The input gate decides which values from the input and the previous hidden state are relevant to update the cell state. The forget gate decides which values from the cell state are no longer needed and should be erased. The output gate decides which values from the cell state are useful to output as the current hidden state.

The diagram below shows the structure of a LSTM unit, where x_t is the input at time step t, h_t is the hidden state at time step t, c_t is the cell state at time step t, and * denotes the pointwise multiplication operation.

```
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|