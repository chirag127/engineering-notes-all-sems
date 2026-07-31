Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of modern block ciphers.

# Modern Block Ciphers

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- Block ciphers are widely used to provide confidentiality, integrity, and authentication in various cryptographic applications, such as encryption, hashing, and digital signatures.
- Block ciphers can be classified into two types: substitution-permutation networks (SPNs) and Feistel networks. Both types use multiple rounds of transformations to achieve confusion and diffusion, as proposed by Shannon's theory of secrecy systems.
- Confusion means that the relationship between the plaintext and the ciphertext is complex and obscure, making it hard to deduce the key or the plaintext from the ciphertext. Diffusion means that each bit of the ciphertext depends on many bits of the plaintext and the key, making it hard to change or manipulate the ciphertext without affecting the plaintext.

## Substitution-Permutation Networks (SPNs)

- An SPN consists of a series of rounds, each of which performs three operations: a key addition, a substitution, and a permutation. The key addition is a bitwise exclusive-or (XOR) of the round key and the input block. The substitution is a nonlinear transformation that replaces each bit or group of bits with another bit or group of bits, according to a predefined table called an S-box. The permutation is a linear transformation that rearranges the bits of the block, according to a predefined pattern called a P-box.
- An example of an SPN is the Advanced Encryption Standard (AES), which operates on 128-bit blocks and uses 10, 12, or 14 rounds, depending on the key size (128, 192, or 256 bits). AES uses a 4x4 matrix of bytes, called a state, to represent the block, and performs four operations in each round: SubBytes, ShiftRows, MixColumns, and AddRoundKey. The last round omits the MixColumns operation. AES also uses an initial round key addition before the first round, and a final round key addition after the last round.

## Feistel Networks

- A Feistel network consists of a series of rounds, each of which splits the block into two halves, called the left and right halves, and performs three operations: a key addition, a substitution, and a swapping. The key addition is a bitwise XOR of the round key and the right half. The substitution is a nonlinear transformation that applies a function, called an F-function, to the result of the key addition. The swapping is an exchange of the left and right halves. The last round omits the swapping operation.
- An example of a Feistel network is the Data Encryption Standard (DES), which operates on 64-bit blocks and uses 16 rounds. DES uses a 56-bit key, derived from a 64-bit key by discarding 8 parity bits. DES also uses an initial and a final permutation, called IP and FP, to rearrange the bits of the block before and after the rounds. The F-function of DES consists of four operations: expansion, key addition, substitution, and permutation. The expansion is a linear transformation that expands the 32-bit input to 48 bits, by duplicating some bits. The key addition is a bitwise XOR of the expanded input and the round key. The substitution is a nonlinear transformation that replaces each group of 6 bits with a group of 4 bits, according to eight predefined tables called S-boxes. The permutation is a linear transformation that rearranges the 32 bits of the output, according to a predefined pattern.

## Strength of Block Ciphers

- The strength of a block cipher depends on several factors, such as the block size, the key size, the number of rounds, the design of the S-boxes and the P-boxes, and the resistance to various attacks, such as brute-force, differential, linear, and algebraic attacks.
- Brute-force attack is the simplest and most generic attack, which tries all possible keys until finding the correct one. The complexity of a brute-force attack is proportional to the key size, so a larger key size provides more security. For example, a 56-bit key, as used by DES, can be broken by a brute-force attack in a matter of hours or days, while a 128-bit key, as used by AES, is considered infeasible to break by a brute-force attack with current technology.
- Differential cryptanalysis is a chosen-plaintext attack, which exploits the statistical properties of the S-boxes and the P-boxes, and analyzes the differences between