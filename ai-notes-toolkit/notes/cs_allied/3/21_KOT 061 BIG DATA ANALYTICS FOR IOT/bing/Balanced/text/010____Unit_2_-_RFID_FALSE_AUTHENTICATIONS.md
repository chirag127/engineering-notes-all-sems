## Unit 2 - RFID False Authentications

- RFID stands for Radio Frequency Identification. It is a technology that uses radio waves to identify objects or people by attaching a small electronic device called a tag or a transponder to them.
- RFID tags can store information such as a unique identifier, a serial number, or other data. They can be read by a device called a reader or an interrogator, which emits radio signals and receives the responses from the tags.
- RFID systems can be used for various applications, such as inventory management, access control, asset tracking, identification, payment, and security.
- However, RFID systems are also vulnerable to false authentication attacks, which are attempts to impersonate a legitimate tag or reader, or to modify or forge the data exchanged between them.
- False authentication attacks can compromise the confidentiality, integrity, and availability of RFID systems, and cause various damages, such as unauthorized access, data theft, fraud, or sabotage.
- There are different types of false authentication attacks, such as:

  - Tag cloning: This is when an attacker copies the data from a legitimate tag and creates a duplicate tag that can be used to impersonate the original one.
  - Tag spoofing: This is when an attacker creates a fake tag that can respond to a reader's query with a valid identifier or data, without having access to the original tag.
  - Reader cloning: This is when an attacker copies the data from a legitimate reader and creates a duplicate reader that can be used to communicate with the tags as if it were the original one.
  - Reader spoofing: This is when an attacker creates a fake reader that can send malicious queries or commands to the tags, or intercept and modify the responses from the tags.
  - Replay attack: This is when an attacker captures and records the radio signals exchanged between a legitimate tag and reader, and then replays them later to fool the reader or the tag.
  - Relay attack: This is when an attacker uses two devices, one near the tag and one near the reader, to relay the radio signals between them, creating a virtual connection that can bypass the distance or security constraints of the RFID system.

- To prevent or detect false authentication attacks, RFID systems can use various countermeasures, such as:

  - Cryptography: This is the use of mathematical techniques to encrypt and decrypt the data exchanged between the tags and the readers, or to generate and verify digital signatures that can prove the identity and authenticity of the parties involved.
  - Authentication protocols: These are sets of rules and procedures that define how the tags and the readers should communicate and verify each other's identity and data, using cryptographic techniques or other methods.
  - Physical protection: This is the use of hardware or software mechanisms to protect the tags and the readers from physical tampering, damage, or theft, such as locks, seals, alarms, passwords, or firewalls.
  - Intrusion detection: This is the use of sensors, monitors, or analyzers to detect and report any abnormal or suspicious activities or events in the RFID system, such as unauthorized access, data modification, or signal interference.