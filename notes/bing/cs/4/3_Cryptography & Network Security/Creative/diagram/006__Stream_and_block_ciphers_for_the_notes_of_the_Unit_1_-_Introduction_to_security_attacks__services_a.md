The following is a detailed ASCII diagram for stream and block ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
Stream Cipher:

Plaintext:  P1 P2 P3 P4 P5 P6 P7 P8 ...
Key:        K
Keystream:  S1 S2 S3 S4 S5 S6 S7 S8 ...
Ciphertext: C1 C2 C3 C4 C5 C6 C7 C8 ...


Pseudorandom bit generator
        |
        | K
        V
    +-------+
    |       |----> S1
    |       |----> S2
    |       |----> S3
    |       |----> S4
    |       |----> ...
    +-------+

Encryption: Ciphertext = Plaintext XOR Keystream
Decryption: Plaintext = Ciphertext XOR Keystream

Block Cipher:

Plaintext:  P1 P2 P3 P4 P5 P6 P7 P8 ...
Key:        K
Ciphertext: C1 C2 C3 C4 C5 C6 C7 C8 ...


Block cipher algorithm
        |
        | K
        V
    +-------+
    |       |----> E(P1) = C1
    |       |----> E(P2) = C2
    |       |----> E(P3) = C3
    |       |----> E(P4) = C4
    |       |----> ...
    +-------+

Encryption: Ciphertext = E(Plaintext)
Decryption: Plaintext = D(Ciphertext)
```