## Unit 2 - RFID False Authentications

- RFID stands for Radio Frequency Identification, a technology that uses radio waves to identify objects or people by attaching tags or chips to them.
- RFID tags can store information such as serial numbers, product codes, personal data, etc. and transmit them to RFID readers when they are in range.
- RFID systems are widely used in various applications such as inventory management, access control, payment systems, identification cards, passports, etc.
- However, RFID systems are also vulnerable to false authentication attacks, where an attacker can impersonate a legitimate tag or reader and gain unauthorized access to information or resources.
- There are two main types of false authentication attacks: tag cloning and reader spoofing.

### Tag Cloning
- Tag cloning is an attack where an attacker copies the information from a legitimate tag and creates a duplicate tag that can be used to fool a reader.
- Tag cloning can be done by using a device called a skimmer, which can read the information from a tag when it is in close proximity, or by eavesdropping on the communication between a tag and a reader.
- Tag cloning can be used to bypass security checks, steal products, access restricted areas, etc.
- To prevent tag cloning, some countermeasures are:
  - Using cryptographic protocols that require tags and readers to authenticate each other using secret keys or digital signatures.
  - Using physical protection mechanisms such as tamper-proof tags, shielding, or locking mechanisms that prevent unauthorized access to the tags.
  - Using random or dynamic identifiers that change every time a tag communicates with a reader, making it harder to copy or replay them.

### Reader Spoofing
- Reader spoofing is an attack where an attacker pretends to be a legitimate reader and sends malicious commands or queries to a tag, or intercepts the responses from a tag.
- Reader spoofing can be done by using a device called a spoofer, which can generate and transmit radio signals that mimic a reader, or by relaying the communication between a tag and a reader.
- Reader spoofing can be used to obtain sensitive information from a tag, modify or erase the data on a tag, deactivate or destroy a tag, etc.
- To prevent reader spoofing, some countermeasures are:
  - Using cryptographic protocols that require tags and readers to authenticate each other using secret keys or digital signatures.
  - Using mutual authentication mechanisms that require both tags and readers to prove their identities before exchanging information.
  - Using distance bounding protocols that measure the time or signal strength of the communication and detect any anomalies that indicate a relay attack.