## Unit 4 - Basic Cryptography

Cryptography is the practice of secure communication in the presence of third parties. It involves techniques for secure communication, data integrity, and authentication.

1. **Encryption** is the process of converting plaintext into ciphertext, which is unreadable without the key to decrypt it. The key is a piece of information that is used to encrypt and decrypt the message.

2. **Decryption** is the process of converting ciphertext back into plaintext using the key.

3. **Symmetric encryption** uses the same key for both encryption and decryption. The key must be kept secret and shared only between the sender and the receiver.

4. **Asymmetric encryption** uses a pair of keys, one for encryption and one for decryption. The public key is used to encrypt the message and can be shared with anyone, while the private key is used to decrypt the message and must be kept secret.

5. **Hashing** is the process of converting a message into a fixed-length string of characters, called a hash, that represents the message. Hashing is used for data integrity and authentication.

6. **Digital signatures** use a combination of hashing and asymmetric encryption to provide authentication and non-repudiation. The sender signs the message by encrypting the hash of the message with their private key. The receiver can verify the signature by decrypting the signature with the sender's public key and comparing the resulting hash with the hash of the received message.

7. **Key exchange** is the process of securely exchanging keys between parties. One common method is the Diffie-Hellman key exchange, which allows two parties to generate a shared secret key over an insecure channel.

These are some of the basic concepts in cryptography. Cryptography is a complex and constantly evolving field, with new techniques and algorithms being developed to improve security and efficiency. It is an essential tool for protecting information in the digital age.