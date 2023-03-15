## Unit 4 - Basic cryptography

Cryptography is the science of securing information by transforming it into unreadable forms, using mathematical techniques and algorithms. Cryptography has many applications, such as protecting data from unauthorized access, ensuring data integrity, authenticating identities, and enabling secure communication.

Some basic concepts and terms in cryptography are:

- **Plaintext**: The original message or data that is to be encrypted or decrypted.
- **Ciphertext**: The encrypted or transformed version of the plaintext that is unreadable by anyone who does not have the key.
- **Encryption**: The process of converting plaintext into ciphertext using a key and an algorithm.
- **Decryption**: The process of converting ciphertext back into plaintext using a key and an algorithm.
- **Key**: A secret value or parameter that is used by the encryption and decryption algorithms to transform the data. The key determines the output of the algorithms and must be kept secret from unauthorized parties.
- **Algorithm**: A set of rules or steps that define how the encryption and decryption are performed. The algorithm must be known by both the sender and the receiver of the encrypted data, but not by anyone else.
- **Symmetric-key cryptography**: A type of cryptography where the same key is used for both encryption and decryption. The sender and the receiver must share the key in advance and keep it secret from anyone else. Examples of symmetric-key algorithms are AES, DES, and RC4.
- **Asymmetric-key cryptography**: A type of cryptography where different keys are used for encryption and decryption. The sender and the receiver do not need to share the key in advance, but they must know each other's public key. The public key can be shared with anyone, but the private key must be kept secret by the owner. Examples of asymmetric-key algorithms are RSA, ECC, and ElGamal.
- **Hash function**: A mathematical function that maps any input data to a fixed-length output, called a hash or a digest. The hash function has the property that it is easy to compute the hash from the input, but it is hard to find the input from the hash, or to find two different inputs that produce the same hash. Hash functions are used for verifying data integrity, generating digital signatures, and creating passwords. Examples of hash functions are SHA-256, MD5, and BLAKE2.