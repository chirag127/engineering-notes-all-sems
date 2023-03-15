# Cryptography – basic concepts

Cryptography is the science and art of designing and using techniques to secure communication and data in the presence of adversaries. Cryptography has many applications, such as protecting the confidentiality, integrity, and authenticity of information, enabling secure transactions, authentication, digital signatures, and encryption.

Some basic concepts of cryptography are:

- **Plaintext**: The original message or data that needs to be encrypted or decrypted.
- **Ciphertext**: The encrypted or transformed version of the plaintext that is unreadable by unauthorized parties.
- **Encryption**: The process of converting plaintext into ciphertext using a secret key and an algorithm.
- **Decryption**: The process of converting ciphertext back into plaintext using the same or a different secret key and an algorithm.
- **Key**: A secret value that is used to encrypt or decrypt the plaintext or ciphertext. The key can be a string of bits, a password, a passphrase, or a file.
- **Algorithm**: A set of rules or steps that defines how to encrypt or decrypt the plaintext or ciphertext. The algorithm can be a mathematical function, a formula, or a program.
- **Symmetric-key cryptography**: A type of cryptography where the same key is used for both encryption and decryption. The key must be shared securely between the sender and the receiver. Examples of symmetric-key algorithms are AES, DES, and RC4.
- **Asymmetric-key cryptography**: A type of cryptography where different keys are used for encryption and decryption. The sender and the receiver each have a pair of keys: a public key and a private key. The public key can be shared openly, while the private key must be kept secret. The sender encrypts the plaintext with the receiver's public key, and the receiver decrypts the ciphertext with their own private key. Examples of asymmetric-key algorithms are RSA, ECC, and DSA.
- **Hash function**: A one-way function that maps an arbitrary input to a fixed-length output, called a hash or a digest. The hash function should be deterministic, meaning that the same input always produces the same output. The hash function should also be collision-resistant, meaning that it is hard to find two different inputs that produce the same output. Hash functions are used to verify the integrity and authenticity of data, such as passwords, digital signatures, and checksums. Examples of hash functions are SHA-1, SHA-2, and MD5.