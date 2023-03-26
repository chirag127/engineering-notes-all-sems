 Here are the points on Modern Block Ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers:

1. Block ciphers principles: Block ciphers operate on fixed-length groups of bits called blocks. For example, AES encrypts 128-bit blocks with a key of predetermined length such as 128, 192, or 256 bits.

2. Shannon’s theory of confusion and diffusion: Claude Shannon proposed that a secure cipher should have confusion and diffusion properties. Confusion hides the relationship between the plaintext and the ciphertext. Diffusion spreads the influence of one plaintext symbol over many ciphertext symbols.

3. Feistel structure: A Feistel structure is commonly used in block ciphers. It uses multiple rounds of encryption where the right half of the block is encrypted using a key-dependent function with the left half acting as an input.

4. Data Encryption Standard (DES): DES is a symmetric-key block cipher with a 64-bit block size and a 56-bit key. It has 16 rounds of encryption using permutations and substitutions. It is no longer considered secure due to its small key size.

5. Strength of DES: Due to its small key size, DES can be brute force attacked with modern computing power. It is also vulnerable to related-key attacks and meet-in-the-middle attacks. Differential cryptanalysis can be applied to significantly reduce the complexity of attacking DES.

6. Idea of differential cryptanalysis: Differential cryptanalysis studies how differences in plaintext can affect the resulting differences in ciphertext. By analyzing these differentials, it may be possible to deduce information about the key. DES is vulnerable to differential cryptanalysis as its substitution-permutation network does not sufficiently diffuse differences.

7. Block cipher modes of operations: Block ciphers are used in various modes of operations to provide different security properties. Some common modes are ECB, CBC, CFB, and OFB. ECB results in similar ciphertext blocks for similar plaintext blocks, while the others solve this problem.

8. Triple DES: Triple DES or 3DES is a strengthened variant of DES that improves its security. It involves applying DES encryption three times with two or three different keys. This increases the key size to 112 or 168 bits, making brute force attacks infeasible with current technology.