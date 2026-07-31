

## Unit 1 - Compression Techniques

Compression techniques are used to reduce the size of data files, making them easier to store and transmit. There are two main types of compression techniques: lossless and lossy.

1. **Lossless Compression**: This type of compression reduces the size of the data file without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression techniques include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This type of compression reduces the size of the data file by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression techniques include JPEG for images and MP3 for audio.

Compression techniques are widely used in many applications, including data storage, data transmission, and multimedia. They help to save storage space, reduce transmission time, and improve the efficiency of data processing.



### Lossless Compression

Lossless compression is a class of data compression algorithms that allows the original data to be perfectly reconstructed from the compressed data. This is possible because most real-world data exhibits statistical redundancy. Lossless compression “packs” data into a smaller file size by using a kind of internal shorthand to signify redundant data.

Some examples of lossless compression methods include:
- Run Length Encoding (RLE)
- String-table compression
- Lempel Ziff Welch (LZW)
- zlib

Lossless compression is different from lossy compression, which reduces file size by discarding less important information. Lossless compression describes data in a different way that takes up less memory, without losing any information.



### Lossy Compression

Lossy compression is a type of data compression technique that reduces the size of the original data by discarding some of the information. This technique is used when the exact reproduction of the original data is not necessary, and some loss of quality is acceptable.

Some key points to remember about lossy compression are:

1. Lossy compression is used for compressing multimedia data such as audio, video, and images.
2. The main advantage of lossy compression is that it can achieve a much higher compression ratio than lossless compression.
3. The disadvantage of lossy compression is that the quality of the compressed data is lower than the original data.
4. The amount of data loss and the resulting quality of the compressed data can be controlled by adjusting the compression parameters.
5. Common lossy compression techniques include JPEG for images, MP3 for audio, and MPEG for video.




### Measures of Performance for Compression Techniques

1. Compression Ratio: The ratio of the size of the compressed data to the size of the original data.
2. Space Savings: The percentage of space saved by compressing the data.
3. Bit Rate: The number of bits per second required to represent the compressed data.
4. Encoding Time: The time required to compress the data.
5. Decoding Time: The time required to decompress the data.
6. Distortion: The difference between the original data and the data after compression and decompression.
7. Fidelity: The degree to which the compressed and decompressed data is similar to the original data.
8. Robustness: The ability of the compression technique to handle errors or changes in the data.




### Unit 1 - Compression Techniques

#### Modeling and coding

1. **Modeling** is the process of constructing a statistical model of the data to be compressed. This model is used to predict the probability of each symbol in the data, which is then used to assign shorter codes to more probable symbols and longer codes to less probable symbols.

2. **Coding** is the process of assigning codes to the symbols in the data based on their probabilities. There are two main types of coding techniques: entropy coding and dictionary coding.

3. **Entropy coding** techniques, such as Huffman coding and arithmetic coding, assign codes to symbols based on their probabilities. Symbols with higher probabilities are assigned shorter codes, while symbols with lower probabilities are assigned longer codes.

4. **Dictionary coding** techniques, such as Lempel-Ziv-Welch (LZW) and Deflate, use a dictionary to encode common substrings in the data. The dictionary is built dynamically during the encoding process, and common substrings are replaced with shorter codes that reference the dictionary.

5. Both modeling and coding are essential components of data compression, and the effectiveness of a compression algorithm depends on the quality of the model and the efficiency of the coding technique used.



### Mathematical Preliminaries for Lossless Compression

Lossless compression is a technique used to reduce the size of data without losing any information. In order to understand the principles behind lossless compression, it is important to have a basic understanding of some mathematical concepts. Here are some key mathematical preliminaries for lossless compression:

1. **Information Theory:** This is a branch of mathematics that deals with the representation, storage, and transmission of information. It is the foundation of data compression techniques.

2. **Entropy:** In information theory, entropy is a measure of the uncertainty associated with a random variable. It is used to quantify the amount of information contained in a message.

3. **Redundancy:** Redundancy refers to the presence of unnecessary or repetitive information in data. Lossless compression techniques aim to remove this redundancy to reduce the size of the data.

4. **Probability:** Probability is the measure of the likelihood of an event occurring. It is used to calculate the entropy of a message and to design efficient compression algorithms.

5. **Huffman Coding:** This is a lossless data compression algorithm that assigns variable-length codes to input symbols based on their probabilities of occurrence. It is widely used in lossless compression techniques.

6. **Arithmetic Coding:** This is another lossless data compression algorithm that encodes data by representing it as a range of real numbers between 0 and 1. It is more efficient than Huffman coding for certain types of data.

These are some of the key mathematical concepts that are important for understanding lossless compression techniques. By having a good grasp of these concepts, one can better understand the principles behind lossless compression and how it can be used to reduce the size of data without losing any information.



### A brief introduction to information theory for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

Information theory is a branch of mathematics that deals with the representation, storage, and transmission of information. It was first introduced by Claude Shannon in 1948, in his paper "A Mathematical Theory of Communication."

Some key concepts in information theory include:

1. **Entropy:** This measures the amount of uncertainty or randomness in a system. In the context of information theory, it is used to quantify the amount of information contained in a message.

2. **Redundancy:** This refers to the presence of unnecessary or repetitive information in a message. Reducing redundancy can help to compress data and make it more efficient to store or transmit.

3. **Data Compression:** This is the process of reducing the size of a data file by removing redundancy and encoding the information in a more efficient manner.

4. **Error Correction:** This involves adding extra information to a message to allow for the detection and correction of errors that may occur during transmission.

Information theory has many applications, including in the fields of telecommunications, data storage, and data compression. It provides a mathematical framework for understanding how information can be efficiently represented, stored, and transmitted. In the context of data compression, information theory can be used to develop algorithms for reducing the size of data files while maintaining the integrity of the information they contain.



### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression algorithms include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression algorithms include JPEG for images and MP3 for audio.

3. **Run-Length Encoding (RLE)**: This is a simple form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

4. **Dictionary-based Compression**: This is a lossless data compression technique that uses a dictionary to encode data. The dictionary is built based on the data being compressed and is used to encode the data in a more compact form. Examples of dictionary-based compression algorithms include LZW and DEFLATE.

5. **Transform-based Compression**: This is a lossy data compression technique that transforms the data into a different representation, making it easier to compress. Examples of transform-based compression algorithms include the Discrete Cosine Transform (DCT) used in JPEG and the Modified Discrete Cosine Transform (MDCT) used in MP3.

6. **Hybrid Compression**: This is a combination of lossless and lossy compression techniques. The data is first compressed using a lossless technique, and then further compressed using a lossy technique. This can result in higher compression ratios than using either technique alone.



### Physical models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples include Huffman coding and arithmetic coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples include JPEG and MP3.

3. **Run-Length Encoding**: This technique compresses data by replacing consecutive occurrences of the same symbol with a single occurrence of the symbol followed by the number of occurrences. For example, the string "AAAABBBCC" would be compressed to "A4B3C2".

4. **Dictionary-based Compression**: This technique compresses data by replacing common substrings with shorter codes. The codes and their corresponding substrings are stored in a dictionary. Examples include LZW and LZ77.

5. **Transform-based Compression**: This technique compresses data by transforming it into a different representation that is more easily compressible. Examples include the Discrete Cosine Transform (DCT) used in JPEG and the Discrete Wavelet Transform (DWT) used in JPEG 2000.

6. **Hybrid Compression**: This technique combines two or more of the above techniques to achieve better compression. Examples include the use of Huffman coding with DCT in JPEG and the use of arithmetic coding with DWT in JPEG 2000.



### Probability Models for Unit 1 - Compression Techniques in Data Compression

1. Probability models are used in data compression to predict the likelihood of occurrence of different symbols in the data.
2. These models are used to assign shorter codes to more frequently occurring symbols and longer codes to less frequently occurring symbols, resulting in a more efficient compression.
3. There are several types of probability models used in data compression, including:
    - **Uniform probability model**: Assumes that all symbols have an equal probability of occurrence.
    - **Empirical probability model**: Estimates the probability of occurrence of each symbol based on its frequency in the data.
    - **Markov model**: Takes into account the dependencies between symbols and predicts the probability of a symbol based on the previous symbols.
4. The choice of probability model depends on the characteristics of the data being compressed and the desired level of compression.
5. Probability models can be static, where the probabilities are fixed, or adaptive, where the probabilities are updated as the data is compressed.
6. The use of probability models in data compression can significantly improve the compression ratio and reduce the size of the compressed data.



### Markov Models

Markov models are a type of mathematical model used in the field of data compression. They are named after the Russian mathematician Andrey Markov, who developed the theory of Markov chains.

A Markov model is a type of statistical model that represents systems that change over time. It is used to predict the future state of a system based on its current state and past history.

In the context of data compression, Markov models are used to predict the probability of a symbol occurring in a data stream based on the previous symbols that have occurred. This information can then be used to compress the data by encoding the symbols with fewer bits if they are more likely to occur.

Some key points to remember about Markov models in the context of data compression are:

1. Markov models are used to predict the probability of a symbol occurring in a data stream based on the previous symbols that have occurred.
2. This information can be used to compress the data by encoding the symbols with fewer bits if they are more likely to occur.
3. Markov models are named after the Russian mathematician Andrey Markov, who developed the theory of Markov chains.
4. Markov models are a type of statistical model that represents systems that change over time.




### Composite Source Model

A composite source model is used in data compression when it is not simple to use a single model to describe the source in many applications. It uses only one source.

A composite source can be represented as a number of individual sources S i, each with its own model M i and a switch that selects a source S i with probability P i. This is an exceptionally rich model and can be used to describe some very complicated processes.



### Unit 1 - Compression Techniques

Data compression is the process of encoding information using fewer bits than the original representation. This is achieved through the use of various compression techniques. In this unit, we will discuss some of the most commonly used compression techniques.

1. **Lossless Compression:** Lossless compression techniques reduce the size of the data without losing any information. This means that the original data can be perfectly reconstructed from the compressed data. Some common lossless compression techniques include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression:** Lossy compression techniques reduce the size of the data by discarding some information. This means that the original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Some common lossy compression techniques include JPEG for images and MP3 for audio.

3. **Run-Length Encoding (RLE):** RLE is a simple lossless compression technique that is used to compress data with long runs of the same value. It works by replacing the long runs with a shorter representation that consists of the value and the number of times it is repeated.

4. **Dictionary-based Compression:** Dictionary-based compression techniques, such as LZW, work by replacing common substrings in the data with shorter codes. These codes are stored in a dictionary, which is used to decode the compressed data.

These are some of the most commonly used compression techniques. Each technique has its own strengths and weaknesses, and the choice of technique depends on the specific requirements of the data being compressed. It is important to understand these techniques in order to make informed decisions when compressing data.



### Uniquely Decodable Codes

Uniquely decodable codes are a type of variable-length code used in data compression techniques. These codes are designed to ensure that the original message can be recovered exactly from the encoded message, without any ambiguity.

Here are some key points to remember about uniquely decodable codes:

1. Uniquely decodable codes are a type of prefix code, meaning that no codeword is a prefix of another codeword. This property ensures that the encoded message can be uniquely decoded.

2. Huffman coding is a commonly used method for constructing uniquely decodable codes. This method assigns shorter codewords to more frequently occurring symbols, resulting in a more efficient code.

3. Uniquely decodable codes are not always optimal in terms of compression efficiency. In some cases, other types of codes, such as arithmetic coding, may provide better compression.

4. The Kraft-McMillan inequality provides a necessary and sufficient condition for the existence of a uniquely decodable code for a given set of symbol probabilities.




### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Definition**: A prefix code is a type of code system used for lossless data compression. It is also known as a prefix-free code or instantaneous code.
2. **Properties**: A prefix code has the property that no codeword is a prefix of another codeword. This means that the code can be decoded unambiguously and instantly.
3. **Examples**: Some examples of prefix codes include Huffman coding and Shannon-Fano coding.
4. **Usage**: Prefix codes are commonly used in data compression algorithms to reduce the size of data without losing any information.
5. **Advantages**: The use of prefix codes in data compression can result in significant savings in storage space and transmission time.
6. **Disadvantages**: The main disadvantage of prefix codes is that they can be less efficient than other types of codes for certain types of data.



## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a lossless data compression algorithm that was developed by David A. Huffman in 1952. It is a variable-length coding algorithm that assigns shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters. The algorithm works as follows:

1. The frequency of each character in the data is determined.
2. A binary tree is constructed with the characters as leaves, where the weight of each leaf is the frequency of the corresponding character.
3. The tree is constructed in such a way that the weight of each non-leaf node is the sum of the weights of its children.
4. The code for each character is determined by traversing the tree from the root to the leaf corresponding to that character, where going left corresponds to a 0 and going right corresponds to a 1.

The Huffman coding algorithm is widely used in data compression, including in file formats such as ZIP and GZIP. It is also used in image and video compression standards such as JPEG and MPEG.



### Minimum variance Huffman codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Minimum variance Huffman codes are a type of Huffman code that aim to minimize the variance of the codeword lengths.
- This is achieved by assigning shorter codewords to symbols with higher probabilities and longer codewords to symbols with lower probabilities.
- The Huffman coding algorithm is used to generate these codes.
- The algorithm works by constructing a binary tree where the leaves represent the symbols and the internal nodes represent the codewords.
- The tree is constructed by repeatedly merging the two nodes with the lowest probabilities until only one node remains.
- The codewords are then assigned by traversing the tree from the root to the leaves, assigning a 0 to the left branch and a 1 to the right branch at each internal node.
- The resulting codes have the property that no codeword is a prefix of another codeword, which is known as the prefix property.
- This property ensures that the codes can be uniquely decoded.
- Minimum variance Huffman codes can be used in data compression to reduce the size of the compressed data while maintaining a low variance in the codeword lengths, which can improve the efficiency of the decoding process.




### Adaptive Huffman coding

Adaptive Huffman coding, also known as Dynamic Huffman coding, is an adaptive coding technique based on Huffman coding. It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data .

- It is a near-minimal variable-length character coding that changes based on the frequency of characters processed. As characters are processed, frequencies are updated and codes are changed (or, the coding tree is modified) .

- The implementation is done using Vitter Algorithm. For example, when encoding a string containing alphabets, let m be the total number of alphabets (m = 26). For Vitter Algorithm, find parameters e & r such that .

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes based on the frequencies of input characters. In order to determine what code to assign to each character, a binary tree is built that will organize the characters based on frequency .



### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Review the current notes for Unit 2 - The Huffman coding algorithm in the subject of Data Compression.
2. Identify any outdated or incorrect information in the current notes.
3. Research the latest developments and advancements in the field of Huffman coding algorithm and data compression.
4. Update the notes with the latest and most accurate information.
5. Verify the accuracy and relevance of the updated information.
6. Organize the updated information in a clear and concise manner.
7. Review the updated notes for completeness and coherence.
8. Make any necessary revisions to the updated notes.
9. Finalize the updated notes for Unit 2 - The Huffman coding algorithm in the subject of Data Compression.
10. Distribute the updated notes to the relevant parties.



### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

The Huffman coding algorithm is a lossless data compression algorithm that is used to compress data without losing any information. The algorithm works by assigning shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters. The steps involved in the encoding procedure are as follows:

1. Determine the frequency of each character in the data to be compressed.
2. Create a priority queue with the characters as nodes and their frequencies as the key.
3. While there is more than one node in the queue:
    a. Remove the two nodes with the lowest frequency from the queue.
    b. Create a new internal node with the two removed nodes as children and the sum of their frequencies as the key.
    c. Add the new internal node to the queue.
4. The remaining node in the queue is the root of the Huffman tree.
5. Assign codes to the characters by traversing the tree from the root to the leaves. The code for a character is the sequence of left (0) and right (1) edges traversed to reach the leaf node representing the character.
6. Encode the data by replacing each character with its code.

This is the basic procedure for encoding data using the Huffman coding algorithm. It is an efficient and effective way to compress data without losing any information.



### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Huffman coding is a lossless data compression algorithm.
2. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
3. The most frequent character gets the smallest code and the least frequent character gets the largest code.
4. The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
5. Let us understand the algorithm with an example:

    - Consider the string `ABRACADABRA`. The frequencies of characters in the string are:

        ```
        A - 5
        B - 2
        R - 2
        C - 1
        D - 1
        ```

    - The Huffman tree for the given string is as follows:

        ```
              /\  
             /  \  
            A    /\  
                /  \  
               R   /\  
                  /  \  
                 B   /\  
                    /  \  
                   C   D
        ```

    - The codes for the characters are as follows:

        ```
        A - 0
        B - 100
        R - 101
        C - 1100
        D - 1101
        ```

    - The encoded bitstream for the given string is `0100100110101100101000`.
    - To decode the bitstream, we start from the root of the Huffman tree and move left if the current bit is 0 and move right if the current bit is 1. When we reach a leaf node, we print the character and start from the root again. For the given bitstream, the decoded string is `ABRACADABRA`.

6. The time complexity of the Huffman coding algorithm is O(nlogn) where n is the number of unique characters in the input string.
7. Huffman coding is widely used in data compression applications such as file compression and image compression.



### Golomb codes

Golomb codes are a form of parameterized coding in which integers to be coded are stored as values relative to a constant b. The coding of a positive number x is represented in two parts:

1. The first part is an unary representation of q+1, where q is the quotient floor((x/b)).
2. The second part is a special binary representation of the remainder r = x-qb. Note that there are b potential remainders.

Golomb codes divide all index values i into equal-sized groups of size m. The codeword is then constructed from a unary code that characterizes each group, followed by a fixed-length code that specifies the remainder of the index that has been encoded.

Golomb coding uses a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder. The quotient is sent in unary coding, followed by the remainder in truncated binary encoding.

For example, for a source x with geometric distribution, with parameter p(0) = 0.2, using Golomb code with M = 3. The 2-bit code 00 is used 20% of the time; the 3-bit codes 010, 011, and 100 are used over 38% of the time; 4 bits or more are needed in a minority of cases.



### Rice codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Rice codes are a type of prefix code used for lossless data compression.
- They are a simplified form of Golomb codes, which are optimal for alphabets following a geometric distribution.
- Rice codes are commonly used in applications where the distribution of the data being encoded is not known in advance, but is expected to be geometric.
- Rice codes are particularly well-suited for encoding small, positive integers.
- The encoding process involves dividing the integer to be encoded by a parameter `m`, and then encoding the quotient using unary coding and the remainder using binary coding.
- The choice of the parameter `m` affects the efficiency of the encoding. A good choice of `m` is one that is close to the median of the data being encoded.
- Rice codes can be decoded using a simple algorithm that involves reading the unary-coded quotient, multiplying it by `m`, and then adding the binary-coded remainder.
- Rice codes are used in a variety of applications, including image and audio compression, and are commonly used in conjunction with other compression techniques such as Huffman coding.



### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall coding is a form of entropy coding used for lossless data compression .
- It was the subject of Brian Parker Tunstall's PhD thesis in 1967, while at Georgia Institute of Technology. The subject of that thesis was "Synthesis of noiseless compression codes" .
- Huffman coding is another algorithm used for lossless data compression .
- It was developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes" .
- The idea behind Huffman coding is to assign variable-length codes to input characters, with the lengths of the assigned codes based on the frequencies of the corresponding characters .




### Applications of Huffman coding

Huffman coding is a lossless data compression algorithm that is widely used in various applications. Some of the applications of Huffman coding are:

1. **File Compression:** Huffman coding is used to compress files such as text, image, audio, and video files. It reduces the size of the file without losing any information, making it easier to store and transmit.

2. **Data Transmission:** Huffman coding is used in data transmission to reduce the amount of data that needs to be transmitted. It is used in various communication systems such as telecommunication, computer networks, and satellite communication.

3. **Error Correction:** Huffman coding is used in error correction to detect and correct errors that may occur during data transmission. It is used in various error correction techniques such as forward error correction and error correction codes.

4. **Image Compression:** Huffman coding is used in image compression to reduce the size of the image without losing any information. It is used in various image compression standards such as JPEG and PNG.

5. **Text Compression:** Huffman coding is used in text compression to reduce the size of the text without losing any information. It is used in various text compression techniques such as dictionary-based compression and statistical compression.

6. **Video Compression:** Huffman coding is used in video compression to reduce the size of the video without losing any information. It is used in various video compression standards such as MPEG and H.264.

These are some of the applications of Huffman coding. It is a widely used algorithm in the field of data compression and has many practical uses.



### Lossless Image Compression

Lossless image compression is a method of reducing the size of an image file without any loss of information. This means that the original image can be perfectly reconstructed from the compressed file. One of the algorithms used for lossless image compression is the Huffman coding algorithm.

#### The Huffman Coding Algorithm

The Huffman coding algorithm is a well-recognized lossless entropy coding algorithm. It removes redundant codes from the image and compresses it, especially for grayscale images. The compressed image can be successfully reconstructed and is an exact representation of the original because it is a lossless compression technique.

A hybrid prediction lossless image compression algorithm has been proposed by combining predictive Differential Pulse Code Modulation (DPCM) and Integer Wavelet Transform (IWT). It has been shown that the best hybrid predictive algorithm is the sequence of DPCM-IWT-Huffman, which has reduced bit sizes by 36%, 48%, 34%, and 13% for tested images of Lena, Cameraman, Pepper, and Baboon, respectively.



### Text Compression - Unit 2: The Huffman Coding Algorithm

Text compression is the process of reducing the size of a text file without losing any information. One of the most popular and effective text compression algorithms is the Huffman coding algorithm.

The Huffman coding algorithm is an entropy encoding algorithm used for lossless data compression. It was developed by David A. Huffman in 1952.

The algorithm works by assigning variable-length codes to input characters, based on the frequencies of their occurrence. The most frequent character is assigned the shortest code and the least frequent character is assigned the longest code.

The steps involved in the Huffman coding algorithm are as follows:

1. Create a frequency table of the characters in the input text.
2. Build a binary tree where each leaf node represents a character and its frequency.
3. Traverse the tree from the root to each leaf node and assign a binary code to each character based on the path taken.
4. Replace each character in the input text with its corresponding binary code.

The Huffman coding algorithm is a greedy algorithm, meaning it makes the locally optimal choice at each step. It is also an example of a variable-length code, where the length of the code for each character varies based on its frequency.

Huffman coding is widely used in data compression, including in popular file formats such as ZIP and GZIP. It is also used in image and video compression standards such as JPEG and MPEG.

In summary, the Huffman coding algorithm is an effective and widely used text compression algorithm that assigns variable-length codes to input characters based on their frequencies, resulting in a smaller compressed file size.



### Audio Compression

Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. The Huffman compression algorithm is named after its inventor, David Huffman, formerly a professor at MIT.
2. Huffman compression is a lossless compression algorithm that is ideal for compressing text or program files.
3. This probably explains why it is used a lot in compression programs like ZIP or ARJ.
4. One algorithm that can be used is Huffman, with the development of its algorithm is called Huffman Shift Coding.
5. Huffman Shift Coding able to change any symbol held on audio data either lossy or lossless.
6. Huffman Shift Coding method that has been tested, average compression ratio −50% above.
7. Efficient compression can be achieved by the Huffman coding at low bit-rate transmission.
8. The proposed method is seen to possess a better frequency characteristic and a simpler processing algorithm than MPEG-1 audio.
9. In practice, Huffman coding is widely used in many applications.
10. For example, it is used in "ZIP" style file compression formats, *.jpeg and *.png image formats, and *.mp3 audio files.
11. There are several types of entropy coding. Some of the commonly used ones are Huffman coding, Arithmetic coding and Rice coding.
12. For our coder, we have used Huffman entropy coding.



## Unit 3 - Coding a sequence

1. A sequence is an ordered list of elements, typically numbers or characters.
2. Sequences can be represented in code using data structures such as arrays or lists.
3. To create a sequence in code, you can use a loop to iterate over a range of values and add each value to the sequence.
4. For example, to create a sequence of the first 10 even numbers in Python, you could use the following code:
```
even_numbers = []
for i in range(1, 11):
    even_numbers.append(i * 2)
```
5. Sequences can also be generated using functions or methods, such as the `range` function in Python or the `arange` function in NumPy.
6. Once a sequence is created, you can access its elements using indexing or slicing.
7. You can also perform operations on sequences, such as sorting, reversing, or finding the sum or average of the elements.
8. It is important to choose the appropriate data structure and algorithms when working with sequences to ensure efficient and effective code.



### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. A binary code is a way of representing data using only two symbols, typically 0 and 1.
2. In the context of data compression, binary codes can be used to encode the symbols in a sequence in a more efficient manner.
3. One approach to generating a binary code for a sequence is to use a variable-length code, where the length of the code for each symbol is determined by the frequency of that symbol in the sequence.
4. Huffman coding is a commonly used algorithm for generating an optimal variable-length binary code for a sequence.
5. The Huffman coding algorithm involves building a binary tree where the leaves represent the symbols in the sequence and the path from the root to a leaf represents the binary code for that symbol.
6. The tree is constructed in such a way that the most frequent symbols have the shortest codes, resulting in a more efficient encoding of the sequence.
7. Once the binary tree is constructed, the binary code for each symbol can be obtained by traversing the tree from the root to the leaf representing that symbol, recording a 0 for each left branch taken and a 1 for each right branch taken.
8. The resulting binary code can then be used to encode the sequence, with each symbol being replaced by its corresponding binary code.



### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Binary coding** is a method of representing data using a fixed number of bits for each symbol, regardless of its frequency in the data. This means that each symbol is assigned a unique binary code of the same length.

2. **Huffman coding**, on the other hand, is an entropy encoding algorithm that assigns variable-length codes to symbols based on their frequency in the data. This means that more frequent symbols are assigned shorter codes, while less frequent symbols are assigned longer codes.

3. The main advantage of Huffman coding over binary coding is that it can achieve better compression ratios, especially for data with highly skewed symbol distributions. This is because Huffman coding takes advantage of the fact that some symbols are more frequent than others and assigns them shorter codes, which reduces the overall size of the encoded data.

4. However, Huffman coding has some disadvantages as well. For example, it requires additional information to be stored or transmitted along with the encoded data, such as the Huffman tree or code table, which can increase the overhead. Additionally, Huffman coding can be more computationally intensive than binary coding, as it requires the construction of the Huffman tree and the assignment of codes to symbols.

5. In summary, the choice between binary and Huffman coding depends on the characteristics of the data being compressed and the requirements of the application. Huffman coding can achieve better compression ratios for data with highly skewed symbol distributions, but it may have higher overhead and computational complexity than binary coding. It is important to carefully evaluate the trade-offs between these two methods when choosing a coding algorithm for data compression.



### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Data storage**: Data compression techniques can be used to reduce the amount of storage space required for a given file or set of files.
2. **Data transmission**: Compressed data can be transmitted more quickly and efficiently over a network or the internet, reducing the time and bandwidth required for data transfer.
3. **Image and video processing**: Image and video files can be compressed to reduce their size without significantly affecting their visual quality, making them easier to store and transmit.
4. **Audio processing**: Audio files can also be compressed to reduce their size, allowing for more efficient storage and transmission of audio data.
5. **Database management**: Data compression techniques can be used to reduce the size of database records, allowing for more efficient storage and retrieval of data.




### Bi-level image compression-The JBIG standard

- JBIG is an early lossless image compression standard from the Joint Bi-level Image Experts Group.
- It was standardized as ISO/IEC standard 11544 and as ITU-T recommendation T.82 in March 1993 .
- JBIG is widely implemented in fax machines .
- JBIG is also known as JBIG1, now that the newer bi-level image compression standard JBIG2 has been released .
- JBIG was designed for compression of binary images, particularly for faxes, but can also be used on other images .
- In most situations, JBIG offers between a 20% and 50% increase in compression efficiency over Fax Group 4 compression, and in some situations, it offers a 30-fold improvement .
- JBIG is the coding standard recommended by the Joint Bi-level Image Processing Group for binary images .
- This lossless compression standard is used primarily to code scanned images of printed or handwritten text, computer-generated text, and facsimile transmissions .



### JBIG2

- JBIG2 is an image compression standard for bi-level images, developed by the Joint Bi-level Image Experts Group.
- It is suitable for both lossless and lossy compression.
- JBIG2 typically generates files 3-5 times smaller than Fax Group 4 and 2-4 times smaller than JBIG in its lossless mode.
- JBIG2 is an international standard for bilevel image compression.
- By segmenting an image into overlapping and/or non-overlapping regions of text, halftone and generic content, compression techniques that are specially optimized for each type of content are employed.
- JBIG2 allows for lossless compression performance better than that of the existing standards, and to allow for lossy compression at much higher compression ratios than the lossless ratios of the existing standards, with almost no visible degradation of quality by using pattern matching and substitution techniques in addition to the technologies of the existing standards.



### Image Compression

Image compression is the process of reducing the size of an image file without degrading the quality of the image to an unacceptable level. This is achieved by removing redundant data from the image file, which can be done in two ways: lossless and lossy compression.

1. **Lossless Compression:** In lossless compression, the original image can be perfectly reconstructed from the compressed image. This is achieved by using algorithms that identify and remove statistical redundancy in the image data. Some common lossless image compression algorithms include PNG, GIF, and TIFF.

2. **Lossy Compression:** In lossy compression, some of the original image data is discarded in order to achieve a higher level of compression. This results in a loss of image quality, but the level of degradation is usually acceptable for most applications. Some common lossy image compression algorithms include JPEG, JPEG 2000, and WebP.

Image compression is an important tool in the field of data compression, as it allows for the efficient storage and transmission of image data. It is widely used in applications such as digital photography, web design, and video streaming.



### Dictionary Techniques

Dictionary techniques are used for coding a sequence in data compression. These techniques involve the use of a dictionary, which is a data structure that stores a set of symbols or strings. The dictionary is used to encode and decode the data by replacing the symbols or strings with their corresponding codes.

Some of the key points to remember about dictionary techniques are:

1. Dictionary techniques are used for lossless data compression, which means that the original data can be perfectly reconstructed from the compressed data.
2. The dictionary is built dynamically during the encoding process, based on the data being compressed.
3. The dictionary can be either static or adaptive. A static dictionary is fixed and does not change during the encoding process, while an adaptive dictionary is updated as new data is encountered.
4. Some common dictionary-based compression algorithms include Lempel-Ziv-Welch (LZW), Lempel-Ziv (LZ77), and Lempel-Ziv-Storer-Szymanski (LZSS).
5. Dictionary techniques are widely used in various applications, including text compression, image compression, and data transmission.




### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Data compression is the process of encoding information using fewer bits than the original representation.
2. The goal of data compression is to reduce the size of data for storage or transmission.
3. Coding a sequence is one of the techniques used in data compression.
4. In this technique, a sequence of symbols is represented using a code, where each symbol is assigned a unique code.
5. The code is designed in such a way that it requires fewer bits to represent the sequence than the original representation.
6. There are two types of coding techniques: lossless and lossy.
7. Lossless coding techniques preserve all the information in the original data, while lossy techniques discard some information to achieve higher compression ratios.
8. Some common lossless coding techniques include Huffman coding, arithmetic coding, and run-length encoding.
9. In this unit, we will learn about the different coding techniques and how to apply them to compress data.




### Static Dictionary

Static dictionary is a type of dictionary used in data compression algorithms. It is a fixed dictionary that is used to encode a sequence of data. The dictionary is created before the encoding process and remains unchanged throughout the encoding process. Here are some key points to remember about static dictionaries:

1. A static dictionary is created before the encoding process and remains unchanged throughout the encoding process.
2. The dictionary is fixed and does not change based on the data being encoded.
3. Static dictionaries are commonly used in lossless data compression algorithms.
4. The effectiveness of a static dictionary depends on how well it represents the data being encoded.
5. Static dictionaries can be created using various techniques, such as frequency analysis or Huffman coding.
6. The size of the dictionary can affect the compression ratio. A larger dictionary can provide better compression, but may also increase the size of the compressed data.




### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Diagram coding is a method of data compression that is used to encode a sequence of symbols.
2. It is based on the idea of representing a sequence of symbols as a single code, rather than encoding each symbol individually.
3. This is achieved by constructing a tree-like diagram, where each node represents a symbol or a sequence of symbols.
4. The diagram is constructed by starting with the most frequent symbol or sequence of symbols and adding nodes for less frequent symbols or sequences.
5. The code for a symbol or sequence is obtained by traversing the tree from the root to the node representing the symbol or sequence, and recording the path taken.
6. The resulting code is a variable-length code, where more frequent symbols or sequences have shorter codes.
7. Diagram coding can achieve high levels of compression, especially for data with repetitive patterns.
8. However, it requires the construction and transmission of the diagram, which can add to the overhead of the compression process.
9. There are several variations of diagram coding, including Huffman coding and arithmetic coding, which use different methods for constructing the diagram and assigning codes to symbols or sequences.
10. Diagram coding is widely used in applications such as text compression, image compression, and data transmission.




### Adaptive Dictionary

An adaptive dictionary is a type of dictionary used in data compression algorithms. It is a dictionary that changes over time to adapt to the data being compressed. This allows the dictionary to better represent the data and achieve higher compression ratios.

Here are some key points to remember about adaptive dictionaries:

1. An adaptive dictionary is used in data compression algorithms to achieve higher compression ratios.
2. The dictionary changes over time to better represent the data being compressed.
3. The dictionary is updated as new data is encountered, allowing it to adapt to changes in the data.
4. Adaptive dictionaries are commonly used in algorithms such as LZW and LZ77.
5. The use of an adaptive dictionary can improve the performance of a data compression algorithm, but it can also increase the complexity of the algorithm.




### The LZ77 Approach

LZ77 is a lossless data compression algorithm that is based on the idea of replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream. Here are some key points to note about the LZ77 approach:

1. LZ77 is a dictionary-based algorithm, where the dictionary is implicitly defined by the data that has already been processed.
2. The algorithm maintains a sliding window of the most recently processed data, which serves as the dictionary.
3. When a match is found between a substring in the current data and a substring in the sliding window, the algorithm outputs a pair of numbers: the distance to the start of the match in the sliding window, and the length of the match.
4. If no match is found, the algorithm outputs the next symbol in the data as a literal.
5. The size of the sliding window is a parameter of the algorithm and can be adjusted to trade off compression ratio and compression speed.
6. LZ77 is the basis for many widely used compression algorithms, including DEFLATE (used in gzip and PNG) and LZW (used in GIF and TIFF).

This is a brief overview of the LZ77 approach to data compression. It is a powerful and widely used algorithm that can achieve high compression ratios while maintaining good compression speed. It is an important topic to understand for anyone studying data compression.



### The LZ78 Approach

LZ78 is a lossless data compression algorithm that is used to compress a sequence of data. It is the second of the Lempel-Ziv algorithms, and was published by Abraham Lempel and Jacob Ziv in 1978. Here are some key points to note about the LZ78 approach:

1. LZ78 builds a dictionary of phrases that have been encountered in the input data.
2. The dictionary is initialized with all possible symbols in the input alphabet.
3. As the input data is processed, new phrases are added to the dictionary.
4. Each phrase in the dictionary is assigned a unique index.
5. The compressed output consists of a sequence of indices that represent the phrases in the input data.
6. The decompression process involves using the dictionary to reconstruct the original data from the sequence of indices.
7. LZ78 is a dictionary-based algorithm, and its performance depends on the size of the dictionary and the nature of the input data.
8. The algorithm is simple to implement and can achieve good compression ratios for certain types of data.




### Applications for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Data storage**: Coding a sequence is used to compress data for storage, reducing the amount of space required to store the data.
2. **Data transmission**: Compressed data can be transmitted more efficiently, reducing the time and bandwidth required for transmission.
3. **Error correction**: Certain coding techniques can be used to detect and correct errors that may occur during data transmission or storage.
4. **Data security**: Coding a sequence can be used in combination with encryption techniques to enhance the security of data.
5. **Image and video compression**: Coding a sequence is widely used in image and video compression, allowing for the efficient storage and transmission of multimedia content.
6. **Audio compression**: Coding a sequence is also used in audio compression, allowing for the efficient storage and transmission of audio content.




### File Compression-UNIX compress

- UNIX compress is a file compression program that uses the Lempel-Ziv-Welch (LZW) algorithm.
- It is commonly used in UNIX and UNIX-like operating systems.
- The program is invoked by the command `compress` followed by the name of the file to be compressed.
- The compressed file is saved with the same name as the original file, but with the extension `.Z` added.
- To decompress a file, the command `uncompress` is used, followed by the name of the compressed file.
- The original file is restored with the same name and without the `.Z` extension.
- The LZW algorithm used by UNIX compress is a lossless data compression algorithm, meaning that no data is lost during the compression process.
- The algorithm works by replacing common substrings in the data with shorter codes, resulting in a smaller file size.
- The effectiveness of the compression depends on the nature of the data being compressed. Data with a lot of repetition can be compressed more effectively than data with little repetition.
- UNIX compress is not as effective as some other compression algorithms, such as gzip or bzip2, but it is still widely used due to its simplicity and availability on UNIX and UNIX-like systems.



### Image Compression

Image compression is a technique used to reduce the size of an image file while maintaining its visual quality. This is achieved by removing redundant or unnecessary information from the image data. There are two main types of image compression: lossless and lossy.

1. **Lossless Compression:** This method compresses the image data without losing any information. The original image can be perfectly reconstructed from the compressed data. Examples of lossless image compression algorithms include PNG, GIF, and TIFF.

2. **Lossy Compression:** This method compresses the image data by discarding some information that is deemed less important. The original image cannot be perfectly reconstructed from the compressed data, but the visual quality is usually maintained. Examples of lossy image compression algorithms include JPEG and WebP.

Image compression is important for reducing the storage space required for images and for improving the speed of transmitting images over the internet. It is widely used in digital photography, web design, and other applications where large numbers of images need to be stored or transmitted efficiently.



### The Graphics Interchange Format (GIF)

- The Graphics Interchange Format (GIF) is a bitmap image format that was developed by a team at the online services provider CompuServe led by American computer scientist Steve Wilhite on June 15, 1987.
- It has since come into widespread usage on the World Wide Web due to its wide support and portability between applications and operating systems.
- The format supports up to 8 bits per pixel for each image, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space.
- It also supports animations and allows a separate palette of up to 256 colors for each frame.
- These palette limitations make the GIF format less suitable for reproducing color photographs and other images with color gradients, but it is well-suited for simpler images such as graphics or logos with solid areas of color.
- GIF images are compressed using the Lempel–Ziv–Welch (LZW) lossless data compression technique to reduce the file size without degrading the visual quality.
- This compression technique was patented in 1985. Controversy over the licensing agreement between the software patent holder, Unisys, and CompuServe in 1994 spurred the development of the Portable Network Graphics (PNG) standard.
- All the relevant patent licenses for GIF have now expired.



### Compression over Modems

1. Compression over modems is a technique used to reduce the amount of data transmitted over a modem connection.
2. This is achieved by using data compression algorithms to encode the data before transmission and then decoding it at the receiving end.
3. The most common compression algorithms used for this purpose are Huffman coding, Lempel-Ziv-Welch (LZW) coding, and run-length encoding (RLE).
4. These algorithms work by identifying and removing redundancy in the data, resulting in a smaller amount of data that needs to be transmitted.
5. Compression over modems can significantly increase the effective data transfer rate of a modem connection, allowing for faster transmission of data.
6. However, the effectiveness of compression over modems depends on the nature of the data being transmitted. Data that is highly compressible, such as text or simple graphics, can benefit greatly from compression, while data that is already compressed, such as audio or video files, may not see much improvement.
7. In addition to improving data transfer rates, compression over modems can also reduce the cost of data transmission, as less data needs to be transmitted.
8. Compression over modems is commonly used in applications such as remote access, file transfer, and internet access.




### V.42 bits for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

V.42 is an error-correcting protocol for modems developed by the International Telecommunication Union (ITU). It is used to detect and correct errors that may occur during data transmission over noisy communication channels.

Here are some key points about V.42 bits:

1. V.42 uses a combination of two error-correcting techniques: **LAPM (Link Access Procedure for Modems)** and **MNP (Microcom Networking Protocol)**.
2. LAPM is the primary error-correcting technique used by V.42. It is based on the **HDLC (High-Level Data Link Control)** protocol and uses a **frame-based** approach to error correction.
3. MNP is used as a fallback error-correcting technique in case LAPM fails. It is a **byte-oriented** protocol and is less efficient than LAPM.
4. V.42 can detect errors using **Cyclic Redundancy Check (CRC)** and can correct them using **retransmission** of corrupted data.
5. V.42 also includes a **flow control** mechanism to prevent data loss due to buffer overflow.
6. V.42 is widely used in **dial-up** and **leased line** connections.




### Predictive Coding

Predictive coding is a method of lossless data compression that is commonly referred to as differential pulse code modulation (DPCM). A special case of this method is delta modulation (DM), which quantizes the error signal using only two quantization levels.

One example of a predictive coding algorithm is Dynamic Markov compression (DMC), which was developed by Gordon Cormack and Nigel Horspool. DMC uses predictive arithmetic coding, similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time, rather than one byte at a time.

Predictive coding techniques can be used for the efficient transmission or storage of digital images. These techniques can also be used in other fields, such as artificial intelligence, machine learning, and neuroscience.

In summary, predictive coding is a method of lossless data compression that uses prediction algorithms to reduce the amount of data that needs to be transmitted or stored. It has applications in a variety of fields and can be used to compress different types of data.



### Prediction with Partial match (ppm) for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Prediction by Partial Matching (PPM) is a lossless compression algorithm which consistently performs well on text compression benchmarks.
- PPM is an adaptive statistical data compression technique based on context modeling and prediction.
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream.
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis.
- Originally, PPM was targeted towards compressing text that can be viewed as a one-dimensional sequence of symbols.



### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. **Identify the symbols**: The first step in coding a sequence is to identify the symbols that make up the sequence. These symbols can be characters, numbers, or any other type of data.

2. **Determine the probabilities**: Once the symbols have been identified, the next step is to determine the probability of each symbol occurring in the sequence. This can be done by counting the number of times each symbol appears in the sequence and dividing by the total number of symbols.

3. **Assign codes**: After the probabilities have been determined, codes can be assigned to each symbol. There are several methods for assigning codes, including Huffman coding and arithmetic coding.

4. **Encode the sequence**: Once the codes have been assigned, the sequence can be encoded by replacing each symbol with its corresponding code.

5. **Decode the sequence**: To decode the sequence, the process is reversed. The codes are replaced with their corresponding symbols to recreate the original sequence.

This is the basic algorithm for coding a sequence in the subject of data compression. It is important to note that there are many variations and optimizations that can be applied to this process to improve its efficiency and effectiveness. However, the fundamental steps remain the same.



# The ESCAPE SYMBOL

The escape symbol is a special character used in data compression algorithms to represent a symbol that is not in the current dictionary. It is used in combination with a variable-length code to encode a sequence of symbols.

Here are some key points to remember about the escape symbol:

1. The escape symbol is used to represent a symbol that is not in the current dictionary.
2. It is used in combination with a variable-length code to encode a sequence of symbols.
3. The escape symbol is typically followed by the actual symbol being represented, which is then added to the dictionary for future use.
4. The use of the escape symbol allows for the dynamic updating of the dictionary, which can improve the efficiency of the compression algorithm.
5. The escape symbol is commonly used in adaptive dictionary-based compression algorithms such as LZW and LZ77.




### Unit 3 - Coding a Sequence: Length of Context

1. The length of context refers to the number of preceding symbols in a sequence that are used to predict the next symbol.
2. In data compression, the length of context is an important parameter that determines the effectiveness of the compression algorithm.
3. A longer context length can result in more accurate predictions and better compression, but it also increases the complexity of the algorithm and the amount of memory required to store the context information.
4. The optimal context length depends on the characteristics of the data being compressed and the trade-off between compression efficiency and computational resources.
5. In practice, the context length is often chosen empirically by testing different values and selecting the one that provides the best balance between compression performance and computational cost.



### The Exclusion Principle

The exclusion principle is a concept in data compression that is used to encode a sequence. It is based on the idea that if a symbol has already occurred in a sequence, it is less likely to occur again. This principle is used to reduce the number of bits required to represent a symbol in the sequence.

Here are some key points to remember about the exclusion principle:

1. The exclusion principle is used to encode a sequence in data compression.
2. It is based on the idea that if a symbol has already occurred in a sequence, it is less likely to occur again.
3. This principle is used to reduce the number of bits required to represent a symbol in the sequence.
4. The exclusion principle can be applied to various types of data, including text, images, and audio.
5. It is often used in combination with other data compression techniques to achieve higher levels of compression.




### The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm used in data compression. It was invented by Michael Burrows and David Wheeler in 1994. Here are some key points to note about the BWT:

1. The BWT rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easier to compress a string that has runs of repeated characters.

2. The BWT is not a compression algorithm by itself. Instead, it is typically used as a pre-processing step before applying another compression algorithm.

3. The BWT is reversible, meaning that the original string can be recovered from the transformed string.

4. The BWT is based on the idea of sorting all the cyclic rotations of a string. The transformed string is then formed by taking the last character of each sorted rotation.

5. The BWT can be computed efficiently using suffix arrays or the FM-index.

6. The BWT has been used in several popular compression algorithms, including bzip2 and the PPM family of compressors.

This is a brief overview of the Burrows-Wheeler Transform and its role in data compression. It is an important concept to understand for the study of data compression techniques.



### Move-to-front coding

Move-to-front coding is a technique used in data compression. It is a type of adaptive coding that is used to encode a sequence of symbols. Here are some key points to note about move-to-front coding:

1. Move-to-front coding is an adaptive coding technique, meaning that it adapts to the data being compressed.
2. It works by maintaining a list of symbols in order of their most recent occurrence.
3. When a symbol is encountered, its index in the list is output and the symbol is moved to the front of the list.
4. This means that frequently occurring symbols will have low indices and will be moved to the front of the list, resulting in shorter codes for these symbols.
5. Move-to-front coding is particularly effective when the data being compressed has a high degree of locality, meaning that symbols that have occurred recently are likely to occur again soon.
6. It is often used in combination with other compression techniques, such as Huffman coding or arithmetic coding, to improve compression performance.




### CALIC

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

JPEG-LS is a lossless/near-lossless compression standard for continuous-tone images. Its official designation is ISO-14495-1/ITU-T.87. It is a simple and efficient baseline algorithm which consists of two independent and distinct stages called modeling and encoding.

The standard is based on the LOCO-I algorithm (LOw COmplexity LOssless COmpression for Images) developed at Hewlett-Packard Laboratories.

JPEG-LS is a low-complexity image compression standard that matches JPEG 2000 compression ratios.



### Multi-resolution Approaches

Multi-resolution approaches are used in data compression to represent data at different levels of resolution or detail. These approaches are commonly used in image and video compression, where the data can be represented at different levels of detail depending on the desired resolution.

Some common multi-resolution approaches used in data compression include:

1. **Pyramid representation:** This approach involves representing the data at multiple levels of resolution by successively down-sampling the data to create a pyramid of lower resolution versions of the data.

2. **Wavelet transform:** This approach involves decomposing the data into a set of wavelet coefficients, which represent the data at different scales and resolutions. The wavelet coefficients can be quantized and encoded to achieve data compression.

3. **Sub-band coding:** This approach involves decomposing the data into multiple frequency bands, each of which can be encoded at a different resolution. This allows for more efficient compression of the data, as different frequency bands may require different levels of detail.

These multi-resolution approaches can be used in combination with other data compression techniques, such as predictive coding and entropy coding, to achieve high levels of data compression while maintaining the desired level of detail in the data.



### Facsimile Encoding

Facsimile encoding is a method used to compress data for transmission in fax machines. It is also known as fax encoding or Group 3 encoding. This method is used to encode black and white images, such as text documents, for transmission over a telephone line.

Here are some key points to remember about facsimile encoding:

1. Facsimile encoding is a lossless compression method, meaning that the original image can be perfectly reconstructed from the compressed data.
2. It uses a combination of run-length encoding and Huffman coding to compress the data.
3. Run-length encoding is used to compress long runs of white or black pixels, while Huffman coding is used to compress the remaining data.
4. The compressed data is transmitted using a standard protocol, such as the ITU-T T.4 or T.6 standard.
5. Facsimile encoding is widely used in fax machines and other devices that transmit black and white images over a telephone line.

This is a brief overview of facsimile encoding. It is an important topic in the study of data compression and is covered in more detail in Unit 3 - Coding a sequence of the subject of Data Compression.



### Dynamic Markov Compression

Dynamic Markov Compression (DMC) is a lossless data compression algorithm that uses a Markov model to predict the next symbol in a sequence based on the previous symbols. It is used in the context of coding a sequence in the subject of data compression.

Here are some key points to note about DMC:

1. DMC is an adaptive algorithm, meaning that it adjusts its model as it processes the data.
2. The Markov model used in DMC is a probabilistic model that predicts the next symbol based on the previous symbols.
3. DMC can achieve high compression ratios, especially for data with strong correlations between adjacent symbols.
4. DMC is a lossless compression algorithm, meaning that the original data can be perfectly reconstructed from the compressed data.
5. DMC is relatively slow compared to other compression algorithms, due to the need to update the Markov model as the data is processed.




## Unit 4 - Distortion criteria

Distortion criteria are used to evaluate the performance of communication systems. They are used to measure the quality of the transmitted signal and to determine the level of distortion introduced by the system. There are several types of distortion criteria, including:

1. **Signal-to-noise ratio (SNR):** This is the ratio of the power of the signal to the power of the noise. A higher SNR indicates a better quality signal with less distortion.

2. **Mean squared error (MSE):** This is the average of the squared differences between the original signal and the distorted signal. A lower MSE indicates a better quality signal with less distortion.

3. **Peak signal-to-noise ratio (PSNR):** This is the ratio of the maximum power of the signal to the power of the noise. A higher PSNR indicates a better quality signal with less distortion.

4. **Total harmonic distortion (THD):** This is the ratio of the sum of the powers of all harmonic components to the power of the fundamental frequency. A lower THD indicates a better quality signal with less distortion.

These are some of the common distortion criteria used in communication systems. Each criterion has its own advantages and disadvantages, and the choice of criterion depends on the specific requirements of the system.



### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

1. Distortion criteria is a measure of the difference between the original and reconstructed data.
2. It is used to evaluate the performance of data compression algorithms.
3. There are several models for distortion criteria, including mean squared error, peak signal-to-noise ratio, and structural similarity index.
4. Mean squared error measures the average of the squared difference between the original and reconstructed data.
5. Peak signal-to-noise ratio measures the ratio between the maximum possible power of a signal and the power of the noise that affects the fidelity of its representation.
6. Structural similarity index measures the similarity between two images by taking into account the luminance, contrast, and structure of the images.
7. The choice of distortion criteria depends on the specific application and the desired trade-off between compression ratio and reconstruction quality.
8. In general, a lower distortion criteria value indicates better reconstruction quality.




### Scalar Quantization

Scalar quantization is a process of mapping a continuous amplitude signal to a discrete amplitude signal. It is a technique used in data compression to reduce the number of bits required to represent a signal. Here are some key points to remember about scalar quantization:

1. Scalar quantization is a type of uniform quantization, where the quantization levels are equally spaced.
2. The quantization error is the difference between the original signal and the quantized signal.
3. The quantization error is also known as the distortion.
4. The goal of scalar quantization is to minimize the distortion while reducing the number of bits required to represent the signal.
5. The performance of scalar quantization can be improved by using non-uniform quantization, where the quantization levels are not equally spaced.
6. The Lloyd-Max algorithm is a commonly used method for designing optimal scalar quantizers.




### The Quantization Problem

Quantization is the process of mapping a large set of input values to a smaller set of output values. This is done to reduce the amount of data that needs to be stored or transmitted. In the context of data compression, quantization is used to reduce the number of bits needed to represent a signal.

The quantization problem arises when trying to determine the optimal way to perform this mapping. There are several factors to consider when designing a quantization scheme, including:

1. **Distortion**: The difference between the original signal and the quantized signal is known as distortion. The goal of quantization is to minimize this distortion while still achieving the desired level of compression.

2. **Rate**: The rate of a quantization scheme refers to the number of bits used to represent each quantized value. A lower rate means that fewer bits are used, resulting in greater compression. However, a lower rate also typically results in greater distortion.

3. **Complexity**: The complexity of a quantization scheme refers to the computational resources required to perform the quantization. A more complex scheme may result in lower distortion or a lower rate, but may also require more processing power or memory.

The quantization problem involves finding the optimal balance between these factors to achieve the desired level of compression while minimizing distortion and complexity. This is a challenging problem, and there are many different approaches to solving it. Some common techniques include uniform quantization, non-uniform quantization, and vector quantization. Each of these techniques has its own strengths and weaknesses, and the best approach will depend on the specific requirements of the application.



### Uniform Quantizer

- Uniform quantization is achieved when the characteristic curve is linear and no compression is done .
- At high bit rates, the best quantization strategy is to use a uniform quantizer followed by an entropy encoder. This results in a fairly simple lossy compression scheme whose performance is very close to that of the best possible performance bound .
- Uniform scalar quantizer (SQ) is commonly applied to the feature maps between the encoder and decoder in deep learning-based image compression frameworks .
- There are few comparisons between quantization methods and the best approximation among them remains unexplored .



### Adaptive Quantization

Adaptive quantization is a technique used in data compression to change the quantization parameters based on the data being compressed. It can be used in both forward and backward adaptive quantization schemes.

- In forward adaptive quantization, the input is divided into blocks and the quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information .
- In backward adaptive quantization, the algorithm is used to adapt the quantizer to the local behavior of nonstationary inputs .
- Adaptive compression is a type of data compression which changes compression algorithms based on the type of data being compressed .
- This enables selecting an appropriate compression for incoming samples, while taking into account overall memory constraints and current progress of the learned compression .

Adaptive quantization can be used in DPCM systems to improve compression efficiency. It is a key technique in the hybrid video coding framework .



### Non-uniform Quantization

Non-uniform quantization is a type of quantization used in data compression where the quantization levels are not equally spaced. This is in contrast to uniform quantization, where the quantization levels are equally spaced.

In non-uniform quantization, the quantization levels are designed to match the statistical distribution of the input signal. This means that the quantization levels are more closely spaced in regions where the input signal is more likely to occur, and more widely spaced in regions where the input signal is less likely to occur.

The advantage of non-uniform quantization is that it can provide a lower distortion for a given number of quantization levels, compared to uniform quantization. This is because the quantization levels are more closely matched to the input signal, which reduces the quantization error.

Non-uniform quantization is commonly used in speech and audio coding, where the input signal has a non-uniform distribution. For example, the human ear is more sensitive to sounds in the mid-frequency range, so the quantization levels in this range are more closely spaced.

There are several methods for designing non-uniform quantizers, including the Lloyd-Max algorithm and the companding method. These methods aim to minimize the distortion by optimizing the placement of the quantization levels.

In summary, non-uniform quantization is a type of quantization used in data compression where the quantization levels are not equally spaced. It is designed to match the statistical distribution of the input signal, which can provide a lower distortion for a given number of quantization levels. Non-uniform quantization is commonly used in speech and audio coding, and there are several methods for designing non-uniform quantizers.



## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

Vector Quantization (VQ) is a technique used in signal processing that allows the modeling of probability density functions by the distribution of prototype vectors. It has several advantages over Scalar Quantization (SQ), which is a simpler technique that quantizes a scalar value into a single value.

1. For a given rate, VQ results in a lower distortion than SQ.
2. If the source output is correlated, vectors of source output values will tend to fall in clusters.
3. Even if there is no dependency, VQ offers greater flexibility.
4. VQ can lower the average distortion with the number of reconstruction levels held constant, while SQ cannot.
5. VQ can reduce the number of reconstruction levels when distortion is held constant, while SQ cannot.
6. The most significant way VQ can improve performance over SQ is by exploiting the statistical dependence among scalars in the block.
7. VQ is also more effective than SQ when the source output values are not correlated.

However, like all things in life, quality comes with a price. For VQ, that price comes in the form of increased encoder complexity and codebook memory.



### The Linde-Buzo-Gray Algorithm

The Linde-Buzo-Gray (LBG) algorithm, introduced by Yoseph Linde, Andrés Buzo, and Robert M. Gray in 1980, is a vector quantization algorithm used to derive a good codebook. It is similar to the k-means method in data clustering. At each iteration, each vector is split into two new vectors.

#### Advantages of Vector Quantization over Scalar Quantization

Vector quantization (VQ) is an effective means of data compression as it maps a set of real numbers into a single integer. Some advantages of vector quantization over scalar quantization include:

- Vector Quantization can lower the average distortion with the number of reconstruction levels held constant.
- Vector Quantization can reduce the number of reconstruction levels when distortion is held constant.

#### Data Compression

Data compression is the process of reducing the size of a data file by encoding its information more efficiently. The LBG algorithm, when used with vector quantization, can result in decent image quality when compressing images.



### Tree structured Vector Quantizers

Tree structured vector quantizers (TSVQ) are a type of vector quantizer that use a tree structure to partition the input space. This allows for efficient encoding and decoding of the input vectors.

Some advantages of vector quantization over scalar quantization include:

1. Vector quantization can achieve higher compression ratios than scalar quantization, as it takes into account the correlation between the components of the input vectors.
2. Vector quantization can produce higher quality reconstructed signals than scalar quantization, as it can better preserve the structure of the input data.
3. Vector quantization can be more robust to channel errors than scalar quantization, as errors in one component of the quantized vector can be compensated for by the other components.

TSVQs have several advantages over other types of vector quantizers:

1. The tree structure allows for fast encoding and decoding, as the search for the closest codeword can be performed efficiently using a tree search algorithm.
2. TSVQs can adapt to changes in the input data distribution, as the tree structure can be updated to better match the input data.
3. TSVQs can be designed to have a variable rate, where the number of bits used to encode each input vector can vary depending on the complexity of the input data.

Overall, TSVQs are a powerful tool for data compression, offering high compression ratios, high quality reconstructed signals, and fast encoding and decoding. They are particularly well-suited for applications where the input data has a complex, correlated structure.



### Structured Vector Quantizers

Vector quantization is a technique used in data compression to reduce the amount of data needed to represent a signal. It is a lossy compression technique, meaning that some information is lost in the process of compressing the data. However, the loss of information is usually not noticeable to the human eye or ear.

One of the advantages of vector quantization over scalar quantization is that it can achieve higher compression ratios. This is because vector quantization takes advantage of the correlation between adjacent samples in the signal. By grouping these samples together into vectors and quantizing the vectors instead of the individual samples, vector quantization can achieve higher compression ratios than scalar quantization.

Structured vector quantizers are a type of vector quantizer that use a predefined structure to represent the codebook. This structure can be a tree, a lattice, or a product code. The advantage of using a structured vector quantizer is that it can reduce the complexity of the quantization process. This is because the structure of the codebook can be used to simplify the search for the closest codeword to a given input vector.

In summary, vector quantization is a powerful technique for data compression that can achieve higher compression ratios than scalar quantization. Structured vector quantizers, in particular, can reduce the complexity of the quantization process by using a predefined structure to represent the codebook. This makes vector quantization an attractive option for applications where high compression ratios and low complexity are important.

