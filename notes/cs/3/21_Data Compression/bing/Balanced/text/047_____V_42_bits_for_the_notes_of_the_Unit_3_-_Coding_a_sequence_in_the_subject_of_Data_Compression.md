### V.42 bits for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- V.42bis is a data compression standard for data circuit terminating equipment (DCE) using error correcting procedures .
- It was adopted by the CCITT (now ITU-T) in 1990 and is widely used by modem manufacturers and network operators .
- It is based on the Lempel-Ziv-Welch (LZW) algorithm, which is a variant of the Ziv-Lempel family of algorithms for lossless data compression .
- It uses a dictionary-based approach, where sequences of input symbols are encoded as codes that refer to entries in a dictionary. The dictionary is dynamically updated as new sequences are encountered .
- It can achieve compression ratios of up to 4:1 for text and 2:1 for binary data, depending on the characteristics of the input data and the size of the dictionary .
- It operates in two modes: transparent mode and compressed mode. In transparent mode, the data is transmitted without compression. In compressed mode, the data is compressed using the LZW algorithm and the dictionary .
- It uses a negotiation procedure to establish the compression parameters, such as the dictionary size, the escape character, and the compression mode. The negotiation is done using the V.42 protocol, which also provides error correction and flow control .
- It uses a special escape character to switch between transparent mode and compressed mode, and to indicate the end of a compressed data block. The escape character is chosen by the DCE during the negotiation and is not used in the input data .
- It uses a limited recycling library, which means that the dictionary is not reset after each compressed data block, but only when it is full. This allows for better compression performance, but also introduces some overhead and complexity .
- It uses a delayed innovation technique, which means that the dictionary is updated only after a code has been transmitted, not before. This reduces the number of escape characters needed, but also increases the latency and the memory requirements .