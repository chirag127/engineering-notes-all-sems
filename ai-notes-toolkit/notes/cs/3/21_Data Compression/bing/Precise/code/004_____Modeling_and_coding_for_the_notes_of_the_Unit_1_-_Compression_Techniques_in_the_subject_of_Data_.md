### Unit 1 - Compression Techniques

#### Modeling and coding

1. **Modeling** is the process of constructing a statistical model of the data to be compressed. This model is used to predict the probability of each symbol in the data, which is then used to assign shorter codes to more probable symbols and longer codes to less probable symbols.

2. **Coding** is the process of assigning a unique binary code to each symbol in the data based on the probabilities determined by the model. There are two main types of coding techniques: entropy coding and dictionary coding.

3. **Entropy coding** techniques, such as Huffman coding and arithmetic coding, assign codes to symbols based on their probabilities. Symbols with higher probabilities are assigned shorter codes, while symbols with lower probabilities are assigned longer codes.

4. **Dictionary coding** techniques, such as Lempel-Ziv-Welch (LZW) and Deflate, use a dictionary to store commonly occurring patterns in the data. These patterns are then replaced with shorter codes, reducing the size of the data.

5. Both modeling and coding are essential components of data compression. The effectiveness of the compression depends on the accuracy of the model and the efficiency of the coding technique used.