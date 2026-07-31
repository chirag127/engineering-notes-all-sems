### Cryptographic primitives and its role in IoT

Cryptographic primitives are basic operations or algorithms that are used to build cryptographic protocols and systems. They provide the essential security functions such as encryption, decryption, authentication, digital signatures, hashing, etc. Cryptographic primitives can be classified into two categories: symmetric and asymmetric.

Symmetric primitives use the same key for both encryption and decryption, and are usually faster and more efficient than asymmetric primitives. Symmetric primitives include block ciphers, stream ciphers, message authentication codes (MACs), etc. Asymmetric primitives use different keys for encryption and decryption, and are usually more secure and flexible than symmetric primitives. Asymmetric primitives include public-key encryption, digital signatures, key exchange, etc.

Cryptographic primitives play an important role in IoT, as they enable the protection of data and communication among the heterogeneous and resource-constrained devices. IoT devices are often vulnerable to various attacks, such as eavesdropping, tampering, spoofing, denial-of-service, etc. Therefore, cryptographic primitives are needed to ensure the confidentiality, integrity, authenticity, and availability of the data and services in IoT.

However, not all cryptographic primitives are suitable for IoT, as they may have high computational, communication, and storage overheads that exceed the capabilities of the IoT devices. Therefore, lightweight cryptography, which is a branch of cryptography that aims to design and optimize cryptographic primitives for resource-limited environments, is a promising solution for IoT security. Lightweight cryptography can reduce the complexity, power consumption, and memory requirements of the cryptographic primitives, while still providing adequate security levels.

Some examples of lightweight cryptographic primitives for IoT are:

- PRESENT: a lightweight block cipher that uses 64-bit blocks and 80-bit or 128-bit keys, and has a simple and compact design that can be implemented in hardware or software.
- ChaCha: a lightweight stream cipher that uses 256-bit keys and 64-bit nonces, and has a fast and parallelizable design that can be implemented in software.
- SipHash: a lightweight MAC that uses 128-bit keys and 64-bit outputs, and has a simple and efficient design that can be implemented in software or hardware.
- ECDSA: a lightweight digital signature scheme that uses elliptic curve cryptography (ECC), which can provide the same security level as RSA with much smaller key sizes and computations.
- ECDH: a lightweight key exchange scheme that also uses ECC, which can enable secure and authenticated communication between IoT devices.