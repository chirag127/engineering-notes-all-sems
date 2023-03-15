# Unit 1 - Compression Techniques

## Modeling and coding

Modeling and coding are two important concepts in data compression. Here are some key points to remember:

1. **Modeling** refers to the process of identifying patterns and relationships in the data to be compressed. This can involve analyzing the statistical properties of the data, such as the frequency of different symbols or the probability of certain sequences of symbols occurring.

2. **Coding** refers to the process of representing the data using a more compact form. This can involve assigning shorter codes to more frequently occurring symbols or sequences of symbols, and longer codes to less frequently occurring symbols or sequences.

3. There are two main types of coding techniques used in data compression: **entropy coding** and **dictionary-based coding**.

4. **Entropy coding** techniques, such as Huffman coding and arithmetic coding, are based on the idea of assigning shorter codes to more probable symbols and longer codes to less probable symbols. These techniques can be very effective when the data being compressed has a skewed distribution, with some symbols occurring much more frequently than others.

5. **Dictionary-based coding** techniques, such as Lempel-Ziv-Welch (LZW) coding, involve building a dictionary of commonly occurring sequences of symbols and assigning codes to these sequences. These techniques can be very effective when the data being compressed contains many repeated sequences of symbols.

6. Both modeling and coding are important for achieving good compression performance. The effectiveness of a compression algorithm depends on how well it can model the data and how efficiently it can represent the data using codes.

7. In practice, many compression algorithms use a combination of modeling and coding techniques to achieve the best possible compression performance.