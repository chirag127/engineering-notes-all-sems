# Services and Mechanism for the Notes of the Unit 1

## Introduction to Security Attacks, Services and Mechanism

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

## Classical Encryption Techniques

- Encryption: The process of transforming plaintext (original message) into ciphertext (encrypted message) using a secret key and an encryption algorithm.
- Decryption: The reverse process of encryption, using the same or a different key and a decryption algorithm.
- Cryptanalysis: The study of techniques for attempting to defeat cryptographic techniques and, more generally, information security services.
- Cryptography: The study of mathematical techniques related to aspects of information security such as confidentiality, data integrity, entity authentication, and data origin authentication.
- Substitution cipher: A cipher that replaces each letter or symbol in the plaintext with another letter or symbol, depending on the key.
  - Examples: Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, one-time pad, etc.
- Transposition cipher: A cipher that rearranges the order of the letters or symbols in the plaintext, depending on the key.
  - Examples: Rail fence cipher, columnar transposition cipher, permutation cipher, etc.
- Steganography: The art and science of hiding information by embedding messages within other, seemingly harmless messages.
  - Examples: Invisible ink, microdots, digital watermarking, etc.

## Stream and Block Ciphers

- Stream cipher: A cipher that encrypts one bit or byte of plaintext at a time, using a keystream generator that produces a sequence of bits or bytes that are combined with the plaintext using a bitwise operation (usually XOR).
  - Examples: RC4, A5/1, A5/2, etc.
- Block cipher: A cipher that encrypts a fixed-length block of plaintext (usually 64 or 128 bits) into a block of ciphertext of the same length, using a secret key and a round function that is applied multiple times.
  - Examples: DES, AES, IDEA, etc.

## Modern Block Ciphers

- Block cipher principles: The basic design principles of block ciphers are:
  - Confusion: The relationship between the plaintext, ciphertext, and key should be complex and obscure, so that an attacker cannot find any statistical or mathematical patterns.
  - Diffusion: The influence of one plaintext bit or key bit on the ciphertext should be spread over as many ciphertext bits as possible, so that an attacker cannot change or guess a small portion of the plaintext or key.
  - Shannon's theory of confusion and diffusion: A theory proposed by Claude Shannon that states that the best way to achieve confusion and diffusion in a block cipher is to use a product cipher, which is a combination of two or more simple ciphers, such as substitution and transposition.
- Fiestel structure: A common structure for block ciphers that consists of a number of identical rounds, each with a subkey derived from the main key, and a final transformation. Each round has a function that takes the subkey and one half of the input block and produces an output that is XORed with the other half of the input block. The two halves are then swapped before the next round.
  - Examples: DES, IDEA, Blowfish, etc.
- Data Encryption Standard (DES): A widely used block cipher