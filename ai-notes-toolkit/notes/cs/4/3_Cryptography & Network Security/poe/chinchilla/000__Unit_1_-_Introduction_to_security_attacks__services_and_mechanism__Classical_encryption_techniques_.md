## Unit 1 - Introduction to Security Attacks, Services, and Mechanisms

### Security Attacks
- Security attack refers to any unauthorized attempt to access, modify, or destroy data or disrupt services.
- Types of security attacks include: 
  - Passive attacks: eavesdropping or monitoring without altering the data.
  - Active attacks: altering or destroying data, or disrupting services.
- Security attacks can occur due to vulnerabilities in the system or human error.

### Security Services
- Security services ensure the confidentiality, integrity, and availability of data and services.
- Confidentiality: data is protected from unauthorized access.
- Integrity: data is protected from unauthorized modification or deletion.
- Availability: data and services are available to authorized users when needed.
- Other security services include authentication, authorization, and non-repudiation.

### Security Mechanisms
- Security mechanisms are techniques used to provide security services.
- Examples of security mechanisms include:
  - Encryption: converting plaintext into ciphertext to protect confidentiality.
  - Hashing: converting data into a fixed-length hash to ensure integrity.
  - Digital signatures: using encryption and hashing to ensure non-repudiation.
  - Access control: granting or denying access to resources based on user identity and permissions.

## Classical Encryption Techniques

### Substitution Ciphers
- Substitution ciphers replace plaintext characters with other characters or symbols.
- Examples of substitution ciphers include:
  - Caesar cipher: shifts each letter by a fixed number of positions.
  - Atbash cipher: replaces each letter with its counterpart at the opposite end of the alphabet.
  - Polybius square cipher: replaces each letter with a pair of numbers indicating its position in a grid.

### Transposition Ciphers
- Transposition ciphers rearrange the order of characters in the plaintext.
- Examples of transposition ciphers include:
  - Rail fence cipher: writes the plaintext in a zigzag pattern across multiple rows, then reads it off in rows.
  - Columnar transposition cipher: writes the plaintext in columns, then reads it off in rows in a specific order.
  - Route cipher: writes the plaintext in a specific pattern, then reads it off in a specific order.

### Cryptanalysis
- Cryptanalysis refers to the process of breaking encryption techniques.
- Methods of cryptanalysis include:
  - Frequency analysis: analyzing the frequency of letters or symbols in the ciphertext to determine the substitution pattern.
  - Known plaintext attack: using known plaintext and ciphertext pairs to determine the encryption key.
  - Brute force attack: trying every possible key until the correct one is found.

### Steganography
- Steganography is the practice of hiding information within other information.
- Examples of steganography techniques include:
  - Concealing messages within images or audio files by manipulating the least significant bits.
  - Hiding messages within whitespace or other non-visible parts of a document.

## Stream and Block Ciphers

### Stream Ciphers
- Stream ciphers encrypt data one bit or byte at a time.
- Examples of stream ciphers include:
  - RC4: a widely used stream cipher that is now considered insecure.
  - Salsa20: a stream cipher designed to be secure and efficient.

### Block Ciphers
- Block ciphers encrypt data in fixed-size blocks.
- Examples of block ciphers include:
  - Data Encryption Standard (DES): a widely used block cipher that has since been replaced by more secure algorithms.
  - Advanced Encryption Standard (AES): a widely used block cipher that is considered secure.
- Principles of block ciphers include:
  - Confusion: making the relationship between the key and ciphertext as complex as possible.
  - Diffusion: spreading changes in the plaintext throughout the ciphertext.
  - Fiestel structure: a method of encrypting data that involves multiple rounds of substitution and transposition.

### Data Encryption Standard (DES)
- DES is a widely used block cipher that was developed in the 1970s.
- DES uses a 56-bit key to encrypt data in 64-bit blocks.
- The strength of DES is based on the difficulty of performing a brute force attack to determine the key.
- DES has been replaced by more secure algorithms, such as AES.

### Differential Cryptanalysis
- Differential cryptanalysis is a method of breaking block ciphers by analyzing the difference between pairs of plaintexts and their corresponding ciphertexts.
- Differential cryptanalysis was used to break DES in the late 1990s.

### Block Cipher Modes of Operation
- Block cipher modes of operation define how a block cipher is used to encrypt data that is larger than the block size.
- Examples of block cipher modes of operation include:
  - Electronic Codebook (ECB): encrypts each block of data separately.
  - Cipher Block Chaining (CBC): XORs each block of plaintext with the previous block of ciphertext before encryption.
  - Counter (CTR): generates a keystream from a counter value and XORs it with the plaintext.

### Triple DES
- Triple DES is a variant of DES that uses