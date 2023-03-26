 Here are the notes on Stream and block ciphers for the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

### Stream Ciphers

- Generate pseudorandom bit stream (keystream)
- Plaintext is XORed with keystream to get ciphertext
- Keystream must be unpredictable and same length as plaintext
- Fast but vulnerable to reuse of keystream
- Ex: Vernam cipher

### Block Ciphers

- Plaintext is divided into blocks and each block is encrypted individually
- Based on Shannon's theory of confusion and diffusion
- Diffusion spreads influence of plaintext widely to ciphertext
- Confusion makes relationship between key and ciphertext complex
- Ex: DES, AES

### Block Cipher Modes of Operation

- ECB: Simple but vulnerable to reuse attacks
- CBC: Cipher block chaining - each block depends on previous ciphertext block
- CFB: Cipher feedback - each block depends on previous ciphertext feedback
- OFB: Output feedback - each block depends on previous output feedback
- CTR: Counter mode - uses a counter to generate keystream

### DES

- Data Encryption Standard - 64-bit block, 56-bit key
- Based on Feistel structure with 16 rounds of encryption
- Weak key schedule and small key space
- Triple DES applies DES three times to increase security
- Vulnerable to related-key attack and meet-in-the-middle attack