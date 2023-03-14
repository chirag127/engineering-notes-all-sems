### Data encryption standard(DES) for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security

- Data encryption standard (DES) is a symmetric-key algorithm for the encryption and decryption of digital data  .
- DES operates on 64-bit blocks of data, using a 56-bit key (with 8 parity bits) and 16 rounds of complex transformations  .
- DES is based on the two fundamental attributes of cryptography: substitution (also called confusion) and transposition (also called diffusion) .
- Substitution means replacing some elements of the plaintext with other elements, while transposition means changing the order of the elements.
- DES uses both substitution and transposition at different stages of the algorithm, as shown in the figure below :

```
 64-bit plaintext
    |
    v
Initial Permutation (IP)
    |
    v
Left Plain Text (LPT)   Right Plain Text (RPT)
    |                       |
    v                       v
   16 rounds of encryption/decryption
    |                       |
    v                       v
Left Cipher Text (LCT)   Right Cipher Text (RCT)
    |                       |
    v                       v
Final Permutation (FP)
    |
    v
 64-bit ciphertext
```

- The initial permutation (IP) is a fixed transposition that rearranges the bits of the plaintext according to a predefined table .
- The final permutation (FP) is the inverse of the IP, that restores the original order of the bits .
- The 16 rounds of encryption/decryption are the core of the DES algorithm, where each round performs the following steps :
  - Key transformation: A 48-bit subkey is derived from the 56-bit key using a process of permutation and rotation .
  - Expansion: The 32-bit RPT is expanded to 48 bits by duplicating some bits according to a predefined table .
  - XOR: The expanded RPT is XORed with the subkey of the current round .
  - Substitution: The result of the XOR is divided into eight 6-bit blocks, each of which is mapped to a 4-bit block using a predefined table called S-box .
  - Permutation: The eight 4-bit blocks are combined and permuted according to another predefined table called P-box .
  - Swap: The output of the permutation is XORed with the LPT, and the result becomes the new RPT. The old RPT becomes the new LPT .
- The encryption and decryption processes are the same, except that the subkeys are used in reverse order for decryption .
- The strength of DES depends on the key length, the design of the S-boxes and P-boxes, and the resistance to various attacks .
- DES has been found vulnerable to brute-force attacks, differential cryptanalysis, linear cryptanalysis, and other techniques .
- Brute-force attack means trying all possible keys until the correct one is found .
- Differential cryptanalysis means exploiting the differences in the output of the S-boxes for different inputs .
- Linear cryptanalysis means approximating the behavior of the S-boxes with linear equations .
- To enhance the security of DES, several variants have been proposed, such as Triple DES (3DES), which applies DES three times with different keys .
- 3DES has a key length of 168 bits (or 112 bits if two keys are