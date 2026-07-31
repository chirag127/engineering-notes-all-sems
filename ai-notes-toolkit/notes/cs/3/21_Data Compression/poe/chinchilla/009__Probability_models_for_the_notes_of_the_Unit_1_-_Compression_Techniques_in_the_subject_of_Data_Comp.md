### Probability models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

In this unit, we will be discussing various compression techniques used in data compression. However, one of the key components in data compression is probability modeling. Probability models help us to estimate the probability of occurrence of a symbol in a stream of data. In this section, we will discuss the various probability models used in data compression.

1. **Binary Probability Model**: Binary probability model is the simplest probability model used in data compression. It assumes that each symbol in the data stream is independent and has a probability of occurrence of 0 or 1. This model is commonly used in lossless data compression techniques such as Huffman coding.

2. **Markov Model**: Markov model is a type of probability model that takes into account the dependence between symbols in a data stream. It assumes that the probability of occurrence of a symbol depends on the previously occurring symbols. Markov models are commonly used in lossy data compression techniques such as predictive coding.

3. **Arithmetic Encoding Model**: Arithmetic encoding model is a type of probability model that assigns a unique probability range to each symbol in the data stream. The probability range is calculated based on the probability of occurrence of the symbol and the probability of occurrence of all the previously occurring symbols. Arithmetic encoding model is commonly used in lossless data compression techniques.

4. **Context-Based Adaptive Binary Arithmetic Coding Model**: Context-Based Adaptive Binary Arithmetic Coding (CABAC) model is a type of probability model that combines the binary probability model and arithmetic encoding model. It takes into account the dependence between symbols in a data stream and assigns a unique probability range to each symbol based on the previously occurring symbols. CABAC model is commonly used in video compression techniques.

5. **Neural Network Model**: Neural network model is a type of probability model that uses artificial neural networks to estimate the probability of occurrence of a symbol in a data stream. It takes into account the dependence between symbols in a data stream and can be used in both lossless and lossy data compression techniques.

In conclusion, probability modeling is an essential component in data compression. The choice of probability model depends on the type of data and the compression technique used. Understanding the various probability models used in data compression can help in selecting the most appropriate model for a given scenario.