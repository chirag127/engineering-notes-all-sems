# YA TRAP

- YA TRAP is a reader/tag authentication protocol for RFID systems   .
- It aims to effectively authenticate tags and readers using hash functions and pseudorandom number generators   .
- It consists of four steps as shown in the following figure :

![YA TRAP protocol](https://link.springer.com/content/images/m4/978-3-319-05029-4_4/978-3-319-05029-4_4-fig1.jpg)

- However, YA TRAP may suffer from false authentications, which means that a legitimate tag could be wrongly rejected by a reader   .
- False authentications may arise from the following reasons :
  - The tag may not be able to update its secret key due to power loss or communication failure.
  - The reader may not be able to synchronize its secret key with the tag due to network delay or database error.
  - The tag may not be able to generate a valid response due to hash collision or random number collision.
- False authentications may lead to serious consequences, such as loss of revenue, privacy breach, or denial of service .
- Therefore, YA TRAP needs to be improved or replaced by more robust and reliable protocols for RFID authentication .