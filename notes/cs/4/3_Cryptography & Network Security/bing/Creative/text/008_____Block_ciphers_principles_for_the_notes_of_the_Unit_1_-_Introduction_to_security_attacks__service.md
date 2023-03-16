### Block ciphers principles

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- A block cipher consists of two functions: an encryption function E that maps a plaintext block P and a secret key K to a ciphertext block C, and a decryption function D that maps C and K back to P.
- A block cipher can be represented as E: {0,1}^n x {0,1}^k -> {0,1}^n and D: {0,1}^n x {0,1}^k -> {0,1}^n, where n is the block size and k is the key size.
- A block cipher should satisfy the following properties:
  - Correctness: D(K, E(K, P)) = P for any P and K.
  - Security: Given a ciphertext C, it should be computationally infeasible to find P or K without knowing K.
  - Efficiency: E and D should be fast and easy to implement in hardware or software.
- A block cipher can be designed using different techniques, such as substitution-permutation networks, Feistel networks, or other structures.
- A block cipher can be used in different modes of operation, such as electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), or counter (CTR), to encrypt a message of arbitrary length. Each mode has different advantages and disadvantages in terms of security, efficiency, and error propagation.