

## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, audio, and some images that require high fidelity.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for images, video, and some audio that can tolerate some degradation.
- Compression techniques can be further divided into two types: symmetric and asymmetric.
- Symmetric compression techniques use the same algorithm for both compression and decompression. They are faster and simpler, but require the same software or hardware at both ends.
- Asymmetric compression techniques use different algorithms for compression and decompression. They are slower and more complex, but allow more flexibility and compatibility.
- Some examples of compression techniques are:

  - Huffman coding: a lossless symmetric technique that assigns variable-length codes to symbols based on their frequency of occurrence.
  - Run-length encoding: a lossless symmetric technique that replaces repeated symbols with a count and a symbol.
  - Lempel-Ziv-Welch (LZW): a lossless symmetric technique that builds a dictionary of common patterns and replaces them with codes.
  - JPEG: a lossy symmetric technique that applies discrete cosine transform (DCT) and quantization to reduce the size of images.
  - MPEG: a lossy symmetric technique that applies DCT, quantization, and motion estimation to reduce the size of video and audio.
  - MP3: a lossy symmetric technique that applies psychoacoustic modeling and Huffman coding to reduce the size of audio.
  - ZIP: a lossless asymmetric technique that combines different algorithms such as LZW, Huffman coding, and deflate to compress files.
  - GZIP: a lossless asymmetric technique that uses deflate algorithm to compress files.
  - BZIP2: a lossless asymmetric technique that uses Burrows-Wheeler transform and Huffman coding to compress files.



# Lossless Compression

Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information. Lossless compression is possible because most real-world data exhibits statistical redundancy, which means that some data elements or patterns are repeated more often than others and can be encoded more efficiently.

Some examples of lossless compression are:

- Run-length encoding (RLE): This method replaces consecutive identical data elements with a single element and a count of how many times it occurs. For example, the string "AAAAABBBBCCCC" can be compressed as "5A4B4C".
- Huffman coding: This method assigns variable-length codes to data elements based on their frequencies of occurrence. The most frequent elements are assigned the shortest codes, and the least frequent elements are assigned the longest codes. For example, if the letter "e" occurs more often than the letter "z" in a text file, it will be assigned a shorter code than "z".
- Lempel-Ziv-Welch (LZW) algorithm: This method builds a dictionary of data elements and their codes as it processes the data. The dictionary is initialized with the basic symbols of the data, and then new symbols are added as combinations of existing symbols. For example, if the data contains the word "compression", the dictionary will start with the letters "c", "o", "m", "p", "r", "e", "s", "i", "n" and their codes, and then add the symbols "co", "om", "mp", "pr", "re", "es", "si", "in", "on" and their codes as they are encountered in the data.

Lossless compression is useful for applications that require exact preservation of the original data, such as text, audio, or image files. Lossless compression can achieve compression ratios of up to 50% for text files and up to 20% for audio or image files. However, lossless compression cannot compress data beyond its entropy, which is a measure of the minimum amount of information needed to represent the data. Therefore, lossless compression is not suitable for data that has high entropy or low redundancy, such as encrypted or random data.



# Lossy Compression

- Lossy compression is a data compression method that sacrifices some information to achieve an even smaller file size than lossless compression.
- Lossy compression is often used on video, audio, and many types of image files.
- Lossy compression uses inexact approximations and partial data discarding to represent the content.
- Lossy compression reduces data size for storing, handling, and transmitting content.
- Lossy compression removes background data and approximates certain details of an image file.
- Lossy compression results in permanent data loss.
- Lossy compression does not decompress back to 100% original quality.
- Lossy compression examples are JPEG, MP3, MPEG, etc.



# Measures of performance for compression techniques

Compression techniques are methods to reduce the size of data by eliminating redundancy or transforming the data into a more compact representation. Compression techniques can improve the efficiency of data storage, transmission, and processing. However, compression techniques also introduce some trade-offs, such as loss of information, increased complexity, and reduced performance. Therefore, it is important to measure the performance of compression techniques and compare them with the original data.

There are different measures of performance for compression techniques, depending on the type of data, the compression algorithm, and the application requirements. Some of the common measures of performance are:

- **Compression ratio (CR)**: This is the ratio of the size of the original data to the size of the compressed data. It indicates how much the data has been reduced by compression. A higher compression ratio means a higher compression efficiency. CR is defined as:

CR = (original size) / (compressed size)

- **Compression factor (CF)**: This is the inverse of the compression ratio. It indicates how many times the original data can fit into the compressed data. A lower compression factor means a higher compression efficiency. CF is defined as:

CF = (compressed size) / (original size)

- **Bits per character (bpc)**: This is the average number of bits used to represent each character in the compressed data. It indicates how compact the compressed data is. A lower bits per character means a higher compression efficiency. bpc is defined as:

bpc = (compressed size) / (number of characters)

- **Bits per pixel (bpp)**: This is the average number of bits used to represent each pixel in the compressed image. It indicates how compact the compressed image is. A lower bits per pixel means a higher compression efficiency. bpp is defined as:

bpp = (compressed size) / (number of pixels)

- **Mean squared error (MSE)**: This is the average of the squared differences between the original data and the decompressed data. It indicates how much the data has been distorted by compression. A lower mean squared error means a higher compression quality. MSE is defined as:

MSE = (1 / N) * sum((original data - decompressed data)^2)

- **Root mean squared error (RMSE)**: This is the square root of the mean squared error. It indicates how much the data has been distorted by compression. A lower root mean squared error means a higher compression quality. RMSE is defined as:

RMSE = sqrt(MSE)

- **Peak signal-to-noise ratio (PSNR)**: This is the ratio of the maximum possible value of the original data to the root mean squared error. It indicates how much the data has been distorted by compression relative to the original data. A higher peak signal-to-noise ratio means a higher compression quality. PSNR is defined as:

PSNR = 10 * log10((max value)^2 / RMSE)

- **Structural similarity index (SSIM)**: This is a measure of the similarity between the original image and the decompressed image based on the luminance, contrast, and structure of the images. It indicates how much the image has been distorted by compression perceptually. A higher structural similarity index means a higher compression quality. SSIM is defined as:

SSIM = (2 * mean(original image) * mean(decompressed image) + c1) * (2 * standard deviation(original image) * standard deviation(decompressed image) + c2) * (covariance(original image, decompressed image) + c3) / ((mean(original image)^2 + mean(decompressed image)^2 + c1) * (standard deviation(original image)^2 + standard deviation(decompressed image)^2 + c2) * (1 + c3))

where c1, c2, and c3 are small constants to avoid division by zero.

- **Multi-scale structural similarity index (MS-SSIM)**: This is an extension of the structural similarity index that considers the similarity between the original image and the decompressed image at different scales or resolutions. It indicates how much the image has been distorted by compression perceptually across different levels of detail. A higher multi-scale structural similarity index means a higher compression quality. MS-SSIM is defined as:

MS-SSIM = product(SSIM(l)^(w(l)))

where l is the scale index, w(l) is the weight for each scale, and SSIM(l) is the structural similarity index at scale l.

- **Percent root



# Modeling and Coding for Data Compression

Data compression is the process of reducing the size of data without losing any essential information. Data compression can be classified into two types: lossless and lossy. Lossless compression preserves the exact original data, while lossy compression discards some information that is deemed less important.

Modeling and coding are the two levels to compress data :

- In the first level, the data will be analyzed for any redundant information and extract it to develop a model. A model is a representation of the data that captures its structure and statistics. For example, a model can be a probability distribution of the symbols in the data, or a dictionary of common patterns in the data.
- In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique. An encoding technique is a method of assigning binary codes to the symbols or patterns in the data, such that the codes are shorter for more frequent or important symbols or patterns, and longer for less frequent or less important ones. For example, an encoding technique can be a Huffman code, an arithmetic code, or a run-length code.

The goal of modeling and coding is to minimize the size of the encoded data, while maintaining the desired quality or fidelity of the original data.

Some examples of modeling and coding techniques for data compression are:

- Statistical modeling and coding: This technique uses the probability of each symbol in the data to assign codes. The symbols with higher probability are assigned shorter codes, and the symbols with lower probability are assigned longer codes. This technique is lossless and can be applied to any type of data. Examples of statistical modeling and coding are Huffman coding, arithmetic coding, and Golomb coding.
- Dictionary-based modeling and coding: This technique uses a dictionary of common patterns or strings in the data to assign codes. The patterns or strings that are in the dictionary are replaced by a single code, and the patterns or strings that are not in the dictionary are encoded as literals. This technique can be lossless or lossy, depending on the size and quality of the dictionary. Examples of dictionary-based modeling and coding are Lempel-Ziv coding, Burrows-Wheeler transform, and JPEG.
- Transform-based modeling and coding: This technique uses a mathematical transform to change the representation of the data from the spatial or temporal domain to the frequency or spectral domain. The transformed data is then quantized and coded. This technique is usually lossy, as some information is lost during the transformation and quantization. Examples of transform-based modeling and coding are discrete cosine transform, wavelet transform, and MPEG.



# Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be reconstructed exactly from the compressed data.
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of information or uncertainty in a data source. The lower the entropy, the more predictable and compressible the data is.
- Entropy can be calculated using different models, such as the zero-order model, the first-order model, the k-th order model, and the universal model. Each model makes different assumptions about the statistical properties of the data source and assigns different probabilities to the symbols or events.
- The entropy of a data source is the lower bound for the average number of bits per symbol required to encode the data. No lossless compression scheme can achieve a compression ratio lower than the entropy of the data source.
- The compression ratio is the ratio of the size of the compressed data to the size of the original data. The higher the compression ratio, the more efficient the compression scheme is.
- The redundancy of a data source is the difference between the entropy and the average number of bits per symbol used by a compression scheme. The lower the redundancy, the more optimal the compression scheme is.
- Lossless compression schemes can be classified into two categories: statistical and dictionary-based. Statistical schemes use the probabilities of the symbols or events to assign variable-length codes, such as Huffman codes or arithmetic codes. Dictionary-based schemes use a predefined or adaptive dictionary to replace common patterns or phrases with shorter codes, such as Lempel-Ziv codes or Burrows-Wheeler transform.



# A brief introduction to information theory

- Information theory is a branch of mathematics that deals with the quantification, transmission, and processing of information.
- Information theory was founded by Claude Shannon in the mid-20th century, who introduced the concepts of entropy, mutual information, channel capacity, and coding schemes.
- Information theory has applications in various fields, such as communication, cryptography, data compression, machine learning, statistics, and biology.
- Information theory is based on probability theory and statistics, where quantified information is usually described in terms of bits, which are the smallest units of information that can be stored or transmitted.
- Information theory often concerns itself with measures of information of the distributions associated with random variables, such as entropy, which is the average amount of information contained in a random variable, or mutual information, which is the amount of information shared between two random variables.
- Information theory also studies the limits and trade-offs of communication systems, such as channel capacity, which is the maximum rate of information that can be reliably transmitted over a noisy channel, or coding schemes, which are methods of encoding and decoding information to achieve efficient and error-free communication.



# Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

Compression techniques are methods to reduce the size of data or models without losing too much information or performance. Compression techniques can be applied to different types of data, such as images, audio, video, text, or neural networks. Compression techniques can be useful for saving storage space, reducing transmission time, or improving efficiency.

There are different models or approaches for compression techniques, depending on the type of data and the desired trade-off between compression ratio and quality. Some of the common models for compression techniques are:

- **Pruning**: Pruning is a technique to remove redundant or unimportant parameters from a model, such as weights, connections, neurons, channels, or layers. Pruning can reduce the size and complexity of a model, while maintaining or even improving its performance. Pruning can be done in different ways, such as magnitude-based pruning, sparsity-based pruning, or structured pruning  .
- **Quantization**: Quantization is a technique to reduce the number of bits required to represent the parameters or activations of a model, such as weights or outputs. Quantization can reduce the memory and computational requirements of a model, while preserving its accuracy. Quantization can be done in different ways, such as uniform quantization, non-uniform quantization, or mixed-precision quantization   .
- **Knowledge distillation**: Knowledge distillation is a technique to transfer the knowledge or performance of a large or complex model (teacher) to a smaller or simpler model (student). Knowledge distillation can reduce the size and inference time of a model, while retaining its functionality. Knowledge distillation can be done in different ways, such as mimicking the outputs, features, or attention of the teacher model by the student model  .
- **Low-rank approximation**: Low-rank approximation is a technique to decompose a large or high-dimensional matrix or tensor into smaller or lower-dimensional matrices or tensors, such as singular value decomposition (SVD) or Tucker decomposition. Low-rank approximation can reduce the number of parameters and operations of a model, while approximating its original behavior. Low-rank approximation can be applied to different layers or components of a model, such as convolutional filters, fully-connected layers, or recurrent units .



# Physical models for data compression

Physical models are mathematical representations of the source data that capture the essential features and statistics of the data. They are used to design efficient compression algorithms that exploit the regularities and redundancies of the data. Some of the common physical models for data compression are:

- **Statistical models**: These models assume that the source data is generated by a random process that follows a certain probability distribution. The goal of statistical models is to estimate the probability of each symbol or sequence of symbols in the data, and use it to assign shorter codes to more probable symbols or sequences. Examples of statistical models are:

  - **Entropy models**: These models measure the average amount of information or uncertainty in the data, and provide a lower bound on the compression ratio that can be achieved by any lossless compression algorithm. The most widely used entropy model is the Shannon entropy, which is defined as the expected value of the logarithm of the inverse probability of each symbol. Other entropy models include the Rényi entropy, the Tsallis entropy, and the Kolmogorov complexity.
  - **Markov models**: These models assume that the probability of the next symbol depends only on the previous k symbols, where k is a fixed parameter. Markov models are particularly useful in text compression, where the probability of the next letter is heavily influenced by the preceding letters. In current text compression, the kth order Markov models are more widely known as finite context models, with the word context being used for what we have earlier defined as state .
  - **Dictionary models**: These models use a predefined or adaptive set of symbols or sequences, called the dictionary, to represent the data. The dictionary can be fixed, such as the ASCII code, or variable, such as the Lempel-Ziv family of algorithms. The goal of dictionary models is to find the longest match between the data and the dictionary, and encode it with a shorter code. Dictionary models are especially effective for compressing data with repeated patterns or phrases.

- **Transform models**: These models transform the source data from one domain to another, where the data can be represented more compactly or sparsely. The goal of transform models is to reduce the correlation or redundancy among the data elements, and concentrate the energy or information in a few coefficients. Examples of transform models are:

  - **Linear transform models**: These models use a linear transformation, such as the discrete Fourier transform (DFT), the discrete cosine transform (DCT), or the wavelet transform, to map the data from the spatial or temporal domain to the frequency or scale domain. Linear transform models are widely used in image and audio compression, where the data can be approximated by a few significant coefficients in the frequency or scale domain, and the rest can be discarded or quantized with lower precision.
  - **Nonlinear transform models**: These models use a nonlinear transformation, such as the fractal transform, the Karhunen-Loève transform (KLT), or the principal component analysis (PCA), to map the data from the original domain to a lower-dimensional or more compact domain. Nonlinear transform models are often used in image and video compression, where the data can be represented by a few parameters or features that capture the essential characteristics of the data, such as the shape, color, or texture.

- **Structural models**: These models exploit the inherent structure or organization of the data, such as the syntax, semantics, or grammar of the data. The goal of structural models is to capture the meaning or context of the data, and use it to compress the data more effectively. Examples of structural models are:

  - **Grammar models**: These models use a set of rules or productions, called the grammar, to generate or parse the data. The grammar can be context-free, such as the Backus-Naur form (BNF), or context-sensitive, such as the attribute grammar. Grammar models are often used in text and natural language compression, where the data can be represented by a parse tree or a derivation sequence that follows the grammar rules.
  - **Semantic models**: These models use a set of concepts or entities, called the ontology, to represent the data. The ontology can be hierarchical, such as the WordNet, or relational, such as the RDF. Semantic models are often used in web and multimedia compression, where the data can be represented by a graph or a network that connects the concepts or entities with their properties and relations.



# Probability models for data compression

- A probability model is a mathematical description of the source of data, which assigns probabilities to different symbols or sequences of symbols that can be generated by the source.
- A probability model can be used to measure the amount of information in the data, and to design efficient compression algorithms that exploit the statistical properties of the data.
- There are different types of probability models, depending on the assumptions made about the source and the data. Some common models are:

  - Uniform model: This model assumes that all symbols in the alphabet have the same probability of occurrence, and that the symbols are independent of each other. This model is simple, but often unrealistic for most data sources.
  - Unigram model: This model assumes that the symbols have different probabilities of occurrence, but that they are independent of each other. This model can capture the frequency distribution of the symbols, but not the correlations or dependencies between them.
  - Markov model: This model assumes that the probability of a symbol depends on the previous k symbols, where k is a fixed parameter. This model can capture the local dependencies or context of the symbols, but not the long-range dependencies or structure of the data.
  - Context tree model: This model assumes that the probability of a symbol depends on a variable-length context, which is determined by a tree structure. This model can adapt to the varying complexity and structure of the data, and can achieve optimal compression for stationary and ergodic sources.
  - Probabilistic grammar model: This model assumes that the data is generated by a probabilistic grammar, which defines the rules and probabilities for producing valid strings. This model can capture the syntax and semantics of the data, and can compress structured or natural language data effectively.



# Markov models for data compression

- A Markov model is a mathematical model that describes a system that changes its state according to some probabilistic rules. A Markov model can be used to model the statistical properties of a source of data, such as a text, an image, or a speech signal.
- A Markov model assumes that the current state of the system depends only on a finite number of previous states, and not on the entire history of the system. This is known as the Markov property or the Markov assumption.
- A Markov model can be represented by a directed graph, where the nodes are the possible states of the system, and the edges are labeled with the transition probabilities between the states. For example, the following graph shows a Markov model of a coin toss, where the states are H (heads) and T (tails), and the transition probabilities are 0.5 for each edge.

Markov model of a coin toss

- A Markov model can be used for data compression by predicting the next symbol in a sequence of data based on the current and previous symbols. The prediction can be encoded using a variable-length code, such as arithmetic coding, that assigns shorter codes to more probable symbols and longer codes to less probable symbols. The better the prediction, the higher the compression ratio.
- A Markov model can be static or dynamic. A static Markov model is fixed and does not change during the compression process. A dynamic Markov model is adaptive and updates its transition probabilities based on the observed data. A dynamic Markov model can adapt to changes in the data source and achieve better compression for non-stationary data.
- A Markov model can have different orders, depending on how many previous symbols are used to predict the next symbol. A zero-order Markov model does not use any previous symbols and predicts the next symbol based on a fixed probability distribution. A first-order Markov model uses the last symbol to predict the next symbol. A second-order Markov model uses the last two symbols to predict the next symbol, and so on. A higher-order Markov model can capture more complex dependencies in the data, but also requires more memory and computation to store and update the transition probabilities.
- A Markov model can also be generalized to a hidden Markov model (HMM), where the states of the system are not directly observable, but only the output symbols that are emitted by the states. A hidden Markov model can be used to model data that have some underlying structure or pattern that is not apparent from the observed symbols, such as speech or handwriting recognition. A hidden Markov model can be trained using algorithms such as the Baum-Welch algorithm or the Viterbi algorithm to estimate the transition and emission probabilities from the observed data.



# Composite Source Model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them with some probability.
- A composite source model can be represented as a number of individual sources S<sub>i</sub>, each with its own model M<sub>i</sub> and a switch that selects a source S<sub>i</sub> with probability P<sub>i</sub> .
- A composite source model is useful for data compression when a single model is not adequate to capture the characteristics of the data .
- A composite source model can reduce the source modeling entropy, which is the lower bound of the compression ratio, by exploiting the correlations and dependencies among the data .
- A composite source model can be applied to various types of data, such as images, text, audio, video, etc.  .
- A composite source model can be combined with different coding techniques, such as Huffman coding, arithmetic coding, run-length coding, etc. to achieve efficient compression .
- A composite source model can be designed based on the statistical analysis of the data, the domain knowledge of the data, or the user preferences .
- A composite source model can be adaptive, meaning that it can change the parameters of the sources and the switch based on the data .
- A composite source model can be hierarchical, meaning that it can have multiple levels of sources and switches .
- A composite source model can be generalized to a composite channel model, which describes the transmission of data over a noisy channel using multiple simpler channels and a switch .



# Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can reduce the storage space or transmission bandwidth required for a given piece of information.
- Data compression can be either lossless or lossy.
  - Lossless compression preserves the exact information of the original data, and can be reversed by decompression.
  - Lossy compression discards some information of the original data, and cannot be reversed by decompression.
- Data compression can be performed by using various techniques, such as :
  - Replacing repeated characters or patterns with shorter sequences or tokens (e.g., Lempel–Ziv algorithm).
  - Introducing pointers or references to a string of bits that the compression program has become familiar with (e.g., Huffman coding).
  - Removing redundant characters or information that are not essential for the data quality (e.g., JPEG compression).
  - Applying mathematical transformations to the data to reduce its complexity or dimensionality (e.g., Fourier transform).
- Data compression can be influenced by several factors, such as:
  - The compression level, which determines how much the data is reduced in size.
  - The compression type, which determines whether the data is lossless or lossy.
  - The coprocessor, which can speed up the compression or decompression process by offloading the workload from the main processor.
  - The data deduplication, which can eliminate duplicate data blocks or files before compression.
  - The multi-stage compression, which can apply different compression techniques in sequence to achieve higher compression ratios.



# Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also called instantaneous codes.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln and code symbols from an alphabet of size D, the following inequality holds:

  ![Kraft inequality](https://wikimedia.org/api/rest_v1/media/math/render/svg/8f1f0b6c9f1f0f0c0f9d9b6f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f



# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images and MP3 for music.
- Prefix codes can be derived from various algorithms, such as Huffman coding, arithmetic coding, Lempel-Ziv coding, etc.
- A universal code is a special kind of prefix code that can encode any positive integer with a near-optimal expected length, regardless of the probability distribution of the integers.
- Examples of universal codes are Elias gamma code, Elias delta code, Fibonacci code, Golomb code, etc.



## Unit 2 - The Huffman coding algorithm

- The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols.
- The algorithm starts by creating a node for each symbol and assigning it a frequency equal to its occurrence in the data. Then, it repeatedly merges the two nodes with the lowest frequencies into a new node, whose frequency is the sum of the two merged nodes. The process continues until there is only one node left, which is the root of the tree.
- The code for each symbol is obtained by traversing the tree from the root to the leaf node corresponding to that symbol, and appending a 0 or a 1 depending on whether the left or the right branch is taken at each node. The codes are prefix-free, meaning that no code is a prefix of another code.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible codes for a given set of symbols and frequencies. It also minimizes the average code length, which is the weighted sum of the code lengths for each symbol, where the weights are the frequencies of the symbols.
- The Huffman coding algorithm can be used to compress any type of data, such as text, images, audio, or video. It is especially effective for data that have a skewed distribution of symbols, where some symbols are much more frequent than others.



# Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The goal of Huffman coding is to minimize the expected code length, which is the weighted average of the code lengths of all symbols.
- The expected code length is also called the **redundancy** of the code, which measures how much extra bits are used compared to the entropy of the source.
- The **variance** of the code is the difference between the maximum and minimum code lengths. It measures how much the code lengths vary among different symbols.
- A **minimum variance Huffman code** is a Huffman code that has the smallest possible variance among all Huffman codes with the same expected code length.
- A minimum variance Huffman code can be constructed by using a modified version of Huffman's algorithm, which assigns codes to symbols in pairs instead of individually.
- The advantage of a minimum variance Huffman code is that it reduces the worst-case decoding time, which depends on the maximum code length.
- The disadvantage of a minimum variance Huffman code is that it may increase the average decoding time, which depends on the distribution of the symbols.
- A minimum variance Huffman code is also called a **length-limited Huffman code**, if there is an additional constraint that the code lengths must not exceed a given constant.
- A length-limited Huffman code can be useful for applications that require fixed-size buffers or have limited memory.
- A length-limited Huffman code can be constructed by using a modified version of Huffman's algorithm, which uses a priority queue to select the symbols with the smallest code lengths first.



# Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted. This allows one-pass encoding and adaptation to changing conditions in data.

## Basic idea

The basic idea of adaptive Huffman coding is to maintain a binary tree that represents the code for each symbol. The tree is initialized with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet. As each symbol is encountered, the tree is updated as follows:

- If the symbol is new, it is added as a child of the NYT node, and the NYT node is split into two nodes: a new NYT node and a node for the new symbol. The new symbol node is assigned a weight of 1, and the new NYT node inherits the weight of the old NYT node. The code for the new symbol is the code for the old NYT node followed by a binary representation of the symbol (e.g., using a fixed-length code or an escape code).
- If the symbol is already in the tree, its weight is incremented by 1, and the tree is restructured to preserve the Huffman property: the weight of any node is equal to the sum of the weights of its children, and the nodes with lower weights are closer to the root than the nodes with higher weights. This may involve swapping nodes or rotating subtrees.

The code for any symbol is the path from the root to the symbol node, where a left branch is 0 and a right branch is 1. The code is transmitted or stored along with the symbol.

## Example

Suppose we want to encode the string "ABRACADABRA" using adaptive Huffman coding. We start with an empty tree with only the NYT node:

```
  NYT
```

The first symbol is A, which is new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the A node and the new NYT node. The code for A is the code for the old NYT node (empty) followed by a binary representation of A (e.g., 00001).

```
     1
   /   \
NYT     A
 1       1
```

The second symbol is B, which is also new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the B node and the new NYT node. The code for B is the code for the old NYT node (0) followed by a binary representation of B (e.g., 00010).

```
     2
   /   \
  1     A
 / \     1
NYT B
 1  1
```

The third symbol is R, which is also new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the R node and the new NYT node. The code for R is the code for the old NYT node (00) followed by a binary representation of R (e.g., 01010).

```
       3
     /   \
    2     A
   / \     1
  1   R
 / \   1
NYT B
 1  1
```

The fourth symbol is A, which is already in the tree, so we increment its weight by 1 and restructure the tree to preserve the Huffman property. This involves swapping the A node with the R node, since they have the same weight and A is more recent. The code for A is the path from the root to the A node (10).

```
       4
     /   \
    2     A
   / \     2
  1   A
 / \   1
NYT B
 1  1
```

The fifth symbol is C, which is new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the C node and the new NYT node. The code for C is the code for the old NYT node (000) followed by a binary representation of



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression:

# Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the data.
- The algorithm works as follows:
  - Create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and the sum of their frequencies as the frequency.
    - Add the new node to the queue.
  - The remaining node is the root of the Huffman tree.
  - Traverse the tree and assign codes to each symbol by appending 0 for left branch and 1 for right branch.
- The Huffman coding algorithm has the following properties:
  - It is optimal, meaning that it produces the shortest possible code for a given set of symbols and frequencies.
  - It is prefix-free, meaning that no code is a prefix of another code.
  - It is unique, meaning that there is only one way to construct the Huffman tree for a given set of symbols and frequencies.
- To update the notes of the Unit 2, you need to do the following steps:
  - Review the definition and the algorithm of the Huffman coding technique and make sure you understand how it works and why it is optimal, prefix-free and unique.
  - Practice some examples of applying the Huffman coding algorithm to different sets of symbols and frequencies and verify the correctness and optimality of the codes.
  - Learn how to encode and decode data using the Huffman codes and how to store and transmit the Huffman tree along with the data.
  - Compare the Huffman coding technique with other lossless data compression techniques, such as run-length encoding, arithmetic coding and Lempel-Ziv coding, and analyze their advantages and disadvantages.
  - Test your knowledge and skills by solving some exercises and problems related to the Huffman coding technique and its applications.



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



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

# Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the source data.
- The Huffman code is a prefix code, which means that no code is a prefix of another code. This property ensures that the code is uniquely decodable.
- The decoding procedure for the Huffman code is the reverse of the encoding procedure. It involves the following steps:

  - Step 1: Construct the Huffman tree from the given code table or frequency table. The Huffman tree is a binary tree that represents the code assignments for each symbol. The root node has no code, and the left and right branches are labeled with 0 and 1 respectively. The leaf nodes contain the symbols and their codes.
  - Step 2: Read the encoded bitstream from left to right, and traverse the Huffman tree from the root node. For each bit, move to the left or right child node according to the bit value. When a leaf node is reached, output the symbol corresponding to that node, and return to the root node. Repeat this process until the end of the bitstream is reached.
  - Step 3: If the bitstream is padded with extra bits to make it a multiple of 8 bits, discard the padding bits before decoding.

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
          /   \
         0     1
        /       \
       B         *
              /   \
             0     1
            /       \
           C         D
```

  - To decode the bitstream 1011011110, we start from the root node and follow the bits:

```
* -> 1 -> * -> 0 -> B (output B and return to root)
* -> 1 -> * -> 1 -> * -> 0 -> C (output C and return to root)
* -> 1 -> * -> 1 -> * -> 1 -> D (output D and return to root)
* -> 0 -> A (output A and return to root)
* -> 1 -> * -> 0 -> B (output B and return to root)
* -> end of bitstream
```

  - The decoded message is BCDA



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on Golomb codes for the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

# Golomb codes

- Golomb codes are a type of prefix codes that are optimal for a geometric distribution of the source symbols.
- Golomb codes are parametric, meaning that they depend on a positive integer parameter m that determines the code length and distribution.
- Golomb codes can be used to compress data that has a Zipf-like distribution, such as natural language text, images, audio, or video.
- Golomb codes have two parts: a unary quotient and a binary remainder.
- The unary quotient is a sequence of q zeros followed by a one, where q is the integer part of n/m, and n is the source symbol to be encoded.
- The binary remainder is the binary representation of r, where r is the remainder of n/m, and has a variable length depending on m.
- The length of the binary remainder is either ⌊log₂m⌋ or ⌈log₂m⌉ bits, depending on whether m is a power of 2 or not.
- If m is a power of 2, then the binary remainder has a fixed length of log₂m bits, and the Golomb code is equivalent to a truncated binary code.
- If m is not a power of 2, then the binary remainder has a variable length, and the Golomb code can be further optimized by using a Rice code, which splits the possible values of r into two subsets of equal size.
- The Rice code assigns ⌊log₂m⌋ bits to the first subset and ⌈log₂m⌉ bits to the second subset, and uses an extra bit to indicate which subset r belongs to.
- The Rice code reduces the expected code length by 1/2 bit per symbol, compared to the Golomb code.
- The optimal value of m for a given source distribution can be calculated by minimizing the expected code length, or by using a heuristic such as m = ⌈-1/log₂(1-p)⌉, where p is the probability of the most frequent symbol.



# Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that are optimal for encoding data with a geometric distribution.
- Rice codes use a parameter k, which is a positive integer, to determine the length and value of the code words.
- To encode a non-negative integer x using Rice codes, the following steps are performed:
  - Divide x by 2^k and write the quotient in unary, i.e., as a sequence of 1s followed by a 0. This is the first part of the code word.
  - Write the remainder of x divided by 2^k in binary, using k bits. This is the second part of the code word.
  - Concatenate the first and second parts to form the final code word.
- For example, if k = 2 and x = 9, then the code word is 11001, because 9 / 4 = 2 (unary: 110), and 9 % 4 = 1 (binary: 01).
- To decode a Rice code, the following steps are performed:
  - Read the unary part of the code word and count the number of 1s. This is the quotient of x divided by 2^k.
  - Read the next k bits of the code word and interpret them as a binary number. This is the remainder of x divided by 2^k.
  - Multiply the quotient by 2^k and add the remainder to obtain x.
- For example, if k = 2 and the code word is 11001, then the quotient is 2 (unary: 110), and the remainder is 1 (binary: 01). Therefore, x = 2 * 4 + 1 = 9.
- Rice codes are simple and efficient to implement, especially when k is a power of 2. They are suitable for encoding data with a high probability of small values and a low probability of large values.
- Rice codes are often used in audio and video compression, where the difference between adjacent samples or pixels tends to follow a geometric distribution. For example, Rice codes are used in FLAC, a lossless audio codec, and JPEG-LS, a lossless image codec.



# Tunstall codes

Tunstall codes are a form of entropy coding used for lossless data compression. They are based on the idea of parsing a stochastic source with codewords of variable length, and then encoding those codewords with fixed-length codes. Tunstall codes have some advantages and disadvantages compared to other entropy coding methods, such as Huffman coding and Lempel-Ziv coding.

## Advantages of Tunstall codes

- Tunstall codes are simple to implement and have low computational complexity.
- Tunstall codes can achieve optimal compression for memoryless sources with rational probabilities, such as geometric distributions.
- Tunstall codes can be easily adapted to changing source statistics by updating the codebook.

## Disadvantages of Tunstall codes

- Tunstall codes require a large codebook size, which increases the storage and transmission overhead.
- Tunstall codes are not universal, meaning they cannot achieve optimal compression for arbitrary sources.
- Tunstall codes are sensitive to errors, as a single bit error can corrupt the entire codeword.

## How to construct Tunstall codes

- Given a source alphabet S and a codebook size N, the goal is to find a set of N codewords C that minimizes the expected codeword length.
- The algorithm starts with a single codeword c0 that represents the entire source alphabet S.
- The algorithm iteratively splits the codeword with the highest probability into |S| new codewords, each appended with a symbol from S.
- The algorithm stops when the codebook size reaches N.
- The algorithm assigns a fixed-length binary code to each codeword in C, such that the most probable codewords have the shortest codes.

## Example of Tunstall codes

- Suppose the source alphabet is S = {a, b, c} with probabilities P(a) = 0.5, P(b) = 0.25, P(c) = 0.25.
- Suppose the codebook size is N = 8.
- The algorithm starts with c0 = S, with P(c0) = 1.
- The algorithm splits c0 into c1 = a, c2 = b, c3 = c, with P(c1) = 0.5, P(c2) = 0.25, P(c3) = 0.25.
- The algorithm splits c1 into c4 = aa, c5 = ab, c6 = ac, with P(c4) = 0.25, P(c5) = 0.125, P(c6) = 0.125.
- The algorithm splits c2 into c7 = ba, c8 = bb, with P(c7) = 0.125, P(c8) = 0.0625.
- The algorithm stops as the codebook size is 8.
- The algorithm assigns the following binary codes:

| Codeword | Probability | Binary code |
|----------|-------------|-------------|
| c4 = aa  | 0.25        | 00          |
| c1 = a   | 0.5         | 01          |
| c2 = b   | 0.25        | 10          |
| c3 = c   | 0.25        | 110         |
| c5 = ab  | 0.125       | 1110        |
| c6 = ac  | 0.125       | 11110       |
| c7 = ba  | 0.125       | 111110      |
| c8 = bb  | 0.0625      | 111111      |

- The expected codeword length is 2.5 bits per symbol, which is optimal for this source.



# Applications of Huffman Coding

Huffman coding is a technique that is used for compressing data to reduce its size without losing any of its details. It is based on the idea of assigning variable-length codes to the data values based on their frequency or weight. The more frequent a data value is, the shorter its code will be. The less frequent a data value is, the longer its code will be. This way, the data can be represented by fewer bits on average, saving space and bandwidth.

Some of the applications of Huffman coding are:

- **Text and fax transmissions**: Huffman coding can be used to compress text and fax data by encoding the characters or symbols based on their frequency in the data. For example, the letter 'e' is more common than the letter 'z' in English, so it will have a shorter code than 'z'. This can reduce the size of the text or fax data by up to 50% .
- **Conventional compression formats**: Huffman coding is used by many popular compression formats like GZIP, BZIP2, PKZIP, etc. to compress various types of data, such as text, images, audio, video, etc. These formats usually combine Huffman coding with other techniques, such as run-length encoding, dictionary encoding, arithmetic coding, etc. to achieve higher compression ratios .
- **Multimedia codecs**: Huffman coding is also used by some multimedia codecs, such as JPEG, PNG, and MP3, to compress the data that is generated by other methods, such as discrete cosine transform, quantization, etc. Huffman coding helps to reduce the redundancy and entropy of the data, making it more compact and efficient .



# Lossless image compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Lossless image compression is the technique that deals with the problem of reducing the amount of data required to represent a digital image without losing any information.
- Lossless image compression is achieved by removal of one or three basic data redundancies: (1) coding redundancy, (2) spatial redundancy, (3) irrelevant information.
- Coding redundancy is the excess of bits used to encode the data. Spatial redundancy is the correlation between neighboring pixels in an image. Irrelevant information is the data that is not essential for the intended use of the image.
- Huffman coding is a particular type of optimal prefix code that is commonly used for lossless data compression. Prefix code means that the code assigned to one character is not a prefix of code assigned to any other character.
- The idea of Huffman coding is to assign variable-length codes to input characters, lengths of assign codes are based on the frequencies of corresponding characters. The most frequent occurring character gets the smallest input code and the most occurring character gets the largest code.
- Huffman coding can be applied to image compression by treating each pixel value as a character and constructing a Huffman tree based on the pixel frequencies. The Huffman tree is a binary tree that assigns a code to each pixel value by traversing the tree from the root to the leaf. The code is formed by appending a 0 for a left branch and a 1 for a right branch.
- The compressed image is obtained by replacing each pixel value with its corresponding Huffman code. The decompressed image is obtained by reversing the process, using the Huffman tree to decode each bit sequence into a pixel value.
- Huffman coding is a lossless compression technique, meaning that the original and decompressed images are identical. It has applications in fields where it is important that the original and decompressed data be identical, like in zip file format and is often used as a component within lossy data compression techniques like mp3 encoder and other lossy audio encoder.
- Huffman coding is also the base of JPEG image compression, which is a lossy compression technique that uses Huffman coding along with other methods like discrete cosine transform and quantization. JPEG image compression can achieve higher compression ratios than Huffman coding alone, but at the cost of some loss of quality.
- Huffman coding is an efficient and simple algorithm for lossless image compression, but it has some limitations. For example, it requires the knowledge of the pixel frequencies before encoding, which may not be available or may change over time. It also assumes that the pixel values are independent of each other, which may not be true for natural images that have spatial correlations. Moreover, it may not be optimal for some types of data that have non-uniform distributions or long-range dependencies.
- To overcome these limitations, some improvements and variations of Huffman coding have been proposed, such as adaptive Huffman coding, arithmetic coding, JPEG 2000, JPEG-LS, and 7-Zip lossless compression  . These methods aim to achieve better compression ratios, faster encoding and decoding, and higher adaptability to different types of data  .



# Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized  .
- Huffman coding consists of two steps: building a Huffman tree and generating codes for each character .
- To build a Huffman tree, we need to follow these steps  :
  - Create a leaf node for each character and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and the sum of their frequencies as the frequency.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
- To generate codes for each character, we need to traverse the Huffman tree and assign 0 or 1 to each edge  .
  - The code for a character is the concatenation of the edge labels along the path from the root to the leaf node representing that character.
  - The codes are prefix-free, meaning that no code is a prefix of another code .
- To compress a text file, we need to replace each character with its corresponding code and store the Huffman tree along with the encoded data  .
- To decompress a text file, we need to use the Huffman tree to decode the encoded data by following the edge labels from the root to the leaf nodes  .



# Audio Compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Audio compression is the process of reducing the size of an audio file by removing or encoding redundant or irrelevant information.
- Audio compression can be lossless or lossy, depending on whether the original data can be perfectly reconstructed or not.
- Lossless audio compression techniques preserve the exact quality and information of the original audio signal, but achieve a lower compression ratio than lossy techniques.
- Lossy audio compression techniques discard some information from the original audio signal, but achieve a higher compression ratio than lossless techniques.
- Huffman coding is a lossless audio compression technique that assigns variable-length codes to the symbols in the audio data, based on their frequencies of occurrence.
- Huffman coding works by creating a binary tree that represents the symbols and their frequencies, where the most frequent symbols are assigned the shortest codes and the least frequent symbols are assigned the longest codes.
- Huffman coding is optimal for a given set of symbols and frequencies, meaning that no other lossless coding scheme can achieve a lower average code length.
- Huffman coding can be static or dynamic, depending on whether the code tree is fixed or updated for each block of data.
- Static Huffman coding uses a predefined code tree that is known to both the encoder and the decoder, and does not change during the compression process.
- Dynamic Huffman coding adapts the code tree to the data as it is processed, and transmits the code tree along with the compressed data.
- Huffman coding is used in many audio compression standards, such as JPEG, MPEG-2, MP3, and FLAC.



## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term of the sequence, usually denoted by a<sub>1</sub>.
  - Define the rule or formula that determines the next term of the sequence, usually denoted by a<sub>n</sub> or a<sub>n+1</sub>.
  - Use a loop or a recursion to generate the terms of the sequence until a certain condition is met, such as reaching a certain number of terms, a certain value, or a certain pattern.
  - Store the terms of the sequence in a data structure, such as an array, a list, or a vector.
  - Display or return the sequence as the output of the code.

- For example, to code the sequence 2, 4, 6, 8, ..., we can use the following Python code:

```python
# Define the first term of the sequence
a1 = 2

# Define the rule or formula that determines the next term of the sequence
def next_term(a):
  return a + 2

# Use a loop to generate the terms of the sequence until a certain condition is met
# In this case, we stop when the term is greater than 20
sequence = [] # Create an empty list to store the terms of the sequence
a = a1 # Initialize the current term to the first term
while a <= 20: # Loop until the condition is met
  sequence.append(a) # Add the current term to the list
  a = next_term(a) # Update the current term to the next term

# Display the sequence as the output of the code
print(sequence)
```

- The output of the code is [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].



# Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits.
- Binary code is a way of representing data using only two symbols: 0 and 1.
- Coding a sequence is the task of assigning a unique binary code to each symbol in a given sequence of data.
- The goal of coding a sequence is to minimize the total number of bits required to encode the data, while preserving the information content and allowing for easy decoding.
- There are two types of coding techniques: fixed-length coding and variable-length coding.
- Fixed-length coding assigns the same number of bits to each symbol, regardless of its frequency or probability in the data. For example, using a 3-bit code, we can encode 8 symbols as follows:

| Symbol | Binary code |
|--------|-------------|
| A      | 000         |
| B      | 001         |
| C      | 010         |
| D      | 011         |
| E      | 100         |
| F      | 101         |
| G      | 110         |
| H      | 111         |

- Variable-length coding assigns different numbers of bits to different symbols, depending on their frequency or probability in the data. For example, using a variable-length code, we can encode the same 8 symbols as follows:

| Symbol | Binary code |
|--------|-------------|
| A      | 0           |
| B      | 10          |
| C      | 110         |
| D      | 1110        |
| E      | 11110       |
| F      | 111110      |
| G      | 1111110     |
| H      | 1111111     |

- Variable-length coding can achieve better compression than fixed-length coding, as it assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. However, variable-length coding requires a special property called prefix-free, which means that no code is a prefix of any other code. This ensures that the codes can be uniquely decoded without ambiguity.
- There are different methods to construct variable-length codes, such as Huffman coding, arithmetic coding, and universal coding. These methods use different algorithms to assign optimal codes to the symbols based on their probabilities or frequencies in the data.



# Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using only two symbols, usually 0 and 1. Each symbol is called a bit, and a sequence of bits is called a binary code. Binary coding is used to store and transmit data in computers and other digital devices.
- Huffman coding is a form of lossless compression which makes files smaller using the frequency with which characters appear in a message. Huffman coding assigns variable length binary codes for each input character in the text file. The length of the binary code depends on the frequency of the character in the file. The most frequent characters are coded with the smaller binary words, thus, the size used to code them is minimal, which increases the compression. Huffman coding uses a binary tree to generate the codes for each character.
- Some advantages of Huffman coding over binary coding are:
  - Huffman coding reduces the size of the file by using fewer bits to represent the most frequent characters, while binary coding uses the same number of bits for all characters.
  - Huffman coding is optimal, meaning that no other compression method can achieve a smaller file size for the same input, while binary coding is not optimal, meaning that there may be other compression methods that can achieve a smaller file size for the same input.
  - Huffman coding is adaptive, meaning that it can adjust the codes based on the input data, while binary coding is fixed, meaning that it uses the same codes for all inputs.
- Some disadvantages of Huffman coding over binary coding are:
  - Huffman coding requires extra information to decode the file, such as the frequency table or the binary tree, while binary coding does not require any extra information to decode the file.
  - Huffman coding is more complex to implement and requires more computation time than binary coding, which is simple and fast to implement.



# Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Coding a sequence is the process of assigning a unique code to each symbol in a sequence, such that the code can be used to reconstruct the original sequence without any loss of information.
- Coding a sequence is useful for data compression, which is the reduction of the size of data without affecting its meaning or quality.
- Data compression has many applications in various fields, such as:
  - **Communication**: Data compression can reduce the bandwidth and storage requirements of transmitting and receiving data over networks, such as the Internet, email, or mobile phones. For example, text messages, images, audio, and video can be compressed to save space and time.
  - **Storage**: Data compression can increase the capacity and efficiency of storing data on devices, such as hard disks, flash drives, or memory cards. For example, compressed files, such as ZIP, RAR, or 7Z, can store more data in less space than uncompressed files.
  - **Encryption**: Data compression can enhance the security and privacy of data by making it harder to decipher or tamper with. For example, encrypted files, such as AES, RSA, or PGP, can use compression to reduce the size and complexity of the data before applying encryption algorithms.
  - **Analysis**: Data compression can facilitate the processing and understanding of data by removing redundant or irrelevant information. For example, data mining, machine learning, or natural language processing can use compression to extract meaningful patterns or features from large or noisy data sets.



# Bi-level image compression-The JBIG standard

- Bi-level images are images that have only two possible pixel values, usually black and white.
- Bi-level image compression is the process of reducing the amount of data needed to represent a bi-level image, without losing any information or quality.
- The JBIG standard is an early lossless image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group, standardized as ISO/IEC 11544 and as ITU-T recommendation T.82 in March 1993.
- The JBIG standard is widely implemented in fax machines, and can also be used on other bi-level images.
- The JBIG standard offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement.
- The JBIG standard uses a combination of arithmetic coding and adaptive template matching to achieve high compression ratios.
- The JBIG standard consists of three main components: the encoder, the decoder, and the arithmetic coder.
- The encoder divides the input image into stripes of 128 rows each, and processes each stripe independently.
- The encoder uses four modes to encode each stripe: typical prediction, generic region, symbol region, and refinement region.
- The typical prediction mode uses a fixed template to predict the value of each pixel based on its neighboring pixels, and encodes the prediction error using arithmetic coding.
- The generic region mode encodes a region of pixels that does not contain any symbols or halftones, using a variable template that adapts to the local image characteristics.
- The symbol region mode encodes a region of pixels that contains symbols or halftones, using a dictionary of symbols that is built dynamically during the encoding process.
- The refinement region mode encodes a region of pixels that is similar to a previously encoded region, using a refinement template that improves the quality of the reconstructed image.
- The decoder performs the inverse operations of the encoder, using the same arithmetic coder and the same modes to decode each stripe.
- The arithmetic coder is a binary adaptive arithmetic coder that assigns probabilities to each symbol based on the previous symbols and the context.
- The arithmetic coder uses a table of 4096 contexts, each of which has two probability estimates, one for the symbol 0 and one for the symbol 1.
- The arithmetic coder updates the probability estimates after each symbol is encoded or decoded, using a simple adaptation algorithm.
- The arithmetic coder also uses a bypass mode to encode or decode symbols with equal probabilities, without updating the probability estimates.



# JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group .
- Bi-level images are images that have only two possible values for each pixel, such as black and white.
- JBIG2 is suitable for both lossless and lossy compression .
- Lossless compression means that the original image can be perfectly reconstructed from the compressed data, while lossy compression means that some information is discarded and the reconstructed image may have some degradation.
- JBIG2 can achieve higher compression ratios than existing standards, such as Fax Group 4, MMR, and JBIG1, by using pattern matching and substitution techniques in addition to the technologies of the existing standards.
- Pattern matching and substitution techniques involve identifying and encoding recurring patterns in the image, such as characters, symbols, or halftone dots, and replacing them with references to a dictionary of patterns .
- JBIG2 can segment an image into overlapping and/or non-overlapping regions of text, halftone, and generic content, and apply compression techniques that are specially optimized for each type of content .
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- JBIG2 is widely used for compressing scanned documents, such as PDF files, and has applications in fax, printing, and archiving .



# Image compression

Image compression is a type of data compression applied to digital images, to reduce their cost for storage or transmission. Algorithms may take advantage of visual perception and the statistical properties of image data to provide superior results compared with generic data compression methods which are used for other digital data.

## Types of image compression

There are two main types of image compression: lossless and lossy.

- Lossless compression preserves the original image data exactly, without any loss of quality or information. Lossless compression is suitable for images that require high fidelity, such as medical images, scientific images, or art images. Lossless compression algorithms include PNG, GIF, TIFF, BMP, and WebP .
- Lossy compression reduces the image data by discarding some information that is deemed less important or less noticeable by human vision. Lossy compression can achieve higher compression ratios than lossless compression, but at the cost of some degradation of image quality. Lossy compression is suitable for images that can tolerate some distortion, such as photographs, web images, or video frames. Lossy compression algorithms include JPEG, JPEG 2000, HEIF, and BPG .

## Methods of image compression

There are various methods of image compression, depending on the type of image data and the desired compression ratio and quality. Some of the common methods are:

- Run-length encoding (RLE): This method encodes the consecutive pixels of the same color or intensity as a single value and a count, instead of repeating the same value. For example, a sequence of 10 white pixels can be encoded as (10, 255) instead of (255, 255, 255, 255, 255, 255, 255, 255, 255, 255). RLE is a simple and fast method, but it is only effective for images with large areas of uniform color or intensity, such as cartoons or logos.
- Huffman coding: This method assigns variable-length codes to the pixel values based on their frequency of occurrence. The more frequent values are assigned shorter codes, and the less frequent values are assigned longer codes. This reduces the average number of bits per pixel. For example, if the value 255 occurs 80% of the time, it can be assigned a code of 0, while the value 0 occurs 10% of the time, it can be assigned a code of 10. Huffman coding is a lossless method that can be applied to any type of image data, but it requires a code table to be stored or transmitted along with the compressed data.
- Lempel-Ziv-Welch (LZW) coding: This method builds a dictionary of variable-length codes for the pixel sequences that occur in the image. The dictionary is initialized with the basic pixel values, and then it is updated with new codes for the longer sequences that are encountered. For example, if the sequence (255, 0, 255) occurs frequently, it can be assigned a new code of 256, and then the sequence (256, 0, 255) can be assigned a new code of 257, and so on. LZW coding is a lossless method that can achieve high compression ratios for images with repetitive patterns, such as text or graphics.
- Discrete cosine transform (DCT): This method transforms the image data from the spatial domain to the frequency domain, by decomposing the image into a sum of cosine functions of different frequencies. The image is divided into small blocks, usually 8x8 pixels, and then each block is transformed by a DCT matrix. The resulting coefficients represent the amount of each frequency component in the block. The coefficients are then quantized, which means they are rounded to a smaller set of values, and then encoded by a Huffman or arithmetic coder. The quantization step introduces some loss of information, but it also reduces the number of bits per coefficient. The quantization level can be adjusted to trade off between compression ratio and image quality. DCT is a lossy method that is widely used for JPEG and MPEG compression, as it exploits the fact that human vision is more sensitive to low-frequency components than high-frequency components .
- Wavelet transform: This method is similar to DCT, but it uses wavelet functions instead of cosine functions to transform the image data. Wavelet functions are more flexible and can adapt to different image features, such as edges, textures, or smooth regions. The image is decomposed into a hierarchy of subbands,



# Dictionary Techniques for Data Compression

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive. A static dictionary is fixed and predefined, while an adaptive dictionary is updated dynamically during the compression and decompression processes.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries. This reduces the redundancy and the size of the data.
- Some examples of dictionary techniques are:

  - Non-adaptive dictionary compression: This technique uses a static dictionary that is known to both the encoder and the decoder. The encoder scans the input text and replaces each string with its corresponding code in the dictionary. The decoder reverses the process by looking up the codes in the dictionary and reconstructing the original text.
  - LZ77 algorithms: This technique uses an adaptive dictionary that consists of a sliding window that contains the most recent part of the input text. The encoder searches for the longest match between the current string and the previous strings in the window. If a match is found, the encoder outputs a triple of <length, offset, next symbol>, where length is the length of the match, offset is the distance from the current position to the match, and next symbol is the symbol following the match. If no match is found, the encoder outputs a single symbol. The decoder maintains a similar sliding window and reconstructs the text by copying the matches or appending the symbols.
  - LZ78 algorithms: This technique uses an adaptive dictionary that consists of a tree that stores all the strings that have been encountered so far. The encoder scans the input text and outputs the index of the longest match in the tree, followed by the symbol that extends the match. The encoder then adds the new string to the tree as a child node of the match. The decoder maintains a similar tree and reconstructs the text by traversing the tree and appending the symbols.
  - LZW algorithm: This technique is a variation of LZ78 that uses a hash table instead of a tree to store the dictionary. The encoder and the decoder use the same hash function to map the strings to the indices. The encoder scans the input text and outputs the index of the longest match in the hash table, followed by the symbol that extends the match. The encoder then adds the new string to the hash table with the next available index. The decoder maintains a similar hash table and reconstructs the text by looking up the indices and appending the symbols.

- Dictionary techniques are widely used in data compression because they can achieve high compression ratios and fast compression and decompression speeds. They are especially suitable for compressing natural language texts, which have a lot of repetition and redundancy. Some applications of dictionary techniques are:

  - ZIP file format: This is a popular file format that uses a combination of LZ77 and Huffman coding to compress files. The LZ77 algorithm reduces the redundancy by finding matches in the sliding window, and the Huffman coding further reduces the size by assigning variable-length codes to the symbols based on their frequencies.
  - GIF image format: This is a popular image format that uses the LZW algorithm to compress images. The LZW algorithm reduces the size by finding matches in the hash table and outputting the indices. The LZW algorithm can also handle variable-width codes, which allows it to adapt to different color depths and image sizes.
  - Deflate algorithm: This is a widely used algorithm that combines LZ77 and Huffman coding to compress data streams. The Deflate algorithm is used in many protocols and formats, such as HTTP, PNG, PDF, and SSH.



# Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, Huffman coding, arithmetic coding, run-length encoding, dictionary-based encoding, etc.
- Coding a sequence is one of the fundamental tasks in data compression, where a given sequence of symbols (such as characters, bits, pixels, etc.) is transformed into another sequence of symbols that is shorter or more efficient to store or transmit.
- Coding a sequence can be classified into two types: lossless and lossy.
  - Lossless coding preserves the exact information of the original sequence, and allows the original sequence to be reconstructed from the coded sequence without any errors or distortion.
  - Lossy coding discards some information of the original sequence, and allows the original sequence to be approximated from the coded sequence with some acceptable errors or distortion.
- Coding a sequence can also be classified into two modes: fixed-length and variable-length.
  - Fixed-length coding assigns a fixed number of bits or symbols to each symbol in the original sequence, regardless of its frequency or probability of occurrence.
  - Variable-length coding assigns a variable number of bits or symbols to each symbol in the original sequence, depending on its frequency or probability of occurrence, such that more frequent or probable symbols are assigned shorter codes and less frequent or probable symbols are assigned longer codes.
- Coding a sequence can be further classified into two methods: source coding and channel coding.
  - Source coding is the process of reducing the redundancy or inefficiency of the original sequence, by exploiting the statistical properties or patterns of the source data, such as frequency, probability, correlation, etc.
  - Channel coding is the process of adding redundancy or robustness to the coded sequence, by exploiting the characteristics or constraints of the communication channel, such as bandwidth, noise, error, etc.



# Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression is fast and simple, but it may not be optimal for data that has a different or unknown distribution than the dictionary .
- Static dictionary compression can be implemented by using a priming text, a hashing function, or a trie data structure .
- A priming text is a known text that is compressed along with the input data, but only the compressed input data is transmitted. The receiver can use the priming text to reconstruct the dictionary and decompress the data.
- A hashing function is a function that maps phrases or symbols to codes, such that the codes are unique and have a fixed length. The dictionary can be stored as a hash table, where the codes are the keys and the phrases or symbols are the values.
- A trie is a tree data structure that stores phrases or symbols as paths from the root to the leaves. Each node in the trie has a code that is appended to the code of its parent. The dictionary can be stored as a trie, where the codes are the paths and the phrases or symbols are the leaves.



# Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a method of data compression that encodes a sequence of symbols using a variable-length code based on a tree structure.
- The tree structure is built from the bottom up, starting with the most frequent symbols as leaves and assigning them shorter codes, and then combining them into higher-level nodes with longer codes.
- The tree structure is also known as a Huffman tree, after its inventor David Huffman, who proposed the algorithm in 1952.
- The algorithm works as follows:
  - Given a sequence of symbols and their frequencies, create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue, do the following:
    - Remove the two nodes with the lowest frequency from the queue and create a new internal node with these two nodes as children. The frequency of the new node is the sum of the frequencies of the children.
    - Assign a bit (0 or 1) to each edge of the tree, such that the left edge is 0 and the right edge is 1. The bit assigned to an edge is also the bit appended to the code of the child node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the tree and has no code.
  - To encode a symbol, traverse the tree from the root to the leaf corresponding to the symbol and concatenate the bits along the path. The code for each symbol is the reverse of the concatenation.
  - To decode a code, traverse the tree from the root to a leaf, using the bits of the code to determine the direction of the traversal. The symbol corresponding to the leaf is the decoded symbol.

- An example of diagram coding is shown below:

| Symbol | Frequency |
|--------|-----------|
| A      | 0.4       |
| B      | 0.3       |
| C      | 0.2       |
| D      | 0.1       |

- The Huffman tree for this sequence is:

```
    1.0
   /   \
  /     \
 0.6     0.4
/  \      |
A   0.2   B
   /  \
  C    D
```

- The codes for each symbol are:

| Symbol | Code |
|--------|------|
| A      | 0    |
| B      | 11   |
| C      | 100  |
| D      | 101  |

- The average code length for this sequence is:

```
0.4 * 1 + 0.3 * 2 + 0.2 * 3 + 0.1 * 3 = 1.9 bits/symbol
```

- The compression ratio for this sequence is:

```
Original size / Compressed size = 2 bits/symbol / 1.9 bits/symbol = 1.05
```

- Diagram coding is optimal in the sense that it minimizes the average code length for a given sequence of symbols and their frequencies.
- Diagram coding is also prefix-free, meaning that no code is a prefix of another code, which makes decoding unambiguous and efficient.



# Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes.
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios than static dictionary methods.
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, LZW, etc.
- Adaptive dictionary algorithms typically consist of the following steps:
  - Initialize the dictionary with some predefined symbols or codes.
  - Read a symbol or a sequence of symbols from the input data.
  - Search the dictionary for a matching entry. If found, output the corresponding code and update the dictionary with a new entry that combines the previous and current symbols or sequences. If not found, output the symbol or sequence as it is and add it to the dictionary as a new entry.
  - Repeat until the end of the input data is reached.
- Adaptive dictionary algorithms have some advantages and disadvantages, such as:
  - Advantages:
    - They can handle any type of data, not just plain text.
    - They can achieve high compression ratios for data with repetitive patterns or structures.
    - They do not require prior knowledge of the data or a fixed dictionary size.
  - Disadvantages:
    - They may require more memory and processing time to maintain and search the dictionary.
    - They may suffer from dictionary overflow or degradation if the dictionary becomes too large or contains too many obsolete entries.
    - They may not be compatible with other compression algorithms or standards.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the LZ77 approach for coding a sequence in data compression:

# The LZ77 Approach

- LZ77 is a **lossless data compression algorithm** published by Abraham Lempel and Jacob Ziv in 1977  .
- It is a **dictionary coder** and maintains a **sliding window** during compression  .
- The sliding window consists of two parts: a **search buffer** and a **look-ahead buffer**  .
- The search buffer contains the previously encoded data, and the look-ahead buffer contains the data to be encoded  .
- The algorithm searches for the longest match between the look-ahead buffer and the search buffer, and encodes it as a **triplet** of the form (offset, length, next symbol)  .
- The offset is the distance from the current position to the start of the match in the search buffer, the length is the number of symbols in the match, and the next symbol is the symbol following the match in the look-ahead buffer  .
- If no match is found, the algorithm encodes the next symbol in the look-ahead buffer as a triplet of the form (0, 0, symbol)  .
- The algorithm then slides the window by the length of the match plus one, and repeats the process until the end of the input data  .
- The output of the algorithm is a sequence of triplets that can be decoded by reversing the process  .
- The LZ77 algorithm can achieve high compression ratios by exploiting the redundancy and repetition in the input data   .
- The performance of the algorithm depends on the size of the sliding window and the search method used to find the matches   .
- The algorithm can be improved by using various techniques such as hashing, binary trees, suffix trees, or suffix arrays to speed up the search process .
- The algorithm can also be modified by using different encoding schemes for the triplets, such as variable-length codes, Huffman codes, or arithmetic codes.
- The LZ77 algorithm is the basis for many variations and extensions, such as LZSS, LZMA, DEFLATE, gzip, and ZIP.



# The LZ78 Approach

LZ78 is a lossless data compression algorithm that was proposed by Abraham Lempel and Jacob Ziv in 1978. It is based on the idea of building a dictionary of phrases from the input data, and replacing repeated occurrences of the phrases with references to the dictionary entries. The algorithm works as follows:

- Initialize an empty dictionary.
- Read the next symbol from the input.
- If the symbol is not in the dictionary, output the symbol and add it to the dictionary as a new entry with a unique index.
- If the symbol is in the dictionary, read the next symbol and form a pair with the previous symbol.
- If the pair is not in the dictionary, output the index of the previous symbol and the current symbol, and add the pair to the dictionary as a new entry with a unique index.
- If the pair is in the dictionary, repeat the previous step until a pair is not found or the input is exhausted.
- Output the index of the last pair found in the dictionary.

## Example

Suppose we want to compress the following string using LZ78:

`abracadabra`

The algorithm would produce the following output:

| Symbol | Pair | Output | Dictionary |
|--------|------|--------|------------|
| a      | N/A  | a      | {1: a}     |
| b      | N/A  | b      | {1: a, 2: b} |
| r      | N/A  | r      | {1: a, 2: b, 3: r} |
| a      | (b, a) | 2a     | {1: a, 2: b, 3: r, 4: ba} |
| c      | N/A  | c      | {1: a, 2: b, 3: r, 4: ba, 5: c} |
| a      | (d, a) | 4a     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da} |
| b      | (r, a) | 3a     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra} |
| r      | (a, b) | 1b     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra, 8: ab} |
| a      | N/A  | 1      | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra, 8: ab} |

The final compressed string is:

`abr2ac4a3a1b1`

## Advantages and Disadvantages

LZ78 has some advantages and disadvantages compared to other compression algorithms. Some of them are:

- It does not require a sliding window or a look-ahead buffer, which simplifies the implementation and reduces the memory usage.
- It can adapt to different types of data and does not need a predefined dictionary or a fixed code length.
- It can achieve high compression ratios for data with long repetitions or regular patterns.
- It can suffer from dictionary overflow, which means that the dictionary can grow too large and exceed the available memory or the maximum index size.
- It can produce long codes for rare or single symbols, which can reduce the compression ratio or even increase the size of the output.
- It can be slow to encode and decode, especially for large dictionaries, as it requires searching and updating the dictionary for every symbol or pair.



# Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation. It can reduce the storage space and transmission time of data. 
- Coding a sequence is a technique of data compression that assigns codes to sequences of bytes or symbols, rather than individual ones. It can exploit the repetition and correlation in the data to achieve higher compression ratios.  
- Some applications of coding a sequence are:

  - **LZW (Lempel–Ziv–Welch) compression**: This is a lossless compression algorithm that uses a dictionary of codes to represent sequences of bytes. It is widely used in GIF images, Unix compress, and ZIP files.  
  - **Huffman coding**: This is a lossless compression algorithm that uses variable-length codes to represent symbols based on their frequencies. It is optimal for compressing data with known or fixed probabilities. It is used in JPEG images, MP3 audio, and DEFLATE compression. 
  - **Arithmetic coding**: This is a lossless compression algorithm that uses fractional codes to represent symbols based on their probabilities. It can achieve higher compression ratios than Huffman coding, but it is more complex and slower. It is used in JPEG 2000 images, Bzip2 files, and H.264 video. 
  - **Sequence statistical code**: This is a lossless compression algorithm that uses SDC and FOST codes to represent sequences of bytes based on their statistics. It is designed to improve the energy efficiency of wireless sensors. 
  - **Delta encoding**: This is a lossless compression algorithm that encodes the difference between successive values, rather than the values themselves. It can reduce the redundancy in data with small variations. It is used in incremental backups, network protocols, and video coding.



# File Compression-UNIX compress

- File compression is the process of reducing the size of a file by encoding its data more efficiently.
- File compression can save disk space, bandwidth, and transmission time.
- UNIX compress is one of the file compression utilities available on UNIX systems.
- UNIX compress uses the Lempel-Ziv algorithm to compress files, which is a lossless data compression technique.
- UNIX compress adds a .Z extension to the compressed file name and preserves the original file name and time stamp.
- UNIX compress can compress only one file at a time. To compress multiple files or directories, one can use the tar command to create an archive and then compress it with UNIX compress.
- UNIX compress can achieve a compression ratio of about 2:1 on average, depending on the type and content of the file.
- UNIX compress is compatible with the gzip utility, which is another file compression utility on UNIX systems. gzip can decompress files compressed by UNIX compress, and vice versa.
- To compress a file with UNIX compress, one can use the following syntax:

  `compress [options] filename`

  where options can be:

  - `-v`: verbose mode, displays the name and percentage reduction for each file compressed
  - `-f`: force compression, overwrites existing compressed files without prompting
  - `-b n`: specifies the maximum number of bits to use for compression, where n can be between 9 and 16, with the default being 16
  - `-c`: writes the output to the standard output, does not modify the original file

- To decompress a file with UNIX compress, one can use the following syntax:

  `uncompress [options] filename`

  where options can be:

  - `-v`: verbose mode, displays the name and percentage reduction for each file decompressed
  - `-f`: force decompression, overwrites existing uncompressed files without prompting
  - `-c`: writes the output to the standard output, does not modify the original file

- Alternatively, one can use the gzip command with the `-d` option to decompress files compressed by UNIX compress, and the compress command with the `-d` option to decompress files compressed by gzip.

- Examples of using UNIX compress:

  - To compress a file named data.txt and save it as data.txt.Z:

    `compress data.txt`

  - To compress a file named data.txt and write the output to the standard output:

    `compress -c data.txt`

  - To compress a file named data.txt with 12 bits and overwrite the existing compressed file if any:

    `compress -f -b 12 data.txt`

  - To decompress a file named data.txt.Z and save it as data.txt:

    `uncompress data.txt.Z`

  - To decompress a file named data.txt.Z and write the output to the standard output:

    `uncompress -c data.txt.Z`

  - To decompress a file named data.txt.Z with gzip and save it as data.txt:

    `gzip -d data.txt.Z`

  - To decompress a file named data.txt.gz with compress and save it as data.txt:

    `compress -d data.txt.gz`



# Image Compression

Image compression is a process applied to a graphics file to minimize its size in bytes without degrading image quality below an acceptable threshold . By reducing the file size, more images can be stored in a given amount of disk or memory space. Image compression also reduces the bandwidth required for transmitting images over the internet or other networks.

Some of the main concepts and techniques involved in image compression are:

- **Image file types**: Different image file types such as JPG, TIF, and PNG use different algorithms to change how image data is stored and to produce smaller-sized files (measured in bytes). Some image file types are more suitable for certain types of images than others. For example, JPG is good for photographs, while PNG is good for graphics with sharp edges and transparency.
- **Lossy and lossless compression**: Image compression can be either lossy or lossless. Lossy compression reduces the image quality by discarding some information that is not perceptible to the human eye. Lossless compression preserves the image quality by finding patterns and redundancies in the image data and encoding them more efficiently. Lossy compression usually achieves higher compression ratios than lossless compression, but at the cost of some image degradation.
- **Compression ratio**: The compression ratio is the ratio of the original file size to the compressed file size. It indicates how much the file size has been reduced by compression. A higher compression ratio means a smaller file size, but it may also mean lower image quality. The optimal compression ratio depends on the purpose and the type of the image. For example, a high compression ratio may be acceptable for a thumbnail image, but not for a high-resolution print.
- **Visual quality**: The visual quality of an image is the subjective perception of how well the image preserves the details, colors, and contrast of the original image. Visual quality is affected by the compression algorithm, the compression ratio, and the display device. Different compression algorithms may have different effects on the visual quality of an image. For example, some algorithms may introduce artifacts such as blurring, blocking, or ringing. Visual quality can be measured by objective metrics such as peak signal-to-noise ratio (PSNR) or structural similarity index (SSIM), or by subjective ratings from human observers.



# The Graphics Interchange Format (GIF)

- GIF stands for Graphics Interchange Format .
- GIF is a raster file format designed for relatively basic images that appear mainly on the internet.
- GIF uses the Lempel-Ziv-Welch (LZW) algorithm to losslessly compress 8-bit indexed color graphics.
- Each GIF file can support up to 8 bits per pixel and can contain 256 indexed colors.
- GIF can also store multiple images in a single file, which can be animated by displaying them in a sequence .
- GIF is one of the oldest and most widely used image formats on the web, especially for animations and logos.
- GIF has some limitations, such as the fixed color palette, the lack of transparency and the low resolution .
- GIF can be created, edited and opened by various software applications, such as Adobe Photoshop, GIMP, Microsoft Paint, etc .

: https://www.adobe.com/creativecloud/file-types/image/raster/gif-file.html
: https://en.wikipedia.org/wiki/GIF
: https://simple.wikipedia.org/wiki/Graphics_Interchange_Format
: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types



# Compression over Modems

- Compression over modems is a technique that allows modems to transmit data faster and more efficiently over phone lines by reducing the size of the data before sending it and expanding it after receiving it.
- Compression over modems can be done by using different algorithms and protocols that are agreed upon by both the sending and receiving modems. Some of the common protocols are V.42bis, MNP5, and STAC.
- Compression over modems can increase the effective data rate of the modems by a factor of 2 to 4, depending on the type and redundancy of the data. For example, text files can be compressed more than images or audio files.
- Compression over modems can also improve the reliability and quality of the data transmission by reducing the number of bits that need to be sent and received, and by using error correction techniques to detect and correct errors that may occur during the transmission .
- Compression over modems can be implemented by using hardware or software solutions. Hardware solutions are faster and more efficient, but they require special devices or modules that are compatible with the modems. Software solutions are more flexible and adaptable, but they consume more CPU and memory resources of the computers .



# V.42 bits

- V.42 bits are the bits used by the V.42bis standard for data compression in modems.
- V.42bis is a data compression standard adopted by the CCITT (now ITU-T) in 1990.
- V.42bis is based on the Lempel-Ziv-Welch (LZW) algorithm, which uses a dictionary to encode and decode data .
- V.42bis can achieve a compression ratio of up to 4:1 for text data and 2:1 for binary data.
- V.42bis operates on data blocks of 512 bytes and uses a 12-bit code to represent each dictionary entry.
- V.42bis uses a dynamic dictionary that can store up to 2048 entries and can be reset or partially cleared when needed.
- V.42bis also uses a technique called delayed innovation, which allows the encoder to send a code that is not yet in the dictionary, but will be added later.
- V.42bis is compatible with the V.42 error correction standard and can be used on any V-Series modem that supports V.42.
- V.42bis is widely used by modem manufacturers and has applications in local and remote area networks (LANs and WANs) .



# Predictive Coding

Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, and then encodes the difference between the actual and the predicted symbol or bit. The difference is also known as the residual or the error. Predictive coding can achieve higher compression ratios than entropy coding alone, because it exploits the redundancy and correlation in the data.

Some examples of predictive coding algorithms are:

- **Linear predictive coding (LPC)**: This is a technique that uses a linear filter to estimate the next sample of a speech signal based on the previous samples. The filter coefficients are derived from the autocorrelation of the signal. The residual is then quantized and encoded using entropy coding. LPC is widely used in speech compression and analysis.
- **Dynamic Markov compression (DMC)**: This is an algorithm that uses a Markov model to predict the next bit in a binary sequence based on the previous bits. The model is updated dynamically as new bits are processed. The residual is then encoded using arithmetic coding. DMC can achieve high compression ratios for natural language texts and other types of data. 
- **Predictive arithmetic coding**: This is a generalization of arithmetic coding that uses a predictor to estimate the probability distribution of the next symbol in a sequence based on the previous symbols. The predictor can be any function that maps the past symbols to a probability distribution. The residual is then encoded using arithmetic coding. Predictive arithmetic coding can adapt to any type of data and achieve optimal compression ratios.

Some advantages of predictive coding are:

- It can exploit the redundancy and correlation in the data, which entropy coding alone cannot do.
- It can adapt to the characteristics and statistics of the data, which fixed coding schemes cannot do.
- It can achieve near-optimal compression ratios for any type of data, as long as the predictor is accurate and the residual is efficiently encoded.

Some disadvantages of predictive coding are:

- It requires a model or a predictor, which may be complex and computationally expensive to construct and update.
- It may introduce distortion or errors in the decoded data, if the predictor is inaccurate or the residual is poorly encoded.
- It may be sensitive to noise or outliers in the data, which may affect the prediction and the encoding.



# Prediction with Partial Match (PPM) for Data Compression

- Prediction by partial matching (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length history of the most recent symbols, called the context, and using it to look up the probability distribution of the next symbol in a table .
- The table is updated dynamically as new symbols are encountered, and the context is adjusted accordingly .
- PPM can achieve high compression ratios by exploiting the redundancy and regularity in natural language and other data sources .
- PPM has several variants, such as PPM-A, PPM-B, PPM-C, PPM-D, PPM-Z, etc., that differ in how they handle the cases when the context is not found in the table or when the predicted symbol is not in the distribution .
- PPM is a generalization of the Markov model and the arithmetic coding techniques .



# The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by encoding its content in a more efficient way.
- Coding a sequence is one of the techniques used in data compression to represent a sequence of symbols (such as characters, bytes, or pixels) with a shorter code.
- There are different types of coding algorithms, such as fixed-length codes, variable-length codes, and dictionary-based codes.
- Fixed-length codes assign the same number of bits to each symbol, regardless of its frequency or importance. For example, ASCII code uses 8 bits to represent 256 symbols.
- Variable-length codes assign different numbers of bits to different symbols, depending on their frequency or importance. For example, Huffman code uses a binary tree to assign shorter codes to more frequent symbols and longer codes to less frequent symbols.
- Dictionary-based codes use a table or a dictionary to store the codes for common sequences of symbols. For example, LZW code uses codes 256 through 4095 to represent sequences of bytes that have occurred previously in the data.
- The basic algorithm for coding a sequence using a dictionary-based code is as follows:

  - Initialize the dictionary with the codes for the individual symbols (usually 0 to 255 for bytes).
  - Read the first symbol from the input and store it in a buffer.
  - While there are more symbols in the input, do the following:
    - Read the next symbol from the input and append it to the buffer.
    - If the buffer is in the dictionary, continue reading the next symbol.
    - If the buffer is not in the dictionary, do the following:
      - Output the code for the buffer without the last symbol.
      - Add the buffer with the last symbol to the dictionary with a new code.
      - Clear the buffer and store the last symbol in it.
  - Output the code for the buffer.



# The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by removing redundant or irrelevant information, or by using more efficient encoding schemes.
- Coding a sequence is one of the techniques of data compression, which involves assigning a unique code to each symbol in the data, such that the code length reflects the symbol frequency or probability.
- The escape symbol is a special symbol that is used to indicate the occurrence of a new or rare symbol that has not been assigned a code yet, or that has a very low probability of occurrence.
- The escape symbol is usually chosen to be a symbol that does not appear in the original data, or that has a very low frequency in the data.
- The escape symbol is followed by a fixed-length code or a uniform probability code that represents the new or rare symbol, using the symbols that have not occurred or have a low probability of occurrence.
- The escape symbol itself has an artificial count, often a constant throughout the encoding, that determines its code length and probability.
- The use of the escape symbol allows the coding scheme to be adaptive, meaning that it can adjust to the changing statistics of the data, and encode new or rare symbols without having to reassign codes to the existing symbols.
- The use of the escape symbol also allows the coding scheme to be universal, meaning that it can encode any data without knowing the alphabet or the probabilities of the symbols in advance.
- Example: Let T = badada and \u0006 be the escape symbol. Using a simple coding scheme that assigns codes based on the symbol frequency, we can encode T as follows:

| Symbol | Frequency | Code  |
|--------|-----------|-------|
| a      | 3         | 0     |
| b      | 1         | 10    |
| d      | 2         | 11    |
| \u0006 | 1         | 01    |

- The encoded sequence is: 10 0 11 0 01 0 11 0
- The escape symbol is used to indicate the first occurrence of a, which is followed by a uniform probability code 0, using the only symbol that has not occurred yet, a.
- The escape symbol has a frequency of 1, which is the same as b, so it has the same code length as b, 2 bits.



# Unit 3 - Coding a sequence

## Length of context

- The length of context is the number of symbols that are used to predict the next symbol in a sequence.
- The length of context affects the performance of compression algorithms, such as arithmetic coding and Lempel-Ziv coding.
- A longer context can capture more patterns and correlations in the data, leading to higher compression ratios.
- However, a longer context also requires more memory and computation to store and process the probabilities of each possible symbol given the context.
- Therefore, there is a trade-off between the length of context and the complexity of the compression algorithm.
- The optimal length of context depends on the characteristics of the data and the compression objective. For example, natural language texts may benefit from longer contexts that capture word and phrase frequencies, while images may require shorter contexts that capture pixel intensities and edges.
- A common way to determine the length of context is to use adaptive methods that adjust the context based on the data. For example, Lempel-Ziv coding uses a variable-length context that grows as new symbols are encountered, while arithmetic coding can use a sliding window that moves along the sequence.



# The Exclusion Principle

- The exclusion principle is a technique used in data compression algorithms that rely on context modeling and prediction, such as PPMC .
- The idea is to exclude symbols that have already been seen in a higher-order context from the probability computation of a lower-order context, thus avoiding double-counting and improving compression efficiency .
- For example, suppose we have a text file that contains the word "compression" several times, and we want to encode the last letter "n" using a PPMC algorithm with a maximum context order of 2.
- The algorithm would first look at the previous two symbols, which are "io", and check if "n" has occurred after "io" before. If yes, it would assign a high probability to "n" and a low probability to an escape symbol, which indicates that the symbol is not in the current context.
- If no, it would use the escape symbol and move to a lower-order context, which is the previous symbol "o". However, it would exclude "n" from the probability computation of "o", because "n" has already been seen after "io", and including it again would overestimate its probability. Instead, it would assign probabilities to other symbols that have occurred after "o" before, and another escape symbol.
- This process would continue until either the symbol is found in a context, or the zero-order context is reached, which assigns equal probabilities to all symbols.
- The exclusion principle helps to avoid wasting bits on symbols that are unlikely to occur in a given context, and to focus on symbols that are more relevant and informative. It also reduces the number of escape symbols needed, which saves space and improves compression ratio .



# The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm that rearranges a string of characters into runs of similar characters. This is useful for data compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding .

The BWT is based on a reversible permutation of the characters of a string, which is obtained by sorting all the cyclic rotations of the string lexicographically and taking the last column of the sorted matrix  .

For example, the BWT of the string "banana" is obtained as follows:

1. Append a special symbol, such as "$", to the end of the string to mark the end of the string and to ensure that the symbol is lexicographically smaller than any other character in the string. The string becomes "banana$".
2. Generate all the cyclic rotations of the string by shifting the characters one by one to the left and wrapping around the last character to the beginning. The cyclic rotations are:

```
banana$
anana$b
nana$ba
ana$ban
na$bana
a$banan
$banana
```

3. Sort the cyclic rotations lexicographically (alphabetically) and form a matrix with each rotation as a row. The sorted matrix is:

```
$banana
a$banan
ana$ban
anana$b
banana$
na$bana
nana$ba
```

4. Take the last column of the matrix as the BWT of the string. The last column is "annb$aa", which is the BWT of "banana$".

The BWT can be reversed by using the fact that the first column of the sorted matrix is the same as the sorted BWT, and that each character in the BWT corresponds to a unique character in the first column by following the same cyclic order .

For example, to reverse the BWT of "annb$aa", we can do the following:

1. Sort the BWT lexicographically and form the first column of the matrix. The first column is "$aaaaabn".
2. Pair each character in the BWT with the corresponding character in the first column by following the same cyclic order. For example, the first "a" in the BWT corresponds to the first "a" in the first column, the second "a" in the BWT corresponds to the second "a" in the first column, and so on. The pairs are:

```
a - $
n - a
n - a
b - a
$ - a
a - b
a - n
```

3. Sort the pairs lexicographically by the first element and form the second column of the matrix. The second column is "a$aaabn".
4. Repeat steps 2 and 3 until the matrix is complete. The complete matrix is:

```
$ - a - n - a - n - a - $
a - $ - a - a - a - b - n
a - a - $ - b - a - n - a
a - a - a - n - a - $ - b
a - b - a - n - a - n - $
b - n - a - $ - a - a - a
n - a - a - a - b - $ - a
```

5. Find the row that ends with the special symbol "$" and take the rest of the row as the original string. The row that ends with "$" is the first row, and the rest of the row is "banana", which is the original string.

The BWT has some properties that make it suitable for data compression, such as:

- The BWT tends to group similar characters together, which makes it easier to apply other compression techniques such as move-to-front transform and run-length encoding .
- The BWT preserves the relative order of the characters in the original string, which makes it possible to reverse the transformation without any additional information .
- The BWT is independent of the alphabet size and the frequency distribution of the characters, which makes it adaptable to different types of data .

The BWT is the basis of some popular compression algorithms, such as bzip2 and FM-index. The BWT can also be



# Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but prepares it for better compression by entropy encoding techniques  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) and output the index of each symbol in the input sequence, while moving the symbol to the front of the list  .
- This way, symbols that appear frequently in the input sequence will have smaller indices and will be more likely to be encoded with fewer bits by entropy encoding techniques such as Huffman coding or arithmetic coding  .
- Movetofront coding is an invertible transformation, meaning that the original input sequence can be recovered from the output sequence and the list of symbols  .
- Movetofront coding is fast and easy to implement, and can improve the compression ratio of data that has long-range dependencies or repetitions   .
- Movetofront coding is used as a sub-step in several compression algorithms, such as bzip2, PAQ, and ZPAQ .



# CALIC for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a codec that obtains higher lossless compression of continuous-tone images than other lossless image coding techniques in the literature  .
- It has relatively low time and space complexities  .
- It can also be used to compress compound video with motion compensation.
- It puts heavy emphasis on image data modeling  .
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics .
- The non-linear predictor adapts via an error feedback mechanism .
- It uses a binary arithmetic coder to encode the prediction residuals .
- It has a feedback loop that updates the context models based on the coding results .
- It has a special mode for coding smooth areas and edges .
- It has a high compression ratio and a low distortion rate .



# JPEG-LS

- JPEG-LS is a compression standard for continuous-tone images that supports both lossless and near-lossless modes  .
- JPEG-LS is based on the LOCO-I (LOw COmplexity LOssless COmpression for Images) algorithm developed at Hewlett-Packard Laboratories .
- JPEG-LS consists of two independent and distinct stages: modeling and encoding .
- In the modeling stage, JPEG-LS predicts the value of each pixel based on its neighboring pixels and computes the prediction error .
- In the encoding stage, JPEG-LS encodes the prediction error using a context-based adaptive Golomb-Rice code .
- JPEG-LS achieves high compression performance by exploiting the local correlation and smoothness of natural images .
- JPEG-LS has low complexity and memory requirements, making it suitable for embedded and real-time applications .
- JPEG-LS is defined in two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), which specifies the core technology, and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), which contains the extensions.
- JPEG-LS extensions include support for progressive coding, hierarchical coding, region of interest coding, and arithmetic coding.
- JPEG-LS is compatible with the JPEG File Interchange Format (JFIF) and the JPEG 2000 File Format (JP2) for storing and exchanging compressed images.



# Multi-resolution Approaches

- Multi-resolution approaches are methods that use different levels of resolution or detail to represent or process data, such as images, vectors, or fluids.
- Multi-resolution approaches can improve the performance, efficiency, and accuracy of data compression algorithms by exploiting the properties of different scales and frequencies in the data.
- Some examples of multi-resolution approaches for data compression are:

  - **Multiresolution vector data compression**: This method uses a quadtree structure to partition a vector data set into blocks of different sizes and shapes, and then compresses each block according to its complexity and importance. The compression efficiency is further improved by grid filtering and binary offset for linear and point geometries. The vector spatial data compression takes visual lossless distance on screen display as accuracy requirement.
  - **Multi-resolution fractal image compression**: This method combines wavelets and fractals transforms to compress images. Wavelets are used to decompose the image into different frequency bands, and fractals are used to encode each band by finding self-similarities within the image. This method reduces the characteristic distortions of conventional fractal compression algorithms, such as blocking artifacts and image blurring, by better coding of high frequencies.
  - **Multi-resolution method for compressible multi-phase flows**: This method uses a sharp interface model to track the interface between different phases of a fluid, and a multi-resolution analysis to adaptively refine or coarsen the computational grid according to the local features of the flow. This method reduces the memory and CPU-time requirements compared to adaptive mesh refinement methods, and preserves the accuracy and stability of the solution.



# Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission .
- Facsimile encoding is based on run-length encoding, which is a method of representing sequences of identical symbols by their length and value .
- For example, the sequence `000000111111000000` can be encoded as `6,0,6,1,6,0`, where the first number is the length and the second number is the value of the run.
- Facsimile encoding is especially suitable for binary images, such as text or line drawings, that have large areas of white or black pixels .
- Facsimile encoding can reduce the size of binary images by a factor of 10 to 20, depending on the image content and quality .
- Facsimile encoding can be further improved by using adaptive models, such as Huffman coding or arithmetic coding, that assign shorter codes to more frequent runs .
- For example, Huffman coding assigns variable-length codes to each run-length pair based on their probability of occurrence, while arithmetic coding encodes the entire sequence of run-length pairs as a single fraction.
- Facsimile encoding can be decompressed quickly for printing or viewing, as long as enough memory and CPU resources are available.



# Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It is based on the idea of Markov chains, which are mathematical models of systems that transition from one state to another with some probability.
- DMC builds a dynamic Markov model of the input data, which adapts to the changing patterns and frequencies of the bits.
- The model consists of a tree of nodes, each representing a context or a history of previous bits. The root node represents the empty context, and each child node represents a context with one more bit appended.
- Each node has two counters, one for the number of times a 0 bit has followed the context, and one for the number of times a 1 bit has followed the context.
- The counters are used to estimate the probability of the next bit given the context, which is then fed to the arithmetic coder.
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input.
- The model is also pruned periodically to remove nodes with low counts, to save memory and avoid overfitting.
- DMC is an effective and flexible compression algorithm that can adapt to various types of data and achieve high compression ratios. However, it is also computationally intensive and requires a large amount of memory.



## Unit 4 - Distortion criteria

- Distortion criteria are the measures of how well a communication system preserves the fidelity of the transmitted signal.
- Distortion criteria are important for evaluating the performance and quality of a communication system, especially for analog signals.
- Distortion criteria can be classified into two categories: linear and nonlinear.
- Linear distortion criteria are based on the assumption that the communication system is a linear system, meaning that it obeys the principles of superposition and scaling.
- Linear distortion criteria include amplitude distortion, phase distortion, group delay distortion, and inter-symbol interference.
- Amplitude distortion occurs when the communication system alters the amplitude of the signal components differently, resulting in a change in the signal shape or spectrum.
- Phase distortion occurs when the communication system alters the phase of the signal components differently, resulting in a change in the signal shape or spectrum.
- Group delay distortion occurs when the communication system alters the delay of the signal components differently, resulting in a change in the signal shape or spectrum.
- Inter-symbol interference occurs when the communication system causes the symbols or pulses of the signal to overlap or interfere with each other, resulting in a loss of information or errors.
- Nonlinear distortion criteria are based on the assumption that the communication system is a nonlinear system, meaning that it does not obey the principles of superposition and scaling.
- Nonlinear distortion criteria include harmonic distortion, intermodulation distortion, cross-modulation distortion, and clipping distortion.
- Harmonic distortion occurs when the communication system generates new frequency components that are multiples of the original signal frequency, resulting in a change in the signal spectrum or noise.
- Intermodulation distortion occurs when the communication system generates new frequency components that are sums or differences of the original signal frequency components, resulting in a change in the signal spectrum or noise.
- Cross-modulation distortion occurs when the communication system modulates one signal with another signal, resulting in a change in the signal spectrum or noise.
- Clipping distortion occurs when the communication system limits or cuts off the peaks of the signal, resulting in a change in the signal shape or spectrum.



# Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Distortion criteria are used to measure the quality of the approximation of the original data by the compressed data.
- Distortion criteria depend on the type and application of the data, such as images, audio, video, text, etc.
- Distortion criteria can be classified into two categories: objective and subjective.
- Objective distortion criteria are based on mathematical formulas that compare the original and reconstructed data, such as mean squared error (MSE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), etc.
- Subjective distortion criteria are based on human perception and evaluation of the quality of the approximation, such as mean opinion score (MOS), just noticeable difference (JND), etc.
- Distortion criteria are used to define the rate-distortion function, which is the minimum achievable compression rate for a given distortion level.
- Rate-distortion theory is the branch of information theory that studies the fundamental limits and trade-offs of data compression problems.
- Rate-distortion theory provides a lower bound for the compression rate, which can only be attained by increasing the coding block length or using optimal source codes.
- Rate-distortion theory also provides an iterative algorithm for calculating the rate-distortion function, which is based on the Blahut-Arimoto theorem.



# Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of levels, called quantization levels or reproduction values .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the precision of the signal representation and introduces quantization error or distortion.
- Scalar quantization can be performed on each signal sample independently, without considering the correlation or dependence among the samples . This makes scalar quantization easy to implement, but also suboptimal in terms of compression efficiency.
- Scalar quantization can be characterized by four main components :
  - The input range, which is the set of possible values of the input signal.
  - The quantizer, which is a function that maps the input range to a finite set of output levels, called the quantization index or code.
  - The reconstruction or dequantizer, which is a function that maps the quantization index to a set of reproduction values, called the output range or reconstruction alphabet.
  - The distortion measure, which is a function that quantifies the difference or error between the input signal and the reproduction value.
- Scalar quantization can be classified into two types, depending on the shape and size of the input range :
  - Uniform scalar quantization, which assumes that the input range is a finite interval and divides it into equal-sized subintervals, called quantization cells or bins. The quantization index is determined by the position of the input value within the input range, and the reproduction value is usually the midpoint or the centroid of the quantization cell.
  - Nonuniform scalar quantization, which adapts the shape and size of the quantization cells to the statistical properties of the input signal, such as its probability density function or its dynamic range. The quantization index is determined by a mapping function that assigns different input values to different quantization cells, and the reproduction value is usually the expected value or the optimal value of the quantization cell according to the distortion measure.
- Scalar quantization can be designed and evaluated using different criteria, such as the rate, the distortion, the signal-to-noise ratio, the mean squared error, the peak signal-to-noise ratio, the entropy, the Lloyd-Max algorithm, the companding technique, the uniform threshold quantization, the uniform midtread quantization, the uniform midrise quantization, the nonuniform threshold quantization, the nonuniform midtread quantization, the nonuniform midrise quantization, the optimal quantization, the high-rate quantization, the low-rate quantization, the dead-zone quantization, the overload distortion, the granular distortion, the quantization noise, the noise shaping, the dithering, the quantization noise power spectrum, the quantization noise shaping filter, the sigma-delta modulation, the wavelet/scalar quantization, etc   .



# The Quantization Problem

Quantization is a process of mapping a large set of input values to a smaller set of output values, such that the distortion or error introduced by this mapping is minimized. Quantization is a necessary step in lossy data compression, where some information is discarded to reduce the size of the data.

The quantization problem can be formulated as follows:

- Given a source X that produces a sequence of samples x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>N</sub> from a continuous or discrete alphabet A, and a distortion measure d(x, y) that quantifies the error between an input sample x and an output sample y, find a quantizer Q that maps each x to a y from a finite set of output levels B, such that the average distortion D is minimized.

- Mathematically, the quantization problem can be expressed as:

  - Q<sup>*</sup> = argmin<sub>Q</sub> D(Q) = argmin<sub>Q</sub> E[d(X, Q(X))]

  - where Q<sup>*</sup> is the optimal quantizer, E is the expectation operator, and Q(X) is the output of the quantizer for a given input X.

- The quantization problem is generally NP-hard, meaning that there is no efficient algorithm to find the optimal quantizer for an arbitrary source and distortion measure. Therefore, various approximation methods and heuristics are used to design practical quantizers.

- Some of the factors that affect the quantization problem are:

  - The size of the output set B, also known as the number of quantization levels M. A larger M allows for more fine-grained representation of the input values, but also requires more bits to encode the output values.

  - The shape and distribution of the input alphabet A. Some input values may be more likely or more important than others, and the quantizer should take this into account when assigning output levels.

  - The type and properties of the distortion measure d(x, y). Different distortion measures may reflect different aspects of the quality or fidelity of the output, such as mean squared error, signal-to-noise ratio, perceptual distortion, etc.

  - The type and structure of the quantizer Q. Quantizers can be classified into scalar or vector quantizers, depending on whether they operate on individual samples or blocks of samples. Quantizers can also be uniform or non-uniform, depending on whether they use equally spaced or variable output levels. Quantizers can also be adaptive or non-adaptive, depending on whether they adjust their parameters based on the input data or not.



# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero.
- A uniform quantizer can be combined with a companding technique to achieve non-uniform quantization, which can reduce the distortion for signals with non-uniform probability distribution.
  - A companding technique is a process of compressing the input signal before quantization and expanding the output signal after quantization.
  - Two common companding techniques are µ-law and A-law, which are used for PCM telephone systems.
    - µ-law companding has a mid-tread characteristic and is more suitable for signals with a large dynamic range.
    - A-law companding has a mid-rise characteristic and is more suitable for signals with a small dynamic range.
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model.
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the rate-distortion trade-off, which is a measure of the compression efficiency and quality .
- A uniform quantizer can be analyzed by using the high-rate regime, which assumes that the input signal has a smooth probability density function and the quantization intervals are nearly flat.
  - A uniform quantizer can be evaluated by using the mean squared error (MSE) or the signal-to-noise ratio (SNR) as the distortion metrics.
  - A uniform quantizer can be compared with the optimal quantizer, which minimizes the distortion for a given number of output levels.
  - A uniform quantizer can be shown to achieve a performance that is very close to the optimal quantizer at high bit rates .



# Adaptive Quantization

- Adaptive quantization is a type of data compression technique that adjusts the quantizer parameters according to the characteristics of the input signal.
- The goal of adaptive quantization is to provide effective data compression of a signal source with time-varying parameters. An adaptive quantizer estimates the statistics of the source and attempts to match the quantizer to the source distribution.
- Adaptive quantization can be classified into two categories: forward adaptive quantization and backward adaptive quantization.
- In forward adaptive quantization, the input is divided into blocks. The quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information. The receiver uses the same quantizer parameters to reconstruct the signal.
- In backward adaptive quantization, the quantizer parameters are updated based on the feedback from the receiver. The receiver sends back the quantization error or the reconstructed signal to the transmitter. The transmitter uses this information to adjust the quantizer parameters for the next input sample.
- Adaptive quantization can be applied to different types of quantizers, such as uniform, non-uniform, scalar, or vector quantizers. The choice of the quantizer depends on the nature of the input signal and the desired compression ratio and distortion level.
- Adaptive quantization can improve the performance of data compression schemes, such as differential pulse-code modulation (DPCM), transform coding, or subband coding, by adapting to the local variations of the signal.



# Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the input values are more concentrated and less bits to the regions where the input values are less frequent.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that adjusts the quantization intervals according to the statistics of the input signal, such as the Lloyd-Max quantizer or the delta modulation quantizer.
  - Using a trainable quantizer that learns the optimal quantization points from the data, such as the vector quantizer or the neural network quantizer .
- Non uniform quantization has applications in data compression, signal processing, machine learning, and communication systems    .



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Quantization is the process of mapping input values from a large set (often a continuous set) to output values in a (countable) smaller set, often with a finite number of elements.
- Scalar quantization is a type of quantization where each input symbol is treated separately in producing the output .
- Vector quantization is a type of quantization where the input symbols are clubbed together in groups called vectors, and processed to give the output .
- Some of the advantages of vector quantization over scalar quantization are:

  - Vector quantization can remove auto-correlation in the encoded signal and therefore, is more efficient in rate-distortion terms than scalar quantization.
  - Vector quantization can exploit the inter-symbol dependencies and reduce the redundancy in the input data.
  - Vector quantization can achieve higher compression ratios and lower distortion than scalar quantization for the same bit rate.
  - Vector quantization can adapt to the statistics of the input data and optimize the codebook according to the source distribution.
  - Vector quantization can handle multidimensional data more effectively than scalar quantization, which requires separate quantizers for each dimension.



# The Linde-Buzo-Gray Algorithm

The Linde-Buzo-Gray (LBG) algorithm is a vector quantization algorithm to derive a good codebook. A codebook is a set of representative vectors that can be used to encode or approximate a given set of data vectors. The LBG algorithm aims to minimize the distortion or error between the data vectors and their corresponding codebook vectors.

The LBG algorithm is based on the following steps :

- Start with a single codebook vector, which is the centroid or mean of the entire data set.
- Split the codebook vector into two slightly perturbed vectors, forming a codebook of size two.
- Assign each data vector to the nearest codebook vector, using the Euclidean distance as a measure of similarity.
- Update each codebook vector by computing the centroid of the data vectors assigned to it.
- Repeat the assignment and update steps until the codebook vectors converge or the distortion falls below a threshold.
- If the desired codebook size is not reached, go back to the splitting step and double the codebook size by splitting each codebook vector into two slightly perturbed vectors.
- Repeat the whole process until the desired codebook size is reached or the distortion cannot be reduced further.

The LBG algorithm is similar to the k-means algorithm in data clustering, except that the codebook size is not fixed in advance, but grows exponentially by splitting. The splitting step introduces some diversity in the codebook vectors, which helps to explore different regions of the data space and avoid local minima.

The LBG algorithm has some advantages over scalar quantization, which is the process of approximating a continuous-valued signal by a discrete set of values. Some of the advantages are:

- Vector quantization can achieve higher compression ratios than scalar quantization, since it exploits the correlation or redundancy among the components of a vector.
- Vector quantization can preserve the quality or fidelity of the signal better than scalar quantization, since it reduces the quantization noise or error.
- Vector quantization can adapt to the characteristics or statistics of the signal better than scalar quantization, since it can generate codebooks that match the distribution or shape of the data vectors.

However, vector quantization also has some disadvantages or challenges, such as:

- Vector quantization requires more computation and memory than scalar quantization, since it involves searching for the nearest codebook vector among a large set of candidates.
- Vector quantization requires a training phase to generate the codebook, which may not be feasible or efficient for some applications or data sets.
- Vector quantization may suffer from the curse of dimensionality, which means that the codebook size grows exponentially with the dimension of the data vectors, making the quantization process more difficult or impractical.



# Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node of a binary tree .
- The root node represents the entire input space, and the leaf nodes represent the final codebook vectors .
- The advantage of TSVQ is that it can be represented and stored efficiently using a binary tree, and the quantization process can be performed fast by traversing the tree from the root to the leaf that matches the input vector .
- TSVQ can be designed to minimize the expected distortion subject to different cost functions, such as storage cost, encoding rate, or quantization time.
- TSVQ can also be adapted to non-stationary sources by using dynamic splitting and pruning algorithms.

## Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of input vectors using a smaller set of codebook vectors .
- Scalar quantization (SQ) is a special case of VQ where the input and codebook vectors are one-dimensional .
- VQ has several advantages over SQ, such as :
  - VQ can exploit the correlation among the components of the input vectors, while SQ treats each component independently.
  - VQ can achieve lower distortion than SQ for the same number of bits per vector, or equivalently, lower bit rate than SQ for the same distortion level.
  - VQ can handle multidimensional data more naturally and efficiently than SQ, which requires vectorization and devectorization operations.
  - VQ can adapt to the statistics of the input data more easily than SQ, which requires uniform quantization or non-uniform quantization with fixed parameters.



# Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity, storage, or encoding time of the quantization process  .
- Vector quantization is a technique that maps a vector of continuous or discrete values (such as an image block or a speech segment) to a finite set of code vectors, each representing a region or a cell in the input space.
- Vector quantization is superior to scalar quantization, which operates on single values, in terms of rate-distortion performance, i.e., the trade-off between the bit rate and the quantization error .
- However, vector quantization also has some drawbacks, such as the high computational complexity of finding the optimal codebook and the optimal code vector for each input vector, and the large storage requirement for storing the codebook  .
- Structured vector quantizers aim to overcome these drawbacks by using some special structures for the codebook or the partition, such as tree-structured, lattice-structured, product-structured, or residual-structured vector quantizers  .
- Tree-structured vector quantizers use a hierarchical partition of the input space, where each node corresponds to a region or a cell, and each leaf node corresponds to a code vector. The encoding process is done by traversing the tree from the root to the leaf that contains the input vector. The decoding process is done by using the code vector of the leaf node as the output .
- Lattice-structured vector quantizers use a regular geometric arrangement of points in the input space, such as a hexagonal or a cubic lattice, as the code vectors. The encoding process is done by finding the nearest lattice point to the input vector. The decoding process is done by using the lattice point as the output .
- Product-structured vector quantizers use a Cartesian product of scalar or lower-dimensional vector quantizers as the codebook. The encoding process is done by applying each component quantizer to the corresponding component of the input vector. The decoding process is done by concatenating the outputs of each component quantizer.
- Residual-structured vector quantizers use a cascade of vector quantizers, where each quantizer operates on the residual error of the previous quantizer. The encoding process is done by applying each quantizer to the residual vector and concatenating the outputs. The decoding process is done by adding the outputs of each quantizer.
- Structured vector quantizers have some advantages over unstructured vector quantizers, such as lower complexity, lower storage, faster encoding, and better adaptability to the input statistics   .
- Structured vector quantizers also have some disadvantages, such as suboptimal rate-distortion performance, higher sensitivity to channel errors, and higher design difficulty  .

