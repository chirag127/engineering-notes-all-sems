 Here are the notes in markdown format with formal tone and without any emojis or external links:

### Feistel Structure

- Feistel structure is a design used in many block ciphers like DES.
- It uses a structure consisting of two halves. One half is used for encryption and the other half is used for decryption.
- The structure ensures that encryption and decryption are very similar processes and ensures that the cipher is invertible.
- The Feistel structure increases the strength and security of the cipher.

### Classical Encryption Techniques

- Substitution ciphers: In substitution ciphers, each letter of the plaintext is replaced by another letter or symbol. Examples: Caesar cipher.
- Transposition ciphers: In transposition ciphers, the positions of the letters are changed according to a permutation. Examples: Rail fence cipher.
- These techniques are vulnerable to cryptanalysis and hence not secure.

### Modern Block Ciphers

- Block ciphers operate on fixed size blocks of plaintext and ciphertext. Examples: DES, AES.
- The principles of block ciphers are confusion and diffusion proposed by Shannon. Confusion hides the relationship between plaintext and ciphertext. Diffusion spreads the influence of one plaintext bit over many ciphertext bits.
- The Feistel structure is commonly used in block ciphers. It uses rounds of encryption consisting of confusion and diffusion.
- Data Encryption Standard (DES) is a block cipher with 64-bit block size and 56-bit key. It is vulnerable to brute force and differential cryptanalysis attacks due to its small key size.
- Triple DES (3DES) applies DES three times to each block to strengthen DES. It has a 112/168-bit key but is slow.
- Block cipher modes of operation describe how to repeatedly apply a block cipher to encrypt longer data. The modes prevent errors from propagating and strengthen security. Examples: ECB, CBC, CFB, OFB, CTR.

[Additional notes on other topics...]