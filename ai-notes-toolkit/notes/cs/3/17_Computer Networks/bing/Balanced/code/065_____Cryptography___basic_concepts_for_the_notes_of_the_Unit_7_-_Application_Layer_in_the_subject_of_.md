### Cryptography – basic concepts

Cryptography is the science and art of designing and using techniques to secure communication and data in the presence of adversaries. Cryptography has many applications, such as protecting the confidentiality, integrity, and authenticity of information, enabling secure transactions, authentication, digital signatures, and encryption.

Some basic concepts of cryptography are:

- **Plaintext**: The original message or data that needs to be encrypted or protected.
- **Ciphertext**: The encrypted or transformed version of the plaintext that is unreadable by unauthorized parties.
- **Encryption**: The process of converting plaintext into ciphertext using a secret key and an algorithm.
- **Decryption**: The process of converting ciphertext back into plaintext using the same or a different secret key and an algorithm.
- **Key**: A secret value that is used to encrypt or decrypt data. The key should be chosen randomly and securely, and should be kept secret from unauthorized parties.
- **Algorithm**: A set of rules or steps that are used to encrypt or decrypt data. The algorithm should be secure, meaning that it is hard to break or reverse without knowing the key.
- **Symmetric-key cryptography**: A type of cryptography where the same key is used to encrypt and decrypt data. The key should be shared securely between the sender and the receiver. Examples of symmetric-key algorithms are AES, DES, and RC4.
- **Asymmetric-key cryptography**: A type of cryptography where different keys are used to encrypt and decrypt data. The sender and the receiver each have a pair of keys: a public key and a private key. The public key can be shared openly, while the private key should be kept secret. The sender can encrypt data using the receiver's public key, and the receiver can decrypt it using their own private key. Examples of asymmetric-key algorithms are RSA, ECC, and DSA.
- **Hash function**: A function that maps any input data to a fixed-length output, called a hash or a digest. The hash function should be one-way, meaning that it is easy to compute the hash from the input, but hard to find the input from the hash. The hash function should also be collision-resistant, meaning that it is hard to find two different inputs that produce the same hash. Hash functions are used to verify the integrity and authenticity of data, such as passwords, digital signatures, and checksums. Examples of hash functions are SHA-256, MD5, and BLAKE2.