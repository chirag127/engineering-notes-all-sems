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