## Unit 2 - RFID False Authentications

- RFID stands for Radio Frequency Identification. It is a technology that uses radio waves to identify objects or people by attaching a small chip or tag to them.
- RFID tags can store information such as a unique identifier, product name, price, or personal data. They can be read by a device called a reader, which sends out radio signals and receives the tag's response.
- RFID systems are widely used in various applications, such as inventory management, access control, payment systems, identification cards, passports, and more.
- However, RFID systems are also vulnerable to various attacks, such as eavesdropping, cloning, spoofing, replaying, and jamming. These attacks can compromise the security and privacy of the RFID system and its users.
- One of the most common attacks on RFID systems is false authentication, which occurs when an unauthorized tag or reader pretends to be a legitimate one and gains access to the system or the data.
- False authentication can be performed by different methods, such as:

  - Cloning: This is when an attacker copies the data from a legitimate tag and creates a duplicate tag with the same identifier. The cloned tag can then be used to access the system or the data as if it were the original tag.
  - Spoofing: This is when an attacker modifies the data or the identifier of a tag to make it appear as a different tag. The spoofed tag can then be used to access the system or the data as if it were the intended tag.
  - Replaying: This is when an attacker captures the communication between a legitimate tag and a reader and then replays it later to the same or a different reader. The replayed communication can then be used to access the system or the data as if it were a fresh communication.
  - Jamming: This is when an attacker interferes with the radio signals between a tag and a reader by sending out noise or fake signals. The jamming attack can prevent the tag and the reader from communicating or cause errors in the communication.

- False authentication can have serious consequences for the RFID system and its users, such as:

  - Data theft: An attacker can steal the data stored on the tag or the reader, such as personal information, credit card numbers, passwords, or product details. The stolen data can then be used for identity theft, fraud, or other malicious purposes.
  - Data corruption: An attacker can alter the data stored on the tag or the reader, such as changing the price, quantity, or status of a product. The corrupted data can then cause errors, losses, or damages to the system or the users.
  - Data denial: An attacker can deny the access to the data stored on the tag or the reader, such as blocking the payment, authentication, or verification of a user or a product. The denied data can then cause inconvenience, delays, or failures to the system or the users.

- To prevent or detect false authentication, RFID systems can use various countermeasures, such as:

  - Encryption: This is when the data or the identifier of the tag or the reader is encoded using a secret key or a mathematical function. The encrypted data or identifier can only be decoded by the authorized parties who have the same key or function. Encryption can protect the data or the identifier from being read, copied, modified, or replayed by an attacker.
  - Authentication: This is when the tag or the reader verifies the identity or the validity of the other party before exchanging data. The authentication can be done by using a password, a challenge-response protocol, a digital signature, or a biometric feature. Authentication can prevent the tag or the reader from communicating with an unauthorized or spoofed party.
  - Anti-collision: This is when the tag or the reader avoids or resolves the interference or the collision of the radio signals from multiple tags or readers. The anti-collision can be done by using a random or a deterministic algorithm, a time division or a frequency division scheme, or a singulation or a grouping protocol. Anti-collision can prevent the tag or the reader from being jammed or confused by an attacker.