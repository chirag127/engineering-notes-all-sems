### Cryptography in application layer

- Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application.
- When encryption occurs at this level, data is encrypted across multiple layers, such as disk, file, and database .
- This approach increases security by reducing the number of potential attack vectors and allows the application to tune the protections to the sensitivity of the data or even to specific users and groups .
- Cryptography in application layer can also help with regulatory compliance, such as PCI DSS, by securing sensitive data before storing it in database, big data, or cloud environments .
- Cryptography in application layer can use either symmetric or asymmetric encryption algorithms, depending on the use case and the security requirements.
- Symmetric encryption uses a single shared key for both encryption and decryption, while asymmetric encryption uses two keys – public key and private key.
- Symmetric encryption is faster and more efficient, but requires a secure way to distribute and manage the keys.
- Asymmetric encryption is slower and more complex, but allows public key distribution and digital signatures.
- Some examples of symmetric encryption algorithms are RC4, DES, AES, while some examples of asymmetric encryption algorithms are RSA, ECC, ElGamal.
- Cryptography in application layer can also use hashing algorithms, which are irreversible functions that produce a fixed-length output from any input.
- Hashing algorithms can be used to verify the integrity and authenticity of the data, such as user passwords, digital signatures, or message digests.
- Some examples of hashing algorithms are MD5, SHA1, SHA256, SHA512, Bcrypt.
- A mnemonic to remember the difference between encoding, encryption, and hashing is: Encoding is reversible, encryption is reversible with a key, hashing is irreversible.
- A mnemonic to remember the difference between symmetric and asymmetric encryption is: Symmetric encryption uses the same key, asymmetric encryption uses different keys.
- A mnemonic to remember some common symmetric and asymmetric encryption algorithms is: RC-DES-AES are symmetric, RSA-ECC-ElGamal are asymmetric.
- A mnemonic to remember some common hashing algorithms is: MD-SHA-BC are hashing.
- A diagram to illustrate the concept of cryptography in application layer is:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Application   |       |   Application   |       |   Application   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Encryption    |       |   Encryption    |       |   Encryption    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|     Disk        |       |     File        |       |    Database     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```