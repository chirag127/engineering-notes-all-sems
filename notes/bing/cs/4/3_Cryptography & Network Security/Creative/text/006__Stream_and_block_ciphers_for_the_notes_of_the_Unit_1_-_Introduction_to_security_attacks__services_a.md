### Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that transform plaintext into ciphertext using a secret key.
- Stream ciphers encrypt data one bit or one byte at a time, while block ciphers encrypt data in fixed-size blocks, usually 64 or 128 bits.
- Stream ciphers are faster and simpler than block ciphers, but they are more vulnerable to attacks such as replay, insertion, deletion, and modification.
- Block ciphers are more secure and versatile than stream ciphers, but they require more processing power and memory, and they may introduce padding or waste bandwidth.
- Stream ciphers can be classified into synchronous and self-synchronizing stream ciphers. Synchronous stream ciphers use the same key stream for encryption and decryption, and they require synchronization between the sender and the receiver. Self-synchronizing stream ciphers use the previous ciphertext bits to generate the key stream, and they can recover from errors or losses in transmission.
- Block ciphers can be classified into substitution-permutation networks (SPNs) and Feistel networks. SPNs consist of alternating rounds of substitution and permutation operations, which provide confusion and diffusion respectively. Feistel networks split the block into two halves and apply a round function to one half using a subkey, then swap the halves and repeat the process for several rounds.
- Some examples of stream ciphers are RC4, A5/1, A5/2, and E0. Some examples of block ciphers are DES, AES, IDEA, and Blowfish.