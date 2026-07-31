# Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Static dictionary compression is a technique that uses a fixed set of entries to replace phrases or symbols in the input data with shorter codes .
- The static dictionary can be derived from prior knowledge of the data source, or from a sample of the data that is representative of the whole .
- Static dictionary compression is fast and simple, but it may not be optimal for data that has a different or unknown distribution than the dictionary .
- Static dictionary compression can be implemented by using a priming text, a hashing function, or a trie data structure .
- A priming text is a known text that is compressed along with the input data, but only the compressed input data is transmitted. The receiver can use the priming text to reconstruct the dictionary and decompress the data.
- A hashing function is a function that maps phrases or symbols to codes, such that the codes are unique and have a fixed length. The dictionary can be stored as a hash table, where the codes are the keys and the phrases or symbols are the values.
- A trie is a tree data structure that stores phrases or symbols as paths from the root to the leaves. Each node in the trie has a code that is appended to the code of its parent. The dictionary can be stored as a trie, where the codes are the paths and the phrases or symbols are the leaves.