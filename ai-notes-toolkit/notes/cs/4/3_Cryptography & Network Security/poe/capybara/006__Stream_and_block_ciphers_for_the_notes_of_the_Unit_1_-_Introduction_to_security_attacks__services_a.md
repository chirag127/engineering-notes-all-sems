### Stream and Block Ciphers

Cryptography is the study of techniques for secure communication in the presence of third parties. In this unit, we will study various encryption techniques, including substitution ciphers, transposition ciphers, cryptanalysis, steganography, stream ciphers, and block ciphers.

#### Classical Encryption Techniques

- Substitution ciphers: These ciphers replace plaintext letters with ciphertext letters using a fixed system. Examples include Caesar cipher and Vigenere cipher.
- Transposition ciphers: These ciphers rearrange the plaintext letters without changing them. Examples include Rail fence cipher and Columnar Transposition cipher.

#### Cryptanalysis

- Cryptanalysis is the study of analyzing and breaking encryption schemes. It includes methods like frequency analysis and brute force attacks.

#### Steganography

- Steganography is the art of hiding information in plain sight. It involves embedding messages within other messages, such as images or audio files.

#### Stream Ciphers

- Stream ciphers encrypt plaintext one bit or one byte at a time, producing a stream of ciphertext bits or bytes. Examples include RC4 and A5/1.

#### Block Ciphers

- Block ciphers encrypt fixed-size blocks of plaintext, producing fixed-size blocks of ciphertext. Examples include Data Encryption Standard (DES), Advanced Encryption Standard (AES), and Blowfish.
- Principles of Block Ciphers: Shannon’s theory of confusion and diffusion, fiestal structure.
- Data Encryption Standard (DES): DES is a symmetric key algorithm that encrypts data in 64-bit blocks using a 56-bit key. It uses a fiestal structure and employs both substitution and transposition ciphers.
- Strength of DES: DES is no longer considered a secure encryption standard as it can be broken using brute force attacks.
- Idea of Differential Cryptanalysis: This is an attack technique that exploits the difference between pairs of plaintexts and their corresponding ciphertexts to recover the secret key of the encryption algorithm.
- Block Cipher Modes of Operations: These are methods of applying block ciphers to large amounts of data. Examples include Electronic Codebook (ECB) mode and Cipher Block Chaining (CBC) mode.
- Triple DES: This is a variant of DES that uses three keys and encrypts data three times. It is more secure than DES, but slower.

By understanding these encryption techniques, we can better understand the security attacks, services, and mechanisms used in cryptography and network security.