 Here are the points on block cipher modes of operations:

### Block Cipher Modes of Operation

1. Electronic Codebook (ECB) Mode:
- Plaintext is divided into blocks and each block is encrypted separately.
- Same plaintext block will always encrypt to same ciphertext block.
- Vulnerable to attacks like ciphertext-only attack and known-plaintext attack.
- Not recommended for use.

2. Cipher Block Chaining (CBC) Mode:
- Each plaintext block is XORed with the previous ciphertext block before encryption.
- First block is XORed with an initialization vector (IV).
- Eliminates the weaknesses of ECB mode.
- More secure than ECB mode but still vulnerable to attacks like padding oracle attack.

3. Cipher Feedback (CFB) Mode:
- A block cipher is used to encrypt an initialization vector to generate a keystream.
- The keystream is XORed with the plaintext to produce the ciphertext.
- Decryption is similar - the keystream is XORed with the ciphertext to produce the plaintext.
- Error propagation is a disadvantage as one error affects the entire message.

4. Output Feedback (OFB) Mode:
- Similar to CFB mode but the keystream is generated independently of the plaintext.
- Decryption is same as encryption.
- Error does not propagate and parallelizability is a advantage but more vulnerable to sync loss attacks.

5. Counter (CTR) Mode:
- Uses a counter (sequential number) to generate a keystream.
- Counter values are encrypted to produce keystream which is XORed with the plaintext to produce ciphertext.
- Parallelization and error confinement are advantages. Most secure mode of operation.

[No emojis or external links included as per the instructions.]