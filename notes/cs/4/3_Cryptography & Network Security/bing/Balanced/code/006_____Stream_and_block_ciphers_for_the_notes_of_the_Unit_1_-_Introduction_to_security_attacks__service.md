Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of stream and block ciphers.

```markdown
### Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that operate on different units of plaintext and ciphertext.
- Stream ciphers encrypt and decrypt one bit or byte of plaintext at a time, using a keystream that is generated from a secret key and an initialization vector (IV).
- Block ciphers encrypt and decrypt fixed-length blocks of plaintext, usually 64 or 128 bits, using a secret key and a mode of operation that specifies how to handle multiple blocks.
- Stream ciphers are faster and more suitable for continuous data streams, such as voice or video, while block ciphers are more secure and more suitable for discrete data, such as files or messages.
- Stream ciphers can be classified into synchronous and self-synchronizing stream ciphers. Synchronous stream ciphers use the same keystream for encryption and decryption, and require the sender and receiver to be synchronized. Self-synchronizing stream ciphers use the previous ciphertext bits to generate the keystream, and can recover from errors or losses in transmission.
- Block ciphers can be classified into substitution-permutation networks (SPNs) and Feistel networks. SPNs consist of multiple rounds of substitution and permutation operations, which provide confusion and diffusion respectively. Feistel networks consist of multiple rounds of splitting, mixing, and swapping operations, which allow the use of reversible functions as round functions.
- Examples of stream ciphers are RC4, A5/1, A5/2, and Salsa20. Examples of block ciphers are DES, AES, IDEA, and Blowfish.
```