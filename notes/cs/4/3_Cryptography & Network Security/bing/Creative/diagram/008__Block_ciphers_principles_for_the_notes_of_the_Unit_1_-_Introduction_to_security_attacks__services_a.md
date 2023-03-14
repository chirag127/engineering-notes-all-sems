A block cipher is a type of symmetric encryption algorithm that operates on fixed-length groups of bits, called blocks. A block cipher uses a secret key and a mathematical function to transform the plaintext block into a ciphertext block of the same size. The inverse function is used to decrypt the ciphertext block using the same key. Block ciphers are widely used to encrypt large amounts of data securely.

There are different types of block ciphers, but most of them are based on the Feistel cipher structure, which was invented by Horst Feistel in the 1970s. A Feistel cipher consists of a number of rounds, each of which performs a substitution and a permutation on the input block. The substitution is done by applying a round function to one half of the block, using a subkey derived from the main key. The permutation is done by swapping the two halves of the block. The round function can be any non-linear function that provides confusion and diffusion, which are the two main principles of block cipher design, according to Claude Shannon.

The following diagram illustrates the basic architecture of a Feistel cipher:

```
    Plaintext block
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    +------+------+  <--- Initial permutation (optional)
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    +------+------+  <--- Round 1
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |  <--- Swap
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    +------+------+  <--- Round 2
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |  <--- Swap
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    +------+------+  <--- Round n
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |  <--- Swap (optional)
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    |      |      |
    +------+------+  <--- Final permutation (optional)
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    Ciphertext block
```

Each round of a Feistel cipher can be represented as follows:

```
    L(i-1)  R(i-1)  <--- Input block halves
      |       |
      |       |
      |       |
      |       |
      |       +-----------------+
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      +-----------------------+
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      +-----------------------+
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |
      |                       |