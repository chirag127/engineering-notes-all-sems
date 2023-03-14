 Here is the content in markdown format for Triple DES for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

### Triple DES

- Triple DES or 3DES is a symmetric-key block cipher, which applies the Data Encryption Standard (DES) cipher algorithm three times to each data block.
- It was designed to replace the original DES algorithm after it was found to be vulnerable.
- The key size is increased to 168 or 192 bits (depending on the variant) to avoid brute-force attacks.
- The encryption process for 3DES involves applying DES encryption, then DES decryption, and then DES encryption again, with two or three different keys. This greatly increases the complexity of cracking the algorithm.
- However, 3DES is slower and has a smaller block size than modern ciphers like AES. Hence, it is not recommended for new systems and is mostly used for legacy systems.

Mnemonics:
Three rounds of DES - Encrypt-Decrypt-Encrypt (EDE)
Key size increased to 168/192 bits
Slower but more secure than DES
Used for legacy systems due to compatibility

Advantages:
- Increased security over DES due to longer key size and triple encryption
- Backwards compatible with DES

Disadvantages:
- Slower than modern ciphers like AES
- Small block size of 64 bits
- Susceptible to meet-in-the-middle attacks due to reusing the same algorithm multiple times

Applications:
- Used in legacy banking systems and networks for compatibility
- SSL/TLS for securing web communications (though AES is preferred now)