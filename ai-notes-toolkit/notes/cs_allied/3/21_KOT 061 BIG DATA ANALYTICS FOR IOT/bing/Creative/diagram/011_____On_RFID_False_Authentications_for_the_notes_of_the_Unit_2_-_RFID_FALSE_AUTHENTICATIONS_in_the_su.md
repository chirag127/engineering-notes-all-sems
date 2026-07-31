### On RFID False Authentications

- RFID (Radio Frequency Identification) is a technology that uses radio waves to identify objects or people by attaching tags to them.
- RFID tags can store information such as a unique identifier, product name, price, etc. and can be read by RFID readers within a certain range.
- RFID authentication is the process of verifying the identity and validity of RFID tags and readers, and preventing unauthorized access or tampering.
- RFID authentication can be used for various purposes, such as product authentication, access control, anti-counterfeiting, etc.
- However, RFID authentication also faces some challenges and threats, such as false authentication, tag cloning, eavesdropping, replay attacks, etc.
- False authentication is a type of attack where a legitimate tag is wrongly rejected by a reader, or an illegitimate tag is wrongly accepted by a reader.
- False authentication can cause serious consequences, such as loss of revenue, damage to reputation, compromise of security, etc.
- False authentication can arise from various factors, such as protocol design flaws, tag memory limitations, reader errors, environmental noise, etc.
- For example, YA-TRAP is a reader/tag authentication protocol that uses a pseudorandom number generator (PRNG) to generate challenges and responses between the reader and the tag.
- However, YA-TRAP can suffer from false authentication when it is applied to C1G2 (class 1 generation 2) passive RFID tags, which have limited memory and computational power.
- C1G2 tags can only store 16 bits of PRNG state, which means that the PRNG can produce only 2^16 different values, and can repeat after 2^16 cycles.
- This makes the PRNG predictable and vulnerable to replay attacks, where an adversary can capture a valid challenge-response pair and reuse it later to fool the reader.
- Moreover, C1G2 tags can only perform bitwise operations, such as XOR, AND, OR, etc., which are not sufficient to implement a secure PRNG.
- Therefore, YA-TRAP can result in false authentication when the reader and the tag have different PRNG states, or when the adversary exploits the PRNG weakness.
- To prevent false authentication, RFID authentication protocols should consider the characteristics and limitations of the RFID tags and readers, and use cryptographic techniques, such as hash functions, encryption, digital signatures, etc., to ensure the randomness, freshness, and integrity of the challenges and responses.