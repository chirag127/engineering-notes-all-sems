A recurrent neural network language model (RNNLM) is a type of neural network language model that uses recurrent neural networks (RNNs) to model the sequential data such as sentences in natural language. RNNs are neural networks that can process variable length inputs and have a memory that can store information from previous computations. RNNLMs can learn long-term dependencies and capture the context of words in a sentence.

The following diagram illustrates the basic architecture of a RNNLM:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Embedding     |    |   Embedding     |    |   Embedding     |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     RNN         |    |     RNN         |    |     RNN         |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Softmax       |    |   Softmax       |    |   Softmax       |
|                 |    |                 |    |                 |
+--------+--------+    +--------+--------+    +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Output        |    |   Output        |    |   Output        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The RNNLM takes a sequence of words as input and outputs a probability distribution over the next word in the sequence. Each word is first mapped to a vector representation using an embedding layer. Then, the vector is fed into an RNN layer, which updates its hidden state based on the previous hidden state and the current input. The hidden state is then passed to a softmax layer, which computes the probability of each word in the vocabulary as the next word. The output of the softmax layer is compared with the actual next word using a loss function, such as cross-entropy, and the parameters of the model are updated using an optimization algorithm, such as gradient descent.

The RNNLM can be trained on a large corpus of text to learn the statistical patterns of natural language. It can also be used to generate text by sampling words from the output distribution at each time step. RNNLMs can achieve better performance than traditional n-gram language models, which rely on a fixed window of previous words to predict the next word. However, RNNLMs also have some limitations, such as the difficulty of handling long-term dependencies, the vanishing or exploding gradient problem, and the high computational cost.