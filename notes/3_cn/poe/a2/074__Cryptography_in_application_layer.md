 Here is the content in markdown format with formal tone and without emojis:

### Cryptography in application layer

1. Encryption of data - Data such as passwords, credit card numbers, personal information etc. are encrypted before storing or transmitting over the network. This ensures data confidentiality. Some commonly used encryption algorithms are AES, RSA, ECC etc.

2. Digital signatures - Digital signatures are used to provide authentication, data integrity and non-repudiation. The sender's private key is used to sign the data which can be verified using the sender's public key. This proves that the data was indeed signed by the sender and was not modified in transit. Digital signatures are used in software distribution, financial transactions etc.

3. Key exchange - Two parties communicating over the network need to establish a shared secret key to encrypt their data. Key exchange protocols are used to negotiate and establish a shared key. Some popular key exchange protocols are Diffie-Hellman key exchange and Elliptic curve Diffie-Hellman key exchange.

4. Hashing - Hashing functions are used to generate a short digest of a larger data such as files and messages. Even a small change in the data results in a different hash value. This is useful to verify data integrity. Some commonly used hashing algorithms are SHA-1, SHA-256, MD5 etc. Hashing is used to store passwords in databases in a secured way.

The above are some of the core ways in which cryptography is used in the application layer to provide security services such as confidentiality, authentication, integrity and non-repudiation. Cryptography, when implemented correctly, serves as a strong defense against potential attacks and threats to applications.