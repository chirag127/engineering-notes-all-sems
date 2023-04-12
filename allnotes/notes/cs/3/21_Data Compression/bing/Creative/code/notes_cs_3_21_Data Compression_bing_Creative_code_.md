

## Unit 1 - Compression Techniques

- Compression is the process of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, audio, and some images that require high fidelity.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for images, video, and some audio that can tolerate some quality degradation.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): replaces consecutive identical symbols with a count and a symbol.
  - Huffman coding: assigns variable-length codes to symbols based on their frequency of occurrence.
  - Lempel-Ziv-Welch (LZW): builds a dictionary of common patterns and encodes them with fixed-length codes.
- Some common lossy compression techniques are:
  - JPEG: uses discrete cosine transform (DCT) and quantization to compress images.
  - MPEG: uses DCT, quantization, and motion estimation to compress video.
  - MP3: uses psychoacoustic model and bit allocation to compress audio.



# Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values or patterns are more frequent than others and can be encoded with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and images that need high quality .
- Lossless compression can reduce the file size by removing unnecessary or repeated information, rearranging the data in a more compact way, or using mathematical algorithms to transform the data into a shorter representation.
- Some examples of lossless compression algorithms are Huffman coding, arithmetic coding, run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, and deflate algorithm.
- The compression ratio of lossless compression depends on the type and characteristics of the data, as well as the compression algorithm used. Typically, lossless compression can achieve compression ratios of 2:1 to 8:1 for text and 1.5:1 to 2:1 for images.
- Lossless compression is different from lossy compression, which discards some data in the compression process and produces a lower quality output. Lossy compression is suitable for applications that can tolerate some loss of information, such as audio, video, and images that need low bandwidth or storage .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of lossy compression for the unit 1 - compression techniques in the subject of data compression.

### Lossy Compression

- Lossy compression is a type of compression technique that reduces the size of data by discarding some information that is not essential or perceptible to the human senses.
- Lossy compression is useful for applications that can tolerate some degradation in quality, such as audio, video, and image compression.
- Lossy compression can achieve higher compression ratios than lossless compression, but at the cost of losing some fidelity or accuracy of the original data.
- Lossy compression is based on the concept of **psychoacoustics** and **psychovisuals**, which are the study of how humans perceive sound and vision, respectively.
- Lossy compression exploits the limitations and characteristics of human perception, such as **masking**, **thresholds**, **quantization**, and **transform coding**.
- Masking is the phenomenon where a stronger signal makes a weaker signal inaudible or invisible. For example, a loud noise can mask a faint sound, or a bright color can mask a dim color.
- Thresholds are the minimum levels of intensity or frequency that humans can perceive. For example, humans cannot hear sounds below 20 Hz or above 20 kHz, or see colors below 380 nm or above 750 nm.
- Quantization is the process of approximating a continuous signal with a discrete set of values. For example, an analog sound wave can be quantized into a digital sequence of bits, or an image can be quantized into a matrix of pixels.
- Transform coding is the process of converting a signal from one domain to another, where it can be more efficiently compressed. For example, an image can be transformed from the spatial domain to the frequency domain, where it can be compressed by discarding high-frequency components that are less visible to humans.

Some examples of lossy compression algorithms are:

- **MP3** for audio compression, which uses a perceptual model of human hearing to discard sounds that are masked by other sounds, and quantizes the remaining sounds with different levels of precision depending on their perceptual importance.
- **JPEG** for image compression, which uses a discrete cosine transform (DCT) to convert an image from the spatial domain to the frequency domain, and quantizes the resulting coefficients with different levels of precision depending on their perceptual importance. It also uses a variable-length coding (VLC) to encode the quantized coefficients with fewer bits for more frequent values.
- **H.264** for video compression, which uses a combination of spatial and temporal prediction, transform coding, quantization, and entropy coding to compress video frames. It also uses a variable bit rate (VBR) to allocate more bits to more complex or important frames.



### Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by eliminating redundancy or approximating the original data.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques allow some distortion or degradation of the original data in exchange for higher compression ratios.
- Compression techniques can be applied to different types of data, such as text, images, audio, video, etc.
- The performance of compression techniques can be measured by various metrics, depending on the type and purpose of the data.
- Some of the common metrics are:

  - Compression ratio (CR): the ratio of the size of the original data to the size of the compressed data. Higher CR means higher compression efficiency.
  - Compression factor (CF): the inverse of CR, i.e., the ratio of the size of the compressed data to the size of the original data. Lower CF means higher compression efficiency.
  - Bits per character (bpc) or bits per pixel (bpp): the average number of bits used to represent each character or pixel in the compressed data. Lower bpc or bpp means higher compression efficiency.
  - Mean squared error (MSE): the average of the squared differences between the original data and the reconstructed data after compression and decompression. Lower MSE means lower distortion or error.
  - Root mean squared error (RMSE): the square root of MSE. Lower RMSE means lower distortion or error.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible value of the original data to the noise or error introduced by compression and decompression. Higher PSNR means lower distortion or error.
  - Structural similarity index (SSIM): a measure of the similarity between the original data and the reconstructed data based on the luminance, contrast, and structure of the data. Higher SSIM means higher similarity or quality.
  - Multi-scale structural similarity index (MS-SSIM): an extension of SSIM that considers the similarity at different scales or resolutions of the data. Higher MS-SSIM means higher similarity or quality.
  - Accuracy: the percentage of the original data that is correctly preserved or reconstructed after compression and decompression. Higher accuracy means higher quality or fidelity.

- Different compression techniques may have different trade-offs between compression efficiency and quality or fidelity. Therefore, the choice of the best compression technique depends on the requirements and constraints of the application or user.



# Modeling and coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can reduce the storage space or transmission bandwidth required for a given piece of information.
- Data compression can be either lossless or lossy.
  - Lossless compression preserves the exact information of the original data, and can be reversed by decompression.
  - Lossy compression discards some information of the original data, and cannot be reversed by decompression.
  - Lossless compression is suitable for text, audio, or executable files, while lossy compression is suitable for images, video, or speech.
- Data compression techniques can be classified into two categories: statistical and dictionary-based.
  - Statistical techniques use the frequency or probability of symbols in the data to assign shorter codes to more common symbols and longer codes to less common symbols.
  - Dictionary-based techniques use a predefined set of symbols or patterns to replace repeated occurrences of the same symbol or pattern in the data.
- Some common data compression techniques are:
  - Lempel–Ziv: a lossless dictionary-based technique that finds repeated characters or sequences in the data and replaces them with tokens or shortened sequences.
  - Huffman coding: a lossless statistical technique that assigns variable-length codes to symbols based on their frequency in the data.
  - Run-length encoding: a lossless technique that replaces consecutive occurrences of the same symbol with a count and the symbol.
  - Arithmetic coding: a lossless statistical technique that assigns codes to symbols based on their cumulative probability in the data.
  - JPEG: a lossy technique that compresses images by transforming them into frequency domain and discarding high-frequency components that are less perceptible to human vision.
  - MPEG: a lossy technique that compresses video by exploiting temporal and spatial redundancy in the frames and applying quantization and entropy coding.
  - MP3: a lossy technique that compresses audio by applying psychoacoustic models and removing sounds that are masked by louder sounds.
- Data compression can be performed by using smaller strings of bits (0s and 1s) in place of the original string and using a ‘dictionary’ to decompress the data if required.
- Data compression can also use pointers (references) to a string of bits that the compression program has become familiar with or removing redundant characters.
- Data compression can be improved by using the following best practices:
  - Determine the compression level: Depending on the needs, the data can be compressed to a certain level, such as low, medium, or high.
  - Choose the appropriate compression type: For every file to be compressed, first determine whether it is lossless or lossy, and then choose the suitable technique.
  - Use a coprocessor: A coprocessor is a hardware device that can perform compression and decompression faster and more efficiently than a general-purpose processor.
  - Consider data deduplication: Data deduplication is a technique that eliminates duplicate or redundant data blocks and stores only one copy of each data block.
  - Determine if multi-stage compression is needed: Multi-stage compression is a technique that applies more than one compression technique to the data, either sequentially or in parallel, to achieve higher compression ratios.



### Mathematical Preliminaries for Lossless compression

- Lossless compression is a technique that reduces the size of a data file without losing any information or distorting the original data.
- Lossless compression is based on the concept of **entropy**, which measures the average amount of information per symbol in a data source.
- Entropy is defined as `H(X) = -sum(p(x) log p(x))`, where `X` is a discrete random variable, `p(x)` is the probability of occurrence of symbol `x`, and `log` is the logarithm base 2.
- Entropy is a lower bound for the average number of bits needed to encode each symbol of a data source. The closer the entropy is to the actual encoding length, the more efficient the compression is.
- Lossless compression algorithms use various techniques to reduce the encoding length, such as **run-length encoding**, **Huffman coding**, **arithmetic coding**, **dictionary coding**, and **Lempel-Ziv coding**.
- Run-length encoding is a simple technique that replaces consecutive identical symbols with a pair of the symbol and its count. For example, `AAAAA` can be encoded as `A5`.
- Huffman coding is a technique that assigns variable-length codes to symbols based on their frequencies. The more frequent a symbol is, the shorter its code is. Huffman coding guarantees that no code is a prefix of another code, which makes decoding unambiguous.
- Arithmetic coding is a technique that assigns codes to symbols based on their cumulative probabilities. The code of a symbol is a fraction that lies between the cumulative probabilities of the previous and the next symbol. Arithmetic coding can achieve encoding lengths close to the entropy of the data source.
- Dictionary coding is a technique that builds a dictionary of common patterns or phrases in the data and replaces them with shorter codes. The dictionary can be fixed or adaptive, depending on whether it is predefined or updated during the encoding process.
- Lempel-Ziv coding is a technique that uses a sliding window to find matches between the current and the previous data. The matches are encoded as references to the previous occurrences, which saves bits. Lempel-Ziv coding is adaptive and does not require a dictionary.



### A brief introduction to information theory for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information  .
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding theorems  .
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits. A bit is the basic unit of information that can have two possible values, 0 or 1.
- Information theory often concerns itself with measures of information of the distributions associated with random variables. Some of these measures are:
  - Entropy: the average amount of information contained in a random variable. It represents the uncertainty or unpredictability of the variable. The higher the entropy, the more information is needed to describe the variable.
  - Mutual information: the amount of information that is shared by two random variables. It represents the reduction in uncertainty about one variable given the knowledge of the other. The higher the mutual information, the more dependent the variables are.
  - Channel capacity: the maximum rate at which information can be reliably transmitted over a communication channel. It depends on the characteristics of the channel, such as the noise level and the bandwidth. The higher the channel capacity, the more information can be sent per unit time.
  - Coding theorems: the fundamental limits and methods for compressing and transmitting information over noisy channels. They show that there exists an optimal code for any given source and channel, and that the code can achieve the channel capacity with arbitrarily low error probability.
- Information theory has many applications in various fields, such as communication, cryptography, data compression, machine learning, statistical inference, and thermodynamics   .



### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact original data and allow perfect reconstruction after decompression. Examples of lossless compression techniques are Huffman coding, arithmetic coding, run-length encoding, Lempel-Ziv coding, etc.
- Lossy compression techniques discard some information and allow only approximate reconstruction after decompression. Examples of lossy compression techniques are JPEG, MP3, MPEG, etc.
- Data compression can also be classified into two components: the model and the coder.
- The model component captures the probability distribution of the data by knowing or discovering something about the structure of the input. Examples of models are Markov models, context models, dictionary models, etc.
- The coder component encodes the data according to the model using some coding scheme. Examples of coding schemes are variable-length codes, fixed-length codes, arithmetic codes, etc.
- Model compression is a technique of deploying state-of-the-art deep neural networks in devices with low power and resources, without compromising much on the accuracy of the model.
- Model compression can be achieved by using various techniques, such as pruning, quantization, knowledge distillation, and low-rank factorization.
- Pruning is a technique that reduces the number of parameters in a neural network by removing redundant and inconsequential parameters. These parameters can be connectors, neurons, channels, or even layers. Pruning can be done in different ways, such as weight pruning, unit pruning, filter pruning, etc.
- Quantization is a technique that reduces the precision of the parameters in a neural network by storing them as lower-bit numbers instead of 32-bit floating point numbers. Quantization can be done in different ways, such as uniform quantization, non-uniform quantization, dynamic quantization, etc.
- Knowledge distillation is a technique that transfers the knowledge from a large, complex model (teacher) to a smaller, simpler model (student) by training the student model to mimic the output of the teacher model. Knowledge distillation can be done in different ways, such as soft target distillation, hard target distillation, attention transfer, etc.
- Low-rank factorization is a technique that reduces the complexity of the parameters in a neural network by decomposing them into lower-rank matrices or tensors. Low-rank factorization can be done in different ways, such as singular value decomposition, tensor decomposition, matrix factorization, etc.



### Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Uniform model**: This model assumes that all the symbols in the source data are equally likely to occur. This model is suitable for data that is random or has no structure, such as encrypted data or white noise. The uniform model can be used to calculate the entropy of the source data, which is the lower bound on the compression ratio.

- **Markov model**: This model assumes that the probability of the next symbol in the source data depends only on the previous k symbols, where k is a fixed parameter. This model is useful for data that has some temporal or spatial correlation, such as text, speech, or images. The Markov model can be used to estimate the conditional entropy of the source data, which is the average number of bits needed to encode each symbol given the previous k symbols.

- **Dictionary model**: This model assumes that the source data can be decomposed into a sequence of words, where each word is a substring of the data that has some meaning or significance. This model is effective for data that has some repetition or common patterns, such as natural language, DNA sequences, or executable files. The dictionary model can be used to construct a codebook that maps each word to a unique codeword, and then encode the source data by replacing each word with its corresponding codeword.

- **Transform model**: This model assumes that the source data can be transformed into a different domain, where the data is more compact or sparse. This model is applicable for data that has some frequency or spectral characteristics, such as audio, video, or images. The transform model can be used to apply a linear or nonlinear transformation to the source data, such as the discrete Fourier transform (DFT), the discrete cosine transform (DCT), or the wavelet transform, and then encode the transformed coefficients using a suitable coding scheme.



### Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to the possible symbols or sequences of symbols that the source can generate.
- A probability model can be used to design and analyze data compression algorithms, which aim to reduce the number of bits needed to represent the data.
- There are different types of probability models, depending on the assumptions and the level of detail about the source. Some common ones are:

  - **Uniform model**: This model assumes that all the symbols in the alphabet have the same probability of occurrence. For example, if the alphabet is A = {a, b, c, d}, then P(a) = P(b) = P(c) = P(d) = 0.25. This model is simple but often unrealistic, as some symbols may be more frequent than others in the data.
  - **Empirical model**: This model estimates the probabilities of the symbols from the data itself, by counting the frequencies of each symbol and dividing by the total number of symbols. For example, if the data is abcdabcd, then P(a) = P(b) = P(c) = P(d) = 0.25. This model is more realistic but may not capture the underlying structure or patterns of the data.
  - **Markov model**: This model assumes that the probability of the next symbol depends only on the previous k symbols, where k is a fixed parameter. For example, if k = 1, then P(a|b) is the probability of a given that the previous symbol was b. This model can capture some local dependencies or context in the data, but may not account for long-range correlations or higher-order structure.
  - **Probabilistic grammar model**: This model assumes that the data is generated by a set of rules or productions, which specify how to combine symbols or sequences of symbols into larger sequences. For example, a rule could be S -> AB, which means that a sequence S can be replaced by a sequence AB. This model can capture some global structure or regularity in the data, but may not account for variations or exceptions.

- A probability model can be used to compute the entropy of the source, which is a measure of the average uncertainty or information content of the data. The entropy is defined as:

  - H(X) = - sum(P(x) * log(P(x))) for all x in A
  - where X is a random variable that represents the source, A is the alphabet, P(x) is the probability of symbol x, and log is the logarithm base 2.
  - The entropy is the lower bound on the average number of bits per symbol that any lossless compression algorithm can achieve. The closer the entropy is to the actual compression ratio, the more efficient the algorithm is.

- A probability model can also be used to design a coding scheme, which is a way of assigning binary codes to the symbols or sequences of symbols in the data. A coding scheme can be optimal, meaning that it achieves the entropy, or suboptimal, meaning that it uses more bits than the entropy. Some common coding schemes are:

  - **Fixed-length code**: This code assigns the same number of bits to each symbol, regardless of its probability. For example, if the alphabet is A = {a, b, c, d}, then a possible code is a -> 00, b -> 01, c -> 10, d -> 11. This code is simple but often wasteful, as some symbols may be more frequent than others and deserve shorter codes.
  - **Variable-length code**: This code assigns different numbers of bits to different symbols, depending on their probabilities. For example, if the alphabet is A = {a, b, c, d}, and P(a) = 0.5, P(b) = 0.25, P(c) = 0.125, P(d) = 0.125, then a possible code is a -> 0, b -> 10, c -> 110, d -> 111. This code is more efficient but may not be optimal, as some codes may be longer than necessary or not uniquely decodable.
  - **Prefix code**: This code is a special type of variable-length code, where no code is a prefix of another code. This means that the code can be uniquely decoded from left to right, without any ambiguity or need for separators. For example, the code in the previous example is a prefix code, but a -> 0, b -> 01, c -> 011, d -> 111 is



### Markov models for data compression

- A Markov model is a mathematical model that describes a system that changes its state according to some probabilistic rules. The system is assumed to have the Markov property, which means that the future state of the system depends only on the current state and not on the past history.
- A Markov model can be used to model the source of a data stream, such as a text, an image, or a speech signal. The model can capture the statistical regularities and patterns in the data, and can be used to predict the next symbol in the stream based on the previous symbols.
- A Markov model can also be used as a basis for data compression, which is the process of reducing the size of a data stream without losing any information. The idea is to use the model to encode the data stream in a way that exploits the redundancy and correlation in the data, and to use the same model to decode the data stream at the receiver end.
- One way to use a Markov model for data compression is to combine it with an arithmetic coding scheme, which is a method of encoding symbols based on their probabilities. The arithmetic coding scheme assigns a variable-length code to each symbol, such that the more probable symbols have shorter codes and the less probable symbols have longer codes. The code is generated by dividing a unit interval into subintervals according to the symbol probabilities, and then recursively subdividing the subinterval corresponding to the symbol to be encoded.
- A Markov model can provide the symbol probabilities for the arithmetic coding scheme, by estimating the probability of each symbol given the previous symbols in the data stream. The Markov model can be dynamically updated as new symbols are observed, so that it adapts to the changing characteristics of the data stream. This makes the compression scheme adaptive and efficient.
- An example of a data compression algorithm that uses a dynamic Markov model and arithmetic coding is the Dynamic Markov Compression (DMC) algorithm, developed by Gordon Cormack and Nigel Horspool . The DMC algorithm predicts one bit at a time, rather than one byte at a time, which makes it slower but gives slightly better compression than other methods. The DMC algorithm has been used as a model or submodel in several highly experimental implementations.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of composite source model for data compression:

### Composite source model for data compression

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub>.
- A composite source model is useful for applications where a single model is not sufficient to capture the characteristics of the data, such as images, speech, text, etc. 
- A composite source model can reduce the source modeling entropy, which is the lower bound of the average number of bits per symbol needed to encode the data, by exploiting the correlations and dependencies among the different sources.
- A composite source model can be combined with different coding techniques, such as Huffman coding, arithmetic coding, run-length encoding, etc., to achieve efficient data compression.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes for the Unit 1 - Compression Techniques:

```markdown
# Unit 1 - Compression Techniques

## Introduction

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be applied to different types of data, such as text, images, audio, video, etc.
- Data compression can be classified into two categories: lossless and lossy.

## Lossless Compression

- Lossless compression is a compression technique that preserves the exact original data after decompression.
- Lossless compression is useful for data that requires high accuracy and fidelity, such as text, source code, medical images, etc.
- Lossless compression algorithms exploit the redundancy and regularity in the data to reduce the number of bits needed to represent it.
- Some examples of lossless compression algorithms are: Huffman coding, Run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, etc.

## Lossy Compression

- Lossy compression is a compression technique that discards some information from the original data to achieve higher compression ratios.
- Lossy compression is suitable for data that can tolerate some degradation in quality, such as audio, video, natural images, etc.
- Lossy compression algorithms exploit the perceptual limitations of human senses to remove the information that is less noticeable or less important.
- Some examples of lossy compression algorithms are: JPEG, MP3, MPEG, etc.

## Compression Metrics

- Compression metrics are used to measure the performance and effectiveness of compression algorithms.
- Some common compression metrics are: compression ratio, bit rate, distortion, quality, etc.

### Compression Ratio

- Compression ratio (CR) is the ratio of the size of the original data to the size of the compressed data.
- CR = Original size / Compressed size
- Higher CR means higher compression and smaller file size.

### Bit Rate

- Bit rate (BR) is the number of bits per second (bps) required to transmit or store the compressed data.
- BR = Compressed size / Duration
- Lower BR means lower bandwidth or storage requirements.

### Distortion

- Distortion (D) is the measure of the difference or error between the original data and the decompressed data.
- D = Original data - Decompressed data
- Lower D means higher fidelity and quality.

### Quality

- Quality (Q) is the subjective or objective evaluation of the perceptual or functional quality of the decompressed data.
- Q can be measured by various methods, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc.
- Higher Q means higher satisfaction and usability.
```



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln and code symbols from an alphabet of size D, the following inequality holds:

  - Sum of D^(-li) from i = 1 to n <= 1

- The Kraft inequality can be extended to any uniquely decodable code by adding dummy code symbols to make it prefix-free.



# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in data compression, because they can achieve optimal or near-optimal compression ratios for various probability distributions of symbols .
- Some examples of prefix codes are Huffman codes, arithmetic codes, Elias codes, Golomb codes and universal codes .
- A universal code is a special kind of prefix code that can compress any monotonic probability distribution of integers (i.e., p(i) ≥ p(i + 1) for all positive i) within a constant factor of the optimal code.
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- To encode a message using a prefix code, one can traverse the binary tree from the root to the leaf that matches each symbol, and output the bits along the path.
- To decode a message using a prefix code, one can traverse the binary tree from the root to the leaf that matches each bit sequence, and output the symbol at the leaf.
- The expected length of a prefix code for a given probability distribution of symbols is the sum of the products of the codeword lengths and the symbol probabilities.
- The optimal prefix code for a given probability distribution of symbols is the one that minimizes the expected length.
- Huffman coding is a popular algorithm for constructing the optimal prefix code for a given probability distribution of symbols.
- Huffman coding works by creating a binary tree from the bottom up, by merging the two least probable symbols at each step, until only one node remains as the root.
- The codeword for each symbol is obtained by reading the bits along the path from the root to the leaf that corresponds to the symbol.
- Huffman coding can achieve the optimal compression ratio for any discrete memoryless source, which is a source that produces symbols independently and with fixed probabilities.
- Huffman coding can also be generalized to adaptive Huffman coding, which can adjust the codewords dynamically based on the changing probabilities of symbols in the input stream.



## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a method of lossless data compression that assigns variable-length codes to symbols based on their frequencies of occurrence.

The main steps of the algorithm are:

- Create a frequency table that counts the number of occurrences of each symbol in the data.
- Create a priority queue of nodes, where each node represents a symbol and its frequency. The nodes with the lowest frequencies have the highest priority.
- While the queue has more than one node, do the following:
  - Dequeue the two nodes with the highest priority (lowest frequency) from the queue.
  - Create a new internal node with the sum of the frequencies of the two nodes as its frequency, and the two nodes as its left and right children.
  - Enqueue the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree.
- Traverse the Huffman tree and assign codes to the symbols. The code of a symbol is the sequence of bits that corresponds to the path from the root to the leaf node that represents the symbol. A left branch is represented by a 0 bit, and a right branch by a 1 bit.
- Encode the data by replacing each symbol with its code.
- Decode the data by following the bits from the root to the leaves of the Huffman tree.

The Huffman coding algorithm has the following properties:

- It is optimal, meaning that it produces the shortest possible code for a given set of symbols and frequencies.
- It is prefix-free, meaning that no code is a prefix of another code. This ensures that the encoded data can be uniquely decoded.
- It is adaptive, meaning that it can adjust to the changing frequencies of the symbols in the data. This can be done by updating the frequency table and the Huffman tree periodically.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies or probabilities of occurrence.
- The goal of Huffman coding is to minimize the expected value of the code length, or the average number of bits per symbol.
- The code length of a symbol is the number of bits in its corresponding code word. For example, if a symbol has a code word of 101, its code length is 3 bits.
- The code variance of a Huffman code is the difference between the maximum and minimum code lengths. For example, if the code lengths range from 2 to 4 bits, the code variance is 2.
- A minimum variance Huffman code is a Huffman code that has the smallest possible code variance among all Huffman codes with the same expected code length.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in non-increasing order of their frequencies or probabilities.
  - Create a binary tree with a leaf node for each symbol.
  - While there are more than two nodes in the tree, do the following:
    - Find the two nodes with the smallest frequencies or probabilities and merge them into a new node with their sum as its frequency or probability.
    - If there are more than two nodes with the same smallest frequency or probability, choose the two nodes that are farthest to the right in the sorted list.
    - Insert the new node into the sorted list in the appropriate position.
  - Assign a bit (0 or 1) to each edge of the tree, starting from the root and going down to the leaves.
  - The code word for each symbol is the sequence of bits along the path from the root to its leaf node.
- A minimum variance Huffman code has the following properties:
  - It is a prefix code, meaning that no code word is a prefix of another code word.
  - It is optimal, meaning that it minimizes the expected code length among all prefix codes.
  - It is unique, meaning that there is only one minimum variance Huffman code for a given set of symbol frequencies or probabilities.
  - It is balanced, meaning that the difference between the depths of any two leaf nodes is at most one.
- An example of a minimum variance Huffman code is shown below:

| Symbol | Probability | Code word | Code length |
|--------|-------------|-----------|-------------|
| a1     | 0.2         | 00        | 2           |
| a2     | 0.2         | 01        | 2           |
| a3     | 0.25        | 10        | 2           |
| a4     | 0.05        | 1100      | 4           |
| a5     | 0.15        | 1101      | 4           |
| a6     | 0.15        | 111       | 3           |

- The expected code length for this code is 2.45 bits per symbol.
- The code variance for this code is 2 bits.
- The entropy of the source is 2.405 bits per symbol.
- The efficiency of the code is 98.16%.



### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data.  

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or changing over time.
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than static Huffman coding, since the code tree has to be modified frequently.
- It may not perform well for very small or very large data sets, since the code may not have enough time to adapt or may become too complex.
- It may introduce some overhead in the encoded data, since the code tree has to be transmitted along with the symbols.

There are different algorithms for implementing adaptive Huffman coding, such as FGK algorithm and Vitter algorithm. They differ in how they update the code tree and how they handle the special case of new symbols that have not been seen before.  

A general procedure for adaptive Huffman coding is:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet.
- For each symbol in the input data:
  - If the symbol has been seen before, encode it using the current code tree and update the frequencies of the nodes along the path from the symbol to the root.
  - If the symbol is new, encode the NYT node using the current code tree, then encode the symbol using a fixed-length code (such as ASCII), and add a new node for the symbol as a child of the NYT node. Update the frequencies of the nodes along the path from the new node to the root.
  - If the code tree violates the sibling property (which states that the nodes with the same frequency should be ordered by increasing symbol value), swap the nodes to restore the property and update the codes accordingly.

A general procedure for adaptive Huffman decoding is:

- Initialize the code tree with a single node, called the NYT node, which represents all the symbols that have not been seen yet.
- For each code in the encoded data:
  - If the code corresponds to an existing node in the code tree, decode it as the symbol represented by that node and update the frequencies of the nodes along the path from the node to the root.
  - If the code corresponds to the NYT node, decode the next fixed-length code as a new symbol, add a new node for the symbol as a child of the NYT node, and update the frequencies of the nodes along the path from the new node to the root.
  - If the code tree violates the sibling property, swap the nodes to restore the property and update the codes accordingly.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression:

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the data.
- The algorithm works by creating a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols. The frequency of each node is the sum of the frequencies of its children.
- The algorithm starts by creating a node for each symbol and placing them in a priority queue, ordered by their frequencies. Then, it repeatedly removes the two nodes with the lowest frequencies from the queue, creates a new node with the sum of their frequencies as its frequency, and makes the two nodes its left and right children. The new node is then inserted back into the queue. This process is repeated until there is only one node left in the queue, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to the symbol, and appending a 0 for each left branch and a 1 for each right branch along the way. The code is then reversed to get the final code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible code for each symbol, given its frequency. The average code length is equal to the entropy of the data, which is the lower bound for any lossless compression technique.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video. However, it requires the knowledge of the frequencies of the symbols in the data, which may not be available or may change over time. In such cases, adaptive Huffman coding can be used, which updates the tree and the codes as new symbols are encountered in the data.



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies . It is also known as data compression encoding. The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized. Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol. Huffman coding is generally useful to compress the data in which there are frequently occurring characters.

The encoding procedure for the Huffman coding algorithm can be summarized as follows  :

- Step 1: Create a leaf node for each character and assign it a weight (frequency of appearance) of the character. Add all the nodes to a priority queue (min-heap) based on their weights.
- Step 2: Extract two nodes with the minimum weights from the priority queue. Create a new internal node with the sum of the weights of the two nodes as its weight. Make the first extracted node as its left child and the second extracted node as its right child. Add this node to the priority queue.
- Step 3: Repeat step 2 until there is only one node left in the priority queue. This node is the root of the Huffman tree.
- Step 4: Traverse the Huffman tree and assign codes to each character. Start from the root and assign 0 to the left edge and 1 to the right edge. Concatenate the edge labels along the path from the root to the leaf to get the code for each character.
- Step 5: Use the codes to encode the input data. Replace each character with its corresponding code and output the compressed data.

Here is an example of Huffman coding for the string "BCCABBDDAECCBBAEDDCC":

- Step 1: Create a leaf node for each character and assign it a weight of the character. Add all the nodes to a priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| A         | 2         | A:2  |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |
| E         | 2         | E:2  |

- Step 2: Extract two nodes with the minimum weights from the priority queue. Create a new internal node with the sum of the weights of the two nodes as its weight. Make the first extracted node as its left child and the second extracted node as its right child. Add this node to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| A         | 2         | A:2  |
| E         | 2         | E:2  |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |

Extract A:2 and E:2 and create a new node AE:4 with A:2 as the left child and E:2 as the right child. Add AE:4 to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| AE        | 4         | AE:4 |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |

Extract AE:4 and B:5 and create a new node BAE:9 with AE:4 as the left child and B:5 as the right child. Add BAE:9 to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| C         | 6         | C:6  |
| D         | 5         | D:5  |
| BAE       | 9         | BAE:9|

Extract C:6 and D:5 and create a new node CD:11 with C:6 as the left child and D:5 as the right child. Add CD:11 to the priority queue.

| Character | Frequency | Node |
|-----------



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression:

### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the source data.
- The Huffman code is a prefix code, which means that no code is a prefix of another code. This property ensures that the code is uniquely decodable.
- The decoding procedure for the Huffman code is the reverse of the encoding procedure. It involves the following steps:

  1. Construct the Huffman tree from the code table or the frequency table. The Huffman tree is a binary tree that represents the code assignments. Each leaf node corresponds to a symbol and its code. Each internal node corresponds to a prefix of some codes. The root node corresponds to the empty prefix.
  2. Read the encoded data bit by bit from left to right. Start from the root node of the Huffman tree and traverse the tree according to the bits. If the bit is 0, go to the left child. If the bit is 1, go to the right child.
  3. When a leaf node is reached, output the symbol associated with that node and return to the root node. Repeat step 2 until all the bits are processed.
  4. The output is the decoded data, which is identical to the original source data.

- Example: Suppose the following code table is given for a source alphabet of four symbols: A, B, C, and D.

| Symbol | Code |
|--------|------|
| A      | 0    |
| B      | 10   |
| C      | 110  |
| D      | 111  |

- The Huffman tree for this code table is shown below:

```
     *
    / \
   0   1
  /     \
 A       *
        / \
       0   1
      /     \
     B       *
            / \
           0   1
          /     \
         C       D
```

- To decode the encoded data 1011011110, we apply the decoding procedure as follows:

  - Start from the root node and read the first bit 1. Go to the right child.
  - Read the next bit 0. Go to the left child. Reach a leaf node B. Output B and return to the root node.
  - Read the next bit 1. Go to the right child.
  - Read the next bit 1. Go to the right child. Reach a leaf node D. Output D and return to the root node.
  - Read the next bit 0. Go to the left child. Reach a leaf node A. Output A and return to the root node.
  - Read the next bit 1. Go to the right child.
  - Read the next bit 1. Go to the right child.
  - Read the next bit 0. Go to the left child. Reach a leaf node C. Output C and return to the root node.
  - Read the next bit 1. Go to the right child.
  - Read the next bit 1. Go to the right child. Reach a leaf node D. Output D and return to the root node.
  - No more bits to read. Stop the decoding procedure.

- The output is the decoded data BDAACD, which is the same as the original source data.



### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to encode integers with a geometric distribution.
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r.
- The binary code for r depends on whether M is a power of 2 or not:
  - If M is a power of 2, say M = 2^n, then r is encoded using n bits in standard binary representation.
  - If M is not a power of 2, say M = 2^n + k, then r is encoded using one of the following methods:
    - Rice coding: if r < 2^n, use n bits; otherwise, use n+1 bits and add 2^n to r.
    - Elias coding: use n bits for the first 2^n - k values of r; for the remaining k values, use n+1 bits and subtract k from r.
    - Quasi-Elias coding: use n bits for the first M - 2^n values of r; for the remaining 2^n values, use n+1 bits and add M - 2^n to r.
- Golomb codes are optimal for encoding a geometric distribution with parameter p when M is chosen to be the closest integer to -1/log(1-p).
- Golomb codes are widely used in data compression, especially for lossless compression of images and audio.

: https://www.geeksforgeeks.org/python-golomb-encoding-for-b2n-and-b2n/
: https://www.sciencedirect.com/topics/engineering/golomb-code
: https://en.wikipedia.org/wiki/Golomb_coding



### Rice codes

- Rice codes are a subset of Golomb codes, which are a family of prefix codes that can efficiently encode positive integers .
- Rice codes are named after Robert F. Rice, who used them in an adaptive coding scheme.
- Rice codes depend on a parameter k, which determines the length of the unary part and the binary part of the code .
- The unary part of the code is a sequence of k zeros followed by a one, which indicates the quotient of the integer divided by 2^k^.
- The binary part of the code is the remainder of the integer divided by 2^k^, represented in k bits.
- For example, if k = 2 and the integer is 9, then the quotient is 2 and the remainder is 1. The unary part is 001 and the binary part is 01. The Rice code is 00101.
- Rice codes are optimal when the integers follow a geometric distribution with parameter 1/2^k^ .
- Rice codes are often used to encode entropy in audio and video codecs, where most of the values are small .



### Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression .
- Tunstall codes are based on the idea of parsing a stochastic source with codewords of variable length, and then encoding each codeword with a fixed-length code .
- Tunstall codes are a precursor to Lempel–Ziv codes, which are widely used in practice.
- Tunstall codes have the following properties :
  - They are prefix codes, meaning that no codeword is a prefix of another codeword.
  - They are optimal for sources that have a geometric distribution of probabilities, such as run-length encoding.
  - They have a fixed compression ratio, which is equal to the ratio of the source entropy to the codeword length.
  - They are easy to construct and decode, using a tree structure and a table lookup.
- Tunstall codes can be constructed as follows :
  - Start with a set of symbols, each with a probability of occurrence.
  - Assign each symbol a codeword of the same length, such as a binary digit.
  - Expand the set of codewords by appending each symbol to each existing codeword, and update the probabilities accordingly.
  - Repeat the expansion until the desired codeword length is reached, or until all possible codewords are exhausted.
  - Prune the tree of codewords by removing any unused or incomplete codewords, and assign a fixed code to each remaining codeword.
- Tunstall codes can be decoded as follows :
  - Read a fixed-length codeword from the input stream, and look up its corresponding variable-length codeword in the table.
  - Output the symbols in the variable-length codeword, and repeat until the end of the input stream is reached.



### Applications of Huffman coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or weight. The more frequent a data value is, the shorter its code will be. The less frequent a data value is, the longer its code will be. This way, the data can be represented with fewer bits on average, saving space and bandwidth.

Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel, reducing the transmission time and cost. For example, the ASCII code uses 8 bits to represent each character, but with Huffman coding, the characters can be encoded with fewer bits depending on their frequency in the text or fax.

- **Conventional compression formats**: Huffman coding is often used by compression formats like PKZIP, GZIP, BZIP2, etc. to compress the data files before storing or transferring them. These formats use Huffman coding along with other techniques like run-length encoding, dictionary encoding, etc. to achieve higher compression ratios .

- **Multimedia codecs**: Huffman coding is also used by multimedia codecs like JPEG, PNG, and MP3 to compress the images, audio, and video data. These codecs use Huffman coding along with other techniques like quantization, transform coding, etc. to reduce the size of the multimedia data while preserving the quality. For example, JPEG uses Huffman coding to encode the coefficients of the discrete cosine transform of the image blocks .



### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequencies of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the image.
  - Sort the symbols in the frequency table in ascending order of frequency.
  - Build a binary tree by repeatedly merging the two least frequent symbols into a new node with a frequency equal to the sum of their frequencies. The merged symbols become the left and right children of the new node. Repeat this process until there is only one node left, which is the root of the tree.
  - Assign a binary code to each symbol by traversing the tree from the root to the leaf. Append a 0 to the code when moving to the left child and a 1 when moving to the right child.
  - Encode the image by replacing each symbol with its corresponding binary code.
  - Decode the image by traversing the tree from the root to the leaf according to the binary code and outputting the symbol at the leaf.

- Huffman coding is optimal for images that have a skewed distribution of symbols, meaning that some symbols are much more frequent than others.
- Huffman coding can achieve a compression ratio of up to 50% for grayscale images and up to 25% for color images.
- Huffman coding is simple, fast, and widely used in lossless compression standards such as JPEG, PNG, and ZIP.



```
### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The steps of the Huffman coding algorithm are  :
  - Create a leaf node for each character and add them to a priority queue based on their frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with the sum of their frequencies as its frequency and the two nodes as its left and right children.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each character. The left edge is 0 and the right edge is 1.
- To compress a text file, replace each character with its corresponding code and write the output in binary format.
- To decompress a compressed file, read the file bit by bit and follow the Huffman tree from the root to the leaf. When a leaf is reached, output the character and return to the root.
- The advantages of Huffman coding are  :
  - It is optimal, meaning it generates the shortest possible codes for a given set of characters and frequencies.
  - It is lossless, meaning no information is lost during compression or decompression.
  - It is simple and efficient, meaning it can be easily implemented and executed.
- The disadvantages of Huffman coding are  :
  - It requires the knowledge of the frequencies of the characters in advance, which may not be available or accurate.
  - It requires the storage or transmission of the Huffman tree along with the compressed file, which adds some overhead.
  - It is not suitable for compressing files that have a uniform distribution of characters, as it will not reduce the size significantly.
```



### Audio Compression

Audio compression is the process of reducing the amount of data required to represent an audio signal. Audio compression can be lossy or lossless, depending on whether the original signal can be perfectly reconstructed from the compressed data or not.

One of the techniques used for lossless audio compression is the Huffman coding algorithm, which assigns variable-length codes to the symbols in the source data based on their frequencies of occurrence. The Huffman coding algorithm can be summarized as follows:

- Create a frequency table that counts the number of occurrences of each symbol in the source data.
- Create a priority queue of nodes, where each node represents a symbol and its frequency. The nodes with the lowest frequencies have the highest priority.
- While the queue has more than one node, do the following:
  - Dequeue the two nodes with the highest priority (lowest frequency) from the queue.
  - Create a new node with the sum of the frequencies of the two nodes as its frequency, and the two nodes as its left and right children.
  - Enqueue the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree, which encodes the symbols as follows:
  - Traverse the tree from the root to the leaves, assigning a 0 to each left branch and a 1 to each right branch.
  - The code for each symbol is the sequence of bits along the path from the root to the leaf corresponding to that symbol.
- To compress the source data, replace each symbol with its code from the Huffman tree.
- To decompress the compressed data, traverse the Huffman tree from the root, following the bits in the compressed data. When a leaf is reached, output the symbol corresponding to that leaf and return to the root.

The Huffman coding algorithm is optimal for lossless compression, meaning that it produces the shortest possible codes for a given source data. However, it has some limitations, such as:

- It requires the knowledge of the frequency table or the Huffman tree to decompress the data, which adds some overhead to the compressed data.
- It assumes that the symbols are independent and identically distributed, which may not be true for some types of audio data, such as speech or music.
- It does not exploit the temporal or spectral redundancy in the audio data, which can be exploited by other techniques, such as differential coding or transform coding.



## Unit 3 - Coding a sequence

- A sequence is a set of ordered values or items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula, a table, a graph, or a list of values.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term or the initial value of the sequence.
  - Define the rule or the function that determines the next term based on the previous term or the position of the term in the sequence.
  - Use a loop or a recursion to iterate over the sequence and generate the desired number of terms or until a certain condition is met.
  - Store the sequence in a data structure, such as an array, a list, or a vector, that can hold multiple values of the same type.
  - Display or return the sequence as the output of the program or the function.

- For example, to code the sequence 2, 4, 6, 8, ..., we can use the following Python code:

```python
# Define the first term of the sequence
first_term = 2

# Define the rule of the sequence
def rule(n):
  # The next term is 2 more than the previous term
  return n + 2

# Define the number of terms to generate
num_terms = 10

# Create an empty list to store the sequence
sequence = []

# Use a for loop to iterate over the sequence
for i in range(num_terms):
  # Append the current term to the list
  sequence.append(first_term)
  # Update the first term to the next term using the rule
  first_term = rule(first_term)

# Print the sequence
print(sequence)
```

- The output of the code is:

```python
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

- This is the end of Unit 3 - Coding a sequence.



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits than the original representation.
- A binary code is a way of representing data using only two symbols, usually 0 and 1.
- A binary code can be fixed-length or variable-length, depending on whether all the codewords have the same number of bits or not.
- A fixed-length binary code can be inefficient if the symbols have different frequencies in the data, as some symbols may be assigned more bits than necessary.
- A variable-length binary code can be more efficient if it assigns shorter codewords to more frequent symbols and longer codewords to less frequent symbols.
- A variable-length binary code must be prefix-free, meaning that no codeword is a prefix of any other codeword, to avoid ambiguity in decoding.
- One example of a variable-length binary code is Huffman coding, which is a lossless bit compression technique that builds a binary tree based on the frequencies of the symbols and assigns codewords according to the path from the root to the leaf.
- Another example of a variable-length binary code is LZW coding, which is a dictionary-based compression technique that builds a code table of sequences of bytes and assigns codewords according to the index of the sequence in the table.
- A universal code for integers is a special type of variable-length binary code that can encode any positive integer with a prefix code that is optimal for any monotonic probability distribution.
- Some examples of universal codes for integers are unary code, Elias gamma code, Elias delta code, and Fibonacci code.



# Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using only two symbols, usually 0 and 1. Each symbol is called a bit, and a sequence of bits is called a binary code. Binary coding is used to store and transmit data in computers and digital devices.
- Huffman coding is a form of lossless compression which makes files smaller using the frequency with which characters appear in a message. Huffman coding assigns variable length binary codes for each input character in the text file. The length of the binary code depends on the frequency of the character in the file. The most frequent characters are coded with the smaller binary words, thus, the size used to code them is minimal, which increases the compression.
- The main difference between binary and Huffman coding is that binary coding uses fixed length codes for all characters, while Huffman coding uses variable length codes for different characters. Binary coding is simpler and faster, but Huffman coding is more efficient and reduces the file size more.
- Some advantages of Huffman coding over binary coding are:
  - Huffman coding can achieve a compression ratio of more than 50%, which means that the compressed file is less than half the size of the original file .
  - Huffman coding is optimal, which means that no other prefix code can achieve a better compression for the same input.
  - Huffman coding is adaptive, which means that it can adjust to the changing frequencies of the characters in the input.
- Some disadvantages of Huffman coding compared to binary coding are:
  - Huffman coding requires more computation and memory to construct and store the Huffman tree, which is a data structure that represents the codes for each character.
  - Huffman coding requires an extra header to store the Huffman tree or the code table, which adds some overhead to the compressed file.
  - Huffman coding is not suitable for compressing files that have a uniform distribution of characters, as the compression ratio will be low or even negative.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some applications for the notes of the Unit 3 - Coding a sequence:

### Applications for the notes of the Unit 3 - Coding a sequence

- Coding a sequence is a technique to represent a sequence of symbols or data using fewer bits or characters than the original representation. It can be used to reduce the storage space, transmission time, or bandwidth required for the sequence.
- Coding a sequence can be applied to various types of data, such as text, images, audio, video, or genomic data. Some examples of applications are:

  - Text compression: Coding a sequence can be used to compress text files, such as documents, emails, or web pages, by using codes that are shorter for more frequent symbols or words. For example, Huffman coding, arithmetic coding, or Lempel-Ziv coding are some common methods for text compression.
  - Image compression: Coding a sequence can be used to compress image files, such as photographs, graphics, or icons, by using codes that are shorter for more common pixel values or patterns. For example, run-length encoding, JPEG, or PNG are some common methods for image compression.
  - Audio compression: Coding a sequence can be used to compress audio files, such as music, speech, or sound effects, by using codes that are shorter for more common sound samples or frequencies. For example, MP3, AAC, or FLAC are some common methods for audio compression.
  - Video compression: Coding a sequence can be used to compress video files, such as movies, animations, or games, by using codes that are shorter for more common frames or regions. For example, MPEG, H.264, or HEVC are some common methods for video compression.
  - Genomic compression: Coding a sequence can be used to compress genomic data, such as DNA or RNA sequences, by using codes that are shorter for more common nucleotides or motifs. For example, DNAzip, Gzip, or CRAM are some common methods for genomic compression.

- Coding a sequence can also be used for other purposes, such as encryption, error detection, or error correction. For example, coding a sequence can be used to encrypt a message by using a secret key to generate a code that is hard to decipher without the key. Coding a sequence can also be used to detect or correct errors in a transmission by using codes that have certain properties, such as parity, checksum, or Hamming distance.



### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image.
- The JBIG standard (Joint Bi-level Image Experts Group) is an early lossless image compression standard for bi-level images, standardized as ISO/IEC 11544 and as ITU-T T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines and can also be used on other bi-level images.
- The JBIG standard offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement.
- The JBIG standard uses a combination of arithmetic coding and adaptive template matching to achieve high compression ratios.
- The JBIG standard has four modes of operation: sequential, progressive, enhanced and lossy.
- The sequential mode encodes the image in one pass, using a fixed template and a context-dependent probability model.
- The progressive mode encodes the image in multiple passes, starting with a low-resolution version and refining it with higher-resolution layers.
- The enhanced mode encodes the image in one pass, using a variable template and a context-dependent probability model.
- The lossy mode encodes the image in one pass, using a fixed template and a context-independent probability model.
- The JBIG standard has been superseded by the JBIG2 standard, which is a newer bi-level image compression standard that is suitable for both lossless and lossy compression .
- The JBIG2 standard uses model-based coding for text and halftones, and nearby neighbor based coding for generic bi-level images.
- The JBIG2 standard can achieve compression ratios of up to 100:1 for lossless compression and up to 400:1 for lossy compression.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG, the previous standards for bi-level image compression .
- JBIG2 can achieve much higher compression ratios than the previous standards by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution means that JBIG2 can identify and group similar regions of an image, such as characters or symbols, and assign them a unique code. Then, instead of storing the pixel values of each region, JBIG2 can store only the code and the location of each region.
- JBIG2 can segment an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and apply compression techniques that are specially optimized for each type of content .
- Text regions are compressed by using a dictionary of symbols and a refinement coding method that encodes the differences between similar symbols.
- Halftone regions are compressed by using a template matching method that encodes the periodicity and the phase of the halftone pattern.
- Generic regions are compressed by using a context-based arithmetic coding method that encodes the pixel values based on the surrounding pixels.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used for compressing scanned documents, such as PDF files, and is supported by many software applications and hardware devices .



# Image compression

Image compression is a process applied to a graphics file to minimize its size in bytes without degrading image quality below an acceptable threshold . By reducing the file size, more images can be stored in a given amount of disk or memory space. Image compression also reduces the bandwidth required to transmit or download images over the internet.

## Types of image compression

There are two main types of image compression: lossless and lossy.

- Lossless compression preserves the original image data exactly, without any loss of information. Lossless compression algorithms use techniques such as run-length encoding, Huffman coding, Lempel-Ziv-Welch (LZW) coding, and arithmetic coding to reduce the redundancy in the image data. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, and logos. Some common lossless image formats are PNG, TIFF, GIF, and BMP.

- Lossy compression discards some of the image data, resulting in some loss of quality. Lossy compression algorithms use techniques such as quantization, transform coding, and entropy coding to reduce the correlation and complexity in the image data. Lossy compression is suitable for images that can tolerate some degradation, such as natural scenes, photographs, and web graphics. Some common lossy image formats are JPEG, JPEG 2000, WebP, and HEIF.

## Factors affecting image compression

The amount of compression that can be achieved by an image compression algorithm depends on several factors, such as:

- The image format: Different image formats use different compression algorithms and have different capabilities and limitations. For example, JPEG is a lossy format that can achieve high compression ratios but may introduce artifacts such as blocking and ringing. PNG is a lossless format that can preserve the image quality but may not achieve high compression ratios.

- The image content: Different images have different characteristics and properties that affect the compression performance. For example, images with smooth regions, low contrast, and low frequency components are easier to compress than images with sharp edges, high contrast, and high frequency components.

- The image quality: The quality of an image is a subjective measure of how well the image represents the original scene or object. The quality of an image can be affected by the compression algorithm, the compression ratio, and the compression parameters. For example, increasing the compression ratio may reduce the file size but also degrade the image quality. Adjusting the compression parameters such as the bit rate, the quantization level, and the quality factor may trade off the file size and the image quality.

## Methods of image compression

There are many methods and techniques that can be used to perform image compression, such as:

- Run-length encoding (RLE): RLE is a simple lossless compression technique that replaces consecutive identical pixels with a single pixel value and a count of how many times it occurs. For example, the sequence of pixels 111111222233333 can be encoded as 16162353. RLE is effective for images with large areas of uniform color, such as cartoons and logos.

- Huffman coding: Huffman coding is a lossless compression technique that assigns variable-length codes to the pixels based on their frequency of occurrence. The more frequent pixels are assigned shorter codes and the less frequent pixels are assigned longer codes. For example, if the pixel values 0, 1, 2, and 3 occur with probabilities 0.5, 0.25, 0.125, and 0.125, respectively, they can be encoded as 0, 10, 110, and 111. Huffman coding is effective for images with non-uniform pixel distributions, such as natural scenes and photographs.

- Lempel-Ziv-Welch (LZW) coding: LZW coding is a lossless compression technique that builds a dictionary of variable-length codes for the pixels based on their patterns of occurrence. The dictionary is initialized with the basic pixel values and is updated dynamically as new patterns are encountered. For example, if the pixel values 0, 1, 2, and 3 are used, the dictionary can be initialized as {0:0, 1:1, 2:2, 3:3}. If the sequence of pixels 012301230123 is encountered, the dictionary can be updated as {0:0, 1:1, 2:2, 3:3, 01:4, 23:5, 012:6, 301:7, 230:8, 123:9} and the sequence can be



### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the redundancy and the size of the data.
- There are many variants of dictionary techniques, such as LZ77, LZ78, LZW, LZSS, LZMA, etc. They differ in how they construct and update the dictionary, how they encode and decode the matches, and how they handle the cases when no match is found.
- Dictionary techniques are suitable for compressing natural language texts, as they can exploit the common words and phrases that appear frequently. They can also be used for other types of data, such as images, audio, and video, but they may require some modifications or enhancements to achieve better compression ratios.



### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or distorting its meaning.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, redundancy, and lossless or lossy compression.
- Encoding is the process of transforming data into a different format that uses fewer bits or symbols.
- Decoding is the process of recovering the original data from the encoded format.
- Entropy is a measure of the uncertainty or randomness of data. It indicates the minimum number of bits or symbols needed to represent the data without loss of information.
- Redundancy is the amount of extra or unnecessary information in data that can be removed or replaced without affecting its meaning.
- Lossless compression is a type of compression that preserves the exact information of the original data. It allows the original data to be reconstructed perfectly from the compressed data.
- Lossy compression is a type of compression that discards some information of the original data. It reduces the size of data more than lossless compression, but it may introduce some distortion or error in the reconstructed data.
- Coding a sequence is a technique of lossless compression that assigns codes to the symbols or characters of a data sequence based on their frequency or probability of occurrence.
- Coding a sequence can be done by using various methods, such as fixed-length coding, variable-length coding, Huffman coding, arithmetic coding, and run-length encoding.
- Fixed-length coding is a method of coding a sequence that assigns codes of equal length to all the symbols or characters of a data sequence.
- Variable-length coding is a method of coding a sequence that assigns codes of different lengths to the symbols or characters of a data sequence based on their frequency or probability of occurrence. The more frequent or probable symbols or characters have shorter codes, and the less frequent or probable symbols or characters have longer codes.
- Huffman coding is a type of variable-length coding that constructs an optimal binary tree that minimizes the average code length of a data sequence. It assigns codes to the symbols or characters of a data sequence by traversing the binary tree from the root to the leaves.
- Arithmetic coding is a type of variable-length coding that assigns codes to the symbols or characters of a data sequence by dividing a unit interval into subintervals based on their frequency or probability of occurrence. It assigns codes to the symbols or characters of a data sequence by narrowing down the subinterval that contains the data sequence.
- Run-length encoding is a type of variable-length coding that assigns codes to the runs or consecutive repetitions of the same symbol or character in a data sequence. It assigns codes to the runs by using a pair of values that indicate the symbol or character and the number of repetitions.



### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that works by replacing phrases in the input string with indexes into some dictionary.
- The dictionary contains a predetermined fixed set of entries that are known to both the compressor and the decompressor.
- Static dictionary compression is suitable for compressing short texts or texts that have a similar structure or vocabulary.
- Static dictionary compression is faster than adaptive or semi-static dictionary compression, but it requires considerable prior knowledge about the source.
- Static dictionary compression can be implemented by using a priming text, a hashing function, a trie, or a digram coding algorithm .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of diagram coding for the notes of the unit 3 - coding a sequence in the subject of data compression.

### Diagram Coding

- Diagram coding is a method of data compression that encodes pairs of symbols instead of single symbols.
- The idea is to exploit the correlation between adjacent symbols in a sequence, and assign shorter codes to more frequent pairs.
- A diagram coder consists of two components: a codebook and a coder.
- A codebook is a table that maps each pair of symbols to a unique binary code. The codebook can be fixed or adaptive, depending on whether it is predefined or updated during the encoding process.
- A coder is a device that reads the input sequence symbol by symbol, and outputs the corresponding code for each pair of symbols. If the input sequence is odd-length, a special symbol can be appended to make it even-length.
- An example of a fixed codebook for the alphabet {a, b, c, d, e} is shown below:

| Pair | Code |
|------|------|
| aa   | 00   |
| ab   | 01   |
| ac   | 100  |
| ad   | 101  |
| ae   | 1100 |
| ba   | 1101 |
| bb   | 1110 |
| bc   | 1111 |
| bd   | 0100 |
| be   | 0101 |
| ca   | 0110 |
| cb   | 0111 |
| cc   | 0010 |
| cd   | 0011 |
| ce   | 0000 |
| da   | 0001 |
| db   | 1010 |
| dc   | 1011 |
| dd   | 1000 |
| de   | 1001 |
| ea   | 01100|
| eb   | 01101|
| ec   | 01110|
| ed   | 01111|
| ee   | 01000|

- An example of a diagram coder using the above codebook is shown below:

| Input sequence | Output code |
|----------------|-------------|
| abcd           | 0110110011  |
| eedcba         | 0100000110111101101 |
| aabbaa         | 000011100000 |



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes.
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios than static dictionary methods.
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, LZW, etc.
- LZ77 and LZ78 are based on the idea of replacing repeated sequences of symbols with references to their previous occurrences in the data stream.
- LZW is based on the idea of building a dictionary of prefixes and suffixes of symbols and encoding them with variable-length codes.
- Adaptive dictionary algorithms have the following advantages:
  - They do not require prior knowledge of the data source or statistics.
  - They can handle any type of data, such as text, audio, video, etc.
  - They can adjust to the changes in the data distribution over time.
  - They can achieve high compression ratios for data with high redundancy or regularity.
- Adaptive dictionary algorithms have the following disadvantages:
  - They require more memory and processing power than static dictionary methods.
  - They may suffer from dictionary overflow or degradation if the dictionary size is limited or not managed properly.
  - They may introduce errors or inefficiencies if the compression and decompression dictionaries are not synchronized or updated consistently.



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
- There are many variations and improvements of LZ77, such as LZSS, LZMA, DEFLATE, and others.



### The LZ78 Approach

- LZ78 is a lossless data compression algorithm that was proposed by Abraham Lempel and Jacob Ziv in 1978 .
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- The dictionary is initialized with all possible single characters as the first entries, and then new entries are added as new sequences are encountered in the input.
- The output of LZ78 consists of pairs of numbers, where the first number is the index of the dictionary entry that matches the longest prefix of the current input, and the second number is the next character after the prefix.
- The output pairs are encoded using a variable-length code, such as Huffman coding, to reduce the size of the output.
- LZ78 has the advantage of being adaptive, meaning that it does not require any prior knowledge of the input data, and it can adjust to changes in the data characteristics.
- LZ78 also has the advantage of being easy to implement and having a fast decoding process, since the dictionary can be reconstructed from the output.
- However, LZ78 has some disadvantages, such as having a large memory requirement for the dictionary, which can grow indefinitely, and having a slow encoding process, since the dictionary has to be searched for every input character.
- LZ78 is the basis for many variations and extensions, such as LZW, LZSS, LZMA, and others, which aim to improve the compression performance and overcome the limitations of LZ78 .



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can be either lossless or lossy, depending on whether the original information can be perfectly recovered or not.
- Coding a sequence is a technique for lossless data compression that assigns codes to sequences of symbols or bytes based on their frequency or occurrence in the data.
- Coding a sequence can reduce the redundancy and improve the efficiency of data transmission and storage.
- Some examples of coding a sequence are:

  - Huffman coding: a variable-length code that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols.
  - Lempel-Ziv-Welch (LZW) coding: a dictionary-based code that builds a table of codes for sequences of symbols or bytes that appear in the data, and outputs the codes instead of the sequences .
  - Sequence statistical code: a code that uses statistical information about the data to generate codes for sequences of symbols or bytes that have similar probabilities.

- Coding a sequence can be applied to various types of data, such as text, images, audio, video, etc. Some applications are:

  - Compression of text files, such as documents, web pages, emails, etc.
  - Compression of image files, such as GIF, PNG, BMP, etc.
  - Compression of audio files, such as WAV, MP3, etc.
  - Compression of video files, such as AVI, MP4, etc.
  - Compression of data streams, such as sensor data, network packets, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of file compression-UNIX compress for the notes of the unit 3 - coding a sequence in the subject of data compression.

### File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save storage space, bandwidth, and transmission time.
- UNIX compress is a file compression utility that uses the Lempel-Ziv-Welch (LZW) algorithm to compress files.
- The LZW algorithm is a dictionary-based algorithm that replaces repeated sequences of bytes with shorter codes from a predefined table.
- The LZW algorithm works as follows:
  - Initialize the dictionary with 256 entries, each corresponding to a single byte value.
  - Read the first byte from the input and output its code.
  - While there is more input, do the following:
    - Read the next byte and append it to the previous byte to form a string.
    - If the string is in the dictionary, output its code and continue.
    - If the string is not in the dictionary, add it to the dictionary with a new code and output the code of the previous byte.
    - Set the previous byte to the current byte and repeat.
  - Output the code of the last byte.
- The compressed file has a .Z extension and can be decompressed with the uncompress utility.
- UNIX compress can achieve a compression ratio of about 2:1 on average, depending on the input data.



### Image Compression

Image compression is the process of reducing the size of an image file without compromising its quality or visual appearance. Image compression is useful for saving storage space, bandwidth, and transmission time, as well as for enhancing the performance of applications that use images.

Image compression techniques can be classified into two categories: lossless and lossy.

- Lossless compression techniques preserve the exact information of the original image, and allow the original image to be reconstructed from the compressed data without any loss of quality. Lossless compression techniques are suitable for images that require high fidelity, such as medical images, text documents, or icons.

- Lossy compression techniques discard some information of the original image, and allow the compressed data to be reconstructed into an approximation of the original image with some loss of quality. Lossy compression techniques are suitable for images that can tolerate some degradation, such as natural images, photographs, or web graphics.

Some of the common methods of image compression are:

- Deflate: The Deflate method is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. The LZ77 algorithm identifies and eliminates repeated sequences of pixels, while the Huffman coding assigns variable-length codes to the remaining pixels based on their frequency of occurrence. The Deflate method is used in formats such as PNG, GIF, and ZIP.

- Run-length encoding (RLE): Run-length encoding is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. For example, a sequence of 10 white pixels can be encoded as (10, white) instead of writing white 10 times. RLE is effective for images that have large areas of uniform color, such as cartoons or logos .

- Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to the pixels based on their probability of occurrence. Unlike Huffman coding, which assigns codes to individual pixels, arithmetic coding assigns codes to entire sequences of pixels, resulting in higher compression ratios. Arithmetic coding is used in formats such as JPEG 2000 and JPEG XR.

- Transform coding: Transform coding is a lossy image compression technique that uses mathematical transformations to reduce the size of an image and commonly used for JPEGs. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. One of the most widely used forms of transform coding is the discrete cosine transform (DCT), which converts the image data into a sum of cosine functions of different frequencies. The DCT coefficients that correspond to high frequencies are usually discarded or quantized, as they are less perceptible to the human eye. The remaining coefficients are then encoded using Huffman coding or arithmetic coding  .

- Other methods: There are many other methods of image compression, such as wavelet coding, fractal coding, vector quantization, and neural network coding, that use different techniques to exploit the properties of images and achieve high compression ratios. However, these methods are beyond the scope of this note.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Graphics Interchange Format (GIF) for the unit 3 of Data Compression.

### The Graphics Interchange Format (GIF)

- GIF is a graphical image format that was introduced by CompuServe in 1987 .
- GIF uses a variant of Lempel–Ziv–Welch (LZW) lossless data compression technique to reduce the file size without degrading the visual quality  .
- GIF supports up to 256 colors per image and allows for transparency and animation .
- GIF is suitable for images with solid areas of color, such as logos, icons, cartoons, and text .
- GIF is not suitable for images with gradients, complex details, or photographic quality, as they may result in large file sizes or poor color reproduction .
- GIF was challenged by the Portable Network Graphics (PNG) format, which was created in 1995 as a response to the patent issue of LZW algorithm used in GIF. PNG offers better compression, more colors, and alpha channel support.
- GIF is still widely used on the web for its simplicity, compatibility, and animation features .



### Compression over Modems

- Compression over modems is a technique that allows modems to transmit data faster and more efficiently over phone lines by reducing the size of the data before sending it and expanding it after receiving it.
- Compression over modems can be done by using different algorithms and protocols, such as V.42bis, MNP5, V.44, etc. These protocols can achieve different compression ratios depending on the type and redundancy of the data .
- Compression over modems can improve the throughput and reliability of data transmission, especially in noisy or low-quality phone lines, by reducing the number of bits that need to be sent and correcting any errors that may occur.
- Compression over modems can also reduce the cost of data transmission by using less bandwidth and phone time. However, compression over modems may also introduce some overhead and latency, and may not be effective for data that is already compressed or encrypted .
- Compression over modems can be implemented by using hardware or software solutions, such as compression service adapters (CSA), advanced integration modules (AIM), or communication software. These solutions can vary in performance, compatibility, and scalability .



### V.42 bits

- V.42 bits are the bits used by the V.42bis standard for data compression in modems   .
- V.42bis is an adaptive data compression standard that can achieve up to 4:1 compression ratio for text and binary data   .
- V.42bis is based on the Lempel-Ziv dynamic dictionary approach, which encodes repeated sequences of data with shorter codes   .
- V.42bis uses a 512-entry dictionary for each direction of transmission, which can be expanded to 2048 entries if both sides agree   .
- V.42bis can switch to transparent mode, in which data is transmitted uncompressed, if the compression ratio falls below a certain threshold or if the data contains escape sequences   .
- V.42bis can also recycle the dictionary entries periodically or when the dictionary is full, to adapt to changing data patterns   .
- V.42bis was developed by British Telecom and adopted by the CCITT (now ITU-T) in 1990 as an extension to the V.42 error correction standard   .
- V.42bis is widely used by modem manufacturers and network operators, and is compatible with other standards such as V.32, V.32bis, V.34, and V.90   .



### Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, and then encodes the difference between the actual and the predicted symbol or bit. The difference, also called the residual or the error, is usually smaller than the original symbol or bit, and can be compressed more efficiently. Predictive coding can be applied to different types of data, such as audio, image, or text.

Some of the main concepts and techniques involved in predictive coding are:

- **Predictor**: A function or an algorithm that estimates the next symbol or bit in a sequence based on the previous symbols or bits. The predictor can be static or adaptive, meaning that it can be fixed or updated based on the input data. The predictor can also be linear or nonlinear, meaning that it can use a simple or a complex function to make the prediction. Examples of predictors are linear predictive coding (LPC) for audio signals, and intra-frame coding for image signals.
- **Residual**: The difference between the actual and the predicted symbol or bit. The residual can be positive or negative, and can be represented by a fixed or a variable number of bits. The residual can be further compressed by using an entropy encoder, such as Huffman coding or arithmetic coding. Examples of entropy encoders are dynamic Markov compression (DMC) for binary data , and prediction by partial matching (PPM) for text data.
- **Decoder**: A function or an algorithm that reconstructs the original sequence from the compressed residual and the predictor. The decoder must use the same predictor and the same entropy decoder as the encoder, and must be able to update the predictor if it is adaptive. The decoder can also perform error correction or detection if the compressed data is corrupted or noisy.

Some of the advantages and disadvantages of predictive coding are:

- **Advantages**: Predictive coding can achieve high compression ratios for data that has strong correlations or patterns, such as speech or natural images. Predictive coding can also adapt to the characteristics of the data and exploit the local or temporal dependencies. Predictive coding can also be combined with other compression techniques, such as transform coding or dictionary coding, to improve the performance.
- **Disadvantages**: Predictive coding can be computationally complex and require a lot of memory, especially for adaptive or nonlinear predictors. Predictive coding can also be sensitive to errors or noise in the data, which can propagate and affect the decoding quality. Predictive coding can also be difficult to design or optimize for different types of data or applications.



### Prediction with Partial Match (PPM) for Data Compression

- Prediction by Partial Match (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length context for each symbol, and using the longest context that matches the current input to assign probabilities to the next symbol.
- PPM uses a hierarchy of models, each corresponding to a different context length, and switches between them dynamically depending on the input data.
- PPM can achieve high compression ratios, especially for natural language texts, but it is also computationally intensive and requires large amounts of memory.
- PPM can be implemented using various data structures, such as linked lists, tries, or suffix trees.
- PPM can be improved by using escape symbols, exclusion mechanisms, interpolation methods, or adaptive order selection.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Coding a sequence is a technique of data compression that assigns codes to sequences of bytes or symbols that occur frequently in the data .
- The basic algorithm for coding a sequence is as follows :

  - Initialize a code table with the codes for the individual bytes or symbols in the data.
  - Scan the data from left to right and gather input bytes or symbols into a sequence until the next byte or symbol would make a sequence with no code yet in the code table.
  - Output the code for the sequence (without the next byte or symbol) and add a new code for the sequence with the next byte or symbol to the code table.
  - Repeat the above steps until the end of the data is reached.

- An example of coding a sequence is the LZW (Lempel–Ziv–Welch) compression technique, which uses codes 256 through 4095 to represent sequences of bytes.
- Coding a sequence can achieve better compression ratio than coding individual bytes or symbols, especially for data with repeated patterns  .
- Coding a sequence is a lossless compression technique, meaning that the original data can be perfectly reconstructed from the compressed data.
- Coding a sequence can be applied to any type of data, such as text, images, videos, etc .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of the escape symbol for the notes of Unit 3 - Coding a sequence in the subject of Data Compression.

```markdown
### The ESCAPE SYMBOL

- An escape symbol is a special symbol that is used to indicate that the next symbol in a sequence is not encoded using the current codebook, but using a different one.
- The escape symbol is useful when the codebook is not complete, meaning that it does not contain all the possible symbols that can occur in the sequence.
- For example, suppose we have a codebook that contains only the symbols A, B, and C, and their corresponding codes 0, 10, and 11. If we want to encode the sequence ABCD, we cannot use the codebook directly, because it does not have a code for D. However, we can use an escape symbol, say E, and its code 01, to indicate that the next symbol is encoded using a different codebook, say the ASCII code. Then, the encoded sequence would be 0 10 11 01 01000100, where 01000100 is the ASCII code for D.
- The escape symbol can also be used to switch between different codebooks during the encoding process, depending on the context or the statistics of the sequence. For example, suppose we have two codebooks, one for uppercase letters and one for lowercase letters, and we want to encode the sequence Hello. We can use an escape symbol, say E, and its code 000, to indicate that the next symbol is encoded using the lowercase codebook. Then, the encoded sequence would be 1000 000 1100 1100 1101 1101, where 1000 is the code for H in the uppercase codebook, and 1100, 1101 are the codes for e, l, o in the lowercase codebook.
- The escape symbol can improve the compression ratio of the encoding, because it allows the use of shorter codes for more frequent symbols, and longer codes for less frequent symbols, by switching between different codebooks. However, the escape symbol also introduces some overhead, because it needs to be encoded and transmitted along with the sequence. Therefore, the optimal choice of the escape symbol and the codebooks depends on the characteristics of the sequence and the compression objective.
```



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of coding a sequence.

### Coding a sequence
- A sequence is a finite or infinite ordered list of symbols or elements from a given alphabet.
- A code is a mapping from the symbols of the alphabet to a set of binary strings, such that no binary string is a prefix of another.
- A code is called uniquely decodable if there is only one way to decode any encoded sequence.
- A code is called instantaneous if it is uniquely decodable and every symbol can be decoded as soon as it is received, without waiting for the next symbol.
- A code is called optimal if it minimizes the expected length of the encoded sequence for a given probability distribution of the symbols.
- A code is called prefix-free if no binary string is a prefix of another. Prefix-free codes are always instantaneous and uniquely decodable.
- A code is called fixed-length if all the binary strings have the same length. Fixed-length codes are easy to encode and decode, but they are not optimal unless the symbols have equal probabilities.
- A code is called variable-length if the binary strings have different lengths. Variable-length codes can achieve optimality, but they require more complex encoding and decoding algorithms.
- A code is called Huffman if it is a variable-length, prefix-free, optimal code that is constructed using a bottom-up approach based on the probabilities of the symbols.
- A code is called arithmetic if it is a variable-length, optimal code that is constructed using a top-down approach based on the cumulative probabilities of the symbols. Arithmetic coding can achieve higher compression than Huffman coding, but it is more computationally intensive and sensitive to errors.



### The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The exclusion principle is a technique used in some data compression algorithms, such as PPM, to improve the accuracy of the probability estimation for each symbol in the input sequence.
- The exclusion principle works by excluding the symbols that have already been seen in a higher-order context from the probability computation of a lower-order context, thus avoiding double-counting and increasing the chances of predicting the next symbol correctly.
- For example, suppose we have a sequence of letters A, B, C, D, and E, and we want to compress it using a PPM model with a maximum context order of 2. The PPM model will use a set of previous symbols (up to 2) to predict the next symbol in the sequence.
- The first symbol A has no previous context, so the PPM model will use a zero-order model, which assigns equal probabilities to all symbols in the alphabet. The probability of A is 1/5, and the subinterval for A is [0, 0.2).
- The second symbol B has a previous context of A, so the PPM model will use a first-order model, which assigns probabilities based on the frequencies of symbols following A in the sequence. The probability of B given A is 1/1, and the subinterval for B is [0, 0.2) * [0, 1) = [0, 0.2).
- The third symbol C has a previous context of AB, so the PPM model will use a second-order model, which assigns probabilities based on the frequencies of symbols following AB in the sequence. However, since AB has not been seen before, the PPM model will use an escape code to indicate that the next symbol is not in the current context, and then switch to a lower-order model. The escape code has a probability of 1/1, and the subinterval for the escape code is [0, 0.2) * [0, 1) = [0, 0.2).
- The PPM model will then use a first-order model based on the previous context of B, which assigns probabilities based on the frequencies of symbols following B in the sequence. However, since B has already been seen in the higher-order context of AB, the PPM model will exclude B from the probability computation, and assign equal probabilities to the remaining symbols in the alphabet. The probability of C given B (excluding B) is 1/4, and the subinterval for C is [0, 0.2) * [0, 0.25) = [0, 0.05).
- The fourth symbol D has a previous context of BC, so the PPM model will use a second-order model, which assigns probabilities based on the frequencies of symbols following BC in the sequence. However, since BC has not been seen before, the PPM model will use an escape code to indicate that the next symbol is not in the current context, and then switch to a lower-order model. The escape code has a probability of 1/1, and the subinterval for the escape code is [0, 0.05) * [0, 1) = [0, 0.05).
- The PPM model will then use a first-order model based on the previous context of C, which assigns probabilities based on the frequencies of symbols following C in the sequence. However, since C has already been seen in the higher-order context of BC, the PPM model will exclude C from the probability computation, and assign equal probabilities to the remaining symbols in the alphabet. The probability of D given C (excluding C) is 1/4, and the subinterval for D is [0, 0.05) * [0.25, 0.5) = [0.0125, 0.025).
- The fifth symbol E has a previous context of CD, so the PPM model will use a second-order model, which assigns probabilities based on the frequencies of symbols following CD in the sequence. However, since CD has not been seen before, the PPM model will use an escape code to indicate that the next symbol is not in the current context, and then switch to a lower-order model. The escape code has a probability of 1/1, and the subinterval for the escape code is [0.0125, 0.025) * [0, 1) = [0.0125,



### The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm that rearranges a string of characters into runs of similar characters. This is useful for data compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding. The BWT is also reversible, meaning that the original string can be recovered from the transformed string.

The BWT works as follows:

- Given a string T, append a special symbol $ to the end of T. The symbol $ should be lexicographically smaller than any other character in T.
- Construct a matrix M that contains all possible cyclic rotations of T$. Sort the rows of M lexicographically.
- The BWT of T is the last column of M.

For example, given the string T = banana, the BWT is annb$aa, as shown below:

| | | | | | | |
|-|-|-|-|-|-|-|
|b|a|n|a|n|a|$|
|a|$|b|a|n|a|n|
|n|a|$|b|a|n|a|
|a|n|a|$|b|a|n|
|n|a|n|a|$|b|a|
|a|n|a|n|a|$|b|
|$|b|a|n|a|n|a|

To reverse the BWT, we can use the following algorithm:

- Given a string BWT(T), construct an array F that contains the first column of the sorted matrix M. This can be done by sorting the characters of BWT(T) lexicographically.
- Construct an array L that contains the last column of M, which is BWT(T).
- Construct an array C that counts the number of occurrences of each character in F up to a given position. For example, C[a][3] is the number of a's in F[0..3].
- Construct an array P that maps each character in L to its corresponding position in F. This can be done by using C to keep track of the next available position for each character. For example, P[0] is the position of L[0] in F, and C[L[0]] is incremented by one.
- Starting from P[0], follow the pointers in P until reaching the position of the $ symbol. The original string T can be obtained by concatenating the characters in L along the way, excluding the $ symbol.

For example, given the string BWT(T) = annb$aa, the reversal algorithm works as follows:

| | | | | | | |
|-|-|-|-|-|-|-|
|F|L|C[a]|C[b]|C[n]|C[$]|P|
|a|a|1|0|0|0|5|
|a|a|2|0|0|0|6|
|a|n|3|0|1|0|2|
|b|n|3|1|2|0|3|
|n|b|3|1|3|0|1|
|n|$|3|1|4|1|0|
|$|a|3|1|4|2|4|

The original string T can be recovered by following the pointers in P:

P[0] -> P[5] -> P[6] -> P[2] -> P[3] -> P[1] -> P[4]

L[0] -> L[5] -> L[6] -> L[2] -> L[3] -> L[1] -> L[4]

a -> a -> n -> a -> n -> a -> b

T = banana

Some properties of the BWT are:

- The BWT preserves the number and frequency of each character in the original string.
- The BWT is a permutation of the original string, meaning that no information is lost or added.
- The BWT tends to group similar characters together, creating long runs of repeated characters. This makes the BWT suitable for compression techniques that exploit redundancy.
- The BWT can also be used for efficient string matching and indexing, by using a data structure called the FM-index. The FM-index combines the BWT with additional information to allow fast queries on the original string without decompressing it.



### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but rearranges the data to make it more suitable for entropy encoding techniques of compression  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is initially sorted in some order (such as ASCII or lexicographic) and update it dynamically as the data is processed.
- For each symbol in the input data, the algorithm outputs the index of that symbol in the list and then moves that symbol to the front of the list, pushing the other symbols back. This way, the symbols that appear more frequently in the data will tend to have smaller indices and thus occupy fewer bits when encoded  .
- Movetofront coding is an invertible transformation, meaning that the original data can be recovered from the transformed data and the list of symbols. The decoding algorithm simply reverses the encoding process: it maintains the same list of symbols and for each index in the input data, it outputs the symbol at that index in the list and then moves that symbol to the front of the list  .
- Movetofront coding is often used as a preprocessing step before applying other compression algorithms, such as Huffman coding or arithmetic coding, to improve their performance. It is especially effective for data that has long runs of identical or similar symbols, such as natural language text or genomic sequences .
- Movetofront coding can be implemented efficiently using arrays or linked lists to store the list of symbols. The time complexity of encoding and decoding is linear in the size of the input data and the size of the alphabet . The space complexity is linear in the size of the alphabet .



### CALIC

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a technique for compressing continuous-tone images without any loss of quality or information  .
- It achieves high compression ratios by using a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics  .
- The non-linear predictor adapts via an error feedback mechanism, which reduces the prediction error and the entropy of the residual signal  .
- The residual signal is then encoded using a binary arithmetic coder with adaptive probability estimation  .
- CALIC has relatively low time and space complexities, and can handle various types of images, such as grayscale, color, and compound images    .
- CALIC can also be extended to compress video data by using motion compensation to exploit the temporal redundancy between frames .
- CALIC is one of the most efficient lossless image coding techniques in the literature, and has been adopted as a standard by the International Organization for Standardization (ISO) and the International Telecommunication Union (ITU)  .



### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- It is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- It consists of two independent and distinct stages: modeling and encoding  .
- The modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error  .
- The encoding stage maps the prediction error to a symbol and encodes it using a Golomb-Rice code  .
- The standard defines four types of contexts: run, regular, edge, and corner  .
- The standard also defines two types of coding modes: near-lossless and lossless  .
- The near-lossless mode allows a small amount of error (specified by a parameter) in the reconstructed image, which can improve the compression ratio  .
- The lossless mode guarantees an exact reconstruction of the original image, which can preserve the image quality  .
- JPEG-LS is suitable for applications that require high fidelity, low complexity, and fast compression and decompression of continuous-tone images  .



### Multi-resolution Approaches

- Multi-resolution approaches are techniques that allow data to be represented and processed at different levels of detail or resolution, depending on the needs and capabilities of the application or the user.
- Multi-resolution approaches can be useful for data compression, which is the process of reducing the amount of data needed to store or transmit information, while preserving its quality or usefulness.
- Data compression can be achieved by exploiting the redundancy or correlation in the data, such as spatial, temporal, or statistical redundancy, and by removing or quantizing the irrelevant or less important information, such as noise or high-frequency details.
- Multi-resolution approaches can enhance data compression by allowing the data to be decomposed into different components or layers, each representing a different level of detail or resolution, and by applying different compression methods or parameters to each component or layer, depending on their importance or relevance.
- Some examples of multi-resolution approaches for data compression are:

  - **Wavelet-based compression**: Wavelets are mathematical functions that can decompose a signal or an image into a set of coefficients, each corresponding to a different scale or frequency band. Wavelet-based compression can achieve high compression ratios by discarding or quantizing the coefficients that have small magnitudes or that are less perceptible by the human eye or ear. Wavelet-based compression can also adapt to the local features or characteristics of the data, such as edges or textures, by using different wavelet functions or parameters for different regions or blocks of the data. Wavelet-based compression is widely used for image, audio, and video compression, such as JPEG 2000, MP3, and MPEG-4 .
  - **Fractal-based compression**: Fractals are geometric shapes or patterns that have self-similarity, meaning that they look similar at different scales or magnifications. Fractal-based compression can exploit the self-similarity in the data by finding and encoding the affine transformations that map parts of the data to other parts of the data at different scales or locations. Fractal-based compression can achieve high compression ratios and resolution-independent reconstruction, meaning that the data can be reconstructed at any desired resolution from the compressed representation. Fractal-based compression is mainly used for image compression, such as FIF and IFS.
  - **Multi-resolution vector data compression**: Vector data are data that represent geometric features or objects, such as points, lines, polygons, or curves, using coordinates and attributes. Multi-resolution vector data compression can reduce the size of vector data by simplifying or generalizing the geometry or the topology of the features or objects, depending on the level of detail or resolution required. Multi-resolution vector data compression can also improve the compression efficiency by using grid filtering and binary offset for linear and point geometries, and by taking visual lossless distance on screen display as accuracy requirement. Multi-resolution vector data compression is mainly used for geographic information systems (GIS) or cartography, such as SVG and GML.



### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding reduces the amount of data needed to represent a binary image, such as a scanned document or a fax page, by exploiting the spatial redundancy and the bi-level nature of the image .
- Facsimile encoding is based on the idea of run-length coding, which is a simple method of compressing a sequence of identical symbols by replacing them with a single symbol and a count of its repetitions .
- For example, the sequence 0000001111100000 can be compressed as 6,0,5,1,4,0 using run-length coding, where the first number is the length of the run and the second number is the symbol in the run.
- Facsimile encoding uses two types of run-length codes: white codes and black codes, which correspond to the runs of white and black pixels in the image, respectively .
- Facsimile encoding also uses a special code called EOL (end of line) to mark the end of each scan line in the image .
- Facsimile encoding assigns variable-length codes to the run-length codes, using a technique called Huffman coding, which is a method of assigning shorter codes to more frequent symbols and longer codes to less frequent symbols .
- For example, the white code 64, which represents a run of 64 white pixels, is assigned the code 11011, while the white code 1792, which represents a run of 1792 white pixels, is assigned the code 0000000110010010111.
- Facsimile encoding uses a standard set of Huffman codes, defined by the CCITT (now ITU-T) Group 3 and Group 4 recommendations, which are widely adopted by many facsimile and document imaging file formats .
- Facsimile encoding can achieve high compression ratios, especially for images that contain large areas of white or black pixels, such as text documents or drawings .
- Facsimile encoding can also be adapted to different transmission rates and channel conditions, by using different modes of operation, such as one-dimensional, two-dimensional, or mixed modes .
- Facsimile encoding can be decompressed quickly and easily, by using a table lookup or a tree traversal method to decode the Huffman codes and reconstruct the run-length codes and the image pixels .



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits  .
- The model consists of a binary tree of nodes, each representing a context of previous bits and storing the probabilities of the next bit being 0 or 1  .
- The model is initialized with a single node, the root, which has equal probabilities for both 0 and 1  .
- As the input is read, the model is updated by creating new nodes or adjusting the probabilities of existing nodes  .
- The model adapts to the changing characteristics of the input data, and can handle any type of data, including text, images, audio, etc.  .
- The arithmetic coder encodes each bit of the input based on the probabilities given by the model, and produces a compressed output that is close to the entropy of the input   .
- DMC is a simple and elegant algorithm that achieves high compression ratios, but it is also slow and memory-intensive, as it requires a large tree to store the model   .
- DMC can be improved by using techniques such as pruning, merging, splitting, or smoothing the nodes of the tree, or by using higher-order contexts or multiple models   .



## Unit 4 - Distortion criteria

- Distortion is the alteration of the original shape or other characteristic of a signal.
- Distortion can degrade the quality and intelligibility of a signal in communication systems.
- Distortion can be caused by various factors, such as non-linear behavior of electronic components, power supply limitations, noise, interference, channel dispersion, etc  .
- Distortion can be classified into different types, such as amplitude distortion, frequency distortion, phase distortion, harmonic distortion, intermodulation distortion, clipping distortion, etc.
- Distortion can be measured by different criteria, such as signal-to-noise ratio (SNR), total harmonic distortion (THD), intermodulation distortion (IMD), error vector magnitude (EVM), etc .
- Distortion can be reduced or compensated by various techniques, such as filtering, equalization, feedback, predistortion, etc  .
- Distortion criteria are important for designing and evaluating communication systems, as they affect the performance, reliability, and efficiency of the systems  .



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not.
- Lossy compression introduces some distortion or error in the reconstructed data, which may be acceptable for some applications such as audio or image compression.
- Distortion criteria are the measures of how close the reconstructed data is to the original data, using some mathematical quantity.
- Distortion criteria can be based on different aspects of the data, such as the numerical difference, the perceptual quality, the statistical properties, or the functional performance.
- Some common distortion criteria are:

  - Mean squared error (MSE): the average of the squared differences between the original and the reconstructed data values.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible value of the data to the root mean squared error, expressed in decibels.
  - Structural similarity index (SSIM): a measure of the similarity of the structural information between the original and the reconstructed data, based on luminance, contrast, and correlation.
  - Bit error rate (BER): the ratio of the number of bits that are different between the original and the reconstructed data to the total number of bits.
  - Mean opinion score (MOS): a subjective rating of the quality of the reconstructed data, usually on a scale from 1 (bad) to 5 (excellent).

- The choice of the distortion criteria depends on the application and the user preference. Different distortion criteria may lead to different optimal compression methods and rates.
- Rate-distortion theory is the branch of information theory that studies the trade-off between the compression rate and the distortion level. It defines the rate-distortion function as the minimum possible compression rate for a given distortion level, or the minimum possible distortion for a given compression rate.
- The rate-distortion function can be calculated using an iterative algorithm, such as the Blahut-Arimoto algorithm, or approximated using some models, such as the Gaussian model or the Laplacian model.
- The rate-distortion function provides a theoretical lower bound for the performance of any compression system. The closer a practical compression system is to the rate-distortion function, the better it performs.



Hello, I am Sydney, your AI assistant. I can help you with your topic of scalar quantization for data compression. Here are some notes that you can use for your study:

### Scalar Quantization
- Scalar quantization is a process of converting a continuous or discrete signal into a finite number of discrete levels, called quantization levels or reconstruction levels .
- Scalar quantization can be seen as a mapping function Q(x) that assigns a quantization level Q(x) to each input value x.
- Scalar quantization can be lossy or lossless, depending on whether the quantization levels can exactly represent the original signal or not.
- Scalar quantization can be uniform or nonuniform, depending on whether the quantization levels are equally spaced or not.
- Scalar quantization can be optimal or suboptimal, depending on whether the quantization levels minimize a certain distortion criterion or not.
- Scalar quantization can be applied to one-dimensional signals, such as audio or speech, or to multidimensional signals, such as images or video, by quantizing each component or dimension separately.
- Scalar quantization can be improved by using vector quantization, which quantizes a group of signal samples together, taking into account their correlation or dependence .

Some examples of scalar quantization are:

- Pulse code modulation (PCM), which is a uniform and lossy scalar quantizer that is widely used for digital audio and telephony.
- Wavelet/scalar quantization (WSQ), which is a nonuniform and lossy scalar quantizer that is used for compressing fingerprint images at high compression ratios.
- Huffman coding, which is a nonuniform and lossless scalar quantizer that is used for compressing text or symbols based on their frequency of occurrence.



### The Quantization Problem

Quantization is a process of mapping a large set of input values to a smaller set of output values, such that the distortion or error introduced by this mapping is minimized. Quantization is a key technique for lossy data compression, as it reduces the number of bits needed to represent the data.

The quantization problem can be stated as follows: given a source distribution p(x) and a distortion measure d(x,y), find a quantizer Q(x) that minimizes the expected distortion

D = E[d(x,Q(x))]

subject to some constraint on the rate or complexity of the quantizer.

There are different types of quantizers, such as uniform, non-uniform, scalar, vector, and entropy-constrained quantizers. Each type has its own advantages and disadvantages, depending on the characteristics of the source and the distortion measure.

Some of the main challenges and trade-offs in quantization are:

- How to design the quantizer levels and regions to match the source distribution and minimize the distortion.
- How to encode the quantizer output efficiently to reduce the rate or complexity.
- How to balance the trade-off between rate and distortion, or equivalently, between complexity and performance.
- How to handle the quantization noise and its effects on the quality of the reconstructed data.
- How to adapt the quantizer to the changing source statistics or user preferences.

Quantization is a fundamental and widely used technique in data compression, and it has many applications in image, audio, video, and speech processing, as well as in communication and storage systems.



# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels .
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero. It is also called a symmetric uniform quantizer.
  - A mid-rise quantizer does not have a zero output level and the output levels are asymmetric around zero. It is also called an asymmetric uniform quantizer.
- A uniform quantizer can be used for data compression by reducing the number of bits required to represent the input values  .
  - A uniform quantizer can be combined with an entropy encoder to further compress the output levels by exploiting their statistical properties .
  - A uniform quantizer can also be incorporated into a deep learning based image compression framework, where the quantizer is applied to the feature maps between the encoder and decoder .
- A uniform quantizer has some advantages and disadvantages for data compression .
  - Advantages:
    - It is simple to implement and analyze .
    - It has a constant signal-to-quantization-noise ratio (SQNR) for any input distribution .
    - It performs well at high bit rates, where the quantization error is small compared to the input signal .
  - Disadvantages:
    - It is not optimal for non-uniform input distributions, where some input values are more likely than others .
    - It suffers from granular noise at low bit rates, where the quantization error is large compared to the input signal .
    - It introduces distortion that is independent of the input signal, which may be perceptually annoying for some applications .



### Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input data.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters, such as synthetic aperture radar (SAR) raw data.
- An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution, minimizing the distortion or the bit rate.
- There are two main types of adaptive quantization: forward adaptive quantization and backward adaptive quantization.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block and transmitted to the receiver as side information. The receiver uses the same parameters to reconstruct the signal.
- In backward adaptive quantization, the quantizer parameters are updated based on the previous quantized samples. The receiver uses the same update rules to track the quantizer parameters. No side information is needed, but the quantizer may be slow to adapt to sudden changes in the input.
- Adaptive quantization can be applied to different types of quantizers, such as uniform, nonuniform, scalar, or vector quantizers.
- Adaptive quantization can improve the performance of data compression schemes, such as differential pulse-code modulation (DPCM) or transform coding, by reducing the quantization error or the bit rate.



# Non uniform Quantization

Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals between the output values. Non uniform quantization is more suitable for sources with non-uniform distributions of values, such as speech or image signals.

Some points to note about non uniform quantization are:

- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the source values are more likely to occur.
- Non uniform quantization can be implemented by using a non-linear function to map the input values to a uniform quantizer, and then applying the inverse function at the decoder. This is called companding.
- Non uniform quantization can also be optimized by adjusting the quantization points according to the network gradients, such as in neural network compression.
- Non uniform quantization can be classified into two types: scalar and vector. Scalar non uniform quantization operates on each input value independently, while vector non uniform quantization operates on a group of input values jointly.
- Non uniform quantization can be evaluated by using distortion criteria, such as mean squared error (MSE), signal to noise ratio (SNR), or perceptual quality measures.



```
## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of output levels, called quantization levels or code words.
- Vector quantization is a process of mapping a vector of continuous-valued components, such as a block of pixels or a segment of speech, to a discrete set of output vectors, called code vectors or code books.
- Vector quantization has some advantages over scalar quantization, such as:

  - Higher compression ratio: Vector quantization can achieve higher compression ratio than scalar quantization by exploiting the correlation among the components of the input vector. For example, in image compression, vector quantization can reduce the number of bits needed to represent a block of pixels by using a code book that captures the common patterns or features of the image.
  - Lower distortion: Vector quantization can achieve lower distortion than scalar quantization by minimizing the mean squared error between the input vector and the output code vector. For example, in speech compression, vector quantization can preserve the perceptual quality of the speech signal by using a code book that matches the characteristics of the human auditory system.
  - Higher robustness: Vector quantization can achieve higher robustness than scalar quantization by reducing the sensitivity to noise or channel errors. For example, in wireless communication, vector quantization can improve the performance of the system by using a code book that is designed to cope with the channel conditions or the interference.
```



### The Linde-Buzo-Gray Algorithm for the notes of the Unit 5 - Advantages of Vector Quantization over Scalar Quantization in the subject of Data Compression

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook   .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in the input space.
- Vector quantization is a technique to compress data by mapping each input vector to the nearest codeword in the codebook, and transmitting the index of the codeword instead of the original vector.
- Scalar quantization is a simpler technique that compresses data by mapping each input scalar (one-dimensional value) to the nearest level in a set of discrete levels, and transmitting the index of the level instead of the original scalar.
- Vector quantization has some advantages over scalar quantization, such as:
  - It can exploit the correlation among the components of the input vector, and reduce the redundancy in the data.
  - It can achieve higher compression ratios and lower distortion for the same number of bits per symbol, compared to scalar quantization.
  - It can adapt to the statistics of the input data, and generate optimal codebooks for different sources and applications.
- The LBG algorithm is based on the k-means clustering method, and it works as follows :
  - Initialize the codebook with one codeword, which is the centroid (average) of the training set of input vectors.
  - Split each codeword in the codebook into two slightly perturbed codewords, and double the size of the codebook.
  - Assign each input vector to the nearest codeword in the codebook, and compute the average distortion (mean squared error) between the input vectors and their assigned codewords.
  - Update each codeword in the codebook by computing the centroid of the input vectors assigned to it, and reduce the distortion.
  - Repeat the assignment and update steps until the distortion converges to a minimum or a predefined threshold is reached.
  - Repeat the splitting, assignment and update steps until the desired size of the codebook is obtained.
- The LBG algorithm is the most common algorithm for codebook generation, and it can produce codebooks with minimum error from a training set.
- However, the LBG algorithm also has some drawbacks, such as:
  - It is sensitive to the initial conditions, and it may converge to a local minimum instead of a global minimum of the distortion function.
  - It is computationally expensive, and it may take a long time to converge for large codebooks and high-dimensional input vectors.
  - It requires a training set of input vectors that is representative of the source distribution, and it may not perform well for unknown or varying sources.



### Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree . The root node represents the entire input space, and the leaf nodes represent the final quantization regions .
- The advantage of TSVQ is that it can be represented by a binary tree, which reduces the storage cost, encoding rate, and quantization time compared to a full-search vector quantizer .
- TSVQ can be designed by using a top-down or a bottom-up approach . The top-down approach starts with the root node and splits it into two child nodes by using a splitting criterion, such as the average of the training vectors or the principal component analysis . The bottom-up approach starts with the leaf nodes and merges them into parent nodes by using a merging criterion, such as the minimum distortion or the maximum likelihood .
- TSVQ can achieve near-optimal performance if the tree structure is well matched to the input distribution . However, TSVQ may suffer from the curse of dimensionality, which means that the number of nodes in the tree grows exponentially with the dimension of the input vectors .

### Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses a sequence of input vectors by mapping them to a finite set of output vectors, called codevectors, which form a codebook .
- Scalar quantization (SQ) is a special case of VQ, where the input and output vectors are scalars, i.e., one-dimensional values .
- VQ has several advantages over SQ, such as :
  - VQ can exploit the correlation among the components of the input vectors, while SQ treats each component independently .
  - VQ can achieve higher compression ratios than SQ, since it can use fewer bits per vector than per scalar .
  - VQ can reduce the quantization noise and distortion, since it can approximate the input vectors more accurately than SQ .
  - VQ can adapt to the statistics of the input vectors, while SQ requires a fixed quantization step size .
  - VQ can perform joint source-channel coding, which means that it can protect the codevectors from transmission errors by using error-correcting codes .



### Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity and storage requirements of vector quantization .
- Vector quantization is a technique that maps a vector of input variables to a discrete set of code vectors, such that the distortion between the input and the output is minimized.
- Vector quantization is superior to scalar quantization, which operates on single variables, in terms of rate-distortion performance, i.e., the trade-off between the number of bits used to represent the input and the quality of the output.
- However, vector quantization also has some drawbacks, such as the high computational complexity of finding the optimal codebook and the optimal code vector for each input vector, and the large storage space needed to store the codebook.
- Structured vector quantizers aim to overcome these drawbacks by using some techniques, such as:
  - Tree-structured vector quantization (TSVQ), which uses a hierarchical partition of the input space and a tree-shaped codebook, such that the encoding and decoding can be done by following a root-to-leaf path in the tree .
  - Lattice vector quantization (LVQ), which uses a regular geometric structure of the code vectors, such that the codebook can be generated algorithmically and the encoding and decoding can be done by simple arithmetic operations.
  - Product vector quantization (PVQ), which decomposes the input vector into smaller subvectors and quantizes each subvector independently using a scalar or a vector quantizer, such that the codebook can be formed by the Cartesian product of the subcodebooks.
- Structured vector quantizers have some advantages over unstructured vector quantizers, such as:
  - Reduced complexity and storage requirements, as the codebook can be represented by a smaller number of parameters or generated on the fly  .
  - Faster encoding and decoding, as the search for the optimal code vector can be done by simple algorithms or operations  .
  - Adaptability to the input statistics, as the structure of the codebook or the partition can be adjusted to the input distribution or the distortion measure  .
  - Scalability and flexibility, as the structure of the codebook or the partition can be modified to suit different applications or constraints  .

