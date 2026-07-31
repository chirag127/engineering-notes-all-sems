### Basic concepts of Cryptography in application layer

- Cryptography is the science of securing communications from adversaries by using mathematical techniques and algorithms.
- Cryptography can provide confidentiality, integrity, authenticity, and non-repudiation to the data transmitted or stored in applications.
- Cryptography can be classified into two main types: symmetric and asymmetric.
- Symmetric cryptography uses the same key for both encryption and decryption of data. The key must be shared securely between the sender and the receiver. Examples of symmetric algorithms are AES, DES, and RC4.
- Asymmetric cryptography, also known as public key cryptography, uses a pair of keys for encryption and decryption of data. One key is public and can be shared with anyone, while the other key is private and must be kept secret. The public key can be used to encrypt data, which can only be decrypted by the private key, or vice versa. Examples of asymmetric algorithms are RSA, ECC, and DSA.
- Cryptography can be applied in various layers of the network stack, such as the physical, data link, network, transport, and application layers. The application layer is the closest to the user and provides end-to-end security for the data.
- Some examples of cryptographic applications in the application layer are:

  - Secure Sockets Layer (SSL) and Transport Layer Security (TLS): These protocols provide secure communication between web browsers and web servers, using both symmetric and asymmetric cryptography. They also support digital certificates, which are used to verify the identity of the web servers and prevent man-in-the-middle attacks.
  - Secure Shell (SSH): This protocol provides secure remote access to servers and devices, using both symmetric and asymmetric cryptography. It also supports authentication, encryption, and integrity of the data.
  - Pretty Good Privacy (PGP) and GNU Privacy Guard (GPG): These are applications that provide secure email communication, using both symmetric and asymmetric cryptography. They also support digital signatures, which are used to verify the identity and integrity of the sender and the message.
  - Bitcoin and other cryptocurrencies: These are digital currencies that use cryptography to create and verify transactions, using both symmetric and asymmetric cryptography. They also use hash functions, which are mathematical functions that map any input to a fixed-length output, to create a public ledger of transactions, called the blockchain.