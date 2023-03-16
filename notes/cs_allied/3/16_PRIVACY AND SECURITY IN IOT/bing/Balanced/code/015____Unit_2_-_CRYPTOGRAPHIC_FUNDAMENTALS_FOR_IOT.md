## Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT

- Cryptography is the science of securing information by transforming it into a form that only the intended recipients can understand.
- Cryptography is essential for IoT devices, which are often connected to the internet and exchange sensitive data with other devices or servers.
- Cryptography can provide the following security services for IoT devices:
  - Confidentiality: preventing unauthorized access to the data.
  - Integrity: ensuring that the data has not been tampered with or corrupted.
  - Authentication: verifying the identity of the sender or receiver of the data.
  - Non-repudiation: preventing the sender or receiver from denying their involvement in the data exchange.
  - Access control: restricting the access to the data based on certain rules or policies.
- Cryptography can be classified into two main types: symmetric and asymmetric.
  - Symmetric cryptography uses the same key for both encryption and decryption. The key must be shared securely between the sender and receiver before the data exchange. Symmetric cryptography is fast and efficient, but it has the drawback of key distribution and management. Examples of symmetric algorithms are AES, DES, and RC4.
  - Asymmetric cryptography uses different keys for encryption and decryption. The sender uses the receiver's public key to encrypt the data, and the receiver uses their own private key to decrypt it. The public key can be shared openly, while the private key must be kept secret. Asymmetric cryptography is more secure and scalable, but it is slower and more computationally intensive than symmetric cryptography. Examples of asymmetric algorithms are RSA, ECC, and DH.
- Cryptography can also be classified into two other types: stream and block.
  - Stream cryptography encrypts or decrypts each bit or byte of the data individually, using a keystream that is derived from a secret key and a nonce. Stream cryptography is suitable for continuous or real-time data streams, such as audio or video. Examples of stream algorithms are RC4, ChaCha20, and A5/1.
  - Block cryptography encrypts or decrypts a fixed-size block of data at a time, using a secret key and a mode of operation. Block cryptography is suitable for discrete or static data, such as files or messages. Examples of block algorithms are AES, DES, and Blowfish.