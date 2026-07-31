

## Unit 1 - Compression Techniques

- Compression is the process of reducing the size of a file or a data stream by removing redundant or irrelevant information.
- Compression can be classified into two types: lossless and lossy.
- Lossless compression preserves the original data exactly, while lossy compression discards some information that is deemed less important or perceptible.
- Lossless compression is suitable for text, documents, or executable files, where any alteration can affect the meaning or functionality of the data.
- Lossy compression is suitable for images, audio, or video, where some degradation in quality can be tolerated or unnoticed by human senses.
- Some common lossless compression algorithms are Huffman coding, run-length encoding, Lempel-Ziv-Welch (LZW), and arithmetic coding.
- Some common lossy compression algorithms are JPEG, MPEG, MP3, and AAC.
- The performance of a compression algorithm can be measured by the compression ratio, which is the ratio of the original size to the compressed size, and the bit rate, which is the number of bits per second required to transmit or store the compressed data.



### Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values are more frequent than others and can be represented with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and lossless audio formats .
- Lossless compression can reduce file sizes without sacrificing any significant information or quality, which can save storage space, bandwidth, and transmission time.
- Lossless compression algorithms typically use techniques such as entropy encoding, dictionary encoding, run-length encoding, and predictive encoding to exploit the redundancy in the data and achieve compression ratios.
- Some examples of lossless compression formats are ZIP, GZIP, BZIP2, PNG, FLAC, and ALAC.



### Lossy Compression

- Lossy compression is a data compression method that sacrifices some information to achieve an even smaller file size than lossless compression.
- Lossy compression is often used on video, audio, and many types of image files, where some loss of quality is acceptable.
- Lossy compression works by using inexact approximations and partial data discarding to represent the content, reducing the amount of bits needed to store or transmit the data.
- Lossy compression can achieve high compression ratios, but at the cost of losing data permanently and degrading the quality of the original data.
- Lossy compression examples include JPEG, MP3, MPEG, and GIF formats.
- Lossy compression can be contrasted with lossless compression, which preserves the original data exactly and can be decompressed back to the original form.
- Lossy compression can be useful for applications that do not require high fidelity or accuracy, such as streaming media, web browsing, or online gaming.
- Lossy compression can also be combined with lossless compression to achieve a trade-off between file size and quality, such as using JPEG for the image and ZIP for the text in a document.



### Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or transforming the data into a more compact representation.
- The performance of compression techniques can be measured by various metrics that reflect the trade-off between compression ratio, quality, complexity, and speed.
- Some of the common metrics are:

  - Compression ratio (CR): The ratio of the original data size to the compressed data size. Higher CR means more compression and less storage space required.
  - Bit rate (BR) or bits per symbol (bps): The average number of bits used to represent each symbol (character, pixel, etc.) in the compressed data. Lower BR or bps means more compression and less bandwidth required.
  - Distortion or error: The difference between the original data and the reconstructed data after compression and decompression. Distortion can be measured by various methods, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc. Lower distortion means higher quality and fidelity of the data.
  - Complexity: The amount of computation or memory required to perform compression and decompression. Complexity can be measured by various methods, such as time complexity, space complexity, algorithmic complexity, etc. Lower complexity means faster and simpler implementation of the compression technique.
  - Accuracy: The degree to which the compressed data preserves the essential information or features of the original data. Accuracy can be measured by various methods, such as information loss, entropy, mutual information, etc. Higher accuracy means more effective and useful compression of the data.



### Modeling and coding for data compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be divided into two levels: modeling and coding .
- Modeling is the process of analyzing the data and finding patterns, redundancies, or correlations that can be used to represent the data more efficiently.
- Coding is the process of encoding the data using a set of symbols or codes that can be decoded by the receiver.
- There are two types of data compression: lossless and lossy.
- Lossless data compression preserves the exact information of the original data and allows perfect reconstruction after decompression.
- Lossy data compression discards some information of the original data and allows only approximate reconstruction after decompression.
- Lossless data compression is generally implemented using one of two different types of modeling: statistical or dictionary-based.
- Statistical modeling reads in and encodes a single symbol at a time using the probability of that character’s appearance. Examples of statistical modeling are Huffman coding, arithmetic coding, and Golomb coding.
- Dictionary-based modeling uses a single code to replace strings of symbols that are stored in a dictionary. Examples of dictionary-based modeling are Lempel-Ziv (LZ) coding, Lempel-Ziv-Welch (LZW) coding, and Burrows-Wheeler transform (BWT) coding.
- Lossy data compression is generally implemented using transform-based modeling, which converts the data into a different domain that allows better compression of the relevant information. Examples of transform-based modeling are discrete cosine transform (DCT), wavelet transform, and Fourier transform.
- A recent approach to data compression is based on deep learning, which uses neural networks to learn the optimal representation of the data and the optimal coding scheme. An example of deep learning-based compression is Bit-Swap, which uses latent variable models and bits-back coding.



### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data.
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of information or uncertainty in a data source. The lower the entropy, the more predictable and compressible the data is.
- Entropy can be calculated using different models, such as the zero-order model, the first-order model, the k-th order model, and the Markov model. These models capture the statistical properties and dependencies of the data symbols.
- The entropy of a data source is the lower bound for the average number of bits per symbol needed to encode the data. No lossless compression scheme can achieve a compression ratio lower than the entropy of the data source.
- The compression ratio is the ratio of the size of the compressed data to the size of the original data. The higher the compression ratio, the more efficient the compression scheme is.
- The compression efficiency is the ratio of the entropy of the data source to the average number of bits per symbol used by the compression scheme. The higher the compression efficiency, the closer the compression scheme is to the optimal encoding.
- Some common lossless compression techniques are Huffman coding, arithmetic coding, run-length encoding, dictionary-based encoding, and Lempel-Ziv encoding. These techniques use different methods to assign variable-length codes to the data symbols based on their probabilities or frequencies.



### A brief introduction to information theory

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding theorems  .
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be stored or transmitted.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared between two random variables.
- Information theory also studies the fundamental limits and trade-offs of communication systems, such as channel capacity, which is the maximum rate of information that can be reliably transmitted over a noisy channel, or source coding, which is the process of compressing data to reduce its redundancy and size  .
- Information theory has many applications in various fields, such as cryptography, data compression, error correction, signal processing, machine learning, and neuroscience   .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on the models for compression techniques in data compression.

### Models for Compression Techniques

- Data compression is the process of reducing the size of data without losing too much information or quality.
- Data compression can be useful for saving storage space, bandwidth, and computational resources.
- There are different models for compression techniques, depending on the type of data, the level of compression, and the trade-off between speed and accuracy.
- Some of the common models for compression techniques are:

  - **Pruning**: This technique removes redundant or unimportant parameters from a neural network, such as weights, connections, neurons, channels, or layers. Pruning can reduce the size and complexity of the network, while maintaining or improving its performance. Pruning can be done in different ways, such as magnitude-based pruning, sparsity-based pruning, or structured pruning  .
  - **Quantization**: This technique reduces the number of bits required to represent the parameters or activations of a neural network, such as weights, biases, or outputs. Quantization can reduce the memory and computational requirements of the network, while minimizing the loss of accuracy. Quantization can be done in different ways, such as uniform quantization, non-uniform quantization, or mixed-precision quantization   .
  - **Knowledge Distillation**: This technique transfers the knowledge from a large and complex teacher network to a smaller and simpler student network, by mimicking the outputs or intermediate representations of the teacher network. Knowledge distillation can reduce the size and complexity of the network, while preserving or enhancing its performance. Knowledge distillation can be done in different ways, such as output distillation, feature distillation, or attention distillation  .
  - **Low-Rank Factorization**: This technique approximates a large and dense matrix (such as a weight matrix or a convolutional filter bank) by a product of two or more smaller and sparse matrices, which have a lower rank than the original matrix. Low-rank factorization can reduce the size and complexity of the network, while maintaining or improving its performance. Low-rank factorization can be done in different ways, such as singular value decomposition, tensor decomposition, or matrix factorization .

- These models for compression techniques can be applied individually or in combination, depending on the data and the desired outcome.
- These models for compression techniques can be evaluated by different metrics, such as compression ratio, accuracy, speed, or energy efficiency.



### Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Uniform model**: This model assumes that all the symbols in the source data have equal probability of occurrence. This model is suitable for data that is random or has no apparent structure. The uniform model can be used to calculate the entropy of the source data, which is the lower bound on the compression ratio. The entropy of a uniform source of size N is log2(N) bits per symbol.

- **Markov model**: This model assumes that the probability of the next symbol in the source data depends only on the previous K symbols, where K is a fixed parameter. This model is useful for data that has some temporal or spatial correlation, such as text or images. The Markov model can be used to estimate the conditional entropy of the source data, which is the average number of bits needed to encode a symbol given its context. The conditional entropy of a Kth order Markov source is H(X|XK), where X is the symbol and XK is the context .

- **Dictionary model**: This model assumes that the source data can be decomposed into a sequence of words, where each word is a substring of the data that has some meaning or significance. This model is effective for data that has some repetition or common patterns, such as natural language or DNA sequences. The dictionary model can be used to construct a codebook that maps each word to a codeword, which is a binary string of fixed or variable length. The codebook can be static or dynamic, depending on whether it is predefined or updated during the compression process.

- **Transform model**: This model assumes that the source data can be transformed into a different domain, where the data has some desirable properties, such as sparsity, decorrelation, or frequency distribution. This model is applicable for data that has some inherent structure or regularity, such as audio or video signals. The transform model can be used to apply a linear or nonlinear transformation to the data, such as discrete Fourier transform, discrete cosine transform, or wavelet transform. The transformed data can then be quantized and encoded using other models, such as uniform or dictionary models .



### Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to the possible symbols or sequences of symbols that can be generated by the source.
- A probability model can be used to measure the information content of the data, and to design efficient compression algorithms that exploit the statistical properties of the data.
- There are different types of probability models, such as:
  - Uniform model: This model assumes that all symbols have the same probability of occurrence, and is suitable for sources that generate random or unpredictable data.
  - Bernoulli model: This model assumes that the source generates binary symbols (0 or 1) with a fixed probability p for 1 and 1-p for 0, and is suitable for sources that generate independent and identically distributed (i.i.d.) binary data.
  - Geometric model: This model assumes that the source generates binary symbols with a probability p for 1 and 1-p for 0, but the probability of 1 decreases exponentially with the number of consecutive 0s, and is suitable for sources that generate sparse binary data.
  - Poisson model: This model assumes that the source generates non-negative integer symbols with a probability that follows the Poisson distribution, and is suitable for sources that generate rare events or counts.
  - Markov model: This model assumes that the source generates symbols from an alphabet A with a probability that depends on the previous n symbols, where n is the order of the model, and is suitable for sources that generate correlated or sequential data, such as text or speech.
  - Context-based model: This model assumes that the source generates symbols from an alphabet A with a probability that depends on the context of the symbol, which can be defined by various factors, such as the position, the surrounding symbols, the image features, etc., and is suitable for sources that generate complex or structured data, such as images or video.



### Markov models for data compression

- Markov models are mathematical models that describe the probability of a system transitioning from one state to another, based on the current state and the previous states.
- Markov models can be used to model the statistical properties of natural language, images, audio, and other types of data, and to predict the next symbol or bit in a sequence.
- Markov models can be used for data compression by encoding the data using an arithmetic coder, which assigns shorter codes to more probable symbols or bits, and longer codes to less probable ones.
- Markov models can be classified into different types, depending on the order of the model (how many previous states are considered), the structure of the model (how the states are connected), and the adaptivity of the model (how the model changes over time).
- Some examples of Markov models for data compression are:

  - Dynamic Markov compression (DMC): a lossless data compression algorithm that uses a variable-order Markov model that adapts to the data as it is processed. It predicts one bit at a time and encodes it using an arithmetic coder  .
  - Prediction by partial matching (PPM): a lossless data compression algorithm that uses a variable-order Markov model that predicts one byte at a time and encodes it using an arithmetic coder. It uses a context tree to store the probabilities of different symbols given different contexts.
  - Burrows-Wheeler transform (BWT): a reversible transformation that reorders the symbols in a block of data based on their lexicographic order. It tends to group similar symbols together, which makes them easier to compress using a Markov model or a run-length encoding scheme.
  - Context-based adaptive lossless image coding (CALIC): a lossless image compression algorithm that uses a high-order Markov model to predict the pixel values based on the neighboring pixels and the previous scan lines. It encodes the prediction errors using an arithmetic coder.



### Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub>.
- A composite source model is useful for data compression when a single model is not adequate to capture the characteristics of the data.
- A composite source model can be used to describe some very complicated processes, such as image signals, natural language, or multimedia data .
- A composite source model can be encoded using different coding techniques, such as Huffman coding, arithmetic coding, or dictionary-based coding, depending on the nature of the component sources.
- A composite source model can achieve better compression ratios than a single source model, as it can exploit the redundancy and correlation among the component sources.
- A composite source model can also be combined with other data reduction techniques, such as filtering, sampling, or quantization, to further improve the compression performance .



### Coding for Compression Techniques

Coding is the process of assigning symbols or codes to the data elements or sequences to reduce their size and facilitate efficient transmission or storage. Coding for compression techniques can be classified into two main categories: lossless and lossy.

- Lossless coding techniques preserve the exact information of the original data, and allow perfect reconstruction after decompression. Lossless coding techniques are suitable for text, audio, and some image data that require high fidelity and accuracy. Some examples of lossless coding techniques are:

  - Huffman coding: A variable-length coding technique that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, based on their probabilities of occurrence. Huffman coding is optimal for a given source with known symbol probabilities, and can achieve the entropy of the source as the average code length. Huffman coding is widely used in text compression, image compression (PNG, GIF), and audio compression (MP3, AAC).
  - LZW (Lempel-Ziv-Welch) coding: A dictionary-based coding technique that builds a code table of sequences of symbols that have occurred in the data, and assigns codes to them. LZW coding is adaptive and does not require prior knowledge of the source statistics. LZW coding is efficient for data with repeated patterns or sequences, and can achieve high compression ratios. LZW coding is used in image compression (TIFF, GIF), text compression (Unix compress), and data compression (ZIP, gzip).
  - Run-length encoding (RLE): A simple coding technique that encodes runs of identical symbols by their length and value. RLE is effective for data with large amounts of redundancy, such as graphics and video data, and can achieve high compression ratios without any data loss or distortion. RLE is used in image compression (BMP, PCX), video compression (MPEG-1, MPEG-2), and fax transmission (CCITT Group 3, Group 4).

- Lossy coding techniques discard some information of the original data, and allow approximate reconstruction after decompression. Lossy coding techniques are suitable for image, video, and some audio data that can tolerate some distortion and quality degradation. Lossy coding techniques exploit the perceptual limitations of the human visual or auditory system, and remove the data that are less important or less noticeable. Some examples of lossy coding techniques are:

  - DCT (Discrete Cosine Transform) coding: A transform coding technique that converts the data from the spatial or temporal domain to the frequency domain, and quantizes and encodes the frequency coefficients. DCT coding exploits the energy compaction property of the DCT, and concentrates most of the signal energy in a few low-frequency coefficients, while discarding or reducing the high-frequency coefficients that are less perceptible. DCT coding is widely used in image compression (JPEG, JPEG 2000), video compression (MPEG, H.26x), and audio compression (MP3, AAC).
  - Motion compensation coding: A predictive coding technique that exploits the temporal redundancy between successive frames in a video sequence, and encodes the difference between the current frame and a predicted frame. Motion compensation coding uses motion estimation to find the best matching block in a reference frame for each block in the current frame, and encodes the motion vector and the prediction error. Motion compensation coding can achieve high compression ratios by reducing the temporal correlation in video data. Motion compensation coding is used in video compression (MPEG, H.26x).
  - Vector quantization coding: A coding technique that partitions the data space into a finite number of regions or clusters, and assigns a representative vector or codebook entry to each region. Vector quantization coding encodes each data vector by the index of the closest codebook entry, and reconstructs the data vector by the corresponding codebook entry. Vector quantization coding can achieve high compression ratios by reducing the spatial correlation in data, but may introduce some distortion or noise. Vector quantization coding is used in image compression (VQ, EZW), speech compression (CELP, LPC), and data compression (V.42bis).



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln and code symbols from an alphabet of size D, the following inequality holds:

  Kraft inequality

- The Kraft inequality can be generalized to any uniquely decodable code by adding a constant term to the right-hand side of the inequality. The constant term depends on the maximum length difference between any two codewords in the code.



# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images and MP3 for music.
- Prefix codes can be derived from various algorithms, such as Huffman coding, arithmetic coding, Lempel-Ziv coding, etc.
- A universal code is a special kind of prefix code that can encode any positive integer with a binary codeword, regardless of the probability distribution of the integers.
- Universal codes have the advantage of being adaptive and efficient for compressing data with unknown or varying statistics.
- Examples of universal codes are Elias gamma code, Elias delta code, Fibonacci code, Golomb code, etc.



## Unit 2 - The Huffman coding algorithm

- The Huffman coding algorithm is a method of lossless data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols.
- The algorithm starts by creating a node for each symbol and assigning it a weight equal to its frequency. Then, it repeatedly merges the two nodes with the lowest weights into a new node, whose weight is the sum of the weights of its children. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to that symbol, and appending a 0 or a 1 depending on whether the left or the right child is chosen at each step. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible codes for a given set of symbols and frequencies. The average code length is equal to the entropy of the data, which is the lower bound for any lossless compression method.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video. However, it requires the knowledge of the symbol frequencies in advance, or a way to estimate them from the data. It also requires the transmission or storage of the code tree along with the compressed data, which may add some overhead.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the minimum expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The minimum variance Huffman code is a variant of the Huffman code that minimizes not only the expected codeword length but also the variance of the codeword length.
- The variance of the codeword length is the difference between the maximum and minimum lengths of the codewords.
- The minimum variance Huffman code is useful when the source has a large alphabet size and the codeword length is constrained by a given constant.
- The algorithm for constructing the minimum variance Huffman code is similar to the standard Huffman algorithm, except that it uses a modified merging criterion.
- The modified merging criterion is to merge the two nodes with the smallest values of p * (2 ^ l), where p is the probability of the node and l is the level of the node in the tree.
- The level of a node is the number of edges from the node to the root of the tree.
- The minimum variance Huffman code can be obtained by assigning 0 and 1 to the left and right branches of the tree, respectively, starting from the root.
- The minimum variance Huffman code has the property that the codewords with the same length are consecutive in the lexicographic order.



### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on the Huffman coding algorithm, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data.  

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or non-stationary (i.e., changing over time).
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication for the code.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than Huffman coding, since the code tree has to be modified frequently.
- It may not be suitable for sources with very low entropy (i.e., high predictability), since the code tree may become unbalanced and inefficient.
- It may not be compatible with some applications that require fixed-length codes or random access to the data.

There are different algorithms for implementing adaptive Huffman coding, such as the FGK algorithm and the Vitter algorithm. These algorithms differ in how they update the code tree and how they handle new symbols that have not been seen before.  

The following diagram shows an example of adaptive Huffman coding using the Vitter algorithm for the string "ABRACADABRA". The algorithm starts with an empty code tree and a special symbol NYT (Not Yet Transmitted) that represents all unseen symbols. As each symbol is encoded, the algorithm updates the code tree by incrementing the frequencies of the nodes, swapping nodes to maintain the sibling property (i.e., nodes with the same frequency are ordered by decreasing weight), and splitting the NYT node into two new nodes for the new symbol and a new NYT node. The algorithm also outputs the code for each symbol, which is obtained by traversing the code tree from the root to the leaf. The code for a new symbol is the code for the NYT node followed by the binary representation of the symbol.

Adaptive Huffman coding example

The final code for the string "ABRACADABRA" is:

```
A: 0000
B: 0001
R: 001
C: 0100
D: 0101
```

The total number of bits is 40, which is less than the 44 bits required by the static Huffman code for the same string. 

: https://en.wikipedia.org/wiki/Adaptive_Huffman_coding
: https://xlinux.nist.gov/dads/HTML/adaptiveHuffman.html
: https://www.geeksforgeeks.org/adaptive-huffman-coding-and-decoding/
: http://ben-tanen.com/adaptive-huffman/



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here is the update procedure for the notes of the Unit 2 - The Huffman coding algorithm:

1. Review the learning objectives and outcomes of the unit. They are:

   - Explain the concept of variable-length codes and prefix codes.
   - Describe the Huffman coding algorithm and its steps.
   - Apply the Huffman coding algorithm to encode and decode messages.
   - Analyze the efficiency and optimality of the Huffman coding algorithm.
   - Compare and contrast the Huffman coding algorithm with other compression methods.

2. Read the updated notes of the unit. They are:

   - Variable-length codes are codes that use different numbers of bits to represent different symbols. For example, in Morse code, the letter E is represented by a single dot, while the letter Q is represented by two dashes and a dot. Variable-length codes can reduce the average number of bits per symbol, and thus achieve compression.
   - Prefix codes are a special type of variable-length codes that have the property that no code is a prefix of another code. This means that the codes can be uniquely decoded without any delimiter or marker. For example, the codes 01, 10, and 11 are prefix codes, but the codes 0, 01, and 10 are not, because 0 is a prefix of 01 and 10.
   - The Huffman coding algorithm is a method of constructing optimal prefix codes for a given set of symbols and their probabilities or frequencies. The algorithm works as follows:

     - Create a leaf node for each symbol and assign it a weight equal to its probability or frequency.
     - Sort the nodes in ascending order of their weights.
     - While there is more than one node in the list:
       - Remove the two nodes with the lowest weights from the list.
       - Create a new internal node with the two nodes as its children and assign it a weight equal to the sum of their weights.
       - Insert the new node into the list in its sorted position.
     - The remaining node is the root of the Huffman tree.
     - Traverse the tree and assign a bit (0 or 1) to each edge. The code for each symbol is the concatenation of the bits along the path from the root to the leaf node.
   - To encode a message using the Huffman coding algorithm, replace each symbol in the message with its corresponding code. To decode a message, start from the root of the tree and follow the bits in the message until reaching a leaf node, then output the symbol and repeat until the end of the message.
   - The Huffman coding algorithm is efficient and optimal because it minimizes the average number of bits per symbol, which is equal to the weighted sum of the lengths of the codes. The algorithm also satisfies the Kraft-McMillan inequality, which states that for any prefix code, the sum of the probabilities raised to the power of the lengths of the codes is less than or equal to one.
   - The Huffman coding algorithm can be compared and contrasted with other compression methods, such as run-length encoding, dictionary-based encoding, and arithmetic coding. Some of the advantages and disadvantages of the Huffman coding algorithm are:

     - It is simple and easy to implement.
     - It is lossless and preserves the original information.
     - It adapts to the statistics of the source and assigns shorter codes to more frequent symbols.
     - It requires the knowledge of the probabilities or frequencies of the symbols, which may not be available or may change over time.
     - It may not be optimal for some sources that have dependencies or correlations among the symbols.
     - It may produce variable-length codes that are not aligned to byte boundaries, which may cause difficulties in storage and transmission.

3. Test your understanding of the unit by answering the following questions:

   - What is the difference between variable-length codes and prefix codes?
   - What are the steps of the Huffman coding algorithm?
   - How do you encode and decode a message using the Huffman coding algorithm?
   - How do you measure the efficiency and optimality of the Huffman coding algorithm?
   - What are some of the advantages and disadvantages of the Huffman coding algorithm compared to other compression methods?

4. Check your answers with the answer key provided at the end of the notes. If you have any doubts or queries, you can ask me for clarification or explanation. I hope you find this update procedure helpful and informative. Good luck with your studies! 😊



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies . The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized. The algorithm works as follows     :

- Create a leaf node for each character and assign it a weight equal to its frequency.
- Sort the nodes in ascending order of their weights.
- While there is more than one node in the list:
  - Remove the two nodes with the lowest weights from the list.
  - Create a new internal node with these two nodes as its children and the sum of their weights as its weight.
  - Insert the new node into the list in its sorted position.
  - Repeat until the list contains only one node, which is the root of the Huffman tree.
- Traverse the Huffman tree and assign a bit (0 or 1) to each edge, such that no two edges along any path have the same bit.
- For each character, concatenate the bits along the path from the root to the leaf node representing that character. This is the Huffman code for that character.

Here is an example of Huffman coding for the string "BANANA":

- The frequencies of the characters are: B: 1, A: 3, N: 2.
- The initial list of nodes is: [B: 1, N: 2, A: 3].
- The first iteration of the loop removes B and N and creates a new node with weight 3 and children B and N. The new list is: [[B, N]: 3, A: 3].
- The second iteration of the loop removes [B, N] and A and creates a new node with weight 6 and children [B, N] and A. The new list is: [[B, N], A]: 6].
- The loop ends and the root of the Huffman tree is [[B, N], A]: 6].
- The Huffman tree looks like this:

```
       [[B, N], A]: 6
       /          \
      /            \
     /              \
    /                \
[B, N]: 3            A: 3
 /    \              / \
B: 1  N: 2          0   1
/ \   / \
0   1 0   1
```

- The Huffman codes for the characters are: B: 00, N: 01, A: 1.
- The encoded string is: 001101011.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the source data.
- The Huffman code is a prefix code, which means that no code is a prefix of another code. This property ensures that the code is uniquely decodable.
- The decoding procedure for the Huffman code is the reverse of the encoding procedure. It involves the following steps:

  1. Construct the Huffman tree from the given code table or frequency table. The Huffman tree is a binary tree that represents the code assignments for each symbol. The root node has no code, and each child node inherits the code of its parent node with an additional bit: 0 for the left child and 1 for the right child. The leaf nodes are the symbols with their codes.
  2. Read the encoded bitstream from left to right and traverse the Huffman tree from the root node. For each bit, move to the left or right child node according to the bit value: 0 for the left and 1 for the right.
  3. When a leaf node is reached, output the symbol corresponding to that node and return to the root node. Repeat this process until the end of the bitstream is reached or a special end-of-file (EOF) symbol is encountered.

- Example: Suppose the following code table is given for a source alphabet of five symbols: A, B, C, D, and E.

| Symbol | Code  |
| ------ | ----- |
| A      | 0     |
| B      | 10    |
| C      | 110   |
| D      | 1110  |
| E      | 1111  |

- The Huffman tree for this code table is shown below:

```
        *
       / \
      0   1
     /     \
    A       *
          /   \
         0     1
        /       \
       B         *
              /     \
             0       1
            /         \
           C           *
                    /     \
                   0       1
                  /         \
                 D           E
```

- To decode the bitstream 10110111101110, we start from the root node and follow the bits:

  - 1: move to the right child node
  - 0: move to the left child node, output B and return to the root node
  - 1: move to the right child node
  - 1: move to the right child node
  - 0: move to the left child node, output C and return to the root node
  - 1: move to the right child node
  - 1: move to the right child node
  - 1: move to the right child node
  - 1: move to the right child node, output E and return to the root node
  - 1: move to the right child node
  - 1: move to the right child node
  - 0: move to the left child node, output D and return to the root node
  - 1: move to the right child node
  - 1: move to the right child node
  - 0: move to the left child node, output C and return to the root node

- The decoded output is BCEEDC.



### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder .
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r  .
- The binary code for r can be either fixed-length or variable-length, depending on the value of M .
- If M is a power of 2, the binary code for r is fixed-length and has log2(M) bits .
- If M is not a power of 2, the binary code for r is variable-length and uses a technique called truncated binary encoding .
- Truncated binary encoding splits the range of possible values of r into two subranges: the lower range [0, b-1] and the upper range [b, M-1], where b = 2^ceil(log2(M))^ - M.
- The lower range has b values and can be encoded with floor(log2(M)) bits, while the upper range has M-b values and can be encoded with ceil(log2(M)) bits.
- The binary code for r is then constructed by appending a 0 or a 1 to indicate which subrange r belongs to, followed by the binary representation of r in the corresponding subrange.
- Golomb codes are optimal for data with geometric distributions, where the probability of x is proportional to (1-p)^x^ for some p .
- The optimal value of M for geometric distributions is M = -1/log2(1-p) or the nearest integer .
- Golomb codes can also be used for data with exponential distributions, where the probability of x is proportional to e^-lambda x^ for some lambda.
- The optimal value of M for exponential distributions is M = 1/lambda or the nearest integer.
- Golomb codes have applications in lossless compression of text, images, audio, and video, especially for data with high skewness or long-tailed distributions .
- Golomb codes are also used in run-length encoding, where the lengths of runs of identical symbols are encoded with Golomb codes .
- Golomb codes are closely related to Rice codes, which are a special case of Golomb codes where M is a power of 2 .



### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a positive integer x using Rice codes, the following steps are performed :
  - Divide x by m and obtain the quotient q and the remainder r.
  - Write q in unary code, which means using q ones followed by a zero.
  - Write r in binary code, using k bits.
  - Concatenate the unary code and the binary code to form the final code.
- For example, if k = 2 and x = 9, then:
  - Divide 9 by 4 and obtain the quotient 2 and the remainder 1.
  - Write 2 in unary code as 110.
  - Write 1 in binary code as 01, using 2 bits.
  - Concatenate 110 and 01 to form the final code 11001.
- Rice codes are generally used to encode entropy in audio/video codecs, where the data tends to have a geometric distribution.
- Rice codes are also adaptive, which means that the parameter k can be changed according to the statistics of the data.
- Rice codes have the advantage of being fast and easy to implement, but they may not achieve the best compression ratio for some data sets.

: Golomb coding - Wikipedia
: Rice Coding - unix4lyfe.org
: 22.(A). Rice Codes Algorithm: Step by Step Explanation. - YouTube



### Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression.
- Tunstall codes are variable-to-fixed length codes, which means they map variable-length source words to fixed-length codewords .
- Tunstall codes are based on a source model that assigns probabilities to source words, which are sequences of symbols from a finite alphabet.
- Tunstall codes are constructed by using a prefix tree, where each leaf node corresponds to a codeword and each internal node corresponds to a source word prefix .
- Tunstall codes are optimal for sources that have a geometric distribution of word probabilities, such as run-length encoded data.
- Tunstall codes have some advantages over other entropy coding methods, such as:
  - They are easy to implement and decode.
  - They have a bounded compression ratio, which means they never expand the data by more than a fixed factor.
  - They are suitable for streaming data, since they do not require a priori knowledge of the source statistics or a header to store them.
- Tunstall codes have some disadvantages, such as:
  - They are not adaptive, which means they cannot adjust to changes in the source statistics.
  - They are not universal, which means they cannot achieve the entropy of any source.
  - They require a large codebook size, which limits their practical applicability.



### Applications of Huffman coding

Huffman coding is a technique of lossless data compression that assigns variable-length codes to the symbols of a data stream based on their frequencies or weights . It is a type of prefix code, which means that no code is a prefix of another code. Huffman coding has several applications in the real world, such as:

- Text and fax transmissions: Huffman coding can reduce the size of text files by encoding the most frequent characters with fewer bits and the less frequent ones with more bits. This can save bandwidth and storage space for text and fax transmissions.
- Image and audio compression: Huffman coding can be used in conjunction with other techniques, such as discrete cosine transform (DCT) and quantization, to compress image and audio files, such as JPEG, PNG, and MP3 . Huffman coding can encode the coefficients of the DCT and the quantized values with variable-length codes, reducing the number of bits needed to represent them.
- Cryptography: Huffman coding can be used to encrypt and decrypt data by using a secret key to generate the code table. The code table can be used to map the symbols of the plaintext to the codes of the ciphertext, and vice versa. This can provide a simple and secure way of data encryption and decryption.



### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each pixel value in the image.
  - Sort the pixel values in ascending order of frequency and consider them as leaf nodes of a binary tree.
  - Merge the two nodes with the lowest frequency and assign them a parent node with the sum of their frequencies. Label the left branch as 0 and the right branch as 1.
  - Repeat the previous step until there is only one node left, which is the root of the tree.
  - Traverse the tree from the root to the leaves and assign a code to each pixel value by concatenating the labels along the path.
  - Replace each pixel value in the image with its corresponding code and output the compressed image file.

- The advantages of Huffman coding are:

  - It is optimal, meaning that it achieves the minimum possible average code length for a given source distribution.
  - It is simple and easy to implement.
  - It is widely used in many applications, such as JPEG, ZIP, MP3, etc.

- The disadvantages of Huffman coding are:

  - It requires the knowledge of the source distribution or the frequency table, which may not be available or may change over time.
  - It may not be efficient for sources with large alphabets or non-uniform distributions, as the code lengths may vary significantly and the tree may become unbalanced.
  - It may not exploit the spatial correlation or redundancy among neighboring pixels in an image, which can be exploited by other techniques such as run-length coding or predictive coding.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies .
- The most frequent character gets the smallest code and the least frequent character gets the largest code.
- Huffman coding works by creating a binary tree that represents the codes of each character .
- The root of the tree has no code, and each child node inherits the code of its parent with an additional bit (0 for left child, 1 for right child).
- The leaf nodes of the tree are the characters and their codes are the paths from the root to the leaf.
- To construct the Huffman tree, the algorithm follows these steps  :
  - Create a node for each character and its frequency and add them to a priority queue (min-heap).
  - While the queue has more than one node, do the following:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with the sum of the frequencies of the two nodes as its frequency.
    - Make the two nodes the left and right children of the new node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
- To encode a text file, the algorithm traverses the Huffman tree and generates the codes for each character .
- To decode a compressed file, the algorithm starts from the root of the Huffman tree and follows the bits of the file until it reaches a leaf node, which is the decoded character.
- Huffman coding is a greedy algorithm that guarantees an optimal compression ratio for a given text file .
- Huffman coding is widely used in various applications such as computer networks, fax machines, modems, and HDTV.



### Audio Compression

- Audio compression is the process of reducing the size of an audio file by removing or encoding redundant or irrelevant information.
- Audio compression can be lossless or lossy, depending on whether the original data can be perfectly reconstructed or not.
- Lossless compression techniques preserve the quality and fidelity of the audio signal, but achieve lower compression ratios than lossy techniques.
- Lossy compression techniques sacrifice some quality and fidelity for higher compression ratios, but may introduce audible artifacts or distortions.

### The Huffman Coding Algorithm

- The Huffman coding algorithm is a lossless compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The Huffman coding algorithm works by building a binary tree that represents the optimal prefix code for the data, where the most frequent symbols have the shortest codes and the least frequent symbols have the longest codes.
- The Huffman coding algorithm consists of two steps: building the Huffman tree and generating the codes from the tree.
- Building the Huffman tree involves the following steps:
  - Create a leaf node for each symbol and assign it a weight equal to its frequency.
  - Sort the nodes in ascending order by their weights.
  - While there is more than one node in the list:
    - Remove the two nodes with the lowest weights from the list.
    - Create a new internal node with a weight equal to the sum of the two nodes' weights.
    - Assign the left child of the new node to the first removed node and the right child to the second removed node.
    - Insert the new node into the list according to its weight.
  - The remaining node in the list is the root of the Huffman tree.
- Generating the codes from the Huffman tree involves the following steps:
  - Traverse the tree from the root to the leaves, assigning a 0 to each left branch and a 1 to each right branch.
  - The code for each symbol is the sequence of bits along the path from the root to the leaf corresponding to that symbol.
  - The codes are prefix-free, meaning that no code is a prefix of another code.



## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python.
- In Python, we can use lists, tuples, ranges, generators, or comprehensions to create sequences.
- A list is a mutable sequence of values that can be of any type, enclosed in square brackets [ ].
- A tuple is an immutable sequence of values that can be of any type, enclosed in parentheses ( ).
- A range is an immutable sequence of numbers that follow a certain arithmetic progression, created by the range() function.
- A generator is an object that can produce a sequence of values on demand, using the yield keyword or a generator expression.
- A comprehension is a concise way of creating a sequence from another sequence, using a for loop and an optional if condition inside brackets [ ] or parentheses ( ).

- To access a specific element of a sequence, we can use indexing, which is the process of specifying the position of the element using an integer inside square brackets [ ].
- Indexing starts from 0 for the first element, and can be negative for the last element (-1) or the previous ones (-2, -3, etc.).
- To access a subsequence of a sequence, we can use slicing, which is the process of specifying the start and end positions of the subsequence using a colon : inside square brackets [ ].
- Slicing can also take a third argument, which is the step size of the subsequence, indicating how many elements to skip between each one.
- Slicing can be used to reverse a sequence by using a negative step size.

- To iterate over a sequence, we can use a for loop, which is a control structure that repeats a block of code for each element of the sequence.
- The for loop has the syntax: for variable in sequence: block of code
- The variable takes the value of each element of the sequence in turn, and the block of code is executed with that value.
- The for loop can be used to perform various operations on a sequence, such as printing, counting, summing, filtering, mapping, etc.

- To test if a value is in a sequence, we can use the in operator, which returns True if the value is found in the sequence, and False otherwise.
- The in operator can also be used to test if a subsequence is in a sequence, by using the subsequence as the left operand and the sequence as the right operand.
- The in operator can be combined with the not operator to test if a value or a subsequence is not in a sequence.

- To compare two sequences, we can use the comparison operators, such as ==, !=, <, >, <=, >=, which return True or False depending on the result of the comparison.
- The comparison operators compare the sequences element by element, from left to right, until they find a difference or reach the end of one of the sequences.
- The comparison operators can also be used to compare a sequence with a single value, by using the sequence as the left operand and the value as the right operand.
- The comparison operators can be combined with the logical operators, such as and, or, not, to form complex conditions involving sequences.



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits than the original representation.
- A binary code is a way of representing data using only two symbols, usually 0 and 1.
- A binary code can be fixed-length or variable-length, depending on whether each symbol or sequence of symbols has the same or different number of bits.
- A fixed-length binary code assigns the same number of bits to each symbol or sequence of symbols, regardless of their frequency or probability. For example, a binary code that uses 3 bits can encode up to 8 symbols or sequences of symbols, such as 000, 001, 010, 011, 100, 101, 110, 111.
- A variable-length binary code assigns different numbers of bits to different symbols or sequences of symbols, depending on their frequency or probability. For example, a binary code that uses fewer bits for more frequent or probable symbols or sequences of symbols and more bits for less frequent or probable symbols or sequences of symbols can achieve better compression. A variable-length binary code must be prefix-free, meaning that no code is a prefix of any other code, to avoid ambiguity in decoding.
- A prefix-free variable-length binary code can be constructed using a technique called Huffman coding, which assigns shorter codes to more frequent or probable symbols or sequences of symbols and longer codes to less frequent or probable symbols or sequences of symbols, based on a binary tree structure that represents the relative frequencies or probabilities of the symbols or sequences of symbols.
- A universal code is a special type of variable-length binary code that can encode any sequence of positive integers, regardless of their probability distribution, with a constant factor of optimality. A universal code can be used to encode the lengths of the variable-length codes in a compressed data stream, or to encode the symbols or sequences of symbols themselves if their probability distribution is unknown or changing. Examples of universal codes are Elias gamma code, Elias delta code, and Fibonacci code.



### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing text, computer instructions, or any other data using a two-symbol system, usually 0 and 1 .
- Huffman coding is a method of compressing data using variable-length codes based on the frequencies of the symbols .
- The main difference between binary and Huffman coding is that binary coding assigns a fixed number of bits to each symbol, while Huffman coding assigns a variable number of bits to each symbol.
- Binary coding is simple and easy to implement, but it may not be efficient for data compression, as some symbols may occur more frequently than others and still use the same number of bits.
- Huffman coding is more complex and requires building a Huffman tree and a code table, but it can achieve optimal data compression, as the most frequent symbols use fewer bits and the least frequent symbols use more bits.
- Binary coding is suitable for data transmission and storage, as it can represent any type of data using a universal binary system.
- Huffman coding is suitable for data compression, as it can reduce the size of the data without losing any information. However, it requires the knowledge of the symbol frequencies and the code table to encode and decode the data.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression:

### Applications

- Coding a sequence is a technique to represent a sequence of symbols using fewer bits than the original representation. This can reduce the storage space and transmission time of the sequence.
- Coding a sequence can be applied to various types of data, such as text, images, audio, video, and genomic data. Some examples of coding a sequence are:

  - Huffman coding: a variable-length code that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. It is optimal for a given symbol distribution and can achieve the entropy of the source.
  - Arithmetic coding: a variable-length code that assigns codes to intervals of the [0, 1) range based on the symbol probabilities. It can achieve the entropy of the source with arbitrary precision and can handle any symbol distribution.
  - Run-length encoding: a fixed-length code that encodes runs of the same symbol as a pair of the symbol and the run length. It is useful for compressing data with long runs of repeated symbols, such as binary images or DNA sequences.
  - Lempel-Ziv coding: a dictionary-based code that encodes substrings of the sequence as references to previous occurrences in the sequence. It is adaptive and can handle any source without prior knowledge of the symbol distribution. It is widely used in compression algorithms such as ZIP, GZIP, and PNG.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on bi-level image compression and the JBIG standard.

### Bi-level image compression

- Bi-level image compression is a technique for reducing the size of binary images, such as black-and-white text, graphics, or fax documents.
- Binary images have only two possible pixel values: 0 (black) or 1 (white).
- Bi-level image compression aims to exploit the redundancy and regularity in binary images, such as repeated patterns, horizontal and vertical lines, and large areas of uniform color.
- Bi-level image compression can be either lossless or lossy, depending on the application and the desired quality of the compressed image.
- Lossless compression preserves the exact pixel values of the original image, while lossy compression allows some distortion or noise in the compressed image, in exchange for higher compression ratios.

### The JBIG standard

- JBIG stands for Joint Bi-level Image Experts Group, a committee that developed an international standard for bi-level image compression, published in 1993 as ISO/IEC 11544 and ITU-T T.82.
- JBIG is also known as JBIG1, to distinguish it from the newer JBIG2 standard, published in 2000 as ISO/IEC 14492 and ITU-T T.88.
- JBIG is a lossless compression standard that uses arithmetic coding and adaptive context modeling to encode binary images.
- JBIG can achieve compression ratios of 20% to 50% over Fax Group 4 compression, the most common standard for fax transmission.
- JBIG can also encode multiple images in a single file, using a technique called progressive coding, which allows the transmission of a low-resolution preview of the image, followed by successive refinements of the image quality.
- JBIG can also encode gray-scale or color images, by treating each bit plane of the image as a separate binary image, and compressing them independently.

### The JBIG2 standard

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group. It is suitable for both lossless and lossy compression.
- JBIG2 improves upon JBIG by using more sophisticated techniques for exploiting the redundancy and regularity in binary images, such as segmentation, symbol dictionary, and refinement coding.
- Segmentation is the process of dividing the image into regions that have similar characteristics, such as text, halftones, graphics, or generic bi-level images.
- Symbol dictionary is a technique that identifies and stores the most frequently occurring symbols or patterns in the image, such as letters, digits, or logos, and assigns them a short code.
- Refinement coding is a technique that encodes the difference between a symbol and a previously encoded symbol that is similar to it, using a template that defines the neighborhood pixels to be used for the comparison.
- JBIG2 can achieve compression ratios of 10 to 100 times over Fax Group 4 compression, depending on the image content and the desired quality of the compressed image.
- JBIG2 can also encode multiple images in a single file, using a technique called shared dictionary, which allows the reuse of the same symbol dictionary for different images.
- JBIG2 can also encode gray-scale or color images, by treating each bit plane of the image as a separate binary image, and compressing them independently.

### References

: JBIG - Wikipedia. https://en.wikipedia.org/wiki/JBIG
: JBIG2 - Wikipedia. https://en.wikipedia.org/wiki/JBIG2
: JBIG2-the ultimate bi-level image coding standard - IEEE Xplore. https://ieeexplore.ieee.org/document/900914/



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group   .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression.
- JBIG2 can also achieve much higher compression ratios than the previous standards with almost no visible degradation of quality by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- JBIG2 works by segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and applying compression techniques that are specially optimized for each type of content.
- Text regions are further divided into symbols, which are matched with a symbol dictionary. The dictionary can be either predefined or dynamically generated from the image. The symbols are then encoded by referring to their dictionary index or by using arithmetic coding.
- Halftone regions are compressed by detecting the halftone pattern and encoding it as a single bitmap, along with the parameters of the grid. The bitmap is then compressed using arithmetic coding.
- Generic regions are compressed using a modified version of the JBIG algorithm, which is based on arithmetic coding and adaptive template switching.
- JBIG2 also supports progressive decoding, refinement coding, and arithmetic coding with adaptive probability estimation.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.



Hello, I am Sydney, your AI assistant. I can help you with your topic of image compression. Here are some notes for you:

### Image compression

- Image compression is a process applied to a graphics file to minimize its size in bytes without degrading image quality below an acceptable threshold .
- By reducing the file size, more images can be stored in a given amount of disk or memory space, and less bandwidth is required for transmission over networks .
- Image compression algorithms may take advantage of visual perception and the statistical properties of image data to provide superior results compared with generic data compression methods which are used for other digital data.
- Image compression can be classified into two types: lossless and lossy .
  - Lossless compression preserves the exact pixel values of the original image, and allows perfect reconstruction of the original image from the compressed file .
  - Lossy compression discards some information from the original image, and introduces some distortion or artifacts in the reconstructed image .
  - Lossless compression is suitable for images that require high fidelity, such as medical images, scientific images, or archival images .
  - Lossy compression is suitable for images that can tolerate some quality degradation, such as natural images, web images, or video images .
- Image compression can be performed in different domains, such as spatial domain, frequency domain, or wavelet domain.
  - Spatial domain compression operates directly on the pixel values of the image, and applies techniques such as run-length encoding, Huffman coding, arithmetic coding, or dictionary coding.
  - Frequency domain compression transforms the image into a representation that consists of frequency components, such as discrete cosine transform (DCT), discrete Fourier transform (DFT), or discrete wavelet transform (DWT), and applies techniques such as quantization, zigzag scanning, or entropy coding.
  - Wavelet domain compression is a special case of frequency domain compression that uses wavelets, which are functions that can capture both the frequency and the spatial information of the image, and applies techniques such as subband coding, embedded zerotree wavelet (EZW) coding, or set partitioning in hierarchical trees (SPIHT) coding.
- Image compression can be performed in different modes, such as predictive coding, transform coding, or hybrid coding.
  - Predictive coding exploits the spatial redundancy of the image, and predicts the pixel values based on the neighboring pixels, and encodes the prediction error.
  - Transform coding exploits the frequency redundancy of the image, and transforms the image into a representation that concentrates most of the energy in a few coefficients, and encodes the significant coefficients.
  - Hybrid coding combines both predictive coding and transform coding, and applies different techniques to different regions of the image, such as intraframe coding and interframe coding.
- Image compression can be performed in different standards, such as JPEG, JPEG 2000, PNG, GIF, or WebP .
  - JPEG is the most widely used standard for lossy compression of natural images, and uses DCT as the transform, quantization as the compression technique, and Huffman coding as the entropy coding .
  - JPEG 2000 is an improved version of JPEG that uses DWT as the transform, and offers better compression performance, scalability, and error resilience .
  - PNG is a standard for lossless compression of images, and uses a combination of filtering and deflate algorithm, which is a variant of LZ77 and Huffman coding .
  - GIF is a standard for lossless compression of images that have a limited number of colors, such as logos, icons, or cartoons, and uses LZW as the dictionary coding .
  - WebP is a new standard for both lossless and lossy compression of images, and uses VP8 as the compression technique, which is based on DCT and intraframe coding .




### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the redundancy and the size of the data.
- There are many variants of dictionary techniques, such as LZ77, LZ78, LZW, LZSS, LZMA, etc. Each variant differs in how the dictionary is constructed, updated, and accessed.
- Dictionary techniques are suitable for compressing natural language texts, as they can exploit the high frequency of common words and phrases. They can also be used for other types of data, such as images, audio, and video, by applying some preprocessing steps to convert the data into a suitable format.
- Dictionary techniques have some advantages and disadvantages. Some of the advantages are:
  - They can achieve high compression ratios for data with high redundancy and regularity.
  - They can adapt to the characteristics of the data and handle different types of data with the same algorithm.
  - They can be implemented efficiently and have low computational complexity.
- Some of the disadvantages are:
  - They can suffer from dictionary overflow, which occurs when the dictionary becomes too large to fit in the memory or the code space.
  - They can be sensitive to noise and errors, which can propagate and corrupt the decompressed data.
  - They can have poor performance for data with low redundancy and irregularity.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here is the introduction for the notes of the Unit 3 - Coding a sequence.

### Introduction

- In this unit, we will learn how to encode a sequence of symbols using different coding techniques, such as fixed-length codes, variable-length codes, prefix codes, and Huffman codes.
- A code is a mapping from a set of symbols (called the source alphabet) to a set of binary strings (called the codewords).
- The goal of coding is to compress the data by reducing the number of bits required to represent the symbols, while preserving the information content and allowing for efficient decoding.
- A code is said to be optimal if it minimizes the average codeword length, which is the expected number of bits per symbol.
- A code is said to be uniquely decodable if there is a unique way to recover the original sequence of symbols from the encoded sequence of bits.
- A code is said to be prefix-free or instantaneous if no codeword is a prefix of another codeword. This property ensures that the code is uniquely decodable and allows for simple decoding without knowing the length of each codeword.
- A Huffman code is a prefix-free code that is optimal for a given source alphabet and a given probability distribution of the symbols. It is constructed by using a binary tree that assigns shorter codewords to more frequent symbols and longer codewords to less frequent symbols.



### Static Dictionary

- A static dictionary is a fixed set of symbols and their corresponding codes that are used to compress and decompress a sequence of symbols.
- A static dictionary is usually predefined and known to both the encoder and the decoder, so it does not need to be transmitted along with the compressed data.
- A static dictionary can be optimal for compressing a sequence if the dictionary matches the probability distribution of the symbols in the sequence.
- A static dictionary can be inefficient or ineffective for compressing a sequence if the dictionary does not match the probability distribution of the symbols in the sequence, or if the sequence contains symbols that are not in the dictionary.
- A static dictionary can be implemented using various data structures, such as arrays, hash tables, trees, or tries.
- A static dictionary can be designed using various methods, such as Huffman coding, arithmetic coding, or Lempel-Ziv coding.



### Diagram Coding

Diagram coding is a lossless data compression method that uses pairs of symbols (digrams) to reduce the size of the source data. It works by finding the most frequent digrams in the data and assigning them codes that correspond to unused symbols, if any. The data is then scanned and replaced by the codes whenever a digram is found. This process can be repeated iteratively until no more compression is possible or the dictionary is full.

Some features of diagram coding are:

- It is an ad hoc method, meaning it does not rely on any prior knowledge of the data or its statistics.
- It is a semi-static method, meaning it builds the dictionary dynamically during the compression, but does not update it during the decompression.
- It is a variable-length method, meaning it uses different number of bits for different symbols or digrams.
- It is a prefix-free method, meaning no code is a prefix of another code, which allows for easy decoding.

An example of diagram coding is:

- Suppose the source data is `ABRACADABRA`.
- The alphabet is `A, B, C, D, R`, and the unused symbols are `E, F, G, H, ...`.
- The most frequent digrams are `AB` and `RA`, each occurring 3 times.
- Assign the code `E` to `AB` and the code `F` to `RA`.
- Scan the data and replace the digrams by the codes: `EEFCADEEF`.
- The compressed data is 9 symbols long, while the original data is 11 symbols long, achieving a compression ratio of 81.8%.



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel .
- LZ77 is a method that uses a sliding window to store the most recent data and searches for matches with the current data in the window. If a match is found, the current data is replaced by a pointer to the location and length of the match in the window .
- LZ78 is a method that builds a dictionary of phrases from the input data and assigns a code to each phrase. The input data is then replaced by the codes of the corresponding phrases in the dictionary. The dictionary is updated with new phrases as they are encountered in the input data .
- LZW is a method that is based on LZ78, but uses a variable-length code for the phrases in the dictionary. The code length increases as the dictionary grows, allowing more phrases to be stored. LZW also uses a special code to indicate when the dictionary needs to be cleared and rebuilt .
- Adaptive dictionary is widely used in applications such as text, image, audio, and video compression, as well as data transmission and storage  .



### The LZ77 Approach

- LZ77 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1977 .
- It is a dictionary coder and maintains a sliding window during compression .
- The sliding window consists of two parts: a search buffer and a look-ahead buffer  .
- The search buffer contains the previously encoded data, and the look-ahead buffer contains the data to be encoded  .
- The algorithm tries to find the longest match between the look-ahead buffer and the search buffer, and encodes it as a triple of the form (offset, length, next symbol)  .
- The offset is the distance from the current position to the start of the match in the search buffer, the length is the number of symbols in the match, and the next symbol is the symbol following the match in the look-ahead buffer  .
- If no match is found, the algorithm encodes the next symbol in the look-ahead buffer as a triple of the form (0, 0, symbol)  .
- The algorithm then slides the window by one or more symbols, depending on the length of the match, and repeats the process until all the data is encoded  .
- The encoded data can be decoded by reversing the process, using the triples to reconstruct the original data  .
- LZ77 is a simple and effective compression algorithm that can achieve high compression ratios for data with repeated patterns .
- However, it also has some drawbacks, such as the limited size of the sliding window, the overhead of the triples, and the inefficiency of encoding single symbols .
- Some variations of LZ77 have been proposed to overcome these drawbacks, such as LZSS, LZMA, DEFLATE, and others.



### The LZ78 Approach

- LZ78 is a lossless data compression algorithm created by Abraham Lempel and Jacob Ziv in 1978 .
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- A token sequence is a string of characters or symbols that can be represented by a single code word.
- A dictionary entry consists of an index and a character. The index is a pointer to a previous token sequence in the dictionary, and the character is the next symbol that follows the token sequence in the input.
- The dictionary is initialized with all possible single characters as the first entries, and then new entries are added as new token sequences are encountered in the input.
- The output of LZ78 is a sequence of tokens, each consisting of an index and a character. The index is a binary number that indicates the position of the token sequence in the dictionary, and the character is the next symbol that follows the token sequence in the input.
- The output can be further compressed by using variable-length codes to encode the indices, such as Huffman codes or arithmetic codes.
- LZ78 has the advantage of being adaptive, meaning that it does not require any prior knowledge of the input data or its statistics. It also has the advantage of being easy to implement and decode.
- LZ78 has the disadvantage of requiring a large dictionary size, which can limit its compression performance and memory usage. It also has the disadvantage of being inefficient for compressing data with high redundancy or low entropy.
- LZ78 is the basis for many variations and extensions, such as LZW, LZSS, LZMA, and others   . These algorithms improve upon LZ78 by using different data structures, encoding methods, or compression techniques.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some applications for the notes of the Unit 3 - Coding a sequence:

- Coding a sequence is a technique to represent a sequence of symbols using fewer bits than the original representation. It can be used to compress data and reduce storage space or transmission bandwidth.
- Coding a sequence can be divided into two types: lossless and lossy. Lossless coding preserves the exact information of the original sequence, while lossy coding discards some information to achieve higher compression ratios.
- Some examples of lossless coding are Huffman coding, arithmetic coding, run-length encoding, and Lempel-Ziv coding. These methods can be used to compress text, images, audio, or any data that requires exact reconstruction.
- Some examples of lossy coding are transform coding, quantization, and entropy coding. These methods can be used to compress images, audio, video, or any data that can tolerate some distortion or noise.
- Coding a sequence can also be combined with other techniques, such as dictionary coding, predictive coding, or hybrid coding, to improve the compression performance or quality. These techniques can exploit the redundancy or correlation in the data to achieve better compression ratios.



### File Compression-UNIX compress

- File compression is a technique to reduce the size of files by removing redundant or unnecessary information, such as repeating patterns, spaces, or symbols.
- File compression can save disk space, bandwidth, and transmission time, and can also protect data from unauthorized access or modification.
- UNIX compress is a file compression utility that uses the Lempel-Ziv-Welch (LZW) algorithm to compress files.
- UNIX compress can reduce the size of text files by 40% to 60%, and binary files by 20% to 40%, depending on the file content and format.
- UNIX compress adds a .Z extension to the compressed file name, and preserves the original file name, permissions, and timestamp.
- UNIX compress can be used with the tar command to create compressed archive files, which can store multiple files and directories in a single file.
- UNIX compress can be invoked by the command `compress [options] [files]`, where options can be:

  - `-b n`: Set the maximum number of bits per code to n (default is 16, minimum is 9, maximum is 24).
  - `-c`: Write the output to the standard output, and do not change the input files.
  - `-d`: Decompress the input files.
  - `-f`: Force compression or decompression, even if the file has multiple links, the output file already exists, or the file has a special or non-regular type.
  - `-v`: Write the name and percentage reduction for each file to the standard error.

- UNIX compress can be used with the following commands to perform various operations on compressed files:

  - `uncompress [options] [files]`: Decompress the files compressed by compress.
  - `zcat [files]`: Write the contents of the compressed files to the standard output, without changing the input files.
  - `zmore [files]`: Display the contents of the compressed files one screen at a time, without changing the input files.
  - `zgrep [options] [pattern] [files]`: Search for a pattern in the compressed files, without changing the input files.
  - `zdiff [options] [file1] [file2]`: Compare two compressed files, without changing the input files.
  - `znew [files]`: Recompress the files from .Z (compress) format to .gz (gzip) format.

- UNIX compress is compatible with most UNIX and Linux systems, but it is not widely used anymore, as newer compression utilities, such as gzip and bzip2, offer better compression ratios and more features.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on image compression for the unit 3 of data compression.

### Image Compression

- Image compression is a type of data compression applied to digital images, to reduce their cost for storage or transmission.
- Image compression can be lossless or lossy. Lossless compression preserves the exact quality and information of the original image, but achieves less compression ratio. Lossy compression discards some information of the original image, but achieves higher compression ratio.
- Image compression algorithms may take advantage of visual perception and the statistical properties of image data to provide superior results compared with generic data compression methods.
- Image compression can be performed in different domains, such as spatial domain, frequency domain, or wavelet domain. Different domains have different advantages and disadvantages in terms of complexity, quality, and compression ratio.
- Some common image compression formats are JPEG, PNG, GIF, TIFF, BMP, and WebP. Each format has its own characteristics and applications. For example, JPEG is suitable for natural images with smooth color transitions, PNG is suitable for images with transparency and sharp edges, GIF is suitable for animations and simple graphics, TIFF is suitable for high-quality images and printing, BMP is suitable for uncompressed images, and WebP is suitable for web images with both lossy and lossless compression .



### The Graphics Interchange Format (GIF)

- GIF stands for Graphics Interchange Format  .
- GIF is a raster file format designed for relatively basic images that appear mainly on the internet.
- GIF uses the Lempel-Ziv-Welch (LZW) algorithm to losslessly compress 8-bit indexed color graphics.
- Each GIF file can support up to 8 bits per pixel and can contain 256 indexed colors .
- GIF files can also store multiple images in a single file, creating an animation effect .
- GIF files have the extension .gif and use the MIME type image/gif .
- GIF files are widely used for web graphics, such as logos, icons, banners, and emoticons .
- GIF files have some limitations, such as the fixed color palette, the lack of transparency support, and the low quality of animation .
- GIF files can be created, edited, and opened using various software tools, such as Adobe Photoshop, GIMP, and online GIF makers .



### Compression over Modems

- Compression over modems is a technique that reduces the amount of data that needs to be transmitted over a phone line or a network by using algorithms that eliminate redundancy and encode information more efficiently .
- Compression over modems can improve the effective data rate and throughput of a modem connection by reducing the transmission time and bandwidth requirements .
- Compression over modems can also enhance the reliability and quality of a modem connection by reducing the impact of noise and errors on the transmitted data.
- Compression over modems can be performed by hardware or software, depending on the type and capability of the modem and the communication protocol used  .
- Compression over modems can be classified into two types: static and dynamic.
  - Static compression uses a fixed dictionary of common patterns and symbols to compress and decompress data. Static compression is fast and simple, but has limited compression ratio and adaptability.
  - Dynamic compression uses a variable dictionary that is updated and exchanged between the modems during the communication. Dynamic compression is more complex and slower, but has higher compression ratio and adaptability.
- Compression over modems can be combined with error correction and modulation techniques to achieve optimal performance and compatibility .
- Compression over modems is standardized by various international organizations and specifications, such as CCITT V.42bis, MNP 5, STAC, and CSA  .



### V.42 bits

- V.42 is an ITU-T standard for error correction in modems .
- V.42bis is an extension of V.42 that provides data compression up to 4:1  .
- V.42bis uses a dynamic dictionary algorithm called BTLZ (British Telecom Lempel Ziv), which is based on the LZW (Lempel Ziv Welch) algorithm  .
- V.42bis can switch to transparent mode, in which data is transmitted uncompressed, when the compression ratio is low or the data is already compressed.
- V.42bis is suitable for implementation on a modem with an 8-bit microprocessor, 40 Kbytes of RAM, 32 Kbytes of ROM, a 9.6 KBaud V.32 modem-modem connection, and a 19.2 KBaud EIA-232-D modem-terminal connection.



### Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, and then encodes the difference between the actual and the predicted symbol or bit. The difference, also called the residual or the error, is usually smaller than the original symbol or bit, and can be compressed more efficiently.

Some examples of predictive coding algorithms are:

- **Linear predictive coding (LPC)**: This is a technique used mostly in audio and speech processing, where the spectral envelope of a signal is represented by a linear combination of previous samples. The coefficients of the linear combination are called the LPC parameters, and they are transmitted along with the residual signal. LPC can achieve high compression ratios for speech signals, as well as synthesize speech from the LPC parameters. 
- **Dynamic Markov compression (DMC)**: This is a technique that uses a Markov model to predict the next bit in a binary sequence, based on the previous bits. The Markov model is updated dynamically as new bits are processed, and the prediction is encoded using arithmetic coding. DMC can achieve high compression ratios for natural language texts, as well as other types of data.  
- **Predictive coding for images**: This is a technique that exploits the spatial redundancy in images, where neighboring pixels tend to have similar values. The value of each pixel is predicted from its neighbors, and the difference is encoded using a suitable entropy coder, such as Huffman coding or arithmetic coding. This technique is used in many image compression standards, such as JPEG, PNG, and WebP.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on prediction with partial match (PPM) for data compression.

### Prediction with Partial Match (PPM)

- PPM is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a trie (a tree-like data structure) of contexts and their associated probabilities for each possible symbol .
- The trie is updated dynamically as new symbols are encountered, and the probabilities are adjusted accordingly .
- The prediction is made by traversing the trie from the root to the leaf that matches the current context, and choosing the symbol with the highest probability .
- If the context is not found in the trie, the algorithm backs off to a shorter context and repeats the process until a match is found or the root is reached .
- The back-off mechanism allows the algorithm to handle unseen contexts and symbols, and to adapt to changing data characteristics .
- The compression is achieved by encoding the predicted symbol using an arithmetic coder, which assigns shorter codes to more probable symbols .
- The decompression is done by reversing the process, using the same trie and arithmetic coder to decode the symbols from the compressed stream .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression:

### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The goal of coding a sequence is to represent a source sequence of symbols with a binary sequence of bits, such that the original sequence can be recovered from the binary sequence with minimal loss of information.
- The basic algorithm for coding a sequence consists of three steps:
  - Step 1: Define a source alphabet, which is the set of symbols that can appear in the source sequence. For example, the source alphabet for English text can be the 26 letters of the alphabet, plus punctuation marks and spaces.
  - Step 2: Define a code alphabet, which is the set of symbols that can appear in the binary sequence. The code alphabet is usually the binary alphabet, which consists of the two symbols 0 and 1.
  - Step 3: Define a code, which is a mapping from the source alphabet to the code alphabet. The code assigns a binary sequence (called a codeword) to each symbol in the source alphabet. For example, the code can assign the codeword 010 to the letter A, the codeword 011 to the letter B, and so on.
- The code should satisfy two properties:
  - Property 1: The code should be uniquely decodable, which means that there is only one way to recover the original source sequence from the binary sequence. This implies that no codeword is a prefix of another codeword, otherwise there would be ambiguity in decoding. For example, the code that assigns 0 to A and 01 to B is not uniquely decodable, because the binary sequence 01 can be decoded as either AB or B.
  - Property 2: The code should be efficient, which means that it minimizes the average length of the binary sequence for a given source sequence. This implies that the code should assign shorter codewords to more frequent symbols, and longer codewords to less frequent symbols. For example, the code that assigns 0 to E and 11111 to Z is more efficient than the code that assigns 0 to Z and 11111 to E, because E is more frequent than Z in English text.
- There are different types of codes that can be used for coding a sequence, such as fixed-length codes, variable-length codes, prefix codes, Huffman codes, arithmetic codes, and so on. Each type of code has its own advantages and disadvantages, depending on the characteristics of the source sequence and the desired level of compression.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of the escape symbol for the notes of Unit 3 - Coding a sequence in the subject of Data Compression.

### The ESCAPE SYMBOL

- An escape symbol is a special symbol that is used to indicate that the next symbol in a sequence is not encoded using the current codebook, but using a different one.
- The escape symbol is useful when the codebook is not fixed, but adaptive, meaning that it changes over time based on the symbols that appear in the sequence.
- The escape symbol allows the encoder and the decoder to switch to a different codebook when they encounter a symbol that is not in the current one, without having to transmit the entire codebook every time.
- The escape symbol can be chosen arbitrarily, as long as it is not confused with any other symbol in the sequence or the codebook. For example, if the sequence consists of ASCII characters, the escape symbol can be a non-printable character, such as 0x1B (ESC).
- The escape symbol can also be used to indicate the end of a sequence, by appending it to the last symbol and followed by a special end-of-sequence symbol, such as 0x00 (NUL).
- The escape symbol can improve the compression ratio of a sequence, by allowing the encoder to use shorter codes for more frequent symbols, and longer codes for less frequent symbols, without having to transmit the entire codebook every time.
- The escape symbol can also reduce the complexity of the encoder and the decoder, by allowing them to use simpler codebooks, such as Huffman codes or arithmetic codes, instead of more complex ones, such as Lempel-Ziv codes or dictionary codes.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of coding a sequence.

### Coding a sequence
- A sequence is a finite or infinite ordered list of symbols, such as letters, digits, or pixels.
- A code is a mapping from symbols to binary strings, such as ASCII or Unicode.
- A code is called **prefix-free** if no codeword is a prefix of another codeword. For example, the code {0, 10, 110, 111} is prefix-free, but the code {0, 01, 10, 11} is not.
- A code is called **uniquely decodable** if there is only one way to decode any encoded sequence. For example, the code {0, 01, 10, 11} is uniquely decodable, but the code {0, 1, 01, 10} is not.
- A code is called **optimal** if it minimizes the expected length of the encoded sequence for a given probability distribution of the symbols. For example, the code {0, 10, 110, 111} is optimal for the distribution {0.5, 0.25, 0.125, 0.125}, but the code {00, 01, 10, 11} is not.
- A **Huffman code** is a prefix-free optimal code that can be constructed by a greedy algorithm. The algorithm starts with a set of nodes, each representing a symbol and its probability. Then, it repeatedly merges the two nodes with the lowest probabilities, assigning 0 and 1 to their edges, until there is only one node left. The codewords are obtained by tracing the paths from the root to the leaves.
- A **Shannon-Fano code** is another prefix-free optimal code that can be constructed by a top-down approach. The algorithm starts with the whole set of symbols and splits it into two subsets with equal or nearly equal probabilities. Then, it assigns 0 and 1 to the subsets and recursively applies the same procedure to each subset until each symbol is assigned a codeword.
- A **Shannon-Fano-Elias code** is a prefix-free code that is asymptotically optimal, meaning that the expected length of the encoded sequence approaches the entropy of the source as the number of symbols increases. The algorithm assigns a codeword to each symbol based on its cumulative probability, which is the sum of the probabilities of all the symbols that precede it in the alphabet. The codeword is obtained by taking the binary representation of the cumulative probability and adding one bit. For example, if the cumulative probability of a symbol is 0.375, its codeword is 0.0110.



### The Exclusion Principle

- The exclusion principle is a technique used in some data compression algorithms, such as PPM, to improve the compression ratio by excluding symbols that are unlikely to occur in a given context.
- The exclusion principle is based on the idea that if a symbol has not occurred in a higher-order context, it is less likely to occur in a lower-order context, and therefore its probability can be reduced or ignored.
- The exclusion principle can be applied in two ways: eager exclusion or lazy exclusion.
  - Eager exclusion: the probabilities of the symbols in the lower-order contexts are reduced by the amount of probability mass assigned to the higher-order context. This requires updating the probabilities of all symbols in the lower-order contexts whenever a new symbol is seen in the higher-order context.
  - Lazy exclusion: the probabilities of the symbols in the lower-order contexts are not reduced, but instead an escape symbol is used to indicate that the actual symbol is not in the current context. This requires only updating the probability of the escape symbol in the lower-order contexts whenever a new symbol is seen in the higher-order context.
- The exclusion principle can improve the compression ratio by assigning more bits to the symbols that are more likely to occur in a given context, and less bits to the symbols that are less likely or impossible to occur in that context.
- The exclusion principle can also reduce the size of the model by eliminating the need to store the probabilities of the symbols that are excluded from the lower-order contexts.
- The exclusion principle is related to the arithmetic coding technique, which divides the unit interval into subintervals based on the probabilities of the symbols. The exclusion principle can be seen as a way of refining the subintervals by excluding the symbols that are not in the current context.



### The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is an algorithm used to prepare data for use with data compression techniques such as bzip2 .
- It was invented by Michael Burrows and David Wheeler in 1994 while Burrows was working at DEC Systems Research Center in Palo Alto, California. It is based on a previously unpublished transformation discovered by Wheeler in 1983.
- The BWT rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding .
- The BWT is a reversible permutation of the characters of a string . One procedure exists for turning a string T into BWT(T) and another exists for turning BWT(T) back into T.
- The procedure for computing BWT(T) is as follows  :
  - Append a special symbol $ to the end of T, which is lexicographically smaller than any other character in T.
  - Construct a table of all cyclic rotations of T$ sorted lexicographically.
  - The BWT(T) is the last column of the table.
- For example, if T = banana, then the table of cyclic rotations is:

| | |
|---|---|
|banana$|anana$b|
|anana$b|nana$ba|
|nana$ba|ana$ban|
|ana$ban|na$bana|
|na$bana|a$banan|
|a$banan|$banana|
|$banana|banana$|

- The last column is annb$aa, which is the BWT(banana).
- The procedure for recovering T from BWT(T) is as follows :
  - Construct the first column of the table by sorting the characters of BWT(T) lexicographically.
  - For each character in BWT(T), find its rank among the characters with the same value in BWT(T) from left to right.
  - For each character in the first column, find its rank among the characters with the same value in the first column from top to bottom.
  - Starting from the row with the $ symbol, follow the rank correspondence between the first and the last column until reaching the $ symbol again.
  - The recovered string T is the sequence of characters encountered along the way, excluding the $ symbol.
- For example, if BWT(T) = annb$aa, then the first column is $aaaabnn and the rank correspondence is:

| | | | | |
|---|---|---|---|---|
|BWT(T)|Rank|First|Rank|T|
|a|1|$|1|a|
|n|1|a|1|n|
|n|2|a|2|a|
|b|1|a|3|n|
|$|1|a|4|a|
|a|2|b|1|b|
|a|3|n|1|$|

- The recovered string T is banana, which is the original string.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of move-to-front coding for data compression.

### Move-to-front coding

- Move-to-front (MTF) coding is a data transformation algorithm that does not compress data by itself, but improves the performance of entropy encoding techniques of compression, such as Huffman coding or arithmetic coding .
- The basic idea of MTF coding is to maintain a list of symbols (such as bytes or characters) in the alphabet, and output the index of the symbol in the list whenever it occurs in the input stream. Then, the symbol is moved to the front of the list, so that it has a smaller index the next time it appears .
- MTF coding is an invertible transform, meaning that the original input can be recovered from the output by using the same list and reversing the process .
- MTF coding is useful for data that has long runs of repeated symbols, or symbols that occur with different frequencies. By moving the symbols to the front of the list, MTF coding reduces the range of possible indices, and makes the output more skewed towards smaller values, which can be encoded more efficiently by entropy encoding techniques  .
- MTF coding is fast and simple to implement, and can be combined with other compression methods to achieve better compression ratios. For example, MTF coding is used as a sub-step in the Burrows-Wheeler transform, which is a key component of the bzip2 compression algorithm .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of CALIC for the Unit 3 - Coding a sequence in the subject of Data Compression.

### CALIC
- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a codec that obtains higher lossless compression of continuous-tone images than other lossless image coding techniques in the literature  .
- It has relatively low time and space complexities  .
- It puts heavy emphasis on image data modeling  .
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics .
- The non-linear predictor adapts via an error feedback mechanism .
- It also uses a context-based binary arithmetic coder to encode the prediction residuals .
- It can be applied to compound video compression by using motion compensation to reduce the temporal redundancy.
- It can achieve high compression ratio and high visual quality for compound video.




### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- JPEG-LS is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- Modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error .
- Encoding stage compresses the prediction errors using a Golomb-Rice code, which is optimal for geometric distributions .
- JPEG-LS has a low complexity and high compression performance, especially for medical and scientific images .
- JPEG-LS is defined in two parts: ISO-14495-1/ITU-T.87 for the core technology and ISO-14495-2/ITU-T.870 for the extensions.
- JPEG-LS extensions include support for higher bit depths, progressive coding, region of interest coding, and arithmetic coding.

: https://en.wikipedia.org/wiki/Lossless_JPEG
: https://www.labs.hp.com/research/info_theory/loco/indexold.htm
: http://www.stat.columbia.edu/~jakulin/jpeg-ls/mirror.htm
: https://jpeg.org/jpegls/
: https://github.com/lnis-uofu/JPEG_LS



### Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of resolution or detail to represent or process data, such as images, signals, or flows.
- The main advantages of multi-resolution approaches are:
  - They can capture long-range phenomena that would otherwise be missed by using a single resolution.
  - They can reduce computational complexity and memory requirements by allowing algorithms to work on both fine and coarse scales .
  - They can improve the performance and quality of data compression by better coding of high frequencies and reducing distortions .
- Some examples of multi-resolution approaches are:
  - Wavelets: Wavelets are functions that can decompose a signal or an image into different frequency components, and then study each component with a resolution matched to its scale.
  - Fractals: Fractals are geometric shapes that have self-similarity, meaning that they look the same at different scales. Fractals can be used to model complex natural phenomena and compress images by finding similarities across different resolutions.
  - Adaptive mesh refinement (AMR): AMR is a technique that dynamically adjusts the resolution of a computational grid according to the features of the solution. AMR can be used to simulate compressible multi-phase flows with high accuracy and efficiency.
  - Cell-averaged multi-resolution: Cell-averaged multi-resolution is a method that uses cell averages of the solution to construct a multi-resolution representation, and then applies a coarsening or refinement operator based on an adaptation strategy. Cell-averaged multi-resolution can be used to solve conservation laws in computational fluid dynamics.
  - B-splines: B-splines are polynomial functions that can be used to approximate a signal or an image with different degrees of smoothness. B-splines can be used to compress data by reconstructing it from a reduced number of coefficients, and to unveil networks of biomarkers from spectroscopy data.



### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for transmitting and storing scanned documents, such as faxes.
- Facsimile encoding exploits the fact that most scanned documents have large areas of white or black pixels, and uses run-length encoding to represent the number of consecutive pixels of the same color  .
- Run-length encoding assigns a variable-length code to each run of pixels, depending on its length and color. For example, a run of 10 white pixels could be encoded as 00001010, and a run of 5 black pixels could be encoded as 11111001.
- Facsimile encoding can achieve high compression ratios for documents that have a lot of white space or simple patterns, such as text or line drawings .
- Facsimile encoding can also use adaptive models to adjust the code lengths based on the statistics of the data, such as the frequency of runs of different lengths and colors .
- Facsimile encoding can be combined with other modulation methods, such as amplitude and phase modulation, to transmit the compressed data over a communication channel.
- Facsimile encoding is standardized by the International Telecommunication Union (ITU) in various recommendations, such as T.4, T.6, and T.82 .



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1.
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input.
- Each node stores a count of how many times each bit has followed the context, and these counts are used to estimate the probabilities of the next bit.
- The probabilities are then fed to an arithmetic coder, which encodes the input bit by bit using fewer bits for more probable symbols.
- The model is updated after each bit is encoded, so that it adapts to the changing statistics of the input.
- DMC is able to achieve high compression ratios for various types of data, especially those with long-range dependencies or non-stationary characteristics .
- However, it also has some drawbacks, such as high memory and computational requirements, and slow encoding and decoding speeds .



## Unit 4 - Distortion criteria

- Distortion criteria are used to determine the onset of yielding or failure in materials under complex loading conditions.
- One of the most widely used distortion criteria is the **von Mises yield criterion**, which states that yielding of a ductile material begins when the second invariant of deviatoric stress reaches a critical value.
- The deviatoric stress is the part of the stress tensor that causes changes in the shape of the material, as opposed to the hydrostatic stress, which causes changes in the volume of the material.
- The von Mises yield criterion can be expressed in terms of the principal stresses as:

$$\sigma_{v}=\sqrt{\frac{1}{2}\left[\left(\sigma_{1}-\sigma_{2}\right)^{2}+\left(\sigma_{2}-\sigma_{3}\right)^{2}+\left(\sigma_{3}-\sigma_{1}\right)^{2}\right]}$$

where $\sigma_{v}$ is the von Mises stress, and $\sigma_{1}$, $\sigma_{2}$, and $\sigma_{3}$ are the principal stresses.

- The von Mises stress can be reduced to simpler forms for different stress conditions, such as uniaxial, biaxial, or triaxial stress.
- The von Mises yield criterion can be interpreted physically as the condition for the onset of plastic deformation in a material, since plastic deformation is associated with distortion energy.
- Another distortion criterion is the **Tresca yield criterion**, which states that yielding of a ductile material begins when the maximum shear stress in the material reaches a critical value.
- The maximum shear stress can be expressed in terms of the principal stresses as:

$$\tau_{max}=\frac{1}{2}\max\left(\left|\sigma_{1}-\sigma_{2}\right|,\left|\sigma_{2}-\sigma_{3}\right|,\left|\sigma_{3}-\sigma_{1}\right|\right)$$

where $\tau_{max}$ is the maximum shear stress, and $\sigma_{1}$, $\sigma_{2}$, and $\sigma_{3}$ are the principal stresses.

- The Tresca yield criterion can also be reduced to simpler forms for different stress conditions, such as uniaxial, biaxial, or triaxial stress.
- The Tresca yield criterion can be interpreted physically as the condition for the onset of slip in a material, since slip is a shear deformation mechanism.
- Distortion criteria can also be applied to other phenomena, such as distortion in amplifiers, which is the deviation of the output signal from the input signal due to non-linearities in the amplifier circuit.
- Distortion in amplifiers can be classified into different types, such as harmonic distortion, intermodulation distortion, crossover distortion, or clipping distortion, depending on the cause and effect of the distortion.
- Distortion criteria can also be used in rate distortion theory, which is a branch of information theory that studies the trade-off between the compression rate and the distortion of a source.
- Rate distortion theory defines the rate distortion function, which is the minimum rate at which a source can be encoded such that the average distortion is below a given threshold.
- The rate distortion function depends on the source statistics, the distortion measure, and the coding scheme.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for the unit 4 - Distortion criteria in the subject of Data Compression.

### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Distortion criteria are the measures of how close an approximation is to its original data, using some mathematical quantity .
- Distortion criteria are important for lossy compression algorithms, which allow some loss of information or quality in exchange for higher compression rates.
- The theory of data compression says that for a given source and a given distortion measure, there is a trade-off between the compression rate and the distortion level.
- The rate-distortion function is the minimum achievable compression rate for a given distortion level .
- The rate-distortion function can be calculated by a powerful iterative algorithm called the Blahut-Arimoto algorithm.
- The rate-distortion function defines the lower bound of the performance of any lossy compression system.
- The closer a practical compression system is to the rate-distortion function, the better it performs.
- Some examples of distortion measures are mean squared error, peak signal-to-noise ratio, structural similarity index, and perceptual distortion measure .



Hello, I am Sydney, your AI assistant. I can help you with your topic of scalar quantization for data compression. Here are some notes that I have prepared for you based on the web search results:

### Scalar Quantization

- Scalar quantization is a process of converting a continuous or discrete signal into a finite number of discrete levels, called quantization levels or reconstruction levels  .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the amount of information needed to represent a signal by discarding some of the less significant bits .
- Scalar quantization can be performed on each sample of the signal independently, without considering the correlation or dependence among the samples. This is called uniform scalar quantization  .
- Scalar quantization can also be performed by adapting the quantization levels to the statistics or characteristics of the signal, such as its mean, variance, or histogram. This is called nonuniform scalar quantization  .
- Scalar quantization can be characterized by three main components: the quantizer, the encoder, and the decoder  .
  - The quantizer is a function that maps each input value to a quantization level, which is usually the closest one to the input value. The quantizer can be represented by a set of decision boundaries and reconstruction levels  .
  - The encoder is a function that assigns a unique binary code to each quantization level, which is usually the shortest possible code to minimize the bit rate. The encoder can be represented by a codebook or a mapping table  .
  - The decoder is a function that reconstructs the original signal from the binary code by using the same codebook or mapping table as the encoder. The decoder can be represented by an inverse quantizer or a lookup table  .
- Scalar quantization can be evaluated by two main criteria: the distortion and the rate  .
  - The distortion is a measure of the difference between the original signal and the reconstructed signal, which is usually quantified by the mean squared error (MSE) or the signal-to-noise ratio (SNR)  .
  - The rate is a measure of the number of bits needed to represent the quantized signal, which is usually quantified by the bit rate (bits per sample) or the entropy (bits per symbol)  .
- Scalar quantization can be optimized by finding the optimal quantizer, encoder, and decoder that minimize the distortion for a given rate, or minimize the rate for a given distortion. This is called the rate-distortion optimization problem  .
- Scalar quantization can be applied to various types of signals, such as audio, image, or video signals. However, scalar quantization is not optimal for signals that have high correlation or dependence among the samples, as it does not exploit the redundancy or structure of the signal. For such signals, vector quantization or transform coding can achieve better compression performance  .
- Scalar quantization can also be combined with other techniques, such as wavelet transform, to achieve higher compression efficiency and quality. For example, the wavelet/scalar quantization (WSQ) standard is a compression algorithm for fingerprint images that uses wavelet transform to decompose the image into subbands, and then applies scalar quantization to each subband.




### The Quantization problem

- Quantization is a process of mapping a large set of input values to a smaller set of output values, with a finite number of levels.
- Quantization is a lossy compression technique, which means that some information is lost in the process and cannot be recovered exactly.
- Quantization is used to reduce the bit rate or storage space required for representing a signal, such as an image or a sound.
- Quantization introduces an error or distortion between the original signal and the quantized signal, which affects the quality of the reconstruction.
- The quantization problem is to find the optimal way of quantizing a signal, such that the distortion is minimized for a given bit rate, or the bit rate is minimized for a given distortion.
- The quantization problem can be formulated as a rate-distortion optimization problem, where the rate is the number of bits per sample and the distortion is a measure of the difference between the original and the quantized signal, such as mean squared error or perceptual distortion.
- The quantization problem can be solved by different methods, depending on the type and dimensionality of the signal, the number and shape of the quantization levels, and the constraints on the rate and distortion.
- Some of the methods for solving the quantization problem are:

  - Uniform quantization: The input range is divided into equal-sized intervals, and each interval is assigned a fixed output value. This method is simple and fast, but may not be optimal for non-uniform signals or perceptual distortion measures.
  - Non-uniform quantization: The input range is divided into variable-sized intervals, and each interval is assigned a fixed output value. This method can adapt to the statistics or characteristics of the signal, and achieve lower distortion or higher quality for the same bit rate.
  - Scalar quantization: The input signal is quantized sample by sample, independently of each other. This method is easy to implement and analyze, but may not exploit the correlation or redundancy among the samples.
  - Vector quantization: The input signal is quantized in blocks or vectors of samples, jointly and dependently. This method can exploit the correlation or redundancy among the samples, and achieve higher compression or lower distortion for the same bit rate.
  - Lloyd algorithm: An iterative algorithm for finding the optimal set of quantization levels for a given set of training samples, based on minimizing the mean squared error distortion. The algorithm alternates between assigning each sample to the closest level and updating each level to the centroid of the assigned samples, until convergence.
  - Rate-distortion theory: A mathematical framework for studying the fundamental limits and trade-offs of lossy compression, based on information theory and statistics. The theory provides the optimal rate-distortion function, which gives the minimum achievable rate for a given distortion, or the minimum achievable distortion for a given rate, for a given source and distortion measure. The theory also provides the optimal coding schemes, such as entropy coding and arithmetic coding, for achieving the rate-distortion function.



### Uniform Quantizer

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values to a finite set of output values with equal spacing between them.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels, and its number of output levels $L$, which is related to the bit rate $R$ by $L = 2^R$.
- A uniform quantizer can be either mid-tread or mid-rise, depending on whether the output levels include zero or not. A mid-tread quantizer has a zero output level and an odd number of levels, while a mid-rise quantizer has a non-zero output level and an even number of levels.
- A uniform quantizer can be used for data compression by encoding the output levels with a fixed number of bits. However, a uniform quantizer may not be optimal for some input distributions, as it may introduce more distortion than a non-uniform quantizer that adapts to the input statistics.
- A uniform quantizer can be combined with a companding function that transforms the input values before quantization and the output values after quantization. A companding function can reduce the dynamic range of the input and increase the perceptual quality of the output. Two common companding functions are the $\mu$-law and the A-law, which are used for PCM telephone systems.



### Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input signal source .
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters, such as synthetic aperture radar (SAR) raw data.
- Adaptive quantization can be classified into two categories: forward adaptive quantization and backward adaptive quantization.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block and transmitted to the receiver as side information. The quantizer parameters can be based on the minimum and maximum values, the mean and variance, or the histogram of the block .
- In backward adaptive quantization, the quantizer parameters are updated based on the previous quantized samples. The quantizer parameters are not transmitted to the receiver, but both the encoder and the decoder use the same update rule to keep the quantizer synchronized.
- Adaptive quantization can be applied to different types of quantizers, such as uniform, nonuniform, scalar, or vector quantizers.
- Adaptive quantization can improve the performance of data compression by reducing the distortion and the bit rate, compared to fixed quantization .
- Adaptive quantization can also be combined with other compression techniques, such as differential pulse-code modulation (DPCM), transform coding, or entropy coding, to achieve higher compression ratios .



### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the input values are more probable and less bits to the regions where the input values are less probable.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that changes the quantization intervals according to the statistics of the input signal.
  - Using an optimal quantizer that minimizes a distortion criterion, such as the mean squared error or the entropy, by adjusting the quantization intervals and levels.
  - Using a trainable quantizer that learns the quantization parameters from the data, such as the network gradients, by using back-propagation or other optimization methods .
- Non uniform quantization has some advantages and disadvantages, such as:
  - Advantages:
    - It can reduce the quantization noise and improve the signal-to-noise ratio.
    - It can preserve more information and details of the input signal.
    - It can be more expressive and flexible to approximate the original signal.
  - Disadvantages:
    - It can be more complex and computationally expensive than uniform quantization.
    - It can require more information to encode and decode the output values, such as the quantization parameters or the non-linear function.
    - It can introduce more distortion and error in the projection process, especially for nonuniformly quantized weights in neural networks.



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Quantization is the process of mapping input values from a large set (often a continuous set) to output values in a (countable) smaller set, often with a finite number of elements.
- Scalar quantization is a type of quantization where each input symbol is treated separately in producing the output.
- Vector quantization is a type of quantization where the input symbols are clubbed together in groups called vectors, and processed to give the output.
- Some of the advantages of vector quantization over scalar quantization are:

  - Vector quantization can remove auto-correlation in the encoded signal and therefore, is more efficient in rate-distortion terms than scalar quantization.
  - Vector quantization can exploit the inter-symbol dependencies and reduce the redundancy in the input data.
  - Vector quantization can achieve higher compression ratios and lower distortion than scalar quantization for the same number of bits per input tuple.
  - Vector quantization can better adapt to the local characteristics of the input data and preserve the perceptual quality of the output.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the Linde-Buzo-Gray algorithm for vector quantization.

### The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in the input space .
- Vector quantization is a technique to compress data by mapping each input vector to the nearest codeword in the codebook .
- Vector quantization has advantages over scalar quantization, such as:
  - Higher compression ratio, as each codeword can represent multiple input vectors.
  - Lower distortion, as each codeword can capture the correlation among the components of the input vector.
  - Higher flexibility, as the codebook can be adapted to the characteristics of the input data.
- The LBG algorithm is similar to the k-means method in data clustering .
- The LBG algorithm works as follows  :
  - Start with a single codeword, which is the centroid of the training set of input vectors.
  - Split each codeword into two slightly perturbed versions, doubling the size of the codebook.
  - Assign each input vector to the nearest codeword, forming clusters around each codeword.
  - Update each codeword by computing the centroid of its cluster, minimizing the distortion within each cluster.
  - Repeat the splitting, assignment and update steps until the desired codebook size is reached or the distortion is below a threshold.
  - Return the final codebook as the output of the algorithm.

Here is a diagram to illustrate the LBG algorithm:

```markdown
| Training set | Initial codebook | Splitting | Assignment | Update |
|:------------:|:----------------:|:---------:|:----------:|:------:|
|              |                  |           |            |        |
|     x1       |        c1        |    c1     |     x1     |   c1'  |
|              |                  |    |      |     |      |    |   |
|     x2       |                  |    v      |     v      |    v   |
|              |                  |   c2      |     x2     |   c2'  |
|              |                  |           |            |        |
|     x3       |                  |           |     x3     |   c1'  |
|              |                  |           |     |      |    |   |
|     x4       |                  |           |     v      |    v   |
|              |                  |           |     x4     |   c2'  |
|              |                  |           |            |        |
```




### Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the final codebook vectors.
- The advantage of TSVQ is that it can be represented by a binary tree, which reduces the storage cost, encoding rate, and quantization time compared to a full-search vector quantizer.
- The encoding process of TSVQ is fast and simple, as it only requires a root-to-leaf traversal of the tree to find the closest codebook vector to the input vector .
- The decoding process of TSVQ is also fast and simple, as it only requires the binary code of the leaf node to reconstruct the output vector.
- The design of TSVQ involves finding the optimal tree structure and the optimal codebook vectors that minimize the expected distortion subject to a cost function.
- One way to design TSVQ is to use a top-down approach, where the input space is recursively split into two subspaces until a desired number of codebook vectors is reached.
- Another way to design TSVQ is to use a bottom-up approach, where the codebook vectors are initially chosen randomly and then merged into larger regions until a desired tree structure is obtained.
- TSVQ can be applied to various types of data, such as speech, image, and video, to achieve high compression ratios and low distortion.

: Design and performance of tree-structured vector quantizers, ScienceDirect, 1994
: Vector Quantization, McMaster University, n.d.



### Structured Vector Quantizers

- Vector quantization is a technique that compresses data by representing a set of input vectors by a smaller set of code vectors, called a codebook.
- The codebook is designed to minimize the distortion between the input vectors and their corresponding code vectors, which are assigned by a mapping function called an encoder.
- The encoder can be implemented as a lookup table, a nearest neighbor search, or a tree search, depending on the structure of the codebook.
- Structured vector quantizers are vector quantizers that impose some constraints or regularities on the codebook or the encoder, to reduce the complexity, storage, or encoding time of the vector quantization process.
- Some examples of structured vector quantizers are:

  - Tree-structured vector quantizers (TSVQ), which use a hierarchical partitioning of the input space, such that each node of the tree corresponds to a cluster of input vectors and a code vector. The encoder performs a top-down search along the tree to find the closest code vector to the input vector. TSVQ can reduce the encoding time and storage cost compared to a full-search vector quantizer, but may introduce some distortion due to the tree constraint .
  - Lattice vector quantizers (LVQ), which use a regular geometric arrangement of code vectors, such as a lattice, to cover the input space. The encoder can use a fast algorithm to find the closest lattice point to the input vector, without storing the codebook explicitly. LVQ can achieve optimal rate-distortion performance for some classes of input vectors, such as Gaussian or Laplacian sources.
  - Product vector quantizers (PVQ), which decompose the input vector into smaller subvectors, and quantize each subvector independently using a separate codebook. The encoder can use a simple concatenation of the subvector indices to represent the input vector. PVQ can reduce the storage cost and the complexity of the codebook design, but may introduce some distortion due to the independence assumption.

- Structured vector quantizers have some advantages over scalar quantizers, which operate on single variables, such as:

  - Higher compression ratio, since vector quantizers can exploit the correlation among the variables in the input vector, and reduce the redundancy in the representation.
  - Lower distortion, since vector quantizers can approximate the input vectors more accurately by using a smaller number of bits per vector, compared to scalar quantizers that use the same number of bits per variable.
  - Higher flexibility, since vector quantizers can adapt to different types of input vectors, such as images, speech, or video, by using different codebook structures, encoding algorithms, or distortion measures.

