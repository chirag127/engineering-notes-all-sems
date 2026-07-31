## Unit 4 - Basic cryptography

- Cryptography is the science of securing information by transforming it into a form that only the intended recipients can understand.
- Cryptography has two main goals: confidentiality and integrity.
  - Confidentiality means that only authorized parties can access the information.
  - Integrity means that the information is not altered or tampered with by unauthorized parties.
- Cryptography uses two basic techniques: encryption and hashing.
  - Encryption is the process of transforming plaintext (the original information) into ciphertext (the encrypted information) using a secret key.
  - Decryption is the reverse process of transforming ciphertext back into plaintext using the same or a different key.
  - Hashing is the process of transforming any information into a fixed-length string called a hash or a digest, using a mathematical function.
  - Hashing is irreversible, meaning that it is impossible to recover the original information from the hash.
- Cryptography can be classified into two types: symmetric and asymmetric.
  - Symmetric cryptography uses the same key for both encryption and decryption. The key must be shared securely between the sender and the receiver.
  - Asymmetric cryptography uses different keys for encryption and decryption. The sender uses the receiver's public key to encrypt the information, and the receiver uses their own private key to decrypt it. The public key can be shared openly, while the private key must be kept secret.
- Some examples of symmetric encryption algorithms are AES, DES, and RC4.
- Some examples of asymmetric encryption algorithms are RSA, ECC, and ElGamal.
- Some examples of hashing algorithms are SHA, MD5, and RIPEMD.