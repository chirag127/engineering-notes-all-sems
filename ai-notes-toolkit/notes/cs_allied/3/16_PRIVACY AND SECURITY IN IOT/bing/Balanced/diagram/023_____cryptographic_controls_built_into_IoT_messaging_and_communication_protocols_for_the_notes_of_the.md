### Cryptographic controls built into IoT messaging and communication protocols

- Cryptographic controls are methods of applying authentication, data integrity, and confidentiality protections to information and communications.
- Cryptographic controls are essential for securing IoT point-to-point and end-to-end communications, as IoT devices often operate in untrusted or hostile environments.
- Cryptographic controls can be integrated into various IoT protocols, such as ZigBee, ZWave, Bluetooth-LE, MQTT, CoAP, and HTTPS.
- Each IoT protocol has different configuration options and trade-offs for applying cryptographic controls, depending on the device capabilities, network topology, and communication requirements.
- Some of the common cryptographic controls used in IoT protocols are:

  - Symmetric encryption: A method of encrypting and decrypting data using the same secret key. Symmetric encryption is fast and efficient, but requires a secure way of distributing and managing the keys. Examples of symmetric encryption algorithms are AES, DES, and RC4.
  - Asymmetric encryption: A method of encrypting and decrypting data using a pair of public and private keys. Asymmetric encryption is more secure and scalable, but requires more computational resources and bandwidth. Examples of asymmetric encryption algorithms are RSA, ECC, and DH.
  - Hashing: A method of generating a fixed-length output from an input data, such that the output is unique and irreversible. Hashing is used to verify the integrity and authenticity of data, but does not provide confidentiality. Examples of hashing algorithms are SHA, MD5, and HMAC.
  - Digital signature: A method of generating and verifying a signature from a message and a private key, such that the signature proves the identity of the sender and the integrity of the message. Digital signature is a form of asymmetric encryption that provides non-repudiation and accountability. Examples of digital signature algorithms are RSA, DSA, and ECDSA.
  - Certificate: A digital document that contains the public key and identity information of an entity, such as a device, a server, or a user. Certificate is used to establish trust and authenticity between entities, but requires a trusted authority to issue and validate the certificates. Examples of certificate standards are X.509, PKCS, and PGP.