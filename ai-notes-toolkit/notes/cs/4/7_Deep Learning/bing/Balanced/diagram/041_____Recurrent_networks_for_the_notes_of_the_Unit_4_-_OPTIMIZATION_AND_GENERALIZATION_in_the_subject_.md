### Recurrent networks

- Recurrent networks are a type of artificial neural networks that can process sequential data or time series data  .
- Recurrent networks have a **memory** that allows them to store information from previous inputs and use it to influence the current input and output .
- Recurrent networks are commonly used for ordinal or temporal problems, such as language translation, natural language processing, speech recognition, and image captioning  .
- Recurrent networks can be classified into different types based on their architecture, such as:
  - Fully recurrent networks: every node is connected to every other node in both directions.
  - Elman networks and Jordan networks: two types of simple recurrent networks that have a hidden layer with feedback connections.
  - Hopfield networks: a type of recurrent network that can store and retrieve patterns as fixed points of the network dynamics.
  - Echo state networks: a type of recurrent network that has a large and randomly initialized hidden layer that is not trained, but only provides a rich dynamic reservoir of features.
  - Independently recurrent networks: a type of recurrent network that has independent recurrent connections for each neuron in the hidden layer, avoiding the vanishing or exploding gradient problem.
  - Recursive networks: a type of recurrent network that can process hierarchical or tree-structured data, such as natural language syntax or scene graphs.
  - Neural history compressor: a type of recurrent network that can compress sequential data into a fixed-length representation by using a stack-like memory.
  - Second order recurrent networks: a type of recurrent network that can model higher-order temporal dependencies by using multiplicative interactions between the hidden units.
  - Long short-term memory networks: a type of recurrent network that can learn long-term dependencies by using a special type of memory cell that has a forget gate, an input gate, and an output gate .
  - Gated recurrent unit networks: a type of recurrent network that is a simplified version of LSTM networks, with only two gates: a reset gate and an update gate .
  - Bi-directional recurrent networks: a type of recurrent network that can access both past and future information by using two hidden layers that process the input sequence in opposite directions .
  - Continuous-time recurrent networks: a type of recurrent network that can model continuous-time dynamics by using differential equations to describe the evolution of the hidden units.