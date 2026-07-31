# Encryption and Decryption

- Encryption is the process of transforming plaintext (readable data) into ciphertext (unreadable data) using a secret key and an encryption algorithm.
- Decryption is the reverse process of encryption, which transforms ciphertext back into plaintext using the same or a different secret key and a decryption algorithm.
- The purpose of encryption and decryption is to protect the confidentiality, integrity and authenticity of data from unauthorized access or modification.
- There are two main types of encryption: symmetric and asymmetric.
  - Symmetric encryption uses the same secret key for both encryption and decryption. The key must be shared securely between the sender and the receiver of the data. Examples of symmetric encryption algorithms are AES, DES, RC4, etc.
  - Asymmetric encryption uses a pair of keys: a public key and a private key. The public key can be shared openly, while the private key must be kept secret. The sender encrypts the data with the receiver's public key, and the receiver decrypts the data with their own private key. Examples of asymmetric encryption algorithms are RSA, ECC, ElGamal, etc.
- Encryption and decryption are essential for ensuring the privacy and security of data in IoT (Internet of Things) applications, where devices communicate with each other over wireless networks that may be vulnerable to eavesdropping, interception, tampering or spoofing.