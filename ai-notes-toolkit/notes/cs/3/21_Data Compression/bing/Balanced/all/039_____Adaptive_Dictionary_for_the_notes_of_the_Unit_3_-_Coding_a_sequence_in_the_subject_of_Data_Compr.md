# Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated based on the input data  .
- Adaptive dictionary can achieve higher compression ratios than static dictionary, especially for non-text data, such as audio or video .
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel, and Welch .
- LZ77 and LZ78 use a sliding window of previous data to find matches with the current data and encode them as pointers to the dictionary .
- LZW uses a fixed-size dictionary that is initialized with all possible symbols and then grows by adding new sequences of symbols that are encountered in the input data .
- Adaptive dictionary compression has some advantages, such as:
  - It does not require prior knowledge of the data characteristics or statistics .
  - It can adapt to changes in the data distribution over time .
  - It can compress data with variable-length symbols, such as natural language or DNA sequences .
- Adaptive dictionary compression has some disadvantages, such as:
  - It requires more memory and processing power than static dictionary compression .
  - It may suffer from dictionary overflow or degradation, which can reduce the compression performance or require periodic resetting of the dictionary .
  - It may introduce errors or ambiguities in the decompression process if the dictionary is not synchronized between the encoder and the decoder .