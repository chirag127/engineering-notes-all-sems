### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes.
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios than static dictionary methods.
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, LZW, etc.
- LZ77 and LZ78 are based on the idea of replacing repeated sequences of symbols with references to their previous occurrences in the data stream.
- LZW is based on the idea of building a dictionary of prefixes and suffixes of symbols and encoding them with variable-length codes.
- Adaptive dictionary algorithms have the following advantages:
  - They do not require prior knowledge of the data source or statistics.
  - They can handle any type of data, such as text, audio, video, etc.
  - They can adjust to the changes in the data distribution over time.
  - They can achieve high compression ratios for data with high redundancy or regularity.
- Adaptive dictionary algorithms have the following disadvantages:
  - They require more memory and processing power than static dictionary methods.
  - They may suffer from dictionary overflow or degradation if the dictionary size is limited or not managed properly.
  - They may introduce errors or inefficiencies if the compression and decompression dictionaries are not synchronized or updated consistently.