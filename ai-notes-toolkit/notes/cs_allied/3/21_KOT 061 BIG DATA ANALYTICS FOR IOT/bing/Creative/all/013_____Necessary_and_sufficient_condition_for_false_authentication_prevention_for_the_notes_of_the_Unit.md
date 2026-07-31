# Necessary and sufficient condition for false authentication prevention for the notes of the Unit 2 - RFID FALSE AUTHENTICATIONS in the subject of KOT 061 BIG DATA ANALYTICS FOR IOT KCS

- RFID false authentication is a situation where a legitimate tag is wrongly rejected by a reader, or an illegitimate tag is wrongly accepted by a reader .
- RFID false authentication can arise from various factors, such as interference in the electromagnetic field, duplication of tag IDs, invalid or counterfeit tags and readers, or protocol design flaws  .
- To prevent RFID false authentication, the following conditions are necessary and sufficient:
  - The reader and the tag should share a secret key or a challenge-response mechanism to verify each other's identity and integrity.
  - The reader and the tag should use a secure channel or encryption to protect the communication from eavesdropping or tampering.
  - The reader and the tag should use a semaphore or a lock to prevent concurrent access or collision from multiple tags or readers.
  - The reader and the tag should use a nonce or a counter to prevent replay attacks or tag cloning.
  - The reader and the tag should use a hash function or a message authentication code to ensure the freshness and authenticity of the messages.