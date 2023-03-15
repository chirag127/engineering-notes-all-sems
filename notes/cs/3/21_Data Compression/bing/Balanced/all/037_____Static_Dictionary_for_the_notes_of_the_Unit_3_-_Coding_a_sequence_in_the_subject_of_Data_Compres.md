# Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression is fast and simple, but it may not be optimal for data that has a variable or unknown distribution.
- Static dictionary compression can be implemented by using a priming text, a hashing function, or a trie data structure .
- A priming text is a known text that is used to initialize the compression algorithm, but is not transmitted with the compressed data. The compression algorithm can use the priming text as a reference to encode the input data.
- A hashing function is a function that maps a phrase or a symbol to a code, such that different phrases or symbols have different codes. The compression algorithm can use the hashing function to look up the codes for the input data in the static dictionary.
- A trie is a tree-like data structure that stores the phrases or symbols in the static dictionary as paths from the root node to the leaf nodes. The compression algorithm can use the trie to traverse the input data and find the longest matching phrases or symbols in the static dictionary.