

## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data without losing essential information.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for applications that require high fidelity, such as text, audio, and images.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for applications that can tolerate some degradation, such as video, speech, and music.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): Replaces consecutive identical symbols with a symbol and a count.
  - Huffman coding: Assigns variable-length codes to symbols based on their frequencies.
  - Lempel-Ziv-Welch (LZW): Builds a dictionary of common patterns and encodes them with fixed-length codes.
- Some common lossy compression techniques are:
  - Transform coding: Applies a mathematical transform to the data and quantizes the coefficients.
  - Vector quantization: Divides the data into blocks and maps them to a set of representative vectors.
  - Differential coding: Encodes the difference between successive samples or frames.



### Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values are more likely than others, or that some data values can be predicted from other data values.
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, and medical imaging  .
- Lossless compression techniques include:
  - Run-length encoding: a simple method that replaces consecutive identical data values with a single value and a count of how many times it occurs.
  - Huffman coding: a variable-length coding method that assigns shorter codes to more frequent data values and longer codes to less frequent data values.
  - Lempel-Ziv coding: a dictionary-based coding method that exploits the repetition of patterns in the data by storing references to previously encountered patterns instead of the actual data values.
  - Arithmetic coding: a coding method that assigns codes to data values based on their probabilities, using a single arithmetic operation to generate the compressed data.
- Lossless compression can achieve compression ratios of up to 8:1, depending on the data and the compression algorithm .
- Lossless compression is different from lossy compression, which discards some data in the compression process, resulting in a loss of quality and information in the decompressed data  . Lossy compression is more suitable for applications that can tolerate some degradation, such as video and image compression .



### Lossy Compression

- Lossy compression is a type of data compression that reduces the size of the data by discarding some information that is not essential or perceptible to the human senses.
- Lossy compression is useful for applications that can tolerate some degradation in quality, such as audio, video, and image compression.
- Lossy compression can achieve higher compression ratios than lossless compression, but at the cost of losing some fidelity or accuracy of the original data.
- Lossy compression techniques are based on the concept of **psychoacoustics** and **psychovisuals**, which are the study of how humans perceive sound and vision, respectively.
- Psychoacoustics and psychovisuals exploit the limitations and characteristics of the human auditory and visual systems, such as masking, threshold, frequency response, and spatial resolution, to remove or reduce the information that is less noticeable or important to the human perception.
- Some examples of lossy compression algorithms are:
  - **MP3** and **AAC** for audio compression, which use perceptual coding to remove or quantize the frequencies that are masked by louder sounds or are beyond the hearing range of humans.
  - **JPEG** and **WebP** for image compression, which use discrete cosine transform (DCT) and quantization to reduce the spatial resolution and color depth of the image, while preserving the most important features and details.
  - **MPEG** and **H.264** for video compression, which use motion estimation, prediction, and DCT to exploit the temporal and spatial redundancy in the video frames, and remove or quantize the information that is less visible or relevant to the human eye.



### Measures of performance for data compression

Data compression is the process of reducing the size of data without losing essential information or quality. Data compression can improve the efficiency of storage, transmission, and processing of data. There are two main types of data compression: lossless and lossy. Lossless compression preserves the exact information of the original data, while lossy compression discards some information that is deemed less important or perceptible.

To evaluate the performance of data compression techniques, we can use different measures, such as:

- **Compression ratio**: This is the ratio of the number of bits required to represent the data before compression to the number of bits required to represent the data after compression. A higher compression ratio means a higher reduction in data size. For example, if a file of 1000 bits is compressed to 200 bits, the compression ratio is 1000/200 = 5.
- **Throughput**: This is the rate at which data can be compressed or decompressed, measured in bits per second (bps) or bytes per second (Bps). A higher throughput means a faster compression or decompression process. For example, if a file of 1000 bits can be compressed in 0.1 seconds, the throughput is 1000/0.1 = 10000 bps.
- **Latency**: This is the time delay between the input and output of data compression or decompression, measured in seconds or milliseconds. A lower latency means a shorter waiting time for the user or the system. For example, if a file of 1000 bits takes 0.1 seconds to be compressed, the latency is 0.1 seconds.
- **Resource consumption**: This is the amount of memory, CPU, or power required to perform data compression or decompression. A lower resource consumption means a more efficient and economical compression or decompression process. For example, if a compression algorithm uses 10 MB of memory, 20% of CPU, and 5 W of power, the resource consumption is 10 MB + 20% + 5 W.
- **Accuracy**: This is the degree of similarity or difference between the original data and the compressed or decompressed data, measured in terms of error, distortion, or quality. A higher accuracy means a better preservation or reconstruction of the original data. For example, if a compressed image has a mean squared error (MSE) of 0.01 compared to the original image, the accuracy is 0.01.

These measures of performance can be used to compare different data compression techniques and to optimize the compressed data queries performance. However, there is often a trade-off between these measures, such as between compression ratio and accuracy, or between throughput and resource consumption. Therefore, the choice of data compression technique depends on the application and the user's requirements.



### Modeling and coding for data compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression preserves the exact original data, while lossy compression discards some data that is considered less important or perceptually redundant.
- Modeling and coding are the two levels to compress data :
  - In the first level, the data will be analyzed for any redundant information and extract it to develop a model.
  - In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique.
- Modeling can be done using one of two different types of techniques: statistical or dictionary-based .
  - Statistical modeling reads in and encodes a single symbol at a time using the probability of that symbol's appearance.
  - Dictionary-based modeling uses a single code to replace strings of symbols that are stored in a dictionary.
- Coding can be done using one of two different types of techniques: entropy coding or arithmetic coding .
  - Entropy coding assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, based on the entropy or information content of the data.
  - Arithmetic coding assigns a single code to the entire data, based on the cumulative probability of the symbols, and can achieve optimal compression.
- Data compression can also be done using deep learning techniques, such as Bit-Swap, which uses latent variable models and bits-back coding to learn the probability distribution of the data and encode it efficiently.



### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be reconstructed exactly from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of uncertainty or randomness in a source of data .
- Entropy is defined as the average number of bits needed to encode a symbol from the source, assuming an optimal encoding scheme .
- Entropy can be calculated using the formula: H(X) = - sum(p(x) log p(x)), where X is the source, p(x) is the probability of a symbol x, and log is the logarithm base 2 .
- Entropy is a lower bound for the compression ratio, which is the ratio of the size of the compressed data to the size of the original data .
- The compression ratio can be improved by using variable-length codes, which assign shorter codes to more frequent symbols and longer codes to less frequent symbols .
- Variable-length codes can be constructed using algorithms such as Huffman coding, arithmetic coding, and Lempel-Ziv coding .
- Huffman coding is a greedy algorithm that builds a binary tree based on the frequencies of the symbols, and assigns codes by traversing the tree from the root to the leaves .
- Arithmetic coding is a more efficient algorithm that assigns codes by dividing a unit interval into subintervals proportional to the probabilities of the symbols, and encoding a sequence of symbols by narrowing down the interval .
- Lempel-Ziv coding is a dictionary-based algorithm that exploits the redundancy and repetition in the data, and encodes a sequence of symbols by referencing previous occurrences in a sliding window .
- Lossless compression can be combined with other techniques such as run-length encoding, Burrows-Wheeler transform, and move-to-front transform to achieve higher compression ratios .



### A brief introduction to information theory

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding schemes.
- Information theory has applications in various fields, such as communication, cryptography, data compression, machine learning, statistics, and biology.
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be stored or transmitted.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared between two random variables.
- Information theory also studies the limitations and possibilities of communication systems, such as channels, which are the mediums through which information is transmitted, or codes, which are the methods of representing information in a compact or error-resistant way.
- Information theory provides fundamental bounds and principles for the design and analysis of communication systems, such as the noisy-channel coding theorem, which states that reliable communication is possible over a noisy channel if the rate of information transmission is below the channel capacity, or the source coding theorem, which states that the optimal compression rate for a source of information is given by its entropy.



### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques discard some information that is deemed less important or perceptually irrelevant.
- Data compression can be achieved by using different models and coders.
- A model is a component that captures the probability distribution of the data by knowing or discovering something about the structure of the input.
- A coder is a component that encodes the data based on the model, using fewer bits for more probable symbols and more bits for less probable symbols.
- Some of the popular model compression techniques are:

  - Pruning: Pruning is a technique that reduces the number of parameters in a deep neural network by removing redundant and inconsequential connections, neurons, channels, or layers . Pruning can improve the efficiency and generalization of the network, as well as reduce the risk of overfitting.
  - Quantization: Quantization is a technique that reduces the precision of the weights and activations in a deep neural network by using fewer bits to represent them, such as 8-bit or 16-bit integers instead of 32-bit floating point numbers . Quantization can reduce the memory and computational requirements of the network, as well as the energy consumption and latency.
  - Knowledge distillation: Knowledge distillation is a technique that transfers the knowledge from a large, complex model (teacher) to a smaller, simpler model (student) by training the student to mimic the output of the teacher . Knowledge distillation can preserve the accuracy of the network while reducing the size and complexity.
  - Low-rank factorization: Low-rank factorization is a technique that decomposes a large, dense matrix (such as a weight matrix or a convolutional kernel) into a product of two smaller, sparse matrices with lower rank . Low-rank factorization can reduce the number of parameters and operations in the network, as well as the storage and bandwidth requirements.



### Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Statistical models**: These models assume that the source data is generated by a random process that follows a certain probability distribution. The compression algorithm then uses the probability information to assign shorter codes to more likely symbols and longer codes to less likely symbols. Examples of statistical models are Huffman coding, arithmetic coding, and Lempel-Ziv coding.

- **Dictionary models**: These models use a predefined or adaptive set of symbols or phrases that represent common patterns or structures in the data. The compression algorithm then replaces the occurrences of these symbols or phrases with shorter codes that refer to their positions in the dictionary. Examples of dictionary models are run-length encoding, Lempel-Ziv-Welch coding, and Burrows-Wheeler transform.

- **Transform models**: These models use a mathematical transformation that converts the source data into a different domain or representation that is more amenable to compression. The compression algorithm then discards or quantizes the less significant or redundant components of the transformed data and encodes the remaining components with shorter codes. Examples of transform models are discrete cosine transform, wavelet transform, and principal component analysis.

- **Markov models**: These models assume that the source data is generated by a Markov process that depends on the previous state or context of the data. The compression algorithm then uses the state or context information to predict the next symbol and encode it with shorter codes if the prediction is correct or longer codes if the prediction is wrong. Examples of Markov models are finite context models, prediction by partial matching, and context tree weighting.



### Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to the possible symbols or sequences of symbols that the source can generate.
- A probability model is useful for data compression because it allows us to measure the amount of information in the data and to design optimal codes that minimize the number of bits needed to represent the data.
- There are different types of probability models, depending on the assumptions and the level of detail that we make about the source. Some common examples are:

  - Uniform model: This model assumes that all the symbols in the alphabet have the same probability of occurrence. For example, if the alphabet is A = {a, b, c, d}, then the uniform model is P = {0.25, 0.25, 0.25, 0.25}.
  - Bernoulli model: This model assumes that the source generates binary symbols (0 or 1) with a fixed probability p for 1 and 1-p for 0. For example, if p = 0.6, then the Bernoulli model is P = {0.4, 0.6}.
  - Geometric model: This model assumes that the source generates binary symbols (0 or 1) with a fixed probability p for 1, but the probability of 0 depends on the number of consecutive 0s that precede it. For example, if p = 0.2, then the geometric model is P = {0.8, 0.16, 0.032, 0.0064, ...}.
  - Poisson model: This model assumes that the source generates symbols from a discrete alphabet with a fixed average rate λ. The probability of each symbol is given by the Poisson distribution, which is P(k) = (λ^k / k!) * e^-λ, where k is the symbol value. For example, if λ = 2, then the Poisson model is P = {0.135, 0.271, 0.271, 0.18, 0.09, ...}.
  - Markov model: This model assumes that the source generates symbols from an alphabet A with a probability that depends on the previous n symbols, where n is the order of the model. The probability of each symbol is given by a conditional probability table, which is P(a_i | a_i-n, ..., a_i-1), where a_i is the current symbol and a_i-n, ..., a_i-1 are the previous n symbols. For example, if A = {a, b, c, d} and n = 2, then the Markov model is P = {P(a | aa), P(a | ab), P(a | ac), P(a | ad), P(b | aa), P(b | ab), P(b | ac), P(b | ad), ...}.



### Markov models for data compression

- Markov models are mathematical models that describe the probability of a system transitioning from one state to another, based on the current state and the previous states.
- Markov models can be used to model the statistical properties of natural language, images, audio, and other types of data, and to predict the next symbol or bit in a data stream.
- Markov models can be used for data compression by encoding the data using an arithmetic coder, which assigns shorter codes to more probable symbols or bits, and longer codes to less probable ones.
- Markov models can be classified into different types, depending on the order of the model (how many previous states are considered), the structure of the model (how the states are connected), and the adaptivity of the model (how the model changes over time).
- Some examples of Markov models for data compression are:

  - Dynamic Markov compression (DMC): a lossless data compression algorithm that uses a variable-order Markov model that adapts to the data dynamically, and predicts one bit at a time  .
  - Prediction by partial matching (PPM): a lossless data compression algorithm that uses a variable-order Markov model that predicts one byte at a time, and uses a context-mixing technique to combine multiple models.
  - Burrows-Wheeler transform (BWT): a reversible transformation that reorders the data in a way that makes it more compressible by a Markov model, by grouping similar symbols together.
  - Context tree weighting (CTW): a lossless data compression algorithm that uses a variable-order Markov model that assigns weights to different contexts, and uses a weighted average of the predictions from different models.



### Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S i, each with its own model M i and a switch that selects a source S i with probability P i.
- A composite source model is useful for data compression when a single model is not adequate to capture the characteristics of the data.
- A composite source model can be used to describe some very complicated processes, such as image signals, natural language, or multimedia data .
- A composite source model can be encoded using different coding techniques, such as Huffman coding, arithmetic coding, or dictionary coding, depending on the nature of the component sources.



### Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Coding is the process of assigning symbols or codes to the data elements or symbols in the source alphabet, such as characters, pixels, or samples.
- Coding can be used for data compression, which is the reduction of the size of data without significant loss of information or quality.
- Data compression can be classified into two types: lossless and lossy.
  - Lossless compression preserves the exact information of the original data, and allows perfect reconstruction of the original data after decompression. Examples of lossless compression techniques are Huffman coding, arithmetic coding, run-length encoding (RLE), and Lempel-Ziv-Welch (LZW) coding.
  - Lossy compression discards some information of the original data, and allows only approximate reconstruction of the original data after decompression. Examples of lossy compression techniques are transform coding, quantization, and vector quantization.
- Coding can also be classified into two types: fixed-length coding and variable-length coding.
  - Fixed-length coding assigns codes of equal length to all the data elements or symbols in the source alphabet. For example, ASCII code uses 8 bits to represent each character.
  - Variable-length coding assigns codes of different lengths to the data elements or symbols in the source alphabet, depending on their probabilities or frequencies of occurrence. For example, Huffman coding assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, resulting in optimal compression for a given source alphabet.
- Coding can also be classified into two types: entropy coding and predictive coding.
  - Entropy coding exploits the statistical properties of the data elements or symbols in the source alphabet, such as their probabilities or frequencies of occurrence, to assign codes that minimize the average code length. Examples of entropy coding techniques are Huffman coding, arithmetic coding, and LZW coding.
  - Predictive coding exploits the correlation or redundancy among the data elements or symbols in the source alphabet, such as their spatial or temporal relationships, to predict the next data element or symbol based on the previous ones, and encode the difference or error between the actual and predicted data element or symbol. Examples of predictive coding techniques are differential coding, delta modulation, and motion compensation.



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords, i.e., no ambiguity in the decoding process.
- A code is non-singular if no two distinct source symbols have the same codeword.
- A non-singular code is not necessarily uniquely decodable, as the following example shows:

  - Let the source symbols be {a, b, c, d} and the codewords be {0, 01, 011, 111}.
  - This code is non-singular, but not uniquely decodable, because the sequence 0111 can be decoded as either ab or cd.

- A code is called an instantaneous code if the end of any codeword is recognizable without examining subsequent code symbols.
- The instantaneous codes have the property that no codeword is a prefix of another codeword. For this reason, prefix-free codes are sometimes known as instantaneous codes.
- Every instantaneous code is uniquely decodable, but not vice versa, as the following example shows:

  - Let the source symbols be {a, b, c, d} and the codewords be {0, 10, 110, 111}.
  - This code is uniquely decodable, but not instantaneous, because 0 is a prefix of 10, and 110 is a prefix of 111.

- A code is called an optimal code if it minimizes the average codeword length for a given source distribution, i.e., it achieves the lowest possible redundancy.
- The Kraft inequality is a necessary and sufficient condition for the existence of an instantaneous code with given codeword lengths.
- The Kraft inequality states that for any instantaneous code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  - Summation from i=1 to n of 2^(-li) <= 1

- The Kraft inequality can also be used to test whether a given code is uniquely decodable, by using the extended codeword lengths, which are the lengths of the codewords after appending a special delimiter symbol to each codeword.



### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of variable-length code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- A prefix code is also called a prefix-free code, a prefix condition code, or an instantaneous code.
- A prefix code has the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- A prefix code can be constructed using various algorithms, such as Huffman coding, arithmetic coding, Elias coding, etc .
- A prefix code is useful for data compression, because it can reduce the average length of the codewords by assigning shorter codewords to more frequent symbols, and longer codewords to less frequent symbols.
- A prefix code can also be used for error detection and correction, because any invalid or corrupted codeword can be detected by checking if it is a prefix of another codeword or not.



## Unit 2 - The Huffman coding algorithm

- The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols.
- The algorithm starts by creating a node for each symbol and assigning it a weight equal to its frequency. Then, it repeatedly merges the two nodes with the lowest weights into a new node, whose weight is the sum of the weights of its children. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to that symbol, and appending a 0 or a 1 depending on whether the left or the right child is chosen at each step. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible codes for a given set of symbols and frequencies. The average length of the codes is equal to the entropy of the data, which is a measure of its information content.
- The Huffman coding algorithm can be used to compress text, images, audio, video, or any other type of data. It is widely used in lossless compression formats, such as ZIP, GZIP, PNG, and MP3.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the minimum expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The minimum variance Huffman code is a variant of the minimum redundancy code that also minimizes the variance of the codeword length.
- The variance of the codeword length is the difference between the maximum and minimum lengths of the codewords.
- A lower variance means that the codewords have more uniform lengths and are less likely to cause buffer overflow or underflow.
- The minimum variance Huffman code can be constructed by modifying the Huffman algorithm to use a priority queue that sorts the symbols by their probabilities and then by their lengths.
- The algorithm merges the two symbols with the lowest probabilities and assigns them a common prefix, then inserts the merged symbol back into the queue with the sum of their probabilities and the length incremented by one.
- The algorithm repeats this process until there is only one symbol left in the queue, which is the root of the Huffman tree.
- The minimum variance Huffman code can be obtained by traversing the Huffman tree and assigning 0 or 1 to each branch.
- The minimum variance Huffman code has the property that the codewords with the same length are lexicographically ordered according to their probabilities.
- The minimum variance Huffman code is useful for applications that require a bounded codeword length or a low variance of the codeword length.
- An example of a minimum variance Huffman code for a source with six symbols and their probabilities is shown below:

| Symbol | Probability | Codeword | Length |
|--------|-------------|----------|--------|
| a1     | 0.2         | 00       | 2      |
| a2     | 0.2         | 01       | 2      |
| a3     | 0.25        | 10       | 2      |
| a4     | 0.05        | 1100     | 4      |
| a5     | 0.15        | 1101     | 4      |
| a6     | 0.15        | 111      | 3      |

- The Huffman tree for this code is shown below:

```
       1.0
      /   \
    0.5   0.5
   /   \ /   \
 0.25 0.2 0.2 0.15
 /  \       /  \
0.15 0.1   0.05 0.1
```

- The entropy of the source is 2.405 bits/symbol.
- The average length of the code is 2.55 bits/symbol.
- The efficiency of the code is 94.32%.
- The variance of the code is 2 bits/symbol.



### Adaptive Huffman coding

- Adaptive Huffman coding (also called Dynamic Huffman coding) is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data.
- It uses a binary tree to represent the codes and frequencies of the symbols, and updates the tree as new symbols are encountered.
- The tree is maintained such that the most frequent symbols are near the root and the least frequent symbols are near the leaves.
- The tree is also kept in a sibling property order, which means that nodes with lower weights are higher in the tree and nodes with equal weights are ordered by the time of their creation.
- There are two main algorithms for adaptive Huffman coding: FGK algorithm and Vitter algorithm.
- FGK algorithm was proposed by Faller, Gallager and Knuth in 1979. It uses a special node called NYT (Not Yet Transmitted) to represent new symbols that have not been seen before. It also uses a procedure called node swapping to maintain the sibling property order of the tree.
- Vitter algorithm was proposed by Jeffrey Vitter in 1987. It improves the FGK algorithm by using a different node swapping procedure that reduces the number of swaps and the size of the tree. It also uses two parameters, e and r, to control the creation and deletion of nodes.
- Adaptive Huffman coding has some advantages over static Huffman coding, such as:
  - It does not require a priori knowledge of the source distribution or a separate transmission of the code table.
  - It can adapt to changing source statistics and achieve near-optimal compression ratios.
  - It can handle infinite or unknown input streams.
- Adaptive Huffman coding also has some disadvantages, such as:
  - It requires more computation and memory than static Huffman coding.
  - It may perform poorly for sources with highly skewed or non-stationary distributions.
  - It may introduce some overhead for transmitting the NYT symbol and the initial tree structure.



### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree that minimizes the total length of the encoded data. The tree is constructed from the bottom up, starting with the least frequent symbols and merging them into a new node that represents their combined frequency. This process is repeated until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf that corresponds to the symbol, and appending a 0 or a 1 depending on whether the left or the right branch is taken. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm can be implemented using a priority queue, which is a data structure that stores elements according to their priorities and allows efficient insertion and deletion of the minimum-priority element. The priority queue can be implemented using a heap, which is a complete binary tree that satisfies the heap property: the value of each node is less than or equal to the value of its children.
- The steps of the algorithm are as follows:

  1. Create a priority queue Q and insert each symbol and its frequency as a leaf node into Q.
  2. While Q has more than one element, do the following:
     - Extract the two nodes with the lowest frequency from Q and create a new node that has the sum of their frequencies as its value and the two nodes as its children.
     - Insert the new node into Q.
  3. The remaining node in Q is the root of the Huffman tree.
  4. Traverse the tree and assign codes to the symbols by appending 0s and 1s along the path.
  5. Encode the data by replacing each symbol with its corresponding code.
  6. Decode the data by following the codes from the root to the leaves of the tree.

- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible code for any given set of symbols and frequencies. However, the algorithm requires the knowledge of the frequencies of the symbols in advance, which may not be available or may change over time. In such cases, adaptive Huffman coding can be used, which updates the tree dynamically as the data is processed.



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- The encoding procedure for the Huffman coding algorithm can be summarized as follows  :

  - Create a leaf node for each character and add them to a priority queue based on their frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and with frequency equal to the sum of their frequencies.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each character. The left child gets a 0 bit and the right child gets a 1 bit.
  - Store the codes in a map or a table for easy lookup.
  - To encode a given message, replace each character with its corresponding code from the map or the table.
  - To decode a given encoded message, start from the root of the Huffman tree and follow the bits until reaching a leaf node, then output the character and restart from the root.



### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the source data.
- To decode a Huffman-coded message, one needs to have access to the Huffman tree that was used to encode the message, or a table that maps each code to its corresponding symbol.
- The decoding procedure is as follows:
  - Start from the root of the Huffman tree and read the bits of the encoded message from left to right.
  - If the current bit is 0, move to the left child of the current node. If the current bit is 1, move to the right child of the current node.
  - If the current node is a leaf, output the symbol stored in the node and return to the root of the tree.
  - Repeat steps 2 and 3 until all the bits of the encoded message are processed.
- For example, consider the following Huffman tree and the encoded message 110010011:

Huffman tree

- The decoding procedure would be:

| Bit | Current Node | Output |
| --- | ------------ | ------ |
| 1   | Root         |        |
| 1   | Right child  |        |
| 0   | Left child   | C      |
| 0   | Root         |        |
| 1   | Right child  |        |
| 0   | Left child   | C      |
| 0   | Root         |        |
| 0   | Left child   |        |
| 1   | Right child  | A      |
| 1   | Root         |        |
| 1   | Right child  |        |
| 1   | Right child  | B      |

- The decoded message is CCAAB.



### Golomb codes

- Golomb codes are a type of parameterized codes that can be used to compress data with geometric or exponential distributions.
- Golomb codes use a positive integer parameter M to divide an input value x into two parts: q, the quotient of x divided by M, and r, the remainder of x modulo M.
- The codeword for x consists of two parts: the unary code for q+1, followed by the binary code for r.
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The binary code for r depends on the value of M. If M is a power of 2, then r is encoded using log2(M) bits. For example, if M=4, then r can be 0, 1, 2, or 3, and can be encoded using 2 bits: 00, 01, 10, or 11.
- If M is not a power of 2, then r is encoded using a truncated binary code, which uses fewer bits for smaller values of r. For example, if M=5, then r can be 0, 1, 2, 3, or 4, and can be encoded using 2 bits for r<4 and 3 bits for r=4: 00, 01, 10, 110, or 111.
- The length of the codeword for x depends on the value of M and the distribution of x. If x has a geometric distribution with parameter p, then the optimal value of M is -log2(p), and the average codeword length is -log2(p) + 1/p bits.
- Golomb codes are useful for compressing data that has a large number of small values and a few large values, such as run-lengths, gaps between occurrences, or residuals in predictive coding.
- Golomb codes can be easily implemented using arithmetic operations such as division, modulo, and bit-shifting.



### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a positive integer x using Rice codes, the following steps are performed:
  - Divide x by m and write the quotient in unary code, i.e., a sequence of 1s followed by a 0.
  - Write the remainder of x/m in binary code, using k bits.
  - Concatenate the unary and binary codes to form the final code.
- For example, if k = 2 and x = 11, then the Rice code is:
  - 11 / 4 = 2 with remainder 3, so the unary code is 110 and the binary code is 11.
  - The final code is 11011.
- Rice codes are generally used to encode entropy in audio/video codecs, where the data often follows a Laplacian distribution.
- Rice codes are also used in adaptive coding schemes, where the parameter k is adjusted according to the statistics of the data.



### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall coding is a method of data compression that converts variable-length source symbols into fixed-length code words.
- Tunstall coding requires the algorithm to know the probability distribution of each source symbol before encoding or decoding.
- Tunstall coding is based on the idea of parsing the source symbols into variable-length words that are as likely as possible, and then assigning a fixed-length code to each word.
- Tunstall coding can be seen as a generalization of Huffman coding, where the source symbols are not single letters, but variable-length words.
- Tunstall coding can achieve a compression ratio close to the entropy of the source, but it has some drawbacks, such as high memory requirements and sensitivity to errors.
- Tunstall coding can be implemented using a tree structure, where each node represents a source word and each branch represents a source symbol. The tree is constructed by starting with a single node containing the empty word, and then iteratively splitting the node with the highest probability into branches corresponding to each source symbol, until the desired number of code words is reached.
- Tunstall coding can be illustrated by the following example, where the source alphabet is {a, b, c} and the probabilities are P(a) = 0.6, P(b) = 0.3, P(c) = 0.1. The code word length is 3 bits, so there are 8 possible code words.

| Source word | Probability | Code word |
| ----------- | ----------- | --------- |
| a           | 0.6         | 000       |
| b           | 0.3         | 001       |
| c           | 0.1         | 010       |
| aa          | 0.36        | 011       |
| ab          | 0.18        | 100       |
| ac          | 0.06        | 101       |
| ba          | 0.18        | 110       |
| bb          | 0.09        | 111       |

- The average code word length is 3 bits, and the entropy of the source is 1.485 bits per symbol, so the compression ratio is 1.485 / 3 = 0.495.



### Applications of Huffman coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or weight. The more frequent a data value is, the shorter its code will be. The less frequent a data value is, the longer its code will be. This way, the data can be represented using fewer bits on average, resulting in compression.

Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel, saving bandwidth and transmission time. For example, the ASCII code uses 8 bits to represent each character, but Huffman coding can use fewer bits for the common characters and more bits for the rare ones.
- **Conventional compression formats**: Huffman coding is often used by compression formats like PKZIP, GZIP, BZIP2, etc. to compress the data before storing it in a file or archive. These formats usually combine Huffman coding with other techniques like run-length encoding, dictionary encoding, etc. to achieve better compression ratios .
- **Multimedia codecs**: Huffman coding is also used by multimedia codecs like JPEG, PNG, and MP3 to compress the data that represents images, audio, or video. These codecs usually use Huffman coding to encode the quantized coefficients of the discrete cosine transform (DCT) or the modified discrete cosine transform (MDCT), which are used to transform the data from the spatial or temporal domain to the frequency domain. Huffman coding helps to reduce the size of the coefficients by assigning shorter codes to the more frequent ones and longer codes to the less frequent ones  .



### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the image.
  - Sort the symbols in the frequency table in ascending order of frequency.
  - Build a binary tree by repeatedly merging the two least frequent symbols into a new node with a frequency equal to the sum of their frequencies. The merged symbols become the left and right children of the new node. Repeat this process until there is only one node left, which is the root of the tree.
  - Assign a binary code to each symbol by traversing the tree from the root to the leaf. Append a 0 to the code when moving to the left child and a 1 when moving to the right child.
  - Encode the image by replacing each symbol with its corresponding binary code.
  - Decode the image by traversing the tree from the root to the leaf according to the binary code and outputting the symbol at the leaf.

- Huffman coding is optimal for images that have a skewed distribution of symbols, i.e., some symbols are much more frequent than others.
- Huffman coding can achieve a compression ratio of up to 50% for grayscale images and up to 25% for color images.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters in a more efficient way.
- Text compression can save storage space, bandwidth, and transmission time, and can also improve security and privacy by making the text less readable by humans or machines.
- One of the most popular and widely used text compression algorithms is the Huffman coding algorithm, which was invented by David A. Huffman in 1952.
- The Huffman coding algorithm is a lossless compression algorithm, which means that it preserves the original information and allows the exact reconstruction of the text from the compressed file.
- The Huffman coding algorithm works by assigning variable-length binary codes to the characters in the text, based on their frequencies of occurrence. The more frequent a character is, the shorter its code will be, and vice versa.
- The Huffman coding algorithm consists of the following steps:

  1. Create a frequency table that counts the number of occurrences of each character in the text.
  2. Create a priority queue (or a min-heap) that contains the characters as nodes, sorted by their frequencies in ascending order.
  3. While the queue has more than one node, do the following:
     - Dequeue the two nodes with the lowest frequencies and create a new internal node with the sum of their frequencies as its frequency.
     - Make the two dequeued nodes the left and right children of the new node, and assign them the binary digits 0 and 1 respectively.
     - Enqueue the new node back to the queue.
  4. The remaining node in the queue is the root of the Huffman tree, which represents the optimal prefix code for the text.
  5. Traverse the Huffman tree from the root to the leaves, and concatenate the binary digits along the path to obtain the code for each character.
  6. Replace each character in the text with its corresponding code, and output the compressed file.

- The Huffman coding algorithm is optimal in the sense that it produces the minimum possible average code length for a given text and its character frequencies.
- The Huffman coding algorithm is also adaptive, which means that it can adjust to the changing frequencies of the characters in the text, by updating the frequency table and the Huffman tree accordingly.
- The Huffman coding algorithm is widely used in various applications, such as data compression, error correction, cryptography, and information theory.



### Audio Compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Audio compression is the process of reducing the amount of data required to represent an audio signal, without significantly affecting the quality of the sound.
- Audio compression can be either lossy or lossless, depending on whether the original signal can be perfectly reconstructed from the compressed data or not.
- Lossy audio compression techniques, such as MP3 and AAC, use psychoacoustic models to remove the parts of the signal that are less perceptible to the human ear, and then encode the remaining data using variable-length codes, such as Huffman coding.
- Huffman coding is a method of data compression that is independent of the data type, that is, the data could represent an image, audio or spreadsheet . This compression scheme is used in JPEG and MPEG-2.
- Huffman coding works by looking at the data stream that makes up the file to be compressed, and assigning shorter codes to the symbols that occur more frequently, and longer codes to the symbols that occur less frequently .
- Huffman coding is based on the principle of minimum redundancy, which states that the optimal code for a given source is the one that minimizes the average code length, and therefore maximizes the compression ratio.
- Huffman coding can be either static or dynamic, depending on whether the code table is fixed or updated during the encoding process. Static Huffman coding requires a priori knowledge of the source statistics, while dynamic Huffman coding adapts to the changing source statistics.
- Huffman coding can be combined with other compression techniques, such as subband coding, run-length encoding, and interpolation, to achieve higher compression ratios and better sound quality .
- Huffman coding is a lossless compression technique, which means that no information is lost during the compression and decompression process, and the original signal can be perfectly recovered from the compressed data.



## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term of the sequence, usually denoted by a<sub>1</sub>.
  - Define the rule or formula that determines the next term of the sequence, usually denoted by a<sub>n</sub>.
  - Use a loop or a recursion to generate the terms of the sequence until a certain condition is met, such as reaching a certain number of terms, a certain value, or a certain pattern.
  - Store the terms of the sequence in a data structure, such as an array, a list, or a vector.
  - Display or return the sequence as the output of the program.
- For example, to code the sequence 2, 4, 6, 8, ..., we can use the following Python code:

```python
# Define the first term of the sequence
a1 = 2

# Define the rule or formula for the next term
def next_term(a):
  return a + 2

# Define the number of terms to generate
n = 10

# Create an empty list to store the terms
sequence = []

# Use a loop to generate the terms
for i in range(n):
  # Append the current term to the list
  sequence.append(a1)
  # Update the current term by applying the rule
  a1 = next_term(a1)

# Display the sequence
print(sequence)
```



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it more efficiently, without losing any information.
- Binary code is a way of representing data using only two symbols, usually 0 and 1.
- Coding a sequence is the task of assigning a unique binary code to each symbol in a given sequence of data, such as text, image, audio, or video.
- There are different types of codes that can be used for coding a sequence, such as fixed-length codes, variable-length codes, prefix codes, and universal codes.
- Fixed-length codes assign the same number of bits to each symbol, regardless of their frequency or importance. For example, a fixed-length code of three bits can encode up to eight symbols, such as 000, 001, 010, 011, 100, 101, 110, and 111.
- Variable-length codes assign different numbers of bits to different symbols, depending on their frequency or importance. For example, a variable-length code can assign one bit to the most frequent symbol, two bits to the second most frequent symbol, and so on. This can reduce the average length of the code and the size of the data.
- Prefix codes are a special type of variable-length codes that have the property that no code is a prefix of any other code. This means that the code can be decoded unambiguously from left to right, without any separators or markers. For example, the code 0, 10, 110, and 111 is a prefix code, but the code 0, 01, 10, and 11 is not, because 0 is a prefix of 01 and 10, and 01 is a prefix of 011.
- Universal codes are a special type of prefix codes that can encode any sequence of positive integers, regardless of their distribution, with a constant factor of optimality. This means that the expected length of the code is close to the expected length of the optimal code for that distribution. For example, the Elias gamma code, the Elias delta code, and the Fibonacci code are universal codes.



### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using fixed-length binary words, where each character or symbol is assigned a unique code. For example, the ASCII code uses 8 bits to represent 256 characters.
- Huffman coding is a method of representing data using variable-length binary words, where each character or symbol is assigned a code based on its frequency of occurrence in the data. For example, the most frequent character may be assigned a single bit, while the least frequent character may be assigned a longer code.
- The main advantage of Huffman coding over binary coding is that it can achieve higher compression ratios, since it uses shorter codes for more frequent characters and longer codes for less frequent characters. This reduces the overall size of the data and saves storage space and bandwidth.
- The main disadvantage of Huffman coding over binary coding is that it requires an extra step of generating a Huffman tree, which is a binary tree that shows the codes for each character. This tree needs to be stored or transmitted along with the data, which adds some overhead. Also, Huffman coding is not suitable for data that has a uniform distribution of characters, since it will not reduce the size of the data significantly.
- The main application of Huffman coding is in lossless data compression, where the original data can be recovered exactly from the compressed data. This is useful for text, audio, and image files that need to preserve their quality and integrity. Binary coding is more commonly used for encoding data that does not need to be compressed, such as binary numbers, instructions, and commands.



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a sequence, such that the code can be used to reconstruct the original sequence without any loss of information.
- Coding a sequence can be used for various applications, such as:
  - **Data compression**: Reducing the size of data by using shorter codes for more frequent symbols and longer codes for less frequent symbols. This can save storage space and bandwidth, and improve the efficiency of data transmission and processing. Examples of data compression algorithms that use coding a sequence are Huffman coding, arithmetic coding, and Lempel-Ziv coding.
  - **Data encryption**: Protecting the confidentiality of data by transforming it into a different form that can only be decoded by authorized parties. This can prevent unauthorized access, modification, or tampering of data. Examples of data encryption algorithms that use coding a sequence are stream ciphers, block ciphers, and public-key cryptography.
  - **Data error detection and correction**: Detecting and correcting errors that may occur during data transmission or storage, due to noise, interference, or defects. This can improve the reliability and accuracy of data communication and storage. Examples of data error detection and correction algorithms that use coding a sequence are parity check, cyclic redundancy check, and Hamming code.



### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image, without losing any information or quality.
- The JBIG standard, also known as JBIG1, is an early lossless image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group.
- The JBIG standard was standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines, as it offers better compression efficiency than Fax Group 4 compression.
- The JBIG standard uses a technique called arithmetic coding, which assigns variable-length codes to symbols based on their probabilities of occurrence.
- The JBIG standard also uses a technique called adaptive template matching, which adapts the coding context to the local image features.
- The JBIG standard can compress bi-level images of any size and resolution, and can handle multiple images in a single file.
- The JBIG standard has been superseded by the JBIG2 standard, which is a newer and more advanced image compression standard for bi-level images.
- The JBIG2 standard can achieve both lossless and lossy compression, and can exploit model-based coding for text and halftones, as well as nearby neighbor based coding for generic bi-level images.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two colors, usually black and white, such as scanned documents, faxes, or text.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than the existing standards, such as MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544), by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve segmenting an image into overlapping and/or non-overlapping regions of text, halftone, and generic content, and then compressing each region using different methods.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and then replacing them with references to a symbol dictionary.
- Halftone regions are compressed by identifying and encoding the shape and position of the halftone dots, and then replacing them with references to a halftone dictionary.
- Generic regions are compressed by using arithmetic coding or MMR, depending on the image quality and compression ratio desired.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.



### Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, meaning that the decompressed image is identical to the original image. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, or icons. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 replaces repeated sequences of pixels with shorter references, while Huffman coding assigns variable-length codes to the most frequent pixels. Deflate is used in formats such as PNG, GIF, and ZIP.

  - Run-length encoding: Run-length encoding is a simple lossless image compression technique that reduces the size of an image by encoding sequences of repeated pixels with a single value and a count. For example, a sequence of 10 white pixels can be encoded as (10, 255), where 10 is the count and 255 is the value. Run-length encoding is effective for images with large areas of uniform color, such as cartoons or logos.

  - Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to the pixels based on their probabilities. Arithmetic coding is more efficient than Huffman coding, as it can use fractional bits to encode the pixels. Arithmetic coding is used in formats such as JPEG 2000 and JPEG-LS.

- Lossy compression: Lossy compression is a technique that discards some of the original data, meaning that the decompressed image is an approximation of the original image. Lossy compression is suitable for images that can tolerate some degradation, such as photographs, videos, or web graphics. Lossy compression algorithms include:

  - Transform coding: Transform coding is the most commonly used method of lossy compression. It converts the image data into a different representation that is more compact and easier to compress. The most widely used form of transform coding is the Discrete Cosine Transform (DCT), which decomposes the image into a sum of cosine functions of different frequencies. DCT is used in formats such as JPEG, MPEG, and MP3 .

  - Quantization: Quantization is the process of reducing the number of possible values for each pixel or coefficient. Quantization reduces the precision and the dynamic range of the image data, resulting in some loss of quality. Quantization is usually applied after transform coding, as the transformed coefficients have different levels of importance and can be quantized differently. Quantization is the main source of compression and distortion in lossy compression.

  - Entropy coding: Entropy coding is the process of assigning variable-length codes to the pixels or coefficients based on their frequencies. Entropy coding removes the redundancy and the statistical correlation in the image data, resulting in a smaller file size. Entropy coding is usually applied after quantization, as the quantized values have a non-uniform distribution and can be encoded more efficiently. Entropy coding algorithms include Huffman coding and arithmetic coding.



### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the redundancy and the size of the data.
- There are many variants of dictionary techniques, such as LZ77, LZ78, LZW, LZSS, LZMA, etc. They differ in the way they construct and manage the dictionary, the way they encode and decode the matches, and the way they handle the trade-off between compression ratio and speed.
- Dictionary techniques are widely used in various applications, such as text, image, audio, and video compression, data transmission, archiving, encryption, etc. Some examples of formats that use dictionary techniques are ZIP, GIF, PNG, MP3, JPEG, etc.



### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data set by removing redundancy or irrelevant information.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly reconstructed from the compressed data or not.
- Coding a sequence is a fundamental task in data compression, where a sequence of symbols (such as characters, bits, pixels, etc.) is represented by a shorter sequence of codes (such as binary numbers, Huffman codes, arithmetic codes, etc.).
- Coding a sequence can be done in two ways: fixed-length coding or variable-length coding.
- Fixed-length coding assigns a fixed number of bits to each symbol, regardless of its frequency or importance. For example, ASCII code uses 8 bits to represent each character.
- Variable-length coding assigns a variable number of bits to each symbol, depending on its frequency or importance. For example, Huffman code uses fewer bits to represent more frequent symbols and more bits to represent less frequent symbols.
- Variable-length coding can achieve better compression ratios than fixed-length coding, but it requires more complex algorithms and data structures to encode and decode the sequences.
- Coding a sequence can also be done in two modes: block coding or stream coding.
- Block coding divides the sequence into fixed-size blocks and encodes each block independently. For example, JPEG image compression uses block coding with 8x8 pixel blocks.
- Stream coding encodes the sequence as a continuous stream of bits, without dividing it into blocks. For example, MP3 audio compression uses stream coding with a variable bit rate.
- Stream coding can adapt to the changing characteristics of the sequence, but it requires more synchronization and error correction mechanisms to ensure reliable transmission and decoding.



### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression is fast and simple, but it may not be optimal for data that has a variable or unknown distribution.
- Static dictionary compression can be implemented by using a hash table, a trie, or a prefix code to map the dictionary entries to their codes .
- Static dictionary compression can be combined with other compression techniques, such as run-length encoding, Huffman coding, or arithmetic coding, to improve the compression ratio .



### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a technique for compressing a sequence of symbols by encoding it as a sequence of numbers.
- The idea is to use a dictionary that maps symbols or pairs of symbols to numbers, and update the dictionary as new symbols or pairs are encountered in the input sequence.
- The dictionary can be initialized with the symbols of the alphabet and their corresponding numbers, or it can be built dynamically from the input sequence.
- The output of the diagram coding is a sequence of numbers that can be decoded by using the same dictionary in reverse.
- Diagram coding can achieve better compression than simple symbol coding, because it can exploit the correlations or patterns between adjacent symbols in the input sequence.
- An example of diagram coding is the LZ77 algorithm, which uses a sliding window to store the most recent symbols of the input sequence, and encodes each symbol or pair as a reference to a previous occurrence in the window.



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel.
- LZ77 uses a sliding window to find matches between the current data and the previous data, and encodes the matches as references to the window positions and lengths.
- LZ78 uses a tree structure to store the prefixes of the data, and encodes the data as references to the tree nodes and the next symbols.
- LZW uses a hash table to store the prefixes of the data, and encodes the data as references to the table entries.
- Adaptive dictionary can compress data that is not plain text, such as audio or video, by building the dictionary from the data itself .
- Adaptive dictionary can also handle data that has varying patterns or frequencies, by updating the dictionary accordingly .
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data, but it may also incur some overheads, such as the dictionary size and the encoding complexity  .



### The LZ77 Approach

- LZ77 is a **lossless data compression algorithm** published by Abraham Lempel and Jacob Ziv in 1977  .
- It is a **dictionary coder** and maintains a **sliding window** during compression  .
- The sliding window consists of two parts: a **search buffer** and a **lookahead buffer**  .
- The search buffer contains the previously encoded data, and the lookahead buffer contains the data to be encoded  .
- The algorithm searches for the longest match between the lookahead buffer and the search buffer, and encodes it as a **triplet** of the form (offset, length, next symbol)  .
- The offset is the distance from the current position to the start of the match, the length is the number of symbols in the match, and the next symbol is the symbol following the match  .
- If no match is found, the algorithm encodes the next symbol as a literal  .
- The algorithm then slides the window by the length of the match plus one, and repeats the process until the end of the input  .
- The decompression algorithm reverses the process by using the triplets to reconstruct the original data  .
- LZ77 is a **greedy algorithm** that tries to find the longest match at each step, but it is not optimal in terms of compression ratio .
- LZ77 can be improved by using **variable-length codes** to encode the triplets, such as Huffman coding or arithmetic coding .
- LZ77 can also be modified by using different window sizes, different matching criteria, or different data structures to speed up the search .
- LZ77 is the basis for many variations and extensions, such as LZSS, LZMA, DEFLATE, and others .



### The LZ78 Approach

- LZ78 is a lossless data compression algorithm that was published by Abraham Lempel and Jacob Ziv in 1978.
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry  .
- LZ78 uses a trie data structure to store the dictionary, as it is more efficient for this compression technique. A trie is a tree-like data structure that stores strings as paths from the root to the leaves, where each node represents a character and each edge represents a prefix.
- The algorithm works as follows :
  - Initialize the dictionary with an empty string as the first entry.
  - Read the next character from the input and append it to the current token.
  - If the current token is already in the dictionary, continue reading the next character and appending it to the current token.
  - If the current token is not in the dictionary, output the index of the longest prefix of the current token that is in the dictionary, followed by the last character of the current token. Then, add the current token to the dictionary as a new entry, and reset the current token to an empty string.
  - Repeat until the end of the input is reached.
- For example, consider the input string "abracadabra" and the following dictionary:

| Index | Token |
| ----- | ----- |
| 0     | ""    |
| 1     | "a"   |
| 2     | "b"   |
| 3     | "r"   |
| 4     | "ab"  |
| 5     | "c"   |
| 6     | "ad"  |
| 7     | "ra"  |
| 8     | "abr" |
| 9     | "aca" |
| 10    | "dab" |

- The output of the LZ78 compression algorithm would be:

| Index | Character |
| ----- | --------- |
| 0     | a         |
| 0     | b         |
| 0     | r         |
| 1     | b         |
| 0     | c         |
| 1     | d         |
| 3     | a         |
| 1     | b         |
| 3     | a         |

- The output can be decoded by using the same dictionary and reversing the process. For each index-character pair, concatenate the token at the index with the character and output it. Then, add the new token to the dictionary as a new entry. For example, the first pair (0, a) would output "a" and add "a" to the dictionary. The second pair (0, b) would output "b" and add "b" to the dictionary. The third pair (0, r) would output "r" and add "r" to the dictionary. The fourth pair (1, b) would output "ab" and add "ab" to the dictionary, and so on.
- The advantages of LZ78 are that it does not require any parameterization, it can handle any type of data, and it can adapt to changes in the data distribution.
- The disadvantages of LZ78 are that it can produce a large dictionary that may not fit in memory, it can output long codes for rare tokens, and it can be slow to encode and decode.



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a sequence, such that the original sequence can be reconstructed from the code.
- Coding a sequence can be used for various applications, such as:
  - Data compression: reducing the size of data by using shorter codes for more frequent symbols and longer codes for less frequent symbols. This can save storage space and bandwidth, and improve transmission speed and efficiency.
  - Data encryption: transforming data into a secret code that can only be deciphered by authorized parties who have the key. This can protect data from unauthorized access, modification, or tampering.
  - Data transmission: sending data over a noisy channel that may introduce errors or distortions. Coding a sequence can help detect and correct errors, or recover the original data from a corrupted code.
  - Data storage: storing data in a compact and reliable way that minimizes the risk of data loss or degradation. Coding a sequence can help reduce redundancy, increase robustness, and enhance retrieval performance.
  - Data analysis: extracting useful information from data by identifying patterns, trends, or anomalies. Coding a sequence can help simplify data representation, facilitate data processing, and enable data mining.



### File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save disk space, bandwidth, and transmission time.
- UNIX compress is one of the file compression utilities available on UNIX systems.
- UNIX compress uses the Lempel-Ziv algorithm to compress files.
- UNIX compress adds a `.Z` extension to the compressed file name and preserves the original file name and time stamp.
- UNIX compress can compress files up to 80% of their original size, depending on the data.
- UNIX compress can be used to compress single files or multiple files in an archive format such as tar or cpio.
- UNIX compress can be invoked by the command `compress filename` or `compress -v filename` for verbose output.
- UNIX compress can be reversed by the command `uncompress filename.Z` or `uncompress -v filename.Z` for verbose output.
- UNIX compress can also be combined with other commands using pipes, such as `cat filename | compress > filename.Z` or `uncompress < filename.Z | more`.
- UNIX compress is not compatible with other compression utilities such as gzip, bzip2, or zip.
- UNIX compress is less efficient and slower than newer compression utilities such as gzip or bzip2.
- UNIX compress is not widely used anymore and is mostly replaced by gzip or bzip2.



### Image Compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, without any loss of information. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, or icons. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. Deflate is used in formats such as PNG, ZIP, and GZIP.
  - Run-length encoding: Run-length encoding is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. For example, a row of 10 white pixels can be encoded as 10W, instead of WWWWWWWWWW. Run-length encoding is used in formats such as BMP and TIFF .
  - Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. Arithmetic coding can achieve higher compression ratios than Huffman coding, but it is more complex and slower.
  - Transform coding: Transform coding is a lossless or lossy image compression technique that uses mathematical transformations to reduce the size of an image and commonly used for JPEGs. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress .

- Lossy compression: Lossy compression is a technique that discards some of the original data, resulting in some loss of quality or resolution. Lossy compression is suitable for images that can tolerate some degradation, such as photographs, videos, or web graphics. Lossy compression algorithms include:

  - Discrete cosine transform: Discrete cosine transform (DCT) is the most widely used form of lossy compression. It is a type of Fourier-related transform, and was originally developed by Nasir Ahmed, T. Natarajan and K. R. Rao in 1974. DCT transforms an image into a frequency domain, where the low-frequency components represent the general shape and color of the image, and the high-frequency components represent the fine details and edges. DCT then quantizes and encodes the frequency coefficients, discarding the ones that are less perceptible to the human eye. DCT is used in formats such as JPEG, MPEG, and MP3.
  - Wavelet transform: Wavelet transform is another form of lossy compression that uses wavelets, which are functions that can represent both frequency and spatial information. Wavelet transform decomposes an image into different levels of resolution, where each level contains a low-frequency subband and several high-frequency subbands. Wavelet transform then quantizes and encodes the subbands, discarding the ones that are less perceptible to the human eye. Wavelet transform is used in formats such as JPEG 2000, DjVu, and ECW.
  - Fractal compression: Fractal compression is a form of lossy compression that uses fractals, which are self-similar patterns that can be repeated at different scales. Fractal compression divides an image into blocks, and then finds the best match for each block from a set of predefined fractal shapes. Fractal compression then encodes the parameters of the fractal shapes, such as the scale, rotation, and color. Fractal compression can achieve high compression ratios, but it is very slow and complex.



### The Graphics Interchange Format (GIF) for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- GIF is a graphical image format that uses a variant of LZW (Lempel-Ziv-Welch) lossless data compression technique to reduce the file size without degrading the visual quality .
- GIF was introduced by CompuServe in 1987 to provide a color image format for their file downloading areas .
- GIF supports up to 8 bits per pixel for each image, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space.
- GIF also supports animations and allows a separate palette of up to 256 colors for each frame. The color limitation makes the GIF format unsuitable for reproducing color photographs and other images with color gradients, but it is well-suited for simpler images such as graphics or logos with solid areas of color.
- GIF images are compressed using the following steps:
  - The image is divided into blocks of 8x8 pixels, each block having its own color palette.
  - Each block is encoded using a variable-length code based on the LZW algorithm, which replaces repeated sequences of pixels with shorter codes.
  - The codes are stored in a data stream, preceded by a header that contains information such as the image size, the number of colors, and the compression method.
  - The data stream is optionally further compressed using a run-length encoding scheme, which replaces consecutive identical codes with a code and a count.
- GIF is a popular format for transmitting images and animations over the Internet, especially for web pages, because of its small file size and wide compatibility.
- However, GIF has some drawbacks, such as the limited color range, the patent issues with the LZW algorithm, and the lack of transparency and alpha channel support.
- PNG (Portable Network Graphics) is a newer image format that was designed to overcome some of the limitations of GIF, such as offering a larger color depth, a lossless compression method that does not use LZW, and support for transparency and alpha channel.



### Compression over Modems

- Compression over modems is a technique that allows modems to transmit data faster and more efficiently over phone lines by reducing the size of the data before sending it and expanding it after receiving it.
- Compression over modems can be done by using different algorithms and protocols that are agreed upon by both the sending and receiving modems. Some of the common protocols are V.42bis, MNP 5, and STAC.
- Compression over modems can increase the effective throughput of the data transmission by a factor of 2 to 4, depending on the type and redundancy of the data. For example, text files can be compressed more than images or audio files.
- Compression over modems can also improve the reliability and quality of the data transmission by reducing the number of bits that need to be sent and received, and by using error correction techniques to detect and correct errors that may occur due to noise or interference on the phone line.
- Compression over modems can be implemented by using hardware or software components that are integrated with the modem or the computer. Some examples of hardware components are the Compression Service Adapter (CSA) for Cisco routers and the Data Compression Advanced Integration Module (AIM) for Cisco 2600 series. Some examples of software components are the compression drivers or utilities that are installed on the computer or the modem.
- Compression over modems can be enabled or disabled by using the appropriate commands or settings on the modem or the computer. For example, to enable compression on a modem that supports V.42bis, the command AT+DS=3,0,0,0 can be used. To disable compression, the command AT+DS=0,0,0,0 can be used.



### V.42 bits for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- V.42bis is a data compression standard for data circuit terminating equipment (DCE) using error correcting procedures .
- It was adopted by the CCITT (now ITU-T) in 1990 and is widely used by modem manufacturers and network operators .
- It is based on the Lempel-Ziv-Welch (LZW) algorithm, which is a variant of the Ziv-Lempel family of algorithms for lossless data compression .
- It uses a dictionary-based approach, where sequences of input symbols are encoded as codes that refer to entries in a dictionary. The dictionary is dynamically updated as new sequences are encountered .
- It can achieve compression ratios of up to 4:1 for text and 2:1 for binary data, depending on the characteristics of the input data and the size of the dictionary .
- It operates in two modes: transparent mode and compressed mode. In transparent mode, the data is transmitted without compression. In compressed mode, the data is compressed using the LZW algorithm and the dictionary .
- It uses a negotiation procedure to establish the compression parameters, such as the dictionary size, the escape character, and the compression mode. The negotiation is done using the V.42 protocol, which also provides error correction and flow control .
- It uses a special escape character to switch between transparent mode and compressed mode, and to indicate the end of a compressed data block. The escape character is chosen by the DCE during the negotiation and is not used in the input data .
- It uses a limited recycling library, which means that the dictionary is not reset after each compressed data block, but only when it is full. This allows for better compression performance, but also introduces some overhead and complexity .
- It uses a delayed innovation technique, which means that the dictionary is updated only after a code has been transmitted, not before. This reduces the number of escape characters needed, but also increases the latency and the memory requirements .



### Predictive Coding

- Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits.
- The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding or Huffman coding.
- Predictive coding can achieve higher compression ratios than fixed-length codes, because the prediction error tends to have a lower entropy than the original data.
- Predictive coding can be applied to different types of data, such as audio, image, video, or text.
- Some examples of predictive coding algorithms are:
  - Linear predictive coding (LPC), which models the spectral envelope of a speech signal using a linear filter and encodes the filter coefficients and the residual signal.
  - Dynamic Markov compression (DMC), which models the probability distribution of the next bit in a binary sequence using a Markov chain and encodes the bits using arithmetic coding.
  - WebP, which is an image format that uses predictive coding to reduce the spatial redundancy in each block of pixels and encodes the residuals using a combination of Huffman coding and arithmetic coding.



### Prediction with Partial Match (PPM) for Data Compression

- PPM is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length context of the most recent symbols, and using it to look up the probability distribution of the next symbol in a table.
- PPM can handle any alphabet size, and can adapt to changes in the data statistics over time.
- PPM compresses the data by encoding each symbol with an arithmetic coder, using the predicted probability distribution as the model.
- PPM has several variants, such as PPM-A, PPM-B, PPM-C, PPM-D, PPM-Z, etc., which differ in how they handle the cases when the context is not found in the table, or when the predicted symbol is not in the distribution .
- PPM is one of the most effective and widely used data compression techniques, especially for natural language texts .



### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Coding a sequence is a technique of data compression that assigns codes to sequences of input bytes, rather than individual bytes.
- Coding a sequence can achieve better compression ratio than coding a symbol, especially for data with repeated patterns.
- One of the most popular coding a sequence algorithms is LZW (Lempel–Ziv–Welch) algorithm .
- The basic steps of LZW algorithm are :
  - Initialize a code table with 256 entries, corresponding to the ASCII codes of single characters.
  - Read the first input byte and store it as the current sequence.
  - While there are more input bytes, do the following:
    - Read the next input byte and append it to the current sequence.
    - If the current sequence is already in the code table, continue reading the next input byte.
    - Otherwise, output the code of the current sequence without the last input byte, and add the current sequence with the last input byte to the code table with a new code.
    - Reset the current sequence to the last input byte.
  - Output the code of the current sequence and stop.
- For example, suppose the input data is "ABABABA". The LZW algorithm will produce the following output:
  - Initialize the code table with 256 entries for single characters.
  - Read the first input byte "A" and store it as the current sequence.
  - Read the next input byte "B" and append it to the current sequence, forming "AB".
  - Since "AB" is not in the code table, output the code of "A" (65), and add "AB" to the code table with a new code (256).
  - Reset the current sequence to "B".
  - Read the next input byte "A" and append it to the current sequence, forming "BA".
  - Since "BA" is not in the code table, output the code of "B" (66), and add "BA" to the code table with a new code (257).
  - Reset the current sequence to "A".
  - Read the next input byte "B" and append it to the current sequence, forming "AB".
  - Since "AB" is in the code table, continue reading the next input byte.
  - Read the next input byte "A" and append it to the current sequence, forming "ABA".
  - Since "ABA" is not in the code table, output the code of "AB" (256), and add "ABA" to the code table with a new code (258).
  - Reset the current sequence to "A".
  - There are no more input bytes, so output the code of "A" (65) and stop.
  - The final output is 65, 66, 256, 65.



### The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The escape symbol is a special symbol that is used to indicate that a character or a sequence of characters is not in the codebook or the dictionary.
- The escape symbol is usually chosen to be a character that is unlikely to appear in the original data, such as `#`, `@`, or `^`.
- The escape symbol is followed by the raw representation of the character or the sequence of characters that is not in the codebook or the dictionary.
- The escape symbol allows the encoder and the decoder to handle new or rare symbols that are not in the codebook or the dictionary, without having to update or transmit the codebook or the dictionary.
- The escape symbol also allows the encoder and the decoder to handle variable-length codes, such as Huffman codes or Lempel-Ziv codes, without having to use end-of-block markers or padding bits.
- The escape symbol can improve the compression ratio if the frequency of new or rare symbols is low, but it can also degrade the compression ratio if the frequency of new or rare symbols is high, or if the raw representation of the symbols is longer than the codebook or the dictionary entries.



### Length of context for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The length of context is the number of symbols that are used to predict the next symbol in a sequence.
- The length of context affects the performance of the compression algorithm, as it determines how well the algorithm can capture the statistical properties of the source data.
- A longer context can provide more information about the probabilities of the next symbol, but it also requires more memory and computation to store and process the context.
- A shorter context can reduce the memory and computation requirements, but it may also lose some information about the source data and result in lower compression ratios.
- The optimal length of context depends on the characteristics of the source data and the compression algorithm. There is no universal rule for choosing the best length of context, but some general guidelines are:
  - For sources with high entropy (i.e., unpredictable or random data), a shorter context may be sufficient, as a longer context may not provide much benefit in terms of compression.
  - For sources with low entropy (i.e., predictable or regular data), a longer context may be beneficial, as it can capture the patterns and correlations in the data and improve the compression ratio.
  - For sources with varying entropy (i.e., data that changes its statistical properties over time), a variable-length context may be preferable, as it can adapt to the changes in the data and achieve a balance between compression and complexity.



### The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The exclusion principle is a technique for encoding a sequence of symbols by using a prefix code that avoids any ambiguity in decoding.
- A prefix code is a code where no codeword is a prefix of another codeword. For example, the code {0, 10, 11} is a prefix code, but the code {0, 01, 10} is not, because 0 is a prefix of 01 and 10.
- The exclusion principle states that if we want to encode a symbol x that has not appeared before in the sequence, we can use any codeword that is not a prefix of any existing codeword. For example, if the existing codewords are {0, 10, 11}, we can use 01, 001, 0001, etc. to encode x, but not 0, 100, 110, etc.
- The exclusion principle ensures that the decoder can uniquely recover the original sequence from the encoded sequence, by using a greedy algorithm that matches the longest possible prefix at each step. For example, if the encoded sequence is 0110010, the decoder can split it into 01|10|010, and decode each codeword according to the code table.
- The exclusion principle can be used to construct a dynamic code that adapts to the frequency of the symbols in the sequence. For example, we can start with an empty code table, and assign a new codeword to each new symbol that appears, using the exclusion principle. This way, the code will assign shorter codewords to more frequent symbols, and longer codewords to less frequent symbols, achieving some compression.



### The Burrows-Wheeler Transform for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The Burrows-Wheeler Transform (BWT) is a reversible transformation that rearranges the characters of a text in a way that makes it more compressible by other methods.
- The BWT is based on the idea of sorting all the cyclic rotations of the text and taking the last column of the sorted matrix as the output.
- The BWT preserves the relative order of the characters in the text, but groups together the characters that are likely to appear in the same context, such as the same word or phrase.
- The BWT can be reversed by using the first and last columns of the sorted matrix and applying a reconstruction algorithm that restores the original text.
- The BWT can be combined with other compression techniques, such as move-to-front coding, run-length encoding, and arithmetic coding, to achieve high compression ratios.



### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but rearranges the data to make it more suitable for entropy encoding techniques of compression  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is updated dynamically as the data is processed. The list is initially sorted in some order, such as lexicographic or frequency-based. 
- For each symbol in the data, the algorithm outputs the index of that symbol in the list, and then moves that symbol to the front of the list. This way, the symbols that occur frequently in the data will have smaller indices and will be closer to the front of the list, making them easier to encode with variable-length codes  .
- Movetofront coding is an invertible transformation, meaning that the original data can be recovered from the transformed data and the initial list. The decoding algorithm simply reverses the encoding process: it maintains the same list of symbols, reads each index from the transformed data, outputs the symbol at that index in the list, and then moves that symbol to the front of the list  .
- Movetofront coding is often used as a preprocessing step in data compression algorithms, such as Burrows–Wheeler transform, arithmetic coding, and Huffman coding. It can improve the compression ratio by reducing the entropy of the data and exploiting the local correlations and repetitions in the data   .
- Movetofront coding is fast and simple to implement, requiring only linear time and constant space. It can also adapt to changes in the data distribution without requiring any parameter tuning or training  .
- An example of movetofront coding is shown below, using the alphabet A = {a, b, c, d, e} and the data "abracadabra":

| Symbol | Index | List |
|--------|-------|------|
| a      | 0     | a, b, c, d, e |
| b      | 1     | b, a, c, d, e |
| r      | 4     | r, b, a, c, d |
| a      | 2     | a, r, b, c, d |
| c      | 3     | c, a, r, b, d |
| a      | 1     | a, c, r, b, d |
| d      | 4     | d, a, c, r, b |
| a      | 1     | a, d, c, r, b |
| b      | 3     | b, a, d, c, r |
| r      | 4     | r, b, a, d, c |
| a      | 2     | a, r, b, d, c |

- The transformed data is the sequence of indices: 0, 1, 4, 2, 3, 1, 4, 1, 3, 4, 2. This sequence can be further compressed using entropy encoding techniques.



### CALIC for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- CALIC stands for Context-based, Adaptive, Lossless Image Coding  .
- It is a codec that obtains higher lossless compression of continuous-tone images than other lossless image coding techniques in the literature  .
- It has relatively low time and space complexities  .
- It puts heavy emphasis on image data modeling  .
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics .
- The non-linear predictor adapts via an error feedback mechanism .
- It also uses a context-based binary arithmetic coder to encode the prediction residuals .
- It can be applied to compound video compression with motion compensation to obtain lossless compression and increased visual quality.




### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes .
- JPEG-LS is based on the LOCO-I algorithm (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- Modeling stage: predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error .
- Encoding stage: encodes the prediction error using a Golomb-Rice code, which adapts to the local statistics of the error distribution .
- JPEG-LS has low complexity, high compression performance, and fast encoding and decoding .
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), which defines the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), which contains the extensions.
- JPEG-LS extensions include: region of interest coding, hierarchical coding, progressive coding, and arithmetic coding.
- JPEG-LS is suitable for applications that require high-quality images, such as medical imaging, remote sensing, and archival.



### Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of detail or resolution to represent or process data, such as images, signals, or geometries.
- The main advantages of multi-resolution approaches are:
  - They can capture the global and local features of the data more efficiently and accurately.
  - They can reduce the computational complexity and memory requirements of the algorithms by working on coarser scales first and then refining the results on finer scales.
  - They can adapt to the data characteristics and the user requirements by selecting the appropriate resolution level for each task or region of interest.
- The main components of a multi-resolution approach are:
  - A coarsening operator that reduces the resolution of the data by removing or aggregating some details.
  - A refinement operator that increases the resolution of the data by adding or restoring some details.
  - An adaptation strategy that decides when and where to apply the coarsening or refinement operators based on some criteria, such as error estimation, visual quality, or user input.
- Some examples of multi-resolution approaches are:
  - Wavelet transforms, which decompose a signal or an image into a series of coefficients that represent the details at different scales and orientations.
  - Fractal transforms, which approximate an image by a set of self-similar patterns that can be scaled and transformed to match the image at different resolutions.
  - Adaptive mesh refinement, which dynamically adjusts the grid size and shape to resolve the regions of interest in a numerical simulation.
  - Multi-resolution vector data compression, which simplifies the geometries of vector data by removing or merging vertices and edges according to a visual lossless distance criterion.



### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding exploits the fact that most documents have large areas of white or black pixels, and uses run-length coding to encode the lengths of consecutive runs of the same color.
- Run-length coding is a simple technique that replaces a sequence of identical symbols with a pair of the symbol and its count. For example, the sequence `WWWWWWWWWW` can be encoded as `(W,10)`.
- Facsimile encoding uses two types of run-length codes: white codes and black codes. White codes are used to encode runs of white pixels, and black codes are used to encode runs of black pixels.
- Facsimile encoding also uses two modes: horizontal mode and vertical mode. Horizontal mode encodes two consecutive runs of different colors on the same scan line. Vertical mode encodes the position of the first changing pixel on the next scan line relative to the current scan line.
- Facsimile encoding uses a variable-length codebook to assign binary codes to each run-length code or vertical mode code. The codebook is designed to minimize the average code length, and is based on the Huffman method or the arithmetic coding method.
- The Huffman method assigns shorter codes to more frequent symbols, and longer codes to less frequent symbols. The arithmetic coding method assigns codes to symbols based on their probabilities, and can achieve optimal compression.
- Facsimile encoding can reduce the transmission requirements of facsimile images while maintaining high intelligibility in mobile communications environments. Facsimile encoding can also be applied to the lossless compression of images with low color depth or high redundancy.



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1 .
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input .
- Each node stores a count of how many times each bit has followed the context, and these counts are used to estimate the conditional probabilities of the next bit given the context .
- The arithmetic coder uses these probabilities to encode or decode each bit of the input, and updates the model accordingly .
- DMC is an adaptive algorithm, meaning that it adjusts to the changing characteristics of the input data as it processes it .
- DMC can achieve high compression ratios for various types of data, especially those with regular patterns or long-range dependencies .
- DMC is also relatively simple and fast, compared to other compression algorithms that use more complex models or larger contexts .



## Unit 4 - Distortion criteria

- Distortion criteria are the measures of how well a communication system preserves the fidelity of the transmitted signal.
- Distortion criteria can be classified into two categories: linear and nonlinear.
- Linear distortion criteria are based on the assumption that the system is linear, meaning that the output signal is a scaled and shifted version of the input signal.
- Nonlinear distortion criteria are based on the assumption that the system is nonlinear, meaning that the output signal is a distorted version of the input signal that depends on the amplitude and frequency of the input signal.
- Some examples of linear distortion criteria are:
  - Amplitude distortion: the variation of the amplitude response of the system with frequency.
  - Phase distortion: the variation of the phase response of the system with frequency.
  - Group delay distortion: the variation of the group delay of the system with frequency. Group delay is the time difference between the input and output signals at a given frequency.
- Some examples of nonlinear distortion criteria are:
  - Harmonic distortion: the generation of harmonics or multiples of the input frequency in the output signal.
  - Intermodulation distortion: the generation of intermodulation products or combinations of the input frequencies in the output signal.
  - Cross-talk distortion: the leakage of signals from one channel to another in a multi-channel system.



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Distortion criteria are used to measure the quality of the approximation of the original data by the compressed data.
- Distortion criteria depend on the type and application of the data, such as images, audio, video, text, etc.
- Distortion criteria can be classified into two categories: objective and subjective.
  - Objective distortion criteria are based on mathematical formulas that compare the original and reconstructed data, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc.
  - Subjective distortion criteria are based on human perception and evaluation of the quality of the compressed data, such as mean opinion score (MOS), just noticeable difference (JND), etc.
- Distortion criteria are related to the rate-distortion theory, which studies the trade-off between the compression rate and the distortion level of the compressed data.
  - The rate-distortion theory defines the rate-distortion function R(D) as the minimum achievable compression rate for a given distortion level D.
  - The rate-distortion function R(D) depends on the source statistics and the distortion measure used.
  - The rate-distortion function R(D) can be computed by an iterative algorithm called the Blahut-Arimoto algorithm.
  - The rate-distortion function R(D) provides a lower bound for the performance of any practical compression system.



### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of symbols, called quantization levels or reconstruction values .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the precision of the signal representation and introduces quantization error or distortion.
- Scalar quantization can be performed on signal samples one at a time, or on blocks of samples, depending on the application and the desired trade-off between complexity and performance .
- Scalar quantization can be classified into two types: uniform and nonuniform .
  - Uniform scalar quantization uses equal-sized intervals or bins to partition the signal range, and assigns a fixed reconstruction value to each bin .
  - Nonuniform scalar quantization uses variable-sized intervals or bins to partition the signal range, and assigns a reconstruction value to each bin based on some criterion, such as minimizing the mean squared error or maximizing the entropy .
- Scalar quantization can be further divided into two categories: midtread and midrise .
  - Midtread scalar quantization uses a zero bin that contains the origin, and assigns a zero reconstruction value to it .
  - Midrise scalar quantization uses a half bin that contains the origin, and assigns a nonzero reconstruction value to it .
- Scalar quantization can be optimized by using techniques such as Lloyd-Max algorithm, companding, dead-zone quantization, and adaptive quantization .
- Scalar quantization can be applied to various types of signals, such as speech, audio, image, and video, and can be combined with other compression methods, such as transform coding, differential coding, and entropy coding  .
- Scalar quantization is not optimal for signals that have correlation or dependence among samples, as it does not exploit the statistical properties of the signal . A better alternative is vector quantization, which quantizes blocks of samples as a whole.



### The Quantization Problem

- Quantization is a process of mapping a large set of input values to a smaller set of output values, with some loss of information.
- Quantization is used in data compression to reduce the number of bits needed to represent a signal, image, or video.
- The quantization problem is to find the optimal way of quantizing a given source, such that the distortion between the original and the quantized data is minimized, subject to some constraints on the bit rate, complexity, or quality.
- The quantization problem can be formulated as an optimization problem, where the objective function is the distortion measure, and the constraints are the number of output levels, the codebook, the partition, or the entropy.
- The quantization problem can be solved in different ways, depending on the type of source, the type of quantizer, and the type of distortion measure.
- Some common types of quantizers are uniform, non-uniform, scalar, vector, and adaptive quantizers.
- Some common types of distortion measures are mean squared error, signal-to-noise ratio, peak signal-to-noise ratio, and perceptual distortion measures.
- Some common methods of solving the quantization problem are the Lloyd algorithm, the K-means algorithm, the LBG algorithm, and the Riemann algorithm.



### Uniform Quantizer

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values to a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels .
- A uniform quantizer can be classified into two types: mid-tread and mid-rise .
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero .
  - A mid-rise quantizer has no zero output level and the output levels are shifted by $\Delta/2$ from the mid-tread quantizer .
- A uniform quantizer can be used for data compression by encoding the output levels with a fixed number of bits .
- A uniform quantizer can achieve optimal performance in terms of mean squared error (MSE) when the input values are uniformly distributed .
- A uniform quantizer can be combined with a companding function to achieve non-uniform quantization, which can better match the input distribution and reduce the distortion .
  - A companding function is a nonlinear function that compresses the input values before quantization and expands them after quantization .
  - Two common companding functions are the $\mu$-law and the A-law, which are used for PCM telephone systems .
- A uniform quantizer can be incorporated into a deep learning based image compression framework, where the feature maps between the encoder and decoder are quantized .
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the rate-distortion trade-off, which balances the compression ratio and the reconstruction quality .



### Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input data.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters, such as synthetic aperture radar (SAR) raw data.
- An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution, minimizing the distortion for a given bit rate.
- There are two main types of adaptive quantization: forward and backward.
  - Forward adaptive quantization divides the input into blocks and computes the quantizer parameters for each block. These parameters are transmitted to the receiver as side information. For example, in uniform quantization, the minimum and maximum values of each block can be used to determine the quantizer step size.
  - Backward adaptive quantization uses feedback from the receiver to adjust the quantizer parameters. The receiver sends back the quantization error or the reconstructed signal to the transmitter, which then updates the quantizer accordingly. For example, in differential pulse-code modulation (DPCM), the quantizer can be adapted based on the prediction error.
- Adaptive quantization can improve the performance of data compression by reducing the quantization noise and the redundancy of the source. However, it also introduces some challenges, such as the overhead of transmitting the quantizer parameters, the delay of feedback, and the complexity of the quantizer design.



### Non uniform Quantization

- Non uniform quantization is a generalization of uniform quantization, where the quantization points are not distributed evenly  .
- Non uniform quantization can be optimized via the back-propagation of the network gradients, which makes it more expressive to approximate the original full-precision network compared to uniform quantization .
- Non uniform quantization can be applied to sources with an arbitrary distribution of values, such as speech signals, images, or neural networks  .
- Non uniform quantization can be classified into two types: companding and adaptive .
  - Companding is a technique that applies a nonlinear function to the input signal before quantizing it uniformly. The nonlinear function compresses the high-amplitude values and expands the low-amplitude values, resulting in a more uniform distribution of the quantization error .
  - Adaptive is a technique that adjusts the quantization intervals according to the statistics of the input signal. The quantization intervals are made smaller for regions with high probability density and larger for regions with low probability density, resulting in a lower average quantization error .
- Non uniform quantization can reduce the distortion and improve the signal-to-quantization-noise ratio (SQNR) compared to uniform quantization, especially for low-bit quantization   .



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of similar vectors (such as image blocks or speech frames) by a single representative vector, called a codevector.
- Scalar quantization (SQ) is a technique that compresses data by representing each individual sample (such as a pixel or a speech sample) by a single representative value, called a codeword.
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ, since it exploits the correlation between adjacent samples in the data. For example, in an image, neighboring pixels tend to have similar values, so they can be grouped into a vector and represented by a single codevector. SQ, on the other hand, treats each pixel independently, so it requires more bits to represent the same information.
  - VQ can reduce the quantization noise and distortion compared to SQ, since it minimizes the mean squared error (MSE) between the original vectors and the codevectors. SQ, on the other hand, minimizes the MSE between the original samples and the codewords, which may not capture the overall similarity between the vectors.
  - VQ can adapt to the statistics of the data, since it can use different codebooks for different regions or classes of the data. For example, in speech coding, VQ can use different codebooks for voiced and unvoiced segments, or for different phonemes. SQ, on the other hand, uses a fixed codebook for the whole data, which may not match the characteristics of the data well.
  - VQ can handle non-uniform data distributions better than SQ, since it can allocate more codevectors to the regions or classes of the data that have higher probability or importance. For example, in image coding, VQ can allocate more codevectors to the edges or textures of the image, which are more perceptually significant. SQ, on the other hand, uses a uniform quantization scheme, which may not reflect the perceptual relevance of the data.



### The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook from a given set of training vectors .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in the input space with a certain distortion.
- The LBG algorithm is similar to the k-means algorithm in data clustering, but it uses a binary splitting technique to generate the codebook iteratively .
- The LBG algorithm consists of the following steps :
  - Initialize the codebook with one codeword, which is the centroid of the training set.
  - Split each codeword in the codebook into two slightly perturbed versions, doubling the size of the codebook.
  - Assign each training vector to the nearest codeword in the codebook, forming clusters of vectors.
  - Update each codeword by computing the centroid of its corresponding cluster, minimizing the distortion within the cluster.
  - Repeat steps 3 and 4 until the distortion measure converges or reaches a predefined threshold.
  - Repeat steps 2 to 5 until the desired codebook size is reached.

### Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of vectors (such as image blocks, speech frames, etc.) with a smaller set of codewords from a codebook.
- Scalar quantization (SQ) is a technique that compresses data by representing each scalar value (such as a pixel, a sample, etc.) with a smaller set of discrete levels from a quantizer.
- VQ has some advantages over SQ, such as :
  - VQ can exploit the correlation among the components of a vector, while SQ treats each component independently.
  - VQ can achieve a lower distortion (or a higher compression ratio) than SQ for the same number of bits per vector (or per scalar).
  - VQ can adapt to the statistics of the input data by using a codebook that matches the data distribution, while SQ uses a fixed quantizer that may not be optimal for the data.
  - VQ can handle nonuniform and nonlinear data better than SQ, which assumes a uniform and linear data model.



### Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the final codebook vectors.
- The advantage of TSVQ is that it can be represented and stored efficiently using a binary tree, and it can provide fast quantization search by following a root-to-leaf path. The quantization error can also be controlled by adjusting the depth of the tree.
- TSVQ can be designed using a top-down or a bottom-up approach. The top-down approach starts with the average of all the training vectors, and splits each node into two subnodes by perturbing the vector slightly. The bottom-up approach starts with a large number of codebook vectors, and merges them into a tree by minimizing the distortion.
- TSVQ can be applied to various types of data, such as speech, image, and video. It can also be combined with other techniques, such as entropy coding, to achieve better compression performance .



### Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity and the storage requirements of the quantization process .
- Vector quantization is a technique that maps a vector of continuous or discrete values (such as an image block or a speech segment) to a finite set of code vectors, each representing a region or a cell in the input space.
- Vector quantization is superior to scalar quantization, which operates on single values, in terms of rate-distortion performance, i.e., the trade-off between the bit rate and the quantization error .
- However, vector quantization also has some drawbacks, such as the high computational complexity of finding the optimal codebook and the optimal code vector for each input vector, and the large storage space needed to store the codebook  .
- Structured vector quantizers aim to overcome these drawbacks by using some forms of regularity or hierarchy in the codebook or the partition, such as tree structures, product structures, lattice structures, etc  .
- Structured vector quantizers can reduce the search time, the encoding rate, the storage cost, or the distortion of the quantization process, depending on the design criteria and the structure used .
- Structured vector quantizers can also exploit some properties of the input vectors, such as correlation, sparsity, or locality, to improve the quantization performance .
- Structured vector quantizers are widely used in applications such as image and video compression, speech coding, pattern recognition, data clustering, etc .

