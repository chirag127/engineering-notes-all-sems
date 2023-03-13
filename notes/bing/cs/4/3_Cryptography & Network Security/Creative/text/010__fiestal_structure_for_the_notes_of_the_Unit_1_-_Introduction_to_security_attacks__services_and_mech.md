### Feistel Structure

- A Feistel cipher is a symmetric structure used in the construction of block ciphers, named after the German-born physicist and cryptographer Horst Feistel who did pioneering research while working for IBM  .
- A Feistel cipher consists of a number of rounds, where each round operates on two halves of the plaintext block and performs the following steps :
  - Split the block into two equal halves, L and R.
  - Apply a round function F to the right half R and a round key K, and XOR the result with the left half L.
  - Swap the halves L and R.
- The final round does not perform the swap, so the ciphertext block is (R, L) instead of (L, R).
- The decryption process is the same as the encryption process, except that the round keys are applied in the reverse order .
- A Feistel cipher can use different round functions and round keys, as long as they are invertible .
- A Feistel cipher can achieve both confusion and diffusion, as defined by Shannon's theory, by using complex and varied round functions and round keys .
- A Feistel cipher is also known as a Luby-Rackoff block cipher, because Luby and Rackoff proved that a Feistel cipher with four rounds and a pseudorandom round function is a pseudorandom permutation, which is secure against chosen-plaintext attacks.
- A Feistel cipher is a flexible and efficient structure that can be implemented in hardware or software, and can accommodate any block and key size .
- A Feistel cipher is used in many block ciphers, such as DES, Triple DES, Blowfish, CAST, and Twofish  .