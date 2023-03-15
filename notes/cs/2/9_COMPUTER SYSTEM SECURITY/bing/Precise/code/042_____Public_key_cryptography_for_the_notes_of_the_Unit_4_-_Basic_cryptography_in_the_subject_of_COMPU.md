### Public key cryptography

Public key cryptography, also known as asymmetric cryptography, is a cryptographic system that uses two keys: a public key and a private key. The public key is used to encrypt messages, while the private key is used to decrypt them.

1. **Encryption**: The sender encrypts the message using the recipient's public key. The encrypted message can only be decrypted using the recipient's private key.
2. **Digital signatures**: The sender signs the message using their private key. The recipient can verify the signature using the sender's public key.
3. **Key exchange**: Two parties can use public key cryptography to securely exchange a shared secret key, which can then be used for symmetric encryption.

Public key cryptography is widely used in secure communication protocols, such as SSL/TLS, SSH, and PGP. It is also used in digital signature schemes, such as DSA and RSA.

Some advantages of public key cryptography include:

- It allows secure communication without the need for a pre-shared secret key.
- It enables the use of digital signatures, which provide non-repudiation and message integrity.
- It can be used for key exchange, allowing two parties to securely establish a shared secret key.

Some disadvantages of public key cryptography include:

- It is computationally intensive, making it slower than symmetric encryption.
- It is vulnerable to man-in-the-middle attacks if the public key is not properly authenticated.
- The private key must be kept secure, as its compromise would allow an attacker to decrypt messages or forge signatures.