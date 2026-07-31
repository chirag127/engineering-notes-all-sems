

## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data or information without losing its quality or meaning.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the original data exactly and allow its reconstruction from the compressed data. Examples of lossless compression techniques are Huffman coding, run-length encoding, Lempel-Ziv algorithm, etc.
- Lossy compression techniques discard some information from the original data and produce an approximation of it. Examples of lossy compression techniques are JPEG, MP3, MPEG, etc.
- Compression techniques can be applied to different types of data, such as text, images, audio, video, etc.
- Compression techniques can have various benefits, such as saving storage space, reducing transmission time, improving performance, etc.



### Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values are more frequent than others and can be represented with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and lossless audio formats .
- Lossless compression can reduce the file size by 50% or more, depending on the data and the compression algorithm.
- Some common lossless compression algorithms are Huffman coding, arithmetic coding, run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, and deflate algorithm.
- Lossless compression is different from lossy compression, which discards some data in the compression process and produces a lower quality output that cannot be restored to the original.
- Lossy compression is more suitable for applications that can tolerate some loss of information, such as images, video, and audio.



### Lossy Compression

- Lossy compression is a technique that reduces the file size of data by discarding some of the original information.
- Lossy compression is typically used for multimedia files, such as images, audio and video, where some loss of quality is acceptable.
- Lossy compression algorithms are based on the principle of perceptual coding, which exploits the limitations of human perception to remove or reduce the less important or less noticeable data.
- Some examples of lossy compression formats are JPEG, MP3, MPEG, GIF, etc.

#### Advantages of Lossy Compression

- Lossy compression can achieve very high compression ratios, which means very small file sizes and lots of storage space saved.
- Lossy compression can improve the performance and speed of data transmission, especially over the internet or other networks.
- Lossy compression can support a wide range of applications and devices, as there are many tools, plugins and software that can handle lossy formats.

#### Disadvantages of Lossy Compression

- Lossy compression can degrade the quality of the data, as some of the original information is lost and cannot be restored.
- Lossy compression can introduce artifacts, such as noise, distortion, blurring, etc., that can affect the appearance or sound of the data.
- Lossy compression can limit the flexibility and functionality of the data, as some features or operations may not be possible or may produce undesirable results on lossy formats.



# Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or transforming the data into a more compact representation.
- Compression techniques can improve the efficiency of data storage, transmission, and processing, but they may also introduce some trade-offs such as complexity, distortion, or loss of information.
- To evaluate the performance of compression techniques, we need to use some measures or metrics that can quantify the benefits and costs of compression.
- Some common measures of performance for compression techniques are:

  - Compression ratio (CR): The ratio of the original data size to the compressed data size. It indicates how much the data is reduced by compression. A higher CR means a higher compression efficiency.
  - Compression factor (CF): The inverse of the compression ratio. It indicates how many times the original data can fit into the compressed data. A lower CF means a higher compression efficiency.
  - Bit rate (BR) or bits per symbol (bps): The average number of bits used to represent each symbol (such as a character, a pixel, or a sample) in the compressed data. It indicates the compactness of the compressed data. A lower BR or bps means a higher compression efficiency.
  - Distortion or error: The difference between the original data and the reconstructed data after compression and decompression. It indicates the quality or fidelity of the compressed data. A lower distortion or error means a higher compression quality.
  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible signal power to the noise power caused by compression. It is often used to measure the distortion or error of image or audio compression. It is expressed in decibels (dB). A higher PSNR means a higher compression quality.
  - Mean squared error (MSE): The average of the squared differences between the original data and the reconstructed data. It is another way to measure the distortion or error of compression. A lower MSE means a higher compression quality.
  - Root mean squared error (RMSE): The square root of the MSE. It is more intuitive than MSE as it has the same unit as the original data. A lower RMSE means a higher compression quality.
  - Structural similarity index (SSIM): A measure of the perceptual similarity between the original data and the reconstructed data. It considers the luminance, contrast, and structure of the data. It ranges from 0 to 1. A higher SSIM means a higher compression quality.
  - Multi-scale structural similarity index (MS-SSIM): An extension of SSIM that considers the similarity at different scales or resolutions of the data. It is more suitable for image or video compression. It also ranges from 0 to 1. A higher MS-SSIM means a higher compression quality.
  - Accuracy: The percentage of the original data that is correctly preserved or recovered by the compression technique. It is often used to measure the performance of lossless compression or specific application-oriented compression. A higher accuracy means a higher compression quality.



### Modeling and coding for data compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression preserves the exact original data, while lossy compression discards some data that is deemed less important or perceptible.
- Modeling and coding are the two levels to compress data :
  - In the first level, the data will be analyzed for any redundant information and extract it to develop a model.
  - In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique.
- Modeling can be done using one of two different types of methods: statistical or dictionary-based .
  - Statistical modeling reads in and encodes a single symbol at a time using the probability of that character’s appearance.
  - Dictionary-based modeling uses a single code to replace strings of symbols that are stored in a dictionary.
- Coding can be done using one of two different types of methods: entropy coding or arithmetic coding .
  - Entropy coding assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, based on the entropy or information content of the data.
  - Arithmetic coding assigns a single code to the entire data, based on the cumulative probability of the symbols, and can achieve optimal compression.
- Data compression can also be done using deep learning techniques, such as Bit-Swap, which uses latent variable models and bits-back coding to learn the probability distribution of the data and encode it efficiently.



### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be reconstructed exactly from the compressed data.
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of information or uncertainty in a data source. The lower the entropy, the more predictable and compressible the data is.
- Entropy can be calculated using different models of the data source, such as the zero-order model (assuming each symbol is independent and identically distributed), the first-order model (assuming each symbol depends only on the previous one), or higher-order models (assuming more complex dependencies).
- The entropy of a data source is the lower bound for the average number of bits per symbol needed to encode the data. No lossless compression scheme can achieve a compression ratio lower than the entropy of the data source.
- Lossless compression schemes can be classified into two categories: statistical and dictionary-based. Statistical schemes use a model of the data source to assign variable-length codes to the symbols, such that the more frequent symbols have shorter codes and the less frequent symbols have longer codes. Dictionary-based schemes use a predefined or adaptive dictionary of strings to replace the original data with shorter codes that refer to the dictionary entries.



### A brief introduction to information theory for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding theorems  .
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be stored or transmitted.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared between two random variables.
- Information theory also studies the limitations and possibilities of communication systems, such as how much information can be reliably transmitted over a noisy channel, or how to efficiently encode and compress information for storage or transmission  .
- Information theory has applications in many fields, such as cryptography, data compression, error correction, signal processing, machine learning, and neuroscience   .
- Information theory overlaps heavily with communication theory, but it is more oriented toward the fundamental limitations on the processing and communication of information and less oriented toward the detailed operation of particular devices.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of Models for the notes of the Unit 1 - Compression Techniques.

### Models

- A model is a representation of the source data that captures its statistical properties and allows for efficient compression.
- A model can be either static or adaptive.
- A static model is fixed and does not change during the compression process. It is usually based on some prior knowledge or analysis of the source data.
- An adaptive model is updated dynamically based on the data that has been processed so far. It can adapt to the changing characteristics of the source data and achieve better compression performance.
- Some examples of models are:
  - Uniform model: This model assumes that all symbols in the source data have equal probability of occurrence. It is simple but not very effective for most real-world data.
  - Huffman model: This model assigns variable-length codes to the symbols based on their frequencies of occurrence. It is optimal for a given set of symbol probabilities and guarantees a minimum average code length.
  - Arithmetic model: This model encodes the entire source data as a single fractional number in the range [0, 1). It assigns subintervals of the range to the symbols based on their probabilities and recursively subdivides the intervals as more symbols are processed. It can achieve near-optimal compression for any source data.
  - Dictionary model: This model uses a predefined or dynamically constructed dictionary of strings to compress the source data. It replaces repeated occurrences of strings with references to their dictionary entries. It can exploit the structure and redundancy of the source data and achieve high compression ratios.



### Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Statistical models**: Statistical models are based on the assumption that the source data is generated by a random process with some known or estimable probability distribution. The goal of statistical models is to assign shorter codes to more probable symbols or sequences of symbols, and longer codes to less probable ones. This way, the average code length is minimized and the compression ratio is maximized. Some examples of statistical models are:

  - **Entropy models**: Entropy models measure the amount of information or uncertainty in the source data using the concept of entropy. Entropy is defined as the average number of bits needed to encode one symbol from the source. The lower the entropy, the more predictable the source is, and the higher the compression ratio can be achieved. Entropy models are used to design optimal prefix codes, such as Huffman codes and arithmetic codes, that achieve the entropy bound.
  - **Markov models**: Markov models are a special type of entropy models that assume that the source data is generated by a Markov process, where the probability of the next symbol depends only on the previous k symbols, where k is a fixed parameter. Markov models are useful for text compression, where the probability of the next letter is heavily influenced by the preceding letters. Markov models are also known as finite context models, and they can be used to design adaptive codes that adjust to the changing statistics of the source.
  - **Dictionary models**: Dictionary models are based on the idea of replacing frequently occurring sequences of symbols with shorter codes from a predefined or dynamically constructed dictionary. Dictionary models are suitable for compressing data that contains repetitions or patterns, such as natural language texts or genomic sequences. Some examples of dictionary models are Lempel-Ziv (LZ) codes, such as LZ77 and LZ78, and Burrows-Wheeler transform (BWT).

- **Structural models**: Structural models are based on the assumption that the source data has some inherent structure or organization that can be exploited for compression. The goal of structural models is to identify and extract the relevant features or components of the data, and encode them separately using appropriate methods. Some examples of structural models are:

  - **Transform models**: Transform models are based on the idea of applying a mathematical transformation to the source data that converts it into a different domain, where the data is more compact or sparse. Transform models are useful for compressing data that has high correlation or redundancy, such as images or audio signals. Some examples of transform models are discrete cosine transform (DCT), discrete wavelet transform (DWT), and Fourier transform (FT).
  - **Predictive models**: Predictive models are based on the idea of using a predictor function to estimate the next symbol or sample from the source data based on the previous ones, and encoding the difference or error between the actual and predicted values. Predictive models are useful for compressing data that has high temporal or spatial correlation, such as video or speech signals. Some examples of predictive models are differential pulse-code modulation (DPCM), delta modulation (DM), and linear predictive coding (LPC).
  - **Fractal models**: Fractal models are based on the idea of using self-similarity or recursion to describe the source data using a set of rules or parameters. Fractal models are useful for compressing data that has complex or irregular shapes or patterns, such as natural images or textures. Some examples of fractal models are iterated function systems (IFS) and partitioned iterated function systems (PIFS).



# Probability models for data compression

- A probability model is a mathematical description of the statistical properties of a source of data.
- A probability model assigns a probability to each possible symbol or sequence of symbols that the source can generate.
- A probability model can be used to measure the information content and the entropy of the source, which are related to the optimal compression rate that can be achieved.
- A probability model can also be used to design a coding scheme that assigns shorter codes to more probable symbols or sequences, and longer codes to less probable ones, thus reducing the average code length and achieving compression.
- There are different types of probability models, depending on the assumptions and the complexity of the source. Some common examples are:

  - Uniform model: This model assumes that all symbols in the alphabet are equally probable, and assigns the same probability to each one. This model is simple but often unrealistic, as most sources have some degree of non-uniformity or structure in their data.
  - Bernoulli model: This model assumes that the source generates a binary sequence of independent and identically distributed (i.i.d.) bits, each with a fixed probability of being 1 or 0. This model is also simple but can capture some degree of non-uniformity in the data.
  - Geometric model: This model assumes that the source generates a sequence of i.i.d. symbols from a finite alphabet, each with a fixed probability of being the last symbol in the sequence. This model can capture the length distribution of the data, and is useful for compressing sources that have variable-length symbols or segments, such as text or speech.
  - Poisson model: This model assumes that the source generates a sequence of i.i.d. symbols from a finite alphabet, each with a fixed probability of being the first symbol in a new segment. The number of symbols in each segment follows a Poisson distribution, which depends on a parameter called the rate. This model can capture the frequency distribution of the data, and is useful for compressing sources that have variable-length segments with different probabilities, such as images or video.
  - Markov model: This model assumes that the source generates a sequence of symbols from a finite alphabet, where the probability of each symbol depends only on the previous symbol or a fixed number of previous symbols. This model can capture the local structure or correlation of the data, and is useful for compressing sources that have patterns or regularities, such as text or speech.
  - Context-based model: This model assumes that the source generates a sequence of symbols from a finite alphabet, where the probability of each symbol depends on the previous symbols or some other information that defines the context. This model can capture the global structure or variation of the data, and is useful for compressing sources that have different characteristics in different regions or situations, such as images or video.



# Markov models for data compression

- Markov models are mathematical models that describe the probability of a system transitioning from one state to another, based on the current state and a set of rules.
- Markov models can be used to model the statistical properties of natural language, images, music, and other types of data that exhibit patterns and dependencies.
- Markov models can be used for data compression by predicting the next symbol in a data stream, based on the previous symbols and their probabilities, and encoding the prediction error with a suitable coding scheme.
- Markov models can be classified into different types, depending on the order of the model (how many previous symbols are considered), the structure of the model (how the states and transitions are defined), and the adaptivity of the model (how the probabilities are updated based on the data).
- Some examples of Markov models for data compression are:

  - Markov chain models: These are the simplest type of Markov models, where the states are the symbols themselves, and the transitions are the probabilities of each symbol following another. The order of the model is the number of previous symbols that determine the current state. For example, a first-order Markov chain model considers only the last symbol, while a second-order Markov chain model considers the last two symbols.
  - Hidden Markov models: These are Markov models where the states are not directly observable, but are inferred from the symbols. The transitions are the probabilities of each state following another, and the emissions are the probabilities of each symbol being generated by each state. Hidden Markov models can capture more complex dependencies and patterns than Markov chain models, but require more parameters and computation.
  - Variable-order Markov models: These are Markov models where the order of the model is not fixed, but varies depending on the context. For example, a variable-order Markov model can switch from a first-order to a second-order model, if the data shows a strong dependency between two symbols. Variable-order Markov models can adapt to the local characteristics of the data, and achieve better compression than fixed-order models.
  - Dynamic Markov compression: This is a data compression algorithm that uses a dynamic Markov model, which is a Markov model that is constructed and updated on the fly, based on the data. The algorithm predicts the next bit in the data stream, based on the previous bits and their probabilities, and encodes the prediction error with arithmetic coding. Dynamic Markov compression is similar to prediction by partial matching (PPM), but operates on bits rather than bytes, which makes it slower but gives slightly better compression.



### Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub>.
- A composite source model is useful for data compression because it can capture the variations and dependencies in the data more accurately than a single model.
- A composite source model can be used to compress different types of data, such as text, images, audio, video, etc.
- A composite source model can be combined with different coding techniques, such as Huffman coding, arithmetic coding, run-length encoding, etc., to achieve optimal or near-optimal compression ratios.
- A composite source model can be illustrated by the following diagram:

```
+-----+     +-----+     +-----+
| S_1 |     | S_2 |     | S_n |
+-----+     +-----+     +-----+
   |           |           |
   +-----------+-----------+
               |
               v
            +-----+
            | M_1 |
            +-----+
               |
               v
            +-----+
            | M_2 |
            +-----+
               |
               v
            +-----+
            | M_n |
            +-----+
               |
               v
            +-----+
            |Switch|
            +-----+
               |
               v
            +-----+
            |Output|
            +-----+
```



### Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact original data, while lossy compression techniques discard some data to achieve higher compression ratios.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): This technique replaces consecutive identical symbols with a symbol and a count. For example, the string "AAAAABBBBCCCC" can be compressed as "A5B4C4".
  - Huffman coding: This technique assigns variable-length codes to symbols based on their frequencies. The most frequent symbols get the shortest codes, while the least frequent symbols get the longest codes. For example, if the symbol "A" occurs 80 times, "B" occurs 10 times, and "C" occurs 10 times in a data set, then the Huffman codes can be "A: 0, B: 10, C: 11".
  - Lempel-Ziv-Welch (LZW) coding: This technique builds a code table of sequences of symbols that occur in the data. As the encoding continues, LZW identifies repeated sequences in the data and adds them to the code table. For example, if the data contains the sequence "ABABABAB", then LZW can add "AB" and "ABAB" to the code table and encode the sequence as "ABAB256".
- Some common lossy compression techniques are:
  - Discrete cosine transform (DCT): This technique transforms a block of data (such as an image or a video frame) into a set of frequency coefficients. The coefficients that represent high frequencies are usually less important than the coefficients that represent low frequencies, so they can be quantized or discarded to reduce the size of the data.
  - Motion estimation and compensation (ME/MC): This technique exploits the temporal redundancy in video data by predicting the current frame from the previous frame. The prediction error (or residual) is then encoded using DCT or other methods. ME/MC can reduce the amount of data that needs to be transmitted or stored for video data.
  - Entropy coding: This technique compresses the data by removing the statistical redundancy in the data. Entropy coding can be combined with other techniques, such as DCT or ME/MC, to achieve better compression ratios. Some examples of entropy coding are arithmetic coding and asymmetric numeral systems (ANS).



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  `sum_{i=1}^n 2^{-l_i} <= 1`

- The Kraft inequality can be generalized to any code alphabet with size r, where r is the number of code symbols. In that case, the inequality becomes:

  `sum_{i=1}^n r^{-l_i} <= 1`

- The Kraft inequality can also be used to prove the existence of a uniquely decodable code with given codeword lengths, but not necessarily prefix-free. However, such a code may not be instantaneous.



### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of variable-length code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images, MP3 for music, and Huffman coding for text .
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- The length of a codeword is equal to the depth of the corresponding leaf node in the tree.
- The expected length of a prefix code is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The optimal prefix code for a given probability distribution is the one that minimizes the expected length.
- One way to construct an optimal prefix code is to use Huffman's algorithm, which builds the tree from the bottom up by merging the two least probable symbols at each step.
- Another way to construct a prefix code is to use a universal code, which is a prefix code that works well for any monotonic probability distribution, without knowing the exact probabilities.
- Some examples of universal codes are Elias gamma code, Elias delta code, Fibonacci code, and Golomb code.



## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence.

The main steps of the algorithm are:

- Create a frequency table that counts the number of occurrences of each symbol in the data.
- Create a priority queue of nodes, where each node represents a symbol and its frequency. The nodes with the lowest frequencies have the highest priority.
- While the queue has more than one node, do the following:
  - Dequeue the two nodes with the highest priority (lowest frequency) from the queue.
  - Create a new internal node with the sum of the frequencies of the two nodes as its frequency, and the two nodes as its left and right children.
  - Enqueue the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree.
- Traverse the Huffman tree and assign codes to the symbols. The code of a symbol is the sequence of bits that corresponds to the path from the root to the leaf node of the symbol. A left branch is represented by 0 and a right branch by 1.

The Huffman coding algorithm has the following properties:

- It is a lossless compression method, meaning that no information is lost in the process of encoding and decoding.
- It is a prefix-free code, meaning that no code is a prefix of another code. This ensures that the codes can be uniquely decoded.
- It is an optimal code, meaning that it minimizes the average code length for a given set of symbols and frequencies. No other code can achieve a smaller average code length.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the minimum expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The expected codeword length is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The variance of the codeword length is the weighted average of the squared deviations of the codeword lengths from the expected codeword length, where the weights are the probabilities of the symbols.
- The variance of the codeword length measures the variability or dispersion of the codeword lengths around the mean.
- A minimum variance Huffman code is a Huffman code that minimizes the variance of the codeword length, subject to the constraint that the code is optimal (minimum redundancy).
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in nonincreasing order of probability.
  - If there are more than two symbols, merge the two symbols with the smallest probabilities into a new symbol with the sum of their probabilities, and repeat until there are only two symbols left.
  - Assign the codeword 0 to the symbol with the larger probability and the codeword 1 to the symbol with the smaller probability.
  - For each merged symbol, split it into its original symbols and append 0 to the codeword of the symbol with the larger probability and 1 to the codeword of the symbol with the smaller probability, and repeat until all the symbols are restored.
- A minimum variance Huffman code has the property that the codeword lengths are as close as possible to the entropy of the source, which is the lower bound on the expected codeword length.
- A minimum variance Huffman code can also be seen as a length-limited Huffman code, where the length of each codeword is restricted to be less than or equal to a given constant.
- A length-limited Huffman code can be constructed by using the package-merge algorithm, which is a generalization of the standard Huffman algorithm that allows merging more than two symbols at a time.



### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on the Huffman coding algorithm, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data. 

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or non-stationary (i.e., changing over time).
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication for the code.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than Huffman coding, since the code tree has to be modified frequently.
- It may not perform well for small or sparse data sets, since the code may not have enough time to converge to the optimal one.
- It may be vulnerable to noise or errors in the transmission, since a single corrupted bit can affect the decoding of the entire data.

There are different algorithms for implementing adaptive Huffman coding, such as the FGK algorithm and the Vitter algorithm. They differ in how they update the code tree and how they handle the special case of new symbols that have not been seen before.  

The basic steps of adaptive Huffman coding are:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet.
- For each symbol in the data:
  - If the symbol is new, output the code for the NYT node, followed by a fixed-length code for the symbol (e.g., its ASCII code). Then, split the NYT node into two nodes: a new NYT node and a leaf node for the symbol, with a frequency of 1. The new nodes become the children of the old NYT node, and the old NYT node becomes an internal node.
  - If the symbol is not new, output the code for its leaf node in the code tree. Then, increment the frequency of the node by 1, and update the code tree to maintain the Huffman property (i.e., the nodes with lower frequencies are farther from the root than the nodes with higher frequencies). This may involve swapping the node with another node in the same level or higher, and updating the frequencies of the nodes along the path from the node to the root.
- Repeat until all the symbols are processed.

The following diagram shows an example of adaptive Huffman coding for the string "ABRACADABRA". The code tree is updated after each symbol, and the codes for the symbols are shown below the tree. 

Adaptive Huffman coding example

The total length of the encoded data is 40 bits, compared to 88 bits for the original data (assuming 8 bits per symbol). The compression ratio is 0.45.



### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree that represents the optimal prefix code for the given data.
- The steps of the algorithm are as follows:
  - Create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and the sum of their frequencies as the frequency.
    - Add the new node to the queue.
  - The remaining node is the root of the tree and the code for each symbol is the path from the root to the leaf node.
- The Huffman coding algorithm can be implemented using a heap data structure to store the nodes in the priority queue.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video.
- The Huffman coding algorithm can achieve optimal compression for data that follows a certain probability distribution, such as the Zipf's law.
- The Huffman coding algorithm has some limitations, such as:
  - It requires the knowledge of the frequency of each symbol in the data, which may not be available or may change over time.
  - It may not be efficient for data that has a uniform or skewed distribution, as the codes may be too long or too similar.
  - It may not be suitable for adaptive compression, as the tree needs to be updated frequently.



Hello, I am Sydney, your AI assistant. I can help you with the encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression. Here is a summary of the main steps:

### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The algorithm works as follows  :
  - Create a leaf node for each character and add it to the priority queue.
  - While there is more than one node in the queue:
    - Remove the two nodes of the highest priority (the lowest frequency) from the queue.
    - Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.
    - Add the new node to the queue.
  - The remaining node is the root node and the tree is complete.
  - Traverse the tree from the root to the leaves and assign a bit (0 or 1) to each edge. The assigned bits to each edge form the Huffman code for each character.
- To encode a message, replace each character by its corresponding Huffman code and concatenate the codes.
- To decode a message, start from the root of the tree and follow the bits until reaching a leaf node, which is the decoded character. Repeat this process until the end of the message.



### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- Huffman coding is an efficient method of compressing data without losing information.

The decoding procedure for the Huffman coding algorithm is as follows:

- Step 1: Construct a Huffman tree from the given frequency table of characters and their codes. The Huffman tree is a binary tree where each leaf node represents a character and its code, and each internal node represents the combined frequency of its children. The root node has the total frequency of all the characters.
- Step 2: Traverse the Huffman tree from the root node to the leaf node that corresponds to the first bit of the encoded message. If the bit is 0, move to the left child; if the bit is 1, move to the right child.
- Step 3: When a leaf node is reached, output the character that is stored in that node and return to the root node.
- Step 4: Repeat steps 2 and 3 until all the bits of the encoded message are processed.

Example:

Suppose the frequency table of characters and their codes is as follows:

| Character | Frequency | Code |
|-----------|-----------|------|
| a         | 5         | 0    |
| b         | 9         | 101  |
| c         | 12        | 100  |
| d         | 13        | 111  |
| e         | 16        | 1101 |
| f         | 45        | 1100 |

The Huffman tree for this table is:

```
        100
       /   \
      45   55
     / \   / \
    f  10 25  30
      / \ / \ / \
     a  b c d e  g
```

The encoded message is: 0110111010001001110111101100

The decoding procedure is:

- Start from the root node and read the first bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character f. Output f and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 30. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character e. Output e and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is an internal node with the frequency 25. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character c. Output c and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is an internal node with the frequency 25. Read the next bit of the encoded message: 1. Move to the right child.
- The right child is a leaf node with the character b. Output b and return to the root node.
- Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character f. Output f and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read



### Golomb codes

Golomb codes are a type of parameterized codes that are suitable for encoding values that follow a geometric distribution. They are often used in data compression applications, such as lossless image compression and entropy coding.

The main idea of Golomb coding is to divide the input value x into two parts: q, the quotient of x divided by a parameter M, and r, the remainder of x modulo M. The quotient q is encoded in unary code, which consists of q ones followed by a zero. The remainder r is encoded in a binary code, which depends on the value of M.

There are two cases for encoding the remainder r:

- If M is a power of 2, say M = 2^n, then r can be encoded in a fixed-length n-bit binary code. For example, if M = 4, then r can be 0, 1, 2, or 3, and can be encoded as 00, 01, 10, or 11, respectively.
- If M is not a power of 2, then r can be encoded in a variable-length binary code, which uses a prefix code to avoid ambiguity. One way to construct such a code is to use a truncated binary code, which divides the possible values of r into two subranges: the lower subrange, which contains floor(M/2) values, and the upper subrange, which contains ceil(M/2) values. The lower subrange values are encoded in a fixed-length floor(log2(M)) bit binary code, while the upper subrange values are encoded in a fixed-length ceil(log2(M)) bit binary code, with a leading 1 to distinguish them from the lower subrange values. For example, if M = 5, then r can be 0, 1, 2, 3, or 4, and can be encoded as 00, 01, 10, 110, or 111, respectively.

The parameter M can be chosen to optimize the compression performance, depending on the probability distribution of the input values. A common choice is to use M = floor(-1/log2(1-p)), where p is the probability of the most frequent value. This minimizes the expected codeword length for a geometric distribution with parameter p.

Here is an example of Golomb coding for a source x with geometric distribution, with parameter p(0) = 0.2, using Golomb code with M = 3.

| x | q | r | q (unary) | r (binary) | Codeword |
|---|---|---|-----------|------------|----------|
| 0 | 0 | 0 | 0         | 00         | 000      |
| 1 | 0 | 1 | 0         | 01         | 001      |
| 2 | 0 | 2 | 0         | 10         | 010      |
| 3 | 1 | 0 | 10        | 00         | 1000     |
| 4 | 1 | 1 | 10        | 01         | 1001     |
| 5 | 1 | 2 | 10        | 10         | 1010     |
| 6 | 2 | 0 | 110       | 00         | 11000    |
| 7 | 2 | 1 | 110       | 01         | 11001    |
| 8 | 2 | 2 | 110       | 10         | 11010    |
| 9 | 3 | 0 | 1110      | 00         | 111000   |
| 10| 3 | 1 | 1110      | 01         | 111001   |
| 11| 3 | 2 | 1110      | 10         | 111010   |

The average codeword length for this example is 3.2 bits, which is close to the entropy of the source, which is -log2(0.2) = 2.32 bits.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on Rice codes for the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

### Rice codes

- Rice codes are a subset of Golomb codes, which are a family of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for some distributions.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a non-negative integer x using Rice codes, the following steps are performed :
  - Divide x by m and write the quotient in unary code, i.e., a sequence of 1s followed by a 0.
  - Write the remainder of x modulo m in binary code, using k bits.
  - Concatenate the unary and binary codes to form the Rice code for x.
- For example, if k = 2 and x = 9, then the Rice code for x is 1110 01, where 1110 is the unary code for 9/4 = 2 and 01 is the binary code for 9 mod 4 = 1.
- To decode a Rice code, the following steps are performed :
  - Read the unary code until a 0 is encountered and count the number of 1s, which is the quotient q.
  - Read the next k bits and interpret them as a binary number, which is the remainder r.
  - Multiply q by m and add r to obtain the original integer x.
  - For example, if k = 2 and the Rice code is 1110 01, then the decoded integer is 2 * 4 + 1 = 9.
- Rice codes are generally used to encode entropy in audio/video codecs, where the data often has a Laplacian distribution.
- Rice codes are also suitable for encoding small differences between consecutive samples, such as in differential pulse-code modulation (DPCM).
- Rice codes are adaptive, meaning that the parameter k can be changed according to the statistics of the data.
- Rice codes have a coding efficiency of 1 + (1 + k)/m bits per symbol, which approaches 1 bit per symbol as k approaches 0.
- Rice codes are optimal for geometric distributions with parameter p = 1/2^k^, where the probability of x is p * (1 - p)^x^.



### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall codes are a form of entropy coding used for lossless data compression.
- Tunstall codes are based on the idea of parsing a stochastic source with codewords of variable length and encoding them with codewords of fixed length.
- Tunstall codes are similar to Lempel-Ziv codes, but they use a predefined dictionary instead of building it dynamically from the input data.
- Tunstall codes have the advantage of being simpler and faster than Lempel-Ziv codes, but they have the disadvantage of requiring more memory and being less adaptive to the source statistics.
- Tunstall codes can be constructed by using a Huffman tree and pruning it to a desired depth, such that each leaf node corresponds to a fixed-length codeword.
- Tunstall codes can achieve the entropy of the source as the codeword length approaches infinity, but they are suboptimal for finite codeword lengths.
- Tunstall codes are suitable for sources with low entropy and high correlation, such as run-length encoded data.



### Applications of Huffman coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or probability of occurrence. The more frequent a data value is, the shorter its code will be, and vice versa. This way, the data can be represented using fewer bits than the original fixed-length codes.

Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel, reducing the bandwidth and transmission time required.
- **Conventional compression formats**: Huffman coding is often used by compression formats like PKZIP, GZIP, BZIP2, etc. to compress the data before storing it in a file, reducing the disk space and memory usage required .
- **Multimedia codecs**: Huffman coding is also used by multimedia codecs like JPEG, PNG, and MP3 to compress the image or audio data, reducing the file size and quality loss. Huffman coding is usually combined with other techniques like run-length encoding, differential encoding, quantization, etc. to achieve higher compression ratios  .
- **Error correction**: Huffman coding can also be used to encode the error correction codes that are added to the data to detect and correct errors during transmission or storage. Huffman coding can reduce the overhead of the error correction codes by assigning shorter codes to the more probable error patterns.



### Lossless Image Compression Using Huffman Coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding are:

  1. Create a frequency table that counts the number of occurrences of each symbol in the image.
  2. Sort the symbols in the frequency table in ascending order of frequency and consider them as leaf nodes of a binary tree.
  3. While there is more than one node in the tree, merge the two nodes with the lowest frequency and create a new parent node with the sum of their frequencies. Assign 0 to the left branch and 1 to the right branch of the parent node.
  4. Repeat step 3 until there is only one node left in the tree, which is the root node. The tree is called the Huffman tree.
  5. Traverse the Huffman tree from the root to the leaf nodes and assign a binary code to each symbol by concatenating the branch labels along the path.
  6. Replace each symbol in the image with its corresponding binary code and output the compressed image file.

- The advantages of Huffman coding are:

  - It is optimal, meaning that it achieves the minimum possible average code length for a given source distribution.
  - It is simple and efficient to implement and decode.
  - It is widely used in various applications, such as JPEG, ZIP, MP3, etc.

- The disadvantages of Huffman coding are:

  - It requires the knowledge of the source distribution or the frequency table, which may not be available or may change over time.
  - It may not be optimal for sources with non-integer or fractional probabilities, as it can only assign integer code lengths.
  - It may not be suitable for sources with large alphabets, as it can generate very long codes for some symbols.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.
- The most frequent character gets the smallest code and the least frequent character gets the largest code.
- Huffman coding works by creating a binary tree that represents the codes and frequencies of the characters.
- The tree is constructed by taking the two least frequent characters and making them the children of a new node with the sum of their frequencies as the parent frequency.
- The process is repeated until there is only one node left, which is the root of the tree.
- The codes are generated by traversing the tree from the root to the leaves and assigning 0 or 1 to each edge.
- The code of a character is the sequence of bits along the path from the root to the leaf corresponding to that character.
- To compress a text file, the algorithm first scans the file and counts the frequencies of each character.
- Then, it builds the Huffman tree and generates the codes for each character.
- Finally, it replaces each character in the file with its code and writes the compressed file along with the tree information.
- To decompress a compressed file, the algorithm first reads the tree information and reconstructs the Huffman tree.
- Then, it reads the compressed file bit by bit and follows the path in the tree until it reaches a leaf node, which is the decoded character.
- It repeats this process until the end of the file and writes the decompressed file.



### Audio Compression

Audio compression is the process of reducing the size of an audio file by removing or encoding redundant or irrelevant information. Audio compression can be either lossy or lossless, depending on whether the original data can be perfectly reconstructed from the compressed file or not.

### The Huffman Coding Algorithm

The Huffman coding algorithm is a method of lossless data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data. The symbols with higher frequencies are assigned shorter codes, while the symbols with lower frequencies are assigned longer codes. The Huffman coding algorithm can be applied to any type of data, such as text, images, or audio.

The Huffman coding algorithm consists of the following steps:

- Create a frequency table that counts the number of occurrences of each symbol in the data.
- Create a priority queue that contains the symbols as nodes, sorted by their frequencies in ascending order.
- While the queue has more than one node, do the following:
  - Dequeue the two nodes with the lowest frequencies and create a new node that has the sum of their frequencies as its frequency and the two nodes as its left and right children.
  - Enqueue the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree, which represents the optimal prefix code for the data.
- Traverse the Huffman tree and assign a binary code to each symbol by appending a 0 for every left branch and a 1 for every right branch.

The Huffman coding algorithm can achieve optimal compression for data that follows a certain probability distribution, such as the Zipf's law. The Huffman coding algorithm is used in many applications, such as JPEG and MPEG-2.



## Unit 3 - Coding a sequence

A sequence is a set of ordered items that follow a certain pattern or rule. For example, the sequence of even numbers is 2, 4, 6, 8, and so on. The sequence of Fibonacci numbers is 1, 1, 2, 3, 5, 8, and so on.

To code a sequence, we need to:

- Define a starting value or a base case. This is the first item in the sequence.
- Define a recursive rule or a formula. This is how we get the next item in the sequence from the previous one or ones.
- Define a stopping condition or a boundary. This is when we stop generating the sequence.

For example, to code the sequence of even numbers, we can use the following pseudocode:

```
# Define the starting value
n = 2

# Define the recursive rule
n = n + 2

# Define the stopping condition
while n < 100
  print n
end
```

This code will print the even numbers from 2 to 98.

To code the sequence of Fibonacci numbers, we can use the following pseudocode:

```
# Define the starting values
a = 1
b = 1

# Define the recursive rule
c = a + b
a = b
b = c

# Define the stopping condition
while a < 100
  print a
end
```

This code will print the Fibonacci numbers from 1 to 89.



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits.
- Binary code is a way of representing data using only two symbols: 0 and 1.
- A fixed-length binary code assigns the same number of bits to each symbol, regardless of its frequency.
- A variable-length binary code assigns different numbers of bits to different symbols, depending on their frequency.
- A prefix code is a variable-length binary code that has the property that no code is a prefix of any other code. This makes it easier to decode the message without ambiguity.
- Huffman coding is a technique for generating a prefix code that minimizes the total number of bits required to encode a message.
- The steps of Huffman coding are :
  - Create a frequency table that counts the occurrence of each symbol in the message.
  - Create a binary tree that has a node for each symbol and its frequency. The root node has the total frequency of all symbols.
  - Sort the nodes in ascending order of frequency and merge the two nodes with the lowest frequency into a new node. The new node has the sum of the frequencies of the two nodes as its frequency. Repeat this step until there is only one node left, which is the root of the tree.
  - Assign a bit (0 or 1) to each edge of the tree. The code for each symbol is the sequence of bits along the path from the root to the leaf node corresponding to that symbol.
  - Encode the message by replacing each symbol with its code.
  - Decode the message by following the path from the root to the leaf node indicated by the bits in the encoded message.



```
### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using fixed-length binary words, where each character or symbol is assigned a unique binary code. For example, the ASCII code uses 8 bits to represent 256 characters.
- Huffman coding is a method of representing data using variable-length binary words, where each character or symbol is assigned a binary code based on its frequency of occurrence in the data. For example, the most frequent character may be assigned a single bit, while the least frequent character may be assigned a longer bit sequence.
- The main advantage of Huffman coding over binary coding is that it can achieve higher compression ratios, as it uses fewer bits to represent more frequent characters and symbols. This reduces the size of the data and saves storage space and bandwidth.
- The main disadvantage of Huffman coding over binary coding is that it requires an extra step of generating and storing the Huffman tree, which is a binary tree that shows the binary codes for each character or symbol. This adds some complexity and overhead to the compression and decompression process.
- Another disadvantage of Huffman coding is that it is not suitable for compressing data that has a uniform distribution of characters or symbols, as it will not reduce the number of bits needed to represent them. In such cases, binary coding may be more efficient or equivalent.
- A comparison of binary and Huffman coding for a sample text is shown below:

| Text | Binary coding | Huffman coding |
|------|---------------|----------------|
| A    | 01000001      | 0              |
| B    | 01000010      | 100            |
| C    | 01000011      | 101            |
| D    | 01000100      | 1110           |
| E    | 01000101      | 1111           |
| F    | 01000110      | 110            |

- Assume that the frequency of the characters in the text is as follows: A (50%), B (12.5%), C (12.5%), D (6.25%), E (6.25%), F (12.5%).
- The Huffman tree for this text is shown below:

```
     / \
    /   \
   /     \
  /       \
 /         \
0          1
|          |
A        / \
       /   \
      /     \
     /       \
    /         \
   1          0
  / \        / \
 /   \      /   \
1    0     1     0
|    |     |     |
E    D     C     B
```

- The total number of bits needed to represent the text using binary coding is 6 x 8 = 48 bits.
- The total number of bits needed to represent the text using Huffman coding is 6 x (0.5 x 1 + 0.125 x 3 + 0.0625 x 4) = 18 bits.
- The compression ratio achieved by Huffman coding over binary coding is 48 / 18 = 2.67, which means that Huffman coding reduces the size of the data by more than 50%.
```



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a sequence, such that the code can be used to reconstruct the original sequence without any loss of information.
- Coding a sequence can be used for various applications, such as:
  - **Data compression**: Reducing the size of data by using shorter codes for more frequent symbols and longer codes for less frequent symbols. This can save storage space and bandwidth, and improve the efficiency of data transmission and processing. Examples of data compression algorithms that use coding a sequence are Huffman coding, arithmetic coding, and Lempel-Ziv coding.
  - **Data encryption**: Protecting the confidentiality of data by transforming it into a different form that can only be deciphered by authorized parties who have the key. This can prevent unauthorized access, modification, or tampering of data. Examples of data encryption algorithms that use coding a sequence are stream ciphers, block ciphers, and public-key cryptography.
  - **Data error detection and correction**: Detecting and correcting errors that may occur during data transmission or storage, due to noise, interference, or defects. This can improve the reliability and accuracy of data communication and storage. Examples of data error detection and correction algorithms that use coding a sequence are parity check, cyclic redundancy check, and Hamming code.
  - **Data compression and encryption**: Combining data compression and encryption to achieve both goals of reducing data size and protecting data security. This can be done by applying compression before encryption, or by using a single algorithm that performs both functions. Examples of data compression and encryption algorithms that use coding a sequence are ZIP, GZIP, and AES.



### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image.
- The JBIG standard (also known as JBIG1) is an early lossless image compression standard from the Joint Bi-level Image Experts Group, standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines, as it offers better compression efficiency than Fax Group 4 compression, which is based on run-length encoding.
- The JBIG standard uses a technique called arithmetic coding, which assigns variable-length codes to symbols based on their probabilities of occurrence.
- The JBIG standard also uses a technique called adaptive template matching, which adapts the coding context to the local image features, such as edges, corners, and textures.
- The JBIG standard can compress bi-level images of any size and resolution, and can handle multiple images in a single file.
- The JBIG standard has some limitations, such as:
  - It cannot compress color or grayscale images, only bi-level images.
  - It cannot exploit the redundancy between similar images, such as pages of a document.
  - It cannot perform lossy compression, which may be desirable for some applications.

### Bi-level image compression-The JBIG2 standard

- The JBIG2 standard (also known as JBIG2) is a newer image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group, standardized as ISO/IEC 14492 and as ITU-T recommendation T.88 in 2000.
- The JBIG2 standard is suitable for both lossless and lossy compression, and can achieve much higher compression ratios than the JBIG standard, especially for text and halftone images .
- The JBIG2 standard uses a technique called model-based coding, which segments the image into regions of different types, such as text, halftone, and generic, and encodes them separately using different models.
- The JBIG2 standard also uses a technique called symbol dictionary coding, which identifies and stores the recurring symbols (such as characters or patterns) in the image, and encodes them using a shared dictionary.
- The JBIG2 standard can compress bi-level images of any size and resolution, and can handle multiple images in a single file.
- The JBIG2 standard can also exploit the redundancy between similar images, such as pages of a document, by using a technique called refinement coding, which encodes the differences between a reference image and a target image.
- The JBIG2 standard has some advantages, such as:
  - It can compress color or grayscale images, by converting them to bi-level images using a technique called halftoning.
  - It can perform lossy compression, by discarding some details or noise in the image, which may improve the visual quality or the compression ratio.
  - It can achieve very high compression ratios, up to 30 times better than the JBIG standard, for some types of images.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two colors, usually black and white, such as scanned documents, faxes, or text.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is lost and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than existing standards, such as MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544), by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve segmenting an image into overlapping and/or non-overlapping regions of text, halftone, and generic content, and then compressing each region with a different method.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and then using a dictionary to store and reference them.
- Halftone regions are compressed by applying a halftone mask to remove the regular pattern and then encoding the remaining pixels with a binary arithmetic coder.
- Generic regions are compressed by using a context-based adaptive binary arithmetic coder, which adapts to the local statistics of the image.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.



### Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or visual appearance. Image compression is useful for saving storage space, bandwidth, and transmission time, as well as for enhancing the performance of applications that use images.

There are two main types of image compression techniques: lossless and lossy.

- Lossless compression techniques preserve the exact information of the original image, and allow the original image to be reconstructed from the compressed data without any loss of quality. Lossless compression techniques are suitable for images that require high fidelity, such as medical images, text documents, or icons. However, lossless compression techniques cannot achieve high compression ratios, and may not reduce the size of the image significantly.

- Lossy compression techniques discard some information of the original image, and allow the compressed data to approximate the original image with some loss of quality. Lossy compression techniques are suitable for images that can tolerate some degradation, such as natural images, photographs, or web graphics. Lossy compression techniques can achieve high compression ratios, and can reduce the size of the image significantly, but at the cost of some distortion or artifacts.

Some of the common methods of image compression are:

- Deflate: This is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 is a dictionary-based algorithm that replaces repeated sequences of pixels with references to previous occurrences. Huffman coding is a variable-length coding scheme that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. Deflate is widely used in formats such as PNG, ZIP, and GZIP.

- Run-length encoding: This is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. For example, a sequence of 10 white pixels can be encoded as (10, white) instead of writing white 10 times. Run-length encoding is effective for images that have large areas of uniform color, such as cartoons or logos.

- Arithmetic coding: This is a lossless image compression technique that is similar to Huffman coding, but uses a more efficient way of assigning codes to symbols. Arithmetic coding assigns codes to symbols based on their probabilities, and uses fractions of bits to represent symbols. Arithmetic coding can achieve higher compression ratios than Huffman coding, but is more complex and computationally intensive. Arithmetic coding is used in formats such as JPEG 2000 and BPG.

- Transform coding: This is a lossy image compression technique that uses mathematical transformations to reduce the size of an image and commonly used for JPEGs. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. One of the most widely used forms of transform coding is the Discrete Cosine Transform (DCT), which converts the image data into a sum of cosine functions of different frequencies. DCT can exploit the fact that human vision is more sensitive to low-frequency components than high-frequency components, and can discard or quantize the high-frequency components with minimal perceptual loss. DCT is used in formats such as JPEG, MPEG, and HEIF .

- Fractal compression: This is a lossy image compression technique that uses the concept of fractals to reduce the size of an image. Fractals are self-similar patterns that can be generated by repeating a simple rule at different scales. Fractal compression tries to find parts of the image that are similar to each other, and encode them using a fractal formula. Fractal compression can achieve high compression ratios and can produce images that can be zoomed in without losing quality, but is very slow and complex to encode and decode. Fractal compression is used in formats such as FIF and FLIF.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of dictionary techniques for data compression:

### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression process.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the amount of data that needs to be transmitted or stored.
- Dictionary techniques can achieve high compression ratios for texts that have a lot of redundancy or repetition. They are also suitable for compressing binary data, such as images or executables, that may not be well compressed by other methods.
- Some examples of dictionary techniques are LZ77, LZ78, LZW, LZSS, LZMA, and Brotli. Each of these algorithms has different variations and optimizations that affect their performance and complexity.



### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, redundancy, and lossless or lossy compression.
- Encoding is the process of transforming data into a different format that uses fewer bits or symbols.
- Decoding is the process of recovering the original data from the encoded format.
- Entropy is a measure of the uncertainty or randomness of data. It indicates the minimum number of bits or symbols needed to represent the data without loss of information.
- Redundancy is the amount of extra or unnecessary information in data that can be removed or reduced without affecting the meaning or quality of data.
- Lossless compression is a type of compression that preserves all the information in the original data and allows exact reconstruction of the data after decompression.
- Lossy compression is a type of compression that discards some information in the original data and allows only approximate reconstruction of the data after decompression. It is usually used for multimedia data, such as images, audio, and video, where some loss of quality is acceptable.
- Coding a sequence is a technique of lossless compression that assigns codes to symbols or sequences of symbols in data based on their frequency of occurrence or probability of occurrence.
- Coding a sequence can be done by using various methods, such as fixed-length codes, variable-length codes, prefix codes, Huffman codes, arithmetic codes, and run-length encoding.
- Fixed-length codes are codes that use the same number of bits or symbols for every symbol or sequence of symbols in data. They are simple and easy to encode and decode, but they are not efficient for compressing data with unequal probabilities of occurrence.
- Variable-length codes are codes that use different numbers of bits or symbols for different symbols or sequences of symbols in data. They are more efficient for compressing data with unequal probabilities of occurrence, but they are more complex and may require additional information to encode and decode.
- Prefix codes are variable-length codes that have the property that no code is a prefix of another code. This means that the codes can be uniquely decoded without any ambiguity or confusion.
- Huffman codes are prefix codes that are optimal for compressing data with known probabilities of occurrence. They are constructed by using a binary tree that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols.
- Arithmetic codes are variable-length codes that are optimal for compressing data with unknown probabilities of occurrence. They are constructed by using a single code that represents the entire data as a fraction between 0 and 1. The code is obtained by dividing the interval [0, 1) into subintervals based on the probabilities of occurrence of the symbols and narrowing down the subinterval that contains the data.
- Run-length encoding is a simple technique of compressing data that contains repeated symbols or sequences of symbols. It replaces the repeated symbols or sequences with a symbol or sequence that indicates the number of repetitions. For example, the sequence AAAABBBBCCCC can be compressed as 4A4B4C.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on static dictionary for the notes of the unit 3 - coding a sequence in the subject of data compression.

### Static Dictionary

- A static dictionary is a **predetermined fixed set of entries** that are used to replace phrases or symbols in the input string with indexes.
- A static dictionary is **faster** than a dynamic or adaptive dictionary, but it requires **prior knowledge** of the source and the distribution of the symbols.
- A static dictionary can be obtained from **clustering** methods that group similar words or phrases together.
- A static dictionary can be used with any compression algorithm, such as Huffman coding, arithmetic coding, or Lempel-Ziv coding, by using a **priming text** that is not transmitted but used to initialize the compression process.
- A static dictionary can be effective for **compressing short texts** or texts with limited vocabulary or repetitive patterns .



### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes.
- Diagram coding works in two passes: the first pass scans the source data and builds a dictionary of digrams and their corresponding codes, the second pass encodes the data using the dictionary .
- Diagram coding can be iterated multiple times, adding more digrams to the dictionary until it is full or the compression ratio is satisfactory.
- Diagram coding can achieve better compression than LZW or BPE for some types of data, such as text or simple images .
- Diagram coding is an example of an ad hoc compression method, meaning that it is not based on a formal model of the source data, but rather on some heuristic or empirical observation .

Here is an example of diagram coding applied to the sentence "This is a test."

- Assume that the source alphabet consists of 26 letters, a space, and a period, and that the unused codes are 28, 29, and 30.
- The first pass scans the source data and finds the following digrams: "is", " a", and "st". These are assigned the codes 28, 29, and 30 respectively, and stored in the dictionary.
- The second pass encodes the data using the dictionary. The encoded data is: 20 8 28 29 1 30 27
- The compression ratio is: (8 * 5) / (7 * 5) = 1.14, meaning that the encoded data is 14% smaller than the original data.



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing information or quality.
- Dictionary compression is a type of data compression that uses a predefined or adaptive dictionary of symbols or patterns to encode the data.
- Adaptive dictionary compression is a variant of dictionary compression that builds the dictionary dynamically based on the data being compressed, rather than using a fixed or predefined dictionary.
- Adaptive dictionary compression can achieve better compression ratios than static dictionary compression, especially for data that is not plain text or has a specific structure or distribution.
- Adaptive dictionary compression can also adapt to changes in the data over time, such as new words or symbols, or different frequencies or contexts of occurrence.
- Some examples of adaptive dictionary compression algorithms are LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel, and Welch.
- LZ77 and LZ78 use a sliding window or a trie data structure, respectively, to store the dictionary and search for matches in the data.
- LZW uses a hash table to store the dictionary and assign codes to the symbols or patterns. It is widely used in UNIX compress, GIF, and PDF formats.
- Adaptive dictionary compression algorithms have some drawbacks, such as memory and computational overhead, complexity of implementation, and possible patent issues.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of LZ77 approach for coding a sequence in data compression:

### The LZ77 Approach

- LZ77 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1977  .
- It is a dictionary coder and maintains a sliding window during compression  .
- The sliding window consists of two parts: a search buffer and a look-ahead buffer  .
- The search buffer contains the previously encoded data, and the look-ahead buffer contains the data to be encoded  .
- The algorithm tries to find the longest match between the look-ahead buffer and the search buffer, and encodes it as a triple of <offset, length, next symbol>  .
- The offset is the distance from the current position to the start of the match in the search buffer, the length is the number of symbols in the match, and the next symbol is the symbol following the match in the look-ahead buffer  .
- If no match is found, the algorithm encodes the next symbol in the look-ahead buffer as a triple of <0, 0, symbol>  .
- The sliding window is then updated by moving forward by the length of the match plus one  .
- The decompression algorithm reverses the process by using the triples to reconstruct the original data  .

Here is an example of LZ77 compression and decompression:

- Suppose the input data is "abracadabra" and the sliding window size is 6.
- The initial sliding window is shown below, with the search buffer empty and the look-ahead buffer containing the input data:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
|               | abracadabra      |
```

- The first symbol "a" is not found in the search buffer, so it is encoded as <0, 0, a> and the sliding window is moved by one:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| a             | bracadabra       |
```

- The second symbol "b" is also not found in the search buffer, so it is encoded as <0, 0, b> and the sliding window is moved by one:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| ab            | racadabra        |
```

- The third symbol "r" is also not found in the search buffer, so it is encoded as <0, 0, r> and the sliding window is moved by one:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| abr           | acadabra         |
```

- The fourth symbol "a" is found in the search buffer, at an offset of 3 and a length of 1, so it is encoded as <3, 1, c> and the sliding window is moved by two:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| abra          | dabra            |
```

- The fifth symbol "d" is not found in the search buffer, so it is encoded as <0, 0, d> and the sliding window is moved by one:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| abrad         | abra             |
```

- The sixth symbol "a" is found in the search buffer, at an offset of 4 and a length of 1, so it is encoded as <4, 1, b> and the sliding window is moved by two:

```
| Search buffer | Look-ahead buffer |
|---------------|-------------------|
| abrada        | ra              |
```

- The seventh symbol "r" is found in the search buffer, at an offset of 5 and a length of 1, so it is encoded as <5, 1, a> and the sliding window is moved by two:

```
| Search buffer | Look-ahead buffer |

```




# The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978.
- It is also known as LZ2 or dictionary-based compression .
- It compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- The dictionary is initialized with all possible single characters as the first entries.
- The algorithm works as follows:
  - Read the next character from the input.
  - If the current token (the longest sequence of characters that has been seen so far) followed by the next character is already in the dictionary, append the next character to the current token and go back to step 1.
  - Otherwise, output a pair of the dictionary index of the current token and the next character, and add the current token followed by the next character to the dictionary as a new entry.
  - Reset the current token to the next character and go back to step 1.
  - Repeat until the end of the input is reached.
- The output can be encoded using variable-length codes, such as Huffman coding, to reduce the size further.
- LZ78 has the advantage of not requiring a sliding window, which reduces the memory usage and allows random access to the compressed data.
- However, it also has some drawbacks, such as the possibility of the dictionary becoming too large, the inefficiency of encoding single characters, and the lack of adaptation to the changing statistics of the input .
- LZ78 is the basis for many variations and improvements, such as LZW, LZSS, LZMA, and others .



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is a technique of data compression that maps a sequence of symbols or data elements into a shorter sequence of codes.
- Coding a sequence can be used for various applications, such as:
  - Image compression: Run length encoding (RLE) is a common method of coding a sequence for image compression. It represents a sequence of pixels of the same color or intensity by a pair of values: the color or intensity and the length of the run.
  - Text compression: Lempel-Ziv-Welch (LZW) is a popular algorithm of coding a sequence for text compression. It builds a dictionary of repeated sequences in the text and assigns them codes of variable length. The codes are shorter than the original sequences, resulting in compression.
  - Genomic compression: Coding a sequence can be used to compress genomic sequencing data, which are typically large and redundant. One approach is to reduce the original data to only variations relative to a reference sequence, and then encode the variations using binary codes.
  - Prediction: Coding a sequence can also be used for prediction, by finding the most probable symbol or sequence given the previous history. This can be done by using arithmetic coding, which assigns codes based on the posterior probabilities of the symbols or sequences.



### File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save storage space, bandwidth, and transmission time.
- UNIX compress is a file compression utility that uses the Lempel-Ziv (LZ) algorithm to compress files.
- The LZ algorithm is based on finding repeated patterns in the data and replacing them with shorter codes.
- The compressed file has a .Z extension and can be decompressed with the uncompress command.
- UNIX compress can achieve a compression ratio of about 2:1 on average, depending on the data.
- UNIX compress is not compatible with other compression formats, such as gzip or zip.
- UNIX compress is useful for compressing text files, such as source code, documents, or logs.
- UNIX compress is not very effective for compressing binary files, such as images, audio, or video, which have less redundancy and require more advanced algorithms.



### Image Compression

Image compression is the process of reducing the size of an image file without affecting its visual quality. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original quality and information of the image. Lossless compression algorithms remove the redundant or unnecessary data from the image, such as repeated pixels or patterns. Lossless compression is suitable for images that require high fidelity, such as medical images, text, or graphics. Some examples of lossless compression methods are:

  - Deflate: Deflate is a popular lossless compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 identifies and replaces repeated sequences of data with shorter references, while Huffman coding assigns variable-length codes to the symbols based on their frequency. Deflate is used in formats such as PNG, ZIP, and GZIP.
  - Run-length encoding: Run-length encoding is a simple lossless compression technique that encodes sequences of repeated pixels with a pair of values: the pixel value and the number of repetitions. For example, the sequence of pixels `BBBBBWWWWWWBBB` can be encoded as `(B,5)(W,6)(B,3)`. Run-length encoding is effective for images with large areas of uniform color, such as icons or logos.
  - Arithmetic coding: Arithmetic coding is a lossless compression technique that assigns variable-length codes to the symbols based on their probability of occurrence. Arithmetic coding is more efficient than Huffman coding, as it can use fractional bits to encode the symbols. Arithmetic coding is used in formats such as JPEG 2000 and BPG.

- Lossy compression: Lossy compression is a technique that reduces the size of the image by discarding some of the less important or perceptually irrelevant data from the image, such as high-frequency details or noise. Lossy compression algorithms use mathematical transformations to convert the image data into a different representation that is more compact and easier to compress. Lossy compression is suitable for images that can tolerate some degradation, such as photographs or videos. Some examples of lossy compression methods are:

  - Transform coding: Transform coding is the most commonly used method for lossy compression. Transform coding applies a mathematical function to the image data, such as the discrete cosine transform (DCT) or the discrete wavelet transform (DWT), to transform the image from the spatial domain to the frequency domain. The frequency domain representation of the image consists of coefficients that indicate the amplitude and phase of the frequency components. The coefficients that correspond to the low-frequency components are more important for the image quality, while the coefficients that correspond to the high-frequency components are less important or perceptually redundant. Therefore, the high-frequency coefficients can be quantized, rounded, or discarded to reduce the size of the image. The quantized coefficients are then encoded using entropy coding, such as Huffman coding or arithmetic coding, to further compress the image. Transform coding is used in formats such as JPEG, JPEG 2000, and HEIF .
  - Vector quantization: Vector quantization is a lossy compression technique that divides the image into blocks of pixels, called vectors, and replaces them with a smaller set of representative vectors, called codebook vectors. The codebook vectors are chosen to minimize the distortion between the original and the reconstructed image. The codebook vectors are then encoded using a fixed-length code, such as a binary code, to compress the image. Vector quantization is used in formats such as GIF and FLIF.



### The Graphics Interchange Format (GIF)

- GIF stands for Graphics Interchange Format .
- GIF is a raster file format designed for relatively basic images that appear mainly on the internet.
- GIF uses the Lempel-Ziv-Welch (LZW) algorithm to losslessly compress 8-bit indexed color graphics.
- Each GIF file can support up to 8 bits per pixel and can contain 256 indexed colors.
- GIF can also store multiple images in a single file, creating a simple animation effect .
- GIF was developed by a team at the online services provider CompuServe led by American computer scientist Steve Wilhite and released on June 15, 1987.
- GIF is widely used for logos, icons, banners, and short animations on the web .
- GIF has some limitations, such as a small color palette, no transparency support, and no audio support .
- GIF is pronounced either as /ɡɪf/ (GHIF) or /dʒɪf/ (JIF), depending on personal preference.



### Compression over Modems

- Compression over modems is a technique to reduce the amount of data that needs to be transmitted over a telephone network, thus increasing the effective bandwidth and speed of the connection.
- Compression over modems is performed by the modems themselves, using special protocols that are negotiated during the handshake phase of the connection.
- The most common protocols for compression over modems are MNP-5 and V.42bis, which are based on the Lempel-Ziv algorithm and can achieve up to 4:1 compression ratio for compressible data  .
- MNP-5 and V.42bis are also error control protocols, which means they can detect and correct errors that may occur during the transmission, ensuring the reliability and integrity of the data.
- MNP-5 and V.42bis work by building a dictionary of frequently occurring patterns in the data stream, and replacing them with shorter codes. The dictionary is updated dynamically and synchronized between the sender and the receiver .
- Compression over modems is most effective for text-based data, such as web pages, emails, or documents, which have a lot of redundancy and repetition. Compression over modems is less effective for binary data, such as images, audio, or video, which are already compressed using other algorithms .
- Compression over modems can improve the throughput and performance of the connection, but it also introduces some overhead and latency, as the modems need to process the data before sending and receiving it. Compression over modems also depends on the quality of the phone line and the compatibility of the modems .
- Compression over modems is an optional feature that can be enabled or disabled by the user or the application. Some applications, such as web browsers, can use their own compression methods to reduce the data size before sending it to the modem, which may result in better compression than the modem's protocol .



### V.42 bits for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- V.42bis is a data compression standard adopted by the CCITT (now ITU-T) in 1990 for data circuit terminating equipment (DCE) using error correcting procedures   .
- V.42bis is based on the Lempel-Ziv-Welch (LZW) algorithm, which is a variant of the Ziv-Lempel family of algorithms that use dictionary-based encoding to compress data   .
- V.42bis uses a dynamic dictionary of up to 2048 entries, which is initialized with 256 ASCII characters and then updated with new strings as they are encountered in the data stream    .
- V.42bis can achieve compression ratios of up to 4:1 for text data and 2:1 for binary data, depending on the characteristics of the data and the dictionary size   .
- V.42bis can operate in two modes: transparent mode and compressed mode. In transparent mode, the data is transmitted without compression, while in compressed mode, the data is compressed using the LZW algorithm    .
- V.42bis can switch between the two modes dynamically, depending on the compressibility of the data and the availability of the dictionary. The mode switching is signaled by special escape sequences    .
- V.42bis also supports two features to improve the compression performance: delayed innovation and limited recycling. Delayed innovation allows the encoder to defer the insertion of new strings into the dictionary until they are repeated, while limited recycling allows the encoder to discard the least recently used entries from the dictionary when it is full   .
- V.42bis is compatible with the V.42 error correction standard, which provides reliable transmission of data over noisy channels. V.42bis can also be used with other modulation standards, such as V.32 and V.34, to achieve higher data rates    .
- V.42bis is widely used by modem manufacturers and network operators, as it can reduce the transmission time and cost of data over the general switched telephone network (GSTN) and other networks    .



### Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits. The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding. The advantage of predictive coding is that it can exploit the statistical dependencies and redundancies in the data, and achieve higher compression ratios than fixed-length codes.

Some examples of predictive coding algorithms are:

- **Linear predictive coding (LPC)**: This is a technique used for speech and audio compression, that models the spectral envelope of the signal using a linear combination of previous samples. The coefficients of the linear combination are called the LPC parameters, and they are transmitted along with the prediction error, or the residual signal. LPC can reduce the bit rate of speech signals by a factor of 10 or more, while preserving the quality and intelligibility of the speech.
- **Dynamic Markov compression (DMC)**: This is a technique that uses a Markov model to predict the next bit in a binary sequence, based on the previous bits. The Markov model is updated dynamically as new bits are observed, and the prediction error is encoded using arithmetic coding. DMC can achieve high compression ratios for text and other types of data, and it adapts well to changes in the data statistics.
- **Predictive coding for images**: This is a technique that exploits the spatial correlation and redundancy in images, by predicting the pixel values based on the neighboring pixels. The prediction error, or the difference image, is then encoded using a lossless compression method, such as Huffman coding or arithmetic coding. Predictive coding for images can reduce the size of uncompressed images by a factor of 2 or more, depending on the image quality and complexity.



# Prediction with Partial Match (PPM) for Data Compression

- PPM is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a set of contexts of different orders, where the order is the number of previous symbols used for prediction.
- For each context, PPM maintains a frequency table of the symbols that have followed that context in the past.
- To encode a symbol, PPM starts with the highest order context that matches the current symbol stream and encodes the symbol using the corresponding frequency table.
- If the symbol is not found in the frequency table, PPM escapes to a lower order context and repeats the process until the symbol is found or the lowest order context is reached.
- To decode a symbol, PPM starts with the highest order context that matches the decoded symbol stream and decodes the symbol using the corresponding frequency table.
- If the symbol is an escape symbol, PPM moves to a lower order context and repeats the process until a non-escape symbol is found or the lowest order context is reached.
- PPM can achieve high compression ratios by adapting to the changing statistics of the data and exploiting the long-range dependencies between symbols .
- PPM can also handle various types of data, such as text, images, audio, etc., by using appropriate symbol alphabets and context orders.



### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can be either lossless or lossy. Lossless compression preserves the exact information of the original data, while lossy compression discards some information to achieve higher compression ratios.
- Coding a sequence is a technique of lossless compression that assigns codes to sequences of symbols or bytes in the data. The codes are usually shorter than the original sequences, resulting in compression .
- One example of coding a sequence is the Lempel–Ziv–Welch (LZW) algorithm, which works as follows :
  - Initialize a code table with 256 entries, corresponding to the 256 possible byte values.
  - Read the first byte of the data and store it as the current sequence.
  - Repeat until the end of the data:
    - Read the next byte and append it to the current sequence.
    - If the current sequence is in the code table, continue reading the next byte.
    - If the current sequence is not in the code table, output the code for the previous sequence (without the last byte), add the current sequence to the code table with a new code, and reset the current sequence to the last byte.
  - Output the code for the final sequence.
- Another example of coding a sequence is the Huffman coding algorithm, which works as follows:
  - Count the frequencies of each symbol or byte in the data and create a leaf node for each symbol with its frequency as the weight.
  - Repeat until there is only one node left:
    - Find the two nodes with the lowest weights and merge them into a new node with the sum of their weights as the new weight.
    - Assign the new node as the parent of the two nodes and label the edges with 0 and 1.
  - The final node is the root of a binary tree that represents the code table. The code for each symbol is the sequence of 0s and 1s along the path from the root to the leaf node.
  - Traverse the data and output the code for each symbol according to the code table.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of the escape symbol for the notes of the unit 3 - coding a sequence in the subject of data compression.

### The ESCAPE SYMBOL

- The escape symbol is a special symbol that is used to indicate that the next symbol in the sequence is not in the current codebook.
- The escape symbol is useful when the codebook is not fixed or complete, and new symbols may appear in the sequence that are not encoded yet.
- The escape symbol allows the encoder and the decoder to update the codebook dynamically, by adding new symbols to the codebook as they are encountered in the sequence.
- The escape symbol must be chosen carefully, so that it does not conflict with any existing symbol in the codebook, and it must be known by both the encoder and the decoder.
- The escape symbol can be either a fixed symbol, or a variable symbol that depends on the context of the sequence.
- The escape symbol can be either a prefix code, or a non-prefix code, depending on the coding scheme used.
- The escape symbol can improve the compression ratio, by reducing the number of bits needed to encode new symbols, but it can also increase the complexity and the overhead of the coding process.

Here is an example of using the escape symbol in a coding scheme:

- Suppose the codebook is {a: 0, b: 10, c: 110, d: 1110, e: 11110, f: 111110, g: 1111110, h: 11111110, i: 111111110, j: 1111111110, k: 11111111110, l: 111111111110, m: 1111111111110, n: 11111111111110, o: 111111111111110, p: 1111111111111110, q: 11111111111111110, r: 111111111111111110, s: 1111111111111111110, t: 11111111111111111110, u: 111111111111111111110, v: 1111111111111111111110, w: 11111111111111111111110, x: 111111111111111111111110, y: 1111111111111111111111110, z: 11111111111111111111111110}
- Suppose the escape symbol is 11111111111111111111111111
- Suppose the sequence to be encoded is "hello world"
- The encoded sequence is 0 11111111111111111111111111 110 110 11110 10 11111111111111111111111111 1111111111111111111111110 1110 110 11110 0 11111111111111111111111111 11111111111111111111111110
- The decoder can decode the sequence by using the escape symbol to identify new symbols, and adding them to the codebook as they are decoded. For example, when the decoder sees the escape symbol followed by 110, it knows that 110 is a new symbol, and it assigns it to the letter l, and adds it to the codebook. Then, it can decode the rest of the sequence using the updated codebook.



### Length of context for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The length of context is the number of previous symbols that are used to determine the probability of the next symbol in a sequence.
- The length of context affects the performance of the compression algorithm, as it determines how well the algorithm can adapt to the statistical properties of the data.
- A longer context can capture more patterns and correlations in the data, but it also requires more memory and computation to store and update the probabilities.
- A shorter context can be faster and simpler, but it may miss some important information and result in suboptimal compression.
- The optimal length of context depends on the characteristics of the data and the trade-off between compression ratio and complexity.
- Some compression algorithms, such as adaptive arithmetic coding, can adjust the length of context dynamically based on the data. Other algorithms, such as Huffman coding, use a fixed length of context.



### The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The exclusion principle is a technique for encoding a sequence of symbols by eliminating the symbols that are not possible in the current context.
- The idea is to use a smaller alphabet for each symbol, based on the previous symbols in the sequence and some rules or constraints that define the valid sequences.
- For example, if the sequence is a word in English, we can use the exclusion principle to reduce the number of possible letters for each position, based on the previous letters and the rules of English spelling.
- The exclusion principle can reduce the number of bits needed to encode each symbol, by using a variable-length code that assigns shorter codes to more frequent symbols in the reduced alphabet.
- The exclusion principle can also improve the compression ratio by increasing the redundancy of the sequence, since the symbols that are excluded are more predictable and less informative.
- The exclusion principle requires the encoder and the decoder to have the same knowledge of the rules or constraints that define the valid sequences, and to update their context after each symbol.
- The exclusion principle can be applied to different types of sequences, such as text, images, audio, video, etc., depending on the domain-specific rules or constraints that can be used to exclude symbols.



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

| T$     |
|--------|
| banana$|
| anana$b|
| nana$ba|
| ana$ban|
| na$bana|
| a$banan|
| $banana|

- The last column is annb$aa, which is the BWT(banana).
- The procedure for recovering T from BWT(T) is as follows :
  - Construct the first column of the table of cyclic rotations by sorting the characters of BWT(T) lexicographically.
  - For each character in BWT(T), count how many times it appears before its position in BWT(T). This is called the rank of the character.
  - For each character in the first column, count how many times it appears before its position in the first column. This is called the index of the character.
  - For each character in BWT(T), find the character in the first column that has the same rank and index. This is called the LF-mapping (last-to-first mapping).
  - Starting from the $ symbol in BWT(T), follow the LF-mapping until reaching the $ symbol in the first column. The recovered string T is the sequence of characters visited in the first column, excluding the $ symbol.
- For example, if BWT(T) = annb$aa, then the first column is $aaabnn, and the ranks and indices are:

| BWT(T) | Rank | First column | Index | LF-mapping |
|--------|------|--------------|-------|------------|
| a      | 0    | $            | 0     | $ -> a     |
| n      | 0    | a            | 0     | a -> n     |
| n      | 1    | a            | 1     | n -> n     |
| b      | 0    | a            | 2     | n -> b     |
| $      | 0    | b            | 0     | b -> $     |
| a      | 1    | n            | 0     | $ -> a     |
| a      | 2    | n            | 1     | a -> a     |

- Following the LF-mapping from $ in BWT(T) to $ in the first column, we get the sequence $ -> a -> n -> n -> b -> $, which corresponds to the string annb, which is T without the $ symbol.



### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but rearranges the data to make it more suitable for entropy encoding techniques of compression  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is updated dynamically as the data is processed. The list is initially sorted in some order, such as lexicographic or frequency-based. Then, for each symbol in the data, the algorithm outputs the index of that symbol in the list and moves that symbol to the front of the list  .
- The advantage of movetofront coding is that it tends to produce long runs of small numbers, especially if the data has high local correlation or repetition. This makes the data more compressible by entropy encoding techniques, such as Huffman coding or arithmetic coding  .
- The disadvantage of movetofront coding is that it adds an extra step in the compression and decompression process, which may increase the computational complexity and time. However, the algorithm is relatively simple and fast to implement, and its benefits usually outweigh its costs  .
- Movetofront coding is reversible, meaning that the original data can be recovered from the transformed data and the list of symbols. The decompression algorithm simply reverses the steps of the compression algorithm, using the same list of symbols and updating it in the same way  .
- Movetofront coding is used as a sub-step in several other compression algorithms, such as Burrows–Wheeler transform, bzip2, and ZPAQ .



### CALIC
- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a technique for compressing continuous-tone images without any loss of quality or information  .
- It achieves high coding efficiency with relatively low time and space complexities  .
- It can also be applied to compress compound video, which consists of computer screen data and natural video.
- The main steps of CALIC are :
  - Image data modeling: It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics. The non-linear predictor adapts via an error feedback mechanism.
  - Entropy coding: It uses a Golomb-Rice code to encode the prediction errors. The code parameter is also adaptive to the local statistics of the errors.
  - Context quantization: It reduces the number of contexts by grouping them into a smaller number of classes based on their similarity. This reduces the overhead of storing the context information.
- The advantages of CALIC are :
  - It can handle various types of images, such as natural, synthetic, medical, etc.
  - It can exploit both the spatial and the spectral correlations in the image data.
  - It can adapt to the local characteristics of the image data and achieve optimal prediction and coding.
  - It can achieve higher compression ratios than other lossless image coding techniques, such as JPEG-LS, PNG, etc.



### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- It is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- It consists of two independent and distinct stages: modeling and encoding .
- In the modeling stage, the algorithm predicts the value of each pixel based on its neighboring pixels and computes the prediction error .
- In the encoding stage, the algorithm maps the prediction errors to symbols and encodes them using a context-based adaptive arithmetic coder .
- JPEG-LS achieves high compression ratios by exploiting the high correlation among neighboring pixels and using a simple and efficient coding scheme  .
- JPEG-LS is suitable for applications that require low complexity, low latency, and high fidelity compression of continuous-tone images  .



### Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of resolution or detail to represent or process data, such as images, vectors, or fluids.
- The main advantages of multi-resolution approaches are:
  - They can capture long-range phenomena that would otherwise be missed by using only one level of resolution.
  - They can reduce computational complexity and memory requirements by allowing algorithms to work on both fine and coarse scales, rather than waiting for local pixel-level operations to converge at large scales.
  - They can improve the compression efficiency and quality by better coding of high frequencies and reducing the characteristic distortions of some compression algorithms, such as blocking artifacts and image blurring.
- Some examples of multi-resolution approaches for data compression are:
  - Wavelet-based compression: This method uses wavelets, which are mathematical functions that can decompose a signal into different frequency components, to represent data at different scales. Wavelet-based compression can achieve high compression ratios and preserve the perceptual quality of the data.
  - Fractal-based compression: This method uses fractals, which are self-similar patterns that can be generated by recursive rules, to model the data at different scales. Fractal-based compression can exploit the self-similarity of natural images and achieve high compression ratios, but it may suffer from slow encoding and decoding speed and low resolution.
  - Multi-resolution vector data compression: This method uses a grid-based approach to partition the vector data into different levels of resolution, and then applies different compression techniques to each level, such as grid filtering, binary offset, and Huffman coding. This method can achieve multiresolution vector data compression with visual lossless distance on screen display as accuracy requirement.
  - Multi-resolution method with sharp interface model: This method uses a cell-averaged multi-resolution method to simulate compressible multi-phase flows, where a sharp interface model is employed to track the interface between different phases. This method can reduce the memory and CPU-time consumption and capture the interface dynamics accurately.



### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding exploits the fact that most documents have large areas of white or black pixels, and uses run-length coding to encode the lengths of consecutive runs of the same color.
- Run-length coding is a simple technique that replaces a sequence of identical symbols with a pair of the symbol and its count. For example, the sequence `WWWWWWWWWW` can be encoded as `(W,10)`.
- Facsimile encoding uses two types of run-length codes: white codes and black codes. White codes are used to encode runs of white pixels, and black codes are used to encode runs of black pixels.
- Facsimile encoding also uses two modes: horizontal mode and vertical mode. Horizontal mode encodes two consecutive runs of different colors on the same scan line. Vertical mode encodes a single run of pixels that differs from the corresponding run on the previous scan line by one pixel.
- Facsimile encoding uses a variable-length codebook to assign codes to different run lengths. The codebook is designed to assign shorter codes to more frequent run lengths, and longer codes to less frequent run lengths. This is similar to Huffman coding, which is another form of lossless data compression.
- Facsimile encoding can reduce the transmission requirements of fax images while maintaining high intelligibility in mobile communications environments. Facsimile encoding can also be applied to the lossless compression of images with 8-bit per pixel or higher.



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, each representing a context or a history of previous bits. Each node has two counters, one for the number of zeros and one for the number of ones that have occurred in that context .
- The model is initialized with a single root node with zero counters. As each bit is read from the input, the model is updated by incrementing the corresponding counter of the current node, and creating a new child node if necessary .
- The model is used to predict the probability of the next bit, given the current context. This probability is then used to encode the bit using arithmetic coding .
- The model adapts to changes in the input data by pruning nodes that have low counts, and splitting nodes that have high counts. This ensures that the model is not too large or too complex, and that it reflects the most recent patterns in the data .
- DMC is an effective and efficient compression algorithm that can handle various types of data, such as text, images, audio, and binary files . It achieves compression ratios comparable to or better than other algorithms, such as PPM, LZW, and Huffman coding.



## Unit 4 - Distortion criteria

- Distortion criteria are the measures of how well a communication system preserves the fidelity of the transmitted signal.
- Distortion criteria can be classified into two types: linear and nonlinear.
- Linear distortion criteria are based on the assumption that the communication system is linear, meaning that the output signal is a scaled and shifted version of the input signal.
- Nonlinear distortion criteria are based on the assumption that the communication system is nonlinear, meaning that the output signal is a distorted version of the input signal that cannot be expressed as a linear function of the input signal.
- Some examples of linear distortion criteria are:
  - Signal-to-noise ratio (SNR): the ratio of the power of the signal to the power of the noise.
  - Bandwidth: the range of frequencies that the signal occupies.
  - Delay: the time difference between the input and output signals.
- Some examples of nonlinear distortion criteria are:
  - Harmonic distortion: the presence of unwanted frequencies that are multiples of the fundamental frequency of the signal.
  - Intermodulation distortion: the presence of unwanted frequencies that are combinations of the frequencies of two or more signals.
  - Cross-talk: the interference of one signal with another signal in a different channel or path.



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not after decompression.
- Lossy compression introduces some distortion or error in the reconstructed data, which may be acceptable or not depending on the application and the user's preference.
- Distortion criteria are the measures that quantify how close the reconstructed data is to the original data, using some mathematical or perceptual metric.
- Some common distortion criteria are:
  - Mean squared error (MSE): the average of the squared differences between the original and the reconstructed data values.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible value of the data to the noise or error introduced by compression, expressed in decibels (dB).
  - Structural similarity index (SSIM): a perceptual metric that compares the luminance, contrast and structure of the original and the reconstructed data, ranging from 0 (no similarity) to 1 (perfect similarity).
  - Bit error rate (BER): the fraction of bits that are different between the original and the reconstructed data.
- Rate-distortion theory is the branch of information theory that studies the trade-off between the compression rate (the number of bits per data unit) and the distortion (the error or loss of quality) introduced by compression.
- Rate-distortion theory defines the rate-distortion function R(D) as the minimum compression rate that can be achieved for a given distortion level D, or equivalently, the minimum distortion that can be achieved for a given compression rate R.
- The rate-distortion function R(D) depends on the source statistics (the probability distribution of the data values) and the distortion measure (the metric used to quantify the error).
- The rate-distortion function R(D) can be calculated using an iterative algorithm called the Blahut-Arimoto algorithm, which alternates between finding the optimal probability distribution of the compressed data and the optimal distortion measure for a given distortion level.
- The rate-distortion function R(D) provides a theoretical lower bound for the performance of any practical compression system. The closer a compression system is to the rate-distortion function, the more efficient it is.



### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization can be used to reduce the bit rate of a signal by encoding each sample with a fixed number of bits, based on its quantization level.
- Scalar quantization can introduce distortion or error in the signal, as the quantized value may not be exactly equal to the original value.
- The performance of scalar quantization depends on the design of the quantizer, which includes the number of quantization levels, the spacing of the levels, and the mapping rule from the input to the output.
- The quantizer can be uniform or nonuniform, depending on whether the quantization levels are equally spaced or not. Uniform quantizers are simpler to implement, but may not be optimal for signals that have nonuniform probability distributions .
- The quantizer can be midtread or midrise, depending on whether the quantization levels include zero or not. Midtread quantizers have better performance for signals that have zero mean, while midrise quantizers have better performance for signals that have nonzero mean .
- The quantizer can be deterministic or stochastic, depending on whether the mapping rule is fixed or random. Deterministic quantizers are more predictable, but may introduce periodic errors or granular noise. Stochastic quantizers are less predictable, but may reduce the errors or noise by introducing dither or randomization .
- The distortion or error of scalar quantization can be measured by different criteria, such as mean squared error (MSE), signal-to-noise ratio (SNR), peak signal-to-noise ratio (PSNR), or perceptual quality. The optimal quantizer design depends on the distortion criterion and the signal characteristics .
- Scalar quantization can be applied to various types of signals, such as audio, image, or video. However, scalar quantization may not be efficient or effective for signals that have high correlation or dependency among the samples. In such cases, vector quantization or transform coding may be more suitable  .

: Scalar Quantization - an overview | ScienceDirect Topics
: Scalar Quantization - Introduction to Data Compression, 4th Edition [Book]
: Scalar Quantizer - an overview | ScienceDirect Topics
: The Wavelet /Scalar Quantization Compression Standard for ... - NIST
: Scalar Quantization - an overview | ScienceDirect Topics



### The Quantization Problem

Quantization is a process of mapping a large set of input values to a smaller set of output values, such that each input value is approximated by one of the output values. Quantization is used in data compression to reduce the number of bits needed to represent a signal, image, or other data. Quantization introduces some distortion or error in the data, which affects the quality of the reconstruction. Therefore, the quantization problem is to find an optimal way of quantizing the data, such that the distortion is minimized and the compression ratio is maximized.

Some of the topics related to the quantization problem are:

- **Quantization error**: The difference between the original value and the quantized value. It can be measured by various criteria, such as mean squared error, signal-to-noise ratio, or perceptual quality.
- **Uniform and non-uniform quantization**: Uniform quantization divides the input range into equal-sized intervals, and assigns a fixed output value to each interval. Non-uniform quantization divides the input range into variable-sized intervals, and assigns a different output value to each interval. Non-uniform quantization can adapt to the characteristics of the data, and achieve lower distortion and higher compression ratio than uniform quantization.
- **Scalar and vector quantization**: Scalar quantization quantizes each input value independently, and produces a single output value for each input value. Vector quantization quantizes a group of input values together, and produces a single output value for each group. Vector quantization can exploit the correlation among the input values, and achieve lower distortion and higher compression ratio than scalar quantization.
- **Optimal quantization**: Optimal quantization is the quantization that minimizes the distortion for a given compression ratio, or maximizes the compression ratio for a given distortion. Optimal quantization depends on the probability distribution of the input values, the distortion measure, and the code length. Optimal quantization can be found by various algorithms, such as the Lloyd algorithm, the K-means algorithm, or the entropy-constrained algorithm.



### Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels, and its number of output levels $M$, which is usually a power of two.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero. It is suitable for signals with zero mean and symmetric distribution.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero. It is suitable for signals with non-zero mean and asymmetric distribution.
- A uniform quantizer can be combined with a companding function to achieve non-uniform quantization, which can reduce the quantization noise for signals with non-uniform distribution.
  - A companding function is a nonlinear function that compresses the input signal before quantization and expands the output signal after quantization.
  - Two common companding functions are the $\mu$-law and the A-law, which are used for PCM telephone systems.
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model.
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the distortion or the rate-distortion trade-off of the image compression model .
- A uniform quantizer can be analyzed by using the high-rate or the low-rate regime, depending on the number of output levels or the bit rate .
  - In the high-rate regime, the quantization noise can be modeled as a uniform distribution and the distortion can be approximated by the mean squared error .
  - In the low-rate regime, the quantization noise can be modeled as a Laplacian distribution and the distortion can be approximated by the mean absolute error .



### Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input data.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters, such as synthetic aperture radar (SAR) raw data.
- An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution, minimizing the distortion or the bit rate.
- There are two main types of adaptive quantization: forward adaptive quantization and backward adaptive quantization.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block and transmitted to the receiver as side information. For example, the minimum and maximum values of each block can be used to determine the quantization step size.
- In backward adaptive quantization, the quantizer parameters are updated based on the previous quantized samples. The receiver can reconstruct the parameters using the same update rule as the transmitter. For example, the Lloyd-Max algorithm can be used to adjust the quantization levels based on the mean squared error criterion.
- Adaptive quantization can improve the performance of differential pulse-code modulation (DPCM), which is a predictive coding technique that exploits the correlation between adjacent samples. By using adaptive quantization, the quantization noise can be reduced and the dynamic range can be increased.
- Adaptive quantization can also be combined with other compression methods, such as transform coding, entropy coding, and vector quantization, to achieve higher compression ratios and better quality.
- Adaptive quantization is a challenging problem that requires balancing the trade-off between complexity, distortion, and bit rate. Some of the factors that affect the performance of adaptive quantization are the block size, the quantizer design, the estimation method, the update rule, and the side information overhead .
- Adaptive quantization is an active research area that explores new methods and applications for data compression. Some of the recent advances include online learned continual compression with adaptive quantization modules, which can adapt to different data types and memory constraints without pretraining.



### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal spacing between the output values.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions of high probability and less bits to the regions of low probability.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that adjusts the output levels according to the statistics of the input signal.
  - Using a trainable quantizer that optimizes the output levels using the back-propagation of the network gradients, such as in neural network compression .
- Non uniform quantization can reduce the quantization noise and improve the signal-to-noise ratio (SNR) of the quantized signal, but it also introduces some challenges, such as:
  - The complexity and cost of the quantizer and the dequantizer, which may require non-linear operations or feedback mechanisms.
  - The compatibility and interoperability of the quantizer and the dequantizer, which may require a common standard or a shared codebook.
  - The accuracy and efficiency of the quantizer and the dequantizer, which may depend on the quality of the non-linear function or the optimization algorithm .



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique for compressing data by representing a large set of vectors (such as image pixels or speech samples) by a smaller set of code vectors (or codebook).
- Scalar quantization (SQ) is a simpler technique that compresses data by representing each individual value (such as a pixel intensity or a speech amplitude) by a discrete level (or codeword).
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ, since it exploits the correlation and redundancy among the data vectors, while SQ treats each value independently.
  - VQ can preserve the quality of the data better than SQ, since it minimizes the distortion (or error) between the original and the reconstructed vectors, while SQ introduces quantization noise (or error) for each value.
  - VQ can adapt to the statistics and characteristics of the data better than SQ, since it can design the codebook based on the distribution and variation of the data vectors, while SQ uses a fixed and uniform quantization scheme for all values.
  - VQ can handle non-linear and complex data better than SQ, since it can approximate the data vectors by non-uniform and non-rectangular regions (or cells), while SQ can only partition the data values by uniform and rectangular intervals (or bins).



### The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in a given data set.
- Vector quantization is a technique to compress data by reducing the number of bits needed to represent each vector.
- The LBG algorithm is similar to the k-means method in data clustering .
- The LBG algorithm works as follows :
  - Start with an initial codebook of size one, which is the centroid of the training set.
  - Split each codeword into two slightly perturbed versions, doubling the size of the codebook.
  - Assign each vector in the training set to the nearest codeword, forming clusters around each codeword.
  - Update each codeword by computing the centroid of its cluster, minimizing the distortion within each cluster.
  - Repeat the last two steps until the distortion converges or a desired codebook size is reached.

### Advantages of Vector Quantization over Scalar Quantization

- Scalar quantization is a technique to compress data by reducing the number of bits needed to represent each scalar value.
- Vector quantization has some advantages over scalar quantization, such as:
  - It can exploit the correlation between adjacent values in a vector, resulting in higher compression ratios.
  - It can achieve lower distortion for a given bit rate, or lower bit rate for a given distortion, compared to scalar quantization.
  - It can handle non-uniform distributions of data more efficiently than scalar quantization, which assumes a uniform distribution.
  - It can adapt to the characteristics of the data by using different codebooks for different regions or classes of data.



### Tree structured Vector Quantizers for the notes of the Unit 5 - Advantages of Vector Quantization over Scalar Quantization in the subject of Data Compression

- Vector quantization (VQ) is a technique for compressing data by representing a set of input vectors with a smaller set of output vectors, called codevectors or codewords.
- Scalar quantization (SQ) is a special case of VQ where the input and output vectors are one-dimensional, i.e., scalars.
- VQ has several advantages over SQ, such as:
  - VQ can exploit the correlation among the components of the input vectors, while SQ treats each component independently.
  - VQ can achieve lower distortion than SQ for the same number of bits per vector, or equivalently, lower bit rate for the same distortion level.
  - VQ can adapt to the statistics of the input data by using variable-length codes or variable-size partitions, while SQ usually uses fixed-length codes or uniform partitions.
- However, VQ also has some disadvantages, such as:
  - VQ requires a large codebook to store the codevectors, which increases the memory and storage requirements.
  - VQ requires a complex search algorithm to find the closest codevector for each input vector, which increases the computational complexity and encoding time.
  - VQ is sensitive to errors in the transmission or storage of the codevectors or the codeword indices, which can cause significant distortion or loss of information.
- Tree-structured vector quantization (TSVQ) is a technique that reduces the complexity and improves the performance of VQ by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the codevectors. The intermediate nodes represent the subspaces that are further divided by their children nodes.
- The advantage of TSVQ is that the tree structure can be represented by a binary code, where each bit indicates whether to go to the left or right child of the current node. This reduces the storage cost and the encoding rate of the codebook, as well as the quantization time, since the search can be performed by following a root-to-leaf path .
- The disadvantage of TSVQ is that the tree structure may not be optimal for the input data, since it imposes a constraint on the shape and size of the regions. This may result in higher distortion or lower rate-distortion efficiency than an unconstrained VQ. Therefore, the design of TSVQ requires finding a balance between the complexity and the performance of the quantizer.



### Structured Vector Quantizers

- Vector quantization is a technique that compresses data by representing a set of input vectors (such as image blocks) by a smaller set of output vectors (called code vectors or codewords) that are stored in a codebook.
- The codebook is designed to minimize the distortion (such as mean squared error) between the input and output vectors, subject to a constraint on the size of the codebook or the number of bits per vector.
- The encoding process consists of finding the closest code vector to each input vector and transmitting its index in the codebook. The decoding process consists of retrieving the code vector from the codebook using the index and reconstructing the output vector.
- Vector quantization has several advantages over scalar quantization, which operates on single variables (such as pixels) instead of vectors. Some of these advantages are :
  - Vector quantization can exploit the correlation among the variables in a vector, resulting in lower distortion and higher compression ratio.
  - Vector quantization can avoid the blocking artifacts and contouring effects that are common in scalar quantization, especially at low bit rates.
  - Vector quantization can adapt to the local statistics of the input data, resulting in better performance for nonstationary sources.
  - Vector quantization can handle multidimensional data (such as color images or video) more efficiently than scalar quantization, which requires separate quantization of each dimension.
- However, vector quantization also has some drawbacks, such as the high complexity of the encoding and decoding processes, the large storage requirement for the codebook, and the sensitivity to channel errors .
- Structured vector quantizers are a class of vector quantizers that aim to overcome some of these drawbacks by imposing some structure on the codebook or the partitioning of the input space  .
- Structured vector quantizers can be classified into two main types: tree-structured vector quantizers and lattice vector quantizers.
- Tree-structured vector quantizers (TSVQ) use a hierarchical partitioning of the input space, such that each node in the tree corresponds to a region and a code vector. The root node corresponds to the entire input space and the code vector is the mean of all input vectors. The leaf nodes correspond to the final regions and code vectors that are used for encoding and decoding.
- TSVQ reduces the complexity of the encoding and decoding processes by using a fast search algorithm that traverses the tree from the root to the leaf node that is closest to the input vector. The index of the code vector is obtained by concatenating the branch labels along the path.
- TSVQ also reduces the storage requirement for the codebook by using a variable-length code for the index, such that shorter codes are assigned to more probable regions and code vectors. The codebook can be stored implicitly by storing only the branch labels and the code vectors at the leaf nodes.
- However, TSVQ also has some limitations, such as the suboptimality of the tree structure, the difficulty of designing optimal trees, and the dependence of the performance on the order of the input vectors.
- Lattice vector quantizers (LVQ) use a regular geometric structure for the codebook, such that the code vectors are generated algorithmically from a lattice (a discrete subset of a vector space that is closed under addition and subtraction). The lattice can be chosen to match the shape of the input space or the distribution of the input vectors.
- LVQ eliminates the need for storing the codebook explicitly, as the code vectors can be computed on the fly using simple arithmetic operations. The index of the code vector can be obtained by mapping the lattice point to a unique integer using a one-to-one function.
- LVQ also simplifies the encoding and decoding processes by using fast algorithms that exploit the symmetry and regularity of the lattice. The encoding algorithm can use a nearest-neighbor search or a successive approximation search to find the closest lattice point to the input vector. The decoding algorithm can use the inverse mapping function to retrieve the lattice point from the index and compute the code vector.
- However, LVQ also has some drawbacks, such as the limited choice of lattices that can achieve good performance, the difficulty of adapting the lattice to the input data, and the sensitivity to channel errors and quantization noise.

: On the structure of

