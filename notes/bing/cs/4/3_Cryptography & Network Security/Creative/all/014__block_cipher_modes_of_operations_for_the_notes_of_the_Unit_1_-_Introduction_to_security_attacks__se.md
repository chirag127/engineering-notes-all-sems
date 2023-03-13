### Block cipher modes of operation

A block cipher is a symmetric-key algorithm that encrypts or decrypts a fixed-length block of data, such as 64 bits or 128 bits. However, most messages are longer than one block, so a block cipher mode of operation is needed to specify how to use a block cipher to process longer messages. A block cipher mode of operation can provide different security services, such as confidentiality, integrity, authentication, or a combination of them. 

There are many block cipher modes of operation, but some of the most common ones are:

- **Electronic Codebook (ECB)**: This mode simply encrypts each block of the message independently with the same key. It is fast and simple, but it has many drawbacks, such as revealing patterns in the message, being vulnerable to replay attacks, and not providing any integrity or authentication.  

- **Cipher Block Chaining (CBC)**: This mode encrypts each block of the message by XORing it with the previous ciphertext block, except for the first block, which is XORed with an initialization vector (IV). This mode provides confidentiality and diffusion, but it requires padding to make the message a multiple of the block size, and it is not parallelizable. It also does not provide any integrity or authentication.  

- **Cipher Feedback (CFB)**: This mode converts a block cipher into a stream cipher by encrypting the IV and XORing the output with the first block of the message, then encrypting the first ciphertext block and XORing the output with the second block of the message, and so on. This mode provides confidentiality and self-synchronization, but it is not parallelizable and it is sensitive to transmission errors. It also does not provide any integrity or authentication.  

- **Output Feedback (OFB)**: This mode also converts a block cipher into a stream cipher by encrypting the IV and XORing the output with the first block of the message, then encrypting the output and XORing it with the second block of the message, and so on. This mode provides confidentiality and randomization, but it is not self-synchronizing and it is sensitive to transmission errors. It also does not provide any integrity or authentication.  

- **Counter (CTR)**: This mode encrypts a counter value that is incremented for each block of the message, and XORs the output with the corresponding block of the message. This mode provides confidentiality and parallelization, but it requires a unique and unpredictable counter value for each message. It also does not provide any integrity or authentication.  

- **Galois/Counter Mode (GCM)**: This mode combines the CTR mode with a Galois field multiplication operation to provide both confidentiality and authentication. It is fast and parallelizable, but it requires a unique and unpredictable IV for each message, and it has a limit on the maximum message length and the number of messages that can be processed with the same key.  

- **Cipher Block Chaining Message Authentication Code (CBC-MAC)**: This mode is not used for encryption, but for generating a message authentication code (MAC) that can verify the integrity and authenticity of a message. It encrypts each block of the message by XORing it with the previous ciphertext block, except for the first block, which is XORed with an IV, and outputs the final ciphertext block as the MAC. It is simple and secure, but it requires a fixed-length message and a different key than the one used for encryption.  

A mnemonic to remember the names of these modes is: **E**very **C**at **C**an **O**pen **F**ish **C**ans **G**ently **C**hewing **M**eat. 

A diagram to illustrate these modes is:

```
Plaintext: P1 P2 P3 P4
Ciphertext: C1 C2 C3 C4
Key: K
IV: Initialization Vector
CTR: Counter Value

ECB: P1 ->|K|-> C1
     P2 ->|K|-> C2
     P3 ->|K|-> C3
     P4 ->|K|-> C4

CBC: P1 ^ IV ->|K|-> C1
     P2 ^ C1 ->|