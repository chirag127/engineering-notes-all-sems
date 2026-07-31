# Cryptographic controls built into IoT messaging and communication protocols

- Cryptographic controls are methods and techniques that use codes to protect information and communications, making them inaccessible to all but those authorized to decipher the codes.
- Cryptographic controls are essential for securing IoT point-to-point and end-to-end communications, as IoT devices often operate in untrusted or hostile environments and transmit sensitive or personal data .
- Cryptographic controls can provide authentication, data integrity, and confidentiality protections for IoT messaging and communication protocols .
- Some examples of IoT messaging and communication protocols that support cryptographic controls are:
  - ZigBee: a low-power, low-data-rate wireless network protocol that uses symmetric-key cryptography for authentication and encryption, and supports the use of pre-shared keys, certificates, or trust center modes for key management .
  - ZWave: a wireless mesh network protocol that uses AES-128 encryption for data protection, and supports the use of network-wide inclusion (NWI) or secure inclusion (S2) modes for key exchange and authentication .
  - Bluetooth-LE: a wireless personal area network protocol that uses AES-CCM encryption for data protection, and supports the use of legacy pairing, secure connections, or out-of-band methods for key exchange and authentication .
  - MQTT: a lightweight publish-subscribe protocol that uses TLS/SSL encryption for data protection, and supports the use of certificates, pre-shared keys, or username/password for authentication .
  - CoAP: a constrained application protocol that uses DTLS encryption for data protection, and supports the use of certificates, pre-shared keys, or raw public keys for authentication .
- Cryptographic controls should be applied in a layered and consistent manner across different types of IoT protocols, and should consider the trade-offs between security, performance, and usability .