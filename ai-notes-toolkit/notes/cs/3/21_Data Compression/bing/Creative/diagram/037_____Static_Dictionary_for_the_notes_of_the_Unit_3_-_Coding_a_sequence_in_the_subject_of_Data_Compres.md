### Static Dictionary

- A static dictionary is a fixed set of symbols and their corresponding codes that are used to compress and decompress a sequence of symbols.
- A static dictionary is usually predefined and known to both the encoder and the decoder, so it does not need to be transmitted along with the compressed data.
- A static dictionary can be optimal for compressing a sequence if the dictionary matches the probability distribution of the symbols in the sequence.
- A static dictionary can be inefficient or ineffective for compressing a sequence if the dictionary does not match the probability distribution of the symbols in the sequence, or if the sequence contains symbols that are not in the dictionary.
- A static dictionary can be implemented using various data structures, such as arrays, hash tables, trees, or tries.
- A static dictionary can be designed using various methods, such as Huffman coding, arithmetic coding, or Lempel-Ziv coding.