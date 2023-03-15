### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel.
- LZ77 uses a sliding window to find matches between the current data and the previous data, and encodes the matches as references to the window positions and lengths.
- LZ78 uses a tree structure to store the prefixes of the data, and encodes the data as references to the tree nodes and the next symbols.
- LZW uses a hash table to store the prefixes of the data, and encodes the data as references to the table entries.
- Adaptive dictionary can compress data that is not plain text, such as audio or video, by building the dictionary from the data itself .
- Adaptive dictionary can also handle data that has varying patterns or frequencies, by updating the dictionary accordingly .
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data, but it may also incur some overheads, such as the dictionary size and the encoding complexity  .