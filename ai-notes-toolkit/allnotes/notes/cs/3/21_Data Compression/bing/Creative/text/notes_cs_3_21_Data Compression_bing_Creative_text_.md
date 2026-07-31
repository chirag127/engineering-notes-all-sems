

## Unit 1 - Compression Techniques

- Compression is the process of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, documents, and executable files.
- Lossy compression techniques discard some data that is considered less important or perceptible. They are suitable for images, audio, and video files.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): Replaces consecutive identical symbols with a symbol and a count.
  - Huffman coding: Assigns variable-length codes to symbols based on their frequency of occurrence.
  - Lempel-Ziv-Welch (LZW): Builds a dictionary of common patterns and replaces them with shorter codes.
- Some common lossy compression techniques are:
  - JPEG: Applies discrete cosine transform (DCT) and quantization to reduce the size of images.
  - MP3: Applies psychoacoustic model and bit allocation to reduce the size of audio files.
  - MPEG: Applies motion estimation and compensation to reduce the size of video files.



### Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values are more frequent than others and can be represented with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and lossless audio formats .
- Lossless compression can reduce the file size by 50% or more, depending on the data and the compression algorithm.
- Some common lossless compression algorithms are Huffman coding, arithmetic coding, run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, and deflate algorithm.
- Lossless compression is different from lossy compression, which discards some data in the compression process and produces a lower-quality approximation of the original data. Lossy compression is suitable for applications that can tolerate some loss of information, such as images, videos, and lossy audio formats.



### Lossy Compression

- Lossy compression is a data compression method that sacrifices some information to achieve an even smaller file size than lossless compression.
- Lossy compression is often used on video, audio, and many types of image files, where some loss of quality is acceptable.
- Lossy compression works by using inexact approximations and partial data discarding to represent the content, reducing the amount of bits needed to store or transmit the data.
- Lossy compression can achieve high compression ratios, but at the cost of losing data permanently and degrading the quality of the original data.
- Lossy compression examples include JPEG, MP3, MPEG, and GIF.
- Lossy compression is suitable for applications where the quality of the data is not critical, such as streaming media, web browsing, and online gaming.
- Lossy compression is not suitable for applications where the quality of the data is important, such as text, medical images, and archival documents.



### Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or transforming the data into a more compact representation.
- Compression techniques can be classified into two categories: lossless and lossy. Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques allow some distortion or degradation of the data quality in exchange for higher compression ratios.
- Compression techniques can be applied to different types of data, such as text, images, audio, video, etc. Depending on the type and characteristics of the data, different compression techniques may be more suitable or efficient.
- To evaluate the performance of compression techniques, several metrics can be used, such as:
  - Compression ratio (CR): the ratio of the size of the original data to the size of the compressed data. Higher CR means higher compression efficiency.
  - Compression factor (CF): the inverse of CR, i.e., the ratio of the size of the compressed data to the size of the original data. Lower CF means higher compression efficiency.
  - Bits per character (bpc) or bits per pixel (bpp): the average number of bits used to represent each character or pixel in the compressed data. Lower bpc or bpp means higher compression efficiency.
  - Distortion: the difference between the original data and the decompressed data. Distortion can be measured by various criteria, such as mean squared error (MSE), root mean squared error (RMSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc. Lower distortion means higher data quality and fidelity.
  - Accuracy: the degree to which the compressed data preserves the essential information or features of the original data. Accuracy can be measured by various criteria, such as precision, recall, F1-score, etc. Higher accuracy means higher data utility and relevance.
  - Resource consumption: the amount of time, memory, or energy required to perform compression or decompression. Lower resource consumption means higher compression efficiency and scalability.
- To measure the performance of compression techniques, various tools and methods can be used, such as:
  - Query logs: records of the queries and responses of the compressed data. Query logs can be used to analyze the query execution time, throughput, latency, and accuracy of the compressed data queries.
  - Monitors: software or hardware devices that measure and display the resource consumption of the compression or decompression processes. Monitors can be used to analyze the CPU, memory, disk, or network usage of the compression or decompression processes.
  - Profilers: software or hardware tools that measure and report the performance characteristics of the compression or decompression algorithms. Profilers can be used to analyze the code complexity, execution time, memory allocation, function calls, etc. of the compression or decompression algorithms.
  - Benchmarks: standardized tests or datasets that evaluate and compare the performance of different compression techniques. Benchmarks can be used to measure and report the CR, CF, bpc, bpp, distortion, accuracy, and resource consumption of different compression techniques on various types of data.



### Modeling and coding for compression techniques

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques discard some information that is considered less important or perceptible.
- Modeling and coding are the two levels to compress data :
  - In the first level, the data will be analyzed for any redundant information and extract it to develop a model. The model captures the probability distribution or the structure of the data.
  - In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique. The encoding technique assigns shorter codes to more frequent or probable symbols and longer codes to less frequent or probable symbols.
- Some examples of modeling techniques are:
  - Markov models: These models assume that the probability of a symbol depends only on a fixed number of previous symbols. They can capture the statistical dependencies and patterns in the data.
  - Dictionary-based models: These models use a predefined or dynamically constructed dictionary of symbols or phrases to represent the data. They can exploit the repetitions and commonalities in the data.
  - Transform-based models: These models apply a mathematical transform to the data to change its representation from one domain to another. They can reduce the correlation and redundancy among the data elements.
- Some examples of coding techniques are:
  - Huffman coding: This is a lossless coding technique that assigns variable-length codes to the symbols based on their frequencies. It guarantees the optimal code length for a given source distribution.
  - Arithmetic coding: This is a lossless coding technique that assigns a single code to the entire data sequence based on its cumulative probability. It can achieve higher compression ratios than Huffman coding by avoiding the rounding errors.
  - Run-length encoding: This is a lossless coding technique that encodes the runs of identical symbols by their length and value. It is effective for compressing data with long runs of repeated symbols.
  - Lempel-Ziv coding: This is a lossless coding technique that uses a sliding window to store the previous symbols and encodes the current symbol by its position and length in the window. It is adaptive and can handle unknown or varying source distributions.
  - JPEG coding: This is a lossy coding technique that compresses images by applying a discrete cosine transform (DCT) to the image blocks, quantizing the DCT coefficients, and encoding them using Huffman or arithmetic coding. It can achieve high compression ratios by discarding the high-frequency components that are less visible to the human eye.
  - MP3 coding: This is a lossy coding technique that compresses audio by applying a modified discrete cosine transform (MDCT) to the audio frames, quantizing the MDCT coefficients, and encoding them using Huffman or arithmetic coding. It can achieve high compression ratios by discarding the components that are less audible to the human ear.



### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of a data file without losing any information or distorting the original data.
- Lossless compression is based on the concept of **entropy**, which measures the average amount of information per symbol in a data source.
- Entropy is defined as `H(X) = -sum(p(x)log(p(x)))`, where `X` is a discrete random variable, `p(x)` is the probability of occurrence of symbol `x`, and `log` is the logarithm base 2.
- Entropy is a lower bound for the average number of bits per symbol required to encode a data source without loss of information.
- Lossless compression algorithms try to achieve an encoding that is close to the entropy of the data source, or in other words, to minimize the **redundancy** of the data.
- Redundancy is the difference between the actual average number of bits per symbol and the entropy of the data source. It can be expressed as `R(X) = L(X) - H(X)`, where `L(X)` is the actual average number of bits per symbol.
- Redundancy can be reduced by exploiting the **statistical properties** of the data source, such as the frequency of occurrence of symbols, the correlation between symbols, and the patterns or regularities in the data.
- Some common lossless compression techniques are **Huffman coding**, **arithmetic coding**, **run-length encoding**, **dictionary-based encoding**, and **Lempel-Ziv encoding**. Each technique has its own advantages and disadvantages, depending on the characteristics of the data source and the compression requirements.



### A brief introduction to information theory for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information  .
- It was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding theorems  .
- Information theory is based on probability theory and statistics, and uses the fundamental unit of bit to measure the amount of information in a message or a source .
- Information theory has applications in various fields, such as communication, cryptography, data compression, machine learning, statistical inference, and thermodynamics .
- Information theory aims to answer questions such as:
  - How much information is contained in a message or a source?
  - How can information be efficiently encoded and decoded?
  - How can information be reliably transmitted and received over a noisy channel?
  - How can information be securely encrypted and decrypted?



### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques discard some information that is deemed less important or perceptible.
- Data compression can be applied to different types of data, such as text, images, audio, video, etc.
- Data compression can be achieved by using different models and techniques, depending on the characteristics and requirements of the data and the application.
- Some of the popular models and techniques for data compression are:

  - Pruning: Pruning is a technique that reduces the number of parameters in a deep neural network by removing redundant and inconsequential connections, neurons, channels, or layers . Pruning can improve the efficiency and speed of the network, as well as reduce the memory and storage requirements. Pruning can be done in different ways, such as weight pruning, unit pruning, channel pruning, layer pruning, etc.
  - Quantization: Quantization is a technique that reduces the precision of the numerical values in a deep neural network by using fewer bits to represent them . Quantization can reduce the size and complexity of the network, as well as the computational and energy costs. Quantization can be done in different ways, such as uniform quantization, non-uniform quantization, binary quantization, ternary quantization, etc.
  - Knowledge distillation: Knowledge distillation is a technique that transfers the knowledge from a large, complex network (teacher) to a smaller, simpler network (student) by using the outputs of the teacher network as soft labels for the student network . Knowledge distillation can improve the performance and generalization of the student network, as well as reduce the inference time and resource consumption. Knowledge distillation can be done in different ways, such as mimic learning, attention transfer, feature distillation, etc.
  - Low-rank factorization: Low-rank factorization is a technique that decomposes a large, dense matrix into a product of smaller, sparse matrices by exploiting the low-rank structure of the matrix . Low-rank factorization can reduce the number of operations and parameters in a deep neural network, as well as the memory and storage requirements. Low-rank factorization can be done in different ways, such as singular value decomposition, Tucker decomposition, tensor train decomposition, etc.



### Physical models for data compression

- Physical models are mathematical representations of the source data that capture the statistical properties and dependencies of the data.
- Physical models are used to estimate the probabilities of the data symbols and sequences, which are then used to design optimal codes for compression.
- Physical models can be classified into two types: memoryless and memory-based models.
- Memoryless models assume that each symbol in the data is independent of the previous symbols, and has a fixed probability distribution. Examples of memoryless models are uniform distribution, geometric distribution, and Huffman coding.
- Memory-based models assume that the probability of a symbol depends on the previous symbols, and can vary over time. Examples of memory-based models are Markov models, finite context models, and arithmetic coding.
- Memory-based models can achieve higher compression ratios than memoryless models, but they are also more complex and require more computation and memory resources.



### Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to different symbols or sequences of symbols that can be generated by the source.
- A probability model can be used to measure the amount of information in the data, and to design efficient compression algorithms that exploit the statistical properties of the data.
- There are different types of probability models, depending on the assumptions and the level of detail that are made about the source. Some common models are:

  - Uniform model: This model assumes that all symbols in the alphabet have the same probability of occurrence, and that the symbols are independent of each other. This model is simple, but often unrealistic for most sources of data.
  - Unigram model: This model assigns probabilities to individual symbols, based on their frequencies in the data, but still assumes that the symbols are independent of each other. This model is more realistic than the uniform model, but still ignores the correlations and patterns that may exist in the data.
  - Markov model: This model assigns probabilities to sequences of symbols, based on the conditional probabilities of the symbols given their previous symbols. This model captures the dependencies and correlations that may exist in the data, and can be generalized to different orders of context. For example, a first-order Markov model considers the probability of a symbol given its immediate predecessor, while a second-order Markov model considers the probability of a symbol given its previous two symbols, and so on.
  - Dictionary model: This model assigns probabilities to variable-length sequences of symbols, based on their frequencies in the data, and uses a dictionary to store and encode the sequences. This model can capture the repetitions and regularities that may exist in the data, and can achieve high compression ratios for some types of data.

- A probability model can be combined with a coding scheme to perform data compression. A coding scheme is a method of assigning binary codes to the symbols or sequences of symbols in the data, such that the codes are unambiguous and efficient. Some common coding schemes are:

  - Fixed-length coding: This coding scheme assigns codes of the same length to all symbols or sequences of symbols, regardless of their probabilities. This coding scheme is simple, but often wasteful of bits, especially for non-uniform sources.
  - Variable-length coding: This coding scheme assigns codes of different lengths to different symbols or sequences of symbols, such that the codes are shorter for more probable symbols or sequences, and longer for less probable ones. This coding scheme is more efficient than fixed-length coding, but requires a prefix-free or uniquely decodable code, which means that no code can be a prefix of another code, to avoid ambiguity in decoding.
  - Arithmetic coding: This coding scheme assigns codes to the entire data as a single fraction, rather than to individual symbols or sequences of symbols. This coding scheme is more efficient than variable-length coding, as it can exploit the exact probabilities of the symbols or sequences, and avoid the rounding errors that may occur in variable-length coding. However, this coding scheme is more complex and requires more arithmetic operations.

- The choice of the probability model and the coding scheme depends on the characteristics of the data and the requirements of the compression task. Some factors that may influence the choice are:

  - The size and complexity of the data: Larger and more complex data may require more sophisticated models and coding schemes to capture the information and achieve high compression ratios.
  - The availability and accuracy of the model: The model may be known in advance, learned from the data, or transmitted along with the data. The model may also be exact, approximate, or adaptive. These factors may affect the complexity and overhead of the compression algorithm.
  - The trade-off between compression ratio and speed: Higher compression ratios may require more complex models and coding schemes, which may increase the computational time and resources needed for compression and decompression. A balance between compression ratio and speed may be desirable for some applications.



### Markov models for data compression

- A Markov model is a mathematical model that describes a system that changes its state according to some probabilistic rules. The system is assumed to have the Markov property, which means that the future state of the system depends only on the current state and not on the past history.
- A Markov model can be used to model the source of a data stream, such as a text or an image, and to predict the next symbol in the stream based on the previous symbols. This prediction can be used to compress the data by encoding the symbols with fewer bits if they are more likely to occur, and more bits if they are less likely to occur. This is the principle of entropy coding, which aims to minimize the average number of bits per symbol.
- A Markov model can be represented by a directed graph, where the nodes are the possible states of the system and the edges are the transitions between the states with some probabilities. For example, a Markov model for a binary source can be represented by a graph with two nodes, 0 and 1, and four edges, each with a probability of transitioning from one state to another. The probabilities can be estimated from the data stream by counting the frequencies of the transitions.
- A Markov model can have different orders, which indicate how many previous symbols are used to predict the next symbol. A zero-order Markov model assumes that the next symbol is independent of the previous symbols, and thus assigns equal probabilities to all symbols. A first-order Markov model assumes that the next symbol depends only on the previous symbol, and thus assigns probabilities based on the frequencies of the pairs of symbols. A higher-order Markov model assumes that the next symbol depends on more previous symbols, and thus assigns probabilities based on the frequencies of the longer sequences of symbols. A higher-order Markov model can capture more complex patterns and dependencies in the data, but it also requires more memory and computation to store and update the probabilities.
- A Markov model can also be dynamic, which means that it can adapt to the changes in the data stream and update the probabilities accordingly. A dynamic Markov model can be more efficient and accurate than a static Markov model, which assumes that the data stream is stationary and uses fixed probabilities. A dynamic Markov model can be implemented by using a sliding window of the most recent symbols to estimate the probabilities, or by using a learning algorithm that adjusts the probabilities based on the feedback from the encoder or decoder.
- A Markov model can be combined with an arithmetic coding scheme to produce a powerful method of data compression. Arithmetic coding is a technique that assigns variable-length codes to the symbols based on their probabilities, such that the more probable symbols have shorter codes and the less probable symbols have longer codes. The codes are not fixed-length binary strings, but fractions of the interval [0, 1), which can be represented by a finite number of bits with some precision. The encoder and the decoder use the same Markov model to predict the probabilities of the symbols, and use them to divide the interval into subintervals for each symbol. The encoder encodes the data stream by choosing the subinterval that corresponds to the next symbol, and then narrowing the interval to that subinterval. The decoder decodes the data stream by finding the subinterval that contains the encoded fraction, and then outputting the symbol that corresponds to that subinterval. The process is repeated until the end of the data stream is reached. The encoded fraction can be converted to a binary string by using a binary search algorithm. The advantage of arithmetic coding is that it can achieve near-optimal compression, as the average number of bits per symbol approaches the entropy of the source. The disadvantage of arithmetic coding is that it requires more computation and precision than other coding schemes, such as Huffman coding.



### Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub>.
- A composite source model is useful for data compression because it can capture the variability and structure of the data more accurately than a single model.
- A composite source model can be used to describe some very complicated processes, such as natural language, images, audio, video, etc.
- A composite source model can be encoded using different techniques, such as arithmetic coding, Huffman coding, run-length encoding, etc.
- A composite source model can achieve high compression ratios and low distortion by exploiting the correlations and redundancies among the component sources.
- A composite source model can also be used to enrich an existing data source by adding new measures, calculations, or transformations.
- A composite source model can be implemented using different tools, such as Power BI, MATLAB, Python, etc .



### Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can reduce the storage space or transmission bandwidth required for a given piece of information.
- Data compression can be either lossless or lossy.
  - Lossless compression preserves the exact information of the original data, and can be reversed by decompression.
  - Lossy compression discards some information of the original data, and cannot be reversed by decompression.
  - Lossless compression is suitable for text, audio, and executable files, while lossy compression is suitable for images, video, and speech.
- Some common data compression techniques are:
  - Lempel–Ziv: a lossless algorithm that finds repeated characters in a data set and replaces them with tokens or shortened sequences.
  - Huffman coding: a lossless algorithm that assigns variable-length codes to symbols based on their frequency of occurrence.
  - Run-length encoding: a lossless algorithm that replaces consecutive identical characters with a single character and a count.
  - Arithmetic coding: a lossless algorithm that assigns codes to symbols based on their probability of occurrence.
  - JPEG: a lossy algorithm that reduces the quality of images by discarding high-frequency components.
  - MPEG: a lossy algorithm that reduces the quality of video and audio by discarding redundant or irrelevant frames or samples.
- Some best practices for data compression are:
  - Determine the compression level: depending on the needs, the data can be compressed to a certain level, such as low, medium, or high.
  - Choose the appropriate compression type: for every file to be compressed, first determine whether it is lossless or lossy, and then select the suitable algorithm.
  - Use a coprocessor: a dedicated hardware device that can perform compression and decompression faster and more efficiently than a general-purpose processor.
  - Consider data deduplication: a technique that eliminates duplicate or redundant data blocks and replaces them with pointers to a single copy.
  - Determine if multi-stage compression is needed: a technique that applies multiple compression algorithms in sequence to achieve higher compression ratios.



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords, i.e., no ambiguity in the decoding process.
- A code is non-singular if no two distinct source symbols have the same codeword.
- A non-singular code is not necessarily uniquely decodable, as there may be more than one way to partition a sequence of codewords into individual codewords.
- For example, the code M2 = {a -> 0, b -> 01, c -> 011} is non-singular, but not uniquely decodable, as the sequence 0110 can be decoded as either ab or ca.
- A code is prefix-free or instantaneous if no codeword is a prefix of another codeword, i.e., no codeword can be extended by adding more code symbols to form another codeword.
- A prefix-free code is always uniquely decodable, as the end of any codeword is recognizable without examining subsequent code symbols.
- For example, the code M3 = {a -> 0, b -> 01, c -> 011} is prefix-free and uniquely decodable.
- A uniquely decodable code is not necessarily prefix-free, as there may be codewords that are suffixes of other codewords, i.e., no codeword can be shortened by removing code symbols from the beginning to form another codeword.
- For example, the code M4 = {a -> 0, b -> 10, c -> 110} is uniquely decodable, but not prefix-free, as c is a suffix of b.
- A code is optimal if it minimizes the average codeword length for a given source distribution, i.e., it achieves the lowest possible redundancy or the highest possible compression ratio.
- A code is optimal if and only if it satisfies the Kraft inequality, which states that for any uniquely decodable code with codewords of lengths l1, l2, ..., ln, the following inequality holds:

  Kraft inequality

  where r is the size of the code alphabet.
- The Kraft inequality provides a necessary and sufficient condition for the existence of a uniquely decodable code with given codeword lengths, but it does not guarantee that such a code is optimal or prefix-free.
- To construct an optimal prefix-free code, one can use algorithms such as Huffman coding or arithmetic coding, which are based on the source probabilities and the code alphabet size.



### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

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
  - Variable-length prefix codes assign codewords of different lengths to symbols, depending on their probabilities, such that more probable symbols have shorter codewords and less probable symbols have longer codewords.
- Prefix codes can also be classified into two types: complete and incomplete.
  - Complete prefix codes assign codewords to all possible symbols in the alphabet, such that the binary tree is full.
  - Incomplete prefix codes assign codewords to only some symbols in the alphabet, such that the binary tree is not full and some leaf nodes are missing.
- Prefix codes can also be classified into two types: static and dynamic.
  - Static prefix codes assign codewords to symbols based on a fixed probability distribution, such that the code is predetermined and does not change during the encoding or decoding process.
  - Dynamic prefix codes assign codewords to symbols based on an adaptive probability distribution, such that the code is updated and changed during the encoding or decoding process according to the symbols encountered.
- Prefix codes can also be classified into two types: universal and non-universal.
  - Universal prefix codes assign codewords to integers such that whatever the true probability distribution on integers, as long as the distribution is monotonic, the expected lengths of the codewords are within a constant factor of the expected lengths that the optimal code for that probability distribution would have assigned.
  - Non-universal prefix codes assign codewords to integers based on a specific probability distribution, such that the expected lengths of the codewords are optimal for that probability distribution.



## Unit 2 - The Huffman coding algorithm

- The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols.
- The algorithm starts by creating a node for each symbol and assigning it a weight equal to its frequency. Then, it repeatedly merges the two nodes with the lowest weights into a new node, whose weight is the sum of the weights of its children. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to that symbol, and appending a 0 or a 1 depending on whether the left or the right child is taken at each step. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible codes for a given set of symbols and frequencies. The average length of the codes is equal to the entropy of the data, which is the lower bound for any lossless compression method.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video. However, it requires the knowledge of the frequencies of the symbols in the data, which may not be available or may change over time. In such cases, adaptive Huffman coding can be used, which updates the tree and the codes as new symbols are encountered.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies or probabilities of occurrence.
- The code with the lowest frequency is assigned the longest code, and the code with the highest frequency is assigned the shortest code.
- The average code length is minimized by Huffman coding, which is equivalent to minimizing the expected value of the code length.
- However, Huffman coding does not necessarily minimize the variance of the code length, which is the measure of how much the code length deviates from the average.
- The variance of the code length is given by the formula:

variance formula

where p_i is the probability of the i-th symbol, l_i is the code length of the i-th symbol, and L bar is the average code length.

- A minimum variance Huffman code is a Huffman code that minimizes the variance of the code length, subject to the constraint that the code is prefix-free.
- A prefix-free code is a code in which no codeword is a prefix of another codeword, which ensures that the code can be uniquely decoded.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm, which is as follows:

  - Sort the symbols in descending order of their probabilities.
  - Create a binary tree with n leaves, where each leaf corresponds to a symbol and its probability.
  - Repeat until there is only one node left in the tree:
    - Select the two nodes with the lowest probabilities and merge them into a new node, whose probability is the sum of the two nodes' probabilities.
    - Assign the new node a code bit of 0 or 1, and append it to the code bits of its children.
    - Insert the new node into the tree and remove the two nodes that were merged.
  - The code for each symbol is obtained by traversing the tree from the root to the leaf and concatenating the code bits along the path.

- The modification for the minimum variance Huffman code is to assign the code bit of 0 to the node with the higher probability and the code bit of 1 to the node with the lower probability, when merging two nodes.
- This ensures that the symbols with higher probabilities have shorter codes and lower variances, and the symbols with lower probabilities have longer codes and higher variances.
- The minimum variance Huffman code is not unique, as there may be more than one way to assign the code bits when merging two nodes with equal probabilities.
- An example of constructing a minimum variance Huffman code is given below:

  - Suppose the source alphabet is A = {a1, a2, a3, a4, a5, a6}, with probabilities P(a1) = P(a2) = 0.2, P(a3) = 0.25, P(a4) = 0.05, P(a5) = P(a6) = 0.15.
  - The initial tree is:

initial tree

  - The first step is to merge a4 and a6, which have the lowest probabilities, into a new node with probability 0.2. Assign the code bit of 0 to a4 and the code bit of 1 to a6. The tree becomes:

first step

  - The second step is to merge a1 and a2, which have the lowest probabilities, into a new node with probability 0.4. Assign the code bit of 0 to a1 and the code bit of 1 to a2. The tree becomes:

second step

  - The third step is to merge the two nodes with probability



### Adaptive Huffman coding

- Adaptive Huffman coding (also called Dynamic Huffman coding) is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data.
- It uses a binary tree to store the symbols and their frequencies, and updates the tree as new symbols are encountered.
- The tree is constructed such that the most frequent symbols are near the root and have shorter codes, while the less frequent symbols are near the leaves and have longer codes.
- The tree is maintained using two rules:
  - Sibling property: The nodes in the tree are ordered by decreasing weight, and the sibling of a node is the node to its right. The weight of a node is the sum of the weights of its children, or the frequency of the symbol if it is a leaf node.
  - Swap property: Whenever a new symbol is added or an existing symbol is updated, the tree is rearranged to preserve the sibling property. This may involve swapping nodes that are not siblings or ancestors.
- The encoding process is as follows:
  - Initialize the tree with a special node called NYT (Not Yet Transmitted), which has a weight of zero and no symbol.
  - For each symbol in the input:
    - If the symbol is already in the tree, output its code and increment its weight and the weights of its ancestors. Then, apply the swap property to the tree.
    - If the symbol is not in the tree, output the code of NYT followed by the fixed-length code of the symbol. Then, add the symbol as a leaf node to the right of NYT, and create a new NYT node as its left sibling. Increment the weights of the new symbol and its ancestors, and apply the swap property to the tree.
- The decoding process is as follows:
  - Initialize the tree with a special node called NYT, which has a weight of zero and no symbol.
  - For each bit in the input:
    - Traverse the tree from the root according to the bit. If the bit is 0, go to the left child; if the bit is 1, go to the right child.
    - If the node reached is a leaf node, output its symbol and increment its weight and the weights of its ancestors. Then, apply the swap property to the tree.
    - If the node reached is NYT, read the next fixed-length bits and output the corresponding symbol. Then, add the symbol as a leaf node to the right of NYT, and create a new NYT node as its left sibling. Increment the weights of the new symbol and its ancestors, and apply the swap property to the tree.
- The advantage of adaptive Huffman coding is that it can handle any source distribution without prior knowledge, and can adjust to changing frequencies dynamically.
- The disadvantage of adaptive Huffman coding is that it requires more computation and memory to update and rearrange the tree, and it may not achieve optimal compression if the source distribution is not stationary.
- An example of adaptive Huffman coding is shown below:

Adaptive Huffman coding example

: https://en.wikipedia.org/wiki/Adaptive_Huffman_coding
: https://xlinux.nist.gov/dads/HTML/adaptiveHuffman.html
: https://www.geeksforgeeks.org/adaptive-huffman-coding-and-decoding/
: http://ben-tanen.com/adaptive-huffman/



### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols. The frequency of each node is the sum of the frequencies of its children.
- The algorithm starts with a list of nodes, each containing a symbol and its frequency. The list is sorted in ascending order of frequency. Then, the algorithm repeatedly performs the following steps until there is only one node left in the list:
  - Select the two nodes with the lowest frequency and create a new node with the sum of their frequencies as its frequency. The two nodes become the left and right children of the new node.
  - Remove the two nodes from the list and insert the new node in the sorted order.
- The final node is the root of the Huffman tree. The code for each symbol is obtained by traversing the tree from the root to the leaf, appending a 0 for each left branch and a 1 for each right branch.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible code for any given data. However, the optimality depends on the accuracy of the frequency estimates and the assumption that the symbols are independent and identically distributed.
- The Huffman coding algorithm can be extended to handle more than two symbols per node, such as ternary Huffman coding, or to handle unequal costs for different symbols, such as arithmetic coding.



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol .
- The encoding procedure for the Huffman coding algorithm can be summarized as follows :
  - Create a leaf node for each character and assign it a weight (frequency of appearance) and add it to a priority queue.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest weight from the queue.
    - Create a new internal node with these two nodes as children and with weight equal to the sum of their weights.
    - Assign a bit (0 or 1) to each edge of the tree, descending from the new node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the tree and assign codes to each character by concatenating the bits along the path from the root to the leaf node.
  - Encode each character in the input data by replacing it with its corresponding code from the tree.
  - Decode the encoded data by starting from the root of the tree and following the bits until reaching a leaf node, and then outputting the character stored in that node. Repeat until the end of the encoded data.



### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the source data.
- The Huffman coding algorithm consists of two phases: building a Huffman tree and generating the codes.
- The Huffman tree is a binary tree that represents the optimal prefix code for the source data. The tree is constructed by merging the two least frequent symbols repeatedly until only one symbol remains. The symbols are stored in the leaves of the tree, and the frequency of each symbol is the sum of the frequencies of its children.
- The codes are generated by traversing the Huffman tree from the root to the leaves. Each time a left branch is taken, a 0 is appended to the code, and each time a right branch is taken, a 1 is appended to the code. The code for each symbol is the sequence of bits obtained by following the path from the root to the corresponding leaf.
- The decoding procedure is the inverse of the encoding procedure. Given a Huffman tree and a sequence of bits, the decoder starts from the root of the tree and follows the branches according to the bits. Each time a leaf is reached, the symbol stored in the leaf is output and the decoder returns to the root. The decoding process ends when all the bits are consumed.



### Golomb codes

- Golomb codes are a type of parameterized codes that can encode positive integers with variable-length codewords.
- Golomb codes use a parameter M to divide an input value x into two parts: q, the quotient of x divided by M, and r, the remainder of x modulo M.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r.
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The binary code for r depends on the value of M. If M is a power of 2, say M=2^n, then the binary code for r is simply the n-bit binary representation of r. For example, if M=8, then the binary code for r=5 is 101.
- If M is not a power of 2, then the binary code for r is a truncated binary code, which uses fewer bits for the smaller values of r. For example, if M=5, then the binary code for r=0 is 0, for r=1 is 10, for r=2 is 110, for r=3 is 1110, and for r=4 is 1111.
- The length of the codeword for x is q+1 plus the number of bits needed to encode r. For example, if M=5 and x=17, then q=3, r=2, the unary code for q+1 is 11110, the binary code for r is 110, and the codeword for x is 11110110, which has length 8.
- Golomb codes are optimal for encoding geometric distributions, where the probability of x is proportional to (1-p)^x for some p. The optimal value of M is approximately -1/log(1-p).
- Golomb codes are widely used in data compression, especially for lossless compression of images and audio. Some examples of applications are run-length encoding, Rice coding, and exp-Golomb coding.



### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the Golomb codes.
- To encode a number x using Rice codes, the following steps are performed :
  - Divide x by m and write the quotient in unary code, i.e., a sequence of 1s followed by a 0.
  - Write the remainder in binary code, using k bits.
  - Concatenate the unary and binary codes to form the Rice code for x.
- For example, if k = 2 and x = 11, then the Rice code is 1110 11, where 1110 is the unary code for 11/4 = 2 and 11 is the binary code for 11%4 = 3.
- To decode a Rice code, the following steps are performed :
  - Read the unary code until a 0 is encountered and count the number of 1s, which is the quotient q.
  - Read the next k bits and interpret them as a binary number, which is the remainder r.
  - Multiply q by m and add r to obtain the original number x.
  - For example, if k = 2 and the Rice code is 1110 11, then the decoded number is 2*4 + 3 = 11.



### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall coding is a type of source coding that converts variable-length words from the source alphabet into fixed-length codewords from the code alphabet  .
- Tunstall coding requires the algorithm to know the probability distribution of each letter of the source alphabet before the encoding process . This is also a requirement for Huffman coding.
- Tunstall coding is based on the idea of parsing the source text into words that are optimal for the given probability distribution. The words are not necessarily the same as the natural words of the language, but rather sequences of letters that have high probabilities of occurring together.
- Tunstall coding uses a tree structure to generate the codewords for each word in the source text. The tree is constructed by starting with a single node that represents the empty word, and then splitting it into branches according to the probabilities of each letter following the empty word. The process is repeated recursively for each branch until the desired number of codewords is reached.
- The codewords are assigned to the words by traversing the tree in a breadth-first order and assigning a binary digit to each branch. The codeword for a word is the concatenation of the binary digits along the path from the root to the node that represents the word.
- Tunstall coding is a prefix code, meaning that no codeword is a prefix of another codeword. This ensures that the decoding process is unambiguous and can be done by matching the codewords with the words in the tree.
- Tunstall coding has some advantages and disadvantages compared to other source coding methods. Some of the advantages are:
  - It produces a fixed-length output, which can be useful for applications that require constant transmission rate or storage size.
  - It can achieve a compression ratio close to the entropy of the source, which is the theoretical limit for lossless compression.
  - It can adapt to changes in the source distribution by updating the tree structure accordingly.
- Some of the disadvantages are:
  - It requires a large amount of memory to store the tree structure, which can be impractical for large alphabets or long codewords.
  - It can be inefficient for sources that have low redundancy or high variability, as the words may not capture the correlations well.
  - It can be sensitive to errors in the transmission or storage of the codewords, as a single bit error can affect the decoding of the entire word.



### Applications of Huffman coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the symbols in the data, such that the symbols that occur more frequently have shorter codes and the symbols that occur less frequently have longer codes. This way, the average length of the codes is minimized and the data can be stored or transmitted more efficiently. Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel, such as a phone line or a wireless network. This reduces the bandwidth and the cost of transmission. For example, the ITU-T T.4 standard for fax transmission uses a variant of Huffman coding called Modified Huffman coding.
- **Conventional compression formats**: Huffman coding is often used by compression formats that are widely used for archiving or transferring files, such as PKZIP, GZIP, BZIP2, etc. These formats combine Huffman coding with other techniques, such as run-length encoding, dictionary encoding, or arithmetic coding, to achieve higher compression ratios .
- **Multimedia codecs**: Huffman coding is also used by multimedia formats that encode images, audio, or video data, such as JPEG, PNG, and MP3. These formats use Huffman coding to encode the quantized coefficients or the frequency components of the data, after applying some transformation, such as discrete cosine transform or discrete Fourier transform. This reduces the redundancy and the size of the data, while preserving the quality  .



### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the image.
  - Sort the symbols in the frequency table in ascending order of frequency.
  - Build a binary tree by repeatedly merging the two least frequent symbols into a new node with a frequency equal to the sum of their frequencies. The merged symbols become the left and right children of the new node. Repeat this process until there is only one node left, which is the root of the tree.
  - Assign a code to each symbol by traversing the tree from the root to the leaf. Append a 0 to the code when moving to the left child and a 1 when moving to the right child. The code of a symbol is the sequence of bits along the path from the root to the leaf corresponding to that symbol.
  - Encode the image by replacing each symbol with its code.
  - Decode the image by traversing the tree from the root to the leaf according to the bits in the code.

- Huffman coding is optimal for a given source if the symbol probabilities are powers of two. Otherwise, it is near-optimal and achieves the Shannon entropy bound asymptotically as the number of symbols increases.
- Huffman coding is widely used in lossless image compression formats such as PNG, GIF, and TIFF. It can also be combined with other techniques such as run-length encoding, arithmetic coding, dictionary techniques, and predictive coding to improve the compression performance.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The idea behind Huffman coding is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized  .
- Huffman coding works as follows  :
  - Create a leaf node for each character and assign it a weight equal to its frequency.
  - Sort the nodes in ascending order of their weights and insert them into a priority queue.
  - While there is more than one node in the queue, do the following:
    - Remove the two nodes with the lowest weights from the queue and create a new internal node with a weight equal to the sum of their weights.
    - Make the two nodes the left and right children of the new node and insert the new node into the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each character by appending 0 for a left branch and 1 for a right branch.
- To compress a text file using Huffman coding :
  - Scan the file and count the frequency of each character.
  - Build the Huffman tree using the frequency table.
  - Generate the codes for each character by traversing the tree.
  - Encode the file by replacing each character with its corresponding code.
  - Write the encoded file along with the frequency table or the Huffman tree for decoding.
- To decompress a text file using Huffman coding :
  - Read the frequency table or the Huffman tree from the encoded file.
  - Reconstruct the Huffman tree using the frequency table or the tree itself.
  - Decode the file by traversing the tree from the root to the leaves for each code in the file.
  - Write the decoded file by replacing each code with its corresponding character.
- Huffman coding is an optimal prefix code, meaning that no code is a prefix of another code, and that it minimizes the expected code length for a given set of characters and frequencies  .
- Huffman coding is a greedy algorithm, meaning that it makes the optimal choice at each step without considering the global optimum  .
- Huffman coding can be used for any type of data, not just text, as long as the data can be represented as a sequence of symbols with known frequencies  .



### Audio Compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Audio compression is the process of reducing the size of an audio file by removing or encoding redundant or irrelevant information.
- Huffman coding is a method of data compression that is independent of the data type, that is, the data could represent an image, audio or spreadsheet.
- Huffman coding works by looking at the data stream that makes up the file to be compressed and assigning variable-length codes to each symbol based on their frequency of occurrence .
- The symbols that occur more often are assigned shorter codes, while the symbols that occur less often are assigned longer codes.
- Huffman coding produces a prefix-free code, which means that no code for any symbol will be at the beginning of the code for another symbol. This makes decoding easier and unambiguous.
- Huffman coding is an optimal method of compression, which means that it minimizes the average code length for a given set of symbols and probabilities.
- Huffman coding can be implemented using a binary tree data structure, where each leaf node represents a symbol and its code, and each internal node represents the combined frequency of its children.
- To construct a Huffman tree, the following steps are followed:
  - Create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and with frequency equal to the sum of their frequencies.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
- To encode a symbol, follow the path from the root to the leaf node representing that symbol and append a 0 for each left branch and a 1 for each right branch.
- To decode a bit stream, start from the root and follow the branches according to the bits until reaching a leaf node, which represents the decoded symbol.
- Huffman coding can be static or dynamic, depending on whether the code table is fixed or updated during the compression process.
- Static Huffman coding uses a predefined code table that is known to both the encoder and the decoder, and does not change during the compression process.
- Dynamic Huffman coding adapts the code table based on the data being compressed, and transmits the code table along with the compressed data.
- Dynamic Huffman coding can achieve better compression ratios than static Huffman coding, especially for non-uniform data distributions.
- Huffman coding can be combined with other compression techniques, such as subband coding, run-length encoding, or differential coding, to improve the compression performance .



## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term of the sequence, usually denoted by a<sub>1</sub>.
  - Define the rule or formula that determines the next term of the sequence, usually denoted by a<sub>n</sub>.
  - Use a loop or a recursion to generate the terms of the sequence until a certain condition is met, such as reaching a limit, a target, or an error.
  - Store, display, or return the terms of the sequence as desired.
- For example, to code the sequence of even numbers starting from 2, we can use the following Python code:

```python
# Define the first term of the sequence
a1 = 2
# Define the rule or formula that determines the next term of the sequence
def next_term(a):
  return a + 2
# Use a loop to generate the terms of the sequence until a limit is reached
limit = 20
a = a1
while a <= limit:
  # Display the term of the sequence
  print(a)
  # Update the term of the sequence using the rule or formula
  a = next_term(a)
```

- The output of this code is:

```text
2
4
6
8
10
12
14
16
18
20
```



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits than the original representation. Data compression can be either lossless or lossy, depending on whether the original data can be perfectly recovered or not.
- A binary code is a way of representing data using only two symbols, usually 0 and 1. A binary code can be fixed-length or variable-length, depending on whether all the codewords have the same length or not. A binary code can also be prefix-free, meaning that no codeword is a prefix of another codeword.
- A coding sequence is a way of assigning binary codewords to a set of symbols, such as letters, numbers, or pixels. A coding sequence can be based on the frequency of the symbols, the structure of the data, or some other criteria. A coding sequence can be either static or dynamic, depending on whether the codewords are fixed or change over time.
- The goal of generating a binary code for a coding sequence is to minimize the average length of the codewords, while preserving the information content of the data. The average length of the codewords can be calculated as the sum of the products of the probabilities and the lengths of the symbols, or L = ∑p_i l_i, where p_i is the probability of symbol i and l_i is the length of its codeword.
- There are different methods for generating a binary code for a coding sequence, depending on the type and characteristics of the data. Some of the common methods are:

  - Huffman coding: This is a lossless and prefix-free method that assigns shorter codewords to more frequent symbols and longer codewords to less frequent symbols. It uses a binary tree to construct the codewords, starting from the bottom and merging the two least probable symbols at each step. The codewords are then obtained by traversing the tree from the root to the leaves and assigning 0 or 1 to each branch. This method guarantees the optimal average length for a given set of symbols and probabilities. 
  - LZW coding: This is a lossless and variable-length method that builds a dictionary of codewords based on the input data. It starts with a fixed set of codewords for the basic symbols, and then adds new codewords for sequences of symbols that appear in the data. It encodes the data by replacing each symbol or sequence with its corresponding codeword. This method adapts to the structure and patterns of the data and can achieve high compression ratios for repetitive data. 
  - Universal coding: This is a lossless and prefix-free method that assigns codewords to positive integers, regardless of their probability distribution. It has the property that the expected length of the codewords is within a constant factor of the optimal length for any monotonic probability distribution. This method is useful for encoding the lengths or frequencies of symbols, or the differences between consecutive symbols. Some examples of universal codes are unary code, binary code, Elias gamma code, and Fibonacci code.



### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing text, computer instructions, or any other data using a two-symbol system, usually 0 and 1 .
- Huffman coding is a method of compressing data using variable-length codes based on the frequencies of the symbols .
- The main difference between binary and Huffman coding is that binary coding assigns a fixed number of bits to each symbol, while Huffman coding assigns a variable number of bits to each symbol.
- Binary coding is simple and easy to implement, but it may not be efficient for data compression, as some symbols may occur more frequently than others and still take the same number of bits.
- Huffman coding is more complex and requires building a Huffman tree and a code table, but it can achieve optimal data compression, as the most frequent symbols take fewer bits and the least frequent symbols take more bits.
- Binary coding is suitable for data transmission and storage, as it can represent any kind of data using a universal binary system.
- Huffman coding is suitable for lossless data compression, as it can reduce the size of the data without losing any information.



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a sequence, such that the code can be used to reconstruct the original sequence without any loss of information.
- Coding a sequence can be used for various applications, such as:
  - **Data compression**: Coding a sequence can reduce the number of bits required to store or transmit a sequence, by using shorter codes for more frequent symbols and longer codes for less frequent symbols. This can save storage space, bandwidth, and energy. Examples of data compression algorithms that use coding a sequence are Huffman coding, arithmetic coding, and Lempel-Ziv coding.
  - **Error detection and correction**: Coding a sequence can add redundancy to a sequence, by using codes that have certain properties, such as parity, checksum, or Hamming distance. This can help detect and correct errors that may occur during transmission or storage of a sequence. Examples of error detection and correction codes are cyclic redundancy check (CRC), Hamming code, and Reed-Solomon code.
  - **Encryption**: Coding a sequence can transform a sequence into a different sequence, by using codes that are based on a secret key or a mathematical function. This can protect the confidentiality, integrity, and authenticity of a sequence. Examples of encryption algorithms that use coding a sequence are substitution cipher, transposition cipher, and stream cipher.



### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image.
- The JBIG standard is an early lossless image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group.
- The JBIG standard was standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines.
- The JBIG standard uses a technique called arithmetic coding, which assigns variable-length codes to symbols based on their probabilities of occurrence.
- The JBIG standard also uses a technique called adaptive template matching, which adapts the coding context to the local image features.
- The JBIG standard can achieve compression ratios of up to 20:1 for typical fax images.
- The JBIG standard has been superseded by the JBIG2 standard, which offers better compression performance and supports both lossless and lossy compression.
- The JBIG2 standard is suitable for compressing text, halftones, and generic bi-level images.
- The JBIG2 standard uses a technique called model-based coding, which segments the image into regions and assigns codes to each region based on its type and content.
- The JBIG2 standard also uses a technique called nearby neighbor based coding, which exploits the similarity between neighboring pixels or regions.
- The JBIG2 standard can achieve compression ratios of up to 100:1 for typical fax images.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression, in its lossless mode.
- JBIG2 can also achieve much higher compression ratios than the previous standards in its lossy mode, with almost no visible degradation of quality, by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- JBIG2 works by segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and applying compression techniques that are specially optimized for each type of content.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and using a dictionary to store them.
- Halftone regions are compressed by identifying and encoding the shape and position of the halftone dots, which are used to create shades of gray or color in printing.
- Generic regions are compressed by using arithmetic coding or MMR (Modified Modified READ), which are entropy coding methods that exploit the statistical properties of the data.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used in document imaging, such as scanning, faxing, and PDF files.



### Image compression

Image compression is a type of data compression applied to digital images, to reduce their cost for storage or transmission. Algorithms may take advantage of visual perception and the statistical properties of image data to provide superior results compared with generic data compression methods which are used for other digital data.

Some of the main concepts and techniques involved in image compression are:

- **Image file formats**: Different image file formats such as JPG, PNG, GIF, TIF, etc. use different algorithms to change how image data is stored and to produce smaller-sized files (measured in bytes). Some formats are lossy, meaning they discard some information from the original image, while others are lossless, meaning they preserve the original image quality.
- **Image quality**: Image quality is a subjective measure of how well an image preserves the details and colors of the original image. Image quality can be affected by factors such as compression ratio, bit depth, resolution, noise, artifacts, etc. Image quality can be measured by objective metrics such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc. or by subjective evaluations by human observers.
- **Image resolution**: Image resolution is the number of pixels (picture elements) that make up an image. Higher resolution images have more pixels and can display more details, but they also require more storage space and bandwidth. Image resolution can be reduced by downsampling, which is the process of removing some pixels from the image, or by resizing, which is the process of changing the dimensions of the image while keeping the same number of pixels.
- **Image color space**: Image color space is the way of representing the colors of an image using numerical values. Different color spaces have different ranges and properties, and they can affect the image quality and size. Some common color spaces are RGB (red, green, blue), CMYK (cyan, magenta, yellow, black), YCbCr (luminance, blue chrominance, red chrominance), etc. Image color space can be changed by color conversion, which is the process of mapping the color values from one color space to another.
- **Image transformation**: Image transformation is the process of changing the representation of an image from the spatial domain (where each pixel has a location and a value) to another domain (such as the frequency domain, where each pixel has a frequency and a magnitude). Image transformation can help to separate the image into different components, such as low-frequency and high-frequency components, and to apply different compression techniques to each component. Some common image transformations are discrete cosine transform (DCT), discrete wavelet transform (DWT), etc.
- **Image quantization**: Image quantization is the process of reducing the number of possible values for each pixel in an image. Image quantization can help to reduce the image size by using fewer bits to represent each pixel, but it can also introduce errors and distortions in the image. Image quantization can be uniform, where each pixel value is mapped to the nearest value in a predefined set, or non-uniform, where the pixel values are clustered into groups based on their similarity or importance.
- **Image coding**: Image coding is the process of encoding the image data into a binary stream that can be stored or transmitted. Image coding can use different methods such as run-length encoding (RLE), Huffman coding, arithmetic coding, etc. to reduce the redundancy and entropy of the image data. Image coding can also use different modes such as predictive coding, differential coding, etc. to exploit the correlation and similarity among the pixels or blocks of pixels in the image.



### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the redundancy and the size of the data.
- There are many variants of dictionary techniques, such as LZ77, LZ78, LZW, LZSS, LZMA, etc. They differ in the way they construct and manage the dictionary, the way they encode and decode the matches, and the way they handle special cases such as unmatched symbols or long matches.
- Dictionary techniques are suitable for compressing natural language texts, executable files, and some types of multimedia data. They can achieve high compression ratios and fast decompression speeds, but they may require large memory space and processing time for compression.



### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- In this unit, we will learn how to encode a sequence of symbols using different coding techniques, such as fixed-length codes, variable-length codes, prefix codes, and Huffman codes.
- A code is a mapping from a set of symbols (called the source alphabet) to a set of binary strings (called the code words).
- The goal of coding is to reduce the number of bits required to represent the sequence, while preserving the information content and allowing for efficient decoding.
- Coding can be lossless or lossy, depending on whether the original sequence can be perfectly reconstructed from the code words or not.
- Lossless coding is suitable for applications where the exact reproduction of the original sequence is essential, such as text, audio, or image compression.
- Lossy coding is acceptable for applications where some distortion or degradation of the original sequence is tolerable, such as video or speech compression.
- In this unit, we will focus on lossless coding techniques, which can be divided into two categories: entropy coding and dictionary coding.
- Entropy coding is based on the statistical properties of the source symbols, such as their frequencies or probabilities of occurrence. It assigns shorter code words to more frequent symbols and longer code words to less frequent symbols, thus minimizing the average code word length.
- Dictionary coding is based on the structural properties of the source symbols, such as their patterns or repetitions. It builds a dictionary of common phrases or substrings and assigns code words to them, thus exploiting the redundancy in the sequence.
- In the next sections, we will discuss the following topics:

  - Fixed-length codes and variable-length codes
  - Prefix codes and their properties
  - Huffman coding algorithm and its optimality
  - Extensions and variations of Huffman coding
  - Applications and examples of coding techniques



### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a data compression technique that uses a fixed set of entries to replace phrases or symbols in the input data .
- The dictionary can be constructed from prior knowledge of the data source, or from a sample of the data to be compressed .
- Static dictionary compression can be faster than adaptive or dynamic dictionary compression, but it may not achieve optimal compression ratios if the dictionary does not match the data well.
- Static dictionary compression can be implemented using various algorithms, such as Huffman coding, arithmetic coding, Lempel-Ziv coding, or digram coding  .
- Static dictionary compression can be applied to compress short texts, such as tweets, SMS, or web pages, by using word-based dictionaries that are derived from clustering methods.
- Static dictionary compression can also be combined with other compression techniques, such as run-length encoding, delta encoding, or entropy encoding, to improve the compression performance .



### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes.
- Diagram coding works in two passes: the first pass scans the source data and builds a dictionary of digrams and their corresponding codes, the second pass encodes the source data using the dictionary .
- Diagram coding can be iterated multiple times to improve the compression ratio, by adding more digrams to the dictionary in each iteration.
- Diagram coding is suitable for compressing text or simple images, but not for binary data or complex images .
- Diagram coding is an example of an ad hoc compression method, which means it is not based on a general model of the source data, but rather on some specific features or patterns .

: https://hbfs.wordpress.com/2009/02/17/ad-hoc-compression-methods-digram-coding/

: https://cai.type.sk/content/2010/5/issdc-digram-coding-based-lossless-data-compression-algorithm/1897.pdf

: https://dzone.com/articles/algorithm-week-data-1

: https://en.wikipedia.org/wiki/Data_compression



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel .
- LZ77 uses a sliding window to store the most recent data and find matches with the current data. It encodes the data as a pair of offset and length, indicating how far back in the window the match is and how long it is .
- LZ78 uses a tree structure to store the data and find matches with the current data. It encodes the data as a pair of index and symbol, indicating the position of the match in the tree and the next symbol after the match .
- LZW is a variation of LZ78 that uses a hash table instead of a tree to store the data and find matches. It encodes the data as a single index, indicating the position of the match in the table .
- Adaptive dictionary can compress data that is stored within data rows, including inlined LOB or XML values . It can also compress data that is not plain text, such as audio or video data.
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data. However, it may also incur some overheads, such as memory usage, dictionary management, and decompression speed .



### The LZ77 Approach

- LZ77 is a lossless data compression algorithm that reduces the size of the input data by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream.
- LZ77 uses a sliding window technique to find matches between the current data and the previous data. The sliding window consists of two parts: a search buffer and a look-ahead buffer. The search buffer contains the data that has been encoded so far, and the look-ahead buffer contains the data that is yet to be encoded.
- LZ77 encodes the input data as a sequence of triples, each consisting of three elements: an offset, a length, and a literal. The offset and the length specify the location and the size of the matching data in the search buffer, and the literal is the next symbol in the look-ahead buffer that does not match the search buffer.
- LZ77 decompresses the data by using the triples to reconstruct the original data. For each triple, it copies the data from the search buffer to the output, and then appends the literal to the output. The search buffer is updated with the copied data and the literal.
- LZ77 is an adaptive algorithm that adjusts the size of the sliding window according to the characteristics of the input data. A larger sliding window can find longer matches and achieve higher compression, but it also requires more bits to encode the offset and the length. A smaller sliding window can encode the offset and the length with fewer bits, but it may miss some matches and achieve lower compression.
- LZ77 is the basis for many variations and improvements, such as LZSS, LZW, LZMA, and others. These algorithms use different techniques to encode the triples more efficiently, such as using variable-length codes, dictionaries, or entropy coding.



### The LZ78 Approach

- LZ78 is a lossless data compression algorithm that was proposed by Abraham Lempel and Jacob Ziv in 1978 .
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- The dictionary is initialized with all possible single characters as the first entries, and then new entries are added as new sequences are encountered in the input.
- The output of LZ78 consists of pairs of numbers, where the first number is the index of the dictionary entry that matches the longest prefix of the current input, and the second number is the next character after the prefix.
- The output pairs are encoded using a variable-length code, such as Huffman coding, to reduce the size of the compressed data.
- LZ78 has the advantage of being adaptive, meaning that it does not require any prior knowledge of the input data or its statistics.
- LZ78 also has the advantage of being easy to implement and having a fast decompression process, since the dictionary can be reconstructed from the output pairs.
- However, LZ78 has some drawbacks, such as having a large memory requirement for the dictionary, which can grow indefinitely as new entries are added.
- LZ78 also has a poor compression ratio for inputs that have a high degree of repetition or redundancy, since it does not exploit the locality of the input data.
- LZ78 is the basis for many variations and improvements, such as LZW, LZSS, LZMA and others, which aim to overcome some of the limitations of LZ78 .



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Coding a sequence is a technique of data compression that assigns codes to sequences of input bytes, rather than individual bytes .
- Coding a sequence can achieve better compression ratio than coding individual bytes, especially for data that contains repeated patterns or sequences .
- Coding a sequence can also improve the energy efficiency of wireless sensors, by reducing the amount of data that needs to be transmitted.
- Some examples of coding a sequence algorithms are:
  - LZW (Lempel–Ziv–Welch) algorithm, which uses a dictionary to store sequences of bytes and their codes, and updates the dictionary as new sequences are encountered .
  - Huffman coding algorithm, which uses a binary tree to assign codes to bytes based on their frequency of occurrence, and can also be extended to code sequences of bytes .
  - Sequence statistical code based algorithm, which uses SDC and FOST codes to encode sequences of bytes based on their statistical properties, and can achieve better compression ratio than arithmetic coding.



### File Compression-UNIX compress

- File compression is the process of reducing the size of a file by removing redundant or irrelevant data, or by using efficient encoding schemes.
- File compression can save disk space, bandwidth, and transmission time, and can also protect data from unauthorized access or modification.
- UNIX compress is one of the file compression utilities available on UNIX systems. It uses the Lempel-Ziv algorithm to compress files and adds a .Z extension to the compressed file name.
- UNIX compress can be invoked by the command `compress filename`, where filename is the name of the file to be compressed. The original file is replaced by the compressed file, unless the -c option is used, which writes the compressed output to the standard output.
- UNIX compress can also compress multiple files at once by specifying a list of file names or a wildcard pattern. For example, `compress *.txt` will compress all the files with the .txt extension in the current directory.
- UNIX compress can decompress files by using the -d option or by invoking the uncompress command. For example, `compress -d filename.Z` or `uncompress filename.Z` will decompress the file filename.Z and restore the original file.
- UNIX compress can also decompress multiple files at once by specifying a list of file names or a wildcard pattern. For example, `compress -d *.Z` or `uncompress *.Z` will decompress all the files with the .Z extension in the current directory.
- UNIX compress is not compatible with other compression utilities, such as gzip or zip, which use different algorithms and file formats. To compress or decompress files using these utilities, one has to use their respective commands, such as gzip, gunzip, zip, or unzip.
- UNIX compress is also less efficient than newer compression utilities, such as gzip or bzip2, which can achieve higher compression ratios and faster speeds. Therefore, UNIX compress is not widely used anymore, except for legacy or compatibility reasons.



### Image Compression

- Image compression is a process applied to a digital image to reduce its size in bytes without degrading its quality below an acceptable level .
- Image compression is useful for saving disk or memory space, transmitting images faster and more efficiently, and enhancing the performance of image processing applications .
- Image compression can be classified into two types: lossless and lossy .
  - Lossless compression preserves the exact information of the original image, and allows the original image to be reconstructed from the compressed image without any loss of quality .
  - Lossy compression discards some information of the original image, and produces a compressed image that is similar but not identical to the original image. Lossy compression can achieve higher compression ratios than lossless compression, but at the cost of some quality degradation .
- Image compression algorithms can exploit the visual perception and the statistical properties of image data to achieve better compression results than generic data compression methods .
- Some common image compression algorithms and formats are:
  - JPEG: a lossy compression standard for continuous-tone images, such as photographs. It uses a discrete cosine transform (DCT) to transform the image into frequency domain, and then quantizes and encodes the coefficients .
  - PNG: a lossless compression standard for images with large areas of uniform color, such as logos or diagrams. It uses a filter to predict the pixel values based on their neighbors, and then applies a deflate algorithm to compress the prediction errors .
  - GIF: a lossless compression standard for images with up to 256 colors, such as cartoons or animations. It uses a Lempel-Ziv-Welch (LZW) algorithm to encode the pixel values based on a dictionary of previously seen patterns .
  - TIFF: a flexible and versatile format that can support both lossless and lossy compression methods, such as LZW, JPEG, or ZIP. It is widely used for high-quality images, such as scanned documents or medical images .
  - WebP: a newer format that can support both lossless and lossy compression methods, and can achieve better compression ratios than JPEG or PNG. It uses a predictive coding scheme to encode the pixel values based on their context, and then applies a variable-length code to compress the residuals .



### The Graphics Interchange Format (GIF) for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- GIF is a graphical image format that uses a variant of LZW (Lempel-Ziv-Welch) lossless data compression technique to reduce the file size without degrading the visual quality .
- GIF was introduced by CompuServe in 1987 to provide a color image format for their file downloading areas .
- GIF supports up to 8 bits per pixel for each image, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space.
- GIF also supports animations and allows a separate palette of up to 256 colors for each frame. The color limitation makes the GIF format unsuitable for reproducing color photographs and other images with color gradients, but it is well-suited for simpler images such as graphics or logos with solid areas of color.
- GIF images are compressed using the LZW algorithm, which works by finding repeated sequences of pixels in the image and replacing them with shorter codes. The codes are stored in a code table, which is initialized with the basic colors of the image. As the algorithm scans the image, it adds new codes to the table for longer sequences of pixels that it encounters.
- The LZW algorithm can achieve high compression ratios for images with large areas of uniform color or repeated patterns, but it is less effective for images with more complex or random features. The compression ratio also depends on the number of colors in the image and the size of the code table.
- The LZW algorithm used in GIF was patented by Unisys in 1985, which led to a controversy over the licensing fees for software supporting GIF. This motivated the creation of the PNG (Portable Network Graphics) format in 1995, which uses a different lossless compression method and supports more features than GIF, such as transparency and true color. However, GIF remains popular for its simplicity and wide compatibility.



### Compression over Modems

- Compression over modems is a technique that allows modems to transmit data faster and more efficiently over phone lines by reducing the size of the data before sending it and expanding it after receiving it.
- Compression over modems can be done by using different algorithms and protocols that are agreed upon by both the sending and receiving modems. Some of the common protocols are:
  - V.42bis: This is an international standard for data compression over modems that was adopted by the CCITT in 1990. It can achieve up to 4:1 compression ratio and supports up to 2400 bps transmission speed.
  - MNP 5: This is a proprietary protocol developed by Microcom that can achieve up to 2:1 compression ratio and supports up to 9600 bps transmission speed.
  - STAC: This is a proprietary protocol developed by Stac Electronics that can achieve up to 4:1 compression ratio and supports up to 14400 bps transmission speed.
- Compression over modems can improve the throughput and reliability of data transmission, especially over poor quality phone lines that may introduce errors and noise. However, compression over modems also has some limitations and drawbacks, such as:
  - Compression over modems is not effective for data that is already compressed, such as images, audio, or video files. In fact, compressing such data may increase its size and reduce the transmission speed.
  - Compression over modems may introduce some delay and overhead in the data transmission, as the modems need to perform the compression and decompression operations and negotiate the protocols and parameters.
  - Compression over modems may not be compatible with some applications or devices that expect the data to be in a certain format or size. For example, some fax machines may not be able to handle compressed data.
- Compression over modems can be enhanced by using hardware-assisted compression devices that can perform the compression and decompression operations faster and more efficiently than the modems themselves. Some examples of such devices are:
  - CSA: This is a compression service adapter that can be installed in Cisco routers to provide high performance compression for Cisco IOS compression services. It can support up to 8 Mbps of compressed data throughput and can use various compression algorithms, such as LZS, MPPC, or Predictor.
  - Data Compression AIM: This is a data compression advanced integration module that can be installed in Cisco 2600 series routers to provide high performance compression for Cisco IOS compression services. It can support up to 8 Mbps of compressed data throughput and can use various compression algorithms, such as LZS, MPPC, or Predictor.



### V.42 bits

- V.42 bits are the bits used by the V.42bis standard for data compression in modems   .
- V.42bis is an adaptive data compression standard that can compress text about as well as the Lempel-Ziv-Welch (LZW) algorithm .
- V.42bis is based on the Lempel-Ziv dynamic dictionary approach, which encodes strings of symbols as codes that refer to previous occurrences of the same or similar strings.
- V.42bis uses a specific algorithm called BTLZ (British Telecom Lempel Ziv), which was developed by Alan Clark (then with BT).
- V.42bis can switch to transparent mode, in which data is transmitted uncompressed, when the compression ratio is low or the data is already compressed.
- V.42bis can achieve compression ratios of up to 4:1 for text and 2:1 for binary data .
- V.42bis is suitable for implementation on a contemporary modem with an 8-bit microprocessor, 40 Kbytes of RAM, 32 Kbytes of ROM, a 9.6 KBaud V.32 modem-modem connection, and a 19.2 KBaud EIA-232-D modem-terminal connection .
- V.42bis is compatible with the V.42 error correction standard and can be used with any modulation scheme that supports V.42  .
- V.42bis is widely used by more than 50 modem manufacturers and is spreading into Local and Remote Area Networks (LANs, WANs) .



### Predictive Coding

- Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits.
- The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding, Huffman coding, or Golomb coding.
- Predictive coding can achieve higher compression ratios than fixed-length codes, because the prediction error tends to have a lower entropy than the original data.
- Predictive coding can be applied to different types of data, such as text, audio, image, or video. Depending on the data, different models can be used to make predictions, such as Markov models, linear models, neural networks, or wavelets.
- Some examples of predictive coding algorithms are:
  - Dynamic Markov compression (DMC), which uses a Markov model to predict the next bit in a binary sequence .
  - Linear predictive coding (LPC), which uses a linear model to predict the next sample in an audio signal.
  - WebP, which uses a directional predictor to predict the next pixel in an image.
  - Compressed predictive information coding (CPIC), which uses a neural network to predict the next state in a dynamic system.



### Prediction with Partial Match (PPM) for Data Compression

- Prediction by Partial Match (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length context for each symbol, and using the longest matching context to assign a probability distribution for the next symbol .
- PPM uses a hierarchy of models, each corresponding to a different context length, and switches between them dynamically depending on the data .
- PPM can achieve high compression ratios, especially for natural language texts, but it is also computationally intensive and requires large amounts of memory .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression:

### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Coding a sequence is a technique of data compression that assigns codes to sequences of symbols or bytes, rather than individual ones.
- Coding a sequence can achieve better compression ratios than coding individual symbols, especially for data with repeated patterns or long runs of the same symbol.
- There are different algorithms for coding a sequence, such as LZW (Lempel–Ziv–Welch), SDC (Sequence Detection Code), FOST (First Occurrence Symbol Table), and Huffman coding.
- The general steps of coding a sequence are:

  1. Initialize a code table with the codes for the individual symbols or bytes in the data.
  2. Scan the data from left to right and gather input symbols or bytes into a sequence until the next symbol or byte would make a sequence with no code yet in the code table.
  3. Output the code for the current sequence (without the next symbol or byte) and add a new code for the extended sequence (with the next symbol or byte) to the code table.
  4. Repeat steps 2 and 3 until the end of the data is reached.
  5. Output the code for the final sequence.

- For example, using the LZW algorithm , the code table is initialized with the codes 0 to 255 for the ASCII characters. The data to be compressed is "ABABABA". The algorithm works as follows:

  1. The code table is initialized with 0 to 255 for the ASCII characters.
  2. The first input symbol is A. The sequence is A and it has a code in the code table, which is 65. The next symbol is B. The extended sequence is AB and it has no code in the code table.
  3. Output the code for A, which is 65, and add a new code for AB, which is 256, to the code table.
  4. The next input symbol is A. The sequence is B and it has a code in the code table, which is 66. The next symbol is B. The extended sequence is BB and it has no code in the code table.
  5. Output the code for B, which is 66, and add a new code for BB, which is 257, to the code table.
  6. The next input symbol is A. The sequence is A and it has a code in the code table, which is 65. The next symbol is B. The extended sequence is AB and it has a code in the code table, which is 256.
  7. Output the code for AB, which is 256, and add a new code for ABA, which is 258, to the code table.
  8. The next input symbol is A. The sequence is B and it has a code in the code table, which is 66. The next symbol is the end of the data.
  9. Output the code for B, which is 66, and add a new code for BA, which is 259, to the code table.
  10. Output the code for the final sequence, which is A, which is 65.

- The compressed output is 65, 66, 256, 66, 65. The compression ratio is 5/7, which is 71.4%. The original data has 7 bytes and the compressed data has 5 bytes. Each byte has 8 bits, so the original data has 56 bits and the compressed data has 40 bits. The bit reduction is 16 bits, which is 28.6%.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of the escape symbol for the notes of the unit 3 - coding a sequence in the subject of data compression.

### The ESCAPE SYMBOL

- The escape symbol is a special symbol that is used to indicate that a code is not part of the original alphabet of a sequence.
- The escape symbol is usually chosen to be a symbol that does not occur in the original sequence, or that occurs very rarely.
- The escape symbol is useful for coding sequences that have unknown or variable alphabets, or that contain symbols that are not in the predefined codebook.
- The escape symbol allows the encoder to send new symbols to the decoder, without having to update the codebook or send the whole alphabet.
- The escape symbol also allows the encoder to adapt to the changing statistics of the sequence, by sending symbols that have low probabilities or frequencies with the escape symbol, and using shorter codes for symbols that have high probabilities or frequencies.
- The escape symbol can be used with different coding methods, such as Huffman coding, arithmetic coding, or Lempel-Ziv coding.
- The escape symbol can improve the compression ratio and the efficiency of the coding, but it also introduces some overhead and complexity, as the encoder and the decoder have to agree on the escape symbol and its code, and handle the cases when the escape symbol is encountered in the sequence.



### Length of context for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The length of context is the number of previous symbols that are used to determine the probability distribution for the next symbol in a sequence.
- The length of context affects the performance of the compression algorithm, as it determines how well the algorithm can adapt to the statistical properties of the data.
- A longer context can capture more patterns and correlations in the data, leading to higher compression ratios, but it also requires more memory and computation to store and update the probability distributions.
- A shorter context can reduce the memory and computation requirements, but it may also miss some patterns and correlations in the data, leading to lower compression ratios.
- The optimal length of context depends on the characteristics of the data and the trade-off between compression ratio and complexity.
- Some compression algorithms, such as adaptive arithmetic coding, can adjust the length of context dynamically based on the data, while others, such as Huffman coding, use a fixed length of context.



### The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by using various techniques that exploit the redundancy or patterns in the data.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not after decompression.
- Coding a sequence is one of the methods of lossless data compression, where a sequence of symbols (such as characters or bytes) is encoded using a shorter sequence of bits.
- The exclusion principle is a technique used in some coding algorithms, such as PPM (Prediction by Partial Matching), to improve the compression ratio by excluding some symbols from the probability computation.
- The exclusion principle works as follows:
  - The unit interval [0, 1) is divided into subintervals, each of which represents a symbol in the alphabet.
  - The size of each subinterval is proportional to the probability of the symbol in the current context, which is determined by the previous symbols in the sequence.
  - The subinterval corresponding to the encoded symbol is further divided into smaller subintervals for the next symbol, and so on, until the end of the sequence is reached.
  - The exclusion principle applies when a symbol is not present in the current context, meaning that it has zero probability. In that case, the subinterval for that symbol is excluded from the division, and the remaining subintervals are scaled up to fill the gap.
  - This way, the exclusion principle avoids wasting bits on symbols that are impossible to occur, and increases the compression ratio by assigning more bits to the symbols that are more likely to occur.



### The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is an algorithm used to prepare data for use with data compression techniques such as bzip2 .
- The BWT rearranges a character string into runs of similar characters, which makes it easier to compress by techniques such as move-to-front transform and run-length encoding .
- The BWT is reversible, meaning that the original string can be recovered from the transformed string without any loss of information  .
- The BWT is based on a lexicographical sorting of all the cyclic rotations of the original string, and appending a special symbol ($) to mark the end of the string  .
- The BWT of a string T is obtained by taking the last column of the sorted matrix of rotations, and the index of the original string in the matrix is called the primary index  .
- For example, the BWT of the string "banana" is computed as follows:

| Original string | Sorted rotations | BWT |
| --------------- | ---------------- | --- |
| banana$         | $banana          | a   |
| anana$b         | a$banan          | n   |
| nana$ba         | ana$ban          | a   |
| ana$ban         | anana$b          | b   |
| na$bana         | banana$          | $   |
| a$banan         | nana$ba          | a   |

- The BWT of "banana" is "annb$aa", and the primary index is 3, which is the position of "banana$" in the sorted matrix.
- The inverse BWT can be performed by using the first and last columns of the sorted matrix, and following the last-to-first mapping that links each character in the last column to its first occurrence in the first column.
- For example, the inverse BWT of "annb$aa" is computed as follows:

| First column | Last column | Last-to-first mapping |
| ------------ | ----------- | --------------------- |
| $            | a           | 0 -> 3                |
| a            | n           | 1 -> 4                |
| a            | n           | 2 -> 5                |
| a            | b           | 3 -> 6                |
| b            | $           | 4 -> 0                |
| n            | a           | 5 -> 1                |
| n            | a           | 6 -> 2                |

- Starting from the primary index 3, we follow the last-to-first mapping until we reach the end symbol $, and we get the original string "banana" by reading the characters in the last column.



### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but prepares it for better compression by entropy encoding techniques  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is updated dynamically as the input data is processed  .
- The list is initialized with all possible symbols in some order (such as alphabetical or numerical). For each input symbol, the output is the index of that symbol in the list, and then the symbol is moved to the front of the list  .
- The output is a sequence of numbers that represent the positions of the input symbols in the list. The numbers are usually smaller for more frequent symbols, which makes them more suitable for entropy encoding  .
- Movetofront coding is reversible, meaning that the original input can be recovered from the output and the list. The decoding algorithm is the same as the encoding algorithm, except that the output symbols are used to look up the input symbols in the list, and then the input symbols are moved to the front of the list  .
- Movetofront coding is often used as a preprocessing step in data compression algorithms, such as Burrows–Wheeler transform and arithmetic coding, to exploit the locality and redundancy of the input data .
- Movetofront coding is fast and simple to implement, and can improve the compression ratio and speed of entropy encoding techniques  .



### CALIC

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a technique for compressing continuous-tone images without any loss of quality or information  .
- It achieves high coding efficiency with relatively low time and space complexities  .
- It can also be applied to compress compound video data, which consists of both text and graphics.
- The main components of CALIC are  :
  - A **non-linear predictor** that estimates the pixel value based on its neighboring pixels and their contexts.
  - A **context modeler** that assigns a probability distribution to the prediction error based on the local image features and the previous errors.
  - A **binary arithmetic coder** that encodes the prediction error using the probability distribution from the context modeler.
- The non-linear predictor and the context modeler are adaptive, meaning they adjust their parameters according to the image data and the prediction errors  .
- The non-linear predictor uses a **gradient-adjusted prediction (GAP)** scheme, which considers the gradients of the neighboring pixels to improve the accuracy of the prediction  .
- The context modeler uses a **large number of modeling contexts** to capture the local image features and the error feedback mechanism  .
- The binary arithmetic coder uses a **binary tree structure** to encode the prediction error in a bit-by-bit fashion, starting from the most significant bit  .
- The coding sequence of CALIC is as follows  :
  - For each pixel in the image, apply the non-linear predictor to obtain the predicted value and the prediction error.
  - For each prediction error, apply the context modeler to obtain the probability distribution and the modeling context.
  - For each prediction error, apply the binary arithmetic coder to obtain the encoded bits using the probability distribution and the modeling context.
  - Concatenate the encoded bits to form the compressed bitstream.



### JPEG-LS

- JPEG-LS is a **lossless/near-lossless compression standard** for continuous-tone images .
- It is based on the **LOCO-I algorithm** (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.
- It consists of two independent and distinct stages called **modeling and encoding**.
- Modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error.
- Encoding stage compresses the prediction error using a **context-based adaptive arithmetic coder**.
- JPEG-LS supports **lossless, near-lossless and lossy modes** of compression .
- Lossless mode preserves the exact pixel values of the original image.
- Near-lossless mode allows a small amount of distortion (controlled by a parameter) to achieve higher compression ratios.
- Lossy mode uses a **quantization step** to reduce the number of prediction errors before encoding.
- JPEG-LS is a **low-complexity algorithm** that matches JPEG 2000 compression ratios .
- It is suitable for applications that require high-quality images with low processing power and memory requirements .



### Multi-resolution Approaches

- Multi-resolution approaches are techniques that allow data to be represented and processed at different levels of detail or resolution, depending on the needs and capabilities of the application or the user .
- Multi-resolution approaches can be useful for data compression, which is the process of reducing the amount of data required to store or transmit information, while preserving its quality and usefulness  .
- Multi-resolution approaches can be applied to different types of data, such as images, videos, audio, vector data, or fluid dynamics simulations   .
- Multi-resolution approaches can be based on different mathematical tools, such as wavelets, fractals, or adaptive mesh refinement   .
- Multi-resolution approaches can have different advantages and challenges, such as:
  - Improving performance, by capturing long-range phenomena that would otherwise not be utilized.
  - Reducing computational complexity, by allowing algorithms to work on both fine and coarse scales, rather than waiting for local pixel-level operations to converge at large scales.
  - Improving compression efficiency, by exploiting the self-similarity and redundancy of data at different scales .
  - Reducing the characteristic distortions of conventional compression algorithms, such as blocking artifacts and image blurring, by better coding of high frequencies.
  - Taking visual lossless distance on screen display as accuracy requirement for vector data compression.
  - Handling the challenges of multi-phase flows, such as sharp interfaces, shocks, and contact discontinuities, by using a sharp interface model and an adaptive strategy .



### Facsimile Encoding

- Facsimile encoding is a technique for compressing binary images, such as scanned documents, maps, or photographs, that consist of black and white pixels.
- Facsimile encoding is based on the observation that most binary images have large regions of uniform color, and the transitions between black and white pixels occur along horizontal lines.
- Facsimile encoding exploits this redundancy by encoding the lengths of consecutive runs of black or white pixels, rather than the individual pixel values.
- Facsimile encoding can be classified into two types: one-dimensional and two-dimensional.
- One-dimensional facsimile encoding, also known as run-length encoding, encodes each row of pixels independently, by alternating the run lengths of black and white pixels, starting from a fixed color (usually white).
- Two-dimensional facsimile encoding, also known as differential encoding, encodes each row of pixels relative to the previous row, by using a reference line and a coding line, and encoding the differences between them.
- Two-dimensional facsimile encoding can achieve higher compression ratios than one-dimensional facsimile encoding, by exploiting the correlation between adjacent rows of pixels.
- Two-dimensional facsimile encoding can be further divided into two modes: line-by-line and block-by-block.
- Line-by-line mode encodes each row of pixels as a sequence of codes that indicate the horizontal displacement of the coding line from the reference line, and the color of the next pixel.
- Block-by-block mode encodes each block of pixels as a two-dimensional array of codes that indicate the vertical and horizontal displacement of the coding line from the reference line, and the color of the next pixel.
- Facsimile encoding can use different coding schemes to represent the run lengths or the displacements, such as Huffman coding, arithmetic coding, or Golomb-Rice coding.
- Facsimile encoding is widely used in fax machines, document scanners, and image compression standards, such as CCITT Group 3 and 4, JBIG, and TIFF.



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1 .
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input .
- Each node stores a count of how many times each bit has occurred in that context, which is used to estimate the probability of the next bit .
- The arithmetic coder uses these probabilities to encode the input bits with variable-length codes, where more probable bits are assigned shorter codes and less probable bits are assigned longer codes .
- The model is updated after each bit is encoded, by incrementing the corresponding count in the current node and creating a new node if necessary .
- The model is also pruned periodically to remove nodes with low counts, to avoid overfitting and reduce memory usage .
- DMC is an adaptive algorithm, which means that it does not require any prior knowledge of the input data and can adjust to changes in the data distribution .
- DMC can achieve high compression ratios for various types of data, especially those with long-range dependencies or repetitive patterns .
- DMC is also relatively simple and fast, compared to other adaptive algorithms like PPM .



## Unit 4 - Distortion criteria

- Distortion is the alteration of the original shape or other characteristic of a signal in a communication system.
- Distortion can degrade the quality and intelligibility of the transmitted or received information, such as sound, images, or data .
- Distortion can be caused by various factors, such as noise, interference, nonlinearity, bandwidth limitations, or filtering.
- Distortion can be classified into different types, such as amplitude, frequency, phase, harmonic, intermodulation, or cross-modulation distortion .
- Distortion criteria are the measures or standards used to evaluate the performance of a communication system in terms of distortion.
- Distortion criteria can be based on different aspects, such as signal-to-noise ratio, signal-to-distortion ratio, total harmonic distortion, intermodulation distortion, or error vector magnitude .
- Distortion criteria can be used to design, optimize, or test communication systems, such as amplifiers, modulators, demodulators, filters, or antennas .
- Distortion criteria can also be used to compare different communication systems or techniques, such as analog or digital, linear or nonlinear, or coherent or noncoherent .



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Distortion criteria are used to measure the quality of the approximation of the original data by the compressed data.
- Distortion criteria depend on the type and application of the data, such as images, audio, video, text, etc.
- Distortion criteria can be classified into two categories: objective and subjective.
- Objective distortion criteria are based on mathematical formulas that compare the original and reconstructed data, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc.
- Subjective distortion criteria are based on human perception and evaluation of the quality of the approximation, such as mean opinion score (MOS), just noticeable difference (JND), etc.
- Distortion criteria are used to define the rate-distortion function, which is the minimum achievable compression rate for a given distortion level.
- Rate-distortion theory is the branch of information theory that studies the fundamental limits and trade-offs of data compression problems.
- Rate-distortion function can be calculated by using an iterative algorithm called the Blahut-Arimoto algorithm, which involves finding the optimal probability distributions that minimize the expected distortion.
- Rate-distortion function can also be derived by using the Lagrange multiplier method, which involves finding the optimal codebook that minimizes the weighted sum of the expected distortion and the expected code length.
- Rate-distortion function can be used to evaluate the performance of practical compression systems, such as JPEG, MP3, H.264, etc. The closer the compression system is to the rate-distortion bound, the better it performs.



### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the number of bits required to represent a signal by discarding some information.
- Scalar quantization can be performed by dividing the range of the signal into intervals, called quantization cells or bins, and assigning a quantization level to each cell .
- The quantization function Q(⋅) maps each input value x to the quantization level Q(x) that corresponds to the cell that contains x.
- The quantization error e(x) is the difference between the input value x and the quantization level Q(x), and it represents the amount of information lost due to quantization .
- The quantization error can be measured by various distortion criteria, such as mean squared error (MSE), signal-to-noise ratio (SNR), peak signal-to-noise ratio (PSNR), or perceptual quality .
- The goal of scalar quantization is to minimize the quantization error for a given number of bits per sample, or equivalently, to maximize the compression ratio for a given distortion level .
- Scalar quantization can be classified into two types: uniform and nonuniform .
  - Uniform scalar quantization uses equal-sized cells and equally spaced quantization levels, and it is suitable for signals that have a uniform distribution .
  - Nonuniform scalar quantization uses variable-sized cells and unequally spaced quantization levels, and it is suitable for signals that have a nonuniform distribution, such as Laplacian or Gaussian .
- Scalar quantization can be further improved by using techniques such as companding, entropy coding, or adaptive quantization .
- Scalar quantization is widely used in various applications, such as speech and audio coding, image and video compression, and fingerprint recognition .



### The Quantization Problem

- Quantization is a process of mapping a large set of input values to a smaller set of output values, with a controlled amount of distortion or error.
- Quantization is a key technique for lossy data compression, as it reduces the number of bits needed to represent the data.
- The quantization problem is to find the optimal way of quantizing a given source, such that the distortion is minimized for a given bit rate, or the bit rate is minimized for a given distortion.
- The quantization problem can be formulated as an optimization problem, where the objective function is the distortion-rate function, which measures the trade-off between the distortion and the bit rate of the quantizer.
- The quantization problem can be solved in different ways, depending on the type and structure of the quantizer, the source statistics, and the distortion measure.
- Some of the common types of quantizers are:
  - Uniform quantizer: the input range is divided into equal-sized intervals, and each interval is mapped to a fixed output value.
  - Non-uniform quantizer: the input range is divided into variable-sized intervals, and each interval is mapped to a fixed output value. The intervals are usually designed to match the source probability density function, such that the more probable values have smaller intervals and lower distortion.
  - Scalar quantizer: the input and output values are scalars, i.e., one-dimensional numbers.
  - Vector quantizer: the input and output values are vectors, i.e., multi-dimensional numbers. The vector quantizer can exploit the correlation among the vector components and achieve higher compression efficiency.
- Some of the common methods of designing quantizers are:
  - Lloyd algorithm: an iterative algorithm that finds the optimal set of output values (also called codebook or representatives) for a given set of input values (also called training set or samples), based on the minimum mean squared error (MMSE) criterion.
  - Zador algorithm: an extension of the Lloyd algorithm that finds the optimal set of output values and the optimal partition of the input range for a given source probability density function, based on the MMSE criterion.
  - K-means algorithm: a clustering algorithm that partitions the input values into K groups, such that each group is assigned to the output value that is the centroid (mean) of the group.
  - LBG algorithm: an extension of the K-means algorithm that finds the optimal codebook size and the optimal codebook for a given distortion level, using a splitting and merging technique.
- Some of the common distortion measures are:
  - Mean squared error (MSE): the average of the squared difference between the input and output values.
  - Signal-to-noise ratio (SNR): the ratio of the average power of the input signal to the average power of the quantization error.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible power of the input signal to the average power of the quantization error, usually expressed in decibels (dB).
  - Mean absolute error (MAE): the average of the absolute difference between the input and output values.
  - Mean absolute percentage error (MAPE): the average of the absolute difference between the input and output values, divided by the input value, expressed as a percentage.
- Some of the common applications of quantization are:
  - Image compression: quantization is used to reduce the number of bits needed to represent the pixel values of an image, such as in JPEG and PNG formats.
  - Audio compression: quantization is used to reduce the number of bits needed to represent the sample values of an audio signal, such as in MP3 and AAC formats.
  - Speech compression: quantization is used to reduce the number of bits needed to represent the parameters of a speech model, such as in G.711 and G.729 formats.
  - Video compression: quantization is used to reduce the number of bits needed to represent the motion vectors and the transform coefficients of a video sequence, such as in MPEG and H.264 formats.



### Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels .
- The quantization error of a uniform quantizer is the difference between the input value and the nearest output level .
- The quantization error can be reduced by increasing the number of output levels or decreasing the step size, but this also increases the bit rate of the quantized signal .
- The distortion of a uniform quantizer can be measured by the mean squared error (MSE) or the signal-to-quantization-noise ratio (SQNR), which are functions of the step size and the input signal statistics  .
- A uniform quantizer can be optimized for a given input signal by choosing the step size that minimizes the distortion or maximizes the SQNR  .
- A uniform quantizer can be combined with an entropy encoder to achieve lossy data compression, where the output levels are assigned variable-length codes based on their probabilities  .
- A uniform quantizer can also be modified by a companding function that compresses the input range before quantization and expands it after quantization, which can improve the performance for signals with non-uniform distributions .
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model, where different approximations of the uniform quantization can affect the quality and efficiency of the compression .



### Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input data. 
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters. 
- An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution. 
- Adaptive quantization can be classified into two categories: forward adaptive quantization and backward adaptive quantization. 
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information. 
- In backward adaptive quantization, the quantizer parameters are updated based on the previous quantized samples. The receiver can reconstruct the parameters using the same update rule. 
- Adaptive quantization can be applied to different types of data, such as images, audio, video, and synthetic aperture radar (SAR) raw data.   
- Adaptive quantization can improve the compression performance and the quality of the reconstructed data by reducing the quantization error and the distortion.



### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal spacing between the output values.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, because it can allocate more bits to the regions where the input values are more concentrated and less bits to the regions where the input values are less frequent.
- Non uniform quantization can be implemented in different ways, such as using a non-linear function to map the input values to the output values, or using an adaptive algorithm to adjust the output values based on the input statistics or the network gradients .
- Non uniform quantization can be classified into two types: companding and pdf-optimized.
  - Companding is a method of applying a non-linear function to the input values before applying uniform quantization, and then applying the inverse function to the output values after quantization. The non-linear function can be logarithmic, such as the μ-law or A-law used in telephony, or power-law, such as the PCM used in audio coding.
  - Pdf-optimized is a method of designing the output values to minimize the distortion for a given input probability density function (pdf). The output values can be obtained by solving the Lloyd-Max algorithm, which iteratively updates the output values and the decision boundaries until convergence.



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Quantization is the process of mapping input values from a large set (often a continuous set) to output values in a (countable) smaller set, often with a finite number of elements.
- Scalar quantization is a type of quantization where each input symbol is treated separately in producing the output.
- Vector quantization is a type of quantization where the input symbols are clubbed together in groups called vectors, and processed to give the output.
- Some of the advantages of vector quantization over scalar quantization are:

  - Vector quantization can remove auto-correlation in the encoded signal and therefore, is more efficient in rate-distortion terms than scalar quantization.
  - Vector quantization can exploit the inter-symbol dependencies and reduce the redundancy in the input data.
  - Vector quantization can achieve higher compression ratios and lower distortion than scalar quantization for the same bit rate.
  - Vector quantization can adapt to the statistics of the input data and optimize the codebook according to the source distribution.
  - Vector quantization can handle multidimensional data and complex signals better than scalar quantization.



### The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in a given data set.
- Vector quantization is a technique to compress data by reducing the number of bits required to represent each vector.
- The LBG algorithm is similar to the k-means method in data clustering .
- The LBG algorithm works as follows :
  - Start with an initial codebook of size one, which is the centroid of the training set.
  - Split each codeword into two slightly perturbed versions, doubling the size of the codebook.
  - Assign each vector in the training set to the nearest codeword, forming clusters around each codeword.
  - Update each codeword by computing the centroid of its cluster, minimizing the distortion within each cluster.
  - Repeat the previous two steps until the distortion falls below a threshold or the codebook reaches the desired size.

### Advantages of Vector Quantization over Scalar Quantization

- Scalar quantization is a technique to compress data by reducing the number of bits required to represent each scalar value.
- Vector quantization has some advantages over scalar quantization, such as:
  - Higher compression ratio: Vector quantization can exploit the correlation among the components of a vector, while scalar quantization treats each component independently.
  - Lower distortion: Vector quantization can better preserve the quality of the original data, while scalar quantization introduces more quantization error.
  - More flexibility: Vector quantization can adapt to different types of data, such as images, speech, or video, while scalar quantization is limited by the range and resolution of the scalar values.



### Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each of which is represented by a code vector. The hierarchy can be represented by a binary tree, where each node corresponds to a region and a code vector.
- The advantage of using a tree structure is that it provides fast quantization search through a root-to-leaf path. The encoder only needs to compare the input vector with the code vectors at each level of the tree, and choose the branch that minimizes the distortion.
- Another advantage of TSVQ is that it can adapt to the local statistics of the input space by allocating more code vectors to the regions with higher density or variance. This can improve the performance of the quantizer in terms of distortion or rate.
- TSVQ can be designed by using a top-down or a bottom-up approach. The top-down approach starts with the average of all the training vectors, and splits each region into two subregions by perturbing the code vector. The bottom-up approach starts with a large number of small regions, and merges them into larger regions by minimizing the distortion.
- TSVQ can be optimized by using different cost functions, such as storage cost, encoding rate, or quantization time. The optimal tree structure depends on the trade-off between these factors.
- TSVQ can be applied to various applications, such as image compression, speech coding, pattern recognition, and data clustering .



### Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity and the storage requirements of the quantization process .
- Structured vector quantizers can be classified into two main types: tree-structured vector quantizers (TSVQ) and lattice vector quantizers (LVQ).
- TSVQ use a hierarchical tree structure to partition the input space, such that each node of the tree corresponds to a subregion and a codeword. The encoding and decoding algorithms are based on a root-to-leaf traversal of the tree, which reduces the search complexity from linear to logarithmic in the codebook size .
- LVQ use a regular lattice structure to generate the codewords, such that each codeword is a linear combination of some basis vectors. The encoding and decoding algorithms are based on simple arithmetic operations, which eliminates the need for storing and searching a codebook .
- Structured vector quantizers have some advantages over scalar quantizers and unstructured vector quantizers, such as:
  - They can achieve better rate-distortion performance by exploiting the correlation and the structure of the input vectors .
  - They can reduce the memory and computational requirements of the quantization process by using efficient encoding and decoding algorithms .
  - They can provide fast and adaptive quantization by adjusting the tree or the lattice structure according to the input statistics or the channel conditions .

