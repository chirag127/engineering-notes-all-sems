The Data Encryption Standard (DES) is a symmetric-key algorithm for the encryption of digital data. It encrypts data in blocks of 64 bits, using a 56-bit key. It is based on a balanced Feistel network with 16 rounds of substitution and transposition operations. The following diagram illustrates the basic architecture of DES:

```
+-----------------+     +-----------------+
| 64-bit plain    |     | 64-bit cipher   |
| text block      |     | text block      |
+-----------------+     +-----------------+
         |                       ^
         |                       |
         v                       |
+-----------------+              |
| Initial         |              |
| Permutation (IP)|              |
+-----------------+              |
         |                       |
         v                       |
+-----------------+              |
| 32-bit LPT      |              |
+-----------------+              |
         |                       |
         v                       |
+-----------------+              |
| 32-bit RPT      |              |
+-----------------+              |
         |                       |
         v                       |
+-----------------+              |
| 16 rounds of    |--------------+
| encryption      |
+-----------------+
         |
         v
+-----------------+
| 32-bit LPT      |
+-----------------+
         |
         v
+-----------------+
| 32-bit RPT      |
+-----------------+
         |
         v
+-----------------+
| Final           |
| Permutation (FP)|
+-----------------+
         |
         v
+-----------------+
| 64-bit cipher   |
| text block      |
+-----------------+
```

Each round of encryption consists of the following steps:

1. Key transformation: The 56-bit key is divided into two 28-bit halves and each half is rotated left by a certain number of bits depending on the round number. Then, a permutation is applied to select 48 bits out of the 56 bits, resulting in a 48-bit subkey for each round.
2. Expansion: The 32-bit RPT is expanded to 48 bits by duplicating some bits at predefined positions.
3. XOR: The expanded RPT is XORed with the subkey of the current round.
4. Substitution: The result of the XOR operation is divided into eight 6-bit blocks, and each block is passed through a substitution box (S-box) that produces a 4-bit output. The S-boxes are predefined and different for each block.
5. Permutation: The outputs of the S-boxes are concatenated and permuted according to a predefined table, resulting in a 32-bit output.
6. Swap: The output of the permutation is XORed with the LPT, and the result becomes the new RPT. The old RPT becomes the new LPT. This swap is not performed in the last round.

The final permutation (FP) is the inverse of the initial permutation (IP), and it produces the 64-bit cipher text block from the final LPT and RPT. The decryption process is the same as the encryption process, except that the subkeys are used in reverse order.