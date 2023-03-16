## Unit 1 - Introduction to security attacks, services and mechanism

1. Security attacks: Security attacks are attempts to exploit vulnerabilities in a system to gain unauthorized access or disrupt normal operations. These attacks can be classified into two categories: passive attacks and active attacks. Passive attacks involve eavesdropping on communications, while active attacks involve modifying or disrupting the normal functioning of a system.

2. Security services: Security services are measures put in place to protect against security attacks. These services include authentication, access control, data confidentiality, data integrity, and non-repudiation.

3. Security mechanisms: Security mechanisms are the tools and techniques used to implement security services. These mechanisms include encryption, digital signatures, firewalls, intrusion detection systems, and security protocols.

## Classical encryption techniques

1. Substitution ciphers: Substitution ciphers are a type of encryption technique where each letter in the plaintext is replaced by another letter, number, or symbol. The most well-known substitution cipher is the Caesar cipher, where each letter is shifted by a fixed number of positions in the alphabet.

2. Transposition ciphers: Transposition ciphers are a type of encryption technique where the letters in the plaintext are rearranged according to a predetermined pattern. An example of a transposition cipher is the rail fence cipher, where the plaintext is written in a zigzag pattern along a set of rails, and the ciphertext is read off row by row.

3. Cryptanalysis: Cryptanalysis is the study of methods for breaking encryption algorithms. Cryptanalysts use various techniques, such as frequency analysis and pattern recognition, to try to recover the plaintext from the ciphertext.

4. Steganography: Steganography is the practice of hiding a message within another message, image, or file. The goal of steganography is to conceal the existence of the message, rather than to protect its contents.

## Stream and block ciphers

1. Stream ciphers: Stream ciphers encrypt data one bit or byte at a time. They use a keystream generator to produce a stream of random bits, which are combined with the plaintext using an exclusive-or (XOR) operation.

2. Block ciphers: Block ciphers encrypt data in fixed-size blocks, typically 64 or 128 bits. They use a series of mathematical operations, called rounds, to transform the plaintext into the ciphertext.

## Modern Block Ciphers

1. Block cipher principles: Block ciphers use a symmetric key, meaning the same key is used for both encryption and decryption. They operate on fixed-size blocks of data, using a series of rounds to transform the plaintext into the ciphertext.

2. Shannon’s theory of confusion and diffusion: Shannon’s theory of confusion and diffusion states that a good encryption algorithm should have two properties: confusion and diffusion. Confusion means that the relationship between the plaintext and the ciphertext should be complex, making it difficult for an attacker to determine the key. Diffusion means that the ciphertext should be spread out over the entire message, making it difficult for an attacker to determine the structure of the plaintext.

3. Fiestal structure: The Fiestal structure is a common design for block ciphers. It involves dividing the block of data into two halves and processing each half separately, using a series of rounds that involve substitution and permutation operations.

4. Data Encryption Standard (DES): DES is a widely-used block cipher that was developed in the 1970s. It uses a 56-bit key and operates on 64-bit blocks of data. DES is considered to be insecure due to its small key size, and has been replaced by more secure algorithms such as AES.

5. Strength of DES: The strength of DES lies in its use of a large number of rounds and its complex key schedule. However, its small key size makes it vulnerable to brute-force attacks.

6. Idea of differential cryptanalysis: Differential cryptanalysis is a technique for breaking block ciphers by analyzing the differences between pairs of plaintexts and their corresponding ciphertexts. It can be used to recover the key used by the cipher.

7. Block cipher modes of operation: Block ciphers can be used in several different modes of operation, including Electronic Codebook (ECB), Cipher Block Chaining (CBC), and Counter (CTR) mode. Each mode has its own advantages and disadvantages, and the choice of mode depends on the specific requirements of the application.

8. Triple DES: Triple DES is a variant of DES that applies the DES algorithm three times to each block of data. It uses two or three keys, and provides a higher level of security than DES. However, it is slower than other modern block ciphers such as AES.