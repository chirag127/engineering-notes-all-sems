### Hashes for the notes of the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT in the subject of PRIVACY AND SECURITY IN IOT

In the world of IoT, data is constantly being generated and transmitted between devices. To ensure privacy and security, cryptographic principles and techniques are used. One of the fundamental cryptographic techniques used in IoT is hashing.

A hash function is a mathematical function that takes in an input (also called a message or data) and returns a fixed-size output (also called a hash or digest). The output is typically a string of characters that is unique to the input that was used. Some key points to keep in mind about hashes include:

- Hashes are deterministic, meaning that the same input will always produce the same output.
- Hashes are one-way, meaning that it's practically impossible to reconstruct the original input from the output.
- Hashes are collision-resistant, meaning that it's very difficult to find two different inputs that produce the same output.
- Hashes are easy to compute, meaning that it's relatively fast to generate a hash from an input.

Some common uses of hashes in IoT include:

- Message Integrity: Hashes are used to ensure that a message sent from one device to another has not been tampered with during transmission. The sender generates a hash of the message before sending it, and the receiver generates a hash of the received message. If the two hashes match, then the message has not been tampered with.
- Password Storage: Hashes are often used to store passwords securely. When a user creates a password, it is hashed and the resulting hash is stored in a database. When the user logs in, their password is hashed and compared to the stored hash. If the two hashes match, then the user is authenticated.
- Digital Signatures: Hashes are used to create digital signatures that can be used to verify the authenticity of a message or document. The sender generates a hash of the message or document and then encrypts the hash with their private key. The receiver can then decrypt the hash using the sender's public key and verify that the message or document has not been tampered with.

Some commonly used hash functions in IoT include:

- SHA-256: This is a widely used hash function that produces a 256-bit output. It is considered to be very secure and is commonly used for message integrity and password storage.
- MD5: This is an older hash function that produces a 128-bit output. It is not considered to be as secure as SHA-256 and is not recommended for new applications.
- SHA-3: This is a newer hash function that was selected as the winner of the NIST hash function competition. It produces variable-length outputs and is considered to be very secure.

In conclusion, hashes are a fundamental tool in the world of IoT security. They provide a way to ensure the integrity and authenticity of messages, passwords, and other data, and are an essential part of any secure IoT system.