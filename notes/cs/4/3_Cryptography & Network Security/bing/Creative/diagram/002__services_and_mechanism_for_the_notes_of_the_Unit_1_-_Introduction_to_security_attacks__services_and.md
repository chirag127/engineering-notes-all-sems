The following is a detailed ASCII diagram for services and mechanism for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

### Services and Mechanism

```
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|     Security        |     |     Security        |     |     Security        |
|     Services        |     |     Mechanisms      |     |     Attacks         |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  - Confidentiality  |     |  - Encryption       |     |  - Passive          |
|  - Authentication   |     |  - Digital          |     |  - Active           |
|  - Integrity        |     |    Signature        |     |                     |
|  - Non-repudiation  |     |  - Hash Function    |     |                     |
|  - Access Control   |     |  - MAC              |     |                     |
|  - Availability     |     |  - Challenge-       |     |                     |
|                     |     |    Response         |     |                     |
|                     |     |  - Biometrics       |     |                     |
|                     |     |  - Firewall         |     |                     |
+---------------------+     +---------------------+     +---------------------+
```

### Classical Encryption Techniques

```
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|     Substitution    |     |     Transposition   |     |     Cryptanalysis   |
|     Ciphers         |     |     Ciphers         |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  - Caesar Cipher    |     |  - Rail Fence       |     |  - Ciphertext-only  |
|  - Monoalphabetic   |     |  - Columnar         |     |  - Known-plaintext  |
|  - Playfair         |     |  - Route            |     |  - Chosen-plaintext |
|  - Hill             |     |                     |     |  - Chosen-ciphertext|
|  - Vigenere         |     |                     |     |  - Differential     |
|  - Vernam           |     |                     |     |  - Linear           |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
```

### Steganography

```
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|     Cover Medium    |     |     Embedded        |     |     Extraction      |
|                     |     |     Message         |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  - Image            |     |  - Text             |     |  - Reverse the      |
|  - Audio            |     |  - Image            |     |    embedding        |
|  - Video            |     |  - Audio            |     |    process          |
|  - Text             |     |  - Video            |     |  - Use a secret key |
|                     |     |                     |     |    or algorithm     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
```

### Stream and Block Ciphers

```
+---------------------+     +---------------------+
|                     |     |                     |
|     Stream Cipher   |     |     Block Cipher    |
|                     |     |                     |
+---------------------+     +---------------------+
|                     |     |                     |
|  - Encrypts one bit |     |  - Encrypts a