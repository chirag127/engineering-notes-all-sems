# V.42 bits

- V.42 bits are the units of data that are transmitted and received by modems that use the V.42bis standard for data compression.
- V.42bis is an international standard adopted by the CCITT in 1990, and is widely used by modem manufacturers and network operators.
- V.42bis is based on the Lempel-Ziv dynamic dictionary approach, which compresses data by replacing repeated sequences of symbols with shorter codes from a dictionary that is updated as new data is processed.
- V.42bis can achieve compression ratios of up to 4:1 for text and 2:1 for binary data, depending on the characteristics of the data and the size of the dictionary.
- V.42bis can also switch to transparent mode, in which data is transmitted uncompressed, when the compression ratio is low or the data is already compressed by another method.
- V.42bis uses a tree structure to store and search the dictionary, which is divided into two parts: a static part that contains the 256 ASCII characters, and a dynamic part that contains up to 2048 variable-length codes that are assigned to new sequences as they are encountered.
- V.42bis also uses a technique called delayed innovation, which allows the encoder to send a code that is not yet in the decoder's dictionary, by sending the code of its parent node and the symbol that follows it.
- V.42bis also uses a limited recycling mechanism, which discards the least recently used codes from the dynamic dictionary when it is full, and replaces them with new codes.
- V.42bis is compatible with the V.42 standard for error correction, which uses the LAPM (Link Access Procedure for Modems) protocol to detect and correct errors in the data transmission.
- V.42bis is suitable for implementation on a contemporary modem with an 8-bit microprocessor, 40 Kbytes of RAM, 32 Kbytes of ROM, a 9.6 KBaud V.32 modem-modem connection, and a 19.2 KBaud EIA-232-D modem-terminal connection.