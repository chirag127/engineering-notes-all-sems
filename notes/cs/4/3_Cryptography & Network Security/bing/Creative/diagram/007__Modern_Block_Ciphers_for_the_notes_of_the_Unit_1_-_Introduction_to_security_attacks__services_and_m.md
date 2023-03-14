A modern block cipher is a cipher that encrypts and decrypts fixed-size blocks of data using a secret key. The key is usually the same for both encryption and decryption, but some block ciphers use different keys for each operation. Block ciphers are widely used in symmetric-key cryptography, where the same key is shared by both parties.

A block cipher consists of two main components: a confusion function and a diffusion function. The confusion function is designed to make the relationship between the key and the ciphertext as complex and obscure as possible, so that an attacker cannot easily recover the key from the ciphertext. The diffusion function is designed to spread the influence of each bit of the plaintext and the key over many bits of the ciphertext, so that changing one bit of the plaintext or the key results in changing many bits of the ciphertext.

One common way to implement a block cipher is to use a Feistel structure, which consists of several rounds of processing. In each round, the block of data is split into two halves, and one half is modified by applying a round function that depends on the key and the other half. Then, the two halves are swapped for the next round. The round function can be any function that provides confusion and diffusion, such as a substitution-permutation network (SPN).

A substitution-permutation network is a network of simple operations that transform a block of data. The operations are usually substitution boxes (S-boxes) and permutation boxes (P-boxes). An S-box is a function that maps a fixed number of input bits to a fixed number of output bits, usually in a non-linear way. A P-box is a function that rearranges the bits of its input, usually in a linear way. By combining S-boxes and P-boxes, a block cipher can achieve both confusion and diffusion.

The following diagram illustrates the basic architecture of a block cipher using a Feistel structure and an SPN as the round function:

```
+-----------------+       +-----------------+
|                 |       |                 |
|  Plaintext      |       |  Ciphertext     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Initial        |       |  Final          |
|  Permutation    |       |  Permutation    |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Round 1        |       |  Round n        |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Round 2        |       |  Round n-1      |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
         .                         .
         .                         .
         .                         .
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Round n-1      |       |  Round 2        |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Round n        |       |  Round 1        |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Final          |       |  Initial        |
|  Permutation    |       |  Permutation    |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         ^
         |                         |
         v                         |
+-----------------+       +-----------------+
|                 |       |                 |
|  Ciphertext     |       |  Plaintext      |
|                 |       |                 |
+-----------------+       +-----------------+
```

The following diagram illustrates the structure of the round function using an SPN:

```
+-----------------+       +-----------------+
|                 |       |                 |
|  Left half      |       |  Left half      |
|                 |       |