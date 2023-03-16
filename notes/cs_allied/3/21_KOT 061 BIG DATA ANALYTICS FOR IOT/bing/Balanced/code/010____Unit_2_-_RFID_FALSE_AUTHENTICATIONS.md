## Unit 2 - RFID False Authentications

- RFID stands for Radio Frequency Identification, a technology that uses radio waves to identify and track objects, such as tags, cards, or chips, that are attached to or embedded in the objects.
- RFID systems consist of three main components: a reader, a tag, and a backend database. The reader emits radio signals to query the tag, which responds with its unique identifier or other data. The reader then communicates with the database to verify the tag's authenticity and perform other operations.
- RFID false authentication is a type of attack that aims to impersonate a legitimate tag or reader, or to modify the data exchanged between them, in order to gain unauthorized access, steal information, or cause damage to the system.
- There are different types of RFID false authentication attacks, such as:

  - Tag cloning: The attacker copies the identifier or data of a legitimate tag and creates a fake tag that can respond to the reader's queries with the same information.
  - Tag spoofing: The attacker uses a device that can generate radio signals to mimic the response of a legitimate tag, without actually having a physical tag.
  - Reader spoofing: The attacker uses a device that can generate radio signals to mimic the query of a legitimate reader, and tries to elicit responses from the tags in the vicinity.
  - Replay attack: The attacker captures the radio signals exchanged between a legitimate reader and tag, and replays them later to fool the system.
  - Relay attack: The attacker uses two devices, one near the legitimate reader and one near the legitimate tag, to relay the radio signals between them, creating a false impression of proximity.
  - Man-in-the-middle attack: The attacker intercepts and modifies the radio signals exchanged between a legitimate reader and tag, altering the data or commands sent or received.

- RFID false authentication attacks pose serious threats to the security and privacy of RFID systems and their users, as they can lead to:

  - Unauthorized access: The attacker can gain access to restricted areas, services, or resources by impersonating a legitimate tag or reader.
  - Information leakage: The attacker can steal sensitive or personal information from the tags or the database by impersonating a legitimate reader or tag.
  - Data corruption: The attacker can alter the data stored on the tags or the database by impersonating a legitimate reader or tag, or by modifying the radio signals in transit.
  - System malfunction: The attacker can disrupt the normal operation of the RFID system by impersonating a legitimate reader or tag, or by sending false or malicious commands or data.

- To prevent or mitigate RFID false authentication attacks, various countermeasures can be employed, such as:

  - Cryptography: The use of encryption, decryption, hashing, digital signatures, or other cryptographic techniques to protect the confidentiality, integrity, and authenticity of the data exchanged between the reader and the tag.
  - Authentication protocols: The use of challenge-response, mutual authentication, or other protocols to verify the identity and legitimacy of the reader and the tag before exchanging data or commands.
  - Physical protection: The use of shielding, tamper-resistance, or other physical methods to prevent unauthorized access, cloning, or modification of the tags or the reader.
  - Distance bounding: The use of timing, signal strength, or other methods to measure the distance between the reader and the tag, and to reject any responses that exceed a certain threshold, indicating a relay attack.
  - Anomaly detection: The use of statistical, behavioral, or other methods to monitor the RFID system and detect any abnormal or suspicious activities, such as repeated queries, unusual responses, or inconsistent data.