### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Diagram coding is a technique used in data compression to encode a sequence of symbols.
2. It is based on the idea of representing a sequence of symbols as a single code, rather than encoding each symbol individually.
3. This is achieved by building a dictionary of commonly occurring symbol pairs or diagrams and assigning them unique codes.
4. As the sequence is processed, pairs of symbols are replaced with their corresponding code from the dictionary.
5. If a pair of symbols is not found in the dictionary, it is added to the dictionary and assigned a new code.
6. This process continues until the entire sequence has been encoded.
7. Diagram coding can achieve higher compression ratios than individual symbol coding, as it takes advantage of the correlations between adjacent symbols in the sequence.
8. However, it requires more computational resources and memory to build and maintain the dictionary.
9. Examples of diagram coding algorithms include LZ77 and LZ78, which are commonly used in data compression applications.
