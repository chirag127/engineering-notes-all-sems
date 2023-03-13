### Block ciphers principles for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

- A block cipher is a deterministic algorithm operating on fixed-length groups of bits, called blocks.
- A block cipher consists of two paired algorithms, one for encryption, E, and the other for decryption, D.
- Both algorithms accept two inputs: an input block of size n bits and a key of size k bits; and both yield an n-bit output block.
- The decryption algorithm D is defined to be the inverse function of encryption, i.e., D = E−1.
- Block ciphers are specified elementary components in the design of many cryptographic protocols and are widely used to encrypt large amounts of data, including in data exchange protocols.
- Block ciphers can be classified into two types: symmetric-key block ciphers and public-key block ciphers.
- Symmetric-key block ciphers use the same key for both encryption and decryption, while public-key block ciphers use different keys for encryption and decryption.
- Block ciphers can also be categorized based on their structure: substitution-permutation network (SPN) and Feistel network.
- SPN is a network of simple operations, such as substitution (S-box) and permutation (P-box), that are applied to the input block in several rounds.
- Feistel network is a network of rounds, each consisting of a function F that operates on half of the input block and an exclusive-or (XOR) operation that combines the output of F with the other half of the input block.
- Block cipher principles are the design criteria that determine the security and efficiency of a block cipher .
- Some of the block cipher principles are:

  - Number of rounds: The number of rounds judges the strength of the block cipher algorithm. It is considered that more rounds increase the security of the cipher, but also increase the complexity and the time required for encryption and decryption .
  - Design of function F: The function F of the block cipher must be designed such that it must be impossible for any attacker to find the key or the plaintext from the ciphertext, even with the knowledge of F. The function F should also introduce confusion and diffusion in the cipher, as proposed by Shannon .
  - Key schedule algorithm: The key schedule algorithm is the algorithm that generates the subkeys for each round of the block cipher from the main key. The key schedule algorithm should be secure and efficient, and should avoid any weak keys or related keys that can compromise the security of the cipher .
  - Block size: The block size determines the amount of data that can be encrypted or decrypted at a time by the block cipher. The block size should be large enough to prevent any statistical analysis or brute-force attacks on the ciphertext, but not too large to cause inefficiency or waste of bandwidth .
  - Key size: The key size determines the number of possible keys that can be used by the block cipher. The key size should be large enough to resist any brute-force attacks or cryptanalysis on the key, but not too large to cause inefficiency or storage problems .
  - Mode of operation: The mode of operation is the way of using a block cipher to encrypt or decrypt a message that is longer than the block size. The mode of operation should provide security, efficiency, and functionality, such as confidentiality, integrity, authentication, and random access .
  - Some of the common modes of operation are: electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR) .

- Some of the modern block ciphers are: Data Encryption Standard (DES), Triple DES (3DES), Advanced Encryption Standard (AES), Blowfish, Twofish, IDEA, RC5, and RC6[^