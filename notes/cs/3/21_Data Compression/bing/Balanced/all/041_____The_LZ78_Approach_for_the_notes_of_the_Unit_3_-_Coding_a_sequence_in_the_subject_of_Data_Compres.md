# The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978 .
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- LZ78 takes advantage of a dictionary-based data structure to compress the data. The dictionary is initialized with all possible single characters as entries .
- The algorithm works as follows :
  - Read the next character from the input.
  - If the current token (the longest sequence of characters that has been seen so far) followed by the next character is already in the dictionary, append the next character to the current token and repeat this step.
  - Otherwise, output a pair of numbers: the index of the current token in the dictionary and the next character. Then, add the current token followed by the next character to the dictionary as a new entry. Reset the current token to empty and go back to the first step.
  - If the end of the input is reached, output the index of the current token in the dictionary and a special end-of-file symbol.
- LZ78 is the basis for many variations and extensions, such as LZW, LZSS, LZMA and others .
- LZ78 has some advantages and disadvantages compared to other compression algorithms :
  - Advantages:
    - It does not require a sliding window or a look-ahead buffer, which reduces the memory usage and complexity.
    - It adapts well to changes in the input data, as the dictionary is dynamically updated.
    - It can achieve high compression ratios for repetitive and structured data, as the dictionary entries can grow arbitrarily long.
  - Disadvantages:
    - It requires a large dictionary size to store all possible token sequences, which may exceed the available memory or the output size limit.
    - It may produce long and redundant output codes for rare or random data, as the dictionary entries may not match the input well.
    - It may suffer from dictionary pollution, where the dictionary is filled with useless or outdated entries that reduce the compression efficiency.