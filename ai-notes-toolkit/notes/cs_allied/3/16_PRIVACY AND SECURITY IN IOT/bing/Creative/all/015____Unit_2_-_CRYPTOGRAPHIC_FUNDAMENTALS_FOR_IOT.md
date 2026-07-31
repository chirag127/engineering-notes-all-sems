## Unit 2 - Cryptographic Fundamentals for IoT

- Cryptography is the science of securing information by transforming it into a form that only the intended recipients can understand.
- Cryptography is essential for IoT devices, which often communicate over wireless networks and store sensitive data on cloud servers.
- Cryptography can provide confidentiality, integrity, authentication, and non-repudiation for IoT data and communications.
- Confidentiality means that only authorized parties can access the information.
- Integrity means that the information is not altered or corrupted during transmission or storage.
- Authentication means that the parties involved can verify each other's identity and legitimacy.
- Non-repudiation means that the parties cannot deny their involvement in the communication or transaction.
- Cryptography relies on two main concepts: encryption and digital signatures.
- Encryption is the process of transforming plaintext (the original information) into ciphertext (the encrypted information) using a secret key.
- Decryption is the reverse process of recovering the plaintext from the ciphertext using the same or a different key.
- There are two types of encryption: symmetric and asymmetric.
- Symmetric encryption uses the same key for both encryption and decryption. It is fast and efficient, but requires a secure way to share the key between the parties.
- Asymmetric encryption uses a pair of keys: a public key and a private key. The public key can be shared with anyone, while the private key is kept secret by the owner. The public key can be used to encrypt messages for the owner, and the private key can be used to decrypt them. The private key can also be used to encrypt messages for others, and the public key can be used to decrypt them. This is called digital signature.
- Digital signature is a way of proving the authenticity and integrity of a message by encrypting a hash (a fixed-length summary) of the message with the private key. The receiver can verify the signature by decrypting it with the public key and comparing the hash with the one computed from the message.
- There are many algorithms and protocols for encryption and digital signature, such as AES, RSA, ECC, SHA, HMAC, etc. Each has its own advantages and disadvantages in terms of security, performance, and compatibility.
- IoT devices should use the most suitable cryptographic methods according to their capabilities and requirements. They should also follow the best practices and standards for key management, encryption modes, padding schemes, etc. to avoid common pitfalls and vulnerabilities.