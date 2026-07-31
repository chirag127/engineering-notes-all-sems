 Here are the notes for the topic "Hashes for the notes of the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT" in markdown format:

### Hashes

- Hashes are one-way functions that take an input and produce a fixed-size output (digest/fingerprint).
- It is infeasible to determine the input from the output.
- Used for data integrity (check if data has been changed).
- Common hash functions: MD5, SHA-1, SHA-256, SHA-512.
- Properties:
-- Deterministic: Same input always produces same output.
-- Quick computation of hash.
-- Collision resistance: Difficult to find two inputs that hash to same output.
-- Small changes in input lead to large changes in hash value.

Uses:

- File/data integrity checking: Calculate hash of file/data and store. Later recalculate hash and compare to stored hash to check if file/data was changed.
- Digital signatures: Data is signed using a private key and the hash of the data. The signature can be verified using the public key and recalculating the hash.
- Password storage: Store hash of password instead of plain password. Makes it more difficult to determine actual password if database is compromised.
- Commitment schemes: Hash lock can be revealed later to open the commitment and prove information without revealing the information itself at commitment time.

That's the notes for the given topic in the required formal format without any emojis or external links. Let me know if you would like me to modify or expand the notes in any way.