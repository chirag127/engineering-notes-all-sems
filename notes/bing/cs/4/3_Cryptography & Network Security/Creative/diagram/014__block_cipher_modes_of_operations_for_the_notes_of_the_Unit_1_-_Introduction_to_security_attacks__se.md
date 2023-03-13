A block cipher mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity. A block cipher by itself is only suitable for the secure cryptographic transformation (encryption or decryption) of one fixed-length group of bits called a block. To encrypt or decrypt messages of arbitrary length, different modes of operation are used. Some of the common modes of operation are:

- Electronic Codebook (ECB): This mode encrypts or decrypts each block of plaintext or ciphertext independently. It is simple and fast, but it has several drawbacks, such as revealing patterns in the data and being vulnerable to replay attacks.
- Cipher Block Chaining (CBC): This mode uses an initialization vector (IV) to XOR the first block of plaintext before encryption, and then XORs each subsequent block of plaintext with the previous block of ciphertext. This makes the ciphertext more random and prevents identical plaintext blocks from producing identical ciphertext blocks. However, this mode requires padding to make the plaintext length a multiple of the block size, and it is not parallelizable.
- Cipher Feedback (CFB): This mode converts a block cipher into a stream cipher by using the previous block of ciphertext as the input to the block cipher, and then XORing the output with the plaintext or ciphertext. This mode allows encryption or decryption of partial blocks, and does not require padding. However, it is also not parallelizable, and it propagates errors in the ciphertext to the plaintext.
- Output Feedback (OFB): This mode also converts a block cipher into a stream cipher by using the previous output of the block cipher as the input to the next block cipher, and then XORing the output with the plaintext or ciphertext. This mode is similar to CFB, but it does not propagate errors in the ciphertext to the plaintext. However, it is also not parallelizable, and it is vulnerable to replay attacks if the IV is reused.
- Counter (CTR): This mode uses a counter as the input to the block cipher, and then XORs the output with the plaintext or ciphertext. The counter is incremented for each block, and it must be unique for each message. This mode allows encryption or decryption of partial blocks, and does not require padding. It is also parallelizable, and it does not propagate errors in the ciphertext to the plaintext. However, it is also vulnerable to replay attacks if the counter is reused.

The following diagram illustrates the basic architecture of each mode of operation using ASCII art:

### ECB mode

```
Plaintext:  P1 P2 P3 P4 ... Pn
             |  |  |  |      |
             v  v  v  v      v
Key:         K  K  K  K      K
             |  |  |  |      |
             v  v  v  v      v
Ciphertext:  C1 C2 C3 C4 ... Cn
```

### CBC mode

```
Plaintext:  P1 P2 P3 P4 ... Pn
             |  |  |  |      |
             v  v  v  v      v
IV:          IV ^ ^ ^ ^      ^
             |  |  |  |      |
             v  v  v  v      v
Key:         K  K  K  K      K
             |  |  |  |      |
             v  v  v  v      v
Ciphertext:  C1 C2 C3 C4 ... Cn
             |  |  |  |      |
             v  v  v  v      v
             ^ ^ ^ ^ ^      ^
             |  |  |  |      |
             v  v  v  v      v
```

### CFB mode

```
Plaintext:  P1 P2 P3 P4 ... Pn
             |  |  |  |      |
             v  v  v  v      v
             ^ ^ ^ ^ ^      ^
             |  |  |  |      |
             v  v  v  v      v
IV:          IV -> -> -> -> ->
             |  |  |  |      |
             v  v  v  v      v
Key:         K  K  K  K      K
             |  |  |  |      |
             v  v  v  v      v
Ciphertext:  C1 C2 C3 C4 ... Cn
             |  |  |  |      |
             v  v  v  v      v
             ->