Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here are some notes on the topic of Models for the notes of the Unit 1 - Compression Techniques.

### Models

- A model is a representation of the source data that captures its statistical properties and allows for efficient compression.
- A model can be either static or adaptive.
- A static model is fixed and does not change during the compression process. It is usually based on some prior knowledge or analysis of the source data.
- An adaptive model is updated dynamically based on the data that has been processed so far. It can adapt to the changing characteristics of the source data and achieve better compression performance.
- Some examples of models are:
  - Uniform model: This model assumes that all symbols in the source data have equal probability of occurrence. It is simple but not very effective for most real-world data.
  - Huffman model: This model assigns variable-length codes to the symbols based on their frequencies of occurrence. It is optimal for a given set of symbol probabilities and guarantees a minimum average code length.
  - Arithmetic model: This model encodes the entire source data as a single fractional number in the range [0, 1). It assigns subintervals of the range to the symbols based on their probabilities and recursively subdivides the intervals as more symbols are processed. It can achieve near-optimal compression for any source data.
  - Dictionary model: This model uses a predefined or dynamically constructed dictionary of strings to compress the source data. It replaces repeated occurrences of strings with references to their dictionary entries. It can exploit the structure and redundancy of the source data and achieve high compression ratios.