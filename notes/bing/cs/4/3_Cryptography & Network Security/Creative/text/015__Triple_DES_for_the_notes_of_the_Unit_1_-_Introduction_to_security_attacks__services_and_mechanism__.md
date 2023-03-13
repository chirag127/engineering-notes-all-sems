### Triple DES

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block .
- It is a simple method of increasing the key size of DES to protect against brute-force attacks, without the need to design a new block cipher algorithm.
- The key size of 3DES is 168 bits, but due to the meet-in-the-middle attack, the effective security it provides is only 112 bits.
- 3DES uses the same key to encrypt and decrypt information in fixed-length blocks of 64 bits .
- 3DES can operate in different modes, such as Electronic Codebook (ECB), Cipher Block Chaining (CBC), Cipher Feedback (CFB), Output Feedback (OFB), and Counter (CTR).
- 3DES is based on a Feistel network, which consists of 16 rounds of encryption or decryption, each using a 48-bit subkey derived from the main key.
- 3DES is slower than other modern block ciphers, such as AES, and is vulnerable to some attacks, such as differential cryptanalysis and linear cryptanalysis .
- 3DES is being phased out by the National Institute of Standards and Technology (NIST) and other organizations, and is recommended to be replaced by AES .