

## Unit 1 - Compression Techniques

Compression techniques are used to reduce the size of data files for storage or transmission. There are two main types of compression techniques: lossless and lossy.

1. **Lossless Compression:** Lossless compression techniques reduce the size of the data without losing any information. This means that the original data can be perfectly reconstructed from the compressed data. Examples of lossless compression techniques include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression:** Lossy compression techniques reduce the size of the data by discarding some information. This means that the original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression techniques include JPEG for images and MP3 for audio.

Both types of compression techniques have their advantages and disadvantages. Lossless compression is useful when the original data must be preserved exactly, such as in the case of text or program files. Lossy compression is useful when the data is intended for human consumption, such as images or audio, where small losses in quality are acceptable in exchange for a significant reduction in size.



### Lossless Compression

Lossless compression is a type of data compression technique that allows the original data to be perfectly reconstructed from the compressed data. This is in contrast to lossy compression, where some information is lost during the compression process.

Here are some key points to remember about lossless compression:

1. Lossless compression is used when it is important that the original and the decompressed data be identical, or when no data can be lost. This is the case when compressing text, computer programs, or certain types of images such as those used in medical imaging.

2. Common lossless compression algorithms include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

3. Lossless compression is generally less effective than lossy compression in terms of reducing file size. However, the amount of compression that can be achieved depends on the characteristics of the data being compressed.

4. Lossless compression is used in many applications, including ZIP and GZIP file compression, PNG image compression, and FLAC audio compression.

5. Lossless compression techniques can be combined with lossy compression techniques to achieve even greater compression. For example, an image can be first compressed using a lossy technique to reduce its size, and then further compressed using a lossless technique to reduce its size even more.




### Lossy Compression

Lossy compression is a type of data compression technique that reduces the size of the original data by discarding some of the information. This technique is used when the exact reproduction of the original data is not necessary. The main advantage of lossy compression is that it can achieve a much higher compression ratio than lossless compression.

Some common examples of lossy compression techniques include:

1. **JPEG** - used for compressing digital images.
2. **MP3** - used for compressing audio files.
3. **MPEG** - used for compressing video files.

Lossy compression works by removing some of the less important information from the original data. For example, in the case of an image, the compression algorithm might remove some of the color information that is not easily noticeable by the human eye. Similarly, in the case of an audio file, the algorithm might remove some of the frequencies that are not easily audible to the human ear.

The main disadvantage of lossy compression is that the quality of the compressed data is lower than the original data. The amount of quality loss depends on the compression ratio and the specific compression algorithm used. In general, the higher the compression ratio, the lower the quality of the compressed data.

Lossy compression is commonly used in applications where the exact reproduction of the original data is not necessary, such as streaming media, online image galleries, and video conferencing. It is also used in applications where storage space is limited, such as mobile devices and digital cameras. However, it is not suitable for applications where the exact reproduction of the original data is important, such as medical imaging and scientific data analysis.



### Measures of performance for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. Compression Ratio: It is the ratio of the size of the compressed data to the size of the original data. It is used to measure the effectiveness of the compression algorithm.
2. Space Savings: It is the percentage of space saved by compressing the data. It is calculated by subtracting the size of the compressed data from the size of the original data and dividing the result by the size of the original data.
3. Bit Rate: It is the number of bits per second that are transmitted or processed. It is used to measure the speed of the compression algorithm.
4. Encoding Time: It is the time taken by the compression algorithm to compress the data. It is used to measure the speed of the compression algorithm.
5. Decoding Time: It is the time taken by the compression algorithm to decompress the data. It is used to measure the speed of the compression algorithm.
6. Fidelity: It is the measure of how accurately the decompressed data represents the original data. It is used to measure the quality of the compression algorithm.
7. Robustness: It is the ability of the compression algorithm to handle errors in the data. It is used to measure the reliability of the compression algorithm.




### Unit 1 - Compression Techniques in the subject of Data Compression

#### Modeling and coding

1. **Modeling** is the process of constructing a statistical model of the data to be compressed. The model is used to predict the probability of each symbol in the data, which is then used to assign shorter codes to more probable symbols and longer codes to less probable symbols.

2. **Coding** is the process of assigning a unique code to each symbol in the data based on the probabilities predicted by the model. There are two main types of coding techniques: entropy coding and dictionary coding.

3. **Entropy coding** techniques, such as Huffman coding and arithmetic coding, assign codes to symbols based on their probabilities. Symbols with higher probabilities are assigned shorter codes, while symbols with lower probabilities are assigned longer codes.

4. **Dictionary coding** techniques, such as Lempel-Ziv-Welch (LZW) and Deflate, use a dictionary to store commonly occurring patterns of symbols. These patterns are then assigned codes, allowing the data to be compressed by replacing the patterns with their corresponding codes.

5. Both modeling and coding are essential components of data compression. The effectiveness of the compression depends on the accuracy of the model and the efficiency of the coding technique used.



### Mathematical Preliminaries for Lossless Compression

Lossless compression is a technique used to reduce the size of data without losing any information. This is achieved by identifying and removing redundancy in the data. In order to understand the concepts and techniques used in lossless compression, it is important to have a basic understanding of some mathematical concepts. Here are some of the key mathematical preliminaries for lossless compression:

1. **Information Theory:** This is a branch of mathematics that deals with the representation, storage, and transmission of information. It provides the theoretical foundation for lossless compression techniques.

2. **Entropy:** Entropy is a measure of the uncertainty or randomness of a random variable. In the context of lossless compression, it is used to measure the amount of information in the data.

3. **Probability:** Probability is the measure of the likelihood of an event occurring. In lossless compression, probability is used to model the data and to determine the likelihood of different symbols or patterns occurring.

4. **Coding Theory:** Coding theory is the study of methods for representing data in a way that is efficient and resistant to errors. In lossless compression, coding theory is used to develop efficient encoding and decoding algorithms.

5. **Data Structures:** Data structures are used to organize and store data in a way that allows for efficient access and manipulation. In lossless compression, data structures such as trees and hash tables are used to implement encoding and decoding algorithms.

These are some of the key mathematical concepts that are important for understanding lossless compression. A good understanding of these concepts will help in understanding the techniques used in lossless compression and in developing efficient compression algorithms.



### A brief introduction to information theory for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

Information theory is a branch of mathematics that deals with the representation, storage, and transmission of information. It was first introduced by Claude Shannon in 1948, in his paper "A Mathematical Theory of Communication."

Some key concepts in information theory include:

1. **Entropy:** This measures the average amount of information that can be conveyed by a random variable. It is a measure of the uncertainty or randomness of the variable.

2. **Redundancy:** This refers to the presence of additional information in a message that is not necessary for its transmission. Redundancy can be used to improve the reliability of communication, by allowing for error correction.

3. **Data Compression:** This is the process of reducing the number of bits needed to represent a piece of information. Data compression techniques can be lossless, where the original data can be perfectly reconstructed, or lossy, where some information is lost in the compression process.

4. **Channel Capacity:** This measures the maximum rate at which information can be transmitted over a communication channel, subject to a given level of noise or error.

Information theory has applications in many fields, including computer science, engineering, and biology. In the context of data compression, information theory provides the theoretical basis for the design of efficient compression algorithms.



### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression algorithms include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression algorithms include JPEG for images and MP3 for audio.

3. **Run-Length Encoding (RLE)**: This technique compresses data by replacing consecutive occurrences of the same symbol with a single occurrence of the symbol followed by the number of occurrences. For example, the string "AAAABBBCC" would be compressed to "A4B3C2" using RLE.

4. **Dictionary-based Compression**: This technique compresses data by replacing common substrings with shorter codes. The codes and their corresponding substrings are stored in a dictionary. Examples of dictionary-based compression algorithms include LZW and DEFLATE.

5. **Transform-based Compression**: This technique compresses data by transforming it into a different representation that is more compressible. Examples of transform-based compression algorithms include the Discrete Cosine Transform (DCT) used in JPEG and the Discrete Wavelet Transform (DWT) used in JPEG 2000.

6. **Hybrid Compression**: This technique combines two or more of the above techniques to achieve better compression. For example, the DEFLATE algorithm combines dictionary-based compression with Huffman coding.




### Physical models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique involves compressing data without losing any information. The original data can be perfectly reconstructed from the compressed data.
2. **Lossy Compression**: This technique involves compressing data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data, but the loss of information is usually not noticeable to the human eye or ear.
3. **Huffman Coding**: This is a lossless compression technique that involves assigning shorter codes to more frequently occurring symbols and longer codes to less frequently occurring symbols.
4. **Run-Length Encoding**: This is a lossless compression technique that involves replacing consecutive occurrences of the same symbol with a single occurrence of the symbol followed by the number of times it occurs.
5. **Arithmetic Coding**: This is a lossless compression technique that involves assigning a range of values to each symbol based on its probability of occurrence.
6. **Lempel-Ziv-Welch (LZW) Algorithm**: This is a lossless compression technique that involves replacing common substrings with codes.
7. **Transform Coding**: This is a lossy compression technique that involves transforming the data into a different domain, such as the frequency domain, and discarding less important information.
8. **Discrete Cosine Transform (DCT)**: This is a lossy compression technique that involves transforming the data into the frequency domain and discarding less important information.
9. **Fractal Compression**: This is a lossy compression technique that involves representing an image as a set of mathematical equations that describe its self-similar patterns.
10. **Vector Quantization**: This is a lossy compression technique that involves dividing the data into blocks and representing each block with a code from a codebook.




### Probability Models for Unit 1 - Compression Techniques in Data Compression

1. Probability models are used to represent the likelihood of different outcomes in a random event.
2. In the context of data compression, probability models are used to estimate the probability of occurrence of different symbols in the data.
3. The more accurate the probability model, the better the compression performance.
4. Common probability models used in data compression include:
    - Uniform distribution: Assumes all symbols have an equal probability of occurrence.
    - Bernoulli distribution: Models binary data where the probability of one outcome is fixed.
    - Markov models: Assumes the probability of a symbol depends on the previous symbol.
    - Context-based models: Assumes the probability of a symbol depends on the context in which it appears.
5. The choice of probability model depends on the characteristics of the data being compressed.
6. Probability models can be static, where the probabilities are fixed, or adaptive, where the probabilities are updated as more data is processed.
7. Adaptive probability models can improve compression performance for data with changing characteristics.




### Markov Models

Markov models are a type of statistical model used to represent systems that change over time. They are named after the Russian mathematician Andrey Markov, who developed the theory of Markov processes.

In the context of data compression, Markov models can be used to model the probability distribution of sequences of symbols, such as characters in a text file. This can be useful for compression techniques that rely on predicting the next symbol in a sequence based on the previous symbols.

Here are some key points to remember about Markov models:

1. Markov models assume that the future state of a system depends only on its current state, and not on its past states. This is known as the Markov property.
2. Markov models can be represented as a directed graph, where the nodes represent the possible states of the system, and the edges represent the probabilities of transitioning between states.
3. Markov models can be used to model a wide range of systems, including physical processes, economic systems, and biological systems.
4. In the context of data compression, Markov models can be used to improve the efficiency of techniques such as Huffman coding and arithmetic coding.




### Composite Source Model

- A composite source model is used in data compression when it is not simple to use a single model to describe the source in many applications.
- A composite source can be represented as a number of individual sources S i, each with its own model M i and a switch that selects a source S i with probability P i.
- This is an exceptionally rich model and can be used to describe some very complicated processes.
- When these models are used for lossless image compression, the composite source models are shown to perform better than the traditional single source model in the sense of reducing the source modeling entropy.



### Unit 1 - Compression Techniques in the subject of Data Compression

1. **Data Compression** is the process of reducing the size of data files without losing the information contained in them.
2. **Lossless Compression** is a type of data compression where the original data can be perfectly reconstructed from the compressed data.
3. **Lossy Compression** is a type of data compression where some information is lost in the process of compression, but the resulting compressed data is still useful for its intended purpose.
4. **Huffman Coding** is a lossless data compression algorithm that assigns shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters.
5. **Run-Length Encoding** is a lossless data compression algorithm that replaces consecutive occurrences of the same character with a single character and a count of the number of occurrences.
6. **Lempel-Ziv-Welch (LZW)** is a lossless data compression algorithm that builds a dictionary of commonly occurring substrings and replaces them with shorter codes.
7. **Arithmetic Coding** is a lossless data compression algorithm that assigns codes to entire messages based on the probability of the message occurring.
8. **Transform Coding** is a lossy data compression algorithm that transforms the data into a different representation, where the most important information is concentrated in a few coefficients, which are then quantized and encoded.



### Uniquely Decodable Codes

Uniquely decodable codes are a type of variable-length code used in data compression techniques. These codes are designed to ensure that the original data can be recovered exactly from the compressed data, without any ambiguity.

Here are some key points to remember about uniquely decodable codes:

1. Uniquely decodable codes are a type of prefix code, which means that no codeword is a prefix of another codeword. This property ensures that the original data can be recovered exactly from the compressed data.

2. Huffman coding is a commonly used method for constructing uniquely decodable codes. This method assigns shorter codewords to more frequently occurring symbols, and longer codewords to less frequently occurring symbols, resulting in efficient compression.

3. Another method for constructing uniquely decodable codes is arithmetic coding. This method represents the entire message as a single real number, and assigns a range of real numbers to each symbol based on its probability of occurrence.

4. Uniquely decodable codes are used in many data compression techniques, including lossless compression methods such as gzip and bzip2.

5. The efficiency of uniquely decodable codes depends on the statistical properties of the data being compressed. If the data has a skewed distribution, with some symbols occurring much more frequently than others, then uniquely decodable codes can achieve high compression ratios.




### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. Prefix codes are a type of variable-length code used for data compression.
2. A prefix code is a code in which no codeword is a prefix of another codeword.
3. Prefix codes are also known as instantaneous codes, as they can be decoded without the need for a look-ahead buffer.
4. Huffman coding is a popular method for constructing prefix codes.
5. Prefix codes can be represented using a binary tree, where the leaves represent the codewords.
6. The average codeword length of a prefix code is minimized when the probabilities of the symbols are sorted in decreasing order.
7. Prefix codes are optimal for data compression when the probabilities of the symbols are known.




## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a lossless data compression algorithm that was developed by David A. Huffman in 1952. It is a variable-length coding algorithm that assigns shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters.

The steps involved in the Huffman coding algorithm are as follows:

1. Create a frequency table for each character in the input data.
2. Create a priority queue and insert each character and its frequency as a node in the queue.
3. While the queue has more than one node:
    1. Remove the two nodes with the lowest frequency from the queue.
    2. Create a new internal node with the sum of the frequencies of the two nodes as its frequency.
    3. Assign the two removed nodes as the left and right children of the new internal node.
    4. Insert the new internal node into the queue.
4. The remaining node in the queue is the root of the Huffman tree.
5. Traverse the Huffman tree and assign codes to the characters based on the path from the root to the leaf node representing the character.

The Huffman coding algorithm is widely used in data compression and has been implemented in various file formats such as JPEG and MP3. It is an efficient algorithm that can significantly reduce the size of the input data while allowing for lossless decompression.



### Minimum variance Huffman codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Minimum variance Huffman codes are a type of Huffman code that aim to minimize the variance of the codeword lengths.
- This is achieved by assigning shorter codewords to symbols with higher probabilities and longer codewords to symbols with lower probabilities.
- The Huffman coding algorithm is used to construct the minimum variance Huffman codes.
- The algorithm starts by creating a list of the symbols and their probabilities.
- The two symbols with the lowest probabilities are then combined into a single node with a probability equal to the sum of their probabilities.
- This process is repeated until there is only one node left, which represents the root of the Huffman tree.
- The codewords are then assigned by traversing the tree from the root to the leaves, assigning a 0 to the left branch and a 1 to the right branch at each node.
- The resulting codewords have minimum variance, which can be beneficial in certain applications, such as in data compression where it can lead to more efficient storage and transmission of data.



### Adaptive Huffman coding

- Adaptive Huffman coding, also known as Dynamic Huffman coding, is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution.
- This allows for one-pass encoding and adaptation to changing conditions in data.
- As characters are processed, frequencies are updated and codes are changed, or the coding tree is modified.
- The implementation of Adaptive Huffman coding is done using the Vitter Algorithm.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes based on the frequencies of input characters.
- A binary tree is built to organize characters based on frequency in order to determine what code to assign to each character.



### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Review the current notes and identify any outdated or incorrect information.
2. Consult reliable sources such as textbooks, research papers, and online resources to gather updated and accurate information.
3. Revise the notes by incorporating the new information and removing any outdated or incorrect information.
4. Organize the revised notes in a clear and logical manner, using headings, subheadings, and bullet points to improve readability.
5. Verify the accuracy and completeness of the revised notes by cross-checking with multiple sources.
6. Share the revised notes with peers or instructors for feedback and further refinement.
7. Continuously review and update the notes to ensure their relevance and accuracy.




### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. The Huffman coding algorithm is a lossless data compression algorithm that assigns variable-length codes to input symbols based on their frequencies of occurrence.
2. The first step in the Huffman coding algorithm is to create a frequency table that counts the number of occurrences of each symbol in the input data.
3. The next step is to build a binary tree, where each leaf node represents a symbol and its weight is the frequency of the symbol.
4. The tree is constructed by repeatedly merging the two nodes with the lowest weights until there is only one node left, which is the root of the tree.
5. The code for each symbol is obtained by traversing the tree from the root to the leaf node representing the symbol, with left branches adding a 0 to the code and right branches adding a 1.
6. The resulting codes are prefix-free, meaning that no code is a prefix of another code, which ensures that the encoded data can be uniquely decoded.
7. The Huffman coding algorithm is optimal in the sense that it produces the shortest possible average code length for a given set of symbol frequencies.
8. The algorithm can be implemented efficiently using a priority queue to keep track of the nodes with the lowest weights during the tree construction.




### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Huffman coding is a lossless data compression algorithm.
2. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
3. The most frequent character gets the smallest code and the least frequent character gets the largest code.
4. The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
5. Let us understand the algorithm with an example:

    - Consider the string `ABRACADABRA`. The frequencies of characters in the string are:

        - A: 5
        - B: 2
        - R: 2
        - C: 1
        - D: 1

    - The Huffman tree for the given string is as follows:

        ```
             /\ 
            /  \
           A   /\
             /  \
            B   /\
              /  \
             R   /\
               /  \
              C   D
        ```

    - The codes for the characters are as follows:

        - A: 0
        - B: 10
        - R: 110
        - C: 1110
        - D: 1111

    - The encoded string is `0110111010001010110111100`.

6. To decode the encoded string, we need to traverse the Huffman tree from the root and for each `0`, we move to the left child and for each `1`, we move to the right child. When we reach a leaf node, we print the character and start traversing the tree from the root again.

7. The decoded string is `ABRACADABRA`.

8. The time complexity of the Huffman coding algorithm is `O(nlogn)` where `n` is the number of unique characters in the input string.

9. The space complexity of the Huffman coding algorithm is `O(n)` where `n` is the number of unique characters in the input string.

10. Huffman coding is widely used in data compression applications such as file compression, image compression, and video compression. It is also used in the implementation of the DEFLATE algorithm which is used in the popular data compression formats such as ZIP and GZIP.



### Golomb codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Golomb codes are a type of prefix code used in lossless data compression.
- They were invented by Solomon W. Golomb in the 1960s.
- Golomb codes are optimal for alphabets following a geometric distribution.
- They are commonly used in Rice coding, which is a variant of Golomb coding.
- Golomb codes can be parameterized by a positive integer m.
- The choice of m determines the length of the codewords.
- The encoding process involves dividing the input value by m and encoding the quotient and remainder separately.
- The quotient is encoded using unary coding, while the remainder is encoded using truncated binary encoding.
- Golomb codes have applications in data compression, error correction, and cryptography.
- They are used in the compression of image, audio, and video data.
- Golomb codes are also used in the encoding of Golomb-Rice filters, which are used in the Bloom filter data structure.




### Rice codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Rice codes and Huffman coding algorithm are both types of lossless compression algorithms .
- Huffman coding is a particular type of optimal prefix code that is commonly used for lossless data compression .
- Huffman coding was developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes" .
- The idea behind Huffman coding is to assign variable-length codes to input characters, with the lengths of the assigned codes being based on the frequencies of the corresponding characters .
- Rice coding is also used in lossless image codecs, such as the FELICS lossless image codec .
- The Golomb–Rice coder is used in the entropy coding stage of Rice algorithm based lossless image codecs .
- One experiment comparing the two algorithms found that the Rice Code algorithm is superior to Huffman .



### Tunstall codes

- Tunstall coding is a form of entropy coding used for lossless data compression .
- It was the subject of Brian Parker Tunstall's PhD thesis in 1967, while at Georgia Institute of Technology. The subject of that thesis was "Synthesis of noiseless compression codes"  .
- Its design is a precursor to Lempel–Ziv .
- Unlike variable-length codes, which include Huffman and Lempel–Ziv coding, both Tunstall codes and Lempel–Ziv codes represent variable-length words by fixed-length codes .
- Tunstall coding parses a stochastic source with codewords of variable length .




### Applications of Huffman coding

Huffman coding is a lossless data compression algorithm that is widely used in various applications. Some of the applications of Huffman coding are:

1. **File Compression:** Huffman coding is used to compress files such as text, images, audio, and video. It reduces the size of the file without losing any information, making it easier to store and transmit.

2. **Data Transmission:** Huffman coding is used in data transmission to reduce the number of bits required to transmit the data. This results in faster transmission and reduced bandwidth usage.

3. **Error Correction:** Huffman coding can be used in error correction to detect and correct errors that may occur during data transmission.

4. **Image Compression:** Huffman coding is used in image compression algorithms such as JPEG to reduce the size of the image file without losing much quality.

5. **Text Compression:** Huffman coding is used in text compression algorithms to reduce the size of the text file. This is useful for storing large amounts of text data, such as books or articles.

6. **Video Compression:** Huffman coding is used in video compression algorithms such as MPEG to reduce the size of the video file without losing much quality. This is useful for streaming videos over the internet.

These are some of the applications of Huffman coding in the field of data compression. It is a widely used algorithm that has proven to be effective in reducing the size of data without losing any information.



### Lossless Image Compression using Huffman Coding Algorithm

- **Image compression** is the technique that deals with the problem of reducing the amount of data required to represent a digital image.
- Image compression is achieved by removal of one or three basic data redundancies: (1) coding redundancy, (2) spatial redundancy, (3) irrelevant information.
- **Huffman coding** is a particular type of optimal prefix code that is commonly used for lossless data compression.
- Prefix code means that the code assigned to one character is not a prefix of code assigned to any other character.
- The idea is to assign variable-length codes to input characters, lengths of assign codes are based on the frequencies of corresponding characters.
- The most frequent occurring character gets the smallest input code and the most occurring character gets the largest code.
- Huffman coding has application in fields where it is important that the original and decompressed data be identical, like in zip file format and is often used as a component within lossy data compression techniques like mp3 encoder and other lossy audio encoder.
- The result from Huffman’s algorithm is viewed as a variable code table. This algorithm derives the table from an estimated probability or frequency of occurrence (weight) for each possible value of source symbol.
- Huffman coding is the base of JPEG image compression.
- An algorithm is created in Delphi to implement Huffman coding method that removes redundant codes from the image and compresses a BMP image file (especially grayscale image) and it is successfully reconstructed and an exact representation of the original because it is lossless compression technique.
- Huffman coding and arithmetic coding both are well-recognized lossless entropy coding algorithms.



### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Text compression is the process of reducing the size of a text file by encoding its content in a more efficient manner.
2. Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.
3. The most frequent characters are assigned the shortest codes, while the least frequent characters are assigned the longest codes.
4. Huffman coding is an optimal prefix code, meaning that no code is a prefix of another code.
5. The Huffman coding algorithm involves building a binary tree where the leaves represent the input characters and their frequencies.
6. The tree is built from the bottom up, by merging the two nodes with the lowest frequencies until there is only one node left, which represents the root of the tree.
7. The codes are then assigned by traversing the tree from the root to the leaves, assigning a 0 to the left branch and a 1 to the right branch at each step.
8. Huffman coding is widely used in data compression, including in file formats such as ZIP and GZIP.



### Audio Compression

Audio compression is the process of reducing the size of an audio file while maintaining its quality. One of the algorithms that can be used for audio compression is the Huffman coding algorithm.

#### The Huffman coding algorithm

The Huffman coding algorithm is named after its inventor, David Huffman, formerly a professor at MIT. Huffman compression is a lossless compression algorithm that is ideal for compressing text or program files. This probably explains why it is used a lot in compression programs like ZIP or ARJ .

One development of the Huffman algorithm is called Huffman Shift Coding. Huffman Shift Coding is able to change any symbol held on audio data either lossy or lossless. The Huffman Shift Coding method that has been tested has an average compression ratio of −50% above .

Efficient compression can be achieved by the Huffman coding at low bit-rate transmission. The proposed method is seen to possess a better frequency characteristic and a simpler processing algorithm than MPEG-1 audio .

In practice, Huffman coding is widely used in many applications. For example, it is used in "ZIP" style file compression formats, *.jpeg and *.png image formats, and *.mp3 audio files .

There are several types of entropy coding. Some of the commonly used ones are Huffman coding, Arithmetic coding, and Rice coding. For our coder, we have used Huffman entropy coding .



## Unit 3 - Coding a sequence

1. A sequence is an ordered collection of elements, where each element can be of any data type such as integer, string, or float.
2. In programming, sequences can be represented using various data structures such as arrays, lists, or tuples.
3. To code a sequence, you need to first choose the appropriate data structure to represent it.
4. For example, in Python, you can use a list to represent a sequence. To create a list, you can use square brackets `[]` and separate the elements with commas.
5. Here is an example of creating a list in Python to represent a sequence of numbers:
```python
my_sequence = [1, 2, 3, 4, 5]
```
6. Once you have created the sequence, you can access its elements using indexing. In Python, indexing starts from 0, so to access the first element of the sequence, you can use `my_sequence[0]`.
7. You can also perform various operations on the sequence such as adding or removing elements, sorting the sequence, or finding the length of the sequence.
8. Here is an example of adding an element to the sequence in Python:
```python
my_sequence.append(6)
```
9. In summary, coding a sequence involves choosing the appropriate data structure to represent it, creating the sequence, and performing operations on it as needed.



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. A binary code is a way of representing data using only two symbols, typically 0 and 1.
2. In the context of data compression, binary codes can be used to encode a sequence of symbols in a more compact form.
3. One approach to generating a binary code for a sequence is to use a fixed-length code, where each symbol is assigned a unique binary code of the same length.
4. Another approach is to use a variable-length code, where the length of the binary code for each symbol varies depending on the frequency of the symbol in the sequence.
5. Huffman coding is a commonly used variable-length coding technique that assigns shorter codes to more frequent symbols and longer codes to less frequent symbols.
6. To generate a Huffman code for a sequence, first, the frequency of each symbol in the sequence is determined.
7. Then, a binary tree is constructed where the leaves represent the symbols and the weight of each leaf is the frequency of the corresponding symbol.
8. The tree is constructed by repeatedly merging the two nodes with the lowest weight until only one node remains.
9. The binary code for each symbol is then determined by the path from the root of the tree to the leaf representing the symbol, where a left branch is represented by a 0 and a right branch is represented by a 1.
10. The resulting Huffman code is a prefix code, meaning that no code is a prefix of another code, which ensures that the encoded sequence can be uniquely decoded.




### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- **Binary coding** is a method of representing data using a fixed number of bits for each symbol. This means that the length of the code for each symbol is the same, regardless of its frequency in the data.

- **Huffman coding** is a variable-length coding method that assigns shorter codes to more frequently occurring symbols and longer codes to less frequently occurring symbols. This results in a more efficient representation of the data, as the most common symbols require fewer bits to represent.

- The main advantage of Huffman coding over binary coding is its ability to reduce the average code length, resulting in a more compact representation of the data. This can lead to significant savings in storage space or transmission time.

- However, Huffman coding requires knowledge of the frequency of each symbol in the data, which may not always be available or easy to determine. In contrast, binary coding does not require any knowledge of the data and can be applied to any set of symbols.

- In summary, Huffman coding is generally more efficient than binary coding, but requires more information about the data to be encoded. The choice between the two methods depends on the specific requirements of the application and the availability of information about the data.



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Lossless data compression**: Lossless data compression algorithms are used to compress data without losing any information. This is useful for applications where the original data must be perfectly preserved, such as text documents, spreadsheets, and databases.

2. **Lossy data compression**: Lossy data compression algorithms are used to compress data by discarding some information. This is useful for applications where some loss of quality is acceptable, such as images, audio, and video.

3. **Data transmission**: Data compression is used to reduce the amount of data that needs to be transmitted over a network. This can reduce the time it takes to transmit the data and can also reduce the cost of data transmission.

4. **Data storage**: Data compression is used to reduce the amount of storage space required to store data. This can reduce the cost of storage and can also make it possible to store more data in the same amount of space.

5. **Error correction**: Some data compression algorithms include error correction codes that can detect and correct errors that may occur during data transmission or storage. This can improve the reliability of the data.



### Bi-level image compression-The JBIG standard

- JBIG is an early lossless image compression standard from the Joint Bi-level Image Experts Group.
- It was standardized as ISO/IEC standard 11544 and as ITU-T recommendation T.82 in March 1993.
- It is widely implemented in fax machines.
- Now that the newer bi-level image compression standard JBIG2 has been released, JBIG is also known as JBIG1.
- JBIG was designed for compression of binary images, particularly for faxes, but can also be used on other images.
- In most situations, JBIG offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement.
- This lossless compression standard is used primarily to code scanned images of printed or handwritten text, computer-generated text, and facsimile transmissions.



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group.
- It is suitable for both lossless and lossy compression.
- JBIG2 typically generates files 3–5 times smaller than Fax Group 4 and 2–4 times smaller than JBIG in its lossless mode.
- JBIG2 was standardized in 2001, as a single part specification, and specifies both encoder and decoder.
- Compression of this type of image is also addressed by existing standards, for example MH&MR (ITU-T T.4), MMR (ITU-T T.6), and JBIG1 (T.82| ISO/IEC 11544).
- By segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, compression techniques that are specially optimized for each type of content are employed.
- JBIG2 allows for lossless compression performance better than that of the existing standards, and to allow for lossy compression at much higher compression ratios than the lossless ratios of the existing standards, with almost no visible degradation of quality by using pattern matching and substitution techniques in addition to the technologies of the existing standards.



### Image Compression

Image compression is the process of reducing the size of an image file while maintaining its visual quality. This is achieved by removing redundant or unnecessary information from the image data. Image compression is important for efficient storage and transmission of digital images.

There are two main types of image compression: lossless and lossy.

1. **Lossless Compression:** This type of compression reduces the size of the image file without any loss of information. The original image can be perfectly reconstructed from the compressed data. Examples of lossless image compression algorithms include PNG, GIF, and TIFF.

2. **Lossy Compression:** This type of compression reduces the size of the image file by discarding some information. The original image cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye. Examples of lossy image compression algorithms include JPEG and WebP.

Image compression algorithms use various techniques to reduce the size of the image data. These techniques include:

- **Predictive coding:** This technique predicts the value of a pixel based on the values of its neighboring pixels. The difference between the predicted value and the actual value is then encoded.

- **Transform coding:** This technique transforms the image data into a different domain, such as the frequency domain. The transformed data is then quantized and encoded.

- **Entropy coding:** This technique encodes the image data based on its statistical properties. The most common entropy coding algorithm used in image compression is Huffman coding.

Image compression is an important topic in the field of data compression and is widely used in various applications, such as digital photography, web design, and video streaming. It is a complex and fascinating subject that continues to evolve with advances in technology.



### Dictionary Techniques

Dictionary techniques are used for coding a sequence in data compression. These techniques involve the use of a dictionary, which is a data structure that stores a set of symbols or strings. The dictionary is used to encode and decode the data by replacing the symbols or strings with their corresponding codes.

Some of the key points to remember about dictionary techniques are:

1. Dictionary techniques are used to compress data by replacing symbols or strings with their corresponding codes.
2. The dictionary is a data structure that stores a set of symbols or strings.
3. The dictionary is used to encode and decode the data.
4. The efficiency of the dictionary technique depends on the size of the dictionary and the frequency of the symbols or strings in the data.
5. Dictionary techniques can be static or adaptive. Static dictionary techniques use a fixed dictionary, while adaptive dictionary techniques update the dictionary dynamically based on the data being compressed.




### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Data compression is the process of encoding information using fewer bits than the original representation.
2. The goal of data compression is to reduce the size of data for storage or transmission.
3. Coding a sequence is one of the techniques used in data compression.
4. In this technique, a sequence of symbols is represented using a code, where each symbol is assigned a unique code word.
5. The code words are chosen in such a way that the resulting coded sequence is shorter than the original sequence.
6. There are two main types of coding techniques: lossless and lossy.
7. Lossless coding techniques preserve all the information in the original sequence, while lossy techniques discard some information to achieve higher compression ratios.
8. In this unit, we will focus on lossless coding techniques for coding a sequence.



### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- A static dictionary is a type of dictionary used in data compression algorithms.
- It is a fixed set of symbols or codes that are used to represent the data being compressed.
- The dictionary is created before the compression process begins and remains unchanged throughout the process.
- The dictionary is typically created by analyzing the data to be compressed and identifying the most frequently occurring symbols or patterns.
- These symbols or patterns are then assigned codes, with the most frequently occurring symbols being assigned the shortest codes.
- During the compression process, the data is scanned and each symbol or pattern is replaced with its corresponding code from the dictionary.
- The use of a static dictionary can result in significant compression, especially if the data being compressed contains many repetitive symbols or patterns.
- However, the effectiveness of a static dictionary can be limited if the data being compressed changes significantly over time, as the dictionary may not accurately represent the new data.
- In such cases, a dynamic dictionary, which is updated during the compression process, may be more effective.




### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

Diagram coding is a method of data compression that is used to encode a sequence of symbols. It is based on the idea of representing a sequence of symbols as a single symbol, called a diagram, that is constructed by concatenating the symbols in the sequence.

Some key points to remember about diagram coding are:

1. Diagram coding is a lossless compression method, meaning that the original data can be perfectly reconstructed from the compressed data.
2. The effectiveness of diagram coding depends on the statistical properties of the data being compressed. If the data contains many repeated sequences of symbols, diagram coding can achieve high compression ratios.
3. Diagram coding can be implemented using a variety of data structures and algorithms, including hash tables, tries, and Huffman coding.
4. Diagram coding is commonly used in text compression, where it is often combined with other compression methods to achieve even higher compression ratios.

Overall, diagram coding is a powerful and flexible method of data compression that can be applied to a wide range of data types and applications. It is an important topic to understand for anyone studying data compression or working in a field that involves the storage or transmission of large amounts of data.



### Adaptive Dictionary

- An adaptive dictionary is a type of dictionary used in data compression algorithms.
- It is called "adaptive" because it changes over time to reflect the data being compressed.
- The dictionary starts with a predefined set of symbols and is updated as new data is encountered.
- The goal of an adaptive dictionary is to improve the compression ratio by encoding frequently occurring data with shorter codes.
- One example of an algorithm that uses an adaptive dictionary is the Lempel-Ziv-Welch (LZW) algorithm.
- The LZW algorithm is commonly used in GIF image compression and the UNIX compress utility.
- The adaptive dictionary is also used in other data compression algorithms such as LZ77 and LZ78.
- The use of an adaptive dictionary can improve the compression ratio, but it can also increase the complexity of the algorithm and the time required for compression and decompression.




### The LZ77 Approach

LZ77 is a lossless data compression algorithm that is based on the idea of replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream. It is named after its inventors, Abraham Lempel and Jacob Ziv, and was published in 1977.

Here are some key points to remember about the LZ77 approach:

1. LZ77 uses a sliding window to find repeated strings of characters.
2. The sliding window is divided into two parts: the search buffer and the look-ahead buffer.
3. The search buffer contains previously seen data, while the look-ahead buffer contains the data to be compressed.
4. The algorithm searches the search buffer for the longest match to the data in the look-ahead buffer.
5. When a match is found, the algorithm outputs a pointer to the location of the match in the search buffer, along with the length of the match.
6. If no match is found, the algorithm outputs the next character in the look-ahead buffer as a literal.
7. The window is then slid forward by the length of the match (or one character if no match was found), and the process is repeated.

This approach is widely used in data compression and is the basis for many popular compression algorithms, such as DEFLATE (used in gzip and PNG) and LZW (used in GIF and TIFF). It is also used in the LZ family of algorithms, which includes LZ77, LZ78, and LZW.



### The LZ78 Approach

LZ78 is a lossless data compression algorithm that is used to compress a sequence of data. It is the second of the Lempel-Ziv algorithms, and was published by Abraham Lempel and Jacob Ziv in 1978. Here are some key points to note about the LZ78 approach:

1. LZ78 builds a dictionary of phrases that are encountered in the input data.
2. The dictionary is initialized with all possible symbols in the input alphabet.
3. As the input data is processed, new phrases are added to the dictionary.
4. Each phrase in the dictionary is assigned a unique index.
5. The compressed output consists of a sequence of indices that correspond to phrases in the dictionary.
6. The decompression process involves using the dictionary to reconstruct the original data from the sequence of indices.
7. LZ78 is a dictionary-based algorithm, and its performance depends on the size of the dictionary and the nature of the input data.
8. The algorithm is well-suited for compressing data with recurring patterns.




### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Data storage**: Coding a sequence can be used to compress data for storage, reducing the amount of space required to store the data.
2. **Data transmission**: Compressed data can be transmitted more efficiently, reducing the time and bandwidth required for transmission.
3. **Error correction**: Certain coding techniques can be used to detect and correct errors that may occur during data transmission or storage.
4. **Data security**: Coding a sequence can be used in combination with encryption techniques to enhance the security of data during transmission or storage.
5. **Image and video compression**: Coding a sequence is widely used in image and video compression, allowing for the efficient storage and transmission of multimedia content.
6. **Audio compression**: Coding a sequence is also used in audio compression, allowing for the efficient storage and transmission of audio content.




### File Compression-UNIX compress

- **Compress** is a fast, simple LZW file compressor. It is the de facto standard in the UNIX community for compressing files .
- Compressed files take up less disk space than normal files, but you cannot read them in the usual way; you must first expand, or decompress, the files .
- By default, this will compress the given file, and create a compressed output file by appending a `.Z` extension to the input file .
- If you like to know how much compression it has done, use the verbose option: `-v` .
- Compress does not have the highest compression rate, but it is one of the fastest programs to compress data .
- Compared to gzip's fastest setting, compress is slightly slower at compression, slightly faster at decompression, and has a significantly lower compression ratio .
- While compress and gzip just compress a single file, zip is a tool that handles packaging of one or many files or directories and compression all in one go .




### Image Compression

Image compression is the process of reducing the size of an image file while maintaining its visual quality. This is achieved by removing redundant or unnecessary information from the image data. Image compression is an important aspect of data compression, as it allows for more efficient storage and transmission of image data.

There are two main types of image compression: lossless and lossy.

1. **Lossless Compression:** This type of compression reduces the size of the image file without any loss of information. The original image can be perfectly reconstructed from the compressed data. Common lossless image compression algorithms include PNG, GIF, and TIFF.

2. **Lossy Compression:** This type of compression reduces the size of the image file by discarding some information. The compressed image may not be identical to the original, but the difference is usually not noticeable to the human eye. Common lossy image compression algorithms include JPEG and WebP.

Image compression is used in a variety of applications, including digital photography, web design, and video streaming. It is an essential tool for managing and transmitting large amounts of image data.



### The Graphics Interchange Format (GIF)

- The Graphics Interchange Format (GIF) is a bitmap image format that was developed by a team at the online services provider CompuServe led by American computer scientist Steve Wilhite on June 15, 1987.
- It has since come into widespread usage on the World Wide Web due to its wide support and portability between applications and operating systems.
- The format supports up to 8 bits per pixel for each image, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space.
- It also supports animations and allows a separate palette of up to 256 colors for each frame.
- These palette limitations make GIF less suitable for reproducing color photographs and other images with color gradients, but it is well-suited for simpler images such as graphics or logos with solid areas of color.
- GIF images are compressed using the Lempel–Ziv–Welch (LZW) lossless data compression technique to reduce the file size without degrading the visual quality.
- This compression technique was patented in 1985. Controversy over the licensing agreement between the software patent holder, Unisys, and CompuServe in 1994 spurred the development of the Portable Network Graphics (PNG) standard.
- All the relevant patent licenses for GIF have now expired.



### Compression over Modems

1. Compression over modems refers to the process of reducing the size of data transmitted over a modem connection.
2. This is achieved through the use of data compression algorithms, which encode the data in a more efficient manner, reducing the number of bits required to represent the data.
3. Compression over modems is particularly useful for transmitting large files or data streams, as it can significantly reduce the time required for transmission.
4. There are several different algorithms and techniques used for compression over modems, including Huffman coding, arithmetic coding, and dictionary-based methods such as Lempel-Ziv-Welch (LZW).
5. The effectiveness of compression over modems depends on several factors, including the type of data being transmitted, the quality of the modem connection, and the specific compression algorithm used.
6. In general, compression over modems can significantly improve the efficiency of data transmission, allowing for faster and more reliable communication.




### V.42 bits for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- V.42 is an error-correcting protocol for modems.
- It was developed by the International Telecommunication Union (ITU) and is used for data transmission over telephone lines.
- V.42 uses a technique called Link Access Procedure for Modems (LAPM) to detect and correct errors in the transmitted data.
- LAPM uses a cyclic redundancy check (CRC) to detect errors in the data.
- If an error is detected, LAPM will request that the data be retransmitted.
- V.42 also includes a feature called data compression, which can reduce the amount of data that needs to be transmitted.
- This can increase the effective data transmission rate.
- V.42 is commonly used in conjunction with the V.32 and V.34 modem standards.
- V.42bis is an extension of the V.42 protocol that provides even more advanced data compression capabilities.




### Predictive Coding

Predictive coding is a method of lossless data compression that is commonly referred to as differential pulse code modulation (DPCM). A special case of this method is delta modulation (DM), which quantizes the error signal using only two quantization levels.

One example of predictive coding is Dynamic Markov compression (DMC), which is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool. It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time).

Predictive coding techniques can also be used for efficient transmission or storage of two-level (black and white) digital images. Part I of the paper "Image Data Compression by Predictive Coding" discusses algorithms for prediction.

In summary, predictive coding is a method of lossless data compression that can be used in various applications, including image data compression and transmission. It involves predicting the input data and quantizing the error signal to achieve efficient compression.



### Prediction with Partial match (ppm) for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Prediction by Partial Matching (PPM) is a statistical data compression technique that uses a context-based, adaptive model to encode data.
- PPM is based on the idea that the probability of a symbol occurring in a sequence depends on the context in which it appears.
- The context is defined as the preceding symbols in the sequence, and the length of the context is a parameter of the algorithm.
- PPM maintains a set of probability estimates for each possible symbol, given a particular context.
- As the data is encoded, the probability estimates are updated based on the observed frequencies of the symbols.
- PPM can achieve high compression ratios, particularly for text data, by exploiting the regularities and patterns in the data.
- However, the algorithm can be computationally intensive, particularly for large context sizes, and may require significant amounts of memory to store the probability estimates.
- There are several variations of the PPM algorithm, including PPM-A, PPM-B, and PPM-C, which differ in the way they handle contexts and update probability estimates.
- PPM has been widely used in text compression and has also been applied to other types of data, such as images and audio.



### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Data compression** is the process of encoding information using fewer bits than the original representation.
2. **Coding a sequence** is one of the techniques used in data compression to reduce the size of the data.
3. The basic algorithm for coding a sequence involves the following steps:
    1. Identify the symbols in the sequence and their frequencies.
    2. Assign codes to the symbols based on their frequencies, with more frequent symbols receiving shorter codes.
    3. Encode the sequence using the assigned codes.
4. There are several algorithms that can be used for coding a sequence, including Huffman coding, arithmetic coding, and run-length encoding.
5. The choice of algorithm depends on the characteristics of the data and the desired level of compression.
6. The effectiveness of the compression can be measured by the compression ratio, which is the ratio of the size of the compressed data to the size of the original data.
7. Data compression can be lossless, where the original data can be perfectly reconstructed from the compressed data, or lossy, where some information is lost during the compression process.
8. Lossless compression is typically used for text and data files, while lossy compression is often used for images, audio, and video files where some loss of quality is acceptable.




### The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The escape symbol is a special character used in data compression algorithms.
- It is used to represent a symbol that is not present in the dictionary or codebook.
- When the escape symbol is encountered, the algorithm knows to add a new symbol to the dictionary or codebook.
- This allows the algorithm to adapt to new data and improve compression efficiency.
- The escape symbol is typically represented by a unique character or sequence of characters that is not present in the data being compressed.
- It is important to choose an appropriate escape symbol to avoid conflicts with the data being compressed.
- The use of an escape symbol is common in adaptive dictionary-based compression algorithms such as LZW and LZ77.
- The escape symbol is also used in arithmetic coding to represent the end of a message or to switch between different probability models.



### Length of Context for the Notes of the Unit 3 - Coding a Sequence in the Subject of Data Compression

1. The length of context refers to the number of previous symbols in a sequence that are used to predict the next symbol.
2. In data compression, the length of context is an important parameter that can affect the performance of the compression algorithm.
3. A longer context length can result in more accurate predictions and better compression, but it also increases the complexity of the algorithm and the amount of memory required.
4. The optimal context length depends on the characteristics of the data being compressed and the specific compression algorithm being used.
5. In general, it is a trade-off between compression performance and computational resources.
6. Experimentation and analysis can help determine the best context length for a given data set and compression algorithm.



### The Exclusion Principle

The exclusion principle is a fundamental concept in data compression. It is based on the idea that certain symbols or sequences of symbols are unlikely to occur in the data being compressed. By excluding these unlikely symbols or sequences, the data can be represented using fewer bits, resulting in a more efficient compression.

Here are some key points to remember about the exclusion principle:

1. The exclusion principle is used in many different data compression algorithms, including Huffman coding and arithmetic coding.
2. The effectiveness of the exclusion principle depends on the characteristics of the data being compressed. For example, if the data contains many repeated sequences, the exclusion principle can be very effective in reducing the size of the compressed data.
3. The exclusion principle can be applied at different levels of the data. For example, it can be applied at the level of individual symbols, or at the level of sequences of symbols.
4. The exclusion principle is not always effective. In some cases, the data may not contain any unlikely symbols or sequences, and the exclusion principle will not result in any reduction in the size of the compressed data.




### The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm used in data compression. It was invented by Michael Burrows and David Wheeler in 1994. The BWT is used to transform a string of characters into a more compressible form. This is achieved by rearranging the characters in the string in a specific way.

The steps involved in the BWT are as follows:

1. Create a table of all possible cyclic rotations of the input string.
2. Sort the rows of the table in lexicographic order.
3. The last column of the sorted table is the BWT of the input string.

The BWT is reversible, meaning that the original string can be recovered from the transformed string. This is done by using the inverse BWT algorithm.

The BWT is commonly used in combination with other compression techniques, such as move-to-front coding and Huffman coding, to achieve high levels of compression.

In summary, the Burrows-Wheeler Transform is a powerful tool in data compression, allowing for the transformation of a string into a more compressible form. It is commonly used in combination with other compression techniques to achieve high levels of compression.



### Move-to-front coding

Move-to-front (MTF) coding is a type of adaptive coding technique used in data compression. It is used to transform the input sequence into a sequence that is more easily compressible. This is achieved by maintaining a list of symbols in the order of their most recent occurrence and encoding each symbol in the input sequence as the position of that symbol in the list. After encoding a symbol, the symbol is moved to the front of the list, hence the name "move-to-front" coding.

Some key points to note about MTF coding are:
- It is an adaptive coding technique, meaning that it adjusts to the data being compressed.
- It is used to transform the input sequence into a sequence that is more easily compressible.
- It maintains a list of symbols in the order of their most recent occurrence.
- Each symbol in the input sequence is encoded as the position of that symbol in the list.
- After encoding a symbol, the symbol is moved to the front of the list.

MTF coding is often used in combination with other compression techniques, such as Huffman coding or arithmetic coding, to improve the overall compression performance. It is particularly effective when the input data has a high degree of locality, meaning that symbols that have occurred recently are more likely to occur again in the near future. In such cases, MTF coding can significantly reduce the entropy of the input sequence, making it more compressible.



### CALIC for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- CALIC stands for Context-Based, Adaptive, Lossless Image Coding .
- It is an image codec that is made for obtaining a high degree of compression for continuous-tone gray-scaled images .
- It uses a single pass and self-correcting GAP (gradient adjusted predictor) to compress image efficiently and with a high compression ratio .
- CALIC obtains higher lossless compression of continuous-tone images than other techniques reported in the literature .
- This high coding efficiency is accomplished with relatively low time and space complexities .
- CALIC puts heavy emphasis on image data modeling .
- A unique feature of CALIC is the use of a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics .
- The non-linear predictor adapts via an error feedback mechanism .
- The Context Adaptive Lossless Image Compression (CALIC) scheme came into being in response to a call for proposals for a new lossless image compression scheme in 1994 .
- It uses both context and prediction of the pixel values .



### JPEG-LS

- JPEG-LS is a lossless/near-lossless compression standard for continuous-tone images.
- Its official designation is ISO-14495-1/ITU-T.87.
- It is a simple and efficient baseline algorithm which consists of two independent and distinct stages called modeling and encoding.
- The standard is based on the LOCO-I algorithm (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.
- JPEG LS was defined to address the need for effective lossless and near-lossless compression of continuous-tone still images.
- This standard can be broken into two parts: ISO/IEC 14495-1:1999 | ITU-T Rec. T.87 (1998), defining the core technology and ISO/IEC 14495-2:2003 | ITU-T Rec. T.870 (03/2002), containing the extensions.
- The ITU T.87 standard describes lossless and near-lossless compression of continuous-tone images.
- The algorithm is developed as a "low complexity implementation" of the standard universal context.



### Multi-resolution Approaches

Multi-resolution approaches are used in the coding of a sequence in the subject of data compression. These approaches allow for the representation of data at different levels of resolution or detail. Here are some key points to consider when studying multi-resolution approaches for data compression:

1. Multi-resolution approaches can be used to compress data by representing it at a lower resolution, which requires fewer bits to store.
2. These approaches can also be used to progressively transmit or display data, starting with a low-resolution version and gradually increasing the level of detail as more data is received or processed.
3. One common multi-resolution approach is the use of wavelet transforms, which can represent data at multiple levels of resolution by decomposing it into a series of coefficients.
4. Another approach is the use of hierarchical data structures, such as quad-trees or oct-trees, which can represent data at different levels of detail by subdividing it into smaller and smaller regions.
5. Multi-resolution approaches can be particularly useful for compressing data with a high level of detail or complexity, such as images or 3D models.




### Facsimile Encoding

Facsimile encoding is a technique used in data compression to encode a sequence of data. It is commonly used in fax machines to compress the data before transmission. Here are some key points to remember about facsimile encoding:

1. Facsimile encoding is a lossless compression technique, meaning that the original data can be perfectly reconstructed from the compressed data.
2. It is based on the run-length encoding (RLE) algorithm, which compresses data by replacing consecutive repeated characters with a single character and a count of the number of repetitions.
3. In facsimile encoding, the data is first converted into a binary image, where each pixel is represented by a 0 or 1.
4. The image is then divided into scan lines, and each scan line is compressed using RLE.
5. The compressed data is then transmitted over a communication channel, such as a telephone line, to the receiving fax machine.
6. The receiving fax machine decompresses the data using the inverse of the RLE algorithm and reconstructs the original image.

Facsimile encoding is an efficient and effective method for compressing data in fax transmission. It allows for fast and reliable transmission of data over communication channels.



### Dynamic Markov Compression

Dynamic Markov Compression (DMC) is a lossless data compression algorithm that uses a Markov model to predict the next symbol in a sequence based on the previous symbols. It is used in the context of coding a sequence in the subject of data compression.

Here are some key points to note about DMC:

1. DMC is an adaptive algorithm, meaning that it adjusts its model as it processes the data.
2. The Markov model used by DMC is a probabilistic model that predicts the probability of the next symbol based on the previous symbols.
3. DMC uses arithmetic coding to encode the data based on the probabilities predicted by the Markov model.
4. The algorithm can achieve high compression ratios, especially for data with strong correlations between symbols.
5. DMC is a relatively complex algorithm and can be slower than other compression algorithms.




## Unit 4 - Distortion criteria

Distortion criteria are used to evaluate the performance of communication systems. They are used to measure the quality of the transmitted signal and the effectiveness of the communication system. There are several types of distortion criteria, including:

1. **Signal-to-Noise Ratio (SNR):** This is the ratio of the signal power to the noise power. A higher SNR indicates a better quality signal.

2. **Mean Squared Error (MSE):** This is the average of the squared differences between the original signal and the received signal. A lower MSE indicates a better quality signal.

3. **Peak Signal-to-Noise Ratio (PSNR):** This is the ratio of the maximum signal power to the noise power. A higher PSNR indicates a better quality signal.

4. **Bit Error Rate (BER):** This is the ratio of the number of bit errors to the total number of bits transmitted. A lower BER indicates a better quality signal.

These are some of the most commonly used distortion criteria in communication systems. They are used to evaluate the performance of the system and to make improvements to the system to achieve better quality communication.



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

1. Distortion criteria is a measure of the difference between the original and reconstructed data.
2. It is used to evaluate the performance of data compression algorithms.
3. There are several models for distortion criteria, including mean squared error, peak signal-to-noise ratio, and structural similarity index.
4. Mean squared error measures the average of the squared difference between the original and reconstructed data.
5. Peak signal-to-noise ratio measures the ratio between the maximum possible power of a signal and the power of the noise that affects the fidelity of its representation.
6. Structural similarity index measures the similarity between two images by taking into account the luminance, contrast, and structure of the images.
7. The choice of distortion criteria depends on the specific application and the type of data being compressed.
8. In general, a lower value of distortion criteria indicates better performance of the data compression algorithm.




### Scalar Quantization

Scalar quantization is a process of mapping a continuous amplitude signal to a discrete amplitude signal. This is done by dividing the range of the signal into a finite number of intervals, called quantization levels, and assigning a discrete value to each interval. The process of assigning a discrete value to each interval is called quantization.

In the context of data compression, scalar quantization is used to reduce the number of bits required to represent a signal. This is achieved by reducing the number of possible amplitude values that the signal can take, which in turn reduces the number of bits required to represent each sample of the signal.

The performance of a scalar quantizer is typically measured in terms of its distortion, which is the difference between the original signal and the quantized signal. There are several distortion criteria that can be used to measure the performance of a scalar quantizer, including mean squared error, maximum absolute error, and signal-to-noise ratio.

In summary, scalar quantization is a process of mapping a continuous amplitude signal to a discrete amplitude signal in order to reduce the number of bits required to represent the signal. The performance of a scalar quantizer is typically measured in terms of its distortion, which can be evaluated using several different criteria.



### The Quantization problem for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

1. Quantization is the process of mapping a large set of input values to a smaller set of output values.
2. The quantization problem arises when trying to represent a continuous signal with a finite number of bits.
3. The goal of quantization is to minimize the distortion between the original signal and the quantized signal.
4. Distortion is the difference between the original signal and the quantized signal.
5. Distortion criteria are used to measure the quality of the quantization process.
6. Common distortion criteria include mean squared error, signal-to-noise ratio, and maximum error.
7. The choice of distortion criteria depends on the application and the characteristics of the signal being quantized.
8. The quantization problem can be solved using various techniques, including uniform quantization, non-uniform quantization, and vector quantization.
9. The choice of quantization technique depends on the characteristics of the signal and the desired trade-off between complexity and performance.
10. The quantization problem is an important topic in the field of data compression, as it is a key step in the process of compressing continuous signals.



### Uniform Quantizer

A uniform quantizer is a type of quantizer that maps a continuous range of input values to a finite set of output values. It is called uniform because the size of the quantization step is the same for all input values. This type of quantizer is commonly used in data compression and signal processing.

Some key points to remember about uniform quantizers are:

1. The quantization step size is constant for all input values.
2. The quantization error is the difference between the input value and the quantized output value.
3. The quantization error is minimized when the input values are uniformly distributed over the range of the quantizer.
4. The number of output values is determined by the number of bits used to represent the quantized values.
5. The uniform quantizer is simple to implement and is commonly used in practice.




### Adaptive Quantization for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Adaptive Quantization is a technique used in data compression to improve coding efficiency.
- In forward adaptive quantization, the input is divided into blocks and the quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information.
- The backward adaptive quantization used in DPCM systems is basically a variation of the backward adaptive Jayant quantizer described in Chapter 9. In Chapter 9, the Jayant algorithm was used to adapt the quantizer to a stationary input. In DPCM, the algorithm is used to adapt the quantizer to the local behavior of nonstationary inputs.
- In a forward adaptive quantization scheme, we would obtain the minimum and maximum values for each block of data, which would be transmitted as side information.
- Concerning adaptive compression, two types of dynamic bit allocation are often applied. First, many approaches allow spatially, content-aware bit allocation, e.g., with a region of interest (ROI) or importance map. Second, rate adaptation is performed to adjust the bitrate during inference with a single trained model and move the operating point along the rate-distortion (RD) curve.
- One of the most powerful solutions is the Moving Picture Experts Group geometry-based point cloud compression (G-PCC) emerging standard. In the G-PCC lifting transform coding technique, an adaptive quantization method is used to improve the coding efficiency.



### Non-uniform Quantization

- Non-uniform quantization is a type of quantization used in data compression where the quantization levels are not equally spaced.
- This method is used when the signal being quantized has a non-uniform probability density function.
- In non-uniform quantization, the quantization levels are spaced closer together in regions where the signal is more likely to occur and further apart in regions where the signal is less likely to occur.
- This results in lower distortion for the same number of quantization levels compared to uniform quantization.
- Non-uniform quantization can be achieved using a variety of methods, including companding and using a non-uniform quantizer.
- Companding is a technique where the signal is compressed before quantization and expanded after quantization.
- A non-uniform quantizer is a quantizer that has non-uniformly spaced quantization levels.
- Non-uniform quantization is commonly used in speech and audio coding, where the human ear is more sensitive to certain frequencies than others.
- In these applications, the quantization levels are spaced closer together in the frequency bands where the ear is more sensitive and further apart in the frequency bands where the ear is less sensitive.
- This results in lower perceived distortion for the same number of quantization levels compared to uniform quantization.



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization
Vector quantization (VQ) is a technique used in signal processing and data compression that involves the quantization of vectors in a multi-dimensional space. This is in contrast to scalar quantization, which involves the quantization of individual scalar values. There are several advantages of using vector quantization over scalar quantization, including:

1. **Improved performance**: Vector quantization can achieve better performance than scalar quantization in terms of signal-to-noise ratio (SNR) and mean squared error (MSE). This is because VQ takes into account the correlation between the components of the vector, whereas scalar quantization treats each component independently.

2. **Reduced bit rate**: Vector quantization can achieve a lower bit rate than scalar quantization for a given level of distortion. This is because VQ can exploit the correlation between the components of the vector to reduce the number of bits required to represent the vector.

3. **Efficient representation**: Vector quantization can provide a more efficient representation of the data than scalar quantization. This is because VQ can represent the data using a smaller number of code vectors, which can result in a more compact representation of the data.

4. **Adaptability**: Vector quantization can be adapted to the characteristics of the data, whereas scalar quantization is typically fixed. This means that VQ can be tailored to the specific characteristics of the data, which can result in improved performance.

Overall, vector quantization offers several advantages over scalar quantization, including improved performance, reduced bit rate, efficient representation, and adaptability. These advantages make VQ a powerful tool for signal processing and data compression.



### The Linde-Buzo-Gray Algorithm for the notes of the Unit 5 - Advantages of Vector Quantization over Scalar Quantization in the subject of Data Compression

- The Linde-Buzo-Gray algorithm (LBG) is a vector quantization algorithm that was introduced by Yoseph Linde, Andrés Buzo, and Robert M. Gray in 1980.
- The LBG algorithm is used to derive a good codebook and is similar to the k-means method in data clustering.
- Vector quantization (VQ) is an effective means of data compression as it maps a set of real numbers into a single integer.
- One advantage of vector quantization over scalar quantization is that it can lower the average distortion with the number of reconstruction levels held constant.
- Another advantage is that vector quantization can reduce the number of reconstruction levels when distortion is held constant.
- The LBG algorithm has been used with vector quantization for compressing images and has resulted in decent image quality when compared with other existing approaches.



### Tree structured Vector Quantizers

Tree structured vector quantizers (TSVQ) are a type of vector quantizer that uses a tree structure to organize the codebook. This allows for faster encoding and decoding compared to a full-search vector quantizer. TSVQs are commonly used in image and speech compression.

Advantages of Vector Quantization over Scalar Quantization:

1. Vector quantization can achieve higher compression ratios than scalar quantization by exploiting the correlation between adjacent samples.
2. Vector quantization can produce higher quality reconstructed signals than scalar quantization, as it takes into account the correlation between adjacent samples.
3. Vector quantization can be used to compress multi-dimensional data, while scalar quantization is limited to one-dimensional data.
4. Vector quantization can be used to compress data with non-uniform probability distributions, while scalar quantization is best suited for data with uniform probability distributions.
5. Vector quantization can be used to compress data with non-stationary statistics, while scalar quantization is best suited for data with stationary statistics.



### Structured Vector Quantizers

Vector quantization is a technique used in data compression to reduce the amount of data needed to represent a signal. It is a lossy compression technique, meaning that some information is lost in the process of compressing the data. However, the loss of information is usually small and not noticeable to the human eye or ear.

One of the advantages of vector quantization over scalar quantization is that it can achieve higher compression ratios. This is because vector quantization takes into account the correlation between adjacent samples in the signal, whereas scalar quantization treats each sample independently.

Another advantage of vector quantization is that it can produce higher quality reconstructed signals. This is because the quantization error is spread over multiple samples, rather than being concentrated in a single sample as in scalar quantization.

Structured vector quantizers are a type of vector quantizer that use a predefined structure to represent the codebook. This structure can be a tree, a lattice, or a product code. The advantage of using a structured vector quantizer is that it can reduce the complexity of the encoding and decoding process, making it faster and more efficient.

In summary, vector quantization has several advantages over scalar quantization, including higher compression ratios and higher quality reconstructed signals. Structured vector quantizers can further improve the efficiency of the encoding and decoding process. These advantages make vector quantization a popular choice for data compression in many applications.

