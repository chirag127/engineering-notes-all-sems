### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing information or quality.
- Dictionary compression is a type of data compression that uses a predefined or adaptive dictionary of symbols or patterns to encode the data.
- Adaptive dictionary compression is a variant of dictionary compression that builds the dictionary dynamically based on the data being compressed, rather than using a fixed or predefined dictionary.
- Adaptive dictionary compression can achieve better compression ratios than static dictionary compression, especially for data that is not plain text or has a specific structure or distribution.
- Adaptive dictionary compression can also adapt to changes in the data over time, such as new words or symbols, or different frequencies or contexts of occurrence.
- Some examples of adaptive dictionary compression algorithms are LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel, and Welch.
- LZ77 and LZ78 use a sliding window or a trie data structure, respectively, to store the dictionary and search for matches in the data.
- LZW uses a hash table to store the dictionary and assign codes to the symbols or patterns. It is widely used in UNIX compress, GIF, and PDF formats.
- Adaptive dictionary compression algorithms have some drawbacks, such as memory and computational overhead, complexity of implementation, and possible patent issues.