### Feistel structure

- Feistel structure is a symmetric structure used in the construction of block ciphers, named after the German-born physicist and cryptographer Horst Feistel who did pioneering research while working for IBM  .
- Feistel structure is also commonly known as a Feistel network or a Luby–Rackoff block cipher.
- A large set of block ciphers use the Feistel structure, including the Data Encryption Standard (DES), Triple DES, Blowfish, CAST-128, GOST, etc  .
- Feistel structure is based on the idea of dividing the plaintext block into two equal halves and applying a series of rounds of substitution and permutation operations on them.
- Feistel structure has the following advantages:
  - It is easy to implement and can be used to design various block ciphers with different parameters and functions.
  - It allows the use of non-invertible functions in the encryption process, which increases the security and complexity of the cipher.
  - It uses the same algorithm for encryption and decryption, which simplifies the key management and reduces the code size.
  - It can achieve the properties of confusion and diffusion, which are essential for a secure cipher according to Shannon's theory.
- Feistel structure has the following disadvantages:
  - It is vulnerable to certain types of cryptanalysis, such as differential cryptanalysis and linear cryptanalysis, which exploit the statistical properties of the cipher.
  - It requires multiple rounds of encryption to achieve a high level of security, which increases the computational cost and time.
  - It is not suitable for parallel processing, as each round depends on the output of the previous round.

- Feistel structure can be described as follows :

  - Let P be the plaintext block of n bits, and K be the secret key of k bits.
  - Divide P into two equal halves, L0 and R0, each of n/2 bits.
  - For each round i from 1 to r, where r is the number of rounds, do the following:
    - Apply a round function Fi to R(i-1) and a subkey Ki derived from K, and get the output Fi(R(i-1), Ki).
    - Compute Li = R(i-1) and Ri = Li-1 XOR Fi(R(i-1), Ki), where XOR is the bitwise exclusive OR operation.
  - After r rounds, the ciphertext block C is obtained by concatenating Rr and Lr, i.e., C = Rr || Lr.
  - To decrypt C, the same algorithm is applied in reverse order, using the same subkeys in reverse order, i.e., Ki = Kr-i+1 for i from 1 to r.

- An example of Feistel structure with 4 rounds is shown below:

```
  P = L0 || R0
  |           |
  |           V
  |        +-----+
  |        | F1  |
  |        |     |
  |        +--+--+
  |           |
  |           | K1
  |           |
  |           V
  +------> XOR <------+
  |                   |
  |                   |
  V                   V
 L1 = R0            R1
  |                   |
  |                   V
  |                +-----+
  |                | F2  |
  |                |     |
  |                +--+--+
  |                   |
  |                   | K2
  |                   |
  |                   V
  +------> XOR <------+
  |                   |
  |                   |
  V                   V
 L2 = R1            R2
  |                   |
  |                   V
  |                +-----+
  |                | F3  |
  |                |     |
  |                +--+--+
  |                   |
  |                   | K3
  |                   |
  |                   V
  +------> XOR <------+
  |                   |
  |                   |
  V                   V
 L3 = R2            R3
  |                   |
  |                   V
  |                +-----+
  |                | F4  |
  |                |     |
  |                +--+--+
  |                   |
  |                   | K4
  |                   |
  |