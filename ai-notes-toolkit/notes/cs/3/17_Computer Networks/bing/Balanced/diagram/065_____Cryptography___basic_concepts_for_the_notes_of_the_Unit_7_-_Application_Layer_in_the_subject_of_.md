### Cryptography – basic concepts

Cryptography is the science and art of designing and using techniques to secure communication and data in the presence of adversaries. Cryptography has many applications, such as protecting the confidentiality, integrity, and authenticity of information, enabling secure transactions, authentication, digital signatures, and encryption.

Some basic concepts of cryptography are:

- **Plaintext**: The original message or data that needs to be encrypted or protected.
- **Ciphertext**: The encrypted or transformed version of the plaintext that is unreadable by unauthorized parties.
- **Encryption**: The process of converting plaintext into ciphertext using a secret key and an algorithm.
- **Decryption**: The process of converting ciphertext back into plaintext using the same or a different key and algorithm.
- **Key**: A secret value or parameter that is used by the encryption and decryption algorithms to produce the ciphertext and plaintext.
- **Algorithm**: A set of rules or steps that define how the encryption and decryption are performed.
- **Symmetric-key cryptography**: A type of cryptography where the same key is used for both encryption and decryption. Examples of symmetric-key algorithms are AES, DES, and RC4.
- **Asymmetric-key cryptography**: A type of cryptography where different keys are used for encryption and decryption. One key is called the public key and can be shared with anyone, while the other key is called the private key and must be kept secret. Examples of asymmetric-key algorithms are RSA, ECC, and DSA.
- **Hash function**: A mathematical function that maps any input to a fixed-length output, called a hash or a digest. A hash function has the property that it is easy to compute the hash from the input, but hard to find the input from the hash. Hash functions are used for verifying the integrity and authenticity of data, such as in digital signatures and message authentication codes. Examples of hash functions are SHA-256, MD5, and BLAKE2.
- **Digital signature**: A cryptographic technique that allows a sender to sign a message with their private key, and a receiver to verify the signature with the sender's public key. A digital signature provides non-repudiation, meaning that the sender cannot deny having sent the message. Examples of digital signature schemes are RSA, DSA, and ECDSA.
- **Public-key infrastructure (PKI)**: A system that manages the creation, distribution, and verification of public keys and digital certificates. A digital certificate is a document that binds a public key to an identity, such as a name or an email address. A certificate authority (CA) is a trusted entity that issues and revokes digital certificates. Examples of PKI standards are X.509, PGP, and SSL/TLS.