
## Unit 1 - Introduction to Security Attacks, Services and Mechanisms

Security attacks, services and mechanisms are essential components of computer security. In this unit, we will discuss the different types of security attacks, services and mechanisms, as well as classical encryption techniques and modern block ciphers. 

### Classical Encryption Techniques

Classical encryption techniques include substitution ciphers and transposition ciphers. Substitution ciphers involve replacing each letter of the plaintext with another letter or symbol to create the ciphertext. Transposition ciphers involve rearranging the letters of the plaintext to create the ciphertext. Cryptanalysis is the study of methods for obtaining the plaintext or key from the ciphertext without knowledge of the encryption algorithm. Steganography is the practice of concealing a message within an image or other file. 

### Stream and Block Ciphers

Stream ciphers are encryption algorithms that encrypt a single bit or byte at a time. Block ciphers are encryption algorithms that encrypt a block of bits or bytes at a time. 

### Modern Block Ciphers

Modern block ciphers are based on the principles of Shannon's theory of confusion and diffusion. This theory states that an encryption algorithm should make the relationship between the plaintext and the ciphertext as complex and unpredictable as possible. The Feistel structure is a common design for modern block ciphers. 

The Data Encryption Standard (DES) is a popular block cipher that encrypts 64-bit blocks of plaintext using a 56-bit key. The strength of DES lies in its key length, as a 56-bit key is long enough to make brute-force attacks impractical. The idea of differential cryptanalysis was developed to attack DES, but it is not practical for long keys. 

Block cipher modes of operation are used to encrypt longer messages without repeating the same encryption key. The most popular block cipher mode of operation is the Electronic Codebook (ECB) mode. The Cipher Block Chaining (CBC) mode is also popular and uses an initialization vector (IV) to avoid repeating the same encryption key. Triple DES (3DES) is a popular block cipher that encrypts data three times using two or three different keys.