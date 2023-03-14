### Classical encryption techniquessubstitution ciphers and transposition ciphers

- Classical encryption techniques are based on two basic components: substitution and transposition.
- Substitution ciphers replace each element of the plaintext with another element of the ciphertext, such as a letter, number, or symbol  .
- Transposition ciphers rearrange the order of the elements of the plaintext, such as letters, words, or blocks  .
- Both substitution and transposition ciphers can be classified into two types: monoalphabetic and polyalphabetic.
- Monoalphabetic ciphers use a fixed substitution rule for each letter of the alphabet, such as Caesar cipher, which shifts each letter by a fixed number of positions .
- Polyalphabetic ciphers use multiple substitution rules for each letter of the alphabet, such as Vigenere cipher, which shifts each letter by a variable number of positions based on a keyword .
- Substitution ciphers are vulnerable to frequency analysis, which exploits the fact that some letters or combinations of letters are more common than others in a given language .
- Transposition ciphers are vulnerable to anagramming, which exploits the fact that some words or phrases can be rearranged to form other words or phrases in a given language .
- To increase the security of classical encryption techniques, product ciphers can be used, which combine both substitution and transposition ciphers in multiple rounds .
- An example of a product cipher is DES (Data Encryption Standard), which uses 16 rounds of substitution and transposition operations on 64-bit blocks of plaintext .
- DES is based on the principles of confusion and diffusion, proposed by Shannon, which aim to make the relationship between the plaintext and the ciphertext as complex and random as possible .
- Confusion means that each bit of the ciphertext should depend on several bits of the key, so that changing one bit of the key should change many bits of the ciphertext .
- Diffusion means that each bit of the plaintext should affect many bits of the ciphertext, so that changing one bit of the plaintext should change many bits of the ciphertext .
- DES uses a fiestel structure, which divides the plaintext block into two halves and applies a round function to one half, which involves a substitution box (S-box) and a permutation box (P-box), and then XORs the result with the other half .
- DES has a key size of 56 bits, which is considered too small for modern standards, as it can be broken by brute force attacks .
- Differential cryptanalysis is a technique that exploits the non-uniformity of the S-boxes in DES, by analyzing the differences between pairs of plaintexts and ciphertexts and finding the most probable key .
- Block cipher modes of operation are methods of applying a block cipher to a message that is longer than the block size, such as ECB (Electronic Code Book), CBC (Cipher Block Chaining), CFB (Cipher Feedback), OFB (Output Feedback), and CTR (Counter) .
- Each mode of operation has different properties and advantages, such as parallelizability, error propagation, random access, and resistance to replay attacks .
- Triple DES is a variant of DES that applies three rounds of DES with different keys, which increases the effective key size to 168 bits and makes it more resistant to brute force and differential attacks .

: https://www.cse.wustl.edu/~jain/cse571-11/ftp/l_02cet.pdf
: https://www.tutorialspoint.com/difference-between-substitution-cipher-technique-and-transposition-cipher-technique
: https://progmohamedali.wordpress.com/2015/03/09/classical-encryption-techniques/