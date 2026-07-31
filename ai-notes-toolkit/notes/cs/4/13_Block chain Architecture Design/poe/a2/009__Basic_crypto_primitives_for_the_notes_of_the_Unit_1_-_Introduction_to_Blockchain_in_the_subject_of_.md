 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design:

1. Hash functions:
- Input of arbitrary size and output a fixed-size hash value.
- Deterministic - Same input yields same output always.
- Quick to compute but infeasible to reverse.
- Collision resistant - Hard to find two inputs that hash to same output.
- Used for data integrity checks, commitment schemes, etc.

2. Digital signatures:
- Used to authenticate the sender of a message and verify integrity of the message.
- Uses public key cryptography - a private key to sign and a public key to verify.
- Unforgeable - Only the legitimate sender can produce a valid signature.
- Non-repudiation - Sender cannot deny sending the message.

3. Public key cryptography:
- Uses a key pair - a public key and a private key.
- The public key can be shared with everyone while the private key is only known to the owner.
- Messages encrypted with the public key can only be decrypted with the private key and vice-versa.
- Used for encryption, digital signatures, key exchange, etc.

4.Trapdoor functions:
- Easy to compute in one direction but infeasible to compute in the reverse direction.
- Public key crypto uses these functions - easy to compute public key from private key but infeasible to compute private key from public key.
- Used to build cryptographic primitives like digital signatures and encryption schemes.

The content is written in points in a formal tone without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.