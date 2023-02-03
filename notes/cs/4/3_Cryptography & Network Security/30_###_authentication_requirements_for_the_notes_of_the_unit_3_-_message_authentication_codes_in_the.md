### Authentication requirements for the notes of the Unit 3 - Message Authentication Codes in the subject of Cryptography & Network Security
Message authentication codes (MACs) provide data integrity and authenticity for messages. Requirements for a secure MAC include:

1. Uniqueness: The MAC algorithm should produce unique output for every unique input.

2. Collision resistance: It should be computationally infeasible to find two inputs that produce the same MAC.

3. Key secrecy: The secret key used to generate the MAC must be kept secret.

4. Tamper detection: Any changes to the message should result in a different MAC, allowing detection of tampering.

5. Length extension attack resistance: The MAC should not allow attackers to extend the message without knowing the secret key.

6. Non-repudiation: The MAC should provide evidence that the sender was the one who sent the message.
