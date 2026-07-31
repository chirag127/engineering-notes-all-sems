# Auto-associative and hetero-associative memory

- Auto-associative memory and hetero-associative memory are two types of associative memory networks that can store and retrieve patterns based on their similarity or association.
- Associative memory networks are artificial neural networks that can learn to associate input patterns with output patterns, and recall the output patterns when given the input patterns or their partial or noisy versions.
- Auto-associative memory retrieves the same pattern Y given an input pattern X, i.e., Y = X . It is also known as auto-association memory or an autoassociation network.
- Hetero-associative memory retrieves the stored pattern Y given an input pattern X such that Y ≠ X . It is also known as hetero-association memory or a hetero-associative correlator.
- Auto-associative memory is useful for de-noising or removing interference from the input and for determining whether the given input is “known” or “unknown”.
- Hetero-associative memory is useful for mapping input patterns to output patterns that are different in size, type, format or content .
- Auto-associative memory can be implemented by a single-layer neural network with symmetric weights, such as the Hopfield network  .
- Hetero-associative memory can be implemented by a two-layer neural network with asymmetric weights, such as the bidirectional associative memory (BAM) network .