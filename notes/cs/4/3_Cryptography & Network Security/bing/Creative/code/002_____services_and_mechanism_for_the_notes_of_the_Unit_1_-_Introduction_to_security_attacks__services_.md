```
# Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

## Security Attacks, Services and Mechanisms

- Security attack: Any action that compromises the security of information owned by an organization.
- Security service: A processing or communication service that is provided by a system to give a specific kind of protection to system resources; security services implement security policies and are implemented by security mechanisms.
- Security mechanism: A mechanism that is designed to detect, prevent or recover from a security attack.

- X.800 divides security services into five categories and fourteen specific services:
  - Authentication: The assurance that the communicating entity is the one that it claims to be.
  - Access control: The prevention of unauthorized use of a resource.
  - Data confidentiality: The protection of data from unauthorized disclosure.
  - Data integrity: The assurance that data has not been altered or destroyed in an unauthorized manner.
  - Non-repudiation: The prevention of denial by one of the parties in a communication of having participated in all or part of the communication.
  - Availability: The assurance that the systems and data are accessible to authorized users when needed.
  - Audit: The ability to monitor and record security-related events and actions.
  - Security management: The administration and control of security policies and mechanisms.

- Security mechanisms can be classified into two types:
  - Specific security mechanisms: Mechanisms that are designed to provide a specific security service, such as encryption, digital signatures, access control lists, etc.
  - Pervasive security mechanisms: Mechanisms that are not specific to any particular service or protocol, but are applied generally across a system or network, such as security labels, event detection, security audit trails, security recovery, etc.

## Classical Encryption Techniques

- Encryption: The process of transforming plaintext (readable data) into ciphertext (unreadable data) using a secret key.
- Decryption: The reverse process of encryption, transforming ciphertext back into plaintext using the same or a different secret key.
- Cryptanalysis: The art of breaking encryption schemes, i.e., recovering the plaintext or the key from the ciphertext without knowing the key.
- Cryptography: The science of designing encryption schemes and cryptanalysis techniques.

- Classical encryption techniques are based on two basic building blocks:
  - Substitution cipher: A cipher that replaces each letter or symbol in the plaintext with another letter or symbol, depending on the key.
  - Transposition cipher: A cipher that rearranges the order of the letters or symbols in the plaintext, depending on the key.

- Examples of classical encryption techniques are:
  - Caesar cipher: A substitution cipher that shifts each letter in the plaintext by a fixed number of positions, modulo 26, according to the key.
  - Monoalphabetic cipher: A substitution cipher that uses a one-to-one mapping between the plaintext and ciphertext alphabets, according to the key.
  - Playfair cipher: A substitution cipher that encrypts pairs of letters using a 5x5 matrix of letters, according to the key.
  - Vigenere cipher: A substitution cipher that uses a series of different Caesar ciphers, based on the letters of a keyword, to encrypt the plaintext.
  - Hill cipher: A substitution cipher that encrypts blocks of letters using matrix multiplication, according to the key.
  - Rail fence cipher: A transposition cipher that writes the plaintext in a zigzag pattern on a number of rails, according to the key, and then reads the ciphertext along the rails.
  - Columnar transposition cipher: A transposition cipher that writes the plaintext in rows of a matrix, according to the key, and then reads the ciphertext by columns in a permuted order.
  - Route cipher: A transposition cipher that writes the plaintext in a rectangular array, according to the key, and then reads the ciphertext by following a route through the array.

## Steganography

- Steganography: The art of hiding information in other information, such as images, audio, video, etc., so that the existence of the hidden information is not noticeable.
- Steganalysis: The art of detecting

```
