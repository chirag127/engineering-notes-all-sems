 Here is the content in markdown format for the topic ### Auto-associative and hetro-associative memory for the notes of the Unit 1 - Neural Networks-I (Introduction & Architecture) in the subject of Application of Soft Computing:

#### Auto-associative memory:
- An auto-associative memory is a type of artificial neural network which is trained to reproduce its own inputs at its output.
- It is composed of an input and an output layer with same number of nodes. The middle layer(s) provide the association between the inputs and outputs.
- During training, the network learns to associate the inputs with the corresponding outputs. After training, when a part of the input is provided, the auto-associative memory recalls and produces the complete input.
- It is used for tasks like noise removal, completing patterns, etc.

Advantages:
- Can be used to recreate complete input from partial input.
- Useful in noise removal as it learns to associate original input with clean output.

Disadvantages:
- May produce undesirable outputs if inputs are very different from training data.
- May not generalize well if overtrained on limited data.

#### Hetero-associative memory:
- A hetero-associative memory is an artificial neural network in which the input and output layers have different number of nodes.
- The input pattern is associated with the target output pattern during training. After training, when an input is provided, the network recalls the associated target output.
- It is used to associate inputs with corresponding outputs when the input-output mappings are not one-to-one.
- Examples: Speech recognition, machine translation, etc.

Advantages:
- Can be used for pattern classification problems where inputs and outputs are not of same dimensions.
- Useful for real-world problems like translations, speech recognition, etc. involving variable length input and output mappings.

Disadvantages:
- May produce undesirable outputs if inputs are very different from training data.
- May have issues with scalability due to "curse of dimensionality".

[Additional details, examples, diagrams, etc. can be added if required.]