## Unit 2 - RFID False Authentications

- RFID stands for Radio Frequency Identification, a technology that uses radio waves to identify objects or people by attaching tags to them.
- RFID tags can store information such as a unique identifier, product name, price, etc. and can be read by RFID readers that emit radio signals and receive the tag's response.
- RFID authentication is the process of verifying the identity and validity of a tag or a reader, to prevent unauthorized access, counterfeiting, or cloning of RFID tags.
- RFID false authentication is the situation where a legitimate tag is wrongly rejected by a reader, or a fake tag is wrongly accepted by a reader, due to flaws or attacks on the authentication protocol.
- RFID false authentication can have serious consequences, such as loss of revenue, damage to reputation, compromise of security, or violation of privacy.
- RFID false authentication can be caused by various factors, such as:
  - Incompatibility between the authentication protocol and the RFID standard, such as C1G2 (class 1 generation 2) passive RFID tags, which have limited memory and computation capabilities .
  - Weaknesses or errors in the design or implementation of the authentication protocol, such as using insecure hash functions, random number generators, or encryption schemes.
  - Attacks by malicious parties, such as eavesdropping, replaying, modifying, or blocking the communication between the tag and the reader, or cloning, spoofing, or destroying the tag .
- RFID false authentication can be prevented or mitigated by using various techniques, such as:
  - Choosing an appropriate authentication protocol that matches the RFID standard and the security requirements of the application.
  - Applying cryptographic methods, such as encryption, digital signatures, or message authentication codes, to protect the confidentiality, integrity, and authenticity of the tag and the reader .
  - Implementing two-factor authentication, which requires the tag to provide something it knows (such as a password or a PIN) and something it has (such as a physical token or a biometric feature) to authenticate itself.
  - Using physical or logical tamper-proof mechanisms, such as seals, locks, or checksums, to detect or prevent any alteration or damage to the tag or the reader.