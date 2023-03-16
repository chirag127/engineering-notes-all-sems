# Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using substitution ciphers, which replace each plaintext symbol with a different ciphertext symbol according to a key-dependent mapping.
- Diffusion can be achieved by using transposition ciphers, which permute the positions of the plaintext symbols according to a key-dependent pattern.
- Confusion and diffusion can be combined by using a fiestal structure, which alternates substitution and transposition operations in multiple rounds with different subkeys derived from the main key.
- A well-designed cipher should have a high degree of both confusion and diffusion, so that changing one bit of the plaintext or the key affects many bits of the ciphertext, and vice versa.