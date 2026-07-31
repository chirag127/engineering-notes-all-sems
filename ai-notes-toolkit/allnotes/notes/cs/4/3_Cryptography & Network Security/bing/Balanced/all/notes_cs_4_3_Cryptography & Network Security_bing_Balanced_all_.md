

# Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

- Security attacks are any actions that compromise the confidentiality, integrity, or availability of information or resources in a system.
- Security services are the measures that provide protection against security attacks, such as authentication, encryption, digital signatures, access control, etc.
- Security mechanisms are the methods or tools that implement security services, such as cryptographic algorithms, protocols, firewalls, etc.
- Classical encryption techniques are the methods of transforming plaintext into ciphertext using simple mathematical operations, such as substitution and transposition.
- Substitution ciphers are the methods of replacing each letter or symbol in the plaintext with another letter or symbol, according to a fixed rule or key. For example, Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, etc.
- Transposition ciphers are the methods of rearranging the order of the letters or symbols in the plaintext, according to a fixed rule or key. For example, rail fence cipher, columnar transposition cipher, etc.
- Cryptanalysis is the science of breaking ciphertext without knowing the key or the encryption algorithm, by exploiting the weaknesses or patterns in the encryption technique or the ciphertext.
- Steganography is the art of hiding information within other information, such as concealing a secret message within an image, audio, or video file, without altering the appearance or quality of the cover medium.
- Stream ciphers are the methods of encrypting plaintext by generating a keystream of random or pseudorandom bits, and combining it with the plaintext using bitwise operations, such as XOR. For example, RC4, A5/1, etc.
- Block ciphers are the methods of encrypting plaintext by dividing it into fixed-length blocks, and applying a symmetric key and a mathematical function to each block, producing ciphertext blocks of the same length. For example, DES, AES, etc.
- Block cipher principles are the basic concepts or properties that a block cipher should have, such as completeness, avalanche effect, confusion, diffusion, etc.
- Shannon’s theory of confusion and diffusion is a framework for designing secure block ciphers, proposed by Claude Shannon. Confusion means that the relationship between the key and the ciphertext should be complex and obscure, making it hard to derive the key from the ciphertext. Diffusion means that the influence of each plaintext bit or key bit should be spread over many ciphertext bits, making it hard to find patterns or correlations in the ciphertext.
- Fiestel structure is a common design for block ciphers, consisting of multiple rounds of encryption, each involving a subkey derived from the main key, a substitution function, and a permutation function. For example, DES, Blowfish, etc.
- Data Encryption Standard (DES) is a widely used block cipher, developed by IBM and adopted by the US government in 1977. It has a block size of 64 bits and a key size of 56 bits, and uses 16 rounds of encryption with a fiestel structure.
- Strength of DES is measured by its resistance to various types of attacks, such as brute force, differential cryptanalysis, linear cryptanalysis, etc. DES is considered insecure by modern standards, as its key size is too small and can be broken by brute force in a matter of hours or days by using specialized hardware or parallel computing.
- Idea of differential cryptanalysis is a technique for breaking block ciphers, based on analyzing the differences between pairs of plaintexts and ciphertexts, and finding statistical patterns that reveal information about the key or the encryption function. It was first introduced by Biham and Shamir in 1990, and was shown to be effective against DES and other block ciphers.
- Block cipher modes of operation are the methods of using a block cipher to encrypt or decrypt data that is larger or smaller than the block size, or to provide additional security features, such as authentication or integrity. For example, ECB, CBC, CFB, OFB, CTR, GCM, etc.
- Triple DES is a variant of DES that applies three rounds of DES encryption with different keys, to increase the security and the effective key size. It has a block size of 64 bits and a key size of 168 bits (or 112 bits if two of the keys are the same). It is more secure than DES, but also slower and less efficient.



# Introduction to security attacks

- Security attacks are attempts to compromise the confidentiality, integrity, availability, authenticity, or non-repudiation of information or resources.
- Security attacks can be classified into two categories: passive attacks and active attacks.
- Passive attacks are those that do not alter the data or resources, but only observe or analyze them. Examples of passive attacks are eavesdropping, traffic analysis, or ciphertext-only attack.
- Active attacks are those that modify or disrupt the data or resources, or create false data or resources. Examples of active attacks are modification, deletion, insertion, replay, masquerade, or denial-of-service attack.
- Security attacks can also be classified based on the source of the attack: insider attacks or outsider attacks.
- Insider attacks are those that are launched by authorized users or entities within the system or network. Examples of insider attacks are disgruntled employees, malicious insiders, or compromised accounts.
- Outsider attacks are those that are launched by unauthorized users or entities outside the system or network. Examples of outsider attacks are hackers, crackers, or cybercriminals.



# Services and Mechanism for the Notes of the Unit 1 - Introduction to Security Attacks, Services and Mechanism, Classical Encryption TechniquesSubstitution Ciphers and Transposition Ciphers, Cryptanalysis, Steganography, Stream and Block Ciphers. Modern Block Ciphers: Block Ciphers Principles, Shannon’s Theory of Confusion and Diffusion, Fiestal Structure, Data Encryption Standard(DES), Strength of DES, Idea of Differential Cryptanalysis, Block Cipher Modes of Operations, Triple DES in the Subject of Cryptography & Network Security

## Security Attacks, Services and Mechanism

- Security attacks are any actions that compromise the security of information or systems. They can be classified into two categories: passive attacks and active attacks.
- Passive attacks are those that do not alter the data or system, but only observe or analyze it. Examples are eavesdropping, traffic analysis, or ciphertext-only attack.
- Active attacks are those that modify the data or system, or prevent its normal operation. Examples are masquerade, replay, modification, or denial of service attack.
- Security services are the countermeasures that provide protection against security attacks. They can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation.
- Confidentiality is the service that ensures that the data or system is accessible only to authorized parties. Examples are encryption, access control, or physical security.
- Integrity is the service that ensures that the data or system is not modified or corrupted by unauthorized parties. Examples are checksum, digital signature, or hash function.
- Availability is the service that ensures that the data or system is accessible and usable by authorized parties when needed. Examples are redundancy, backup, or fault tolerance.
- Authentication is the service that ensures that the identity of a party or the origin of a message is verified. Examples are password, certificate, or challenge-response.
- Non-repudiation is the service that ensures that a party cannot deny having sent or received a message. Examples are digital signature, timestamp, or audit trail.
- Security mechanisms are the methods or tools that implement security services. They can be classified into two categories: preventive mechanisms and detective mechanisms.
- Preventive mechanisms are those that prevent or deter security attacks from happening. Examples are encryption, access control, or firewall.
- Detective mechanisms are those that detect or identify security attacks that have happened or are happening. Examples are intrusion detection, audit, or alarm.

## Classical Encryption Techniques

- Encryption is the process of transforming plaintext (the original message) into ciphertext (the encrypted message) using a secret key. Decryption is the reverse process of recovering plaintext from ciphertext using the same or a different key.
- Encryption techniques can be classified into two categories: substitution ciphers and transposition ciphers.
- Substitution ciphers are those that replace each symbol or group of symbols in the plaintext with another symbol or group of symbols in the ciphertext. Examples are Caesar cipher, monoalphabetic cipher, or polyalphabetic cipher.
- Transposition ciphers are those that rearrange the order of symbols or groups of symbols in the plaintext to form the ciphertext. Examples are rail fence cipher, columnar transposition cipher, or permutation cipher.
- Cryptanalysis is the process of breaking encryption techniques by finding the key or the plaintext without knowing the key. Cryptanalysis can be based on different types of information available to the attacker, such as ciphertext-only, known-plaintext, chosen-plaintext, or chosen-ciphertext.
- Steganography is the process of hiding a message within another message or medium, such as an image, audio, or video. Steganography is different from encryption in that it does not alter the message, but only conceals its existence. Examples are least significant bit (LSB) steganography, frequency domain steganography, or spread spectrum steganography.

## Stream and Block Ciphers

- Stream ciphers are encryption techniques that encrypt each symbol or bit of the plaintext individually using a keystream (a sequence of random or pseudorandom symbols or bits). Examples are one-time pad, RC4, or A5/1.
- Block ciphers are encryption techniques that encrypt each block (a fixed-size group of symbols or bits) of the plaintext using a key. Examples are DES, AES, or Blowfish.
- Stream ciphers are faster and simpler than block ciphers, but they are more vulnerable to attacks such as ciphertext-only or known-plaintext. Block ciphers are more secure and flexible than stream ciphers, but they are slower and more complex.

## Modern Block Ciphers

- Block ciphers are encryption techniques that encrypt each block (a fixed-size group of symbols or bits) of the plaintext using a key. Modern block ciphers are based on two principles: confusion and diffusion.
- Conf



# Classical encryption techniques

## Substitution ciphers

- A substitution cipher is a method of encryption that replaces each plaintext symbol with a different ciphertext symbol.
- The key of a substitution cipher is the mapping of plaintext symbols to ciphertext symbols.
- There are two types of substitution ciphers: monoalphabetic and polyalphabetic.
- A monoalphabetic substitution cipher uses a fixed mapping for the entire message, such as the Caesar cipher or the Atbash cipher.
- A polyalphabetic substitution cipher uses a variable mapping that changes according to a predefined rule, such as the Vigenère cipher or the Enigma machine.
- Substitution ciphers are vulnerable to frequency analysis, which exploits the statistical patterns of the plaintext language.

## Transposition ciphers

- A transposition cipher is a method of encryption that rearranges the order of the plaintext symbols without changing their identity.
- The key of a transposition cipher is the rule of permutation that determines how the symbols are shuffled.
- There are two types of transposition ciphers: simple and complex.
- A simple transposition cipher applies the same permutation to each block of fixed length, such as the rail fence cipher or the columnar transposition cipher.
- A complex transposition cipher applies different permutations to different blocks or uses multiple stages of permutation, such as the double transposition cipher or the ADFGVX cipher.
- Transposition ciphers are vulnerable to anagramming, which exploits the fact that the ciphertext symbols are the same as the plaintext symbols.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of cryptanalysis for the subject of Cryptography & Network Security. Here is the content I have generated for you in markdown format:

# Cryptanalysis

Cryptanalysis is the art and science of breaking the encryption of a message or a cipher. Cryptanalysis aims to find the secret key, the plaintext, or the encryption algorithm used by the sender.

## Security Attacks, Services and Mechanisms

Security attacks are any actions that compromise the security of information. Security attacks can be classified into two categories: passive attacks and active attacks.

- Passive attacks are those that only observe or analyze the data without modifying it. Examples of passive attacks are eavesdropping, traffic analysis, and ciphertext-only attack.
- Active attacks are those that alter or disrupt the data or the system. Examples of active attacks are replay, modification, insertion, deletion, and man-in-the-middle attack.

Security services are the countermeasures that protect the information and the system from security attacks. Security services can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation.

- Confidentiality is the service that ensures that the information is only accessible to the authorized parties. Examples of confidentiality mechanisms are encryption, access control, and physical protection.
- Integrity is the service that ensures that the information is not modified or corrupted by unauthorized parties. Examples of integrity mechanisms are checksum, hash, digital signature, and message authentication code.
- Availability is the service that ensures that the information and the system are accessible and functional to the authorized parties. Examples of availability mechanisms are backup, redundancy, fault tolerance, and denial-of-service prevention.
- Authentication is the service that ensures that the identity of the parties involved in the communication is verified and confirmed. Examples of authentication mechanisms are password, biometric, token, certificate, and challenge-response.
- Non-repudiation is the service that ensures that the parties involved in the communication cannot deny their actions or involvement. Examples of non-repudiation mechanisms are digital signature, timestamp, and audit trail.

## Classical Encryption Techniques

Classical encryption techniques are the encryption methods that were used before the advent of modern cryptography. Classical encryption techniques can be divided into two types: substitution ciphers and transposition ciphers.

- Substitution ciphers are those that replace each letter or symbol of the plaintext with another letter or symbol according to a fixed rule or a key. Examples of substitution ciphers are Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, and one-time pad.
- Transposition ciphers are those that rearrange the order of the letters or symbols of the plaintext according to a fixed rule or a key. Examples of transposition ciphers are rail fence cipher, columnar cipher, and permutation cipher.

## Cryptanalysis of Classical Encryption Techniques

Cryptanalysis of classical encryption techniques is the process of finding the key or the plaintext of a classical cipher without knowing the encryption algorithm or having access to the sender or the receiver. Cryptanalysis of classical encryption techniques can be performed by using various methods, such as:

- Frequency analysis: This method exploits the fact that some letters or symbols are more frequent than others in a given language or a message. By comparing the frequency distribution of the ciphertext with the expected frequency distribution of the plaintext, the cryptanalyst can guess the key or the plaintext of a substitution cipher.
- Pattern recognition: This method exploits the fact that some words or phrases are more common than others in a given language or a message. By looking for patterns or repetitions in the ciphertext, the cryptanalyst can guess the key or the plaintext of a transposition cipher or a polyalphabetic cipher.
- Brute force: This method involves trying all possible keys or plaintexts until the correct one is found. This method is guaranteed to succeed, but it is very time-consuming and impractical for large keys or plaintexts.

## Steganography

Steganography is the art and science of hiding a message or a cipher within another message or a medium, such as an image, a sound, or a text. Steganography aims to conceal the existence of the secret message or the cipher, rather than encrypting it. Steganography can be combined with encryption to provide an additional layer of security. Examples of steganography techniques are:

- Least significant bit (LSB): This technique modifies the least significant bit of each pixel or sample of an image or a sound to store the secret message or the cipher.
- Invisible ink: This technique uses a special ink that is invisible to the naked eye, but can be revealed by applying heat, light, or a chemical agent.
- Null cipher: This technique uses a cover text that contains the secret message or the cipher in the form of the first or the last



# Steganography

- Steganography is the art or practice of concealing a message, image, or file within another message, image, or file  .
- Steganography can be used along with cryptography as an extra-secure method to protect data.
- Steganography can be applied to various types of media, such as images, video, audio, text, or network packets  .
- Steganography works by hiding the secret information in a way that is not evident to human inspection or analysis.
- Steganography can be classified into two types: technical and linguistic.
  - Technical steganography uses physical or digital methods to hide the information, such as embedding data in images, audio, or video files, or using invisible ink, microdots, or watermarking .
  - Linguistic steganography uses language or text to hide the information, such as using code words, acronyms, anagrams, or secret languages, or modifying the structure or appearance of the text .
- Steganography has been used for various purposes, such as espionage, communication, political activism, or cyber attacks .
- Steganography has some advantages and disadvantages over cryptography .
  - Advantages:
    - Steganography can provide an additional layer of security to encrypted data by hiding its existence .
    - Steganography can avoid arousing suspicion or attracting attention from unwanted parties .
    - Steganography can be more user-friendly and less complex than cryptography .
  - Disadvantages:
    - Steganography can be vulnerable to steganalysis, which is the process of detecting and extracting hidden information from steganographic media .
    - Steganography can be limited by the capacity and quality of the carrier media, which may affect the amount and integrity of the hidden information .
    - Steganography can be unethical or illegal if used for malicious or criminal purposes .



Hello, I am Sydney, your AI assistant. I can help you with your study material on cryptography and network security. Here are some notes on stream and block ciphers:

# Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that operate on different units of plaintext and ciphertext.
- Stream ciphers encrypt and decrypt one bit or byte of plaintext at a time, using a keystream that is derived from a secret key and an initialization vector (IV).
- Block ciphers encrypt and decrypt fixed-length blocks of plaintext, usually 64 or 128 bits, using a secret key and a mode of operation that specifies how to handle multiple blocks.
- Stream ciphers are faster and more suitable for continuous data streams, such as voice or video, while block ciphers are more secure and more suitable for discrete data, such as files or messages.
- Stream ciphers can be classified into synchronous and self-synchronizing stream ciphers. Synchronous stream ciphers use the same keystream for encryption and decryption, and require the sender and receiver to be synchronized. Self-synchronizing stream ciphers use the previous ciphertext bits to generate the keystream, and can recover from errors or losses in transmission.
- Block ciphers can be classified into substitution-permutation networks (SPNs) and Feistel networks. SPNs consist of multiple rounds of substitution and permutation operations that provide confusion and diffusion, respectively. Feistel networks consist of multiple rounds of splitting, mixing, and swapping operations that provide diffusion and confusion, respectively.
- Examples of stream ciphers are RC4, A5/1, A5/2, and E0. Examples of block ciphers are DES, 3DES, AES, and IDEA.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of Modern Block Ciphers:

# Modern Block Ciphers

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- Block ciphers are widely used to provide confidentiality, integrity, and authentication in various cryptographic protocols and applications, such as encryption modes, hash functions, message authentication codes, and digital signatures.
- Block ciphers can be classified into two types: substitution-permutation networks (SPNs) and Feistel networks. SPNs consist of alternating layers of substitution and permutation operations, while Feistel networks consist of repeated rounds of splitting, mixing, and swapping operations.
- Block ciphers can also be characterized by their key size, block size, number of rounds, and design principles, such as Shannon's theory of confusion and diffusion, which aim to increase the complexity and security of the cipher.

## Shannon's Theory of Confusion and Diffusion

- Shannon's theory of confusion and diffusion is a framework for designing secure block ciphers, proposed by Claude Shannon in his seminal paper "Communication Theory of Secrecy Systems" in 1949.
- Confusion means that the relationship between the plaintext and the ciphertext should be as complex and obscure as possible, so that an attacker cannot easily deduce the key or the plaintext from the ciphertext. This can be achieved by using nonlinear and variable substitution operations, such as S-boxes, that depend on the key and the input.
- Diffusion means that the influence of each plaintext bit should be spread over as many ciphertext bits as possible, so that changing one bit in the plaintext results in changing many bits in the ciphertext. This can be achieved by using linear and fixed permutation operations, such as P-boxes, that shuffle and rearrange the bits.
- Confusion and diffusion are complementary and mutually reinforcing concepts, and they should be applied alternately and repeatedly in a block cipher to achieve a high level of security.

## Fiestal Structure

- A Feistel network is a type of block cipher structure that was invented by Horst Feistel at IBM in the 1970s. It is named after him and his colleagues, who developed the Data Encryption Standard (DES), the first widely adopted block cipher based on this structure.
- A Feistel network consists of a number of rounds, each of which performs the following steps:
  - Split the input block into two equal halves, L and R.
  - Apply a round function F to the right half R and the round key K, and obtain the output F(R, K).
  - XOR the output F(R, K) with the left half L, and obtain the new right half R'.
  - Swap the halves, so that the new left half is R and the new right half is L'.
  - Repeat the above steps for the next round, using a different round key.
- The final round does not perform the swap, so that the output block is (L', R').
- The decryption process is the same as the encryption process, except that the round keys are used in reverse order and the swap is performed before the XOR.

## Data Encryption Standard (DES)

- The Data Encryption Standard (DES) is a block cipher that was developed by IBM and adopted by the US National Bureau of Standards (NBS) as a federal standard in 1977. It was widely used for encryption and decryption of sensitive data until the late 1990s, when it was replaced by more secure and efficient ciphers, such as the Advanced Encryption Standard (AES).
- DES operates on 64-bit blocks and uses a 56-bit key (plus 8 parity bits). It consists of 16 rounds of Feistel network, with a fixed initial and final permutation, and a complex round function that involves expansion, substitution, permutation, and XOR operations. The round keys are derived from the main key using a key schedule algorithm that involves shifts and permutations.
- DES has a simple and elegant structure, but it also has several weaknesses, such as low key size, weak keys, complementation property, and susceptibility to differential and linear cryptanalysis. These weaknesses have been exploited by various attacks, such as brute-force, rainbow tables, and chosen-plaintext, that can break DES in a matter of hours or minutes using modern hardware and software.

## Differential Cryptanalysis

- Differential cryptanalysis is a technique for analyzing and breaking block ciphers, proposed by Eli Biham and Adi Shamir in 1990. It is based on the idea of studying how differences in plaintext pairs propagate through the rounds of the cipher and produce differences in



Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of block ciphers principles:

# Block ciphers principles

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- A block cipher can be seen as a function that maps a plaintext block to a ciphertext block, using a secret key as a parameter. The function must be invertible, meaning that there is a way to recover the plaintext from the ciphertext using the same key.
- A block cipher can be used to encrypt a message by dividing it into blocks of equal size and applying the encryption function to each block. Similarly, a block cipher can be used to decrypt a message by dividing it into blocks and applying the inverse function to each block.
- A block cipher can also be used to construct other cryptographic primitives, such as stream ciphers, hash functions, message authentication codes, and digital signatures, by using different modes of operation or techniques.
- The security of a block cipher depends on the strength of the key, the size of the block, the design of the encryption function, and the resistance to various attacks, such as brute-force, differential, linear, or algebraic attacks.

## Shannon's theory of confusion and diffusion

- Shannon's theory of confusion and diffusion is a framework for analyzing the security of a block cipher, based on the concepts of confusion and diffusion.
- Confusion means that the relationship between the plaintext, the ciphertext, and the key is complex and obscure, making it hard to infer any information about them from each other. Confusion can be achieved by using nonlinear and irregular functions, such as substitution or S-boxes, in the encryption function.
- Diffusion means that the influence of each plaintext bit or key bit is spread over many ciphertext bits, making it hard to isolate and manipulate any part of the ciphertext. Diffusion can be achieved by using permutation or P-boxes, or by mixing the plaintext blocks or key blocks, in the encryption function.
- A good block cipher should have a high degree of both confusion and diffusion, so that any change in the plaintext or the key results in a significant and unpredictable change in the ciphertext, and vice versa.

## Fiestel structure

- A Fiestel structure is a common way of designing a block cipher, based on the idea of iterating a simple round function multiple times, with different subkeys derived from the main key.
- A Fiestel structure consists of four components: a round function F, a key schedule K, a number of rounds n, and a final swap S.
- The round function F takes two inputs: a subkey k and a half-block of plaintext or ciphertext x, and produces a half-block of ciphertext or plaintext y. The round function F can be any function that is invertible and provides confusion and diffusion, such as a combination of S-boxes and P-boxes.
- The key schedule K takes the main key K and generates a sequence of subkeys k1, k2, ..., kn, one for each round. The key schedule K can be any function that is efficient and secure, such as a simple shift or a more complex algorithm.
- The number of rounds n determines how many times the round function F is applied to the plaintext or ciphertext blocks. The number of rounds n should be large enough to provide adequate security, but not too large to affect the efficiency or performance of the block cipher.
- The final swap S is a simple operation that swaps the two half-blocks of the final round output, to ensure that the encryption and decryption processes are symmetric and can be performed using the same algorithm.
- The encryption process of a Fiestel structure can be described as follows:

  - Divide the plaintext block P into two equal-sized half-blocks L0 and R0.
  - For i = 1 to n, do the following:
    - Compute Li = Ri-1
    - Compute Ri = Li-1 XOR F(Ri-1, ki), where ki is the subkey for round i and XOR is the bitwise exclusive-or operation.
  - Swap the final half-blocks Ln and Rn, and concatenate them to form the ciphertext block C = RnLn.
- The decryption process of a Fiestel structure can be described as follows:

  - Divide the ciphertext block C into two equal-sized half-blocks Rn and Ln.
  - For i = n to 1, do the following:
    - Compute Ri-1 = Li
    - Compute Li-1 = Ri XOR F(Li, ki), where ki is the subkey for round i and XOR is the bitwise exclusive-or



# Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using substitution ciphers, which replace each plaintext symbol with a different ciphertext symbol according to a key-dependent mapping.
- Diffusion can be achieved by using transposition ciphers, which permute the positions of the plaintext symbols according to a key-dependent pattern.
- Confusion and diffusion can be combined by using a fiestal structure, which alternates substitution and transposition operations in multiple rounds with different subkeys derived from the main key.
- A well-designed cipher should have a high degree of both confusion and diffusion, so that changing one bit of the plaintext or the key affects many bits of the ciphertext, and vice versa.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of fiestal structure for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security. Here is the content in markdown format:

# Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

## Security Attacks, Services and Mechanisms
- Security attacks are any actions that compromise the security of information or systems. They can be classified into two types: passive attacks and active attacks.
- Passive attacks are those that do not alter the data or system, but only observe or analyze it. Examples are eavesdropping, traffic analysis, and ciphertext-only attacks.
- Active attacks are those that modify the data or system, or create false data or messages. Examples are replay, modification, deletion, insertion, fabrication, and man-in-the-middle attacks.
- Security services are the countermeasures that protect the information or system from security attacks. They can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation.
- Confidentiality is the service that ensures that the data or system is accessible only to authorized parties. It can be achieved by encryption, access control, and physical protection.
- Integrity is the service that ensures that the data or system is not modified or corrupted by unauthorized parties. It can be achieved by checksums, hashes, digital signatures, and audit trails.
- Availability is the service that ensures that the data or system is accessible and usable by authorized parties when needed. It can be achieved by redundancy, backup, recovery, and fault tolerance.
- Authentication is the service that ensures that the identity of a party or the origin of a message is verified. It can be achieved by passwords, tokens, certificates, biometrics, and challenge-response protocols.
- Non-repudiation is the service that ensures that a party cannot deny having sent or received a message or performed an action. It can be achieved by digital signatures, timestamps, and receipts.
- Security mechanisms are the methods or tools that implement the security services. They can be classified into two types: preventive mechanisms and detective mechanisms.
- Preventive mechanisms are those that prevent or deter security attacks from happening. Examples are encryption, access control, authentication, and digital signatures.
- Detective mechanisms are those that detect or identify security attacks that have happened or are happening. Examples are checksums, hashes, audit trails, and intrusion detection systems.

## Classical Encryption Techniques
- Encryption is the process of transforming plaintext (the original message or data) into ciphertext (the encrypted message or data) using a secret key. Decryption is the reverse process of transforming ciphertext back into plaintext using the same or a different secret key.
- Encryption techniques can be classified into two types: substitution ciphers and transposition ciphers.
- Substitution ciphers are those that replace each symbol or group of symbols in the plaintext with another symbol or group of symbols in the ciphertext. Examples are Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, and one-time pad.
- Transposition ciphers are those that rearrange the symbols or groups of symbols in the plaintext to form the ciphertext. Examples are rail fence cipher, columnar transposition cipher, and permutation cipher.
- Cryptanalysis is the process of breaking or analyzing encryption techniques, either by finding the secret key or by finding the plaintext without the key. Cryptanalysis can be classified into four types: ciphertext-only attack, known-plaintext attack, chosen-plaintext attack, and chosen-ciphertext attack.
- Ciphertext-only attack is the type of cryptanalysis where the attacker only has access to the ciphertext and tries to find the plaintext or the key by using statistical analysis, frequency analysis, or brute force.
- Known-plaintext attack is the type of cryptanalysis where the attacker has access to some pairs of plaintext and ciphertext and tries to find the key by using pattern matching, linear algebra, or differential analysis.
- Chosen-plaintext attack is the type of cryptanalysis where the attacker can choose some plaintext



# Data Encryption Standard (DES)

- Data Encryption Standard (DES) is a symmetric-key block cipher that was adopted by the US government in 1977 as a standard for encrypting and decrypting sensitive data.
- DES operates on 64-bit blocks of plaintext and ciphertext, using a 56-bit key that is derived from a 64-bit key by discarding 8 parity bits.
- DES uses a Feistel structure, which consists of 16 rounds of encryption or decryption, each involving a subkey that is derived from the main key using a key schedule algorithm.
- DES applies two main operations on the data blocks: substitution and permutation. Substitution involves replacing bits with other bits according to a predefined table called a S-box. Permutation involves rearranging the bits according to another predefined table called a P-box.
- DES achieves confusion and diffusion, two properties that make a cipher resistant to cryptanalysis, by applying multiple rounds of substitution and permutation, and by using different subkeys in each round.
- DES has a simple and elegant design, but it is no longer considered secure due to its small key size and the advances in computing power and cryptanalysis techniques. It can be broken by brute-force attacks, differential cryptanalysis, linear cryptanalysis, and other methods.
- DES can be used in various modes of operation, such as Electronic Codebook (ECB), Cipher Block Chaining (CBC), Cipher Feedback (CFB), Output Feedback (OFB), and Counter (CTR), to achieve different security and performance goals.
- Triple DES (3DES) is a variant of DES that applies three rounds of DES encryption or decryption with two or three different keys, to increase the effective key size and the security level. However, 3DES is also slow and outdated, and has been replaced by more modern and efficient block ciphers, such as Advanced Encryption Standard (AES).



# Strength of DES

- Data Encryption Standard (DES) is a symmetric key block cipher algorithm that encrypts data in 64-bit blocks using a 56-bit key .
- The strength of DES depends on two factors: the key size and the nature of the algorithm.
- The key size of 56 bits is considered too small by modern standards, as it can be brute-forced by trying all possible 2^56 keys  . This was demonstrated by the DES Cracker project in 1998, which cracked a DES-encrypted message in 56 hours using a custom-built machine.
- The nature of the algorithm is based on a Feistel network, which consists of 16 rounds of substitution and permutation operations that create confusion and diffusion in the ciphertext . The algorithm also uses a complex key schedule that derives 16 subkeys from the main key for each round .
- The strength of the algorithm is measured by its resistance to various types of cryptanalysis, such as differential cryptanalysis, linear cryptanalysis, and related-key attacks. DES has been shown to be vulnerable to some of these attacks, especially when using weak or semi-weak keys that have certain patterns or symmetries .
- To increase the security of DES, several variants have been proposed, such as Triple DES (3DES), which applies DES three times with different keys, and DESX, which adds extra bits to the key and the plaintext . However, these variants also have some limitations, such as reduced speed, increased complexity, and reduced effective key size .
- Therefore, DES is no longer considered a secure encryption standard, and has been replaced by more advanced algorithms, such as Advanced Encryption Standard (AES), which uses 128, 192, or 256-bit keys and has higher resistance to cryptanalysis .



# Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It operates by taking many pairs of plaintexts with fixed xor difference, and looking at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys. As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- It is usually launched as an adaptive chosen plaintext attack; the attacker chooses the plaintext to be encrypted (but does not know the key) and then encrypts related plaintexts.
- It studies how the differences evolve through the various rounds and various operations of the cipher.
- It is based on the assumption that the exclusive-or (XOR) operation is the difference operation.
- It can be used to find weaknesses in the design of block ciphers, such as DES, and to mount attacks on reduced-round versions of them .



# Block Cipher Modes of Operation

A block cipher is a cryptographic algorithm that encrypts or decrypts a fixed-length block of data, such as 64 bits or 128 bits, using a secret key. A block cipher by itself can only process one block at a time, so it needs a mode of operation to handle messages of arbitrary length or to provide additional security properties.

A mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity. There are different modes of operation for different purposes and applications. Some of the most common modes of operation are:

- Electronic Codebook (ECB) mode: This mode encrypts or decrypts each block of data independently, using the same key. This mode is simple and fast, but it is not secure because it does not hide patterns or repetitions in the data. For example, if two blocks of data are identical, they will produce identical ciphertexts, which can reveal information to an attacker.
- Cipher Block Chaining (CBC) mode: This mode encrypts or decrypts each block of data by XORing it with the previous ciphertext block, using the same key. This mode provides confidentiality and diffusion, because it hides patterns and makes each ciphertext block depend on all the previous ones. However, this mode requires an initialization vector (IV), which is a random or unpredictable value that is used to encrypt or decrypt the first block. The IV must be known to both the sender and the receiver, and must not be reused for different messages.
- Cipher Feedback (CFB) mode: This mode encrypts or decrypts each block of data by XORing it with the output of the block cipher applied to the previous ciphertext block, using the same key. This mode also requires an IV, and provides confidentiality and diffusion. However, this mode can also work as a stream cipher, because it can encrypt or decrypt data of any size, not just multiples of the block size. This mode is useful for encrypting data that comes in irregular or unpredictable lengths, such as network packets or keystrokes.
- Output Feedback (OFB) mode: This mode encrypts or decrypts each block of data by XORing it with the output of the block cipher applied to the previous output block, using the same key. This mode also requires an IV, and provides confidentiality and diffusion. However, this mode also works as a stream cipher, and it is different from CFB mode because it does not depend on the ciphertext. This mode is useful for encrypting data in noisy or unreliable channels, such as wireless networks or satellite communications, because it can recover from errors or losses in the ciphertext.
- Counter (CTR) mode: This mode encrypts or decrypts each block of data by XORing it with the output of the block cipher applied to a counter, using the same key. The counter is a value that is incremented for each block, and it can be based on the IV, the message number, the block number, or any other sequence. This mode also works as a stream cipher, and provides confidentiality and diffusion. However, this mode is different from OFB mode because it does not depend on the previous output. This mode is useful for encrypting data in parallel or distributed systems, because it allows random access to any block of the ciphertext.



# Triple DES

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block .
- It is a simple method of increasing the key size of DES to protect against brute-force attacks, without the need to design a new block cipher algorithm.
- The key size of 3DES is 168 bits, but due to the meet-in-the-middle attack, the effective security it provides is only 112 bits.
- 3DES uses the DES cipher three times in one of the following modes :
  - Encrypt-Decrypt-Encrypt (EDE): The first key is used to encrypt the data, the second key is used to decrypt the data, and the third key is used to encrypt the data again.
  - Encrypt-Encrypt-Encrypt (EEE): The first key is used to encrypt the data, the second key is used to encrypt the data again, and the third key is used to encrypt the data once more.
- 3DES can use either two keys (K1 and K2) or three keys (K1, K2, and K3) for encryption and decryption :
  - Two-key 3DES: The same key (K1) is used for the first and third encryption/decryption, and a different key (K2) is used for the second encryption/decryption. The key size is 112 bits.
  - Three-key 3DES: Three different keys (K1, K2, and K3) are used for each encryption/decryption. The key size is 168 bits.
- 3DES is more secure than DES, but it is also slower and more complex .
- 3DES is being phased out by newer and more efficient encryption algorithms, such as AES .



## Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A **field** is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity, and non-zero inverses. For example, the set of rational numbers with addition and multiplication is a field.
- A **finite field** is a field that has a finite number of elements. A finite field of order p, where p is a prime number, is denoted by GF(p) and is defined as the set of integers modulo p with arithmetic operations modulo p. For example, GF(5) is the set {0, 1, 2, 3, 4} with addition and multiplication modulo 5.
- **Modular arithmetic** is a system of arithmetic where numbers are reduced to a fixed range by taking the remainder after division by a modulus. For example, in modulo 7 arithmetic, 9 is equivalent to 2, since 9 mod 7 = 2. Modular arithmetic is useful for cryptography, as it allows operations to be performed on large numbers without overflow or loss of precision.
- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19 are prime numbers. Prime numbers are important for cryptography, as they are the building blocks of many cryptographic algorithms and protocols.
- Two numbers are **relatively prime** or **coprime** if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, since their only common divisor is 1. Relatively prime numbers are useful for cryptography, as they allow the use of modular inverses and Euler's theorem.
- The **Extended Euclidean Algorithm** is an algorithm that computes the greatest common divisor (gcd) of two numbers, as well as the coefficients of a linear combination of the two numbers that equals the gcd. For example, the gcd of 30 and 18 is 6, and the Extended Euclidean Algorithm can find that 6 = 2 * 30 - 3 * 18. The Extended Euclidean Algorithm is useful for cryptography, as it can be used to find modular inverses and solve linear congruences.
- The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits using a secret key of 128, 192, or 256 bits. AES is the most widely used encryption standard in the world, and is considered to be secure and efficient. AES uses a series of transformations on the data blocks, such as substitution, permutation, mixing, and key addition, to achieve confusion and diffusion.
- **Fermat's theorem** states that if p is a prime number and a is any integer, then a^p - a is divisible by p. For example, 3^5 - 3 = 240 is divisible by 5. Fermat's theorem is useful for cryptography, as it can be used to test for primality and to compute modular exponentiation.
- **Euler's theorem** states that if a and n are relatively prime, then a^phi(n) = 1 mod n, where phi(n) is the Euler's totient function, which counts the number of positive integers less than n that are relatively prime to n. For example, phi(10) = 4, and 3^4 = 1 mod 10. Euler's theorem is useful for cryptography, as it generalizes Fermat's theorem and can be used to compute modular exponentiation and inverses.
- **Primality testing** is the problem of determining whether a given number is prime or composite. There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, and AKS test. Some of these



# Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity and the existence of a multiplicative inverse for every nonzero element.
- A finite field is a field that has a finite number of elements. A finite field of order p, where p is a prime number, is denoted by GF(p) and is also called a prime field. The elements of GF(p) are the integers from 0 to p-1, and the operations are performed modulo p.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range of values by using the remainder operation. For example, in modulo 7 arithmetic, 8 is equivalent to 1, since 8 mod 7 = 1. Modular arithmetic is useful for cryptography because it allows for easy computation of inverses and exponentiation.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A relative prime number is a natural number that is coprime to another natural number, meaning that they have no common positive divisors other than 1. For example, 6 and 35 are relative prime numbers, since their only common divisor is 1.
- The Extended Euclidean Algorithm is an algorithm that computes the greatest common divisor (gcd) of two natural numbers, as well as the coefficients of a linear combination of the two numbers that equals the gcd. For example, the gcd of 30 and 18 is 6, and the Extended Euclidean Algorithm can find integers x and y such that 30x + 18y = 6. The algorithm is useful for cryptography because it can be used to find the multiplicative inverse of an element in a finite field.
- The Advanced Encryption Standard (AES) is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192 or 256 bits. The encryption and decryption processes involve several rounds of substitution, permutation, mixing and key addition operations, which provide security against various attacks.
- Fermat's theorem states that if p is a prime number and a is any integer, then a^p - a is divisible by p. Euler's theorem generalizes Fermat's theorem to the case where p is not necessarily prime, but a and p are coprime. It states that a^phi(p) - 1 is divisible by p, where phi(p) is the Euler totient function, which counts the number of positive integers less than p that are coprime to p.
- Primality testing is the problem of determining whether a given natural number is prime or composite. There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc. Some of them are deterministic, meaning that they always give the correct answer, while others are probabilistic, meaning that they give the correct answer with high probability, but may fail with a small probability.
- The Chinese Remainder theorem is a theorem that states that if n1, n2, ..., nk are pairwise coprime natural numbers, and a1, a2, ..., ak are any integers, then there exists a unique integer x, modulo the product of n1, n2, ..., nk, such that x is congruent to ai modulo ni, for i = 1, 2, ..., k. The theorem also provides a method to find such an x. The theorem is useful for cryptography because it can be used to speed up computations involving large numbers, such as RSA encryption and decryption.
- The Discrete Logarithm Problem is the problem of finding an integer x, given a finite cyclic group G, a generator g of G, and an element



# Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- **Group**: A set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- **Field**: A group with two binary operations, usually called addition and multiplication, that satisfy four additional properties: commutativity, distributivity, identity and inverse.
- **Finite field of the form GF(p)**: A field with a finite number of elements, where p is a prime number. The elements are the integers from 0 to p-1, and the operations are performed modulo p.
- **Modular arithmetic**: A system of arithmetic where numbers are reduced to a fixed range by using the remainder operation. For example, 7 mod 3 = 1, because 7 divided by 3 gives a remainder of 1.
- **Prime and relative prime numbers**: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A relative prime number is a natural number that has no common positive divisors with another natural number, except 1. For example, 5 and 7 are both prime and relative prime numbers.
- **Extended Euclidean Algorithm**: An algorithm that computes the greatest common divisor (GCD) of two natural numbers, as well as the coefficients of Bézout's identity, which are integers x and y such that ax + by = GCD(a, b). For example, the GCD of 30 and 18 is 6, and the coefficients of Bézout's identity are -1 and 2, because 30(-1) + 18(2) = 6.
- **Advanced Encryption Standard (AES) encryption and decryption**: A symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192 or 256 bits. The encryption process consists of four stages: byte substitution, row shift, column mix and key addition. The decryption process is the reverse of the encryption process, using the inverse operations.
- **Fermat’s and Euler’s theorem**: Two theorems in number theory that relate modular exponentiation with prime and relative prime numbers. Fermat's theorem states that if p is a prime number and a is any integer, then a^p mod p = a mod p. Euler's theorem states that if a and n are relative prime numbers, then a^phi(n) mod n = 1, where phi(n) is Euler's totient function, which counts the number of positive integers less than n that are relative prime to n.
- **Primality testing**: The problem of determining whether a given natural number is prime or composite. There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test and AKS test. Some of these algorithms are deterministic, meaning they always give the correct answer, while others are probabilistic, meaning they give the correct answer with high probability.
- **Chinese Remainder theorem**: A theorem that states that if n1, n2, ..., nk are pairwise coprime natural numbers, and a1, a2, ..., ak are any integers, then there exists a unique integer x such that x mod ni = ai for all i from 1 to k, and x is in the range from 0 to n1n2...nk - 1. The theorem also provides a method to compute x from the given values.
- **Discrete Logarithmic Problem**: The problem of finding an integer x such that a^x mod p = b, where a, b and p are given integers, and p is a prime number. This problem is believed to be hard to solve in general, and it is the basis of some cryptographic schemes, such as the Diffie-Hellman key exchange and the ElGamal encryption.
- **Principles of public key crypto systems**: A public key crypto system is a cryptographic scheme that uses two different keys: a public key and a private key. The public key can be shared with anyone



# Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p    .
- GF(p) is also called the Galois field, in honor of the founder of finite field theory, Évariste Galois.
- GF(p) can be constructed from the set of integers modulo p, i.e., Zp = {0, 1, ..., p-1}, together with arithmetic operations modulo p   .
- For example, GF(5) is the set {0, 1, 2, 3, 4}, with addition and multiplication modulo 5. The following tables show the addition and multiplication tables for GF(5):

| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |

- Some properties of GF(p) are:
  - It is a commutative ring, i.e., it satisfies the axioms of closure, associativity, commutativity and distributivity for both addition and multiplication   .
  - It has an additive identity element, 0, and a multiplicative identity element, 1   .
  - Every element has an additive inverse, i.e., for any a in GF(p), there exists b in GF(p) such that a + b = 0 (mod p)   .
  - Every nonzero element has a multiplicative inverse, i.e., for any a in GF(p), there exists b in GF(p) such that a x b = 1 (mod p)   . This is also called the multiplicative inverse axiom.
  - It is a field, i.e., it satisfies all the axioms of a field   .
  - It is a cyclic group under both addition and multiplication, i.e., there exists an element g in GF(p) such that every element in GF(p) can be obtained by repeatedly adding or multiplying g by itself   . Such an element g is called a generator or a primitive element of GF(p)   .
  - For example, in



# Modular Arithmetic

- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus  .
- For example, if the modulus is 12, then 13 is equivalent to 1, 14 is equivalent to 2, and so on. We write this as 13 ≡ 1 (mod 12), 14 ≡ 2 (mod 12), etc.
- Modular arithmetic can be used to model situations where numbers cycle or repeat, such as clocks, calendars, cryptography, etc.
- The basic operations of modular arithmetic are addition, subtraction, multiplication, and division. They follow the same rules as normal arithmetic, except that the result is always reduced to the smallest positive remainder by dividing by the modulus and taking the remainder.
- For example, 7 + 8 = 15, but 15 ≡ 3 (mod 12), so 7 + 8 ≡ 3 (mod 12). Similarly, 9 - 5 = 4, but 4 ≡ 4 (mod 12), so 9 - 5 ≡ 4 (mod 12). Likewise, 6 × 4 = 24, but 24 ≡ 0 (mod 12), so 6 × 4 ≡ 0 (mod 12). Finally, 8 ÷ 4 = 2, but 2 ≡ 2 (mod 12), so 8 ÷ 4 ≡ 2 (mod 12).
- However, not every integer has a multiplicative inverse in modular arithmetic. A multiplicative inverse of a number a is a number b such that a × b ≡ 1 (mod n). For example, 3 has a multiplicative inverse of 4 in modulo 11, because 3 × 4 ≡ 1 (mod 11). But 2 has no multiplicative inverse in modulo 12, because there is no number b such that 2 × b ≡ 1 (mod 12).
- A number a has a multiplicative inverse in modulo n if and only if a and n are coprime, meaning that they have no common factors other than 1. For example, 3 and 11 are coprime, but 2 and 12 are not.
- To find the multiplicative inverse of a number a in modulo n, we can use the extended Euclidean algorithm, which finds the greatest common divisor (gcd) of a and n, and also the coefficients x and y such that ax + ny = gcd(a, n). If gcd(a, n) = 1, then a and n are coprime, and x is the multiplicative inverse of a in modulo n. For example, to find the multiplicative inverse of 3 in modulo 11, we have:

3x + 11y = 1

- Using the extended Euclidean algorithm, we get:

11 = 3 × 3 + 2

3 = 2 × 1 + 1

2 = 1 × 2 + 0

- Working backwards, we get:

1 = 3 - 2 × 1

1 = 3 - (11 - 3 × 3) × 1

1 = 3 × 4 - 11 × 1

- Therefore, x = 4 and y = -1, and 4 is the multiplicative inverse of 3 in modulo 11. We can check that 3 × 4 ≡ 1 (mod 11).
- Modular arithmetic is useful for many applications in cryptography, such as the RSA algorithm, which is based on the difficulty of factoring large numbers. It is also related to other concepts in number theory, such as Fermat's theorem, Euler's theorem, primality testing, Chinese remainder theorem, and discrete logarithm problem.



Hello, I am Sydney, your AI assistant. I can help you with your topic of prime and relative prime numbers for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security. Here is the content I have generated for you in markdown format:

# Prime and Relative Prime Numbers

## Prime Numbers

- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29 are prime numbers.
- Prime numbers are important in cryptography because they are the building blocks of many encryption schemes, such as RSA and Diffie-Hellman.
- Prime numbers are also used to generate pseudorandom numbers, which are essential for secure communication and data protection.

## Relative Prime Numbers

- Two natural numbers are said to be relatively prime or coprime if they have no common positive divisors other than 1.
- For example, 8 and 15 are relatively prime because their only common divisor is 1, but 8 and 12 are not relatively prime because they have 2 and 4 as common divisors.
- The greatest common divisor (GCD) of two numbers is the largest positive number that divides both of them. For example, the GCD of 8 and 12 is 4, and the GCD of 8 and 15 is 1.
- The GCD of two numbers can be computed using the Euclidean algorithm, which is based on repeated division and remainder operations.
- For example, to find the GCD of 8 and 15, we can use the following steps:

  - Divide 15 by 8 and get the quotient 1 and the remainder 7.
  - Divide 8 by 7 and get the quotient 1 and the remainder 1.
  - Divide 7 by 1 and get the quotient 7 and the remainder 0.
  - The last nonzero remainder is the GCD, which is 1 in this case.

- Two numbers are relatively prime if and only if their GCD is 1.
- Relatively prime numbers are important in cryptography because they are used to create public and private keys, such as in RSA and Diffie-Hellman.
- Relatively prime numbers are also used to ensure that encryption and decryption operations are reversible and unique, such as in modular arithmetic and Chinese remainder theorem.



# Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's identity, which states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and mod is the modulo operation.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax = 1 mod b.
- The extended Euclidean algorithm is also useful for computing the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

## Algorithm

- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works as follows:

  - If A = 0 then GCD(A,B) = B, since the GCD(0,B) = B, and we can stop.
  - If B = 0 then GCD(A,B) = A, since the GCD(A,0) = A, and we can stop.
  - Write A in quotient remainder form (A = B⋅Q + R)
  - Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)

- The extended Euclidean algorithm keeps track of the quotients Q and the remainders R in each step, and uses them to compute the coefficients x and y of Bézout's identity. The algorithm works as follows:

  - Initialize x1 = 1, y1 = 0, x2 = 0, y2 = 1
  - If A = 0 then x = x2, y = y2, and we can stop.
  - If B = 0 then x = x1, y = y1, and we can stop.
  - Write A in quotient remainder form (A = B⋅Q + R)
  - Update x1 = x2, y1 = y2, x2 = x1 - Q⋅x2, y2 = y1 - Q⋅y2
  - Find x and y using the extended Euclidean Algorithm with inputs B and R

- The algorithm terminates when either A or B becomes zero, and returns the values of x and y such that ax + by = gcd(a,b).

## Example

- Suppose we want to find the integers x and y such that 99x + 78y = gcd(99,78) using the extended Euclidean algorithm. We start by applying the Euclidean algorithm to find the gcd:

  - 99 = 78⋅1 + 21
  - 78 = 21⋅3 + 15
  - 21 = 15⋅1 + 6
  - 15 = 6⋅2 + 3
  - 6 = 3⋅2 + 0

- The gcd is the last nonzero remainder, which is 3. Now we use the extended Euclidean algorithm to find the coefficients x and y:

  - Initialize x1 = 1, y1 = 0, x2 = 0, y2 = 1
  - 99 = 78⋅1 + 21, update x1 = 0, y1 = 1, x2 = 1 - 1⋅0 = 1, y2 = 0 - 1⋅1 = -1
  - 78 = 21⋅3 + 15, update x1 = 1, y1 = -1, x2 = 0 - 3⋅1 = -3, y2 = 1 - 3⋅(-1) = 4
  - 21 = 15⋅1 + 6, update x1 = -3, y1 = 4, x2 = 1 -



# Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric block cipher that can encrypt and decrypt data using the same key  .
- AES operates on blocks of 128 bits and can use keys of 128, 192, or 256 bits .
- AES consists of four main operations: byte substitution, row shift, column mix, and key addition  .
- AES performs these operations in several rounds, depending on the key size. For 128-bit keys, there are 10 rounds; for 192-bit keys, there are 12 rounds; and for 256-bit keys, there are 14 rounds .
- AES encryption transforms plaintext into ciphertext by applying the operations in each round, using a different round key derived from the original key .
- AES decryption reverses the process by applying the inverse operations in the reverse order, using the same round keys .
- AES is a widely used and secure algorithm that can protect electronic data from unauthorized access or modification  .

# Fermat's and Euler's theorem

- Fermat's theorem (or Fermat's little theorem) states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p   .
- Euler's theorem (or Euler's totient theorem) is a generalization of Fermat's theorem that states that if n and a are coprime positive integers, and φ(n) is Euler's totient function, then a^φ(n) is congruent to 1 modulo n   .
- Euler's totient function φ(n) counts the number of positive integers less than or equal to n that are coprime to n   .
- Fermat's theorem is a special case of Euler's theorem when n is a prime number, since φ(p) = p - 1 for any prime p   .
- Both Fermat's and Euler's theorems are useful in number theory and cryptography, especially in the RSA algorithm, which is based on the difficulty of finding the modular inverse of large numbers   .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography and Network Security:

# Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A **field** is a group with an additional binary operation that satisfies four more properties: closure, associativity, identity, and inverse. The additional operation is also commutative and distributive over the first operation. For example, the set of rational numbers with addition and multiplication is a field.
- A **finite field** is a field with a finite number of elements. A finite field of the form GF(p) is a field with p elements, where p is a prime number. The elements are the integers from 0 to p-1, and the operations are addition and multiplication modulo p. For example, GF(5) is a field with 5 elements: 0, 1, 2, 3, and 4.
- **Modular arithmetic** is a system of arithmetic where numbers are reduced to a fixed range by using the remainder after division by a modulus. For example, in modulo 7 arithmetic, 8 is equivalent to 1, and 15 is equivalent to 1. Modular arithmetic is useful for cryptography because it allows operations on large numbers to be performed efficiently and securely.
- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, and 11 are prime numbers. Prime numbers are important for cryptography because they are the building blocks of many cryptographic algorithms and protocols.
- Two numbers are **relatively prime** or **coprime** if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, but 8 and 12 are not. Relatively prime numbers are useful for cryptography because they ensure that certain operations have unique inverses and solutions.
- The **Extended Euclidean Algorithm** is an algorithm that computes the greatest common divisor (GCD) of two numbers, as well as the coefficients of a linear combination of the two numbers that equals the GCD. For example, the GCD of 30 and 18 is 6, and 6 = 2 * 30 - 3 * 18. The Extended Euclidean Algorithm is useful for cryptography because it can be used to find the inverse of a number modulo another number, which is needed for some encryption and decryption algorithms.
- The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192, or 256 bits. The AES algorithm consists of four main steps: subbytes, shiftrows, mixcolumns, and addroundkey, which are repeated for a number of rounds depending on the key size. The AES algorithm is widely used for cryptography because it is fast, secure, and standardized.
- **Fermat's theorem** states that if p is a prime number, and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p. For example, if p = 5 and a = 2, then 2^4 is congruent to 1 modulo 5. Fermat's theorem is useful for cryptography because it can be used to test whether a number is prime or not, which is needed for some cryptographic algorithms and protocols.
- **Euler's theorem** is a generalization of Fermat's theorem that states that if a and n are relatively prime, then a^(phi(n)) is congruent to 1 modulo n, where phi(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n. For example, if a = 2 and n = 10, then phi(10) = 4, and 2^4 is congruent to 1 modulo



# Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution.
- The theorem has its origin in the work of the 3rd-century- AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1).
- The theorem can be expressed in terms of congruences as follows: Suppose a1, a2, ..., ak are integers and n1, n2, ..., nk are pairwise coprime positive integers. Then, for any given sequence of integers x1, x2, ..., xk, there exists an integer x such that

x ≡ x1 (mod n1)  
x ≡ x2 (mod n2)  
...  
x ≡ xk (mod nk)

Moreover, any two such integers x and y are congruent modulo the product N = n1n2...nk, that is, x ≡ y (mod N).
- The theorem can be proved by using the Euclidean algorithm and the extended Euclidean algorithm to find the modular inverses of the divisors.
- The theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The theorem is also useful for solving systems of congruences, cryptography, and number theory problems .



# Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log<sub>g</sub>h in finite groups G is to raise g to larger and larger powers k until the desired h is found. This is called the **brute-force** or **exhaustive search** algorithm.
- The brute-force algorithm has a time complexity of O(|G|) and a space complexity of O(1), where |G| is the order of the group.
- There are more efficient algorithms for finding discrete logarithms in some special groups, such as the group Z<sub>p</sub><sup>*</sup>, where p is a prime number.
- The current best algorithm for solving the discrete logarithm problem in Z<sub>p</sub><sup>*</sup> is the **number field sieve** (NFS) algorithm, whose running time is exponential in log<sub>e</sub>p.
- The NFS algorithm has a time complexity of O(exp((c+o(1))(log p)<sup>1/3</sup>(log log p)<sup>2/3</sup>)) and a space complexity of O(exp((c+o(1))(log p)<sup>1/3</sup>(log log p)<sup>2/3</sup>)), where c is a constant.
- The discrete logarithm problem is the basis of many cryptographic schemes, such as the **Diffie-Hellman** key exchange, the **ElGamal** encryption and signature schemes, and the **Digital Signature Algorithm** (DSA).
- The security of these schemes relies on the assumption that the discrete logarithm problem is hard to solve in the chosen group.

