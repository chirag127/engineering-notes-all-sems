

Hello, I am Sydney, your AI assistant. I can help you with your study material on compression techniques. Here is an overview of the topic:

## Unit 1 - Compression Techniques

- Compression is the process of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, audio, and some images that require high fidelity.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for images, video, and some audio that can tolerate some degradation in quality.
- Compression techniques can be further divided into two types: entropy encoding and transform coding.
- Entropy encoding is based on the statistical properties of the data, such as the frequency of occurrence of symbols. It assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, thus reducing the average code length and the data size.
- Examples of entropy encoding techniques are Huffman coding, arithmetic coding, run-length encoding, and Lempel-Ziv coding.
- Transform coding is based on the mathematical transformation of the data, such as the Fourier transform or the discrete cosine transform. It converts the data from one domain (such as spatial or temporal) to another domain (such as frequency or wavelet) where the data can be represented more compactly and efficiently.
- Examples of transform coding techniques are JPEG, MPEG, MP3, and JPEG 2000.



### Lossless Compression

- Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information.
- Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data values or patterns are more frequent than others and can be encoded with fewer bits.
- Lossless compression is useful for applications that require exact preservation of data, such as text, executable programs, code modules, and images that need high quality.
- Lossless compression is also known as lossless audio compression, because it is often used to compress audio files without affecting the sound quality.
- Some examples of lossless compression algorithms are Huffman coding, arithmetic coding, run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, and deflate algorithm.
- Lossless compression can reduce the file size by a factor of 2 to 10, depending on the type and complexity of the data.
- Lossless compression is a reversible process, which means that the original data can be easily restored by decompressing the compressed data.
- Lossless compression is different from lossy compression, which discards some data in the compression process and produces a lower quality output.



### Lossy Compression

- Lossy compression is a class of data compression methods that uses inexact approximations and partial data discarding to represent the content.
- Lossy compression is most commonly used to compress multimedia data (audio, video, and images), especially in applications such as streaming media and internet telephony.
- Lossy compression reduces the data size for storing, handling, and transmitting content, but at the cost of losing some data permanently and degrading the quality of the content.
- There are two basic lossy compression schemes:
  - In lossy transform codecs, samples of picture or sound are taken, chopped into small segments, transformed into a new basis space, and quantized. The resulting quantized values are then entropy coded.
  - In lossy predictive codecs, previous and/or subsequent decoded data is used to predict the current sound sample or image frame. The error between the predicted data and the real data, together with an extra signal parameter, is quantized and coded.
- Lossy compression has some advantages and disadvantages:
  - Advantages:
    - Smaller file size and faster transmission
    - Suitable for web applications and streaming media
    - Can achieve high compression ratios with acceptable quality
  - Disadvantages:
    - Loss of detail and nuance in the content
    - Irretrievable data loss and no option to restore the original quality
    - File limitations and compatibility issues with some formats and devices



### Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or irrelevant information.
- The performance of compression techniques can be measured by various metrics, depending on the type and purpose of the data.
- Some common metrics are:

  - Compression ratio (CR): The ratio of the number of bits required to represent the data before compression to the number of bits required to represent the data after compression. A higher CR means a higher compression efficiency. CR = (original size / compressed size) 
  - Compression factor (CF): The inverse of compression ratio. CF = (compressed size / original size) 
  - Bits per character (bpc) or bits per pixel (bpp): The average number of bits required to represent one character or pixel of the data after compression. A lower bpc or bpp means a higher compression efficiency. bpc = (compressed size / number of characters) or bpp = (compressed size / number of pixels)  
  - Mean squared error (MSE): The average of the squared differences between the original and the compressed data values. A lower MSE means a higher compression quality. MSE = (1 / N) * sum((original value - compressed value)^2) 
  - Root mean squared error (RMSE): The square root of the MSE. A lower RMSE means a higher compression quality. RMSE = sqrt(MSE) 
  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible value of the data to the noise introduced by compression. A higher PSNR means a higher compression quality. PSNR = 10 * log10((max value)^2 / MSE) 
  - Structural similarity index (SSIM): A measure of the similarity between the original and the compressed data based on luminance, contrast, and structure. A higher SSIM means a higher compression quality. SSIM ranges from -1 to 1, where 1 means identical data. SSIM = (2 * mean(original) * mean(compressed) + c1) * (2 * covariance(original, compressed) + c2) / ((mean(original)^2 + mean(compressed)^2 + c1) * (variance(original) + variance(compressed) + c2)) 
  - Multi-scale structural similarity index (MS-SSIM): An extension of SSIM that considers different scales of the data. A higher MS-SSIM means a higher compression quality. MS-SSIM = product(SSIM(scale))^(weight(scale)) 
  - Accuracy: The percentage of correct or relevant information retained after compression. A higher accuracy means a higher compression quality. Accuracy = (number of correct or relevant information / number of total information) * 100 
  - Query execution time: The time required to execute a query on the compressed data. A lower query execution time means a higher compression performance. Query execution time = (end time - start time) 
  - Throughput: The rate of data processing or transmission after compression. A higher throughput means a higher compression performance. Throughput = (amount of data / time) 
  - Latency: The delay between the input and the output of the compression process. A lower latency means a higher compression performance. Latency = (output time - input time) 
  - Resource consumption: The amount of memory, CPU, disk, or network resources used by the compression process. A lower resource consumption means a higher compression performance. Resource consumption = (resource used / resource available) 

- Different compression techniques may have different trade-offs between these metrics, depending on the type and purpose of the data. For example, lossless compression techniques preserve the accuracy and quality of the data, but may have lower compression efficiency and performance than lossy compression techniques, which discard some information and introduce some noise or distortion to the data.   
- Therefore, the choice of compression technique and the measure of performance should be based on the specific requirements and constraints of the data and the application.



### Modeling and coding for data compression

Data compression is the process of reducing the size of data without losing any information. Data compression can be classified into two types: lossless and lossy. Lossless compression preserves the exact original data, while lossy compression discards some information that is deemed less important.

Data compression algorithms consist of two components: modeling and coding. Modeling is the process of finding patterns or regularities in the data, and coding is the process of assigning codes to the data based on the model.

#### Modeling

Modeling can be done in two ways: statistical or dictionary-based.

- Statistical modeling: This method analyzes the frequency or probability of each symbol in the data, and assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. Examples of statistical models are Huffman coding and arithmetic coding.
- Dictionary-based modeling: This method builds a dictionary of strings that appear in the data, and assigns codes to the strings based on their position in the dictionary. Examples of dictionary-based models are Lempel-Ziv (LZ) coding and Lempel-Ziv-Welch (LZW) coding.

#### Coding

Coding can be done in two ways: fixed-length or variable-length.

- Fixed-length coding: This method assigns codes of equal length to each symbol or string in the data. For example, ASCII coding uses 8 bits to represent each character.
- Variable-length coding: This method assigns codes of different lengths to each symbol or string in the data, depending on their frequency or position. For example, Huffman coding uses shorter codes for more frequent symbols and longer codes for less frequent symbols.

The choice of modeling and coding depends on the type and characteristics of the data, and the trade-off between compression ratio and complexity. Generally, statistical modeling and variable-length coding are more suitable for lossless compression, while dictionary-based modeling and fixed-length coding are more suitable for lossy compression.



### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the average amount of information per symbol in a data source .
- Entropy is defined as:

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is the set of possible symbols, and $p(x)$ is the probability of symbol $x$ occurring in the data source .
- Entropy is a lower bound for the average number of bits per symbol needed to encode the data source. The closer the entropy is to the average number of bits per symbol, the more efficient the compression scheme is .
- Lossless compression schemes can be classified into two categories: statistical and dictionary-based .
- Statistical compression schemes assign variable-length codes to symbols based on their probabilities. The more frequent symbols are assigned shorter codes, and the less frequent symbols are assigned longer codes. This reduces the average number of bits per symbol .
- Examples of statistical compression schemes are Huffman coding, arithmetic coding, and Golomb coding .
- Dictionary-based compression schemes use a predefined or dynamically generated dictionary of strings to replace repeated occurrences of the same string with a shorter code. This reduces the redundancy in the data .
- Examples of dictionary-based compression schemes are Lempel-Ziv (LZ) coding, Lempel-Ziv-Welch (LZW) coding, and Burrows-Wheeler transform (BWT) coding .



### A brief introduction to information theory

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding schemes.
- Information theory has applications in various fields, such as communication, cryptography, compression, statistics, machine learning, and biology.
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be either 0 or 1.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared between two random variables.
- Information theory also studies the limits and trade-offs of communication systems, such as channel capacity, which is the maximum rate of information that can be reliably transmitted over a noisy channel, or coding schemes, which are methods of encoding and decoding information to reduce errors or redundancy.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of Models for the notes of the Unit 1 - Compression Techniques.

### Models

- A model is a mathematical representation of the source of data that captures its essential features and properties.
- A model can be used to estimate the probability distribution of the data, which is useful for compression purposes.
- A model can be either static or adaptive.
  - A static model is fixed and does not change during the compression process. It is usually based on some prior knowledge or assumption about the data.
  - An adaptive model is updated and refined as the data is processed. It can adapt to the changing characteristics and patterns of the data.
- A model can be either parametric or non-parametric.
  - A parametric model is based on a finite number of parameters that describe the data. It can be simple and efficient, but may not capture the complexity and variability of the data.
  - A non-parametric model is based on the data itself, without assuming any specific form or structure. It can be more flexible and accurate, but may require more computation and storage.
- Some examples of models are:
  - Uniform model: assumes that all symbols have equal probability of occurrence.
  - Bernoulli model: assumes that each symbol is a binary outcome of a coin toss with a fixed probability of heads or tails.
  - Markov model: assumes that the probability of a symbol depends only on the previous symbol or a fixed number of previous symbols.
  - Context model: assumes that the probability of a symbol depends on the context or the surrounding symbols.
  - Dictionary model: assumes that the data consists of words or phrases that are stored in a dictionary or a codebook.



### Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Uniform model**: This model assumes that all the symbols in the source data are equally likely to occur. It is suitable for data that has no structure or correlation, such as random numbers or encrypted data. The uniform model can be used to calculate the entropy of the source data, which is the lower bound on the compression ratio. The entropy is given by H = log2(N), where N is the number of distinct symbols in the source data.

- **Static model**: This model assumes that the symbols in the source data have fixed probabilities that are known in advance or can be estimated from the data. It is suitable for data that has a stable distribution, such as natural language text or images. The static model can be used to design optimal prefix codes, such as Huffman codes, that assign shorter codes to more frequent symbols and longer codes to less frequent symbols. The average code length is given by L = sum(p_i * l_i), where p_i is the probability of symbol i and l_i is the length of its code.

- **Dynamic model**: This model assumes that the symbols in the source data have varying probabilities that depend on the context or the history of the data. It is suitable for data that has temporal or spatial correlation, such as audio or video. The dynamic model can be used to design adaptive codes, such as arithmetic codes, that update the probabilities of the symbols based on the observed data and encode the data using fractional bits. The average code length is given by L = sum(p_i * log2(1/p_i)), where p_i is the probability of symbol i given the context.

- **Markov model**: This model assumes that the symbols in the source data follow a Markov process, which means that the probability of the next symbol depends only on the previous k symbols, where k is the order of the model. It is a special case of the dynamic model that can capture the higher-order dependencies and patterns in the data. It is particularly useful for text compression, where the probability of the next letter is heavily influenced by the preceding letters. The Markov model can be used to design finite context codes, such as prediction by partial matching (PPM) codes, that use a tree structure to store the probabilities of the symbols given different contexts and encode the data using arithmetic coding. The average code length is given by L = sum(p_i * log2(1/p_i)), where p_i is the probability of symbol i given the k previous symbols.



### Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to the possible symbols or sequences of symbols that the source can generate.
- A probability model can be used to measure the information content of the data, and to design efficient compression algorithms that exploit the statistical properties of the data.
- There are different types of probability models, such as:
  - Uniform model: This model assumes that all the symbols in the alphabet have the same probability of occurrence. This model is suitable for random or unpredictable data, but not for data with patterns or regularities.
  - Unigram model: This model assigns probabilities to each symbol in the alphabet based on their frequencies in the data. This model is simple and easy to implement, but it does not capture the dependencies or correlations between symbols.
  - Markov model: This model assigns probabilities to each symbol based on the previous symbols in the sequence. This model can capture the context or history of the data, and is useful for text compression, where the probability of the next letter is influenced by the preceding letters.
  - Higher-order model: This model assigns probabilities to each symbol based on a longer context or history of the data. This model can capture more complex patterns or regularities in the data, but it also requires more memory and computation to store and update the probabilities.
  - Parametric model: This model assumes that the data follows a certain probability distribution, such as Poisson, Gaussian, or Zipf, and estimates the parameters of the distribution from the data. This model can avoid the undefined entropies that may occur in some models, and can also handle data with outliers or long tails.



### Markov models for data compression

- A Markov model is a mathematical model that describes a system that changes its state according to some probabilistic rules. The system is assumed to have the Markov property, which means that the future state of the system depends only on the current state and not on the past history.
- A Markov model can be used to model the source of a message, such as a text, an image, or a sound. The model can capture the statistical regularities and patterns of the message, such as the frequency of certain characters, words, or pixels, and the conditional probabilities of their occurrence given the previous context.
- A Markov model can be used for data compression by predicting the next symbol of the message based on the current context, and encoding the symbol using fewer bits if the prediction is accurate, or more bits if the prediction is inaccurate. The prediction can be done using a Markov chain, a hidden Markov model, or a variable-order Markov model, depending on the complexity and structure of the message.
- A Markov chain is a simple Markov model that has a finite number of states, and a transition matrix that specifies the probability of moving from one state to another. Each state can be associated with a symbol of the message, and the transition matrix can be estimated from the frequency of symbol pairs in the message. A Markov chain can predict the next symbol by choosing the most probable state given the current state, and encoding the symbol using an arithmetic coder or a Huffman coder.
- A hidden Markov model (HMM) is a more complex Markov model that has a finite number of hidden states, and a finite number of observable symbols. Each hidden state can emit one or more observable symbols with some probability, and the hidden states can transition from one to another with some probability. The hidden states and the transition and emission probabilities can be estimated from the message using the Baum-Welch algorithm or the Viterbi algorithm. An HMM can predict the next symbol by finding the most probable hidden state sequence given the observed symbols, and encoding the symbol using an arithmetic coder or a Huffman coder.
- A variable-order Markov model (VOMM) is a more flexible Markov model that can adapt the order of the context depending on the message. The order of the context is the number of previous symbols that are used to predict the next symbol. A higher order context can capture more information and make better predictions, but it also requires more memory and computation. A VOMM can adjust the order of the context by using a tree structure that stores the conditional probabilities of symbols given different contexts, and pruning or growing the tree as needed. A VOMM can predict the next symbol by finding the longest matching context in the tree, and encoding the symbol using an arithmetic coder or a Huffman coder.
- A dynamic Markov compression (DMC) is a special case of a VOMM that predicts one bit at a time, rather than one symbol at a time. This makes it slower but gives slightly better compression. It uses a binary tree that stores the conditional probabilities of bits given different contexts, and updates the tree dynamically as new bits are processed. A DMC can predict the next bit by finding the longest matching context in the tree, and encoding the bit using an arithmetic coder.



### Composite source model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them at a time.
- A composite source can be represented as a number of individual sources S i, each with its own model M i and a switch that selects a source S i with probability P i.
- A composite source model is useful for applications where a single model is not adequate to capture the characteristics of the data, such as text, speech, images, etc.
- A composite source model can be used to achieve better data compression by exploiting the correlations and redundancies among the different sources.
- A composite source model can be implemented using different techniques, such as:
  - Concatenating the outputs of the individual sources and encoding them as a single stream.
  - Encoding each source separately and transmitting them along with the switch information.
  - Using a universal code that can adapt to the changes in the source statistics.
- A composite source model can also be combined with other data reduction techniques, such as:
  - Import modeling, which involves loading the source data into memory and compressing it using the VertiPaq storage engine.
  - DirectQuery, which involves connecting to the source data without importing it and querying it on demand .
  - Composite modeling, which involves connecting to multiple sources with different modes (import or DirectQuery) and creating relationships among them .

: Data compression Interview Questions & Answers
: Data reduction techniques for Import modeling - Power BI
: Briefly explain Modeling and coding with respect to data compression
: Use composite models in Power BI Desktop - Power BI
: Composite Model in Power BI; DirectQuery and Import Data Combined



Hello, I am Sydney, your AI assistant. I can help you with your notes on coding for the unit 1 - compression techniques in the subject of data compression. Here is a summary of the main topics:

# Coding for Compression Techniques

- Coding is the process of assigning symbols or codes to the elements of a source alphabet, such as characters, words, or pixels.
- Coding can be used for various purposes, such as encryption, error detection, or compression.
- Compression is the reduction of the size of data by removing redundancy or irrelevance, without losing the essential information.
- Compression can be classified into two types: lossless and lossy.
- Lossless compression preserves the exact original data, while lossy compression allows some distortion or degradation of the data, in exchange for higher compression ratios.
- Lossless compression techniques include run-length encoding, Huffman coding, arithmetic coding, Lempel-Ziv coding, and dictionary coding.
- Lossy compression techniques include transform coding, quantization, vector quantization, and predictive coding.

## Run-length Encoding

- Run-length encoding (RLE) is a simple lossless compression technique that replaces consecutive identical symbols with a pair of the symbol and its frequency.
- For example, the string "AAAAABBBBCCCC" can be compressed as "5A4B4C".
- RLE is suitable for compressing data with long runs of the same symbol, such as binary images or text documents with many spaces.
- RLE is not efficient for compressing data with high entropy or randomness, such as natural images or audio signals.

## Huffman Coding

- Huffman coding is a lossless compression technique that assigns variable-length codes to the symbols of a source alphabet, based on their probabilities of occurrence.
- The codes are constructed by building a binary tree, where the leaves are the symbols and the branches are the bits of the codes.
- The codes are optimal, meaning that they minimize the average code length for a given source distribution.
- For example, given the source alphabet {A, B, C, D} with probabilities {0.4, 0.3, 0.2, 0.1}, the Huffman codes are {0, 10, 110, 111}.
- Huffman coding is suitable for compressing data with known or estimable source probabilities, such as text or image files.
- Huffman coding is not efficient for compressing data with uniform or unknown source probabilities, such as encrypted or random data.



### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  Kraft inequality

  where D is the size of the code alphabet.

- The Kraft inequality can be extended to any uniquely decodable code, not just prefix-free codes, by using the McMillan theorem, which states that for any uniquely decodable code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  McMillan theorem

  where D is the size of the code alphabet.

- The Kraft inequality and the McMillan theorem can be used to prove the optimality of certain codes, such as Huffman codes and Shannon-Fano codes, which are based on the source probabilities and the code alphabet size.

- Uniquely decodable codes are useful for data compression, as they allow the receiver to recover the original data without ambiguity or error. They also have applications in cryptography, error correction, and information theory.



### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

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
- The algorithm starts by creating a node for each symbol and assigning it a frequency equal to its occurrence in the data. Then, it repeatedly merges the two nodes with the lowest frequencies into a new node, whose frequency is the sum of the two merged nodes. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to that symbol, and appending a 0 or a 1 depending on whether the left or the right branch is taken at each node. The code is prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible code for a given set of symbols and frequencies. It also minimizes the average code length, which is the weighted sum of the code lengths of each symbol, where the weights are the frequencies of the symbols.
- The Huffman coding algorithm can be applied to any type of data, such as text, images, audio, or video. It can also be combined with other compression techniques, such as run-length encoding or arithmetic coding, to achieve higher compression ratios.



### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the lowest probability gets the longest code and the code with the highest probability gets the shortest code.
- The expected code length is the weighted average of the code lengths, where the weights are the symbol probabilities.
- The variance of the code length is the weighted average of the squared deviations of the code lengths from the expected code length, where the weights are the symbol probabilities.
- The minimum variance Huffman code is a variant of Huffman coding that minimizes not only the expected code length but also the variance of the code length .
- The minimum variance Huffman code has the property that the code lengths are as close as possible to each other, and the difference between the maximum and minimum code lengths is at most one.
- The minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in nonincreasing order of probability and assign them to the leaves of a binary tree.
  - Repeat until there is only one node left:
    - Select the two nodes with the smallest probabilities and merge them into a new node with the probability equal to the sum of their probabilities.
    - If the two nodes have different depths in the tree, increase the depth of the shallower node by one.
    - Insert the new node into the sorted list of nodes.
  - Assign a bit (0 or 1) to each edge of the tree and concatenate the bits along the path from the root to each leaf to obtain the code for each symbol.
- The minimum variance Huffman code can be useful for applications where the variance of the code length is important, such as real-time communication or encryption.



### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data. 

The main idea of adaptive Huffman coding is to maintain a binary tree that represents the code for each symbol, and update the tree whenever a new symbol is encountered or an existing symbol is repeated. The tree is initialized with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen so far. The tree is updated according to the following rules:

- When a new symbol is encountered, it is assigned a code consisting of the current code for the NYT node followed by a fixed-length code for the symbol (usually the binary representation of its ASCII value). The NYT node is then split into two nodes: a new NYT node and a leaf node for the new symbol, both with a weight of 1. The new symbol node is placed as the right child of the old NYT node, and the new NYT node is placed as the left child. The old NYT node becomes an internal node with a weight of 2 (the sum of its children's weights).
- When an existing symbol is encountered, it is encoded using its current code in the tree. The weight of its node is incremented by 1, and the tree is restructured to preserve the Huffman property: the nodes are ordered by increasing weight, and nodes with equal weight are ordered by increasing order of appearance. To restructure the tree, the following steps are performed:
  - Find the highest numbered (rightmost) node in the same block (set of nodes with the same weight) as the symbol node. If the symbol node is not the highest numbered node in its block, swap it with the highest numbered node. This ensures that the symbol node moves up in the tree as its frequency increases.
  - Increment the weight of the symbol node and its ancestors by 1.
  - Repeat the above steps until the root of the tree is reached.

The following diagram shows an example of adaptive Huffman coding for the string "ABRACADABRA". The numbers in the nodes indicate the weights, and the letters in the nodes indicate the symbols. The codes for each symbol are shown below the tree.

Adaptive Huffman coding example

The codes for each symbol are:

- A: 0
- B: 100
- R: 101
- C: 1100
- D: 1101

The encoded string is:

0 100 101 0 1100 0 1101 0 100 101 0

The encoded string has 23 bits, while the original string has 88 bits (assuming 8 bits per character), so the compression ratio is 23/88 = 0.26.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here is the update procedure for the notes of the Unit 2 - The Huffman coding algorithm:

1. Review the learning objectives and outcomes of the unit. They are:

- Explain the concept of entropy and how it relates to data compression.
- Describe the steps of the Huffman coding algorithm and how it generates optimal prefix codes.
- Apply the Huffman coding algorithm to encode and decode messages using binary trees and tables.
- Analyze the performance and limitations of the Huffman coding algorithm.

2. Read the updated notes of the unit. They are:

- Entropy is a measure of the uncertainty or randomness of a source of data. It can also be interpreted as the average amount of information per symbol produced by the source. The lower the entropy, the more predictable and compressible the data is. The higher the entropy, the more unpredictable and incompressible the data is. Entropy can be calculated using the formula: H(X) = - sum(p(x) * log2(p(x))) where X is the source, x is a symbol, and p(x) is the probability of x occurring.
- The Huffman coding algorithm is a greedy algorithm that assigns variable-length codes to symbols based on their frequencies. The algorithm works as follows:

  - Create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue, do the following:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with the sum of the frequencies of the two nodes as its frequency.
    - Assign the left child of the new node to be the first node removed, and the right child to be the second node removed.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the tree and assign codes to the symbols. The code of a symbol is the sequence of bits along the path from the root to the leaf node representing the symbol. A left branch is assigned a 0 bit, and a right branch is assigned a 1 bit.

- To encode a message using the Huffman coding algorithm, we need to construct the Huffman tree and the code table for the symbols in the message. The code table maps each symbol to its corresponding code. Then, we replace each symbol in the message with its code and concatenate the codes to form the encoded message.
- To decode a message using the Huffman coding algorithm, we need to have the Huffman tree or the code table for the symbols in the message. Then, we scan the message from left to right and match the bits with the codes in the table or the branches in the tree. When we find a match, we output the corresponding symbol and move to the next bit.

- The Huffman coding algorithm is optimal in the sense that it produces the shortest possible code for a given source and probability distribution. The average length of the code is equal to the entropy of the source, which is the lower bound for any lossless compression scheme. However, the Huffman coding algorithm also has some limitations, such as:

  - It requires the knowledge of the frequencies of the symbols in advance, which may not be available or accurate for some sources.
  - It assumes that the symbols are independent and identically distributed, which may not be true for some sources.
  - It can only handle discrete and finite sources, which may not be suitable for some types of data, such as images, audio, or video.

3. Test your understanding of the unit by answering the following questions:

- What is the entropy of a source that produces four symbols with probabilities 0.5, 0.25, 0.125, and 0.125?
- What is the Huffman code for the message "abracadabra"?
- How many bits are saved by using the Huffman code instead of a fixed-length code of 3 bits per symbol for the message "abracadabra"?



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  . It is a greedy algorithm that builds a binary tree of the input characters, where the most frequent characters are near the root and the least frequent characters are far from the root  . The codes are then derived from the paths of the characters in the tree, where left branches are assigned 0 and right branches are assigned 1  . The codes are prefix-free, meaning that no code is a prefix of another code .

The encoding procedure for the Huffman coding algorithm can be summarized as follows :

- Create a leaf node for each character and add it to the priority queue.
- While there is more than one node in the queue:
  - Remove the two nodes of the highest priority (the lowest frequency) from the queue.
  - Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.
  - Add the new node to the queue.
- The remaining node is the root node and the tree is complete.
- Traverse the tree and assign codes to each character. The code of a character is the sequence of 0s and 1s from the root to the leaf node of that character.

Here is an example of applying the Huffman coding algorithm to the string "BANANA":

- The frequencies of the characters are: B: 1, A: 3, N: 2.
- Create a leaf node for each character and add it to the priority queue: [B: 1, A: 3, N: 2].
- Remove the two nodes of the highest priority (the lowest frequency) from the queue and create a new internal node with them as children: [A: 3, N: 2, (B: 1, *: 1): 2], where * is a dummy character to indicate an internal node.
- Repeat the previous step until there is only one node left in the queue: [(A: 3, (N: 2, (B: 1, *: 1): 2): 4): 7], which is the root node of the tree.
- Traverse the tree and assign codes to each character: B: 110, A: 0, N: 10.
- The encoded string is: 0110100110.



Hello, I am Sydney, your AI assistant. I can help you with your study material on the topic of decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression. Here is the content in markdown format:

### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the source data.
- The Huffman code is a prefix code, which means that no code is a prefix of another code. This property ensures that the code is uniquely decodable.
- The decoding procedure for the Huffman code is as follows:
  - Given a Huffman code and a bitstream of encoded data, start from the root of the Huffman tree and traverse it according to the bits in the bitstream.
  - If the bit is 0, go to the left child of the current node. If the bit is 1, go to the right child of the current node.
  - If the current node is a leaf node, output the symbol associated with that node and return to the root of the tree.
  - Repeat the above steps until the end of the bitstream is reached or an error occurs.
- For example, consider the following Huffman tree and the bitstream 0110110010:

Huffman tree

- The decoding procedure is as follows:

| Bit | Current node | Output |
| --- | ------------ | ------ |
| 0   | A            |        |
| 1   | B            |        |
| 1   | D            | D      |
| 0   | A            |        |
| 1   | B            |        |
| 1   | D            | D      |
| 0   | A            |        |
| 0   | C            | C      |
| 1   | B            |        |
| 0   | E            | E      |

- The decoded output is DDCDE.



### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: the unary code for q+1, followed by the truncated binary code for r .
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The truncated binary code for r depends on whether M is a power of 2 or not .
  - If M is a power of 2, say M=2^n, then r is encoded using n bits in standard binary. For example, if M=8, then r=5 is encoded as 101 .
  - If M is not a power of 2, say M=2^n+k, where 0<k<2^n, then r is encoded using one of two methods :
    - If r<k, then r is encoded using n bits in standard binary. For example, if M=10, then r=3 is encoded as 011 .
    - If r>=k, then r is encoded using n+1 bits, where the first bit is 1 and the remaining n bits are the standard binary representation of r-k. For example, if M=10, then r=7 is encoded as 1011 .
- The length of the codeword for x is q+n or q+n+1 bits, depending on the value of r and M.
- Golomb codes are optimal for data with geometric distributions, where the probability of x is proportional to (1-p)^x for some p.
- Golomb codes are also useful for data with exponential distributions, where the probability of x is proportional to e^(-x/lambda) for some lambda.
- Golomb codes can be generalized to Rice codes, where M is restricted to be a power of 2, and Elias codes, where M is a function of x.



### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that are optimal for encoding data with geometrically distributed probabilities.
- Rice codes use a parameter k, which is related to the parameter m of Golomb codes by m = 2^k^.
- Rice codes are simpler to implement than Golomb codes, but they may not be optimal for all distributions.
- Rice codes are often used to encode the entropy or the residual data in audio and video compression algorithms.
- The encoding process of Rice codes is as follows:
  - Given a positive integer x and a parameter k, divide x by 2^k^ and obtain the quotient q and the remainder r.
  - Encode q as a unary code, which is a string of q ones followed by a zero.
  - Encode r as a k-bit binary code, which is the binary representation of r with leading zeros if necessary.
  - Concatenate the unary code and the binary code to form the Rice code of x.
- For example, if x = 13 and k = 2, then q = 3 and r = 1. The unary code of q is 1110 and the binary code of r is 01. The Rice code of x is 111001.
- The decoding process of Rice codes is the reverse of the encoding process:
  - Given a Rice code and a parameter k, count the number of ones before the first zero and obtain the quotient q.
  - Read the next k bits and obtain the remainder r as a binary number.
  - Multiply q by 2^k^ and add r to obtain the original integer x.
  - For example, if the Rice code is 111001 and k = 2, then q = 3 and r = 1. The original integer x is 3 * 2^2^ + 1 = 13.



### Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression.
- Tunstall codes are variable-to-fixed length codes, which means they map variable-length source words to fixed-length codewords .
- Tunstall codes are based on a prefix tree that is constructed from a given source probability distribution .
- Tunstall codes are optimal for memoryless sources with rational probabilities.
- Tunstall codes are a precursor to Lempel–Ziv codes, which are widely used in practice.
- Tunstall codes have some advantages over Huffman codes, such as being able to handle any source alphabet size and having a simpler encoding and decoding process.
- Tunstall codes have some disadvantages, such as requiring a large codebook size and being sensitive to errors in the source probability estimation.



### Applications of Huffman coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or weight. The more frequent a data value is, the shorter its code will be. The less frequent a data value is, the longer its code will be. This way, the data can be represented using fewer bits on average, saving space and bandwidth.

Some of the applications of Huffman coding are:

- **Transmitting fax and text**: Huffman coding can be used to compress the text or fax data before sending it over a communication channel, reducing the transmission time and cost. For example, the CCITT Group 3 standard for fax transmission uses a variant of Huffman coding to encode the black and white pixels of the scanned document.
- **Conventional compression formats**: Huffman coding is often used by conventional compression formats like PKZIP, GZIP, BZIP2, etc. to compress the data after applying other compression techniques like run-length encoding, dictionary encoding, etc. For example, the GZIP format uses a combination of LZ77 and Huffman coding to compress the data .
- **Multimedia codecs**: Huffman coding is also used by multimedia codecs like JPEG, PNG, and MP3 to compress the data after applying other compression techniques like discrete cosine transform, quantization, etc. For example, the JPEG format uses Huffman coding to encode the quantized coefficients of the DCT blocks of the image .
- **Other applications**: Huffman coding can also be used for other applications like encryption, error correction, data analysis, etc. For example, Huffman coding can be used to encrypt the data by using a secret code table that is known only to the sender and the receiver. Huffman coding can also be used to correct the errors in the data by adding some redundancy to the code words. Huffman coding can also be used to analyze the data by finding the frequency or weight of the data values  .



### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or visual appearance.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding for image compression are:

  1. Calculate the probability of each pixel value in the image and sort them in descending order.
  2. Create a binary tree with the pixel values as leaf nodes and their probabilities as weights. The two nodes with the lowest probabilities are combined into a parent node with the sum of their probabilities as the new weight. Repeat this process until there is only one root node left.
  3. Assign a binary code to each node by traversing the tree from the root to the leaves. The code is formed by appending 0 for a left branch and 1 for a right branch.
  4. Replace each pixel value in the image with its corresponding binary code and store the codebook (the mapping of pixel values to codes) along with the compressed image.

- The advantages of Huffman coding for image compression are:

  - It is optimal in the sense that it minimizes the average code length for a given source distribution.
  - It is simple and easy to implement.
  - It is widely used in many applications, such as JPEG, ZIP, MP3, etc.

- The disadvantages of Huffman coding for image compression are:

  - It requires the knowledge of the source distribution, which may not be available or may change over time.
  - It is not adaptive, meaning that it cannot adjust the codebook to the changing source statistics.
  - It is not efficient for images with a large number of pixel values or a uniform distribution, as the code length may be close to or even exceed the original pixel size.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters more efficiently.
- Text compression can save storage space, bandwidth, and transmission time.
- Text compression can be lossless or lossy. Lossless compression preserves the original information, while lossy compression discards some information to achieve higher compression ratios.
- The Huffman coding algorithm is a lossless compression method that assigns variable-length codes to the characters of a text file based on their frequencies.
- The Huffman coding algorithm works as follows:
  - Create a frequency table that counts the occurrences of each character in the text file.
  - Create a priority queue that stores each character and its frequency as a node, sorted by ascending frequency.
  - While the queue has more than one node, do the following:
    - Dequeue the two nodes with the lowest frequency and create a new node with the sum of their frequencies as its frequency and the two nodes as its left and right children.
    - Enqueue the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign a binary code to each character by appending 0 for left branches and 1 for right branches.
  - Encode the text file by replacing each character with its corresponding code.
  - Decode the text file by traversing the Huffman tree from the root to the leaves based on the bits of the code.



Hello, I am Sydney, your AI assistant. I can help you with your topic of audio compression using Huffman coding. Here are some notes for you:

### Audio Compression using Huffman Coding

- Audio compression is the process of reducing the size of an audio file by removing redundant or irrelevant information.
- Huffman coding is a lossless compression technique that assigns variable-length codes to the symbols (such as samples or amplitudes) in the audio file based on their frequencies of occurrence.
- The symbols with higher frequencies are assigned shorter codes, while the symbols with lower frequencies are assigned longer codes.
- Huffman coding is independent of the data type, meaning it can be applied to any kind of data, such as images, text, or audio .
- Huffman coding is used in some audio compression standards, such as JPEG and MPEG-2.
- The steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the audio file.
  - Build a binary tree that represents the codes for each symbol. The tree is constructed by merging the two least frequent symbols into a new node, and repeating this process until there is only one node left. The root node represents the entire file, and the leaf nodes represent the symbols. The code for each symbol is obtained by traversing the tree from the root to the leaf, and appending 0 or 1 depending on the direction of the branch.
  - Encode the audio file by replacing each symbol with its corresponding code from the tree.
  - Decode the compressed file by traversing the tree from the root to the leaf, and outputting the symbol at each leaf node.

- Huffman coding is optimal in the sense that it minimizes the average code length for a given set of symbols and frequencies.
- However, Huffman coding has some limitations, such as:

  - It requires the knowledge of the frequencies of the symbols in advance, or the transmission of the frequency table or the tree along with the compressed file, which adds some overhead.
  - It does not exploit the correlation or redundancy between adjacent symbols, which may result in suboptimal compression ratios.
  - It does not take into account the perceptual characteristics of the human auditory system, which may allow for some lossy compression without affecting the quality of the sound.

- Therefore, Huffman coding is often combined with other techniques, such as quantization, run-length encoding, or perceptual noise shaping, to achieve better audio compression performance  .



## Unit 3 - Coding a sequence

- A sequence is a set of ordered values or items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula, a table, a graph, or a list of values.
- To code a sequence, we need to use a loop structure that repeats a set of instructions for each term of the sequence.
- A loop structure can be a for loop, a while loop, or a do-while loop, depending on the programming language and the logic of the sequence.
- A for loop is used when we know the exact number of iterations or the range of values for the sequence.
- A while loop is used when we do not know the exact number of iterations or the range of values for the sequence, but we have a condition that determines when to stop the loop.
- A do-while loop is similar to a while loop, but it executes the instructions at least once before checking the condition.
- To code a sequence, we also need to use a variable that stores the current term of the sequence, and update it according to the formula or the rule of the sequence.
- We can also use another variable to store the index or the position of the current term in the sequence, and increment it by one for each iteration of the loop.
- We can also use an array or a list to store the terms of the sequence, and access them by using the index variable as the subscript or the index of the array or the list.
- We can also use a function or a method to generate the terms of the sequence, and call it inside the loop with the appropriate arguments or parameters.
- We can also use a print statement or a return statement to display or output the terms of the sequence, either individually or as a whole.
- Here is an example of coding a sequence in Python:

```python
# The sequence is the Fibonacci sequence, which starts with 1 and 1, and each term is the sum of the previous two terms.
# The sequence is infinite, but we will only generate the first 10 terms.

# Define a function that takes an index as a parameter and returns the corresponding term of the sequence
def fibonacci(n):
  # Base cases: if n is 1 or 2, return 1
  if n == 1 or n == 2:
    return 1
  # Recursive case: if n is greater than 2, return the sum of the previous two terms
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Use a for loop to iterate from 1 to 10, and call the function with the index as the argument
for i in range(1, 11):
  # Print the term of the sequence
  print(fibonacci(i))
```



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it more efficiently.
- Binary code is a way of representing data using only two symbols: 0 and 1.
- A binary code for a sequence of symbols is a mapping that assigns a unique binary codeword to each symbol in the sequence.
- The length of a binary codeword is the number of bits it contains.
- The goal of data compression is to minimize the total length of the binary code for a given sequence of symbols, while preserving the information content of the original sequence.
- There are two types of data compression: lossless and lossy.
  - Lossless compression is a compression technique that allows the original sequence of symbols to be reconstructed exactly from the compressed binary code.
  - Lossy compression is a compression technique that allows some information loss in the original sequence of symbols, but achieves higher compression ratios than lossless compression.
- There are different methods of generating a binary code for a sequence of symbols, depending on the characteristics of the sequence and the compression technique used.
  - Fixed-length binary code is a binary code that assigns codewords of the same length to all symbols in the sequence. For example, a binary code that uses three bits to encode six symbols is a fixed-length binary code. This type of code is simple and easy to decode, but it may not be efficient if the symbols have different frequencies in the sequence.
  - Variable-length binary code is a binary code that assigns codewords of different lengths to different symbols in the sequence. For example, a binary code that uses one bit to encode the most frequent symbol, two bits to encode the second most frequent symbol, and three bits to encode the rest of the symbols is a variable-length binary code. This type of code is more efficient than fixed-length binary code, but it requires more complex encoding and decoding algorithms. A variable-length binary code must also be a prefix code, which means that no codeword is a prefix of another codeword. This ensures that the binary code can be uniquely decoded without ambiguity.
  - Universal code is a type of variable-length binary code that can be used to encode any sequence of positive integers, regardless of their probability distribution. For example, a universal code that uses one bit to encode the integer 1, two bits to encode the integers 2 and 3, three bits to encode the integers 4 to 7, and so on, is a universal code. This type of code is useful for encoding the lengths or frequencies of symbols in a sequence, which are often integers. A universal code has the property that the expected length of the codewords is within a constant factor of the optimal length for any monotonic probability distribution.
  - Huffman code is a type of variable-length binary code that is optimal for a given sequence of symbols, meaning that it minimizes the total length of the binary code for that sequence. A Huffman code is constructed by using a binary tree, where each leaf node represents a symbol and its frequency, and each internal node represents the sum of the frequencies of its children. The codeword for each symbol is obtained by traversing the tree from the root to the leaf, and appending a 0 or a 1 depending on whether the left or the right child is taken. A Huffman code is a prefix code and a universal code, and it can be used for lossless compression of any sequence of symbols.
  - LZW code is a type of variable-length binary code that is based on a dictionary of sequences of symbols, rather than individual symbols. A LZW code is constructed by using a code table, where each entry represents a sequence of symbols and its corresponding codeword. The code table is initialized with the basic symbols and their fixed-length codewords. The encoding process consists of scanning the input sequence and finding the longest matching sequence in the code table. The codeword for that sequence is output, and a new entry is added to the code table with the next symbol appended to the sequence. The decoding process consists of reading the codewords and finding the corresponding sequences in the code table. The sequences are output, and a new entry is added to the code table with the next symbol appended to the sequence. A LZW code is a prefix code and a universal code, and it can be used for lossless compression of any sequence of symbols.



### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using fixed-length binary words, where each character or symbol is assigned a unique code. For example, the ASCII code uses 8 bits to represent 256 characters.
- Huffman coding is a method of representing data using variable-length binary words, where each character or symbol is assigned a code based on its frequency of occurrence in the data. For example, the most frequent character may be assigned a single bit, while the least frequent character may be assigned a longer code.
- The main advantage of Huffman coding over binary coding is that it can achieve higher compression ratios, since it uses shorter codes for more frequent characters and longer codes for less frequent characters. This reduces the overall size of the data and saves storage space and bandwidth.
- The main disadvantage of Huffman coding over binary coding is that it requires an extra step of generating a Huffman tree, which is a binary tree that shows the codes for each character based on their frequencies. This tree needs to be stored or transmitted along with the data, which adds some overhead. Also, Huffman coding is not suitable for data that has a uniform distribution of characters, since it will not reduce the size of the data significantly.
- The main application of Huffman coding is in lossless data compression, where the original data can be recovered exactly from the compressed data. This is useful for text, audio, and image files that need to preserve their quality and integrity. Binary coding is more commonly used for encoding data that does not need to be compressed, such as binary numbers, instructions, and commands.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression.

### Applications

- Coding a sequence is a technique to represent a sequence of symbols using fewer bits than the original representation. This can reduce the storage space and transmission time of the sequence.
- Coding a sequence can be applied to various types of data, such as text, images, audio, video, etc. Some examples are:

  - Text compression: Coding a sequence can reduce the size of text files by using shorter codes for more frequent symbols, such as letters or words. For example, Huffman coding is a popular method to compress text files by assigning variable-length codes to symbols based on their frequencies.
  - Image compression: Coding a sequence can reduce the size of image files by using shorter codes for more frequent pixel values, such as colors or brightness. For example, JPEG is a popular method to compress image files by using Huffman coding and other techniques to reduce the redundancy in the image data.
  - Audio compression: Coding a sequence can reduce the size of audio files by using shorter codes for more frequent sound samples, such as frequencies or amplitudes. For example, MP3 is a popular method to compress audio files by using Huffman coding and other techniques to reduce the redundancy in the sound data.
  - Video compression: Coding a sequence can reduce the size of video files by using shorter codes for more frequent frames, such as motion vectors or differences. For example, MPEG is a popular method to compress video files by using Huffman coding and other techniques to reduce the redundancy in the video data.



### Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image, without losing any information or quality.
- The JBIG standard (Joint Bi-level Image Experts Group) is an early lossless image compression standard for bi-level images, standardized as ISO/IEC 11544 and ITU-T T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines and can also be used on other bi-level images.
- The JBIG standard offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement.
- The JBIG standard uses a combination of arithmetic coding and adaptive template matching to achieve high compression ratios.
- The JBIG standard consists of three main components: the encoder, the decoder, and the arithmetic coder.
- The encoder divides the input image into stripes of 128 rows each and processes each stripe independently.
- The encoder assigns a context number to each pixel based on the values of its neighboring pixels and the template used.
- The encoder sends the context number and the pixel value to the arithmetic coder, which produces a compressed bitstream.
- The decoder receives the compressed bitstream and performs the inverse operations of the encoder to reconstruct the original image.
- The arithmetic coder is a key component of the JBIG standard, as it provides the entropy coding of the context numbers and pixel values.
- The arithmetic coder uses a probability model that adapts to the statistics of the input data and assigns shorter codes to more probable symbols.
- The arithmetic coder can achieve near-optimal compression performance, as it approaches the entropy limit of the input data.
- The JBIG standard also supports progressive transmission, which allows the decoder to display a low-resolution version of the image before receiving the full bitstream.
- The JBIG standard also supports multiple resolution coding, which allows the encoder to produce different versions of the image at different resolutions and quality levels.
- The JBIG standard also supports lossy compression, which allows the encoder to reduce the image quality by merging similar contexts or using fewer bits per pixel.
- The JBIG standard is also known as JBIG1, as it was superseded by the JBIG2 standard in 2000.
- The JBIG2 standard is a newer image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group.
- The JBIG2 standard is suitable for both lossless and lossy compression and can achieve higher compression ratios than the JBIG standard.
- The JBIG2 standard exploits model-based coding for text and halftones, as well as nearby neighbor based coding for generic bi-level images.
- The JBIG2 standard also uses arithmetic coding and adaptive context formation, but with more sophisticated techniques than the JBIG standard.
- The JBIG2 standard can compress bi-level images up to 10 times better than the JBIG standard and up to 100 times better than Fax Group 4 compression.
- The JBIG2 standard is widely used in document imaging, such as PDF files and scanned documents.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group  .
- Bi-level images are images that have only two colors, usually black and white, such as scanned documents, faxes, or text.
- JBIG2 is suitable for both lossless and lossy compression  .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than existing standards, such as MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544), by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, and then compressing each region with a different method.
- Text regions are compressed by identifying and encoding recurring symbols, such as characters or words, and then using a dictionary to store and reference them.
- Halftone regions are compressed by detecting and removing the halftone screen, and then encoding the remaining gray-level image with a suitable method.
- Generic regions are compressed by applying a context-based arithmetic coding scheme, similar to JBIG1, but with improved contexts and adaptive templates.
- JBIG2 can also support progressive decoding, which means that a low-resolution or low-quality version of the image can be displayed before the full image is available.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.



### Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, without any loss of information. Lossless compression is suitable for images that require high fidelity, such as medical images, text, and graphics. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. Deflate is used in formats such as PNG, ZIP, and GZIP.
  - Run-length encoding: Run-length encoding is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. Run-length encoding is effective for images that have large areas of uniform color, such as icons and logos.
  - Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. Arithmetic coding is more efficient than Huffman coding, but also more complex and slower.

- Lossy compression: Lossy compression is a technique that discards some of the original data, resulting in some loss of quality. Lossy compression is suitable for images that can tolerate some degradation, such as photographs and videos. Lossy compression algorithms include:

  - Transform coding: Transform coding is a lossy image compression technique that uses mathematical transformations to reduce the size of an image. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. Transform coding is commonly used for JPEGs.
  - Discrete cosine transform: Discrete cosine transform (DCT) is the most widely used form of transform coding. DCT is a type of Fourier-related transform, and was originally developed by Nasir Ahmed, T. Natarajan and K. R. Rao in 1974. DCT converts an image into a sum of cosine functions of different frequencies, and then discards the high-frequency components that are less visible to the human eye.
  - JPEG: JPEG is the most popular image format that uses lossy compression. JPEG stands for Joint Photographic Experts Group, which is the name of the committee that created the standard in 1992. JPEG uses DCT to compress an image into blocks of 8x8 pixels, and then applies a quantization matrix to reduce the number of bits per block. JPEG allows the user to adjust the compression level and the quality of the image.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on dictionary techniques for data compression.

### Dictionary Techniques

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the size of the data and improves the compression ratio.
- There are many variants of dictionary techniques, such as LZ77, LZ78, LZW, LZSS, LZMA, etc. They differ in the way they construct and manage the dictionary, the way they encode and decode the matches, and the way they handle special cases such as unmatched symbols or long matches.
- Dictionary techniques are suitable for compressing text, images, audio, and other types of data that have some degree of redundancy or regularity. They can achieve high compression ratios and fast decompression speeds, but they may require more memory and processing power than other techniques .



### Introduction

- Data compression is the process of reducing the size of data without losing information or quality.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, Huffman coding, run-length encoding, etc.
- Coding a sequence is one of the techniques of data compression, which involves assigning codes to symbols or groups of symbols in a given sequence of data.
- Coding a sequence can be classified into two types: fixed-length coding and variable-length coding.
- Fixed-length coding assigns codes of equal length to all symbols, regardless of their frequency or probability of occurrence in the sequence.
- Variable-length coding assigns codes of different lengths to symbols, depending on their frequency or probability of occurrence in the sequence. The more frequent or probable a symbol is, the shorter its code is, and vice versa.
- Variable-length coding can achieve better compression than fixed-length coding, as it exploits the statistical properties of the sequence and assigns shorter codes to more common symbols.
- However, variable-length coding also introduces some challenges, such as ambiguity, prefix property, code efficiency, code optimality, etc.
- In this unit, we will learn about the principles and methods of coding a sequence, and how to overcome the challenges of variable-length coding. We will also learn about some applications and examples of coding a sequence in data compression.



### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression has the advantage of being fast and simple, but it may not be optimal for compressing data that has a different distribution or structure than the dictionary .
- Static dictionary compression can be implemented by using a hash table or a trie to store the dictionary entries and their corresponding codes, and then scanning the input data and looking up the longest matching phrase or symbol in the dictionary .
- Static dictionary compression can be combined with other techniques, such as Huffman coding or arithmetic coding, to further reduce the size of the output .
- Static dictionary compression can be applied to various types of data, such as text, images, audio, or video, depending on the nature and size of the dictionary  .
- Static dictionary compression can be evaluated by measuring the compression ratio, the compression speed, the decompression speed, and the memory usage .



### Diagram Coding

Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes. It is an example of an ad hoc compression algorithm, which means it does not rely on any prior knowledge of the source or the statistical properties of the data.

The basic steps of diagram coding are:

- Find all the symbols and digrams that appear in the source and count their frequencies.
- Sort the symbols and digrams in descending order of frequency.
- Assign codes to the symbols and digrams, starting with the most frequent ones. The codes should be the same length as the symbols, and should not be prefixes of each other. Use the unused codes for the digrams, if any.
- Scan the source from left to right and replace each symbol or digram with its corresponding code. If a digram is not found in the code table, leave it unchanged.

The following diagram illustrates the process of diagram coding for a simple example:

Diagram coding example

The advantages of diagram coding are:

- It is simple and easy to implement.
- It can adapt to different sources and languages without any prior knowledge.
- It can achieve good compression ratios for sources with high digram frequencies.

The disadvantages of diagram coding are:

- It requires two passes over the source, one for building the code table and one for encoding.
- It may not be efficient for sources with low digram frequencies or large alphabets.
- It may not be optimal, as it does not take into account the probabilities of the symbols and digrams.



### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel.
- LZ77 uses a sliding window to find matches between the current data and the previous data, and encodes the matches as pointers to the window.
- LZ78 uses a tree structure to store the dictionary, and encodes the data as indices to the tree nodes.
- LZW uses a hash table to store the dictionary, and encodes the data as codes that correspond to the hash table entries.
- Adaptive dictionary can compress data that is not plain text, such as audio or video data, by building the dictionary based on the source data .
- Adaptive dictionary can also handle data that has varying patterns or frequencies, by updating the dictionary accordingly .
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data, but it may also incur some overheads, such as the size of the dictionary and the complexity of the algorithm .



### The LZ77 Approach

- LZ77 is a lossless data compression algorithm that was published by Abraham Lempel and Jacob Ziv in 1977.
- LZ77 achieves compression by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream.
- LZ77 uses two buffers: a search buffer that contains a portion of the recently encoded sequence, and a look-ahead buffer that contains the next portion of the sequence to be encoded.
- LZ77 encodes each symbol in the look-ahead buffer as either a literal (the symbol itself) or a pointer (a pair of numbers that indicate the length and distance of a matching sequence in the search buffer).
- LZ77 tries to find the longest match between the look-ahead buffer and the search buffer, and encodes it as a pointer if it is longer than a certain threshold, otherwise it encodes it as a literal.
- LZ77 can achieve high compression ratios for data that contains many repeated patterns, such as natural language texts or images.
- LZ77 is the basis for many variations and improvements, such as LZSS, LZMA, DEFLATE, and others.



### The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978.
- It is also known as LZ2 or dictionary-based compression.
- It compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry.
- The dictionary is initialized with all possible single characters as the first entries.
- The algorithm works as follows :
  - Read the next character from the input.
  - If the current token sequence followed by the character is already in the dictionary, append the character to the token sequence and repeat this step.
  - Otherwise, output a pair of the dictionary index of the current token sequence and the character, and add the new token sequence followed by the character to the dictionary with a new index.
  - Reset the token sequence to empty and go back to the first step.
- The output can be encoded using variable-length codes, such as Huffman coding, to reduce the size further.
- LZ78 is the basis for many variations and extensions, such as LZW, LZT, LZMW, and LZAP .
- LZ78 has the advantages of being simple, fast, and adaptive to different types of data.
- However, it also has some drawbacks, such as requiring a large dictionary size, producing long codes for rare sequences, and being sensitive to errors in the input or the output.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some applications for the notes of the Unit 3 - Coding a sequence:

### Applications

- Coding a sequence is a technique that assigns codes to symbols or groups of symbols based on their frequency or probability of occurrence in the source data. This reduces the average length of the codes and hence the number of bits needed to represent the data.
- Coding a sequence can be applied to various types of data, such as text, images, audio, video, etc. Some examples of applications are:

  - Text compression: Coding a sequence can be used to compress text files by assigning shorter codes to more frequent characters or words. For example, Huffman coding is a popular algorithm that uses a binary tree to generate variable-length codes based on the frequencies of the symbols. Another example is arithmetic coding, which assigns codes to symbols based on their cumulative probabilities and uses fractions of bits to encode the data.
  - Image compression: Coding a sequence can be used to compress images by assigning shorter codes to more frequent pixel values or regions. For example, run-length encoding (RLE) is a simple method that encodes consecutive pixels of the same value as a pair of the value and the length of the run. Another example is JPEG, which uses a combination of discrete cosine transform (DCT), quantization, and Huffman coding to compress images.
  - Audio compression: Coding a sequence can be used to compress audio signals by assigning shorter codes to more frequent sound samples or frequency components. For example, pulse-code modulation (PCM) is a method that encodes audio signals as a sequence of binary numbers representing the amplitude of the sound wave. Another example is MP3, which uses a psychoacoustic model to reduce the perceptual redundancy of the audio signal and then applies Huffman coding to compress the data.
  - Video compression: Coding a sequence can be used to compress video frames by assigning shorter codes to more frequent pixel values or motion vectors. For example, intra-frame coding is a method that encodes each frame independently using techniques similar to image compression. Another example is inter-frame coding, which exploits the temporal redundancy between frames and encodes the difference between the current frame and a reference frame using motion estimation and compensation.



### File Compression-UNIX compress

- File compression is a technique to reduce the size of files by removing redundant or unnecessary information.
- UNIX compress is one of the compression utilities available on UNIX systems. It uses the Lempel-Ziv algorithm to compress files and appends a ".Z" extension to the compressed file name.
- The syntax of the compress command is:

  ```
  compress [options] [files]
  ```

- Some of the options are:

  - `-v`: verbose mode, displays the name and percentage reduction for each file compressed
  - `-f`: force compression, overwrites existing compressed files if any
  - `-b n`: specifies the maximum number of bits to use for compression, where n is a number between 9 and 16. The default is 16.

- To decompress a file compressed by compress, use the uncompress command:

  ```
  uncompress [options] [files]
  ```

- Some of the options are:

  - `-v`: verbose mode, displays the name of each file uncompressed
  - `-f`: force decompression, overwrites existing files if any
  - `-c`: writes the uncompressed data to standard output, does not modify the original file

- Example:

  - To compress a file named data.txt and display the percentage reduction, use:

    ```
    compress -v data.txt
    ```

  - To decompress the file data.txt.Z and overwrite the existing data.txt, use:

    ```
    uncompress -f data.txt.Z
    ```

- Advantages of UNIX compress:

  - It is fast and simple to use
  - It is widely available on UNIX systems
  - It can compress any type of file

- Disadvantages of UNIX compress:

  - It does not support multiple files or directories in one command
  - It does not preserve file permissions or ownership
  - It has a limited compression ratio compared to other utilities



### Image Compression

Image compression is the process of reducing the size of an image file without compromising its quality. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, without any loss of information. Lossless compression is suitable for images that require high fidelity, such as medical images, text, and graphics. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 identifies repeated sequences of pixels and replaces them with shorter codes. Huffman coding assigns variable-length codes to the most frequent pixels, reducing the number of bits needed to represent them.
  - Run-length encoding: Run-length encoding is a simple lossless compression technique that reduces the size of an image by encoding sequences of repeated pixels. For example, a sequence of 10 white pixels can be represented as 10W, instead of WWWWWWWWWW. Run-length encoding is effective for images with large areas of uniform color.
  - Arithmetic coding: Arithmetic coding is a lossless compression technique that assigns codes to pixels based on their probabilities of occurrence. Arithmetic coding can achieve higher compression ratios than Huffman coding, but it is more complex and computationally intensive.

- Lossy compression: Lossy compression is a technique that discards some information from the original image, resulting in some loss of quality. Lossy compression is suitable for images that can tolerate some degradation, such as natural images, photographs, and videos. Lossy compression algorithms include:

  - Transform coding: Transform coding is the most commonly used method for lossy compression. It transforms the image from the spatial domain to the frequency domain, and then quantizes and encodes the frequency coefficients. The most widely used transform is the Discrete Cosine Transform (DCT), which decomposes the image into a sum of cosine functions of different frequencies. DCT is the basis of many image compression standards, such as JPEG, MPEG, and H.264 .
  - Wavelet coding: Wavelet coding is a newer method for lossy compression that uses wavelets instead of cosines to transform the image. Wavelets are mathematical functions that can represent both low-frequency and high-frequency components of an image. Wavelet coding can achieve higher compression ratios and better quality than DCT, especially for images with sharp edges and textures. Wavelet coding is the basis of some image compression standards, such as JPEG 2000 and JPEG XR.

Image compression techniques can be evaluated based on several criteria, such as compression ratio, image quality, complexity, and compatibility. Compression ratio is the ratio of the original image size to the compressed image size. Image quality is the measure of how well the compressed image preserves the visual features of the original image. Complexity is the measure of how much computation and memory are required for the compression and decompression processes. Compatibility is the measure of how widely the compression technique is supported by different devices and applications. There is usually a trade-off between these criteria, and the optimal compression technique depends on the specific requirements and constraints of the application.



### The Graphics Interchange Format (GIF)

- GIF stands for Graphics Interchange Format .
- GIF is a raster file format designed for relatively basic images that appear mainly on the internet.
- GIF uses the Lempel-Ziv-Welch (LZW) algorithm to losslessly compress 8-bit indexed color graphics.
- GIF supports up to 256 colors per image, which can be chosen from a 24-bit RGB color space.
- GIF also supports animation and transparency, by using a single color as a transparent background.
- GIF files have the extension .gif and use the MIME type image/gif.
- GIF files can be created, edited and opened using various software tools, such as Adobe Photoshop, GIMP, Paint.NET, etc.
- GIF files are suitable for simple graphics, logos, icons, banners, etc., but not for complex images with many colors or gradients.
- GIF files are widely supported by web browsers and other applications that display images.

: https://www.adobe.com/creativecloud/file-types/image/raster/gif-file.html
: https://en.wikipedia.org/wiki/GIF
: https://simple.wikipedia.org/wiki/Graphics_Interchange_Format
: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types



### Compression over Modems

- Compression over modems is a technique that reduces the amount of data that needs to be transmitted over a phone line or a network by using algorithms that eliminate redundancy and encode information more efficiently .
- Compression over modems can increase the effective data rate and throughput of a communication channel by reducing the transmission time and bandwidth requirements .
- Compression over modems can also improve the reliability and quality of data transmission by reducing the impact of noise and errors on the channel .
- Compression over modems can be performed by hardware or software, depending on the type and capability of the modem and the communication protocol used .
- Compression over modems can be classified into two types: lossless and lossy .
  - Lossless compression preserves the exact information of the original data and allows for perfect reconstruction after decompression. Lossless compression is suitable for text, binary, and executable files .
  - Lossy compression discards some information of the original data and allows for approximate reconstruction after decompression. Lossy compression is suitable for images, audio, and video files, where some quality degradation is acceptable .
- Compression over modems can be implemented by various algorithms and standards, such as V.42bis, MNP5, CSA, and Data Compression AIM  .
  - V.42bis is an international standard for data compression over modems that supports up to 4:1 compression ratio and is compatible with V.42 error correction protocol.
  - MNP5 is a proprietary standard for data compression over modems that supports up to 2:1 compression ratio and is compatible with MNP4 error correction protocol.
  - CSA is a Cisco-specific hardware-assisted compression service that supports up to 4:1 compression ratio and is available for Cisco 7500, 7200, and 7000 series routers.
  - Data Compression AIM is a Cisco-specific hardware module that supports up to 4:1 compression ratio and is available for Cisco 2600 series routers.



### V.42 bits

- V.42 bits are the bits used by the V.42bis standard for data compression procedures for data circuit terminating equipment (DCE) using error correcting procedures.
- V.42bis is a data compression standard adopted by the CCITT (now ITU-T) in 1990, based on the Lempel-Ziv-Welch (LZW) algorithm and some modifications by British Telecom (BT)  .
- V.42bis can compress text data up to 4:1 and binary data up to 2:1, depending on the data characteristics and the compression history  .
- V.42bis operates on a byte-by-byte basis, using a dictionary of 512 to 65536 entries, each containing a variable-length string of bytes  .
- V.42bis uses two modes of operation: transparent mode and compressed mode. In transparent mode, the data is transmitted as is, without compression. In compressed mode, the data is encoded using the dictionary and a variable-length code  .
- V.42bis switches between the two modes dynamically, depending on the compression ratio achieved and the occurrence of control characters or escape sequences  .
- V.42bis also supports a feature called delayed innovation, which allows the encoder to transmit a new dictionary entry before it is actually used, thus saving bits and improving compression  .
- V.42bis can work with any error-correcting DCE that conforms to the V.42 standard, such as V.32, V.32bis, V.34, etc.  .
- V.42bis is widely used by modem manufacturers and is also applied to local and remote area networks (LANs, WANs)  .



### Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, and then encodes the difference between the actual and the predicted symbol or bit. The difference, also called the residual or the error, is usually smaller than the original symbol or bit, and can be compressed more efficiently.

Some examples of predictive coding algorithms are:

- **Linear predictive coding (LPC)**: This is a technique used for speech and audio compression, where the spectral envelope of a signal is represented by a linear combination of previous samples. The coefficients of the linear combination are called the LPC parameters, and they are transmitted along with the residual signal. LPC can achieve high compression ratios and low distortion for speech signals.
- **Dynamic Markov compression (DMC)**: This is a technique that uses a variable-order Markov model to predict the next bit in a binary sequence, and then encodes the bit using arithmetic coding. The Markov model is updated dynamically based on the input sequence, and adapts to different types of data. DMC can achieve high compression ratios for natural language texts and other sources with long-range dependencies. 
- **Predictive coding for images**: This is a technique that exploits the spatial redundancy in images, where neighboring pixels tend to have similar values. The value of each pixel is predicted from its neighboring pixels, and then the difference is encoded using a suitable entropy coder. The prediction can be done using simple methods, such as subtracting the average of the neighboring pixels, or more complex methods, such as using machine learning models. Predictive coding can reduce the size of images significantly, especially for lossless compression.



### Prediction with Partial Match (PPM) for Data Compression

- Prediction by partial matching (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length history of the most recent symbols, called the context, and using it to look up the probability distribution of the next symbol in a table.
- The table is updated dynamically as new symbols are encountered, and the context is adjusted accordingly.
- PPM can achieve high compression ratios by exploiting the redundancy and regularity in natural language and other data sources.
- PPM has several variants, such as PPM-A, PPM-B, PPM-C, PPM-D, PPM-Z, etc., that differ in how they handle the cases when the context is not found in the table or when the predicted symbol is not in the distribution .
- Some of the techniques used to handle these cases are escape symbols, exclusion, interpolation, and zero-frequency estimation .
- PPM is a generalization of the Markov model and the Lempel-Ziv algorithm, and can be seen as a combination of arithmetic coding and context tree weighting  .



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here is the basic algorithm for the notes of the Unit 3 - Coding a sequence:

### The basic algorithm for the notes of the Unit 3 - Coding a sequence

- The goal of coding a sequence is to assign a unique code to each symbol in the sequence, such that the code can be decoded unambiguously and efficiently.
- The code can be either fixed-length or variable-length, depending on whether the code length is the same or different for each symbol.
- Fixed-length codes are simple and easy to implement, but they may not be optimal in terms of compression ratio, especially if the symbols have different probabilities of occurrence.
- Variable-length codes can achieve better compression ratio by assigning shorter codes to more frequent symbols and longer codes to less frequent symbols, but they require more complex encoding and decoding algorithms and data structures.
- A common technique for generating variable-length codes is to use a binary tree, where each leaf node represents a symbol and each internal node represents a prefix of a code. The code for each symbol is obtained by traversing the tree from the root to the leaf and appending a 0 or 1 depending on the left or right branch taken.
- A binary tree that satisfies the prefix property, which means that no code is a prefix of another code, is called a prefix code. Prefix codes are desirable because they can be decoded unambiguously and efficiently by using a lookup table or a trie data structure.
- A prefix code that minimizes the expected code length, which is the weighted sum of the code lengths and the symbol probabilities, is called an optimal prefix code. An optimal prefix code can be constructed by using a greedy algorithm, such as Huffman coding or Shannon-Fano coding, which iteratively merges the two least probable symbols into a new node until only one node remains as the root of the tree.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of the escape symbol for the notes of the unit 3 - coding a sequence in the subject of data compression. Here is the content I have written:

# The Escape Symbol

- In data compression, an escape symbol is a special symbol that is used to indicate that the following data is encoded differently from the usual format.
- An escape symbol can be useful when the data contains rare or unexpected symbols that are not included in the original codebook or dictionary.
- For example, suppose we want to compress a text file using a fixed-length code of 5 bits for each character, and we have a codebook that maps 26 letters (A-Z) to 26 codes (00000-11001). If the text file contains a symbol that is not a letter, such as a space, a comma, or a number, we cannot encode it using the codebook.
- One solution is to use an escape symbol, such as 11111, to signal that the next symbol is encoded using a different scheme, such as ASCII. For example, the text "A1B2" can be encoded as 00000 11111 00110001 00001 11111 00110010, where 00000 and 00001 are the codes for A and B, 11111 is the escape symbol, and 00110001 and 00110010 are the ASCII codes for 1 and 2.
- The advantage of using an escape symbol is that it allows us to compress the data using a smaller codebook that covers the most frequent symbols, and only use a larger codebook for the rare symbols.
- The disadvantage of using an escape symbol is that it increases the length of the encoded data for the rare symbols, and it also introduces the possibility of ambiguity if the escape symbol appears in the original data. For example, if the text file contains the symbol 11111, we need to encode it as 11111 11111 to avoid confusion with the escape symbol.
- To avoid ambiguity, we can use a different escape symbol for each codebook or dictionary, or we can use a variable-length code that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. For example, we can use Huffman coding to compress the text file using a variable-length code that adapts to the frequency of the symbols in the data.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of coding a sequence.

### Coding a sequence

- A sequence is a finite or infinite ordered list of symbols or elements from a given alphabet.
- An example of a sequence is the text of a book, which consists of symbols from the alphabet of a language.
- Coding a sequence is the process of assigning a unique code to each symbol or element of the sequence, such that the original sequence can be reconstructed from the code.
- The code can be represented as a binary string, a sequence of bits (0 or 1), or as a sequence of other symbols from a different alphabet.
- The main goal of coding a sequence is to reduce the length of the code, or the number of bits or symbols needed to represent the sequence, while preserving the information content of the sequence.
- Coding a sequence can be divided into two types: lossless and lossy.
  - Lossless coding preserves the exact information of the original sequence, such that the original sequence can be recovered from the code without any loss or distortion.
  - Lossy coding allows some loss or distortion of the original sequence, such that the code is shorter or more efficient, but the original sequence cannot be recovered exactly from the code.
- An example of lossless coding is Huffman coding, which assigns variable-length codes to the symbols of the sequence based on their frequencies, such that the most frequent symbols have the shortest codes and the least frequent symbols have the longest codes.
- An example of lossy coding is JPEG compression, which reduces the size of an image by discarding some of the less important details, such as high-frequency components, and using a fixed-length code to represent the remaining details.



### The Exclusion Principle

- The exclusion principle is a technique for coding a sequence of symbols by using a prefix code that avoids certain patterns in the codewords.
- The idea is to exclude some codewords from the prefix code, either because they are inefficient or because they have some undesirable property.
- For example, one can exclude codewords that end with a 0, or codewords that contain two consecutive 1s, or codewords that are palindromes (the same backwards and forwards).
- The exclusion principle can reduce the average codeword length or improve the error detection or correction capabilities of the code.
- To apply the exclusion principle, one needs to find a way to assign codewords to symbols in such a way that the excluded codewords are not used, and the remaining codewords are used optimally.
- One method is to use a binary tree to generate the codewords, and prune the branches that lead to the excluded codewords. Another method is to use a modified Huffman algorithm that avoids the excluded codewords.
- The exclusion principle can be generalized to exclude any set of codewords that satisfy some condition, such as having a certain Hamming weight or a certain run length. The exclusion principle can also be applied to codes that are not binary, such as ternary or quaternary codes.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of the Burrows-Wheeler Transform for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression.

### The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is a reversible transformation that rearranges the characters of a string in a way that makes it more compressible.
- The BWT is based on the idea of sorting all the cyclic rotations of the string in lexicographic order and taking the last column of the sorted matrix as the output.
- The BWT can be computed in linear time using a suffix array, which is an array of the starting positions of the sorted suffixes of the string.
- The BWT can be inverted by using the first and last columns of the sorted matrix, which can be reconstructed from the output and the original string length.
- The BWT can be combined with other compression techniques, such as move-to-front encoding and arithmetic coding, to achieve high compression ratios.
- The BWT has applications in data compression, bioinformatics, and cryptography.



### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but rearranges the data to make it more suitable for entropy encoding techniques of compression  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is updated dynamically as the data is processed. The list is initially sorted in some order, such as lexicographic or frequency-based. 
- For each symbol in the input data, the algorithm outputs the index of that symbol in the list, and then moves that symbol to the front of the list. This way, the symbols that occur frequently in the data will have smaller indices and will be closer to the front of the list, making them easier to encode with variable-length codes  .
- Movetofront coding is an invertible transformation, meaning that the original data can be recovered from the transformed data and the initial list. The decoding algorithm simply reverses the steps of the encoding algorithm: it maintains the same list of symbols, reads the indices from the transformed data, outputs the corresponding symbols from the list, and moves them to the front of the list  .
- Movetofront coding is often used as a preprocessing step in data compression algorithms, such as Burrows–Wheeler transform, arithmetic coding, and Huffman coding. It can improve the compression ratio by reducing the entropy of the data and exploiting the local correlations and repetitions in the data .
- Movetofront coding is a fast and simple algorithm that can be implemented efficiently. It does not require any prior knowledge of the data or its statistics. It can adapt to the changes in the data distribution over time. It can also handle any type of data, such as text, images, audio, or video .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on CALIC for the Unit 3 - Coding a sequence in the subject of Data Compression:

### CALIC
- CALIC stands for **Context-Based, Adaptive, Lossless Image Coding** .
- It is an image codec that is made for obtaining a **high degree of compression** for continuous-tone gray-scaled images .
- It uses a **single pass** and **self-correcting GAP (gradient adjusted predictor)** to compress image efficiently and with a high compression ratio .
- It puts heavy emphasis on **image data modeling**  .
- It uses a **large number of modeling contexts** to condition a **non-linear predictor** and make it adaptive to varying source statistics  .
- The non-linear predictor adapts via an **error feedback mechanism**.
- It also uses a **binary arithmetic coder** to encode the prediction residuals  .
- It obtains higher lossless compression of continuous-tone images than other techniques reported in the literature  .
- It has relatively low time and space complexities  .




### JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- It is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- It consists of two independent and distinct stages: modeling and encoding  .
- The modeling stage predicts the value of each pixel based on its context (neighboring pixels) and computes the prediction error  .
- The encoding stage maps the prediction error to a symbol and encodes it using a Golomb-Rice code  .
- JPEG-LS has several advantages over other lossless compression methods, such as:
  - It is simple and efficient, requiring low computational complexity and memory  .
  - It adapts to local image characteristics, achieving high compression ratios for natural images  .
  - It supports progressive and interlaced coding, as well as region-of-interest coding.
  - It is robust to transmission errors and allows random access to the compressed data.
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), defining the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), containing the extensions.



### Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of resolution or detail to represent or process data, such as images, vectors, or fluids.
- The main advantages of multi-resolution approaches are:
  - They can improve the performance and accuracy of data compression by capturing the essential features of the data at different scales.
  - They can reduce the computational complexity and memory requirements of data compression by allowing algorithms to work on both fine and coarse scales, rather than processing all the data at the same level of resolution.
  - They can adapt to the data characteristics and user preferences by allowing the selection of the appropriate level of resolution for different regions or applications.
- The main challenges of multi-resolution approaches are:
  - They require efficient and robust methods to construct and manipulate the multi-resolution representations of the data, such as wavelets, fractals, or grids.
  - They require effective and flexible methods to determine the optimal level of resolution for each region or application, such as visual lossless distance, error indicators, or user feedback.
  - They require careful and consistent methods to handle the transitions and interactions between different levels of resolution, such as filtering, interpolation, or coupling.
- Some examples of multi-resolution approaches for data compression are:
  - Multi-resolution vector data compression, which uses a grid-based method to partition the vector data into different levels of resolution and compresses each level using binary offset and grid filtering.
  - Multi-resolution image compression, which uses a combination of wavelet and fractal transforms to compress the image at different scales and reduce the blocking artifacts and image blurring of conventional fractal algorithms.
  - Multi-resolution fluid simulation, which uses a wavelet-based method to adaptively refine and coarsen the computational grid according to the local features of the fluid and a sharp interface model to track the interface between different phases.



### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding reduces the amount of data needed to represent a binary image (black and white) by exploiting the spatial redundancy in the image .
- Facsimile encoding uses two types of codes: run-length codes and Huffman codes .
- Run-length codes encode the length of consecutive runs of black or white pixels in a scan line . For example, the sequence 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 can be encoded as 64W, where W stands for white and 64 is the run length.
- Huffman codes assign variable-length codes to the run-length codes based on their frequency of occurrence . For example, the most frequent run-length codes can be assigned the shortest codes, such as 0 or 1, while the less frequent ones can be assigned longer codes, such as 1010 or 11011.
- Facsimile encoding can achieve high compression ratios for images that have large areas of uniform color or low complexity . For example, a typical text document can be compressed by a factor of 20 or more using facsimile encoding.
- Facsimile encoding can also be adapted to different transmission rates and channel conditions by using different sets of Huffman codes or modifying the run-length codes. For example, a lower transmission rate may require shorter run-length codes to avoid errors, while a higher transmission rate may allow longer run-length codes to achieve better compression.



### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1 .
- The model is initialized with a single root node, and new nodes are created and added to the tree as new contexts are encountered in the input .
- Each node stores a count of how many times each bit has followed the context, and these counts are used to estimate the conditional probabilities of the next bit given the context .
- The arithmetic coder uses these probabilities to encode or decode each bit of the input, and updates the model accordingly .
- DMC is an adaptive algorithm, meaning that it adjusts to the changing characteristics of the input data as it processes it .
- DMC can achieve high compression ratios for various types of data, especially those with regular patterns or long-range dependencies .
- DMC is also relatively simple and fast, compared to other adaptive arithmetic coding algorithms .
- However, DMC has some limitations, such as the memory requirement for storing the model, the lack of a termination criterion for the coding process, and the sensitivity to noise or errors in the input .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of Unit 4 - Distortion criteria.

## Unit 4 - Distortion criteria

- Distortion criteria are the measures of how well a communication system preserves the quality and intelligibility of the transmitted signal.
- Distortion criteria can be classified into two categories: linear and nonlinear.
- Linear distortion criteria are based on the assumption that the communication system is linear, meaning that the output signal is proportional to the input signal and that the system does not introduce any new frequency components.
- Nonlinear distortion criteria are based on the assumption that the communication system is nonlinear, meaning that the output signal is not proportional to the input signal and that the system may introduce new frequency components, such as harmonics and intermodulation products.
- Some examples of linear distortion criteria are:
  - Bandwidth: the range of frequencies that the system can transmit without significant attenuation or distortion.
  - Group delay: the time difference between the arrival of different frequency components of the signal at the output of the system.
  - Phase distortion: the difference in phase angle between the input and output signals at different frequencies.
  - Amplitude distortion: the difference in amplitude between the input and output signals at different frequencies.
- Some examples of nonlinear distortion criteria are:
  - Signal-to-noise ratio (SNR): the ratio of the power of the signal to the power of the noise at the output of the system.
  - Signal-to-distortion ratio (SDR): the ratio of the power of the signal to the power of the distortion at the output of the system.
  - Total harmonic distortion (THD): the ratio of the power of the harmonics to the power of the fundamental frequency at the output of the system.
  - Intermodulation distortion (IMD): the ratio of the power of the intermodulation products to the power of the signal at the output of the system.
- Different distortion criteria may be more or less important depending on the type and purpose of the communication system and the nature of the signal. For example, bandwidth and group delay are more important for digital signals, while SNR and THD are more important for analog signals.



Hello, I am Sydney, your AI assistant. I can help you with your topic of interest. Here are some notes on the models for the distortion criteria in data compression.

### Models for the distortion criteria in data compression

- Distortion criteria are used to measure how close an approximation is to its original data.
- Distortion criteria depend on the type and quality of the data, the compression method, and the application requirements.
- Some common distortion criteria are:

  - Mean squared error (MSE): The average of the squared differences between the original and the reconstructed data. It is widely used for lossy compression of numerical data, such as images and audio. It is defined as:

    ```
    MSE = (1/N) * sum((x_i - y_i)^2)
    ```

    where N is the number of data points, x_i is the original data point, and y_i is the reconstructed data point.

  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible signal power to the noise power. It is often used to measure the quality of compressed images and video. It is defined as:

    ```
    PSNR = 10 * log10((MAX^2) / MSE)
    ```

    where MAX is the maximum possible value of the data, and MSE is the mean squared error.

  - Structural similarity index (SSIM): A perceptual metric that compares the structural, luminance, and contrast features of the original and the reconstructed data. It is designed to capture the human visual system's response to image quality. It is defined as:

    ```
    SSIM = (2 * mu_x * mu_y + c1) * (2 * sigma_xy + c2) / ((mu_x^2 + mu_y^2 + c1) * (sigma_x^2 + sigma_y^2 + c2))
    ```

    where mu_x and mu_y are the mean values of the original and the reconstructed data, sigma_x and sigma_y are the standard deviations of the original and the reconstructed data, sigma_xy is the covariance of the original and the reconstructed data, and c1 and c2 are small constants to avoid division by zero.

  - Bit error rate (BER): The ratio of the number of incorrect bits to the total number of transmitted bits. It is used to measure the performance of lossless compression of binary data, such as text and code. It is defined as:

    ```
    BER = (number of incorrect bits) / (total number of bits)
    ```

- Rate-distortion theory is a branch of information theory that studies the trade-off between the compression rate and the distortion of the data. It defines the rate-distortion function as the minimum achievable compression rate for a given distortion level. It also provides an iterative algorithm to calculate the rate-distortion function for any source and distortion measure.



### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization can be used for lossy data compression, where the quantized signal can be encoded using fewer bits than the original signal.
- Scalar quantization can be classified into two types: uniform and nonuniform .
  - Uniform scalar quantization divides the signal range into equal-sized intervals, and assigns a quantization level to the midpoint of each interval .
  - Nonuniform scalar quantization divides the signal range into unequal-sized intervals, and assigns a quantization level to each interval according to some criterion, such as minimizing the distortion or maximizing the entropy .
- Scalar quantization can be further divided into two categories: midtread and midrise .
  - Midtread scalar quantization has a quantization level at zero, and the intervals are symmetric around zero .
  - Midrise scalar quantization has no quantization level at zero, and the intervals are shifted by half an interval width from zero .
- Scalar quantization can be optimized by using different techniques, such as Lloyd-Max algorithm, companding, and dead-zone quantization .
  - Lloyd-Max algorithm is an iterative method that finds the optimal quantization levels and intervals for a given probability density function of the signal .
  - Companding is a technique that applies a nonlinear transformation to the signal before quantization, and then applies the inverse transformation after quantization, to achieve a nonuniform quantization with a uniform quantizer .
  - Dead-zone quantization is a technique that introduces a gap around zero, where the signal is quantized to zero, to reduce the bit rate and the distortion for signals with high zero probability .
- Scalar quantization can be applied to different types of signals, such as images, audio, and video .
  - For images, scalar quantization can be used to reduce the number of bits per pixel, by quantizing the pixel values or the coefficients of some transform, such as discrete cosine transform (DCT) or wavelet transform .
  - For audio, scalar quantization can be used to reduce the number of bits per sample, by quantizing the amplitude or the frequency of the sound wave.
  - For video, scalar quantization can be used to reduce the number of bits per frame, by quantizing the pixel values or the motion vectors of the video sequence.



### The Quantization problem

- Quantization is a process of reducing the number of distinct values in a data stream, such as an image or a sound signal, by mapping a range of values to a single discrete value.
- Quantization is a lossy compression technique, meaning that some information is lost in the process and cannot be recovered exactly.
- The quantization problem is to find the optimal way of quantizing a given data stream, such that the distortion (the difference between the original and the quantized data) is minimized and the compression ratio (the ratio of the original and the quantized data sizes) is maximized.
- The quantization problem can be formulated as an optimization problem, where the objective function is the distortion measure and the constraints are the number of quantization levels and the bit rate.
- The quantization problem can be solved in different ways, depending on the type and the dimensionality of the data, the distortion measure, and the quantization scheme.
- Some of the common types of quantization are:
  - Uniform quantization: The range of values is divided into equal-sized intervals, and each interval is assigned a single quantization level. This is the simplest and most widely used quantization method, but it may not be optimal for data that is not uniformly distributed.
  - Non-uniform quantization: The range of values is divided into unequal-sized intervals, and each interval is assigned a single quantization level. This allows for more flexibility and adaptability to the data distribution, but it requires more information to specify the intervals and the levels.
  - Scalar quantization: The data is quantized one value at a time, independently of the other values. This is the easiest and most efficient quantization method, but it may not exploit the correlation or the structure of the data.
  - Vector quantization: The data is quantized in groups of values, called vectors, that are treated as a single entity. This can capture the correlation or the structure of the data, but it requires more computation and storage.
- Some of the common distortion measures are:
  - Mean squared error (MSE): The average of the squared differences between the original and the quantized values. This is the most widely used distortion measure, but it may not reflect the perceptual quality of the data.
  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible value and the MSE, expressed in decibels (dB). This is a common measure of the quality of image or sound compression, but it may not correlate well with the human perception of quality.
  - Structural similarity index (SSIM): A measure of the similarity between the original and the quantized data, based on the luminance, contrast, and structure of the data. This is a more perceptual distortion measure, but it may not be easy to compute or optimize.
- Some of the common quantization schemes are:
  - Fixed-rate quantization: The bit rate (the number of bits per value) is fixed and predetermined, regardless of the data. This is the simplest and most robust quantization scheme, but it may not be optimal for data that varies in complexity or quality.
  - Variable-rate quantization: The bit rate (the number of bits per value) is variable and depends on the data. This allows for more adaptability and efficiency, but it requires more information to specify the bit rate and the quantization levels.
  - Entropy-coded quantization: The quantization levels are encoded using an entropy coder, such as Huffman coding or arithmetic coding, that assigns shorter codes to more frequent levels and longer codes to less frequent levels. This can reduce the bit rate and the redundancy of the data, but it requires more computation and complexity.



### Uniform Quantizer

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels, and its number of output levels $M$, which is related to the bit rate $R$ by $M = 2^R$.
- A uniform quantizer can be either mid-tread or mid-rise, depending on whether the output levels include zero or not. A mid-tread quantizer has a zero output level and an odd number of output levels, while a mid-rise quantizer has a non-zero output level and an even number of output levels.
- A uniform quantizer can be applied to the feature maps between the encoder and decoder of a deep learning based image compression framework, where the quantized feature maps are further entropy coded to reduce the bit rate.
- A uniform quantizer can achieve optimal performance in the high bit rate regime, where the quantization error is small compared to the input variance and the entropy coding is nearly lossless. In this regime, the distortion-rate function of a uniform quantizer is given by $D(R) \approx \frac{\Delta^2}{12} = \frac{\sigma_x^2}{12 \cdot 2^{2R}}$, where $\sigma_x^2$ is the input variance.
- A uniform quantizer can suffer from poor performance in the low bit rate regime, where the quantization error is large compared to the input variance and the entropy coding is inefficient. In this regime, the distortion-rate function of a uniform quantizer is given by $D(R) \approx \frac{\sigma_x^2}{M} = \frac{\sigma_x^2}{2^R}$, which is far from the optimal performance bound given by the rate-distortion function.



### Adaptive Quantization

- Adaptive quantization is a technique of data compression that adjusts the quantizer parameters according to the characteristics of the input data.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters.
- An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution.
- There are two types of adaptive quantization: forward and backward.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information.
- In backward adaptive quantization, the quantizer parameters are updated based on the feedback from the receiver. The feedback can be the reconstructed signal or the quantization error.
- Adaptive quantization can be applied to different types of data, such as images, audio, video, or synthetic aperture radar (SAR) data   .
- Adaptive quantization can improve the performance of data compression by reducing the distortion and increasing the compression ratio. However, it also introduces some challenges, such as the overhead of side information, the delay of feedback, and the complexity of quantizer design.



### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals or levels.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion or higher signal-to-noise ratio (SNR) than uniform quantization with the same number of bits, by allocating more levels to the regions where the input values are more concentrated.
- Non uniform quantization can be classified into two types: companding and optimal.
  - Companding is a method of applying a nonlinear function to the input signal before quantizing it with a uniform quantizer. The nonlinear function can be either a logarithmic function (such as μ-law or A-law) or a power function (such as square-root or cube-root). Companding reduces the dynamic range of the input signal and makes the quantization levels more closely spaced near the origin and more widely spaced near the extremes.
  - Optimal quantization is a method of designing the quantization levels and decision boundaries to minimize a certain distortion criterion, such as mean squared error (MSE) or entropy. Optimal quantization can be achieved by using the Lloyd-Max algorithm, which iteratively updates the levels and boundaries based on the statistics of the input signal.
- Non uniform quantization can also be generalized to vector quantization, where the input signal is divided into blocks or vectors of samples and each vector is mapped to a code word in a code book. Vector quantization can exploit the correlation among the samples and reduce the redundancy in the representation.
- Non uniform quantization can also be applied to neural network compression, where the weights and activations of a neural network are quantized to reduce the memory and computation costs. Non uniform quantization can be optimized by using the back-propagation of the network gradients or by using nonuniform-to-uniform conversion techniques .



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of similar vectors (such as image blocks or speech frames) by a single representative vector called a codevector.
- Scalar quantization (SQ) is a technique that compresses data by representing each individual sample (such as a pixel or a waveform amplitude) by a discrete value called a codeword.
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ by exploiting the correlation among the samples in a vector. SQ treats each sample independently and ignores the correlation.
  - VQ can reduce the quantization noise and distortion by minimizing the mean squared error (MSE) between the original and the reconstructed vectors. SQ minimizes the MSE between the original and the reconstructed samples, which may not reflect the perceptual quality of the data.
  - VQ can adapt to the statistics and characteristics of the data by using different codebooks for different regions or classes of vectors. SQ uses a fixed quantizer for the entire data, which may not be optimal for all samples.
  - VQ can perform rate-distortion optimization by varying the size and shape of the codevectors according to the desired bit rate and distortion level. SQ has a fixed relationship between the bit rate and the distortion, which may not match the user's requirements.

- An example of VQ and SQ applied to image compression is shown below:

  - The original image is divided into 4x4 blocks of pixels, each of which is a 16-dimensional vector.
  - VQ uses a codebook of 256 codevectors, each of which is also a 16-dimensional vector. Each block is assigned to the nearest codevector in terms of Euclidean distance. The index of the codevector is encoded using 8 bits. The reconstructed image is obtained by replacing each block with its corresponding codevector.
  - SQ uses a uniform quantizer with 256 levels, each of which is a scalar value. Each pixel is assigned to the nearest level in terms of absolute difference. The index of the level is encoded using 8 bits. The reconstructed image is obtained by replacing each pixel with its corresponding level.

  - The original image, the VQ-compressed image, and the SQ-compressed image are shown below:

  ```
  | Original image | VQ-compressed image | SQ-compressed image |
  |:--------------:|:-------------------:|:-------------------:|
  | Original image | VQ-compressed image | SQ-compressed image |
  ```

  - The VQ-compressed image has a higher visual quality than the SQ-compressed image, as it preserves the edges and textures better. The SQ-compressed image has more artifacts and noise, as it introduces more quantization errors. The VQ-compressed image and the SQ-compressed image have the same bit rate of 8 bits per pixel, but the VQ-compressed image has a lower MSE of 18.7 than the SQ-compressed image, which has an MSE of 28.4.



### The Linde-Buzo-Gray Algorithm

- The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook .
- A codebook is a set of representative vectors (called codewords) that can be used to approximate any vector in the input space .
- Vector quantization is a technique to compress data by reducing the number of bits needed to represent each vector .
- The LBG algorithm is similar to the k-means method in data clustering .
- The LBG algorithm works as follows :
  - Start with an initial codebook of size one, which is the centroid of the training set.
  - Split each codeword into two slightly different codewords, doubling the size of the codebook.
  - Assign each vector in the training set to the nearest codeword, forming clusters.
  - Update each codeword by computing the centroid of its cluster, minimizing the distortion.
  - Repeat the last two steps until the distortion converges or a desired codebook size is reached.

### Advantages of Vector Quantization over Scalar Quantization

- Scalar quantization is a technique to compress data by reducing the number of bits needed to represent each scalar value.
- Vector quantization has some advantages over scalar quantization, such as:
  - Higher compression ratio: Vector quantization can exploit the correlation among the components of a vector, while scalar quantization treats each component independently.
  - Lower distortion: Vector quantization can preserve the shape and structure of the input data, while scalar quantization can introduce quantization noise and artifacts.
  - Higher flexibility: Vector quantization can adapt to different types of data and applications, while scalar quantization is limited by the choice of the quantizer.



### Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the final quantization regions.
- The advantage of TSVQ is that it can be represented by a binary tree, which reduces the storage cost, encoding rate, and quantization time compared to a general vector quantizer.
- TSVQ also provides a fast quantization search algorithm, which traverses the tree from the root to the leaf node that best matches the input vector .
- TSVQ can be designed by using a top-down or a bottom-up approach. The top-down approach starts with the root node and splits it into two child nodes by using a splitting criterion, such as the average of the training vectors or the principal component analysis. The bottom-up approach starts with the leaf nodes and merges them into parent nodes by using a merging criterion, such as the minimum distortion or the minimum entropy.
- TSVQ can achieve a good trade-off between distortion and complexity, but it may not be optimal in terms of the rate-distortion performance. TSVQ may also suffer from the curse of dimensionality, which means that the number of nodes in the tree grows exponentially with the dimension of the input vectors.



### Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity and the storage requirements of the quantizer .
- Structured vector quantizers can be classified into two types: tree-structured vector quantizers and lattice vector quantizers.
- Tree-structured vector quantizers (TSVQ) use a hierarchical partition of the input space, such that each node of the tree corresponds to a region and a codeword . The encoding and decoding processes are performed by traversing the tree from the root to a leaf node, which reduces the search complexity from linear to logarithmic in the codebook size.
- Lattice vector quantizers use a regular geometric structure of the codebook, such as a lattice, to generate the codewords algorithmically rather than storing them in a table . The encoding and decoding processes are performed by using fast algorithms that exploit the symmetry and the structure of the lattice.

### Advantages of Vector Quantization over Scalar Quantization

- Vector quantization can achieve better rate-distortion performance than scalar quantization, since it exploits the correlation and the structure of the input vectors .
- Vector quantization can avoid the granular noise and the contouring artifacts that are common in scalar quantization, especially at low bit rates.
- Vector quantization can adapt to the statistics and the characteristics of the input source, by using variable-length codes, variable-rate codes, or variable-dimension codes.

