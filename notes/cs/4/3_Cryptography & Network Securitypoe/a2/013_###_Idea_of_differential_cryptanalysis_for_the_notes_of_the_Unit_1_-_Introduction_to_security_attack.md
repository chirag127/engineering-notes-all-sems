 Here is the content in markdown format:

### Idea of differential cryptanalysis for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

Differential cryptanalysis is a chosen plaintext attack on block ciphers. It analyzes the differences in the ciphertext produced by encrypting two plaintexts which differ in a few bits (also known as differential). If the differences in the ciphertext can be predicted, it can lead to the derivation of the key used.

The steps involved in differential cryptanalysis are:

1. Select a pair of plaintexts (P1, P2) which differ in a known way (one or more bits are flipped).
2. Encrypt the plaintexts using the cipher and obtain the corresponding ciphertexts (C1, C2).
3. Analyze the differences in the ciphertexts (C1 ⊕ C2). If the differences can be predicted, it reveals some information about the key.
4. Repeat the above steps with multiple pairs of plaintexts and analyze the results to deduce more bits of the key.
5. Once sufficient bits of the key are determined, exhaustive search can be used to find the actual key.

The time complexity of differential cryptanalysis depends on the number of rounds in the cipher and the probability of the differentials occurring. Ciphers with high number of rounds and low probability of predictable differentials are resistant to differential cryptanalysis. Some ways to achieve this are - using sboxes that output a uniform distribution of outputs for a given set of inputs, using rounds with strong diffusion properties, and using whitening techniques.

Some of the advantages of differential cryptanalysis are:

- It can be automated and scaled to attack ciphers with large keys.
- It does not require a large amount of data to be effective.

The disadvantages are:

- It may not be effective against ciphers with a high number of rounds.
- It requires a large computational power to find pairs of plaintexts and analyze the differences.