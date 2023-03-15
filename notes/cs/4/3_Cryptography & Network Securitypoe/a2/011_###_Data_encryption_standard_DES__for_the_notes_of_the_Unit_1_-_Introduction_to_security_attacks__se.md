 Here are the notes for ### Data encryption standard(DES) for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

Data Encryption Standard (DES)
- DES is a symmetric-key algorithm for the encryption of electronic data.
- DES uses a 56-bit key to encrypt and decrypt data in 64-bit blocks.
- The key length is relatively short which makes it susceptible to brute-force attacks.
- DES has a complex set of steps which incorporates permutations and substitutions.
- The steps of DES are - Initial permutation, Splitting into two halves, Applying 16 rounds of Feistel structure, Final permutation.
- Each round of Feistel structure uses a 48-bit subkey derived from the original key.
- The rounds involve substitutions, permutations and XOR operations to confuse and diffuse the plaintext.
- DES is cryptanalytically strong and proved resilient to attacks for several years but brute-force attacks are now feasible due to increased computing power.
- Triple DES (3DES) uses DES three times with two or three different keys to increase security but it is slow.

Mnemonics -

Dear (D)ata (E)ncryption (S)tandard
Diffuse and confuse, that's what we do
Inverse then switch, that's round anew
Subs and permut', the Feistel view
Initial and final, the permutations too

Advantages -
- Widely used and tested algorithm
- Simple and efficient software implementations

Disadvantages -
- Small key size makes it vulnerable to brute-force attacks
- Slow compared to modern block ciphers
- 3DES is even slower although more secure

Applications -
- DES is still used in some applications like SSH and SSL for compatibility.
- 3DES is sometimes used where compatibility with DES is desired but higher security is needed.