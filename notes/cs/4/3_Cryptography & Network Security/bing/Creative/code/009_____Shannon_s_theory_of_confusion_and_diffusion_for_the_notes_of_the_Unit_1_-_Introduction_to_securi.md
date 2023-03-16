# Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using a complex substitution function that depends on the key and the plaintext.
- Diffusion can be achieved by using a permutation function that spreads the influence of each plaintext bit over many ciphertext bits.
- A cipher that has both confusion and diffusion is more resistant to linear and differential cryptanalysis.
- A common way to implement confusion and diffusion is to use a fiestal structure, which alternates substitution and permutation layers in multiple rounds.