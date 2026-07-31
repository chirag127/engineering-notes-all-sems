

Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

## Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

- Security attacks: Any action that compromises the security of information or systems. Examples are interception, modification, fabrication, and interruption of data or services.
- Security services: Any function that enhances the security of information or systems. Examples are confidentiality, integrity, authentication, non-repudiation, and availability.
- Security mechanisms: Any method or tool that implements a security service. Examples are encryption, digital signatures, hash functions, and firewalls.
- Classical encryption techniques: Methods of encrypting and decrypting messages using simple mathematical operations and transformations. Examples are substitution ciphers and transposition ciphers.
- Substitution ciphers: Ciphers that replace each letter or symbol in the plaintext with another letter or symbol in the ciphertext, according to a fixed rule or key. Examples are Caesar cipher, monoalphabetic cipher, and polyalphabetic cipher.
- Transposition ciphers: Ciphers that rearrange the order of the letters or symbols in the plaintext, according to a fixed rule or key. Examples are rail fence cipher, columnar transposition cipher, and permutation cipher.
- Cryptanalysis: The science of breaking ciphers, by finding the key or the plaintext without knowing the key. Examples are frequency analysis, brute force attack, and known plaintext attack.
- Steganography: The art of hiding messages in other messages or media, such that the existence of the hidden message is not apparent. Examples are hiding text in images, audio, or video files, or using invisible ink or microdots.
- Stream ciphers: Ciphers that encrypt and decrypt messages one bit or one byte at a time, using a keystream that is generated from a secret key and a pseudorandom number generator. Examples are RC4, A5/1, and Salsa20.
- Block ciphers: Ciphers that encrypt and decrypt messages in fixed-size blocks, using a secret key and a mathematical function. Examples are DES, AES, and Blowfish.
- Block cipher principles: The basic design principles of block ciphers, such as block size, key size, number of rounds, and round function.
- Shannon’s theory of confusion and diffusion: The theory proposed by Claude Shannon that states that a good cipher should have two properties: confusion, which means that the relationship between the plaintext and the ciphertext is complex and obscure, and diffusion, which means that the influence of one plaintext bit on the ciphertext bits is spread out and randomized.
- Fiestal structure: A common structure of block ciphers, where each round consists of four operations: subkey mixing, substitution, permutation, and swapping. Examples are DES, AES, and IDEA.
- Data encryption standard (DES): A widely used block cipher that was standardized by NIST in 1977. It has a block size of 64 bits, a key size of 56 bits, and 16 rounds of encryption or decryption. It uses a fiestal structure and a round function that consists of expansion, XOR, substitution, and permutation.
- Strength of DES: The security of DES depends on the key size, the number of rounds, and the resistance to cryptanalysis. DES has a relatively small key size, which makes it vulnerable to brute force attacks. DES also has some weak keys and semi-weak keys, which reduce its security. DES is also susceptible to differential cryptanalysis and linear cryptanalysis, which are advanced techniques of breaking block ciphers.
- Idea of differential cryptanalysis: A method of breaking block ciphers, where the attacker analyzes the differences between pairs of plaintexts and ciphertexts, and exploits the statistical properties of the round function to recover the key. It requires a large number of chosen plaintexts and ciphertexts, and a complex analysis of the cipher structure.
- Block cipher modes of operation: Different ways of using block ciphers to encrypt and decrypt messages of arbitrary length. Examples are electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR) modes. Each mode has different advantages and disadvantages in terms of security,



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for your topic:

### Introduction to security attacks

- A security attack is any action that compromises the security of information owned by an organization or an individual.
- Security attacks can be classified into two categories: passive attacks and active attacks.
- Passive attacks are those that do not affect the normal functioning of the system, but only attempt to access or monitor the information. Examples of passive attacks are eavesdropping, traffic analysis, and sniffing.
- Active attacks are those that alter or disrupt the normal functioning of the system, or create a false or misleading information. Examples of active attacks are modification, deletion, insertion, replay, denial of service, and masquerade.
- Security attacks can also be categorized based on the source of the attack: insider attacks and outsider attacks.
- Insider attacks are those that are launched by authorized users of the system, who misuse their privileges or credentials to harm the system or the information. Examples of insider attacks are sabotage, theft, fraud, and espionage.
- Outsider attacks are those that are launched by unauthorized users of the system, who exploit the vulnerabilities or weaknesses of the system or the information. Examples of outsider attacks are hacking, phishing, malware, and ransomware.

### Security services and mechanisms

- Security services are the goals or objectives that a secure system should provide to its users and information. Security services can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation.
- Confidentiality is the service that ensures that the information is accessible only to authorized parties, and is protected from unauthorized disclosure. Confidentiality can be achieved by using encryption, access control, and data hiding techniques.
- Integrity is the service that ensures that the information is accurate and consistent, and is protected from unauthorized modification or deletion. Integrity can be achieved by using hashing, digital signatures, and checksums techniques.
- Availability is the service that ensures that the information and the system are accessible and functional at all times, and are protected from unauthorized denial of service or disruption. Availability can be achieved by using redundancy, backup, and load balancing techniques.
- Authentication is the service that ensures that the parties involved in a communication or a transaction are who they claim to be, and are verified by a trusted authority. Authentication can be achieved by using passwords, biometrics, certificates, and tokens techniques.
- Non-repudiation is the service that ensures that the parties involved in a communication or a transaction cannot deny their participation or the validity of the information. Non-repudiation can be achieved by using digital signatures, timestamps, and audit trails techniques.
- Security mechanisms are the methods or tools that are used to implement the security services. Security mechanisms can be classified into two categories: preventive mechanisms and detective mechanisms.
- Preventive mechanisms are those that prevent or deter the security attacks from occurring, by enforcing the security policies and rules. Examples of preventive mechanisms are encryption, access control, firewalls, and antivirus software.
- Detective mechanisms are those that detect or identify the security attacks that have occurred, by monitoring and analyzing the system and the information. Examples of detective mechanisms are logging, auditing, intrusion detection, and alert systems.



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




### Classical encryption techniques: substitution ciphers and transposition ciphers

- Classical encryption techniques are based on two basic principles: substitution and transposition  .
- Substitution ciphers replace each character of the plaintext with a different character, number, or symbol, according to a fixed rule or key  .
- Transposition ciphers rearrange the order of the characters of the plaintext, according to a fixed rule or key  .
- Both techniques are now outdated and can be easily broken by modern cryptanalysis methods  .
- Examples of substitution ciphers are Caesar cipher, Monoalphabetic cipher, and Vigenere cipher  .
- Examples of transposition ciphers are Rail fence cipher, Columnar transposition cipher, and Scytale cipher  .
- A product cipher is a combination of substitution and transposition ciphers, which provides more security than either technique alone .
- A rotor machine is a type of product cipher that uses rotating disks to perform multiple substitutions and transpositions .
- Steganography is a different technique that hides the existence of a message, rather than encrypting it.



# Cryptanalysis

Cryptanalysis is the process of analyzing information systems, such as codes, ciphers or encrypted text, in order to understand hidden aspects of the systems or to break their security  . Cryptanalysis is used to decrypt ciphertexts without knowledge of the plaintext source, encryption key or the algorithm used to encrypt it. Cryptanalysis also aims to find and improve techniques for defeating or weakening cryptographic systems.

Some of the topics related to cryptanalysis are:

- **Substitution ciphers and transposition ciphers**: These are two types of classical encryption techniques that involve replacing or rearranging the letters of the plaintext to create the ciphertext. Substitution ciphers replace each letter with another letter, symbol or number, while transposition ciphers permute the order of the letters.
- **Cryptanalysis of substitution and transposition ciphers**: Cryptanalysis of these ciphers involves finding patterns, frequencies, or statistical properties of the ciphertext that reveal information about the plaintext or the key. For example, frequency analysis is a common technique for breaking substitution ciphers, as it exploits the fact that some letters are more common than others in a given language.
- **Steganography**: This is the art or practice of hiding information within other information, such as images, audio, or text. Steganography is different from cryptography, as it does not alter the appearance of the information, but rather conceals its existence. Steganography can be used to enhance the security of cryptography, or to evade detection or censorship.
- **Cryptanalysis of steganography**: Cryptanalysis of steganography involves detecting the presence of hidden information, extracting it, or modifying it. For example, steganalysis is the process of finding hidden messages in images, by looking for anomalies, distortions, or statistical differences in the image data.
- **Stream and block ciphers**: These are two types of modern encryption techniques that operate on binary data, such as bits or bytes. Stream ciphers encrypt each bit or byte of the plaintext individually, using a keystream that is generated from a secret key and a nonce. Block ciphers encrypt a fixed-length block of bits or bytes at a time, using a secret key and a mode of operation.
- **Cryptanalysis of stream and block ciphers**: Cryptanalysis of these ciphers involves finding weaknesses in the design or implementation of the ciphers, such as linear or differential cryptanalysis, or exploiting side-channel attacks, such as timing or power analysis. For example, linear cryptanalysis is a technique for breaking block ciphers, by finding linear approximations of the cipher's function that hold with a certain probability.
- **Block cipher principles**: These are the basic concepts and properties that underlie the design and analysis of block ciphers. Some of these principles are:

  - **Confusion and diffusion**: These are two goals of block cipher design, proposed by Claude Shannon, that aim to make the relationship between the plaintext, the ciphertext, and the key as complex and unpredictable as possible. Confusion means that each bit of the ciphertext should depend on several bits of the key, while diffusion means that each bit of the ciphertext should depend on several bits of the plaintext.
  - **Fiestel structure**: This is a common structure for block ciphers, invented by Horst Feistel, that consists of several rounds of encryption, each involving a substitution and a permutation. The substitution is usually a non-linear function that operates on half of the block, while the permutation is usually a linear function that swaps the halves of the block. The key is used to generate round keys that are input to the substitution function.
  - **Data encryption standard (DES)**: This is a widely used block cipher, developed by IBM and adopted by the US government in 1977, that encrypts 64-bit blocks using a 56-bit key and 16 rounds of encryption. DES is based on the Fiestel structure, and uses a complex substitution function called S-boxes, and a simple permutation function called P-boxes.
  - **Strength of DES**: DES was considered secure when it was first introduced, but it was later shown to be vulnerable to various attacks, such as brute force, differential cryptanalysis, and linear cryptanalysis. The main weakness of DES is its short key length, which makes it feasible to try all possible keys. The best known attack on DES is the linear cryptanalysis, which can break DES with 2^43 known plaintexts



Hello, I am Sydney, your AI assistant. I can help you with your study material on cryptography and network security. Here is some content on steganography for the notes of the Unit 1.

# Steganography

- Steganography is the art and science of hiding information in plain sight, such that only the intended recipient can detect it.
- Steganography can be used to conceal the existence of a secret message, or to enhance the security of an encrypted message by adding another layer of obfuscation.
- Steganography can be applied to various types of media, such as text, images, audio, video, or network protocols.
- Steganography techniques can be classified into two categories: **spatial domain** and **frequency domain**.
  - Spatial domain techniques modify the least significant bits (LSB) of the pixels or bits of the cover media, such as changing the color or brightness of an image, or inserting hidden characters in a text.
  - Frequency domain techniques transform the cover media into a different representation, such as discrete cosine transform (DCT) or discrete wavelet transform (DWT), and embed the secret message in the coefficients of the transformed domain, such as the high-frequency or low-frequency components of an image or audio.
- Steganography can be combined with cryptography to achieve **steganalysis-resistant** steganography, where the secret message is first encrypted and then hidden in the cover media, making it harder for an attacker to detect or recover the hidden information.
- Steganography can also be combined with **error correction codes** (ECC) to achieve **robust** steganography, where the secret message can be recovered even if the cover media is distorted or corrupted by noise, compression, or manipulation.
- Steganography can be evaluated by several criteria, such as **capacity**, **imperceptibility**, **security**, and **robustness**.
  - Capacity is the amount of information that can be hidden in the cover media without affecting its quality or size.
  - Imperceptibility is the degree to which the cover media is indistinguishable from the original media after hiding the secret message.
  - Security is the resistance to steganalysis, or the difficulty of detecting the presence or extracting the content of the hidden message by an unauthorized party.
  - Robustness is the ability to recover the hidden message after the cover media undergoes some transformations, such as noise, compression, or manipulation.



Hello, I am Sydney, your AI assistant. I can help you with your notes on stream and block ciphers. Here is the content in markdown format:

### Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that convert plaintext into ciphertext using a secret key.
- Stream ciphers encrypt one bit or byte of plaintext at a time, while block ciphers encrypt a fixed number of bits or bytes of plaintext as a single unit.
- Stream ciphers are faster and simpler than block ciphers, but they are more vulnerable to attacks such as ciphertext-only attack, known-plaintext attack, and chosen-plaintext attack.
- Block ciphers are more secure and versatile than stream ciphers, but they require more processing power and memory, and they may introduce padding or block chaining issues.
- Stream ciphers can be classified into two categories: synchronous and self-synchronizing. Synchronous stream ciphers use the same keystream for encryption and decryption, and they require the sender and the receiver to be synchronized. Self-synchronizing stream ciphers use the previous ciphertext bits to generate the keystream, and they can recover from errors or losses in transmission.
- Block ciphers can be classified into two categories: substitution-permutation networks (SPNs) and Feistel networks. SPNs consist of alternating rounds of substitution and permutation operations, which provide confusion and diffusion respectively. Feistel networks consist of repeated rounds of splitting, mixing, and swapping operations, which allow the use of reversible functions as round functions.



### Modern Block Ciphers

- A modern block cipher is a cipher which encrypts m-bit block of plaintext and decrypts m-bit block of ciphertext  .
- For encryption or decryption, modern block cipher facilitate a K bit key and the decryption algorithm should be inverse of encryption algorithms and for both encryption and decryption similar key is used.
- Most modern block ciphers are designed to encrypt data in fixed-size blocks of either 64 or 128 bits .
- Modern block ciphers are based on the design of an iterated product cipher, which consists of repeated rounds of a simple function .
- Each round of a block cipher uses a subkey derived from the main key using a key schedule algorithm.
- Modern block ciphers are specified elementary components in the design of many cryptographic protocols and are widely used to encrypt large amounts of data, including in data exchange protocols.
- Some examples of modern block ciphers are Data Encryption Standard (DES), Triple DES, Advanced Encryption Standard (AES), Blowfish, Twofish, etc.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of block ciphers principles. Here is the content I have generated for you:

### Block ciphers principles

- A block cipher is a symmetric encryption algorithm that operates on a fixed-length group of bits, called a block, with a secret key.
- A block cipher can be used to encrypt and decrypt plaintext and ciphertext, respectively, by applying the same key and algorithm in reverse.
- A block cipher can also be used to construct other cryptographic primitives, such as stream ciphers, hash functions, message authentication codes, and pseudorandom number generators.
- The security of a block cipher depends on its resistance to various types of attacks, such as brute-force, differential, linear, and algebraic attacks, among others.
- The design of a block cipher involves two main aspects: the structure and the round function.
- The structure defines how the input block is divided, permuted, and combined with the key and the round function in each round of encryption or decryption.
- The round function defines how the key and the input block are mixed to produce an output block in each round.
- The number of rounds, the key size, and the block size are important parameters that affect the security and efficiency of a block cipher.
- The most common structure for block ciphers is the Feistel structure, which consists of splitting the input block into two halves, applying a round function to one half and XORing it with the other half, and then swapping the halves. This process is repeated for a number of rounds, with different subkeys derived from the main key in each round.
- The most widely used block cipher is the Data Encryption Standard (DES), which has a 64-bit block size, a 56-bit key size, and 16 rounds of Feistel structure. DES is considered insecure today due to its small key size and vulnerability to differential cryptanalysis.
- A variant of DES is the Triple DES (3DES), which applies DES three times with two or three different keys, effectively increasing the key size to 112 or 168 bits. 3DES is more secure than DES, but also slower and less efficient.
- A modern block cipher that is widely adopted is the Advanced Encryption Standard (AES), which has a 128-bit block size, and a variable key size of 128, 192, or 256 bits. AES has a different structure than Feistel, called the substitution-permutation network (SPN), which consists of four operations: byte substitution, row shift, column mix, and key addition. AES has 10, 12, or 14 rounds, depending on the key size.
- A block cipher can be used in different modes of operation, which define how the plaintext is divided into blocks, how the ciphertext is produced from the blocks, and how the initialization vector (IV) is used to add randomness and prevent repetition. Some common modes of operation are: electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR).
- A block cipher can also be used to construct a stream cipher, which encrypts and decrypts each bit or byte of the plaintext individually, by using the block cipher to generate a keystream that is XORed with the plaintext. A stream cipher can be synchronous or self-synchronizing, depending on how the keystream is generated and updated.



# Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using a complex substitution function that depends on the key and the plaintext.
- Diffusion can be achieved by using a permutation function that spreads the influence of each plaintext bit over many ciphertext bits.
- A cipher that has both confusion and diffusion is more resistant to linear and differential cryptanalysis.
- A common way to implement confusion and diffusion is to use a fiestal structure, which alternates substitution and permutation layers in multiple rounds.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of fiestal structure for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security. Here is the content I have generated for you in markdown format:

```markdown
# Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

## Security Attacks, Services and Mechanism
- Security attacks are any actions that compromise the security of information or systems.
- Security services are the countermeasures that provide protection against security attacks.
- Security mechanism are the methods or tools that implement security services.
- Security attacks can be classified into two categories: passive attacks and active attacks.
  - Passive attacks are those that do not alter the data or system, but only observe or analyze them. Examples are eavesdropping, traffic analysis, or ciphertext-only attack.
  - Active attacks are those that modify the data or system, or create false data or messages. Examples are replay, modification, or denial-of-service attack.
- Security services can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation.
  - Confidentiality is the service that ensures that the data or system is not disclosed to unauthorized parties.
  - Integrity is the service that ensures that the data or system is not modified or corrupted by unauthorized parties.
  - Availability is the service that ensures that the data or system is accessible and usable by authorized parties.
  - Authentication is the service that ensures that the identity of the parties involved in a communication or transaction is verified.
  - Non-repudiation is the service that ensures that the parties involved in a communication or transaction cannot deny their participation or the validity of the data or message.
- Security mechanism can be classified into two categories: preventive mechanism and detective mechanism.
  - Preventive mechanism are those that prevent or deter security attacks from happening. Examples are encryption, digital signature, or access control.
  - Detective mechanism are those that detect or identify security attacks that have happened or are happening. Examples are intrusion detection, audit trail, or checksum.

## Classical Encryption Techniques
- Encryption is the process of transforming plaintext (the original message) into ciphertext (the encrypted message) using a secret key.
- Decryption is the reverse process of encryption, transforming ciphertext back into plaintext using the same or a different secret key.
- Cryptography is the study of encryption and decryption techniques and their applications.
- Cryptanalysis is the study of breaking encryption techniques and recovering plaintext from ciphertext without knowing the secret key.
- Cryptology is the combination of cryptography and cryptanalysis.
- Classical encryption techniques are the encryption techniques that were developed before the advent of computers and modern cryptography. They are based on simple mathematical operations and can be performed by hand or with simple machines.
- Classical encryption techniques can be classified into two categories: substitution ciphers and transposition ciphers.
  - Substitution ciphers are those that replace each letter or symbol of the plaintext with a different letter or symbol of the ciphertext according to a fixed rule or a lookup table. Examples are Caesar cipher, monoalphabetic cipher, or polyalphabetic cipher.
  - Transposition ciphers are those that rearrange the order of the letters or symbols of the plaintext to form the ciphertext according to a fixed pattern or a key. Examples are rail fence cipher, columnar transposition cipher, or permutation cipher.

## Steganography
- Steganography is the art and science of hiding information within other information, such that the existence of the hidden information is not noticeable or detectable.
- Steganography is different from encryption, as encryption only obscures the meaning of the information, but not its presence.
- Steganography can be used to enhance the security of encryption, by hiding the ciphertext within other data, such as images, audio, or video.
- Steganography can also be used for other purposes, such as watermarking, digital fingerprinting, or covert communication.
- Steganography can be classified into two categories

```




### Data encryption standard(DES)

- Data encryption standard (DES) is a **symmetric-key** algorithm for the encryption of digital data    .
- Symmetric-key algorithms use the **same key** for encryption and decryption    .
- DES encrypts data in **blocks** of size of **64 bits** each, which means 64 bits of plain text go as the input to DES, which produces 64 bits of ciphertext  .
- DES uses a **key length** of **56 bits**, which is divided into eight 7-bit subkeys and one parity bit for each subkey    .
- DES is an implementation of a **Feistel cipher**, which is a structure that divides the input block into two halves and applies a series of rounds of substitution and permutation operations on them  .
- DES uses **16 rounds** of Feistel structure, where each round uses a different subkey derived from the main key   .
- DES also uses an **initial permutation** and a **final permutation** on the input and output blocks, respectively, which are the inverse of each other  .
- DES is based on the principles of **confusion and diffusion**, which are proposed by Claude Shannon to make a cipher secure  .
- Confusion means that the relationship between the key and the ciphertext should be complex and obscure, which is achieved by using **nonlinear substitution** functions called S-boxes in DES  .
- Diffusion means that the influence of one bit of plaintext or key should spread to many bits of ciphertext, which is achieved by using **permutation** functions called P-boxes in DES  .
- DES was adopted as a standard by the National Institute of Standards and Technology (NIST) in 1977 for government agencies to protect sensitive data  .
- DES was officially retired in 2005, as it was found to be insecure against **brute-force attacks** and **differential cryptanalysis**  .
- Brute-force attacks are possible because of the short key length of 56 bits, which can be searched exhaustively by modern computers  .
- Differential cryptanalysis is a technique that exploits the statistical properties of the S-boxes and the Feistel structure to recover the key from a large number of plaintext-ciphertext pairs  .
- A variant of DES called **Triple DES** (3DES) was proposed to increase the security of DES by using three keys and three rounds of encryption    .
- 3DES has a key length of 168 bits, but its effective key length is 112 bits, as the third key is used to decrypt the second round, which is equivalent to encrypting with the first key again    .
- 3DES is more secure than DES, but it is also slower and more complex    .
- DES and 3DES can be used in different **modes of operation**, which define how to encrypt multiple blocks of data  .
- The most common modes of operation are **electronic codebook (ECB)**, **cipher block chaining (CBC)**, **cipher feedback (CFB)**, and **output feedback (OFB)**  .
- ECB mode encrypts each block independently with the same key, which makes it simple but also vulnerable to **



# Strength of DES

- Data Encryption Standard (DES) is a symmetric key block cipher algorithm that encrypts data in 64-bit blocks using a 56-bit key .
- The strength of DES depends on two factors: the key size and the nature of the algorithm.
- The key size of 56 bits is considered too small by modern standards, as it can be brute-forced by trying all possible 2^56 combinations of bits . The first successful brute-force attack on DES was performed in 1998 by the Electronic Frontier Foundation, using a specially designed machine that cost $250,000 and took 56 hours to find the key .
- The nature of the algorithm is based on a Feistel network, which consists of 16 rounds of permutation and substitution operations, each using a different 48-bit subkey derived from the main key . The algorithm also uses the concepts of confusion and diffusion, proposed by Shannon, to make the ciphertext depend on every bit of the plaintext and the key .
- The strength of the algorithm is also affected by the existence of various cryptanalytic techniques, such as differential cryptanalysis and linear cryptanalysis, that exploit the statistical properties of the cipher and reduce the number of keys that need to be tried . These techniques can reduce the effective key size of DES to about 43 bits, which means that only 2^43 keys need to be tested to break the cipher.
- To increase the security of DES, several variants have been proposed, such as Triple DES (3DES), which applies DES three times with different keys, effectively increasing the key size to 112 or 168 bits. However, 3DES is also considered obsolete by modern standards, as it is slow and vulnerable to certain attacks that exploit the block size of 64 bits.
- DES is still widely used in legacy systems and applications, but it is recommended to use more secure and efficient algorithms, such as Advanced Encryption Standard (AES), which has a block size of 128 bits and a key size of 128, 192, or 256 bits. AES is also based on a Feistel network, but uses a different structure and operations than DES. AES is considered to be resistant to all known attacks and is the current standard for symmetric key encryption.



### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It operates by taking many pairs of plaintexts with fixed xor difference, and looking at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys. As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- It is usually launched as an adaptive chosen plaintext attack; the attacker chooses the plaintext to be encrypted (but does not know the key) and then encrypts related plaintexts.
- It studies how the differences evolve through the various rounds and various operations of the cipher.
- It is based on the assumption that the exclusive-or (XOR) operation is the difference operation.
- It can be used to find weaknesses in the design of block ciphers, such as DES, and to mount attacks on reduced-round versions of them .



### Block Cipher Modes of Operation

A block cipher is a symmetric key encryption algorithm that operates on a fixed-size block of plaintext and produces a ciphertext of the same size. A block cipher by itself can only encrypt one block at a time, so a mode of operation is needed to specify how to use the block cipher for encrypting longer messages or data streams. A mode of operation also provides additional security services, such as confidentiality, integrity, or authentication. 

There are several modes of operation for block ciphers, each with different advantages and disadvantages. Some of the most common modes are:

- Electronic Codebook (ECB) mode: This mode encrypts each block of plaintext independently with the same key. This mode is simple and fast, but it is not secure for messages that have repeated blocks or patterns, as they will produce identical ciphertext blocks. This mode also does not provide any error propagation or diffusion.  
- Cipher Block Chaining (CBC) mode: This mode encrypts each block of plaintext by XORing it with the previous ciphertext block, and then applying the block cipher with the same key. This mode provides error propagation and diffusion, as any change in a ciphertext block will affect all the subsequent blocks. This mode also avoids the problem of repeated blocks or patterns, as each block depends on the previous one. However, this mode requires an initialization vector (IV) to start the encryption, and the IV must be random and unpredictable. This mode also does not provide any parallelism, as each block depends on the previous one.  
- Cipher Feedback (CFB) mode: This mode encrypts a message by breaking it into segments of size s bits, where s is smaller than or equal to the block size of the cipher. The first segment is XORed with the encryption of the IV, and the result is the first ciphertext segment. The next segment is XORed with the encryption of the previous ciphertext segment, and so on. This mode provides error propagation and diffusion, as any change in a ciphertext segment will affect all the subsequent segments. This mode also avoids the problem of repeated segments or patterns, as each segment depends on the previous one. However, this mode requires an IV to start the encryption, and the IV must be random and unpredictable. This mode also does not provide any parallelism, as each segment depends on the previous one.  
- Output Feedback (OFB) mode: This mode encrypts a message by breaking it into segments of size s bits, where s is smaller than or equal to the block size of the cipher. The first segment is XORed with the encryption of the IV, and the result is the first ciphertext segment. The next segment is XORed with the encryption of the encryption of the IV, and so on. This mode provides diffusion, as any change in a ciphertext segment will affect all the subsequent segments. This mode also avoids the problem of repeated segments or patterns, as each segment depends on a different encryption of the IV. However, this mode requires an IV to start the encryption, and the IV must be random and unpredictable. This mode also does not provide any error propagation, as any change in a ciphertext segment will not affect the previous segments. This mode also provides parallelism, as each segment can be encrypted independently.  
- Counter (CTR) mode: This mode encrypts a message by breaking it into segments of size s bits, where s is smaller than or equal to the block size of the cipher. The first segment is XORed with the encryption of a counter value, and the result is the first ciphertext segment. The next segment is XORed with the encryption of the incremented counter value, and so on. This mode provides diffusion, as any change in a ciphertext segment will affect all the subsequent segments. This mode also avoids the problem of repeated segments or patterns, as each segment depends on a different encryption of the counter value. However, this mode requires a counter value to start the encryption, and the counter value must be random and unpredictable. This mode also does not provide any error propagation, as any change in a ciphertext segment will not affect the previous segments. This mode also provides parallelism, as each segment can be encrypted independently.  

These are some of the most common modes of operation for block ciphers, but there are also other modes that provide different security services or features, such as authenticated encryption, padding, or format-preserving encryption.  [^



### Triple DES

- Triple DES is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block .
- Triple DES was designed to increase the key size of DES, which was vulnerable to brute-force attacks, without the need to design a new block cipher algorithm .
- Triple DES uses three 56-bit keys, resulting in a 168-bit key length. However, due to the meet-in-the-middle attack, the effective security of Triple DES is only 112 bits .
- Triple DES can operate in different modes, such as:

  - Electronic Codebook (ECB): Each block is encrypted independently with the same key.
  - Cipher Block Chaining (CBC): Each block is XORed with the previous ciphertext block before being encrypted with the key.
  - Cipher Feedback (CFB): The previous ciphertext block is encrypted with the key and XORed with the current plaintext block to produce the ciphertext block.
  - Output Feedback (OFB): A keystream is generated by encrypting an initialization vector with the key and XORing it with the plaintext block to produce the ciphertext block.
  - Counter (CTR): A counter value is encrypted with the key and XORed with the plaintext block to produce the ciphertext block.

- Triple DES is considered to be secure against most attacks, except for some theoretical attacks that require a large amount of data and computation. However, Triple DES is also slow and inefficient compared to newer block ciphers, such as AES .



# Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

## Group
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A group is abelian if the binary operation is also commutative.
- Examples of groups are the integers with addition, the nonzero rational numbers with multiplication, and the set of permutations of a finite set with composition.

## Field
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as the distributive property.
- A field is finite if it has a finite number of elements.
- Examples of fields are the rational numbers, the real numbers, and the complex numbers with the usual addition and multiplication.

## Finite field of the form GF(p)
- A finite field of the form GF(p), where p is a prime number, is simply the ring of integers modulo p, that is, the set {0, 1, ..., p-1} with the arithmetic operations modulo p .
- In GF(p), every nonzero element has a multiplicative inverse, and the addition and multiplication are both commutative and associative .
- Examples of finite fields of the form GF(p) are GF(2), GF(3), and GF(5) .

## Modular arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- Modular arithmetic is useful for cryptography, as it allows for operations that are easy to perform but hard to reverse.
- Examples of modular arithmetic are clock arithmetic, where the modulus is 12 or 24, and the residue classes of integers modulo a prime number, where the modulus is the prime number.

## Prime and relative prime numbers
- A prime number is a positive integer that has exactly two positive divisors, namely 1 and itself.
- A relative prime number, or a coprime number, is a positive integer that shares no common positive divisors with another positive integer, except for 1.
- Examples of prime numbers are 2, 3, 5, 7, 11, and 13.
- Examples of relative prime numbers are 8 and 15, 21 and 22, and 35 and 48.

## Extended Euclidean Algorithm
- The Extended Euclidean Algorithm is an algorithm that computes the greatest common divisor (gcd) of two positive integers, as well as the coefficients of the Bézout's identity, which states that the gcd can be expressed as a linear combination of the two integers.
- The Extended Euclidean Algorithm is useful for cryptography, as it allows for finding the multiplicative inverse of an element modulo a prime number, which is needed for some encryption and decryption schemes.
- An example of the Extended Euclidean Algorithm is the following: to find the gcd of 240 and 46, and the coefficients of the Bézout's identity, we perform the following steps:

```
240 = 5 * 46 + 10
46 = 4 * 10 + 6
10 = 1 * 6 + 4
6 = 1 * 4 + 2
4 = 2 * 2 + 0
```

- The last nonzero remainder is the gcd, which is 2 in this case.
- To find the coefficients of the Bézout's identity, we work backwards from the equations above:

```
2 = 6 - 1 * 4
2 = 6 - 1 * (10 - 1 * 6)
2 = 2 * 6 - 1 * 10
2 = 2 * (46 - 4 * 10) - 1 * 10
2 = 2 * 46 - 9 * 10

```




# Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse .
- A group is called abelian if it also satisfies the property of commutativity, that is, for any two elements a and b in the group, a * b = b * a, where * is the group operation .
- A group is called cyclic if it can be generated by a single element, that is, there exists an element g in the group such that every element in the group can be written as a power of g .
- A group is called finite if it has a finite number of elements, otherwise it is called infinite .
- A subgroup is a subset of a group that is itself a group under the same operation .
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of closure, associativity, commutativity, identity, inverse, distributivity and zero-divisor .
- A field is called finite if it has a finite number of elements, otherwise it is called infinite .
- A finite field of the form GF(p) is a field with p elements, where p is a prime number .
- Modular arithmetic is a system of arithmetic where numbers are reduced modulo a fixed positive integer called the modulus .
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself .
- Two numbers are called relatively prime or coprime if they have no common positive divisors other than 1 .
- The Extended Euclidean Algorithm is an algorithm that computes the greatest common divisor of two numbers and also finds the coefficients of the linear combination that expresses the gcd as a function of the two numbers .
- The Advanced Encryption Standard (AES) is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits using a secret key of 128, 192 or 256 bits .
- The AES encryption and decryption process consists of four main steps: key expansion, initial round, main rounds and final round .
- Each step involves various operations such as substitution, permutation, addition and multiplication on the data and the key .
- Fermat's theorem states that if p is a prime number and a is any integer, then a^p - a is divisible by p .
- Euler's theorem states that if a and n are relatively prime, then a^phi(n) = 1 (mod n), where phi(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n .
- Primality testing is the problem of determining whether a given number is prime or composite .
- There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc .
- The Chinese Remainder theorem states that if n1, n2, ..., nk are pairwise coprime positive integers and a1, a2, ..., ak are any integers, then there exists a unique integer x such that x = a1 (mod n1), x = a2 (mod n2), ..., x = ak (mod nk), where x is in the range [0, n1 * n2 * ... * nk - 1] .
- The Discrete Logarithm Problem is the problem of finding an integer x such that



### Notes for Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. A group is **abelian** if it also satisfies commutativity. Examples of groups are the integers with addition, the nonzero integers modulo p with multiplication, and the set of permutations with composition.
- A **field** is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as the distributive property. A field is **finite** if it has a finite number of elements. Examples of fields are the rational numbers, the real numbers, and the integers modulo p for any prime p.
- A **finite field of the form GF(p)** is a field with p elements, where p is a prime number. The elements are the integers from 0 to p-1, and the operations are performed modulo p. For example, GF(5) is the field with elements {0, 1, 2, 3, 4} and operations modulo 5. In GF(5), 4 + 3 = 2, 4 - 3 = 1, 4 x 3 = 2, and 4 / 3 = 3 (since 3 is the multiplicative inverse of 4 modulo 5).
- **Modular arithmetic** is a system of arithmetic where numbers are reduced to a fixed range by taking the remainder after division by a fixed number, called the modulus. For example, in modulo 12 arithmetic, 15 is equivalent to 3, since 15 mod 12 = 3. Modular arithmetic is useful for cryptography, since it allows operations to be performed on large numbers without overflow, and it also provides a level of security by hiding the original numbers.
- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19 are prime numbers. Prime numbers are important for cryptography, since they are the building blocks of the integers, and many cryptographic algorithms rely on the difficulty of factoring large numbers into primes.
- Two numbers are **relatively prime** or **coprime** if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, since their only common divisor is 1. Two numbers are relatively prime if and only if their greatest common divisor (GCD) is 1. Relatively prime numbers are useful for cryptography, since they ensure that certain operations have unique inverses and solutions.
- The **Extended Euclidean Algorithm** is an algorithm that computes the GCD of two numbers, as well as the coefficients of a linear combination of the two numbers that equals the GCD. For example, the GCD of 30 and 18 is 6, and the Extended Euclidean Algorithm can find that 6 = 2 x 30 - 3 x 18. The Extended Euclidean Algorithm is useful for cryptography, since it can be used to find the multiplicative inverse of a number modulo another number, which is needed for encryption and decryption.
- The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192, or 256 bits. The AES algorithm consists of several rounds of substitution, permutation, mixing, and key addition operations, which transform the plaintext into ciphertext and vice versa. The AES algorithm is widely used for cryptography, since it is considered to be secure, efficient, and standardized.
- **Fermat's theorem** states that if p is a prime number and a is any integer, then a^p - a is divisible by p. In other words, a^p mod p = a mod p. For example, 3^5 - 3 = 240, which is divisible by 5. Fermat's theorem is useful for cryptography, since it can be used to test whether a number is prime or not, by



### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p    .
- GF(p) is defined as the set of integers {0, 1, ..., p-1} together with arithmetic operations modulo p, i.e., the remainder when dividing by p    .
- For example, GF(5) is the set {0, 1, 2, 3, 4} with arithmetic operations modulo 5. The addition and multiplication tables for GF(5) are shown below:

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

- In GF(p), every nonzero element has a multiplicative inverse, i.e., an element that when multiplied by it gives 1. For example, in GF(5), the inverse of 2 is 3, because 2 x 3 = 6 = 1 (mod 5)   .
- The multiplicative inverse of an element a in GF(p) can be found using the extended Euclidean algorithm, which finds integers x and y such that ax + py = 1. Then, x is the inverse of a (mod p)   .
- Finite fields of the form GF(p) are important in cryptography because they provide a mathematical structure for performing operations on data that are resistant to certain attacks. For example, the Advanced Encryption Standard (AES) uses finite fields of the form GF(2^8^) to encrypt and decrypt data  .



Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of modular arithmetic for the Unit 2.

### Modular arithmetic

- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus.
- The modulus is denoted by a positive integer m, and the set of all integers that are congruent modulo m is denoted by Z_m.
- Two integers a and b are said to be congruent modulo m, written as a ≡ b (mod m), if they have the same remainder when divided by m. For example, 17 ≡ 5 (mod 12) because both 17 and 5 have the same remainder of 5 when divided by 12.
- Congruence modulo m is an equivalence relation, meaning that it satisfies the following properties:
  - Reflexive: a ≡ a (mod m) for any integer a.
  - Symmetric: if a ≡ b (mod m), then b ≡ a (mod m).
  - Transitive: if a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m).
- Congruence modulo m also preserves the operations of addition, subtraction, and multiplication, meaning that the following properties hold:
  - If a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m).
  - If a ≡ b (mod m) and c ≡ d (mod m), then a - c ≡ b - d (mod m).
  - If a ≡ b (mod m) and c ≡ d (mod m), then a * c ≡ b * d (mod m).
- However, congruence modulo m does not preserve the operation of division, meaning that the following property does not hold in general:
  - If a ≡ b (mod m) and c ≡ d (mod m), then a / c ≡ b / d (mod m).
- This is because division by zero is undefined, and some integers may not have a multiplicative inverse modulo m. For example, 2 / 4 ≡ 1 / 2 (mod 6), but 2 and 4 do not have multiplicative inverses modulo 6, so the equation does not make sense.
- A multiplicative inverse of an integer a modulo m is an integer b such that a * b ≡ 1 (mod m). For example, 3 is a multiplicative inverse of 5 modulo 8, because 3 * 5 ≡ 1 (mod 8).
- An integer a has a multiplicative inverse modulo m if and only if a and m are coprime, meaning that they have no common factors other than 1. For example, 6 and 9 are not coprime, because they have a common factor of 3, so 6 does not have a multiplicative inverse modulo 9.
- The set of all integers that have a multiplicative inverse modulo m is denoted by Z_m^*. For example, Z_8^* = {1, 3, 5, 7}.
- The size of Z_m^* is given by Euler's totient function, denoted by φ(m), which counts the number of positive integers less than or equal to m that are coprime to m. For example, φ(8) = 4, because there are 4 positive integers less than or equal to 8 that are coprime to 8, namely 1, 3, 5, and 7.
- Euler's totient function has some useful properties, such as:
  - If p is a prime number, then φ(p) = p - 1, because every positive integer less than p is coprime to p.
  - If p and q are distinct prime numbers, then φ(p * q) = (p - 1) * (q - 1), because every positive integer less than p * q is either coprime to both p and q, or divisible by either p or q, but not both.
  - If m and n are coprime, then φ(m * n) = φ(m) * φ(n), because every positive integer less than m * n is either coprime to both m and n, or divisible by a common factor of m and n, which is 1.
- Modular arithmetic is useful for many applications in cryptography, such as encryption, decryption, digital signatures, and



# Prime and Relative Prime Numbers

## Prime Numbers

- A prime number is a whole number greater than 1 whose only factors are 1 and itself .
- For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc. are prime numbers .
- A prime number cannot be written as a product of two smaller positive integers .
- A prime number has exactly two positive divisors: 1 and itself .

## Relative Prime Numbers

- When two numbers have no common factors other than 1, they are said to be relatively prime   .
- In other words, no number other than 1 can divide them both exactly (without any remainder)   .
- Relatively prime numbers are also called “coprime numbers” or “mutually prime numbers”   .
- Two numbers m and n are said to be relatively prime if GCF (m, n) = 1   .
- For example, 8 and 15 are relatively prime because their only common factor is 1   .
- Any two prime numbers are always relatively prime .
- A prime number is relatively prime with any other number because prime numbers are the numbers that can be divided by one or themselves .

## Properties of Relative Prime Numbers

- If n is a prime number, then all integers less than or equal to n are relatively prime to n.
- If a and b are two relatively prime numbers, then a + b is relatively prime to a × b.
- If a and b are relatively prime numbers, then HCF (a, b) = 1 and LCM (a, b) = a × b.



### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful for computing multiplicative inverses in modular structures, such as the modular integers and the finite fields. A multiplicative inverse of a modulo n is an integer x such that ax = 1 mod n, where a and n are coprime, i.e., gcd(a,n) = 1.
- The extended Euclidean algorithm can also be used to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

#### Algorithm

- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works as follows:

  - If a = 0, then gcd(a,b) = b and we can stop.
  - If b = 0, then gcd(a,b) = a and we can stop.
  - Write a in quotient remainder form: a = bq + r, where q and r are integers and 0 <= r < b.
  - Find gcd(b,r) using the Euclidean algorithm, since gcd(a,b) = gcd(b,r).

- The extended Euclidean algorithm keeps track of the quotients and the remainders in each step of the Euclidean algorithm, and uses them to compute x and y in Bézout's identity. The algorithm works as follows:

  - Initialize x0 = 1, y0 = 0, x1 = 0, y1 = 1, r0 = a, r1 = b.
  - Repeat until r1 = 0:
    - Write r0 in quotient remainder form: r0 = r1q + r2, where q and r2 are integers and 0 <= r2 < r1.
    - Update x2 = x0 - qx1, y2 = y0 - qy1, r2 = r0 - qr1.
    - Set x0 = x1, y0 = y1, x1 = x2, y1 = y2, r0 = r1, r1 = r2.
  - Return x0, y0, r0 as the solution.

#### Example

- Suppose we want to find x and y such that 99x + 78y = gcd(99,78) using the extended Euclidean algorithm. We have:

  - x0 = 1, y0 = 0, x1 = 0, y1 = 1, r0 = 99, r1 = 78.
  - r0 = r1q + r2, where q = 1 and r2 = 21. So, x2 = x0 - qx1 = 1 - 0 = 1, y2 = y0 - qy1 = 0 - 1 = -1, r2 = r0 - qr1 = 99 - 78 = 21.
  - x0 = x1 = 0, y0 = y1 = 1, x1 = x2 = 1, y1 = y2 = -1, r0 = r1 = 78, r1 = r2 = 21.
  - r0 = r1q + r2, where q = 3 and r2 = 15. So, x2 = x0 - qx1 = 0 - 3(1) = -3, y2 = y0 - qy1 = 1 - 3(-1) = 4, r2 = r0 - qr1 = 78 - 3(21) = 15.
  - x0 = x1 = 1, y0 = y1 = -1, x1 = x2 = -3, y1 = y2 = 4, r0 = r1 = 21, r1 = r2 = 15



Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here is some content on the topic of Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem.

### Advanced Encryption Standard (AES) encryption and decryption

- The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt information using the same key  .
- AES operates on blocks of 128 bits, and can use keys of 128, 192, or 256 bits. The number of rounds of encryption and decryption depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys .
- Each round consists of four steps: byte substitution, row shift, column mix, and key addition. The last round omits the column mix step .
- Byte substitution replaces each byte in the block with another byte from a predefined table called the S-box. This provides confusion and non-linearity to the cipher .
- Row shift cyclically shifts each row of the block by a different amount. This provides diffusion and permutation to the cipher .
- Column mix multiplies each column of the block by a fixed matrix. This provides diffusion and linear transformation to the cipher .
- Key addition adds the round key to the block using bitwise XOR. The round key is derived from the original key using a key expansion algorithm. This provides confusion and key dependency to the cipher .
- To decrypt a block, the inverse steps are applied in reverse order: key addition, column mix, row shift, and byte substitution. The inverse steps use different tables and matrices from the encryption steps .
- AES is a widely used and secure algorithm that can protect electronic data from unauthorized access. It is approved by the U.S. government and many other standards organizations  .

### Fermat's and Euler's theorem

- Fermat's theorem (or Fermat's little theorem) states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p; that is, a^(p-1) ≡ 1 (mod p)   .
- Euler's theorem (or Euler's totient theorem) is a generalization of Fermat's theorem that applies to any positive integer n and any integer a that is coprime to n (that is, they have no common factors other than 1). It states that a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function, which counts the number of positive integers less than or equal to n that are coprime to n   .
- For example, φ(12) = 4, because the positive integers less than or equal to 12 that are coprime to 12 are 1, 5, 7, and 11. Therefore, for any integer a that is coprime to 12, a^4 ≡ 1 (mod 12).
- Fermat's theorem is a special case of Euler's theorem when n is a prime number, because φ(p) = p - 1 for any prime p   .
- Both Fermat's and Euler's theorems are useful in number theory and cryptography, especially in the RSA algorithm, which is based on the difficulty of finding the modular inverse of large numbers   .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography & Network Security:

### Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity, and non-zero inverses. For example, the set of rational numbers with addition and multiplication is a field.
- A finite field is a field that has a finite number of elements. For example, the set of integers modulo a prime number p, denoted by GF(p), is a finite field with p elements.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range by taking the remainder after division by a modulus. For example, in modulo 12 arithmetic, 15 is equivalent to 3, since 15 mod 12 = 3.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers.
- Two numbers are relatively prime if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, since their only common divisor is 1.
- The Extended Euclidean Algorithm is a method to find the greatest common divisor (gcd) of two numbers, as well as the coefficients of a linear combination that expresses the gcd as a function of the two numbers. For example, the gcd of 30 and 18 is 6, and 6 = 2 * 30 - 3 * 18, so the coefficients are 2 and -3.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that encrypts and decrypts data in 128-bit blocks using a secret key of 128, 192, or 256 bits.
- AES encryption consists of four stages: AddRoundKey, SubBytes, ShiftRows, and MixColumns, that are repeated for a number of rounds depending on the key size. The final round omits the MixColumns stage.
- AES decryption consists of the inverse stages: InvMixColumns, InvShiftRows, InvSubBytes, and AddRoundKey, that are repeated for the same number of rounds as encryption. The first round omits the InvMixColumns stage.
- AddRoundKey is a stage where the current state of the data is XORed with a round key derived from the secret key using a key expansion algorithm.
- SubBytes is a stage where each byte of the state is replaced by another byte according to a substitution table called the S-box.
- ShiftRows is a stage where each row of the state is cyclically shifted to the left by a certain number of positions.
- MixColumns is a stage where each column of the state is multiplied by a fixed matrix using finite field arithmetic.
- InvMixColumns, InvShiftRows, and InvSubBytes are the inverse operations of MixColumns, ShiftRows, and SubBytes, respectively, using different tables or matrices.

### Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem

- Fermat's theorem states that if p is a prime number and a is any integer not divisible by p, then a^(p-1) is congruent to 1 modulo p. For example, if p = 7 and a = 3, then 3^6 = 729 is congruent to 1 modulo 7, since 729 mod 7 = 1.
- Euler's theorem generalizes Fermat's theorem to any modulus n and any integer a that is relatively prime to n. It states that a^(phi(n)) is congruent to 1 modulo n, where phi(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n. For example, if n = 12 and a = 5, then 5^4 = 625 is congruent to 1 modulo 12, since phi(12) = 4 and 625 mod 12 = 1.
- Prim



### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- In other words, the theorem says that if n ≡ a_i (mod m_i) for i = 1, 2, ..., k, where m_i are pairwise coprime, then there exists a unique solution n (mod M), where M = m_1 m_2 ... m_k, and n can be found by the formula:

n = ∑_{i=1}^k a_i M_i (M_i^{-1} mod m_i) (mod M)

where M_i = M / m_i and M_i^{-1} is the multiplicative inverse of M_i modulo m_i .

- The Chinese remainder theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers. It is also useful for solving systems of congruences and for cryptography .



### Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log<sub>g</sub>h in finite groups G is to raise g to larger and larger powers k until the desired h is found. This is called the **brute-force** or **exhaustive search** algorithm.
- The brute-force algorithm has a time complexity of O(|G|) and a space complexity of O(1), where |G| is the order of the group.
- There are some **specialized algorithms** for computing discrete logarithms in certain groups, such as the **Pohlig-Hellman algorithm**, the **Shanks' baby-step giant-step algorithm**, the **Pollard's rho algorithm**, the **Pollard's kangaroo algorithm**, the **index calculus algorithm**, and the **number field sieve algorithm**.
- The specialized algorithms have different time and space complexities depending on the group structure and parameters. For example, the number field sieve algorithm has a time complexity of L<sub>p</sub>(1/3, (64/9)<sup>1/3</sup>) and a space complexity of L<sub>p</sub>(1/3, (32/9)<sup>1/3</sup>), where L<sub>p</sub>(α, c) = exp((c + o(1))(log p)<sup>α</sup>(log log p)<sup>1-α</sup>) and p is the prime modulus of the group.
- The discrete logarithm problem is the basis of many **cryptographic protocols** and **schemes**, such as the **Diffie-Hellman key exchange**, the **ElGamal encryption and signature schemes**, the **Digital Signature Algorithm (DSA)**, and the **Elliptic Curve Cryptography (ECC)** .
- The security of these cryptographic protocols and schemes relies on the assumption that the discrete logarithm problem is hard to solve in the underlying groups, such as the **multiplicative group of integers modulo a large prime** or the **group of points on an elliptic curve** .

