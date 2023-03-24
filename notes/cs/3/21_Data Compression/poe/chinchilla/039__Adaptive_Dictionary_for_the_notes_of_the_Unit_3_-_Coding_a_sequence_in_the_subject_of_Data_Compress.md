### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

In the field of data compression, the adaptive dictionary is a crucial technique used to encode a sequence. It is a data structure that maintains a dictionary of previously encountered symbols or patterns and their corresponding codewords. Here are some important points to understand about adaptive dictionaries:

- An adaptive dictionary is updated on-the-fly while encoding a sequence. It starts with an empty dictionary and adds new symbols or patterns encountered in the sequence.
- The dictionary is used to assign shorter codewords to frequently occurring symbols or patterns and longer codewords to infrequently occurring ones. Thus, it helps in reducing the overall length of the encoded sequence.
- The technique of using an adaptive dictionary is known as adaptive coding. It is different from the static coding, where the dictionary is fixed and known to both the encoder and decoder.
- The most widely used adaptive dictionary-based compression technique is the Lempel-Ziv algorithm. It uses a sliding window to search for previously encountered patterns and adds new patterns to the dictionary.
- The Lempel-Ziv algorithm is further divided into two variants: LZ77 and LZ78. The former uses a sliding window and a lookahead buffer to encode a sequence, while the latter uses a trie data structure to store the dictionary.
- Adaptive dictionaries are also used in image and video compression algorithms like JPEG and MPEG. In these algorithms, a dictionary of previously encoded frames is maintained and used to encode the current frame.

In conclusion, the adaptive dictionary is an important technique used in data compression to reduce the overall length of the encoded sequence. It is updated on-the-fly while encoding the sequence and assigns shorter codewords to frequently occurring symbols or patterns. The Lempel-Ziv algorithm is the most widely used adaptive dictionary-based compression technique, which uses a sliding window and a lookahead buffer to encode a sequence.