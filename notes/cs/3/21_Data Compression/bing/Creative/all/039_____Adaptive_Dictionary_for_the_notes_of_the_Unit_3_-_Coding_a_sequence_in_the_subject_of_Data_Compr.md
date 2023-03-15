# Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes.
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios than static dictionary methods.
- Adaptive dictionary can be implemented using various algorithms, such as LZ77, LZ78, LZW, etc.
- Adaptive dictionary algorithms typically consist of the following steps:
  - Initialize the dictionary with some predefined symbols or codes.
  - Read a symbol or a sequence of symbols from the input data.
  - Search the dictionary for a matching entry. If found, output the corresponding code and update the dictionary with a new entry that combines the previous and current symbols or sequences. If not found, output the symbol or sequence as it is and add it to the dictionary as a new entry.
  - Repeat until the end of the input data is reached.
- Adaptive dictionary algorithms have some advantages and disadvantages, such as:
  - Advantages:
    - They can handle any type of data, not just plain text.
    - They can achieve high compression ratios for data with repetitive patterns or structures.
    - They do not require prior knowledge of the data or a fixed dictionary size.
  - Disadvantages:
    - They may require more memory and processing time to maintain and search the dictionary.
    - They may suffer from dictionary overflow or degradation if the dictionary becomes too large or contains too many obsolete entries.
    - They may not be compatible with other compression algorithms or standards.