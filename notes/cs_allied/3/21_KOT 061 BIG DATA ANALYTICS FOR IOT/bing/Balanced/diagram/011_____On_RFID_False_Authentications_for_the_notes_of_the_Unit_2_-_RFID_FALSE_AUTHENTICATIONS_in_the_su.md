### On RFID False Authentications

- RFID (Radio Frequency Identification) is a technology that uses radio waves to identify objects or people by attaching tags to them.
- RFID tags can store information such as a unique identifier, product name, price, etc. and can be read by RFID readers within a certain range.
- RFID authentication is the process of verifying the identity and validity of RFID tags and readers, and preventing unauthorized access or tampering.
- RFID authentication can be used for various purposes, such as product authentication, access control, anti-counterfeiting, etc.
- However, RFID authentication also faces some challenges and risks, such as false authentication, privacy leakage, replay attack, etc.
- False authentication is a situation where a legitimate tag is wrongly rejected by a reader, or an illegitimate tag is wrongly accepted by a reader.
- False authentication can cause serious problems, such as loss of revenue, damage to reputation, security breach, etc.
- False authentication can be caused by various factors, such as tag cloning, tag collision, tag malfunction, reader malfunction, protocol design flaw, etc.
- For example, YA-TRAP is a reader/tag authentication protocol that uses a hash function and a pseudorandom number generator to generate and verify authentication messages.
- However, YA-TRAP can suffer from false authentication when applied to C1G2 (class 1 generation 2) passive RFID tags, which have limited memory and computation capabilities.
- C1G2 tags can only store 16 bits of pseudorandom numbers, which can be easily guessed or exhausted by an attacker.
- Moreover, C1G2 tags can only perform bitwise operations, which can cause errors or inconsistencies in the hash function computation.
- Therefore, YA-TRAP can fail to authenticate legitimate tags or accept illegitimate tags when used with C1G2 tags.
- To prevent or reduce false authentication, some possible solutions are:

  - Using stronger or more secure authentication protocols that can resist tag cloning, tag collision, replay attack, etc.
  - Using more advanced or robust RFID tags that can support more memory, computation, and encryption functions.
  - Using multiple or hybrid authentication factors, such as password, biometrics, RFID, etc.
  - Using error detection or correction techniques, such as checksum, parity, CRC, etc.
  - Using feedback or confirmation mechanisms, such as LED, buzzer, display, etc.