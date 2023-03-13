The following is a detailed ASCII diagram for services and mechanism for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

### Services and Mechanism

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Confidentiality|     |  Integrity      |     |  Authentication |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Encryption     |     |  Hashing        |     |  Digital        |
|  Decryption     |     |  MAC            |     |  Signature      |
|                 |     |                 |     |  Certificate    |
+-----------------+     +-----------------+     +-----------------+
```

### Classical Encryption Techniques

```
+-----------------+     +-----------------+
|                 |     |                 |
|  Substitution   |     |  Transposition  |
|  Cipher         |     |  Cipher         |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Caesar Cipher  |     |  Rail Fence     |
|  Monoalphabetic |     |  Cipher         |
|  Cipher         |     |                 |
|  Polyalphabetic |     |  Columnar       |
|  Cipher         |     |  Transposition  |
|  Playfair Cipher|     |  Cipher         |
|  Hill Cipher    |     |                 |
|  Vigenere Cipher|     |  Route Cipher   |
|                 |     |                 |
+-----------------+     +-----------------+
```

### Cryptanalysis

```
+-----------------+
|                 |
|  Cryptanalysis  |
|                 |
+-----------------+
|                 |
|  Frequency      |
|  Analysis       |
|                 |
|  Brute Force    |
|  Attack         |
|                 |
|  Known-Plaintext|
|  Attack         |
|                 |
|  Chosen-Plaintext|
|  Attack         |
|                 |
|  Ciphertext-Only|
|  Attack         |
|                 |
+-----------------+
```

### Steganography

```
+-----------------+
|                 |
|  Steganography  |
|                 |
+-----------------+
|                 |
|  Text           |
|  Steganography  |
|                 |
|  Image          |
|  Steganography  |
|                 |
|  Audio          |
|  Steganography  |
|                 |
|  Video          |
|  Steganography  |
|                 |
+-----------------+
```

### Stream and Block Ciphers

```
+-----------------+     +-----------------+
|                 |     |                 |
|  Stream Cipher  |     |  Block Cipher   |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Synchronous    |     |  ECB            |
|  Stream Cipher  |     |                 |
|                 |     |  CBC            |
|  Asynchronous   |     |                 |
|  Stream Cipher  |     |  CFB            |
|                 |     |                 |
|  RC4            |     |  OFB            |
|                 |     |                 |
|  A5/1           |     |  CTR            |
|                 |     |                 |
+-----------------+     +-----------------+
```

### Modern Block Ciphers

```
+-----------------+     +-----------------+
|                 |     |                 |
|  Block Cipher   |     |  DES            |
|  Principles     |     |                 |
|                 |     +-----------------+
+-----------------+     |                 |
|                 |     |  Fiestel        |
|  Confusion      |     |  Structure      |
|                 |     |                 |
|  Diffusion      |     |  S-Box          |
|                 |     |                 |
|  Avalanche      |