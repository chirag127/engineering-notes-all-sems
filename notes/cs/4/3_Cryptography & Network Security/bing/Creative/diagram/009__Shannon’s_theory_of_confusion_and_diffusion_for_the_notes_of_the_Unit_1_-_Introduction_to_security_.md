Shannon's theory of confusion and diffusion is a design principle for secure ciphers, which aims to make the ciphertext as random and as independent of the plaintext and the key as possible. Confusion means that each bit of the ciphertext should depend on several parts of the key, obscuring the connections between the two. Diffusion means that if we change a single bit of the plaintext, then about half of the bits in the ciphertext should change, and similarly, if we change one bit of the ciphertext, then about half of the plaintext bits should change. This is also known as the avalanche effect.

One way to achieve confusion and diffusion is to use a substitution-permutation network, which consists of several rounds of applying substitution boxes (S-boxes) and permutation boxes (P-boxes) to the plaintext. S-boxes provide confusion by replacing bits of the plaintext with bits of the key, according to some nonlinear function. P-boxes provide diffusion by rearranging the bits of the output of the S-boxes, according to some linear function. The result is a ciphertext that has no apparent statistical relationship with the plaintext or the key.

The following diagram illustrates the basic architecture of a substitution-permutation network:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Plaintext     |     |   Round 1       |     |   Round 2       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  S-box   |   |     |  |  S-box   |   |     |  |  S-box   |   |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|     |           |     |     |           |     |     |           |
|     |           |     |     |           |     |     |           |
|     v           |     |     v           |     |     v           |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  P-box   |   |     |  |  P-box   |   |     |  |  P-box   |   |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|     |           |     |     |           |     |     |           |
|     |           |     |     |           |     |     |           |
|     v           |     |     v           |     |     v           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Ciphertext    |<----|   Round Key     |<----|   Round Key     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```