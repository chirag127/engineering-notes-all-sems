# RSA public key cryptography

- RSA is a type of public-key cryptography that is widely used for secure data transmission over the internet  .
- Public-key cryptography is a system that uses two different keys: a public key and a private key. The public key can be shared with anyone, while the private key is kept secret by the owner .
- RSA is named after its inventors, Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman, who publicly described the algorithm in 1977 .
- RSA is based on the mathematical problem of factoring large numbers, which is believed to be hard to solve efficiently by classical computers .
- RSA works as follows  :
  - Key generation: The sender and the receiver each generate a pair of keys (public and private) by choosing two large prime numbers and performing some calculations.
  - Encryption: The sender encrypts a message (plaintext) by using the receiver's public key and a mathematical function to produce a ciphertext, which is sent to the receiver.
  - Decryption: The receiver decrypts the ciphertext by using their own private key and another mathematical function to recover the original message (plaintext).
- RSA encryption can be used for various purposes, such as establishing secure connections, signing digital documents, encrypting files, and authenticating users .
- RSA encryption has some advantages and disadvantages, such as:
  - Advantages: It is simple, elegant, and widely supported. It does not require a secure channel to exchange keys. It can provide both confidentiality and integrity.
  - Disadvantages: It is slow, computationally intensive, and vulnerable to some attacks. It requires large key sizes and padding schemes to be secure. It does not provide forward secrecy or anonymity.