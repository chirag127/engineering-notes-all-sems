### Stream and block ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

- Stream and block ciphers are two types of symmetric key encryption techniques that convert plaintext into ciphertext using a secret key    .
- Stream ciphers encrypt plaintext one bit or one byte at a time, while block ciphers encrypt plaintext in fixed-size blocks   .
- Stream ciphers use a key and a nonce (a random number used only once) to generate a keystream of pseudorandom bits, which is then XORed with the plaintext to produce the ciphertext   .
- Stream ciphers can be classified into synchronous and self-synchronizing stream ciphers. Synchronous stream ciphers generate the keystream independently of the plaintext and ciphertext, while self-synchronizing stream ciphers use the previous ciphertext to generate the keystream  .
- Stream ciphers are fast, simple, and suitable for applications that require continuous encryption, such as voice and video communication. However, stream ciphers are vulnerable to bit-flipping attacks, replay attacks, and keystream reuse attacks   .
- Block ciphers use a key and a block cipher algorithm to transform plaintext blocks into ciphertext blocks   .
- Block ciphers can operate in different modes, such as electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR). Each mode has different advantages and disadvantages in terms of security, efficiency, and error propagation   .
- Block ciphers are more complex, secure, and versatile than stream ciphers. They can provide both confusion and diffusion, which are two principles of secure encryption proposed by Shannon  . Confusion means that the ciphertext should not reveal any statistical relationship with the key, and diffusion means that the ciphertext should depend on every bit of the plaintext.
- Block ciphers can be designed using different structures, such as Feistel, substitution-permutation network (SPN), and balanced Feistel network (BFN). Feistel structure is a common and flexible way of building block ciphers, which consists of repeated rounds of substitution and transposition operations.
- Data encryption standard (DES) is a widely used block cipher that uses a 64-bit block size and a 56-bit key size. It is based on the Feistel structure and has 16 rounds of encryption.
- DES is considered insecure today because of its small key size, which makes it vulnerable to brute-force attacks. It also suffers from some weak keys and some known plaintext attacks, such as differential cryptanalysis and linear cryptanalysis.
- Differential cryptanalysis is a technique that exploits the differences between two plaintexts and their corresponding ciphertexts to recover the key. It is based on the observation that some input differences propagate to some output differences with a higher probability than others.
- Triple DES (3DES) is a variant of DES that applies DES three times with either two or three different keys. It is more secure than DES, but also slower and less efficient. It has a 64-bit block size and a 112-bit or 168-bit key size.

A possible mnemonic to remember the difference between stream and block ciphers is:

- Stream ciphers are like streams of water, flowing continuously and smoothly. Block ciphers are like blocks of ice, solid and fixed in shape.
- Stream ciphers use a keystream, which is like a stream of random bits. Block ciphers use a block cipher algorithm, which is like a block of mathematical operations.
- Stream c