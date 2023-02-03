### Stream and block ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security

Stream Ciphers:
- A stream cipher is a symmetric key cipher that encrypts/decrypts one bit or byte at a time
- Stream ciphers operate on a continuous stream of data and generate a keystream that is XORed with the plaintext to produce ciphertext
- Examples of stream ciphers include RC4, Salsa20, and ChaCha20

Block Ciphers:
- A block cipher is a symmetric key cipher that encrypts/decrypts fixed-sized blocks of data, usually 64 or 128 bits at a time
- Block ciphers use a key to transform the plaintext into ciphertext
- Block ciphers are widely used in modern cryptography, including AES and Blowfish

Shannon’s theory of confusion and diffusion:
- Developed by Claude Shannon in 1949, it is a mathematical theory that explains how to design a secure cipher
- Confusion refers to the relationship between the plaintext and the ciphertext, making it difficult to determine the plaintext from the ciphertext
- Diffusion refers to the spreading of plaintext over the ciphertext, making it difficult to determine the plaintext from a small portion of the ciphertext

Fiestal Structure:
- Developed by Horst Fiestal, it is a structure used in block ciphers to ensure that each bit of the plaintext affects many bits of the ciphertext
- The Fiestal structure is used in many modern block ciphers, including DES and AES

Data Encryption Standard (DES):
- Developed in the 1970s by IBM and the National Bureau of Standards, it is a widely used block cipher
- DES uses a 56-bit key and encrypts 64-bit blocks of data
- Despite its widespread use, DES has been found to be vulnerable to attack and is no longer considered secure

Triple DES:
- An extension of DES that uses three keys and encrypts data three times to increase security
- Triple DES is still widely used, but is being replaced by more secure ciphers such as AES.
