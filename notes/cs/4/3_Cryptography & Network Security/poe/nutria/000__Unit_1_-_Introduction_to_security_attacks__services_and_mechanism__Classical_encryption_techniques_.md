

## Unit 1 - Introduction to Security Attacks, Services and Mechanisms

- Security attacks: A security attack is any attempt to gain unauthorized access to a system and its resources, or to disrupt the normal operations of a system.
- Services: A service is a set of functions provided by a computer system to another computer system or to an end user.
- Mechanisms: A mechanism is a set of rules, procedures, and processes used to control the behavior of a system.

### Classical Encryption Techniques
- Substitution ciphers: Substitution ciphers involve replacing one character with another character or symbol. Examples include the Caesar cipher and the Atbash cipher.
- Transposition ciphers: Transposition ciphers involve rearranging the order of the characters in a message. Examples include the Rail Fence cipher and the Columnar Transposition cipher.
- Cryptanalysis: Cryptanalysis is the process of attempting to break a cipher by analyzing the patterns in the ciphertext.
- Steganography: Steganography is the process of hiding a secret message within an ordinary message in such a way that the secret message is not visible.

### Stream and Block Ciphers
- Stream ciphers: Stream ciphers encrypt data one bit or one byte at a time, and are typically used for encrypting real-time data streams.
- Block ciphers: Block ciphers encrypt data in blocks of fixed size, and are typically used for encrypting files or larger amounts of data.

### Modern Block Ciphers
- Block ciphers principles: Block ciphers use a symmetric key to encrypt data in blocks of fixed size. The key is used to generate a set of round keys, which are used to encrypt and decrypt the data.
- Shannon’s theory of confusion and diffusion: Shannon’s theory states that a cipher should make the relationship between the plaintext and the ciphertext as difficult to determine as possible. This is achieved by introducing randomness into the encryption process, and by making sure that small changes in the plaintext result in large changes in the ciphertext.
- Fiestal structure: The Fiestal structure is a structure used in modern block ciphers to achieve confusion and diffusion. It consists of a series of rounds, each of which performs a specific set of operations on the data.
- Data Encryption Standard (DES): DES is a symmetric key block cipher developed by IBM in the 1970s. It uses a 56-bit key and is considered to be vulnerable to brute force attacks.
- Strength of DES: DES is considered to be vulnerable to brute force attacks due to its relatively small key size.
- Idea of differential cryptanalysis: Differential cryptanalysis is a technique used to analyze the structure of a cipher and find weaknesses that can be exploited.
- Block cipher modes of operations: Block cipher modes of operations specify how a block cipher should be used to encrypt data. Examples include Electronic Codebook (ECB) and Cipher Block Chaining (CBC).
- Triple DES: Triple DES (3DES) is a variant of DES that uses three rounds of encryption instead of one. It is considered to be more secure than DES, but is still vulnerable to brute force attacks.