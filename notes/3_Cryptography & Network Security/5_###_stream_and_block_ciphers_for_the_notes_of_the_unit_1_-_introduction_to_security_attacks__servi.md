### Stream and block ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism in the subject of Cryptography & Network Security
Stream Ciphers:
- Operate on plaintext one bit/byte at a time
- Keystream is generated independently for each bit/byte
- Keystream is XORed with plaintext to produce ciphertext
- Fast, but vulnerable to key reuse and keystream prediction

Block Ciphers:
- Operate on plaintext in fixed-size blocks (64 or 128 bits)
- Key is used to encrypt each block independently
- More secure than stream ciphers, but slower
- Can be used in various modes of operation (e.g. ECB, CBC, CFB, OFB) to overcome limitations.
