### V.42 bits

- V.42 bits are the bits used by the V.42bis standard for data compression procedures for data circuit terminating equipment (DCE) using error correcting procedures.
- V.42bis is a data compression standard adopted by the CCITT (now ITU-T) in 1990, based on the Lempel-Ziv-Welch (LZW) algorithm and some modifications by British Telecom (BT)  .
- V.42bis can compress text data up to 4:1 and binary data up to 2:1, depending on the data characteristics and the compression history  .
- V.42bis operates on a byte-by-byte basis, using a dictionary of 512 to 65536 entries, each containing a variable-length string of bytes  .
- V.42bis uses two modes of operation: transparent mode and compressed mode. In transparent mode, the data is transmitted as is, without compression. In compressed mode, the data is encoded using the dictionary and a variable-length code  .
- V.42bis switches between the two modes dynamically, depending on the compression ratio achieved and the occurrence of control characters or escape sequences  .
- V.42bis also supports a feature called delayed innovation, which allows the encoder to transmit a new dictionary entry before it is actually used, thus saving bits and improving compression  .
- V.42bis can work with any error-correcting DCE that conforms to the V.42 standard, such as V.32, V.32bis, V.34, etc.  .
- V.42bis is widely used by modem manufacturers and is also applied to local and remote area networks (LANs, WANs)  .