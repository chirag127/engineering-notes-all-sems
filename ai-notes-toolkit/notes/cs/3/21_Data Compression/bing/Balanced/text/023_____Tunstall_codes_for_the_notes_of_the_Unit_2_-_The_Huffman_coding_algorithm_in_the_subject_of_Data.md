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