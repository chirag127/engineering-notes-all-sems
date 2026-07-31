### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It operates by taking many pairs of plaintexts with fixed xor difference, and looking at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys. As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- It is usually launched as an adaptive chosen plaintext attack; the attacker chooses the plaintext to be encrypted (but does not know the key) and then encrypts related plaintexts.
- It studies how the differences evolve through the various rounds and various operations of the cipher.
- It is based on the assumption that the exclusive-or (XOR) operation is the difference operation.
- It can be used to find weaknesses in the design of block ciphers, such as DES, and to mount attacks on reduced-round versions of them .