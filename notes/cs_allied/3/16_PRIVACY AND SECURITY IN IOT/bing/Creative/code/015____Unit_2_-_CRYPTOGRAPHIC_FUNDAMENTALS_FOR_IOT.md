# Unit 2 - Cryptographic Fundamentals for IoT

Cryptography is the process of securing information by transforming the information into a secure format and vice versa. In other words, encrypting and decrypting the information to protect it. Cryptography can be used in various areas of an IoT deployment, such as:

- Securing communication channels. IoT-centric communication protocols like MQTT and AMQP allow developers to use Transport Layer Security (TLS) to ensure all data sent over the network is unreadable to outside parties.
- Securing data storage. IoT devices and applications may need to store sensitive data locally or in the cloud, and cryptography can help to encrypt the data and prevent unauthorized access or modification.
- Securing device identity and authentication. IoT devices and applications may need to verify their identity and authenticate with other devices or services, and cryptography can help to generate and validate digital signatures and certificates.

There are different types of cryptography algorithms that can be used for IoT, depending on the security requirements, performance, and resource constraints. Some of the common types are:

- Symmetric-key cryptography. This type of cryptography uses the same key for both encryption and decryption, and it is fast and efficient. However, it requires a secure way to distribute and manage the keys among the parties involved. Examples of symmetric-key algorithms are Data Encryption Standard (DES), Advanced Encryption Standard (AES), and Twofish.
- Asymmetric-key cryptography. This type of cryptography uses different keys for encryption and decryption, and it is more secure and flexible. However, it is slower and more computationally intensive. Examples of asymmetric-key algorithms are RSA, Elliptic Curve Cryptography (ECC), and Diffie-Hellman Key Exchange (DHKE).
- Hashing. This type of cryptography does not use any keys, but it generates a fixed-length output from any input, and it is irreversible and unique. Hashing can be used to verify the integrity and authenticity of data, but it cannot be used to encrypt or decrypt data. Examples of hashing algorithms are Secure Hash Algorithm (SHA), Message Digest Algorithm (MD), and Hash-based Message Authentication Code (HMAC).

Cryptography is an essential component of IoT security, but it is not sufficient by itself. IoT developers and users also need to consider other aspects of security, such as physical protection, network security, access control, and privacy. Cryptography should be used as a part of a comprehensive security strategy that addresses the specific needs and challenges of each IoT scenario.