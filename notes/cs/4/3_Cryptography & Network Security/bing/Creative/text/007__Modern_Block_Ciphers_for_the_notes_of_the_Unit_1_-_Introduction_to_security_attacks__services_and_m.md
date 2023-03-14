### Modern Block Ciphers

- Block ciphers are symmetric-key encryption algorithms that operate on fixed-length blocks of plaintext and produce blocks of ciphertext of the same length.
- Block ciphers can be classified into two types: substitution-permutation networks (SPNs) and Feistel networks.
- Substitution-permutation networks consist of several rounds of substitution and permutation operations, where substitution replaces bits or groups of bits with other bits, and permutation rearranges the bits in a fixed pattern.
- Feistel networks consist of several rounds of splitting, mixing, and swapping operations, where splitting divides the block into two halves, mixing applies a round function to one half using a subkey, and swapping exchanges the two halves.
- Block ciphers can be designed using different principles, such as confusion, diffusion, avalanche effect, completeness, and strict avalanche criterion.
- Confusion is the property that the relationship between the plaintext and the ciphertext is obscured by using complex and nonlinear transformations.
- Diffusion is the property that the influence of one plaintext bit on the ciphertext bits is spread over the entire ciphertext.
- Avalanche effect is the property that a small change in the plaintext or the key results in a significant change in the ciphertext.
- Completeness is the property that each ciphertext bit depends on every plaintext bit and every key bit.
- Strict avalanche criterion is the property that changing one plaintext bit or one key bit changes each ciphertext bit with a probability of 0.5.

#### Data Encryption Standard (DES)

- DES is a widely used block cipher that was standardized by NIST in 1977 and is based on a Feistel network.
- DES operates on 64-bit blocks of plaintext and produces 64-bit blocks of ciphertext, using a 56-bit key (plus 8 parity bits).
- DES consists of 16 rounds of encryption, each using a different 48-bit subkey derived from the main key using a key schedule algorithm.
- DES also uses an initial and a final permutation that are inverses of each other, and do not affect the security of the algorithm.
- DES uses a round function that consists of four steps: expansion, substitution, permutation, and XOR.
- Expansion takes a 32-bit input and produces a 48-bit output by duplicating some bits.
- Substitution takes a 48-bit input and produces a 32-bit output by applying eight 6-to-4 bit S-boxes, each with a different nonlinear mapping.
- Permutation takes a 32-bit input and produces a 32-bit output by rearranging the bits according to a fixed pattern.
- XOR takes a 32-bit input and a 48-bit subkey and produces a 32-bit output by applying the bitwise exclusive OR operation.
- DES has a simple and elegant structure, but it has been shown to be insecure against various attacks, such as brute force, differential cryptanalysis, linear cryptanalysis, and related-key attacks.

#### Differential Cryptanalysis

- Differential cryptanalysis is a chosen-plaintext attack that exploits the differences between two plaintexts and the corresponding ciphertexts to recover the key or some information about the key.
- Differential cryptanalysis uses a concept called differential, which is the XOR of two values, such as two plaintexts or two ciphertexts.
- Differential cryptanalysis also uses a concept called differential probability, which is the probability that a given differential in the input of a function results in a given differential in the output of the function.
- Differential cryptanalysis works by finding a differential characteristic, which is a sequence of differentials for the inputs and outputs of each round of a block cipher, that has a high probability of occurring.
- Differential cryptanalysis then collects a large number of plaintext pairs that satisfy the input differential of the characteristic, and computes the corresponding ciphertext pairs and the output differential of the characteristic.
- Differential cryptanalysis then analyzes the ciphertext pairs and the output differential to derive some information about the subkeys used in the last rounds of the block cipher, and uses this information to recover the main key or reduce the key space.

#### Block Cipher Modes of Operation

- Block cipher modes of operation are methods of using a block cipher to encrypt or decrypt messages of arbitrary length or that are streamed.
- Block cipher modes of operation can provide different security properties, such as confidentiality, integrity, authentication, and non-repudiation.
- Block cipher modes of operation can be classified into two types: single-block modes and multiple-block modes.
- Single-block modes encrypt or decrypt each block of plaintext or ciphertext independently, using the same key. Examples of single-block modes are electronic codebook (ECB) and counter (CTR).
- Multiple-block modes encrypt or decrypt each block of plaintext or ciphertext dependently, using the same key and some additional parameters, such as an initialization vector (IV), a nonce, or a counter. Examples