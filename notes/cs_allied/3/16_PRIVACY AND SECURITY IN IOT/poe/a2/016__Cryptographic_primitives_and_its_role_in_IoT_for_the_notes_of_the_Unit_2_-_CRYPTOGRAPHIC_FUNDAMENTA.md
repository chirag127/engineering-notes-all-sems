 Here are the notes in markdown format without any emojis or external links and in a formal tone:

### Cryptographic primitives and its role in IoT

1. Cryptographic hash functions
- Produce a fixed-size hash value from a variable-sized input
- Used for data integrity (detect changes in data) and as a building block for other primitives like HMAC and digital signatures
- Examples: SHA-256, SHA-512, MD5

2. Symmetric-key cryptography
- Uses the same key for encryption and decryption
- Provides confidentiality (encryption) and data origin authentication (HMAC)
- Examples: AES, DES, RC4, HMAC
- Used to securely establish shared keys between devices for subsequent encryption/authentication

3. Asymmetric-key cryptography (public-key cryptography)
- Uses a public/private key pair - data encrypted with one key can only be decrypted with the other key
- Used for key exchange, digital signatures, and confidentiality
- Examples: RSA, ECC, DSA, ECDSA
- Used during initial device onboarding to securely establish a shared symmetric key

4. Digital signatures
- Produced using the private key of an asymmetric key pair and verified using the corresponding public key
- Provide data origin authentication and non-repudiation (prevent sender from denying they sent the data)
- Examples: RSA, DSA, ECDSA signatures
- Used to sign software/firmware updates, ensure authenticity of sensitive data, etc.

The cryptographic primitives described above form the building blocks for securing communications and data in IoT systems. They are crucial for ensuring properties like confidentiality, integrity, authentication, and non-repudiation in IoT implementations. Appropriate choices and correct usage of these primitives is vital to designing robust and secure IoT systems.