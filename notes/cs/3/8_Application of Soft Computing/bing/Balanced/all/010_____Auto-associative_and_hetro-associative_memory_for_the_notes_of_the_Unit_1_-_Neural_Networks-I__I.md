# Auto-associative and hetero-associative memory

- Auto-associative and hetero-associative memory are two types of associative memory in neural networks.
- Associative memory is the ability to recall a stored pattern given a partial or noisy input that is related to the pattern.
- Auto-associative memory retrieves the same pattern Y given an input pattern X, i.e., Y = X. It is also known as unidirectional memory or self-associative memory.
- Hetero-associative memory retrieves a stored pattern Y given an input pattern X such that Y ≠ X. It is also known as bidirectional memory or cross-associative memory.
- Auto-associative memory is used to simulate and explore the associative process and to perform error correction, pattern completion, and noise reduction.
- Hetero-associative memory is used to perform pattern recognition, classification, and mapping between different domains.
- The architecture of auto-associative memory consists of a single layer of neurons with recurrent connections, so that each neuron interlinks with several or even all of the other neurons in the set. A common example of auto-associative memory is the Hopfield network.
- The architecture of hetero-associative memory consists of two layers of neurons with feedforward connections, so that each input neuron is connected to every output neuron. A common example of hetero-associative memory is the Hebbian network.
- Auto-associative memory and hetero-associative memory are both based on the Hebbian learning rule, which states that the synaptic weight between two neurons is proportional to the product of their activity.
- Auto-associative memory and hetero-associative memory are both static in nature, hence, there are no non-linear and delay operations.