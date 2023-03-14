A block cipher mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity. A block cipher by itself is only suitable for the secure cryptographic transformation (encryption or decryption) of one fixed-length group of bits called a block. A mode of operation describes how to repeatedly apply a cipher's single-block operation to securely transform amounts of data larger than a block. Most modes require a unique binary sequence, often called an initialization vector (IV), for each encryption operation. The IV has to be non-repeating and, for some modes, random as well. The initialization vector is used to ensure distinct ciphertexts are produced even when the same plaintext is encrypted multiple times independently with the same key.

There are several modes of operations for a block cipher, such as Electronic Code Book (ECB), Cipher Block Chaining (CBC), Cipher Feedback Mode (CFB), Output Feedback Mode (OFB), Counter Mode (CTR), and XTS Mode. Each mode has its own advantages and disadvantages, and some are more suitable for certain applications than others. The following diagram illustrates the basic architecture of each mode, where P is the plaintext block, C is the ciphertext block, E is the encryption function, D is the decryption function, K is the secret key, and IV is the initialization vector. The diagram uses the notation of XOR (exclusive OR) and concatenation (+) for simplicity.

### Block cipher modes of operation

```
ECB:   P1   P2   P3   P4
       |    |    |    |
       v    v    v    v
E(K)  E(K) E(K) E(K) E(K)
       |    |    |    |
       v    v    v    v
       C1   C2   C3   C4

CBC:   P1   P2   P3   P4
       |    |    |    |
       v    v    v    v
       +    +    +    +
       |    |    |    |
       v    v    v    v
IV   C1   C2   C3   C4
 |    |    |    |    |
 v    v    v    v    v
E(K) E(K) E(K) E(K) E(K)
 |    |    |    |    |
 v    v    v    v    v
 C1   C2   C3   C4   C5

CFB:   P1   P2   P3   P4
       |    |    |    |
       v    v    v    v
       +    +    +    +
       |    |    |    |
       v    v    v    v
IV   C1   C2   C3   C4
 |    |    |    |    |
 v    v    v    v    v
E(K) E(K) E(K) E(K) E(K)
 |    |    |    |    |
 v    v    v    v    v
 C1   C2   C3   C4   C5

OFB:   P1   P2   P3   P4
       |    |    |    |
       v    v    v    v
       +    +    +    +
       |    |    |    |
       v    v    v    v
IV   O1   O2   O3   O4
 |    |    |    |    |
 v    v    v    v    v
E(K) E(K) E(K) E(K) E(K)
 |    |    |    |    |
 v    v    v    v    v
 O1   O2   O3   O4   O5
       |    |    |    |
       v    v    v    v
       C1   C2   C3   C4

CTR:   P1   P2   P3   P4
       |    |    |    |
       v    v    v    v
       +    +    +    +
       |    |    |    |
       v    v    v    v
IV+0 IV+1 IV+2 IV+3 IV+4
 |    |    |    |    |
 v    v    v    v    v
E(K) E(K) E(K) E(K) E(K)
 |    |    |    |    |
 v    v    v