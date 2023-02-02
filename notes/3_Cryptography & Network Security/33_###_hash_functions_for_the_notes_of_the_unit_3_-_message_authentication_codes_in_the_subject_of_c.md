### hash functions for the notes of the Unit 3 - Message Authentication Codes in the subject of Cryptography & Network Security
A hash function is a mathematical function that takes an input (or "message") and returns a fixed-size string of bytes. The output is called the "hash" or "digest". The same input will always produce the same hash, but even a small change to the input will produce a completely different hash. Hash functions are used in cryptography for message authentication and digital signatures. 

Properties of a good hash function:
1. Deterministic: Same input always produces the same hash.
2. Quick computation of the hash value for any given message.
3. Infeasible to generate the same hash value for two different messages.
4. Infeasible to regenerate the original message from the hash value.
5. The hash value should change significantly for even small changes in the input message.

Hash functions are used in Message Authentication Codes (MACs) to ensure that a message has not been altered in transit. A MAC is a short piece of information used to authenticate a message and to provide integrity and authenticity assurances on the message. The MAC value is computed using a secret key shared between the sender and receiver.

Examples of hash functions include SHA-256, SHA-3, and MD5.
