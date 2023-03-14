 Here is the markdown content for the given topic:

### Services and mechanism for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

Security services provided by cryptography are:

- Confidentiality: Ensuring that information is accessible only to authorized individuals. Eg. Encryption techniques like substitution ciphers and transposition ciphers provide confidentiality.
- Integrity: Ensuring that information has not been altered in transit. Eg. Hash functions and MAC codes are used to provide integrity.
- Authentication: Ensuring that the identity of a user/device is correct. Eg. Digital signatures and certificates are used for authentication.
- Non-repudiation: Ensuring that the sender of a message cannot deny sending the message. Eg. Digital signatures provide non-repudiation.

Mechanisms provided by cryptography are:

- Encryption: Conversion of plaintext into ciphertext using a key. Eg. Substitution ciphers, transposition ciphers, stream ciphers, block ciphers.
- Cryptanalysis: Study of methods to break ciphers without knowing the key. Eg. Frequency analysis, brute force attack.
- Steganography: Hiding the existence of a secret message. Eg. Least significant bit insertion, image cryptography.

Stream ciphers and block ciphers are two types of symmetric key ciphers. Block ciphers encrypt one block of bits at a time and the modern block ciphers have the principles of confusion and diffusion given by Shannon for stronger encryption.

Principles of confusion and diffusion in block ciphers:

- Confusion: The relationship between the key and the ciphertext should be complex.
- Diffusion: A small change in the plaintext should result in a large change in the ciphertext.

Fiestel structure is a design used in many block ciphers like DES. It divides the block into two halves and encrypts each half alternatively.

DES is a block cipher with a 64-bit block and 56-bit key. It has been cracked due to its small key size. Triple DES extends DES to use three independent keys to strengthen it against attacks.

Modes of operation of block ciphers:

- ECB: Electronic Codebook mode. Each block is encrypted independently. Vulnerable to chosen plaintext attacks.
- CBC: Cipher Block Chaining mode. Each block is XORed with the previous ciphertext block before encryption. Prevents chosen plaintext attacks but vulnerable to ciphertext manipulation attacks.
- CFB: Cipher Feedback mode. A shift register is used whose contents are encrypted and XORed with the plaintext to generate the