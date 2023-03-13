 Here is the content in markdown format on the topic -

### Basic concepts of Cryptography in application layer

1. Encryption - Conversion of plaintext into ciphertext using a key. It ensures confidentiality.
Mnemonic - Lock and key; plaintext goes in, ciphertext comes out.

2. Decryption - Conversion of ciphertext back into plaintext using a key.
Mnemonic - Unlock with key; ciphertext goes in, plaintext comes out.

3. Symmetric key cryptography - Uses same key for encryption and decryption.
 eg. AES, DES, Blowfish.
Advantage - Fast and simple.
Disadvantage - Key distribution and management is difficult.

4. Asymmetric key cryptography (Public key cryptography) - Uses a pair of keys, public and private.
 eg. RSA, ECC.
Public key is used for encryption and private key is used for decryption.
Advantage - Secure key distribution.
Disadvantage - Computationally more intensive.

5. Digital signatures - Used to authenticate the sender and verify integrity of the message.
 eg. RSA, DSA, ECDSA.
The private key is used to sign the message and public key is used to verify the signature.

6. Hash functions - Produce a fixed-size hash value from a variable size input.
 eg. MD5, SHA-1, SHA-256.
Used to check integrity of data and as a building block for other cryptographic protocols.

Applications - Ecommerce, banking, emails, software distribution, etc.

[Detailed diagrams, examples, codes can be added here if required.]