### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel .
- LZ77 uses a sliding window to store the most recent data and find matches with the current data. It encodes the data as a pair of offset and length, indicating how far back in the window the match is and how long it is .
- LZ78 uses a tree structure to store the data and find matches with the current data. It encodes the data as a pair of index and symbol, indicating the position of the match in the tree and the next symbol after the match .
- LZW is a variation of LZ78 that uses a hash table instead of a tree to store the data and find matches. It encodes the data as a single index, indicating the position of the match in the table .
- Adaptive dictionary can compress data that is stored within data rows, including inlined LOB or XML values . It can also compress data that is not plain text, such as audio or video data.
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data. However, it may also incur some overheads, such as memory usage, dictionary management, and decompression speed .