### Basic concepts of cryptography in application layer

Cryptography is the science of securing communications from unauthorized parties. It involves the use of mathematical techniques to transform plain text into cipher text, which is unintelligible, and vice versa. Cryptography can provide confidentiality, integrity and authenticity to the data transmitted or stored in applications.

Some of the basic concepts of cryptography in application layer are:

- **Symmetric key cryptography**: This is a type of cryptography where the same key is used for both encryption and decryption. The key must be shared securely between the communicating parties. Symmetric key cryptography is fast and efficient, but it suffers from the key distribution problem, which is how to securely exchange the key without compromising it. Examples of symmetric key algorithms are AES, DES, RC4, etc.

- **Asymmetric key cryptography**: This is a type of cryptography where a pair of keys is used for encryption and decryption. One key is called the public key, which can be freely distributed, and the other is called the private key, which must be kept secret. The public key can be used to encrypt a message, which can only be decrypted by the corresponding private key. The private key can also be used to sign a message, which can be verified by the public key. Asymmetric key cryptography solves the key distribution problem of symmetric key cryptography, but it is slower and more complex. Examples of asymmetric key algorithms are RSA, ECC, DSA, etc.

- **Hash functions**: These are mathematical functions that map an arbitrary input to a fixed-length output, called the hash or digest. Hash functions are one-way, meaning that it is easy to compute the hash from the input, but hard to find the input from the hash. Hash functions can be used to provide integrity to the data, by verifying that the data has not been tampered with. Examples of hash functions are SHA, MD5, etc.

- **Digital signatures**: These are a way of using asymmetric key cryptography to provide authenticity and non-repudiation to the data. A digital signature is a value that is computed from the data and the signer's private key, and attached to the data. Anyone who has the signer's public key can verify the signature and the data. A digital signature proves that the data was signed by the owner of the private key, and that the data was not altered after signing. Examples of digital signature algorithms are RSA, DSA, ECDSA, etc.

- **Encryption modes**: These are ways of applying symmetric key cryptography to encrypt or decrypt a stream of data. Different encryption modes have different properties and trade-offs, such as security, performance, error propagation, etc. Examples of encryption modes are ECB, CBC, CTR, GCM, etc.

- **Cryptographic protocols**: These are rules and procedures that define how cryptography is used in applications to achieve specific goals, such as secure communication, authentication, key exchange, etc. Cryptographic protocols often involve multiple steps and parties, and use various cryptographic primitives and techniques. Examples of cryptographic protocols are SSL/TLS, SSH, PGP, etc.