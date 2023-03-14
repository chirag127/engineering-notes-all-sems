 Here is the content in markdown format for the given topic:

### Block Cipher Modes of Operation

Some of the popular block cipher modes of operation are:

1. Electronic Codebook (ECB) Mode:
- Plaintext is divided into blocks of size same as the block size of the cipher.
- Each block is encrypted independently.
- Same plaintext block will always encrypt to the same ciphertext block.
- Vulnerable to statistical attacks and patterns in the plaintext may be revealed.
- Not recommended for usage in practical applications.

2. Cipher Block Chaining (CBC) Mode:
- Each plaintext block is XORed with the previous ciphertext block before encryption.
- First plaintext block is XORed with an initialisation vector (IV).
- IV must be randomly generated and transmitted with the ciphertext.
- Prevents identical plaintext blocks from producing identical ciphertext blocks.
- Vulnerable to certain attacks like padding oracle attacks.

3. Cipher Feedback (CFB) Mode:
- A portion of the previous ciphertext block is used as the IV to encrypt the next plaintext block.
- The cipher is used in a feedback mode to generate keystream blocks.
- The keystream blocks are XORed with the plaintext to produce the ciphertext.
- Allows encryption and decryption of data in a streaming fashion.
- Vulnerable to certain attacks if a portion of ciphertext is lost or delayed.

[Additional points, diagrams, examples, applications, advantages, disadvantages, etc. can be included here if required.]

The above points cover the major block cipher modes of operation. The mode used depends on the specific application and the level of security required. Certain modes are more secure than others against certain attacks. A combination of modes can also be used to achieve high security.