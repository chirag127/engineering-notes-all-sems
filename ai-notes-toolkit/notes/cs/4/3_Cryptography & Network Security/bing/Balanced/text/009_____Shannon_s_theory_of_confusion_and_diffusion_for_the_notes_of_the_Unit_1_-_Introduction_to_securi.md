### Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography.
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis.
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible.
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using substitution ciphers, which replace plaintext symbols with ciphertext symbols according to a key-dependent mapping.
- Diffusion can be achieved by using transposition ciphers, which permute the positions of plaintext symbols according to a key-dependent pattern.
- A good cipher should have both confusion and diffusion, so that changing one bit of the plaintext or the key affects many bits of the ciphertext, and vice versa.
- Shannon also introduced the concept of perfect secrecy, which means that the ciphertext does not reveal any information about the plaintext or the key, regardless of the computational power of the attacker.
- Shannon proved that the only cipher that achieves perfect secrecy is the one-time pad, which uses a random key of the same length as the plaintext, and performs bitwise exclusive-or operation to produce the ciphertext.
- However, the one-time pad is impractical for most applications, as it requires a secure way of generating and distributing the key, and the key can never be reused.
- Therefore, modern block ciphers aim to achieve a high level of security by using a combination of confusion and diffusion techniques, such as the fiestal structure, the data encryption standard (DES), and the triple DES.