## Unit 2 - Cryptographic Fundamentals for IoT

- Cryptography is the science of securing information by transforming it into unintelligible forms using mathematical techniques and algorithms.
- Cryptography is essential for IoT devices, which are often connected to the internet and transmit sensitive data such as personal information, location, health status, etc.
- Cryptography can provide the following security services for IoT devices:
  - Confidentiality: preventing unauthorized access to the data by encrypting it with a secret key.
  - Integrity: ensuring that the data has not been tampered with by using a hash function or a message authentication code (MAC).
  - Authentication: verifying the identity of the sender or the receiver by using a digital signature or a challenge-response protocol.
  - Non-repudiation: preventing the sender or the receiver from denying their involvement in the communication by using a digital signature or a timestamp.
  - Key management: generating, distributing, storing, and revoking cryptographic keys in a secure and efficient way.
- Cryptography can be classified into two main types: symmetric and asymmetric.
  - Symmetric cryptography uses the same key for both encryption and decryption. It is fast and efficient, but requires a secure way to share the key between the parties. Examples of symmetric algorithms are AES, DES, RC4, etc.
  - Asymmetric cryptography uses different keys for encryption and decryption. The encryption key is public and can be shared with anyone, while the decryption key is private and kept secret by the owner. It is slower and more complex, but does not require a secure way to share the key. Examples of asymmetric algorithms are RSA, ECC, ElGamal, etc.
- Cryptography can also be classified into two main modes: block and stream.
  - Block cryptography operates on fixed-length blocks of data, usually 64 or 128 bits. It can provide both confidentiality and integrity, but may introduce padding or block alignment issues. Examples of block modes are ECB, CBC, CTR, etc.
  - Stream cryptography operates on individual bits or bytes of data, usually in a sequential manner. It can provide only confidentiality, but is more flexible and adaptable to different data formats. Examples of stream modes are OFB, CFB, Salsa20, etc.