### Modeling and coding for data compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression preserves the exact original data, while lossy compression discards some data that is deemed less important or perceptible.
- Modeling and coding are the two levels to compress data :
  - In the first level, the data will be analyzed for any redundant information and extract it to develop a model.
  - In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique.
- Modeling can be done using one of two different types of methods: statistical or dictionary-based .
  - Statistical modeling reads in and encodes a single symbol at a time using the probability of that character’s appearance.
  - Dictionary-based modeling uses a single code to replace strings of symbols that are stored in a dictionary.
- Coding can be done using one of two different types of methods: entropy coding or arithmetic coding .
  - Entropy coding assigns shorter codes to more frequent symbols and longer codes to less frequent symbols, based on the entropy or information content of the data.
  - Arithmetic coding assigns a single code to the entire data, based on the cumulative probability of the symbols, and can achieve optimal compression.
- Data compression can also be done using deep learning techniques, such as Bit-Swap, which uses latent variable models and bits-back coding to learn the probability distribution of the data and encode it efficiently.