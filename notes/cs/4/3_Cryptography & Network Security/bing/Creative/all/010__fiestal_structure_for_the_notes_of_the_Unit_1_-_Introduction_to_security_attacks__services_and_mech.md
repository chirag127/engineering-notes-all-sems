### Feistel structure for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, feistel structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

- A Feistel cipher is a symmetric structure used in the construction of block ciphers, named after the German-born physicist and cryptographer Horst Feistel, who did pioneering research while working for IBM.
- A Feistel cipher consists of a number of rounds, where each round operates on two halves of the data block: the left half and the right half. The round function takes the right half and a subkey as inputs and produces an output that is XORed with the left half. The resulting value becomes the new right half, and the original right half becomes the new left half. This process is repeated for a fixed number of rounds, and the final output is the encrypted data.
- The advantage of a Feistel cipher is that it is guaranteed to be invertible, even if the round function is not. This means that the encryption and decryption algorithms are very similar, and only require reversing the order of the subkeys.
- A Feistel cipher can be represented by the following diagram:

```
    Plaintext
    L0             R0
     |              |
     |              |
     |              V
     |            f(K1)
     |              |
     V              |
   XOR <------------
     |              |
     |              |
     |              V
     |            f(K2)
     |              |
     V              |
   XOR <------------
     |              |
     |              |
    L16            R16
     |              |
     |              |
    Ciphertext
```

- Some examples of block ciphers that use the Feistel structure are DES, Triple DES, GOST, Blowfish, and Twofish .
- The Feistel structure can be modified in various ways, such as using different round functions, different number of rounds, different subkey generation methods, or unbalanced splits of the data block.
- The security of a Feistel cipher depends on the properties of the round function, the subkey generation, and the number of rounds. Some of the criteria for a secure Feistel cipher are :
  - The round function should be nonlinear and complex, so that it is hard to analyze or invert.
  - The subkeys should be independent and unpredictable, so that they provide enough diffusion and confusion.
  - The number of rounds should be large enough, so that the cipher resists various attacks such as differential cryptanalysis or linear cryptanalysis.
- A mnemonic to remember the Feistel structure is: **F**eistel **E**ncrypts **I**n **S**ymmetric **T**ransformations **E**ach **L**eft and right half.
- A learning trick to understand the Feistel structure is to use a toy example with a simple round function and a small data block. For example, suppose we have a 4-bit data block 1011 and two 2-bit subkeys 01 and 10. The round function is simply XORing the right half with the subkey. Then the Feistel encryption process is as follows:

```
    Plaintext: 1011
    L0: 10    R0: 11
    f(K1): 11 XOR 01 = 10
    L1: R0 = 11    R1: L0 XOR f(K1) = 10 XOR 10 = 00
    f(K2): 00 XOR 10 = 10
    L2: R1 = 00    R2: L1 XOR f(K2) = 11 XOR 10 = 01
    Ciphertext: L2R2 = 0001
```

- To decrypt the ciphertext, we reverse the order of the subkeys and apply the same process:

```
    Ciphertext: 0001
    L2: 00    R2: 01
    f(K2