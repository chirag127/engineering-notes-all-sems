### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It operates by taking many pairs of plaintexts with fixed xor difference, and looking at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys. As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- It is usually launched as an adaptive chosen plaintext attack; the attacker chooses the plaintext to be encrypted (but does not know the key) and then encrypts related plaintexts.
- It studies how the differences evolve through the various rounds and various operations of the cipher.
- It is based on the assumption that the exclusive-or (XOR) operation is the difference operation.
- It was first introduced by Biham and Shamir in 1990 as a technique to break the Data Encryption Standard (DES) cipher.
- It can also be used to analyze other block ciphers, such as FEAL, Khufu, Khafre, REDOC, LOKI, and GOST.
- It can also be extended to deal with other difference operations, such as modular addition, subtraction, or rotation.