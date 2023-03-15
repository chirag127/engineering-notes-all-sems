### Diagram Coding

Diagram coding is a lossless data compression method that uses pairs of symbols (digrams) to reduce the size of the source data. It works by finding the most frequent digrams in the data and assigning them codes that correspond to unused symbols, if any. The data is then scanned and replaced by the codes whenever a digram is found. This process can be repeated iteratively until no more compression is possible or the dictionary is full.

Some features of diagram coding are:

- It is an ad hoc method, meaning it does not rely on any prior knowledge of the data or its statistics.
- It is a semi-static method, meaning it builds the dictionary dynamically during the compression, but does not update it during the decompression.
- It is a variable-length method, meaning it uses different number of bits for different symbols or digrams.
- It is a prefix-free method, meaning no code is a prefix of another code, which allows for easy decoding.

An example of diagram coding is:

- Suppose the source data is `ABRACADABRA`.
- The alphabet is `A, B, C, D, R`, and the unused symbols are `E, F, G, H, ...`.
- The most frequent digrams are `AB` and `RA`, each occurring 3 times.
- Assign the code `E` to `AB` and the code `F` to `RA`.
- Scan the data and replace the digrams by the codes: `EEFCADEEF`.
- The compressed data is 9 symbols long, while the original data is 11 symbols long, achieving a compression ratio of 81.8%.