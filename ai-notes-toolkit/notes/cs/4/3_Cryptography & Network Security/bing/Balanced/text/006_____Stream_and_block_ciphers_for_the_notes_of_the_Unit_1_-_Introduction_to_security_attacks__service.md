Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of stream and block ciphers.

### Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that use a secret key to encrypt and decrypt data.
- Stream ciphers encrypt and decrypt data one bit or one byte at a time, while block ciphers encrypt and decrypt data in fixed-size blocks, usually 64 or 128 bits.
- Stream ciphers are faster and simpler than block ciphers, but they are more vulnerable to attacks such as replay, insertion, deletion, and modification.
- Block ciphers are more secure and versatile than stream ciphers, but they require more processing power and memory, and they may introduce padding or waste bandwidth.
- Stream ciphers can be classified into two categories: synchronous and self-synchronizing.
  - Synchronous stream ciphers use the same key and initialization vector (IV) to generate a keystream that is independent of the plaintext and ciphertext. The sender and the receiver must be synchronized to use the same keystream. Examples of synchronous stream ciphers are RC4, A5/1, and ChaCha20.
  - Self-synchronizing stream ciphers use the previous ciphertext bits to generate the keystream, so they can recover from errors or losses in transmission. However, they are less efficient and more complex than synchronous stream ciphers. Examples of self-synchronizing stream ciphers are CFB, OFB, and CTR modes of block ciphers.
- Block ciphers can be classified into two categories: substitution-permutation networks (SPNs) and Feistel networks.
  - SPNs consist of alternating rounds of substitution and permutation operations, where substitution replaces bits or groups of bits with different bits, and permutation rearranges the bits in a fixed pattern. The key is used to select the substitution and permutation functions. Examples of SPNs are AES, PRESENT, and Serpent.
  - Feistel networks consist of alternating rounds of splitting, mixing, and swapping operations, where splitting divides the block into two halves, mixing combines one half with a subkey derived from the main key, and swapping exchanges the two halves. The final round does not swap the halves. Examples of Feistel networks are DES, 3DES, and Blowfish.