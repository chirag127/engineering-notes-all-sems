 Here is the content in markdown format for the topic ### Probability models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression:

### Probability models

- Probability models are statistical models which estimate the likelihood of a certain symbol appearing in the input.
- These models are built based on the frequency of occurrence of symbols in the input data.
- The compressor encodes the most likely symbols using fewer bits and less likely symbols using more bits.
- This results in an average code length that is less than the original per symbol code length (like ASCII codes) and thus achieves compression.
- The most commonly used probability models are:

1. Unigram (0-order) model: Symbols are modeled independently. Good for inputs with little correlation.
2. Bigram (1-order) model: Symbols are modeled based on the previous symbol. Captures local correlation.
3. Trigram (2-order) model: Symbols are modeled based on previous 2 symbols. Can capture more correlation but at the cost of more complexity and memory.

- Higher order models can capture more correlation leading to better compression but they suffer from sparcity of data issues as the number of parameters to estimate increase exponentially with increase in order.
- adaptivity and context modelling are techniques used to overcome some of these challenges.
- Examples of compression algorithms using probability models are Huffman coding, Arithmetic coding, Prediction by Partial Matching (PPM), Context Tree Weighting (CTW), etc.

- Advantages: Simple to implement, achieve decent compression without complex processing
- Disadvantages: Do not capture long range correlations, suffer from overfitting and sparcity of data issues for higher order models.
- Applications: Text, code and database compression, speech coding, etc.

[Detailed diagrams and examples can be added here if required for learning.]