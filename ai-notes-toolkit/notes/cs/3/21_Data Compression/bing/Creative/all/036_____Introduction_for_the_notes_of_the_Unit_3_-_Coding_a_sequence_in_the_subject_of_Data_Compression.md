# Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, Huffman coding, arithmetic coding, run-length encoding, dictionary-based encoding, etc.
- Coding a sequence is one of the fundamental tasks in data compression, where a given sequence of symbols (such as characters, bits, pixels, etc.) is transformed into another sequence of symbols that is shorter or more efficient to store or transmit.
- Coding a sequence can be classified into two types: lossless and lossy.
  - Lossless coding preserves the exact information of the original sequence, and allows the original sequence to be reconstructed from the coded sequence without any errors or distortion.
  - Lossy coding discards some information of the original sequence, and allows the original sequence to be approximated from the coded sequence with some acceptable errors or distortion.
- Coding a sequence can also be classified into two modes: fixed-length and variable-length.
  - Fixed-length coding assigns a fixed number of bits or symbols to each symbol in the original sequence, regardless of its frequency or probability of occurrence.
  - Variable-length coding assigns a variable number of bits or symbols to each symbol in the original sequence, depending on its frequency or probability of occurrence, such that more frequent or probable symbols are assigned shorter codes and less frequent or probable symbols are assigned longer codes.
- Coding a sequence can be further classified into two methods: source coding and channel coding.
  - Source coding is the process of reducing the redundancy or inefficiency of the original sequence, by exploiting the statistical properties or patterns of the source data, such as frequency, probability, correlation, etc.
  - Channel coding is the process of adding redundancy or robustness to the coded sequence, by exploiting the characteristics or constraints of the communication channel, such as bandwidth, noise, error, etc.