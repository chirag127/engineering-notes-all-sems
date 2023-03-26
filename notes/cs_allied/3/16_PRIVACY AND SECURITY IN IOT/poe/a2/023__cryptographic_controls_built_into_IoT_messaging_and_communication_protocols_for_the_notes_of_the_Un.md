 Here are the notes on cryptographic controls built into IoT messaging and communication protocols:

### Cryptographic controls in IoT protocols

- Encryption: Encrypting the data being transmitted between IoT devices and servers ensures confidentiality. Common encryption algorithms for IoT include AES, ECC, etc. The keys used for encryption/decryption must be securely managed.
- Digital signatures: Digital signatures using asymmetric keys ensure authenticity and non-repudiation. The sender signs the message with their private key and the receiver verifies it with the sender's public key. This proves that the message came from the legitimate sender and the sender cannot deny it.
- Hashing: Hash functions like SHA-256 can be used to generate message digests/hashes to ensure integrity. The sender calculates the hash of the message and sends it with the message. The receiver recalculates the hash and compares it with the sent hash to check for any changes in the message.
- Certificate-based authentication: X.509 certificates can bind devices' identities to their public keys through a chain of trust anchored to a CA. This enables authentication of devices and secure communication using digital certificates. The CAs must securely issue and revoke certificates.

The above cryptographic controls can be implemented in IoT messaging protocols like MQTT, CoAP, etc. to provide security services for IoT data. However, the keys and certificates must be properly managed to avoid vulnerabilities. Furthermore, lightweight cryptography may be needed for constrained IoT devices.

The content summarizes some of the major cryptographic controls that can be built into IoT messaging and communication protocols to provide security services like confidentiality, authenticity, integrity, and non-repudiation. The notes are written in a formal tone with points and no emojis as instructed. Please let me know if you would like me to modify or expand the answer.