

## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data or information without losing its quality or meaning.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the original data exactly and allow for perfect reconstruction of the original data from the compressed data. Examples of lossless compression techniques are Huffman coding, run-length encoding, Lempel-Ziv algorithm, etc.
- Lossy compression techniques discard some information from the original data and allow for approximate reconstruction of the original data from the compressed data. Examples of lossy compression techniques are JPEG, MP3, MPEG, etc.
- Compression techniques can be applied to different types of data, such as text, images, audio, video, etc.
- Compression techniques can have various benefits, such as saving storage space, reducing transmission time, improving performance, enhancing security, etc.



# Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values or patterns are more frequent than others and can be encoded with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and lossless audio formats .
- Lossless compression can reduce the file size by removing unnecessary or redundant information, such as spaces, punctuation, or repeated characters, or by using more efficient encoding schemes, such as Huffman coding, arithmetic coding, or Lempel-Ziv coding.
- Lossless compression can also be achieved by applying transformations to the data, such as run-length encoding, delta encoding, or Burrows-Wheeler transform, that make it more suitable for compression.
- Lossless compression has a limit on how much it can compress a given data set, which depends on the entropy or randomness of the data. The lower the entropy, the higher the compression ratio.
- Lossless compression is different from lossy compression, which discards some information from the original data to achieve higher compression ratios, but at the cost of quality degradation. Lossy compression is often used for images, video, and audio that can tolerate some imperfections .



# Lossy Compression

- Lossy compression is a data compression method that sacrifices some information to achieve an even smaller file size than lossless compression.
- Lossy compression is often used on video, audio, and many types of image files.
- Lossy compression removes background data and approximates certain details of an image file, making it smaller and easier to handle, store or send.
- However, in return for a more manageable file size, you will lose data permanently, hence the term 'lossy'.
- Lossy compression does not decompress back to 100% original quality.
- Lossy compression is useful when the exact reproduction of the original data is not necessary or when some loss of quality is acceptable.
- Some examples of lossy compression formats are JPEG, MP3, MPEG, and GIF.



# Measures of performance for compression techniques

Compression techniques are methods of reducing the size of data without losing essential information. Compression techniques can improve the efficiency of data storage, transmission, and processing. However, compression techniques also have some trade-offs, such as increased complexity, overhead, and distortion. Therefore, it is important to measure the performance of compression techniques using various metrics and criteria.

Some of the common measures of performance for compression techniques are:

- **Compression ratio (CR)**: This is the ratio of the original data size to the compressed data size. It indicates how much the data has been reduced by compression. A higher compression ratio means a higher compression efficiency. CR can be calculated as:

  CR = original data size / compressed data size

- **Compression factor (CF)**: This is the inverse of the compression ratio. It indicates how many times the original data can fit into the compressed data. A lower compression factor means a higher compression efficiency. CF can be calculated as:

  CF = compressed data size / original data size

- **Bits per character (bpc)**: This is the average number of bits used to represent each character in the compressed data. It indicates how compact the compressed data is. A lower bits per character means a higher compression efficiency. bpc can be calculated as:

  bpc = compressed data size / number of characters in original data

- **Distortion**: This is the difference between the original data and the decompressed data. It indicates how much the data has been altered by compression. Distortion can be measured by various methods, such as mean squared error (MSE), root mean squared error (RMSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc. A lower distortion means a higher compression quality.

- **Complexity**: This is the amount of computation and memory required to perform compression and decompression. It indicates how fast and easy the compression technique is. Complexity can be measured by various methods, such as time complexity, space complexity, algorithmic complexity, etc. A lower complexity means a higher compression performance.

- **Accuracy**: This is the degree of correctness and completeness of the compressed data. It indicates how well the compressed data preserves the essential information of the original data. Accuracy can be measured by various methods, such as error rate, precision, recall, F-measure, etc. A higher accuracy means a higher compression performance.

Depending on the type and application of the data, different measures of performance may have different weights and importance. For example, for text compression, CR, CF, and bpc may be more important than distortion and accuracy, while for image compression, distortion and accuracy may be more important than CR, CF, and bpc. Therefore, it is necessary to choose the appropriate measures of performance for the specific compression technique and data.



# Modeling and coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Modeling and coding are two fundamental steps in data compression.
- Modeling is the process of finding a suitable representation of the data that captures its essential features and reduces its redundancy.
- Coding is the process of assigning binary codes to the symbols or units of the model, such that the length of the code reflects the probability or frequency of the symbol.
- There are two main types of models: statistical and dictionary-based.
- Statistical models use the probability distribution of the data to assign codes to the symbols. The most common statistical models are Huffman coding and arithmetic coding.
- Dictionary-based models use a predefined or adaptive set of strings to represent the data. The most common dictionary-based models are LZ77, LZ78, and LZW.
- The choice of the model and the coding scheme depends on the characteristics of the data and the compression objectives. Some factors that affect the choice are:
  - The size and complexity of the data
  - The type and amount of redundancy in the data
  - The desired compression ratio and quality
  - The computational and memory resources available
  - The encoding and decoding speed and complexity
- Modeling and coding are often combined or integrated to achieve better compression performance and efficiency. Some examples of integrated methods are:
  - Adaptive Huffman coding, which updates the model and the code dynamically based on the data
  - Run-length encoding, which uses a simple model of repeated symbols and a fixed-length code
  - Burrows-Wheeler transform, which transforms the data into a more compressible form and then applies a statistical or dictionary-based coding
  - JPEG, which uses a discrete cosine transform to model the image blocks and a Huffman or arithmetic coding to encode the coefficients



# Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files .
- Lossless compression is based on the concept of entropy, which measures the amount of uncertainty or randomness in a data source .
- Entropy is defined as the average number of bits needed to encode a symbol from the source, assuming an optimal encoding scheme .
- Entropy can be calculated using the formula: H(X) = - sum(p(x) log p(x)), where X is the source, p(x) is the probability of a symbol x, and log is the logarithm base 2 .
- Entropy is a lower bound for the compression ratio, which is the ratio of the compressed size to the original size. The compression ratio cannot be lower than the entropy of the source .
- Lossless compression techniques can be classified into two categories: statistical and dictionary-based .
- Statistical techniques use the probability distribution of the source symbols to assign variable-length codes to each symbol. The more frequent symbols are assigned shorter codes, and the less frequent symbols are assigned longer codes .
- Dictionary-based techniques use a predefined or dynamically generated dictionary of strings to replace repeated occurrences of the same string with a shorter code. The dictionary can be shared or transmitted along with the compressed data .
- Some examples of lossless compression algorithms are Huffman coding, arithmetic coding, Lempel-Ziv-Welch (LZW) algorithm, and run-length encoding (RLE) .



# A brief introduction to information theory

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding schemes.
- Information theory has applications in various fields, such as communication, cryptography, compression, statistics, machine learning, and biology.
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be either 0 or 1.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared by two random variables.
- Information theory also studies the optimal ways of encoding and decoding information, such as lossless and lossy compression, which aim to reduce the size of data without or with some loss of information, respectively, or error-correcting codes, which add redundancy to data to enable detection and correction of errors during transmission.
- Information theory also analyzes the limits and trade-offs of communication systems, such as channel capacity, which is the maximum rate of information that can be reliably transmitted over a noisy channel, or rate-distortion theory, which studies the minimum distortion that can be achieved for a given rate of compression.



# Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing information or degrading its quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression, while lossy compression techniques discard some information and produce an approximation of the original data after decompression.
- Lossless compression techniques are suitable for applications that require exact reproduction of the original data, such as text, audio, or executable files.
- Lossy compression techniques are suitable for applications that can tolerate some degradation of the original data, such as images, video, or speech.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): replaces consecutive identical symbols with a symbol and a count.
  - Huffman coding: assigns variable-length codes to symbols based on their frequencies of occurrence.
  - Lempel-Ziv coding: exploits the repetition of patterns in the data by using pointers to previous occurrences.
  - Arithmetic coding: assigns codes to symbols based on their probabilities of occurrence and the context of the data.
- Some common lossy compression techniques are:
  - Transform coding: transforms the data into a different domain, such as frequency or wavelet, and discards the less significant components.
  - Quantization: reduces the number of bits used to represent each symbol by grouping them into levels or bins.
  - Vector quantization: represents blocks of data as vectors and assigns them to clusters or codebooks.
  - Differential coding: encodes the difference between successive symbols rather than the symbols themselves.
  - Predictive coding: predicts the next symbol based on the previous symbols and encodes the error or residual.



# Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. Physical models are useful for data compression because they allow us to estimate the probability distribution of the data and design optimal codes based on the model. Some of the common physical models for data compression are:

- **Uniform model**: This model assumes that all the symbols in the data are equally likely to occur. This model is suitable for data that has no structure or correlation, such as random noise. The optimal code for this model is a fixed-length code, where each symbol is assigned a code of the same length.

- **Binary symmetric model**: This model assumes that the data consists of binary symbols (0 or 1) and that the probability of a symbol being 0 or 1 is the same for all positions in the data. This model is suitable for data that has some structure or correlation, such as text or images. The optimal code for this model is a variable-length code, such as Huffman code, where the more frequent symbols are assigned shorter codes.

- **Markov model**: This model assumes that the data consists of symbols from a finite alphabet and that the probability of a symbol depends only on the previous k symbols, where k is a fixed parameter. This model is particularly useful for text compression, where the probability of the next letter is heavily influenced by the preceding letters. The optimal code for this model is a context-dependent code, where the code for each symbol depends on the previous k symbols.

- **Dictionary model**: This model assumes that the data consists of symbols from a finite alphabet and that the data can be divided into segments that are repeated throughout the data. This model is suitable for data that has a lot of redundancy or repetition, such as natural language or DNA sequences. The optimal code for this model is a dictionary-based code, where each segment is assigned a code based on its position in a predefined or adaptive dictionary.



# Probability models for data compression

- Probability models are mathematical representations of the source data that assign probabilities to different symbols or sequences of symbols.
- Probability models are used to estimate the entropy or information content of the source data, which is the lower bound for the compression ratio.
- Probability models are also used to design optimal codes that assign shorter codewords to more probable symbols or sequences, and longer codewords to less probable ones.
- Probability models can be classified into two types: static and adaptive.
  - Static models are fixed and do not change during the compression process. They are based on some prior knowledge or analysis of the source data.
  - Adaptive models are dynamic and change during the compression process. They are based on the observed frequencies or statistics of the source data.
- Some examples of probability models are:
  - Uniform model: This model assumes that all symbols in the source alphabet have equal probability. It is suitable for random or unpredictable data, but not for data with patterns or structure.
  - Bernoulli model: This model assumes that the source data consists of binary symbols (0 or 1) that have a fixed probability p of being 1 and 1-p of being 0. It is suitable for data with a constant bias or skewness.
  - Markov model: This model assumes that the probability of a symbol depends on the previous k symbols, where k is the order of the model. It is suitable for data with dependencies or correlations among symbols, such as text or speech.
  - Dictionary model: This model assumes that the source data consists of words or phrases that are drawn from a finite set or dictionary. It is suitable for data with repetitions or commonalities, such as natural language or DNA sequences.



# Markov models for data compression

- A Markov model is a mathematical model that describes a system that changes its state according to some probabilistic rules.
- A Markov model can be used to model the statistical properties of a source of data, such as a text, an image, or a speech signal.
- A Markov model can be used to predict the next symbol in a sequence of data, based on the previous symbols and their probabilities.
- A Markov model can be used as a basis for data compression, by encoding the symbols with fewer bits according to their probabilities, and decoding them using the same model.
- A Markov model can be of different orders, depending on how many previous symbols are used to predict the next one. A zero-order Markov model assumes that each symbol is independent of the others, while a higher-order Markov model captures more dependencies and correlations among the symbols.
- A Markov model can be static or dynamic. A static Markov model has fixed probabilities that are determined before the compression process, while a dynamic Markov model adapts its probabilities during the compression process, based on the observed data.
- A Markov model can be combined with an arithmetic coding scheme, which is a lossless data compression technique that assigns variable-length codes to the symbols, based on their probabilities. The codes are generated by dividing a unit interval into subintervals, and assigning each symbol to a subinterval proportional to its probability. The codes are then decoded by locating the subinterval that contains the encoded value, and retrieving the corresponding symbol.
- A Markov model can be combined with a dynamic arithmetic coding scheme, which is an adaptive version of arithmetic coding that updates the probabilities and the subintervals as new symbols are encoded or decoded. This allows the compression to adjust to the changing characteristics of the data, and achieve better compression ratios.
- A Markov model can be combined with a dynamic arithmetic coding scheme to form a data compression algorithm called dynamic Markov compression (DMC), which was developed by Gordon Cormack and Nigel Horspool. DMC predicts the next bit in a binary sequence, based on a dynamic Markov model of order one, and encodes or decodes it using a dynamic arithmetic coding scheme. DMC is similar to prediction by partial matching (PPM), except that it operates on bits rather than bytes, which makes it slower but gives slightly better compression. DMC is used as a model or submodel in several highly experimental implementations.



# Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be useful for data compression when a single model is not adequate to capture the characteristics of the data.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub>.
- A composite source model can be used to describe some very complicated processes, such as natural language, speech, images, etc.
- A composite source model can be combined with different coding techniques, such as Huffman coding, arithmetic coding, run-length encoding, etc., to achieve efficient data compression.
- A composite source model can also be used to enrich an existing data source by adding new measures or calculations that are not available in the original source .
- A composite source model can be implemented in various tools and platforms, such as Power BI, which allows connecting to multiple data sources and creating a composite model .



# Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can reduce the storage space or transmission time of data, and improve the performance and efficiency of data processing.
- Data compression can be classified into two types: lossless and lossy.
  - Lossless compression preserves the exact information of the original data, and allows the original data to be reconstructed from the compressed data.
  - Lossy compression discards some information of the original data, and allows the compressed data to be approximated to the original data.
  - Lossless compression is suitable for text, audio, and executable files, while lossy compression is suitable for images, video, and speech files.
- Data compression can be performed by using various techniques, such as:
  - Run length encoding (RLE): a lossless technique that replaces repeated characters or pixels with a count and a symbol.
  - Lempel-Ziv (LZ): a lossless technique that finds repeated patterns in a data set and replaces them with tokens or shortened sequences.
  - Huffman coding: a lossless technique that assigns variable-length codes to symbols based on their frequencies.
  - Arithmetic coding: a lossless technique that assigns codes to symbols based on their probabilities.
  - Dictionary coding: a lossless technique that uses a predefined dictionary of symbols and codes.
  - Transform coding: a lossy technique that transforms the data into a different domain, such as frequency or wavelet, and discards the less important components.
  - Quantization: a lossy technique that reduces the number of possible values of a data set by rounding or grouping them.
  - Predictive coding: a lossy technique that predicts the next value of a data set based on the previous values and encodes the difference.
- Data compression can be improved by using best practices, such as:
  - Determining the compression level: depending on the needs, the data can be compressed to a certain level, such as low, medium, or high.
  - Choosing the appropriate compression type: for every file, the compression type should match the data type, such as lossless or lossy.
  - Using a coprocessor: a dedicated hardware device that can perform compression faster and more efficiently than a general-purpose processor.
  - Considering data deduplication: a technique that eliminates duplicate or redundant data blocks and stores only one copy of them.
  - Determining if multi-stage compression is needed: a technique that applies more than one compression method to the data, such as RLE followed by LZ.



# Uniquely Decodable Codes

- A code is a mapping from a set of symbols (source alphabet) to a set of binary strings (code words).
- A code is uniquely decodable if there is only one way to decode any sequence of code words back to the original symbols.
- A code is non-singular if no two different symbols have the same code word.
- A code is instantaneous if the end of any code word is recognizable without examining subsequent code symbols.
- A code is prefix-free if no code word is a prefix of another code word. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average code word length for a given source alphabet and probability distribution.

## Examples

- Consider the code M1 = {a -> 0, b -> 10, c -> 110, d -> 111}. This code is prefix-free, instantaneous, uniquely decodable, and optimal for a source alphabet of four symbols with probabilities 0.5, 0.25, 0.125, and 0.125 respectively.
- Consider the code M2 = {a -> 0, b -> 01, c -> 011}. This code is non-singular, but not uniquely decodable, because the sequence 0110 could be decoded as either ab or ca. This code is also not instantaneous, because the end of the code word for b is not recognizable without examining the next symbol.
- Consider the code M3 = {a -> 0, b -> 1, c -> 00}. This code is non-singular and uniquely decodable, but not instantaneous, because the end of the code word for a is not recognizable without examining the next symbol. This code is also not prefix-free, because the code word for a is a prefix of the code word for c.



# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images and MP3 for music.
- Prefix codes can be derived from various algorithms, such as Huffman coding, arithmetic coding, Elias coding, etc .
- Prefix codes can be represented by binary trees, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- Prefix codes can be evaluated by their average codeword length, which is the weighted sum of the lengths of all codewords, where the weights are the probabilities of the symbols.
- Prefix codes can be optimized by minimizing the average codeword length, which is equivalent to minimizing the entropy of the source.
- Prefix codes can be classified into two types: fixed-length and variable-length.
  - Fixed-length prefix codes assign codewords of the same length to all symbols, regardless of their probabilities.
  - Variable-length prefix codes assign codewords of different lengths to symbols, depending on their probabilities, such that more frequent symbols have shorter codewords and less frequent symbols have longer codewords.
  - Variable-length prefix codes are more efficient than fixed-length prefix codes in terms of compression ratio, but they require more complex encoding and decoding algorithms.
- Prefix codes can also be classified into two types: static and dynamic.
  - Static prefix codes use a fixed codebook that is known to both the encoder and the decoder, and does not change during the transmission.
  - Dynamic prefix codes use an adaptive codebook that is updated during the transmission, based on the statistics of the source.
  - Dynamic prefix codes are more adaptive than static prefix codes in terms of changing source characteristics, but they require more overhead for transmitting the codebook.



## Unit 2 - The Huffman coding algorithm

- The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols.
- The algorithm starts by creating a node for each symbol and assigning it a frequency equal to the number of times the symbol appears in the data. Then, it repeatedly merges the two nodes with the lowest frequencies into a new node, whose frequency is the sum of the frequencies of the merged nodes. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to the symbol, and appending a 0 or a 1 to the code depending on whether the left or the right branch is taken at each node. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible codes for a given set of symbols and frequencies. It also minimizes the average code length, which is the weighted sum of the code lengths of all symbols, where the weights are the frequencies of the symbols.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video. It can also be combined with other compression techniques, such as run-length encoding or arithmetic coding, to achieve higher compression ratios.



# Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the lowest expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The expected codeword length is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The variance of the codeword length is the weighted average of the squared deviations of the codeword lengths from the expected codeword length, where the weights are the probabilities of the symbols.
- The variance of the codeword length measures the variability or dispersion of the codeword lengths around the expected codeword length.
- A lower variance implies a more uniform distribution of the codeword lengths, which may be desirable for some applications.
- A minimum variance Huffman code is a Huffman code that minimizes the variance of the codeword length, subject to the constraint that the expected codeword length is also minimized.
- A minimum variance Huffman code may not be unique, and it may not exist for some probability distributions.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Start with a set of nodes, each representing a symbol and its probability.
  - Sort the nodes in ascending order of their probabilities.
  - While there are more than two nodes in the set:
    - Select the two nodes with the lowest probabilities and merge them into a new node, whose probability is the sum of the probabilities of the two nodes.
    - Assign a 0 bit to the edge connecting the new node and the node with the lower probability, and a 1 bit to the edge connecting the new node and the node with the higher probability.
    - Insert the new node into the set, maintaining the ascending order of probabilities.
  - Assign a 0 bit to the edge connecting the root node and the node with the lower probability, and a 1 bit to the edge connecting the root node and the node with the higher probability.
  - Traverse the tree from the root to the leaves, and concatenate the bits along the path to form the codeword for each symbol.
- An example of a minimum variance Huffman code is shown below for the following probability distribution:

| Symbol | Probability |
|--------|-------------|
| a      | 0.2         |
| b      | 0.2         |
| c      | 0.25        |
| d      | 0.05        |
| e      | 0.15        |
| f      | 0.15        |

- The Huffman tree and the corresponding codewords are:

```
     1.00
    /    \
  0.45    0.55
 /   \    /  \
0.2  0.25 0.3 0.25
a    c   / \  f
       0.15 0.15
       e    b
```

| Symbol | Codeword |
|--------|----------|
| a      | 00       |
| b      | 111      |
| c      | 01       |
| d      | 1100     |
| e      | 100      |
| f      | 101      |

- The expected codeword length is:

```
0.2 * 2 + 0.2 * 3 + 0.25 * 2 + 0.05 * 4 + 0.15 * 3 + 0.15 * 3 = 2.55 bits/symbol
```

- The variance of the codeword length is:

```
0.2 * (2 - 2.55)^2 + 0.2 * (3 - 2.55)^2 + 0.25 * (2 - 2.55)^2 + 0.05 * (4 - 2.55)^2 + 0.15 * (3 - 2.55)^2 + 0.15 * (3 - 2.55)^2 = 0.3475 bits^2/symbol
```

- The entropy of the source is:

```
-0.2 * log2(0.2) - 0.2 * log2(0.2) - 0.25 * log2(0.25) - 0.05 * log2(0.05) - 0.15 * log2(0.15) - 0

```




# Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, adaptive Huffman coding does not require a separate step to construct the code tree. Instead, it builds and updates the code tree dynamically as the symbols are being transmitted, adapting to the changing conditions in the data.

The main advantages of adaptive Huffman coding are:

- It allows one-pass encoding and decoding, without the need to store or transmit the code tree separately.
- It can handle non-stationary sources, where the symbol frequencies may vary over time.
- It can achieve optimal compression for any source, as long as the encoder and decoder use the same algorithm.

The main challenges of adaptive Huffman coding are:

- It requires more complex algorithms and data structures to maintain and update the code tree efficiently.
- It may incur some overhead in the beginning of the transmission, when the code tree is not well adapted to the source.

There are different algorithms for implementing adaptive Huffman coding, such as Vitter's algorithm, which uses a special data structure called a splay tree to update the code tree. The basic steps of adaptive Huffman coding are:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been encountered yet. Assign a weight of zero to this node.
- For each symbol to be encoded or decoded, do the following:
  - If the symbol has not been encountered before, output the code for the NYT node, followed by the fixed-length code for the symbol (usually the ASCII code). Then, add a new node for the symbol as a child of the NYT node, and assign a weight of one to it. Also, create a new NYT node as the other child of the old NYT node, and assign a weight of zero to it.
  - If the symbol has been encountered before, output the code for the node corresponding to the symbol. Then, increment the weight of the node by one.
  - After encoding or decoding a symbol, update the code tree to maintain the following properties:
    - The nodes are ordered by increasing weight, from left to right and from bottom to top. This means that the nodes with the same weight are ordered by the order of their appearance in the data.
    - The sibling property: the nodes with the same parent have different codes, and the left child has a code of 0 and the right child has a code of 1.
    - The weight-balanced property: for any node in the tree, the weight of its left subtree is less than or equal to the weight of its right subtree, and the weight of any node is less than or equal to the weight of its parent.
    - To update the code tree, find the node with the highest number (the most recent node) that has the same weight as the node that was encoded or decoded. If this node is not the same as the node that was encoded or decoded, swap them. Then, increment the weight of the node and all its ancestors, and repeat the process until reaching the root of the tree.

The following diagram shows an example of adaptive Huffman coding for the string "abracadabra", using Vitter's algorithm:

Adaptive Huffman coding example

The code tree is initialized with a single NYT node with weight 0. The first symbol, "a", is encoded as the code for the NYT node (empty), followed by the ASCII code for "a" (01100001). Then, a new node for "a" is added as the left child of the NYT node, with weight 1, and a new NYT node is created as the right child of the old NYT node, with weight 0. The second symbol, "b", is encoded as the code for the new NYT node (1), followed by the ASCII code for "b" (01100010). Then, a new node for "b" is added as the left child of the new NYT node, with weight 1, and a new NYT node is created as the right child of the new NYT node, with weight 0. The third symbol, "r", is encoded as the code for the new NYT node (11), followed by the ASCII code for "r" (01110010). Then, a new node for "r" is added as the left child of the new NYT node, with



# Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the source data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire source data, and the leaf nodes represent the individual symbols. The frequency of each node is the sum of the frequencies of its children.
- The algorithm starts with a list of nodes sorted by their frequencies in ascending order. Then, it repeatedly performs the following steps until there is only one node left in the list:
  - Remove the two nodes with the lowest frequencies from the list and create a new node with the sum of their frequencies as its frequency.
  - Assign the new node as the parent of the two removed nodes, and label the edge from the parent to the left child as 0 and the edge from the parent to the right child as 1.
  - Insert the new node back into the list in the correct position according to its frequency.
- The resulting binary tree is called the Huffman tree, and the code for each symbol is obtained by traversing the tree from the root to the leaf corresponding to that symbol and concatenating the edge labels along the path.
- The Huffman coding algorithm guarantees that the code for each symbol is optimal, meaning that it has the shortest possible length among all possible codes for that symbol. Moreover, the code for each symbol is prefix-free, meaning that no code is a prefix of another code. This ensures that the encoded data can be uniquely decoded by following the Huffman tree from the root to the leaves.

- To update the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression, the following steps are recommended:
  - Review the definition and the steps of the algorithm and make sure they are clear and accurate.
  - Provide examples of source data and their corresponding Huffman trees and codes to illustrate the algorithm and its properties.
  - Explain the advantages and disadvantages of the Huffman coding algorithm compared to other data compression techniques, such as run-length encoding, arithmetic coding, and Lempel-Ziv coding.
  - Include exercises and problems that test the students' understanding and application of the algorithm, such as finding the Huffman code for a given source data, finding the source data for a given Huffman code, and comparing the compression ratio and the encoding/decoding time of different algorithms.
  - Provide references and links to additional resources and materials that cover the Huffman coding algorithm in more depth and detail, such as books, articles, videos, and online courses.



# Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- Huffman coding is an efficient method of compressing data without losing information.

The encoding procedure for the Huffman coding algorithm consists of the following steps:

1. Create a leaf node for each character and add it to the priority queue.
2. While there is more than one node in the queue:
    - Remove the two nodes of the highest priority (the lowest frequency) from the queue.
    - Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.
    - Add the new node to the queue.
3. The remaining node is the root node and the tree is complete.
4. Traverse the tree from the root to the leaves and assign a bit (0 or 1) to each edge, such that no two edges along any path have the same bit.
5. For each character, concatenate the bits along the path from the root to the leaf node, forming the code for that character.

Here is an example of Huffman coding for the string "BCCABBDDAECCBBAEDDCC":

Huffman coding example

The codes for each character are:

- A: 000
- B: 001
- C: 01
- D: 10
- E: 110

The encoded string is:

- 00101100100100101000011001100100100011010100101101

The encoded string has 38 bits, while the original string has 80 bits, resulting in a compression ratio of 47.5%.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

# Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the source data.
- The Huffman codes are prefix-free, meaning that no code is a prefix of another code. This property ensures that the codes can be uniquely decoded without ambiguity.
- The decoding procedure for the Huffman codes is as follows:

  - Step 1: Construct the Huffman tree from the code table. The code table is a list of symbols and their corresponding codes. The Huffman tree is a binary tree where each leaf node represents a symbol and its code, and each internal node represents a prefix of some codes. The root node has an empty prefix, and the left and right branches of each node add a 0 or 1 to the prefix, respectively.
  - Step 2: Read the encoded data bit by bit from left to right. Start from the root node of the Huffman tree and follow the branches according to the bits. If the bit is 0, go to the left branch; if the bit is 1, go to the right branch.
  - Step 3: When a leaf node is reached, output the symbol corresponding to that node and return to the root node. Repeat step 2 until all the bits are processed.

- Example: Suppose the code table is as follows:

  | Symbol | Code |
  |--------|------|
  | A      | 0    |
  | B      | 10   |
  | C      | 110  |
  | D      | 111  |

  The Huffman tree for this code table is:

  ```
       *
      / \
     0   *
        / \
       1   *
          / \
         1   1
        / \ / \
       A  B C  D
  ```

  If the encoded data is 01101110, the decoding procedure is:

  - Start from the root node (*).
  - Read the first bit (0) and go to the left branch. The node is A, output A and return to the root node.
  - Read the second bit (1) and go to the right branch. The node is *, continue to the next bit.
  - Read the third bit (0) and go to the left branch. The node is B, output B and return to the root node.
  - Read the fourth bit (1) and go to the right branch. The node is *, continue to the next bit.
  - Read the fifth bit (1) and go to the right branch. The node is *, continue to the next bit.
  - Read the sixth bit (1) and go to the right branch. The node is D, output D and return to the root node.
  - Read the seventh bit (1) and go to the right branch. The node is *, continue to the next bit.
  - Read the eighth bit (0) and go to the left branch. The node is C, output C and return to the root node.
  - All the bits are processed, the decoding is done.

  The decoded data is ABDC.



# Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r .
- The binary code for r can be either fixed-length or variable-length, depending on the value of M .
- If M is a power of 2, the binary code for r is fixed-length and has log2(M) bits .
- If M is not a power of 2, the binary code for r is variable-length and uses a technique called truncated binary encoding .
- Truncated binary encoding splits the range of possible values of r into two subranges: a lower range of size b, where b is the largest power of 2 that is less than or equal to M, and an upper range of size M-b.
- The values in the lower range are encoded with log2(b) bits, while the values in the upper range are encoded with log2(b)+1 bits, with the extra bit indicating that the value belongs to the upper range.
- Golomb codes are optimal for data that follows a geometric distribution with parameter p, where p = 1/M.
- Golomb codes can also be used for data that follows a Zipfian distribution, where the frequency of the i-th most common symbol is proportional to 1/i.
- Golomb codes have applications in lossless compression of text, images, audio, and video, especially for data with high entropy or long-tailed distributions .



# Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a number x using Rice codes, the following steps are performed :
  - Divide x by m and write the quotient in unary code. Unary code is a code that uses only one symbol, usually 1, to represent a number. For example, 5 in unary code is 11111.
  - Write the remainder of x/m in binary code, using k bits. For example, if k = 3 and the remainder is 6, then the binary code is 110.
  - Concatenate the unary code and the binary code to form the Rice code. For example, if x = 23, k = 3, m = 8, then the quotient is 2, the remainder is 7, the unary code is 11, the binary code is 111, and the Rice code is 11111.
- To decode a Rice code, the following steps are performed :
  - Count the number of 1s in the unary code until a 0 is encountered. This is the quotient of x/m.
  - Read the next k bits as the binary code for the remainder of x/m.
  - Multiply the quotient by m and add the remainder to obtain x.
  - For example, if the Rice code is 11111, k = 3, m = 8, then the quotient is 2, the remainder is 7, and x = 2*8 + 7 = 23.
- Rice codes are suitable for data sets that have a geometric or exponential distribution, where most of the values are small and the probability of larger values decreases rapidly.
- Rice codes are often used in audio and video compression, where the difference between adjacent samples or pixels tends to be small.



# Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression .
- Tunstall codes are based on the idea of parsing a stochastic source with codewords of variable length and encoding them with fixed-length codes.
- Tunstall codes are a precursor to Lempel-Ziv codes, which are widely used in practice.
- Tunstall codes have the following properties :
  - They are prefix codes, meaning that no codeword is a prefix of another codeword.
  - They are optimal for sources with geometrically distributed symbols, such as run-length encoding.
  - They are adaptive, meaning that they can adjust to the changing statistics of the source.
  - They are simple to implement and decode, requiring only a lookup table and a buffer.
- Tunstall codes can be constructed using the following algorithm :
  - Start with a set of source symbols and their probabilities, and a desired codeword length n.
  - Initialize a codebook with one entry for each source symbol, and assign each entry a probability equal to the symbol's probability.
  - Repeat until the codebook has 2^n entries:
    - Find the entry with the highest probability in the codebook, and remove it.
    - For each source symbol, create a new entry by appending the symbol to the removed entry, and assign it a probability equal to the product of the removed entry's probability and the symbol's probability.
    - Add the new entries to the codebook.
  - Assign each entry in the codebook a unique n-bit codeword.
- Tunstall codes can be decoded using the following algorithm :
  - Start with an empty buffer and a codebook that maps n-bit codewords to variable-length source symbols.
  - Read n bits from the input and append them to the buffer.
  - If the buffer matches a codeword in the codebook, output the corresponding source symbol and clear the buffer.
  - Otherwise, repeat from step 2.



# Applications of Huffman Coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or weight. The more frequent a data value is, the shorter its code will be. This way, the data can be represented using fewer bits than the original fixed-length codes.

Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel. This reduces the bandwidth and transmission time required for the data. 
- **Conventional compression formats**: Huffman coding is often used by compression formats like PKZIP, GZIP, BZIP2, etc. to compress the data files. These formats use Huffman coding along with other techniques like run-length encoding, dictionary encoding, etc. to achieve high compression ratios.  
- **Multimedia codecs**: Huffman coding is also used by multimedia codecs like JPEG, PNG, and MP3 to compress the images and audio files. These codecs use Huffman coding to encode the quantized coefficients of the discrete cosine transform (DCT) or the modified discrete cosine transform (MDCT) of the data. This reduces the size of the data without affecting the quality significantly.



# Lossless Image Compression Using Huffman Coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding for image compression are:

  - Step 1: Calculate the probability of each pixel value in the image and sort them in descending order.
  - Step 2: Create a binary tree with the pixel values as leaf nodes and their probabilities as weights. The two nodes with the lowest probabilities are combined to form a parent node with the sum of their probabilities as the weight. This process is repeated until there is only one root node left.
  - Step 3: Assign a binary code to each leaf node by traversing the tree from the root to the leaves. The code is formed by appending a 0 for a left branch and a 1 for a right branch.
  - Step 4: Encode the image by replacing each pixel value with its corresponding binary code. The encoded image is stored along with the Huffman tree for decoding.
  - Step 5: Decode the image by using the Huffman tree to map each binary code back to its pixel value.

- Huffman coding is an optimal and efficient lossless compression technique that achieves the Shannon bound, which is the theoretical limit of compression for a given source.
- Huffman coding can be applied to grayscale or color images, but it is more effective for images with a small number of distinct pixel values or a skewed distribution of pixel values.



# Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters in a more efficient way.
- Text compression can save storage space, bandwidth, and transmission time, and can also improve security and privacy by making the text less readable by humans or machines.
- Text compression can be lossless or lossy. Lossless compression preserves the original information and allows exact reconstruction of the text, while lossy compression discards some information and only allows approximate reconstruction of the text.
- One of the most popular and widely used lossless text compression algorithms is the Huffman coding algorithm, named after its inventor David Huffman.
- The Huffman coding algorithm assigns variable-length binary codes to the characters of a text based on their frequencies of occurrence. The more frequent a character is, the shorter its code will be, and vice versa. This way, the most common characters will take up less space than the less common ones, resulting in a smaller file size.
- The Huffman coding algorithm consists of the following steps:

  1. Create a frequency table that counts the number of occurrences of each character in the text.
  2. Create a priority queue (or a min-heap) that contains the characters as nodes, sorted by their frequencies in ascending order.
  3. While the queue has more than one node, do the following:
     - Dequeue the two nodes with the lowest frequencies and create a new internal node with the sum of their frequencies as its frequency.
     - Assign the left child of the new node to be the first dequeued node and the right child to be the second dequeued node.
     - Enqueue the new node back to the queue.
  4. The remaining node in the queue is the root of the Huffman tree, which represents the optimal prefix-free code for the text.
  5. Traverse the Huffman tree and assign a 0 to every left edge and a 1 to every right edge. The code for each character is the concatenation of the edge labels along the path from the root to the leaf node corresponding to that character.
  6. Encode the text by replacing each character with its code and output the compressed file.
  7. To decode the compressed file, use the Huffman tree to convert each code back to its original character and output the decompressed file.



# Audio Compression

Audio compression is the process of reducing the amount of data required to represent an audio signal. Audio compression can be either lossy or lossless, depending on whether the original signal can be perfectly reconstructed from the compressed data or not. Lossy compression techniques, such as MP3 and AAC, achieve higher compression ratios by discarding some information that is deemed perceptually irrelevant or less important. Lossless compression techniques, such as FLAC and ALAC, preserve the exact quality of the original signal, but achieve lower compression ratios.

## The Huffman Coding Algorithm

The Huffman coding algorithm is a lossless compression technique that assigns variable-length codes to the symbols of an input data stream, based on their frequencies of occurrence. The codes are constructed in such a way that no code is a prefix of another code, which allows for unambiguous decoding. The codes are also optimal, meaning that they minimize the expected length of the encoded data.

The Huffman coding algorithm works as follows:

- Create a leaf node for each symbol and add it to a priority queue based on its frequency.
- While there is more than one node in the queue:
  - Remove the two nodes with the lowest frequency from the queue.
  - Create a new internal node with these two nodes as children and with frequency equal to the sum of their frequencies.
  - Add the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree.
- Traverse the Huffman tree and assign codes to the nodes by appending a 0 for a left branch and a 1 for a right branch.
- To encode a symbol, find its leaf node in the tree and output its code.
- To decode a bit stream, start from the root of the tree and follow the branches according to the bits until reaching a leaf node, which gives the decoded symbol.

The Huffman coding algorithm can be applied to audio compression by treating each sample or subband coefficient as a symbol and encoding it with a variable-length code. This can reduce the number of bits required to represent the audio signal, especially if some symbols are more frequent than others. However, the Huffman coding algorithm requires the knowledge of the symbol frequencies, which may vary depending on the audio content. Therefore, dynamic or adaptive Huffman coding techniques are often used, which update the codebook based on the incoming data. Alternatively, the codebook can be transmitted along with the encoded data, but this adds some overhead.



## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula that generates each term from its position or index in the sequence.
- A sequence can also be represented by a list of its terms, separated by commas and enclosed in brackets or parentheses.
- For example, the sequence of even numbers can be represented by the formula 2n, where n is the index, or by the list [2, 4, 6, 8, ...].
- To code a sequence, we need to use a loop that iterates over the indices or positions of the terms, and calculates each term using the formula or rule of the sequence.
- We also need to store the terms in a data structure, such as a list or an array, that can hold multiple values of the same type.
- We can use a for loop or a while loop to code a sequence, depending on the situation and preference.
- A for loop is more suitable when we know the exact number of iterations or terms in the sequence, and we want to use a fixed increment or step for the index.
- A while loop is more suitable when we do not know the exact number of iterations or terms in the sequence, and we want to use a variable or condition to control the loop.
- For example, to code the sequence of even numbers up to 100 using a for loop, we can write:

```python
# create an empty list to store the terms
even_numbers = []

# loop from 1 to 50, since 2 * 50 = 100
for n in range(1, 51):
  # calculate the term using the formula 2n
  term = 2 * n
  # append the term to the list
  even_numbers.append(term)

# print the list of terms
print(even_numbers)
```

- To code the same sequence using a while loop, we can write:

```python
# create an empty list to store the terms
even_numbers = []

# initialize the index to 1
n = 1

# loop until the term exceeds 100
while True:
  # calculate the term using the formula 2n
  term = 2 * n
  # check if the term is greater than 100
  if term > 100:
    # break the loop
    break
  # append the term to the list
  even_numbers.append(term)
  # increment the index by 1
  n = n + 1

# print the list of terms
print(even_numbers)
```



Hello, I am Sydney, your AI assistant. I can help you with your topic of generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression. Here is some content that you can use for your study material:

# Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- A binary code is a way of representing information using only two symbols, usually 0 and 1. Binary codes are used in many applications, such as digital communication, encryption, and data compression.
- Data compression is the process of reducing the size of data by removing redundancy or using efficient encoding methods. Data compression can save storage space, bandwidth, and transmission time.
- Coding a sequence is one of the techniques of data compression, where a sequence of symbols (such as letters, numbers, or musical notes) is mapped to a shorter sequence of binary digits (bits).
- There are two types of coding a sequence: fixed-length coding and variable-length coding. Fixed-length coding assigns the same number of bits to each symbol, while variable-length coding assigns different numbers of bits to different symbols, depending on their frequency or importance.
- To generate a binary code for the notes of the Unit 3, we can use either fixed-length coding or variable-length coding, depending on the requirements and constraints of the application. Here are some examples of both types of coding:

## Fixed-length coding

- In fixed-length coding, each note is represented by a fixed number of bits, regardless of how often it appears in the sequence. For example, if we use 4 bits per note, we can represent 16 different notes, from 0000 to 1111. Here is a possible mapping of the notes to the binary code:

| Note | Binary code |
|------|-------------|
| A    | 0000        |
| B    | 0001        |
| C    | 0010        |
| D    | 0011        |
| E    | 0100        |
| F    | 0101        |
| G    | 0110        |
| A#   | 0111        |
| B#   | 1000        |
| C#   | 1001        |
| D#   | 1010        |
| E#   | 1011        |
| F#   | 1100        |
| G#   | 1101        |
| R    | 1110        |
| S    | 1111        |

- R and S are special symbols that represent a rest and a silence, respectively.
- Using this fixed-length coding, we can encode any sequence of notes using 4 bits per note. For example, the sequence A, C, E, G, R, S, A, C, E, G would be encoded as 0000 0010 0100 0110 1110 1111 0000 0010 0100 0110.
- The advantage of fixed-length coding is that it is simple and easy to encode and decode. The disadvantage is that it may not be very efficient, especially if some notes are more frequent or important than others. For example, if the sequence consists mostly of A, C, E, and G, we are wasting a lot of bits on the other notes that rarely appear.

## Variable-length coding

- In variable-length coding, each note is represented by a variable number of bits, depending on how often it appears in the sequence. For example, if we use a Huffman code, which is a type of optimal variable-length code, we can assign shorter codes to more frequent notes and longer codes to less frequent notes. Here is a possible Huffman code for the notes of the Unit 3, based on their relative frequencies:

| Note | Frequency | Binary code |
|------|-----------|-------------|
| A    | 0.25      | 0           |
| C    | 0.25      | 10          |
| E    | 0.25      | 110         |
| G    | 0.1       | 1110        |
| R    | 0.05      | 11110       |
| S    | 0.05      | 11111       |
| B    | 0.01      | 1111100     |
| D    | 0.01      | 1111101     |
| F    | 0.01      | 1111110     |
| A#   | 0.005     | 111111100   |
| B#   | 0.005     | 111111101   |
| C#



# Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using only two symbols, usually 0 and 1. Each symbol is called a bit, and a sequence of bits is called a binary code. Binary coding is used to store and transmit data in computers and other digital devices.
- Huffman coding is a form of lossless compression which makes files smaller using the frequency with which characters appear in a message. Huffman coding assigns variable length binary codes for each input character in the text file. The length of the binary code depends on the frequency of the character in the file. The most frequent characters are coded with the smaller binary words, thus, the size used to code them is minimal, which increases the compression.
- The main difference between binary and Huffman coding is that binary coding uses fixed length codes for all characters, while Huffman coding uses variable length codes for different characters. Binary coding is simpler and faster, but Huffman coding is more efficient and reduces the file size more.
- The advantages of Huffman coding over binary coding are:
  - Huffman coding achieves optimal compression, meaning that no other lossless compression method can produce a smaller output for the same input.
  - Huffman coding adapts to the data, meaning that it can compress any type of file, regardless of the distribution of characters in the file.
  - Huffman coding is easy to implement and decode, using a binary tree data structure that represents the codes for each character.
- The disadvantages of Huffman coding over binary coding are:
  - Huffman coding requires extra space to store the code table, which maps each character to its corresponding binary code. This code table has to be transmitted or stored along with the compressed file, which adds some overhead.
  - Huffman coding is slower than binary coding, as it involves sorting the characters by frequency and building the binary tree. It also requires more memory and processing power to encode and decode the variable length codes.



# Applications of Coding a Sequence in Data Compression

Coding a sequence is a technique that maps a sequence of symbols or data elements into a shorter sequence of codes, such that the original sequence can be recovered from the coded sequence. Coding a sequence is useful for data compression, which reduces the size of data and saves storage space and transmission bandwidth. Some of the applications of coding a sequence in data compression are:

- **Image compression**: Images can be compressed by using run length encoding (RLE), which replaces consecutive pixels of the same color or intensity with a pair of the color and the length of the run. Another technique is Lempel-Ziv-Welch (LZW) coding, which builds a dictionary of repeated sequences of pixels and assigns them shorter codes.
- **Text compression**: Text can be compressed by using Huffman coding, which assigns variable-length codes to characters based on their frequencies, such that the most frequent characters have the shortest codes. Another technique is arithmetic coding, which assigns codes to entire sequences of characters based on their probabilities, such that the most probable sequences have the shortest codes.
- **Audio compression**: Audio can be compressed by using transform coding, which converts the audio signal into a frequency domain representation and discards the less perceptible frequencies. Another technique is predictive coding, which exploits the temporal correlation of the audio signal and encodes the difference between the actual and the predicted samples.
- **Video compression**: Video can be compressed by using a combination of spatial and temporal techniques, such as RLE, LZW, Huffman coding, arithmetic coding, transform coding, and predictive coding. Additionally, video compression can use motion estimation and compensation, which reduces the redundancy between successive frames by encoding the motion vectors and the residual errors.
- **Genomic compression**: Genomic data can be compressed by using reference-based methods, which encode the variations of the genomic sequences relative to a reference sequence, such as single nucleotide polymorphisms (SNPs), insertions, deletions, and inversions. Another technique is Burrows-Wheeler transform (BWT) coding, which transforms the genomic sequences into a sorted permutation that is more compressible by other methods.



# Bi-level image compression-The JBIG standard

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



# JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than existing standards, such as Fax Group 4, MMR, and JBIG1, by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve identifying and encoding recurring patterns in the image, such as characters, symbols, or halftone dots, and replacing them with references to a dictionary of patterns .
- JBIG2 can segment an image into overlapping and/or non-overlapping regions of text, halftone, and generic content, and apply different compression techniques for each type of content .
- Text regions are compressed by using arithmetic coding, dictionary coding, and refinement coding.
- Halftone regions are compressed by using arithmetic coding, adaptive template matching, and refinement coding.
- Generic regions are compressed by using arithmetic coding, adaptive template matching, and context-based modeling.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used for compressing scanned documents, such as PDF files, and has applications in fax, printing, and archiving .



# Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

## Lossless compression

Lossless compression is a technique that preserves the exact quality and details of the original image. Lossless compression works by removing the redundant or unnecessary information from the image file, such as repeated pixels or patterns. Lossless compression can be achieved by using various methods, such as:

- Deflate: This method uses a combination of the LZ77 compression algorithm and Huffman coding to compress the image data. LZ77 identifies and replaces repeated sequences of pixels with shorter codes, while Huffman coding assigns variable-length codes to the most frequent pixels. Deflate is commonly used for PNG and GIF images.
- Run-length encoding: This method encodes sequences of repeated pixels with a single value and a count. For example, a sequence of 10 white pixels can be encoded as (10, 255), where 10 is the count and 255 is the pixel value. Run-length encoding is simple and fast, but it is only effective for images with large areas of uniform color.
- Arithmetic coding: This method assigns variable-length codes to the pixels based on their probabilities of occurrence. The codes are generated by dividing a unit interval into subintervals proportional to the pixel probabilities, and then selecting the subinterval that contains the pixel value. Arithmetic coding can achieve higher compression ratios than Huffman coding, but it is more complex and slower.
- Transform coding: This method transforms the image data into a different representation that is more compact and easier to compress. The most common transform used for image compression is the discrete cosine transform (DCT), which converts the image into a sum of cosine functions of different frequencies. The DCT coefficients are then quantized and encoded. Transform coding is used for JPEG images .

## Lossy compression

Lossy compression is a technique that reduces the size of an image file by discarding some of the information that is not essential for human perception. Lossy compression works by exploiting the limitations of the human visual system, such as the lower sensitivity to high-frequency details or color variations. Lossy compression can achieve much higher compression ratios than lossless compression, but it also introduces some distortion or artifacts in the image. Lossy compression can be achieved by using various methods, such as:

- JPEG: This is the most widely used lossy image compression format. JPEG uses the DCT to transform the image into frequency components, and then applies a quantization matrix to reduce the number of bits needed to represent each coefficient. The quantization matrix is based on the human visual sensitivity, and it assigns more bits to the low-frequency coefficients and less bits to the high-frequency coefficients. The quantized coefficients are then encoded using Huffman coding or arithmetic coding. JPEG allows the user to adjust the compression level and the image quality .
- JPEG 2000: This is an improved version of JPEG that uses the discrete wavelet transform (DWT) instead of the DCT. The DWT decomposes the image into different scales and orientations, and then applies a quantization and coding scheme that adapts to the local image characteristics. JPEG 2000 offers better compression performance, higher image quality, and more features than JPEG, such as progressive decoding, region of interest coding, and lossless compression mode.
- WebP: This is a newer lossy image compression format developed by Google. WebP uses a modified version of the VP8 video codec to compress the image data. WebP supports both lossy and lossless compression modes, as well as alpha channel transparency and animation. WebP claims to provide better compression efficiency and image quality than JPEG and PNG.



# Dictionary Techniques for Data Compression

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive, depending on whether it is fixed or updated during the compression process.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries where the original strings are stored.
- Dictionary techniques can achieve high compression ratios for texts that have a lot of redundancy or repetition.
- Some examples of dictionary techniques are:

  - Non-adaptive dictionary compression: This technique uses a predefined dictionary that is known to both the encoder and the decoder. The dictionary can be based on the frequency or the length of the strings, or on some other criteria. A simple example of this technique is text compression using 4-bit coding, where each character is represented by a 4-bit code that corresponds to its position in the dictionary.
  - Adaptive dictionary compression: This technique builds and updates the dictionary dynamically during the compression process. The dictionary starts with a set of basic symbols (such as individual characters) and grows as new strings are encountered. The encoder and the decoder synchronize their dictionaries by sending the new entries along with the compressed data. A common example of this technique is the family of LZ algorithms, which use a sliding window to find matches between the current string and the previous text. Some variants of LZ algorithms are LZ77, LZ78, LZW, LZSS, LZJB, LZ4, etc.



# Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, redundancy, and distortion.
- Encoding is the process of transforming data into a different format that uses less space or bandwidth.
- Decoding is the process of recovering the original data from the encoded format.
- Entropy is a measure of the uncertainty or randomness of data. It indicates the minimum number of bits needed to represent the data without loss of information.
- Redundancy is the amount of extra or unnecessary information in the data that can be removed or replaced without affecting the meaning or quality of the data.
- Distortion is the difference between the original data and the compressed data. It indicates the loss of information or quality due to compression.
- Coding a sequence is a technique of data compression that assigns codes to symbols or sequences of symbols in the data, such that the codes are shorter than the symbols or sequences they represent.
- Coding a sequence can be classified into two types: fixed-length coding and variable-length coding.
- Fixed-length coding assigns codes of equal length to all symbols or sequences in the data, regardless of their frequency or probability of occurrence.
- Variable-length coding assigns codes of different lengths to symbols or sequences in the data, depending on their frequency or probability of occurrence. The more frequent or probable symbols or sequences are assigned shorter codes, and the less frequent or probable ones are assigned longer codes.
- Variable-length coding can achieve higher compression ratios than fixed-length coding, but it requires more complex encoding and decoding algorithms.



# Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression is fast and simple, but it may not be optimal for data that has a variable or unknown distribution.
- Static dictionary compression can be implemented by using a priming text, a hashing function, or a trie data structure .
- A priming text is a known text that is used to initialize the compression algorithm, but is not transmitted with the compressed data. The compression algorithm can use the priming text as a reference to encode the input data.
- A hashing function is a function that maps a phrase or a symbol to a code, such that different phrases or symbols have different codes. The compression algorithm can use the hashing function to look up the codes for the input data in the static dictionary.
- A trie is a tree-like data structure that stores the phrases or symbols in the static dictionary as paths from the root node to the leaf nodes. The compression algorithm can use the trie to traverse the input data and find the longest matching phrases or symbols in the static dictionary.



# Diagram Coding

Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes. It is an example of an ad hoc compression algorithm, which means it does not rely on any prior knowledge of the source or the statistical properties of the data.

## Steps of diagram coding

1. Scan the source data and identify all the symbols and digrams that are used. Assign a code to each symbol, usually of fixed length, such as 8 bits for ASCII characters. Also, find the unused codes that can be used for digrams, such as control characters or extended ASCII codes.
2. Create a dictionary that maps each digram to an unused code. The dictionary can be sorted by the frequency of the digrams, so that the most common ones get the shortest codes. Alternatively, the dictionary can be built dynamically during the compression process, by adding new digrams as they are encountered.
3. Scan the source data again and output the codes for each symbol or digram. If the current symbol and the next one form a digram that is in the dictionary, output the code for that digram and skip the next symbol. Otherwise, output the code for the current symbol and move to the next one.
4. Optionally, repeat steps 2 and 3 until the dictionary is full or no further compression is possible. This is called iterative diagram coding, and it can improve the compression ratio by capturing longer patterns of symbols.

## Example of diagram coding

Suppose we want to compress the following text:

`Hello, world!`

Assume we use 8-bit ASCII codes for the symbols, and we have 32 unused codes from 128 to 159. The dictionary for the first iteration of diagram coding would look like this:

| Digram | Code  |
| ------ | ----- |
| He     | 128   |
| ll     | 129   |
| lo     | 130   |
| wo     | 131   |
| ld     | 132   |
| or     | 133   |
| !      | 134   |

The compressed output for the first iteration would be:

`128 130 44 32 131 133 132 134`

The compression ratio for the first iteration would be:

`(8 * 13) / (8 * 8) = 1.625`

If we repeat the process for the second iteration, the dictionary would look like this:

| Digram | Code  |
| ------ | ----- |
| 130 44 | 135   |
| 131 133| 136   |
| 132 134| 137   |

The compressed output for the second iteration would be:

`128 135 32 136 137`

The compression ratio for the second iteration would be:

`(8 * 13) / (8 * 5) = 2.6`

We can see that the compression ratio has improved by using iterative diagram coding. However, the dictionary is now full and no further compression is possible. Also, note that the dictionary has to be transmitted along with the compressed data, which adds to the overhead.



# Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated based on the input data  .
- Adaptive dictionary can achieve higher compression ratios than static dictionary, especially for non-text data, such as audio or video .
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel, and Welch .
- LZ77 and LZ78 use a sliding window of previous data to find matches with the current data and encode them as pointers to the dictionary .
- LZW uses a fixed-size dictionary that is initialized with all possible symbols and then grows by adding new sequences of symbols that are encountered in the input data .
- Adaptive dictionary compression has some advantages, such as:
  - It does not require prior knowledge of the data characteristics or statistics .
  - It can adapt to changes in the data distribution over time .
  - It can compress data with variable-length symbols, such as natural language or DNA sequences .
- Adaptive dictionary compression has some disadvantages, such as:
  - It requires more memory and processing power than static dictionary compression .
  - It may suffer from dictionary overflow or degradation, which can reduce the compression performance or require periodic resetting of the dictionary .
  - It may introduce errors or ambiguities in the decompression process if the dictionary is not synchronized between the encoder and the decoder .



# The LZ77 Approach

- LZ77 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1977  .
- It is a dictionary coder and maintains a sliding window during compression  .
- The sliding window contains a fixed-size buffer of recently processed data, divided into two parts: the search buffer and the look-ahead buffer .
- The search buffer contains the data that has already been encoded, and the look-ahead buffer contains the data that is yet to be encoded .
- The algorithm scans the look-ahead buffer for the longest match with any string in the search buffer .
- If a match is found, the algorithm outputs a triple of the form (offset, length, next symbol), where offset is the distance from the current position to the start of the matching string, length is the number of matching symbols, and next symbol is the symbol following the match in the look-ahead buffer .
- If no match is found, the algorithm outputs a special symbol indicating a literal, followed by the first symbol in the look-ahead buffer .
- The algorithm then slides the window by one or more symbols, depending on the length of the match or the literal, and repeats the process until the end of the input data .
- The output of the algorithm is a sequence of triples and literals that can be decoded by reversing the process .
- The algorithm achieves compression by replacing repeated occurrences of data with references to previous occurrences .
- The compression ratio depends on the size of the sliding window, the characteristics of the input data, and the encoding scheme for the output .
- The algorithm is simple, fast, and widely used in various applications, such as ZIP, gzip, PNG, and others.



# The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978 .
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- LZ78 takes advantage of a dictionary-based data structure to compress the data. The dictionary is initialized with all possible single characters as entries .
- The algorithm works as follows :
  - Read the next character from the input.
  - If the current token (the longest sequence of characters that has been seen so far) followed by the next character is already in the dictionary, append the next character to the current token and repeat this step.
  - Otherwise, output a pair of numbers: the index of the current token in the dictionary and the next character. Then, add the current token followed by the next character to the dictionary as a new entry. Reset the current token to empty and go back to the first step.
  - If the end of the input is reached, output the index of the current token in the dictionary and a special end-of-file symbol.
- LZ78 is the basis for many variations and extensions, such as LZW, LZSS, LZMA and others .
- LZ78 has some advantages and disadvantages compared to other compression algorithms :
  - Advantages:
    - It does not require a sliding window or a look-ahead buffer, which reduces the memory usage and complexity.
    - It adapts well to changes in the input data, as the dictionary is dynamically updated.
    - It can achieve high compression ratios for repetitive and structured data, as the dictionary entries can grow arbitrarily long.
  - Disadvantages:
    - It requires a large dictionary size to store all possible token sequences, which may exceed the available memory or the output size limit.
    - It may produce long and redundant output codes for rare or random data, as the dictionary entries may not match the input well.
    - It may suffer from dictionary pollution, where the dictionary is filled with useless or outdated entries that reduce the compression efficiency.



# Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a given sequence, such that the code can be used to reconstruct the original sequence without any loss of information.
- Coding a sequence can be used for various applications, such as:
  - **Data compression**: Reducing the size of data by using shorter codes for more frequent symbols and longer codes for less frequent symbols, thus saving storage space and transmission bandwidth. Examples of data compression algorithms that use coding a sequence are Huffman coding, arithmetic coding, and Lempel-Ziv coding.
  - **Error detection and correction**: Adding extra bits to the code of each symbol, such that the code can be checked for errors and corrected if possible. Examples of error detection and correction codes are Hamming code, cyclic redundancy check (CRC), and Reed-Solomon code.
  - **Encryption**: Transforming the code of each symbol into a different code, such that the original sequence can only be recovered by using a secret key. Examples of encryption algorithms that use coding a sequence are stream ciphers, block ciphers, and public-key cryptography.
  - **Information theory**: Measuring the amount of information in a sequence by using the code length as a proxy. Examples of information theory concepts that use coding a sequence are entropy, mutual information, and channel capacity.



# File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save storage space, bandwidth, and transmission time.
- File compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not.
- UNIX compress is a lossless file compression utility that uses the Lempel-Ziv-Welch (LZW) algorithm.
- The LZW algorithm is based on the idea of building a dictionary of common patterns in the data and replacing them with shorter codes.
- The LZW algorithm works as follows:

  - Initialize the dictionary with 256 entries, corresponding to the 8-bit ASCII characters.
  - Read the next symbol from the input and append it to a string variable S.
  - If S is in the dictionary, go back to step 2.
  - Otherwise, output the code of S without the last symbol, add S to the dictionary with a new code, and set S to the last symbol.
  - Repeat steps 2-4 until the end of the input is reached, then output the code of S.

- The LZW algorithm can achieve high compression ratios for files that contain repetitive patterns or long runs of the same symbol.
- The LZW algorithm can also adapt to different types of data by dynamically updating the dictionary.
- The LZW algorithm has some limitations, such as:

  - The dictionary size is fixed and can be exhausted, leading to reduced compression efficiency or code expansion.
  - The dictionary is not transmitted with the compressed file, so the decompressor must reconstruct it exactly as the compressor did, which can cause errors if the implementations are not compatible.
  - The LZW algorithm is not optimal for compressing files that have high entropy or low redundancy, such as encrypted or random data.



# Image Compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

## Lossless Compression

Lossless compression is a technique that preserves the original data exactly, meaning that the decompressed image is identical to the original image. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, or icons. Lossless compression techniques include:

- **Deflate**: This is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 identifies repeated sequences of pixels and replaces them with shorter codes, while Huffman coding assigns variable-length codes to the pixel values based on their frequency. Deflate is used in formats such as PNG, GIF, and ZIP.
- **Run-length encoding**: This is a simple lossless image compression technique that reduces the size of an image by encoding sequences of repeated pixels. For example, a row of 10 white pixels can be represented as 10W instead of WWWWWWWWWW. Run-length encoding is effective for images with large areas of uniform color, such as cartoons or logos.
- **Arithmetic coding**: This is a lossless image compression technique that assigns codes to the pixel values based on their probability of occurrence. Arithmetic coding can achieve higher compression ratios than Huffman coding, but it is more complex and slower. Arithmetic coding is used in formats such as JPEG-LS and JPEG 2000.
- **Transform coding**: This is a lossless or lossy image compression technique that uses mathematical transformations to reduce the size of an image. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. Transform coding can be divided into two types: linear and nonlinear.

## Lossy Compression

Lossy compression is a technique that discards some of the original data, meaning that the decompressed image is an approximation of the original image. Lossy compression is suitable for images that can tolerate some degradation, such as photographs, videos, or web graphics. Lossy compression techniques include:

- **Discrete cosine transform (DCT)**: This is the most widely used form of lossy compression. It is a type of linear transform coding that converts the image data into a sum of cosine functions of different frequencies. DCT can exploit the fact that the human eye is more sensitive to low-frequency components than high-frequency components, and thus discard or quantize the high-frequency components with minimal perceptual loss. DCT is used in formats such as JPEG, MPEG, and MP3 .
- **Wavelet transform**: This is a type of nonlinear transform coding that converts the image data into a sum of wavelet functions of different scales and positions. Wavelet transform can capture both the spatial and frequency information of the image, and thus adapt to the local features of the image. Wavelet transform can achieve higher compression ratios and better quality than DCT, especially for images with edges, textures, or fine details. Wavelet transform is used in formats such as JPEG 2000, DjVu, and WebP.
- **Fractal compression**: This is a type of nonlinear transform coding that converts the image data into a set of fractal equations that describe the self-similarity of the image. Fractal compression can exploit the fact that natural images often contain repeated patterns at different scales and orientations, and thus generate the image from a small set of parameters. Fractal compression can achieve very high compression ratios and resolution independence, but it is very complex and slow. Fractal compression is used in formats such as FIF and IFS.



# The Graphics Interchange Format (GIF)

- GIF is a **graphical image format** that supports up to **256 colors** and allows to send images between different computers .
- GIF images are compressed using the **Lempel–Ziv–Welch (LZW) lossless data compression technique** to reduce the file size without degrading the visual quality .
- GIF also supports **animation** and **transparency** features, which make it suitable for web graphics .
- GIF was introduced by **CompuServe** in **1987** as a color image format for their file downloading areas .
- GIF was later replaced by **PNG** (Portable Network Graphics) format, which offers better compression, more colors, and alpha channel support.
- GIF is still widely used for simple animations and low-resolution images on the web.



# Compression over Modems

- Compression over modems is a technique that reduces the amount of data that needs to be transmitted over a phone line or a network.
- Compression can improve the speed and efficiency of data transmission by removing redundant or unnecessary information from the data.
- Compression can be performed by the modem itself or by the software on the computer that communicates with the modem.
- Compression can be either lossless or lossy. Lossless compression preserves the original data exactly, while lossy compression discards some information that is deemed less important or less noticeable.
- Compression can be either static or adaptive. Static compression uses a fixed algorithm or dictionary to compress the data, while adaptive compression adjusts the algorithm or dictionary based on the characteristics of the data.
- Compression can be either symmetric or asymmetric. Symmetric compression uses the same algorithm or dictionary for both compression and decompression, while asymmetric compression uses different algorithms or dictionaries for compression and decompression.
- Compression can be either transparent or non-transparent. Transparent compression does not require any special configuration or negotiation between the modems, while non-transparent compression requires the modems to agree on the compression parameters and protocols before transmitting data.

## Examples of compression standards and protocols for modems

- V.42bis: A CCITT standard for data compression that uses adaptive dictionary-based compression. It can achieve up to 4:1 compression ratio and supports error correction. It is compatible with V.42 error correction protocol and V.32bis modulation standard.
- MNP 5: A Microcom Networking Protocol for data compression that uses static run-length encoding and Huffman coding. It can achieve up to 2:1 compression ratio and supports error correction. It is compatible with MNP 2-4 error correction protocols and MNP 10 network protocol.
- STAC: A proprietary compression algorithm developed by Stac Electronics that uses adaptive Lempel-Ziv-Welch (LZW) compression. It can achieve up to 4:1 compression ratio and supports error correction. It is compatible with V.42 error correction protocol and V.32bis modulation standard.
- CSA: A Cisco Systems Algorithm for data compression that uses adaptive Lempel-Ziv-Stac (LZS) compression. It can achieve up to 4:1 compression ratio and supports error correction. It is compatible with V.42 error correction protocol and V.32bis modulation standard. It is available for Cisco 7500, 7200, and 7000 series routers and Cisco 2600 series access routers .



# V.42 bits

- V.42 bits are the units of data that are transmitted and received by modems that use the V.42bis standard for data compression.
- V.42bis is an international standard adopted by the CCITT in 1990, and is widely used by modem manufacturers and network operators.
- V.42bis is based on the Lempel-Ziv dynamic dictionary approach, which compresses data by replacing repeated sequences of symbols with shorter codes from a dictionary that is updated as new data is processed.
- V.42bis can achieve compression ratios of up to 4:1 for text and 2:1 for binary data, depending on the characteristics of the data and the size of the dictionary.
- V.42bis can also switch to transparent mode, in which data is transmitted uncompressed, when the compression ratio is low or the data is already compressed by another method.
- V.42bis uses a tree structure to store and search the dictionary, which is divided into two parts: a static part that contains the 256 ASCII characters, and a dynamic part that contains up to 2048 variable-length codes that are assigned to new sequences as they are encountered.
- V.42bis also uses a technique called delayed innovation, which allows the encoder to send a code that is not yet in the decoder's dictionary, by sending the code of its parent node and the symbol that follows it.
- V.42bis also uses a limited recycling mechanism, which discards the least recently used codes from the dynamic dictionary when it is full, and replaces them with new codes.
- V.42bis is compatible with the V.42 standard for error correction, which uses the LAPM (Link Access Procedure for Modems) protocol to detect and correct errors in the data transmission.
- V.42bis is suitable for implementation on a contemporary modem with an 8-bit microprocessor, 40 Kbytes of RAM, 32 Kbytes of ROM, a 9.6 KBaud V.32 modem-modem connection, and a 19.2 KBaud EIA-232-D modem-terminal connection.



# Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits. The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding. The advantage of predictive coding is that it can exploit the statistical dependencies and redundancies in the data, and achieve higher compression ratios than fixed-length codes.

Some examples of predictive coding algorithms are:

- **Linear predictive coding (LPC)**: This is a technique used for speech and audio compression, that models the spectral envelope of the signal using a linear combination of past samples. The coefficients of the linear combination are called the LPC parameters, and they are transmitted along with the prediction error, or the residual signal. LPC can reduce the bit rate of speech signals by a factor of 10 or more, while preserving the quality and intelligibility of the speech. 
- **Dynamic Markov compression (DMC)**: This is a technique that uses a Markov model to predict the next bit in a binary sequence, based on the previous bits. The Markov model is dynamically updated as new bits are observed, and the prediction error is encoded using arithmetic coding. DMC can achieve high compression ratios for text and other types of data, and it adapts well to changes in the data statistics.  
- **WebP compression**: This is a technique used for image compression, that uses a prediction mode to estimate the value of each pixel, based on the neighboring pixels. The prediction mode is chosen from a set of 14 modes, and it is transmitted along with the prediction error, or the residual, using a variable-length code. WebP compression can reduce the file size of images by 25-34% compared to JPEG, while maintaining the quality and fidelity of the images.



# Prediction with Partial Match (PPM) for Data Compression

- Prediction by Partial Match (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-order Markov model of the source data, where the order is the number of previous symbols used to predict the next one .
- PPM assigns probabilities to each possible next symbol based on the frequency of occurrence in the context, and encodes the symbol with the highest probability using fewer bits .
- PPM adapts to the changing statistics of the data by updating the model after each symbol is encoded or decoded .
- PPM handles unseen symbols or contexts by using a technique called escape coding, which switches to a lower-order model or a uniform distribution .
- PPM has several variants, such as PPM-A, PPM-B, PPM-C, PPM-D, PPM-Z, etc., which differ in the way they update the model, handle escapes, and prune the model to reduce memory usage .
- PPM can achieve high compression ratios, especially for natural language texts, but it is also computationally intensive and memory demanding .



# The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Coding a sequence is a technique of data compression that assigns codes to sequences of input bytes, rather than individual bytes .
- Coding a sequence can achieve better compression ratio than coding individual bytes, especially for data that contains repeated patterns .
- One example of coding a sequence is the LZW (Lempel–Ziv–Welch) algorithm, which is widely used in GIF images, Unix compress, and ZIP files .
- The basic steps of the LZW algorithm are :
  - Initialize a code table with 256 entries, corresponding to the 256 possible byte values.
  - Read the first byte from the input and store it as the current sequence.
  - While there are more bytes to read from the input:
    - Read the next byte and append it to the current sequence.
    - If the current sequence is already in the code table, continue reading the next byte.
    - Otherwise, output the code for the current sequence (without the last byte) and add a new entry to the code table for the current sequence with the next available code.
    - Set the current sequence to the last byte read.
  - Output the code for the current sequence and end the compression.
- Another example of coding a sequence is the Huffman coding algorithm, which is a lossless bit compression technique that assigns variable-length codes to input symbols based on their frequencies.
- The basic steps of the Huffman coding algorithm are:
  - Create a frequency table that counts the occurrences of each symbol in the input data.
  - Build a Huffman tree that represents the optimal prefix codes for each symbol, using the following procedure:
    - Create a leaf node for each symbol and add it to a priority queue based on its frequency.
    - While there is more than one node in the queue:
      - Remove the two nodes with the lowest frequency from the queue.
      - Create a new internal node with these two nodes as children and the sum of their frequencies as the new frequency.
      - Add the new node to the queue.
    - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each symbol by appending 0 or 1 depending on the left or right branch taken.
  - Encode the input data by replacing each symbol with its corresponding code from the Huffman tree.
  - Output the encoded data and the Huffman tree (or a header that can reconstruct the tree) and end the compression.



# The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The ESCAPE SYMBOL is a special symbol that is used to indicate that a character in a sequence is not in the codebook.
- The ESCAPE SYMBOL is usually chosen to be a character that is unlikely to appear in the sequence, such as `#` or `*`.
- The ESCAPE SYMBOL is followed by the binary representation of the character that is not in the codebook, using a fixed number of bits.
- The ESCAPE SYMBOL allows the encoder to handle any character that is not in the codebook, without having to update the codebook or send it to the decoder.
- The ESCAPE SYMBOL also allows the encoder to adapt to changes in the source distribution, by adding new characters to the codebook as they appear in the sequence.
- The ESCAPE SYMBOL has a trade-off between the size of the codebook and the length of the encoded sequence. A smaller codebook requires fewer bits to represent each character, but also increases the probability of using the ESCAPE SYMBOL. A larger codebook reduces the use of the ESCAPE SYMBOL, but also increases the number of bits needed for each character.
- The ESCAPE SYMBOL can be combined with other coding techniques, such as Huffman coding or arithmetic coding, to improve the compression ratio.



# Length of context for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The length of context is the number of symbols that are used to predict the next symbol in a sequence.
- The length of context affects the performance of compression algorithms, such as arithmetic coding and Lempel-Ziv coding.
- A longer context can capture more patterns and correlations in the data, leading to higher compression ratios and lower redundancy.
- However, a longer context also requires more memory and computation to store and process the probabilities of each possible symbol given the context.
- Therefore, there is a trade-off between the length of context and the complexity and efficiency of the compression algorithm.
- The optimal length of context depends on the characteristics of the data and the compression method.
- For example, natural language texts often have a short context length, as the probabilities of words depend mostly on the previous few words.
- On the other hand, images and audio signals may have a longer context length, as the pixels or samples are more correlated with their neighbors.



# The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by using various techniques that exploit the redundancy or regularity in the data.
- One of the techniques for data compression is arithmetic coding, which assigns variable-length codes to symbols based on their probabilities of occurrence in a given context.
- The exclusion principle is a method to improve the performance of arithmetic coding by excluding some symbols from the probability computation when they are not likely to occur in the current context.
- The exclusion principle works as follows :
  - When encoding a symbol, the arithmetic coder divides the unit interval into subintervals, each of which represents a possible symbol.
  - The size of each subinterval is proportional to the probability of the corresponding symbol in the current context.
  - The encoder then selects the subinterval that matches the symbol to be encoded and narrows the unit interval to that subinterval.
  - The encoder repeats this process until the entire input sequence is encoded.
  - When decoding a symbol, the arithmetic decoder performs the inverse process by finding the subinterval that contains the encoded value and outputting the corresponding symbol.
  - The exclusion principle allows the encoder and decoder to exclude some symbols from the subinterval division when they are not likely to occur in the current context.
  - This reduces the number of subintervals and increases their sizes, which leads to shorter codes and higher compression ratios.
  - The exclusion principle can be implemented by using escape codes, which indicate that the symbol to be encoded is not in the current context and that a lower-order context should be used instead.
  - Alternatively, the exclusion principle can be implemented by using lazy exclusions, which avoid using escape codes and instead adjust the probabilities of the remaining symbols to account for the excluded ones.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is a summary of the Burrows-Wheeler Transform for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression.

# The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is a reversible algorithm that transforms a sequence of symbols into another sequence of symbols that is more suitable for compression.
- The BWT works by sorting all the cyclic rotations of the input sequence in lexicographic order and taking the last symbol of each rotation as the output sequence. The output sequence is usually followed by an index that indicates the position of the original sequence in the sorted list of rotations.
- The BWT has the property of creating long runs of identical symbols in the output sequence, especially if the input sequence has low entropy or high redundancy. This makes the output sequence easier to compress with run-length encoding or other entropy coding methods.
- The BWT can be reversed by using the index and the output sequence to reconstruct the sorted list of rotations and then finding the original sequence among them. This can be done efficiently by using a data structure called the suffix array, which stores the starting positions of the sorted rotations in the input sequence.
- The BWT is widely used in data compression, especially for text and DNA sequences. It is also the basis of the bzip2 compression algorithm, which combines the BWT with run-length encoding and Huffman coding. The BWT can achieve high compression ratios and fast decompression speeds.



# Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but prepares it for better compression by entropy encoding techniques  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) and output the index of each symbol in the input sequence, while moving the symbol to the front of the list  .
- This way, symbols that occur frequently in the input sequence will have smaller indices and can be encoded with fewer bits by entropy encoding techniques such as Huffman coding or arithmetic coding  .
- Movetofront coding is an invertible transformation, meaning that the original input sequence can be recovered from the output sequence and the list of symbols  .
- Movetofront coding is used as a sub-step in several data compression algorithms, such as bzip2 and Burrows–Wheeler transform .
- Movetofront coding can improve the compression ratio of data that has long runs of identical symbols or symbols that appear in clusters .



# CALIC for Data Compression

CALIC stands for Context-Based, Adaptive, Lossless Image Coding, and is an image codec that is made for obtaining a high degree of compression for continuous-tone gray-scaled images. It uses a single pass and self-correcting GAP (gradient adjusted predictor) to compress image efficiently and with a high compression ratio.

Some of the main features of CALIC are  :

- It puts heavy emphasis on image data modeling and adapts to varying source statistics.
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics.
- The non-linear predictor adapts via an error feedback mechanism.
- It uses a bias cancellation technique to remove the systematic prediction errors in each context.
- It uses a Golomb-Rice code to encode the residuals with a context-dependent parameter.

The basic steps of the CALIC algorithm are:

1. Find the initial prediction using the GAP method based on the neighboring pixels.
2. Compute the prediction context based on the local image features and the prediction error of the previous pixel.
3. Refine the prediction by removing the estimate of the bias in that context.
4. Update the bias estimate based on the current prediction error.
5. Obtain the residual and remap it so the residual values lie between 0 and M, where M is the size of the initial alphabet.
6. Encode the residual using a Golomb-Rice code with a context-dependent parameter.

The following diagram illustrates the CALIC encoder and decoder:




# JPEG-LS

- JPEG-LS is a **lossless/near-lossless compression standard** for continuous-tone images .
- Its official designation is **ISO-14495-1/ITU-T.87**   .
- It is based on the **LOCO-I** algorithm (LOw COmplexity LOssless COmpression for Images) developed at **Hewlett-Packard Laboratories** .
- It consists of two independent and distinct stages called **modeling** and **encoding** .
- The modeling stage predicts the value of each pixel based on its **local context** (the neighboring pixels) and computes the **prediction error**  .
- The encoding stage maps the prediction error to a **symbol** and encodes it using a **context-based adaptive arithmetic coder**  .
- JPEG-LS can achieve **high compression ratios** and **low complexity** compared to other lossless compression methods   .
- JPEG-LS also supports **near-lossless compression**, which allows a small amount of distortion (controlled by a parameter) in exchange for higher compression ratios .
- JPEG-LS has two parts: the **core** and the **extensions**.
- The core defines the basic algorithm and the syntax for the compressed data stream.
- The extensions define additional features such as **progressive coding**, **hierarchical coding**, **region of interest coding**, and **multi-component coding**.



# Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of resolution or detail to represent or process data, such as images, vectors, or fluids.
- Multi-resolution approaches can improve the performance, efficiency, and accuracy of data compression by exploiting the properties of different scales and frequencies in the data.
- Some examples of multi-resolution approaches for data compression are:

  - **Multiresolution vector data compression**: This method uses a quadtree structure to partition the vector data into blocks of different sizes and shapes, and then applies a linear approximation algorithm to each block. The compression efficiency is further improved by grid filtering and binary offset for linear and point geometries. This method can achieve visual lossless compression for vector spatial data.
  - **Multi-resolution fractal image compression**: This method combines wavelet and fractal transforms to compress images. Wavelet transform decomposes the image into subbands of different frequencies, and fractal transform encodes the self-similarity of the image across scales. This method can reduce the blocking artifacts and image blurring of conventional fractal compression algorithms, and improve the quality of the reconstructed image.
  - **Multi-resolution method for compressible multi-phase flows**: This method uses a wavelet-based adaptive mesh refinement technique to simulate the dynamics of fluids with different phases and densities. The method employs a sharp interface model to track the interface between the phases, and adapts the mesh resolution according to the local features of the flow. This method can reduce the memory and CPU time requirements, and capture the complex phenomena of multi-phase flows.



# Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding reduces the amount of data needed to represent a binary image, such as a scanned document or a fax page, by exploiting the spatial redundancy and the high contrast between black and white pixels.
- Facsimile encoding consists of two steps: run-length encoding and Huffman encoding.

## Run-length encoding

- Run-length encoding is a simple technique that replaces consecutive identical symbols (runs) with a pair of the symbol and the run length.
- For example, the binary sequence 0000001111100000 can be encoded as (0,6)(1,5)(0,4), where each pair is a symbol and a run length.
- Run-length encoding is effective for binary images that have large areas of black or white pixels, such as text or line drawings.
- Run-length encoding can be further improved by using different codes for black and white runs, and by using variable-length codes for the run lengths.

## Huffman encoding

- Huffman encoding is a technique that assigns optimal variable-length codes to symbols based on their probabilities of occurrence.
- Huffman encoding builds a binary tree that represents the code assignments, where the most frequent symbols are assigned the shortest codes and the least frequent symbols are assigned the longest codes.
- Huffman encoding can compress the run-length encoded data by using shorter codes for the more common runs and longer codes for the less common runs.
- Huffman encoding can be adaptive, meaning that the code assignments can be updated based on the statistics of the data.

## Example

- Consider the following binary image of size 8x8 pixels:

```
00000000
00000000
00000000
00000000
00000000
00000000
00000000
00000000
```

- The run-length encoded data is:

```
(0,64)
```

- The Huffman encoded data is:

```
0
```

- The original image requires 64 bits to store, while the facsimile encoded data requires only 1 bit, achieving a compression ratio of 64:1.



# Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which adapts to the changing statistics of the data as it is processed  .
- The Markov model consists of a tree of nodes, each representing a context of previous bits. Each node has two counters, one for the number of zeros and one for the number of ones that have occurred in that context  .
- The probability of the next bit being zero or one is estimated by the ratio of the corresponding counter to the total count in the current node  .
- The algorithm starts with a single node, the root, which has no context. As the input is read, new nodes are created and added to the tree as needed, to represent longer contexts  .
- The algorithm uses a threshold parameter to control the growth of the tree and the complexity of the model. If the total count in a node exceeds the threshold, the node is split into two child nodes, one for each possible next bit  .
- The algorithm also uses a halving parameter to prevent the counters from overflowing. If the total count in a node reaches a certain limit, the counters are halved and rounded up  .
- The algorithm achieves an excellent degree of data compression, comparable to or better than PPM, especially for highly structured or repetitive data.
- The algorithm is also fast and simple to implement, requiring only a small amount of memory.



## Unit 4 - Distortion criteria

- Distortion criteria are the measures of how well a communication system preserves the quality and intelligibility of the transmitted signal.
- Distortion criteria can be classified into two categories: linear and nonlinear.
- Linear distortion criteria are based on the assumption that the communication system is linear, meaning that the output signal is proportional to the input signal and that the system does not introduce any new frequency components.
- Nonlinear distortion criteria are based on the assumption that the communication system is nonlinear, meaning that the output signal is not proportional to the input signal and that the system may introduce new frequency components, such as harmonics and intermodulation products.
- Some examples of linear distortion criteria are:
  - Amplitude distortion: the variation of the amplitude response of the system with frequency.
  - Phase distortion: the variation of the phase response of the system with frequency.
  - Group delay distortion: the variation of the group delay of the system with frequency. Group delay is the time difference between the arrival of two signals with different frequencies at the output of the system.
  - Envelope delay distortion: the variation of the envelope delay of the system with frequency. Envelope delay is the time difference between the arrival of the envelope of two signals with different frequencies at the output of the system.
- Some examples of nonlinear distortion criteria are:
  - Harmonic distortion: the presence of frequency components at integer multiples of the input frequency in the output signal.
  - Intermodulation distortion: the presence of frequency components at the sum and difference of two or more input frequencies in the output signal.
  - Cross modulation distortion: the modulation of one input signal by another input signal in the output signal.
  - Noise: the presence of unwanted random signals in the output signal.



# Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be either lossless or lossy, depending on whether the original data can be perfectly reconstructed or not.
- Lossless compression is suitable for applications that require exact reproduction of the original data, such as text, audio, or executable files.
- Lossy compression is suitable for applications that can tolerate some degradation of the original data, such as images, video, or speech.
- Distortion criteria are the measures that quantify how close the compressed data is to the original data, using some mathematical or perceptual metric.
- Distortion criteria can be either objective or subjective, depending on whether they are based on numerical or human evaluation.
- Objective distortion criteria are the ones that can be computed by a formula or an algorithm, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), or structural similarity index (SSIM).
- Subjective distortion criteria are the ones that depend on the opinion or preference of the user, such as quality score, preference rating, or mean opinion score (MOS).
- The choice of distortion criteria depends on the type and purpose of the data, the compression method, and the user's expectations and requirements.
- The trade-off between compression rate and distortion is the main challenge of data compression, and it is studied by rate-distortion theory.
- Rate-distortion theory is the branch of information theory that deals with the optimal compression rate for a given distortion level, or the minimum distortion for a given compression rate.
- Rate-distortion theory defines the rate-distortion function, which is the lower bound of the achievable compression rate for a given distortion level, and the distortion-rate function, which is the lower bound of the achievable distortion for a given compression rate.
- Rate-distortion theory also provides an iterative algorithm for calculating the rate-distortion function and the distortion-rate function, based on the source statistics and the distortion criteria.
- Rate-distortion theory tells us that no compression system can perform better than the rate-distortion function or the distortion-rate function, and that the closer a practical compression system is to these bounds, the better it performs.



# Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the precision of the signal representation and introduces quantization error or distortion.
- Scalar quantization can be performed on each signal sample independently, without considering the correlation or dependence among the samples .
- Scalar quantization can be represented by a function Q(x) that maps a real number x to a quantization level y, such that Q(x) = y.
- Scalar quantization can be characterized by three parameters: the number of quantization levels N, the quantization step size Δ, and the quantization rule R.
- The quantization step size Δ is the distance between two adjacent quantization levels, and it determines the resolution or granularity of the quantization.
- The quantization rule R is the criterion for assigning a signal sample to a quantization level, and it can be uniform or nonuniform, depending on the distribution of the signal values.
- Uniform quantization uses a constant step size Δ and assigns a signal sample to the nearest quantization level, while nonuniform quantization uses a variable step size Δ and assigns a signal sample to the quantization level that minimizes some distortion measure, such as mean squared error (MSE) or entropy.
- Scalar quantization can be optimized by finding the optimal quantization levels and the optimal quantization rule that minimize the distortion for a given number of quantization levels N.
- Scalar quantization can be applied to various types of signals, such as audio, image, or video, and it can be combined with other compression techniques, such as transform coding or entropy coding, to achieve higher compression ratios .
- Scalar quantization is not optimal for signals that have correlation or dependence among the samples, as it does not exploit the redundancy or structure of the signal .
- A more general and powerful approach to quantization is vector quantization, which quantizes a block or a vector of signal samples together, rather than one sample at a time .



# The Quantization Problem

Quantization is a process of mapping a large set of input values to a smaller set of output values, with a certain amount of distortion or error. Quantization is used in data compression to reduce the number of bits needed to represent a signal, image, or other data. Quantization can be uniform or non-uniform, depending on whether the output values are equally or unequally spaced.

The quantization problem is to find the optimal output values and the corresponding mapping function that minimize the distortion or error for a given input set and a given number of output values. The distortion or error can be measured by different criteria, such as mean squared error, signal-to-noise ratio, or perceptual quality.

Some of the topics related to the quantization problem are:

- The rate-distortion theory, which provides the theoretical limits of compression and quantization for a given source and a given distortion measure.
- The Lloyd algorithm, which is an iterative method to find the optimal output values and the mapping function for a given input set and a given distortion measure.
- The μ-law and A-law, which are two examples of non-uniform quantization that are used in audio compression and telecommunication systems.
- The scalar and vector quantization, which are two types of quantization that operate on single or multiple input values at a time.



# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero.
- A uniform quantizer can be used for data compression by applying a companding technique, which is a nonlinear mapping of the input values to reduce the dynamic range before quantization.
  - Two common companding techniques are $\mu$-law and A-law, which are used for PCM telephone systems.
  - $\mu$-law companding compresses the input values more at higher amplitudes and less at lower amplitudes.
  - A-law companding compresses the input values more uniformly across the range.
- A uniform quantizer can also be used for deep image compression, where the feature maps between the encoder and decoder are quantized to reduce the bit rate .
  - Different approximations of the uniform quantizer can affect the performance and complexity of the deep image compression model .
  - Some examples of uniform quantizer approximations are scalar quantizer (SQ), trellis coded quantizer (TCQ), vector quantizer (VQ), and product quantizer (PQ) .
- A uniform quantizer can be analyzed in terms of its distortion, rate, and efficiency .
  - The distortion of a uniform quantizer is the mean squared error (MSE) between the input and output values .
  - The rate of a uniform quantizer is the number of bits per sample required to represent the output levels .
  - The efficiency of a uniform quantizer is the ratio of the rate to the entropy of the input source .
  - The performance of a uniform quantizer can be improved by increasing the rate or decreasing the distortion .
  - The optimal performance of a uniform quantizer can be achieved at high rates, where the distortion is minimized and the efficiency is maximized .



# Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input signal source.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters, such as synthetic aperture radar (SAR) raw data.
- Adaptive quantization can be classified into two categories: forward adaptive quantization and backward adaptive quantization.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block and transmitted to the receiver as side information. For example, the minimum and maximum values of each block can be used to determine the quantization step size and offset.
- In backward adaptive quantization, the quantizer parameters are updated based on the previous quantized samples and the feedback from the receiver. For example, the Lloyd-Max algorithm can be used to iteratively adjust the quantization levels and boundaries to minimize the distortion.
- Adaptive quantization can improve the performance of differential pulse-code modulation (DPCM), which is a method of encoding the difference between successive samples of a signal. By using adaptive quantization, the quantization noise can be reduced and the signal-to-noise ratio (SNR) can be improved.
- Adaptive quantization can also be applied to image compression, where different regions of an image may have different levels of detail and contrast. By using adaptive quantization, the image quality can be preserved while reducing the bit rate.
- Adaptive quantization can be implemented using various methods, such as block adaptive quantization, adaptive quantization modules, adaptive arithmetic coding, etc  . The choice of the method depends on the application, the data characteristics, and the compression requirements.



# Non uniform Quantization

- Non uniform quantization is a technique of data compression that assigns different step sizes to different input ranges.
- Non uniform quantization can reduce the distortion and improve the signal-to-noise ratio (SNR) for signals that have non-uniform probability distributions or non-linear characteristics.
- Non uniform quantization can be achieved by using companding, adaptive quantization, or non-linear mapping functions.
- Companding is a process of compressing the input signal before applying uniform quantization and expanding the output signal after decoding. Companding can be implemented by using logarithmic or power-law functions, such as the μ-law or A-law algorithms .
- Adaptive quantization is a process of adjusting the step size of the quantizer according to the local characteristics of the input signal, such as the variance or the amplitude. Adaptive quantization can be implemented by using feedback or feedforward mechanisms, such as the Lloyd-Max algorithm or the Jayant algorithm.
- Non-linear mapping functions are functions that map the input signal to a discrete set of output levels that are not equally spaced. Non-linear mapping functions can be designed by using optimization methods, such as the K-means algorithm or the gradient descent algorithm .



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of similar vectors by a single representative vector called a codebook vector.
- Scalar quantization (SQ) is a technique that compresses data by representing each scalar value by a discrete level called a quantization level.
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ by exploiting the correlation among the vectors in the data set.
  - VQ can reduce the quantization noise or distortion by minimizing the mean squared error (MSE) between the original and the reconstructed vectors.
  - VQ can adapt to the statistics of the data set by using variable-length codebook vectors and variable-rate encoding schemes.
  - VQ can handle multidimensional data more efficiently than SQ by avoiding the curse of dimensionality, which is the exponential increase in the number of quantization levels required to maintain a given distortion level as the dimensionality increases.
  - VQ can provide better visual quality than SQ for image and video compression by preserving the edges and textures of the original data.



# The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in a given data set .
- Vector quantization is a technique to compress data by reducing the number of bits required to represent each vector .
- The LBG algorithm is similar to the k-means method in data clustering .
- The LBG algorithm works as follows :
  - Start with an initial codebook of size one, which is the centroid of the training set.
  - Split each codeword into two slightly perturbed versions, doubling the size of the codebook.
  - Assign each vector in the training set to the nearest codeword, forming clusters around each codeword.
  - Update each codeword by computing the centroid of its cluster, minimizing the distortion within each cluster.
  - Repeat the previous two steps until the distortion converges or a desired codebook size is reached.
- The LBG algorithm is the most common algorithm for code generation that generates a codebook with minimum error from a training set.
- The LBG algorithm has some advantages over scalar quantization, such as :
  - It can achieve higher compression ratios by exploiting the correlation among the components of a vector.
  - It can preserve the quality of the reconstructed data by reducing the quantization noise and distortion.
  - It can adapt to the statistics of the data by using a variable-length codebook.



# Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the final codebook vectors.
- The advantage of TSVQ is that it can be represented by a binary tree, which reduces the storage cost, encoding rate, and quantization time compared to a full-search vector quantizer.
- TSVQ also allows for fast quantization search, as the encoder only needs to traverse a root-to-leaf path to find the closest codebook vector for a given input vector.
- TSVQ can be designed by using a top-down or a bottom-up approach. The top-down approach starts with the average of all the training vectors, and splits each node into two subnodes by perturbing the vector slightly. The bottom-up approach starts with a large number of initial codebook vectors, and merges them into a binary tree by minimizing the distortion.



# Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that use a predefined structure or algorithm to generate the codebook and encode the input vectors, rather than storing and searching the codebook explicitly.
- Structured vector quantizers can reduce the complexity, memory, and rate of vector quantization, while maintaining good performance in terms of distortion and quality.
- Some examples of structured vector quantizers are:

  - Tree-structured vector quantizers (TSVQs), which use a hierarchical partitioning of the input space and a binary tree to represent the codebook. TSVQs can be designed using clustering algorithms, such as the generalized Lloyd algorithm, or using classification algorithms, such as the CART algorithm  .
  - Lattice vector quantizers (LVQs), which use a regular geometric arrangement of points, such as a hexagonal or cubic lattice, to form the codebook. LVQs can be generated algorithmically, rather than stored, and can be encoded using fast algorithms, such as the nearest plane algorithm.
  - Product vector quantizers (PVQs), which use a Cartesian product of scalar or lower-dimensional vector quantizers to form the codebook. PVQs can exploit the correlation and structure of the input vectors, and can be encoded using a simple concatenation of the component quantizers.

- Structured vector quantizers have some advantages over scalar quantizers, such as:

  - Higher compression ratio, since vector quantizers can exploit the redundancy and correlation among the input variables, while scalar quantizers treat each variable independently.
  - Lower distortion, since vector quantizers can achieve the optimal rate-distortion performance for a given memory or block length, while scalar quantizers are suboptimal and depend on the distribution of the input variables.
  - Better quality, since vector quantizers can preserve the perceptual features and avoid the artifacts, such as contouring and blocking, that scalar quantizers may introduce.

