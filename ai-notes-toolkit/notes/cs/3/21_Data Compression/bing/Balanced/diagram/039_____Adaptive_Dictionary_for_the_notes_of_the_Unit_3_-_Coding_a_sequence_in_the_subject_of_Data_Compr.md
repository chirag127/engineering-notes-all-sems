### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel.
- LZ77 uses a sliding window to find matches between the current data and the previous data, and encodes the matches as pointers to the window.
- LZ78 uses a tree structure to store the dictionary, and encodes the data as indices to the tree nodes.
- LZW uses a hash table to store the dictionary, and encodes the data as codes that correspond to the hash table entries.
- Adaptive dictionary can compress data that is not plain text, such as audio or video data, by building the dictionary based on the source data .
- Adaptive dictionary can also handle data that has varying patterns or frequencies, by updating the dictionary accordingly .
- Adaptive dictionary can achieve high compression ratios, especially for large and repetitive data, but it may also incur some overheads, such as the size of the dictionary and the complexity of the algorithm .