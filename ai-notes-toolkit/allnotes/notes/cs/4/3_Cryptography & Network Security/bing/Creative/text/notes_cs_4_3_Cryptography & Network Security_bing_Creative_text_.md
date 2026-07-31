

## Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

- Security attacks are any actions that compromise the security of information systems and the data they process. They can be classified into two categories: passive attacks and active attacks. Passive attacks are those that do not affect the normal functioning of the system, but only attempt to observe or analyze the data. Active attacks are those that modify or disrupt the system, such as deleting, altering, or injecting data. Examples of passive attacks are eavesdropping, traffic analysis, and cryptanalysis. Examples of active attacks are masquerade, replay, modification, and denial of service.
- Security services are the measures that are taken to protect the system and the data from security attacks. They can be classified into five categories: confidentiality, integrity, availability, authentication, and non-repudiation. Confidentiality is the service that ensures that the data is only accessible to authorized parties. Integrity is the service that ensures that the data is not modified or corrupted by unauthorized parties. Availability is the service that ensures that the system and the data are accessible and usable by authorized parties. Authentication is the service that verifies the identity of the parties involved in a communication. Non-repudiation is the service that prevents the parties from denying their involvement in a communication.
- Security mechanisms are the tools and techniques that are used to implement the security services. They can be classified into two categories: preventive mechanisms and reactive mechanisms. Preventive mechanisms are those that aim to prevent security attacks from happening, such as encryption, digital signatures, access control, and firewalls. Reactive mechanisms are those that aim to detect, recover, or respond to security attacks, such as intrusion detection, audit trails, backups, and alarms.
- Classical encryption techniques are the methods of encrypting and decrypting data that were used before the advent of modern cryptography. They are based on two basic principles: substitution and transposition. Substitution is the principle of replacing each element of the plaintext (the original message) with another element, according to a predefined rule or key. Transposition is the principle of rearranging the elements of the plaintext, according to a predefined rule or key. Examples of substitution ciphers are Caesar cipher, monoalphabetic cipher, and polyalphabetic cipher. Examples of transposition ciphers are rail fence cipher, columnar transposition cipher, and permutation cipher.
- Cryptanalysis is the science of breaking encryption techniques, that is, recovering the plaintext from the ciphertext (the encrypted message) without knowing the key or the rule. Cryptanalysis can be performed by various methods, such as brute force, frequency analysis, known plaintext, chosen plaintext, chosen ciphertext, and differential cryptanalysis.
- Steganography is the art of hiding information within other information, such as images, audio, or video. The goal of steganography is to conceal the existence of the hidden information, rather than its content. Steganography can be combined with encryption to enhance the security of the hidden information. Examples of steganography techniques are least significant bit (LSB) insertion, masking, filtering, and transformation.
- Stream and block ciphers are two types of symmetric encryption techniques, that is, techniques that use the same key for encryption and decryption. Stream ciphers are those that encrypt and decrypt each element of the plaintext individually, such as bits or bytes, using a keystream that is generated from the key and a nonce (a random or unique value). Block ciphers are those that encrypt and decrypt each block of the plaintext, such as 64 bits or 128 bits, using a key and a mode of operation. Examples of stream ciphers are RC4, Salsa20, and ChaCha20. Examples of block ciphers are DES, AES, and Blowfish.
- Modern block ciphers are the block ciphers that are widely used in modern cryptography. They are based on four basic principles: block cipher principles, Shannon’s theory of confusion and diffusion, fiestal structure, and data encryption standard (DES). Block cipher principles are the rules that define how a block cipher operates, such as the block size, the key size, the number of rounds, and the round function. Shannon’s theory



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of Introduction to security attacks for the subject of Cryptography & Network Security. Here is the content I have generated for you in markdown format:

### Introduction to security attacks

- Security attacks are any actions that compromise the security goals of confidentiality, integrity, availability, authenticity, or non-repudiation of information or systems.
- Security attacks can be classified into two categories: passive attacks and active attacks.
- Passive attacks are those that do not alter the data or system, but only observe or analyze it. Examples of passive attacks are eavesdropping, traffic analysis, or ciphertext-only attacks.
- Active attacks are those that modify the data or system, or create false data or messages. Examples of active attacks are replay, modification, deletion, insertion, fabrication, or man-in-the-middle attacks.
- Security attacks can also be classified into four types based on the origin and the target of the attack: interception, interruption, modification, or fabrication.
- Interception is an attack where an unauthorized party gains access to the data or system. Examples of interception are wiretapping, sniffing, or keylogging.
- Interruption is an attack where an authorized party loses access to the data or system. Examples of interruption are denial-of-service, jamming, or cutting.
- Modification is an attack where an unauthorized party alters the data or system. Examples of modification are tampering, changing, or encrypting.
- Fabrication is an attack where an unauthorized party creates false data or messages. Examples of fabrication are spoofing, impersonation, or forgery.



### Services and Mechanism for the Notes of the Unit 1 - Introduction to Security Attacks, Services and Mechanism, Classical Encryption TechniquesSubstitution Ciphers and Transposition Ciphers, Cryptanalysis, Steganography, Stream and Block Ciphers. Modern Block Ciphers: Block Ciphers Principles, Shannon’s Theory of Confusion and Diffusion, Fiestal Structure, Data Encryption Standard(DES), Strength of DES, Idea of Differential Cryptanalysis, Block Cipher Modes of Operations, Triple DES in the Subject of Cryptography & Network Security

- Security Attacks, Services and Mechanism
  - Security Attack: Any action that compromises the security of information owned by an organization.
  - Security Service: A service that enhances the security of data processing systems and information transfers. X.800 divides these services into five categories and fourteen specific services.
  - Security Mechanism: A mechanism that is designed to detect, prevent or recover from a security attack. A security mechanism may be incorporated into the appropriate protocol layer in order to provide some of the OSI security services.
- Classical Encryption Techniques
  - Substitution Cipher: A cipher that replaces each plaintext symbol with a different ciphertext symbol. Examples are Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, etc.
  - Transposition Cipher: A cipher that rearranges the order of the plaintext symbols to form the ciphertext. Examples are rail fence cipher, columnar transposition cipher, etc.
  - Cryptanalysis: The art of breaking ciphers, i.e., recovering the plaintext from the ciphertext without knowing the key. Cryptanalysis can be based on various techniques, such as frequency analysis, known plaintext attack, chosen plaintext attack, etc.
  - Steganography: The art of hiding messages in other messages, such as images, audio, video, etc., so that the existence of the secret message is not revealed. Steganography can be combined with encryption to provide more security.
- Stream and Block Ciphers
  - Stream Cipher: A cipher that encrypts each plaintext symbol (usually a bit) with a different key symbol (usually a bit) generated by a pseudorandom key stream. Examples are RC4, A5/1, A5/2, etc.
  - Block Cipher: A cipher that encrypts a fixed-length block of plaintext (usually 64 or 128 bits) with a fixed-length key (usually 64 or 128 bits) to produce a block of ciphertext of the same length. Examples are DES, AES, IDEA, etc.
- Modern Block Ciphers
  - Block Cipher Principles: The basic principles of designing a block cipher are based on Shannon's theory of confusion and diffusion. Confusion means that the relationship between the plaintext and the ciphertext is obscured by using a complex key-dependent substitution. Diffusion means that the influence of each plaintext bit is spread over many ciphertext bits by using a permutation.
  - Fiestal Structure: A common structure for block ciphers that consists of multiple rounds of encryption, each involving a subkey derived from the main key, a substitution function (S-box) and a permutation function (P-box). Examples are DES, AES, etc.
  - Data Encryption Standard (DES): A widely used block cipher that encrypts 64-bit blocks of plaintext with a 56-bit key using 16 rounds of fiestal structure. DES is vulnerable to brute-force attacks and differential cryptanalysis.
  - Strength of DES: The strength of DES depends on the key size, the number of rounds, and the design of the S-boxes and P-boxes. The key size of 56 bits is too small for modern computing power, and the number of rounds is not enough to provide adequate diffusion. The S-boxes and P-boxes are carefully chosen to resist differential cryptanalysis, but they are not optimal for other types of attacks.
  - Idea of Differential Cryptanalysis: A powerful technique for breaking block ciphers that exploits the statistical properties of the S-boxes and P-boxes. Differential cryptanalysis analyzes the differences between pairs of plaintexts and ciphertexts, and tries to find a differential characteristic that has a high probability of occurrence. Then, it uses the characteristic to recover the subkeys and the main key.
  - Block Cipher Modes of Operation: Different ways of using a block cipher to encrypt a message that is longer than the block size. The modes of operation are Electronic Codebook (



### Classical encryption techniques: substitution ciphers and transposition ciphers

- Classical encryption techniques are the traditional methods of cryptography that use symmetric keys to encrypt and decrypt messages.
- Substitution ciphers and transposition ciphers are two basic types of classical encryption techniques.
- Substitution ciphers replace each character of the plaintext with a different character, number, or symbol, according to a fixed rule or key.
- Transposition ciphers rearrange the order of the characters of the plaintext, according to a fixed rule or key.
- Both substitution ciphers and transposition ciphers can be further classified into mono-alphabetic, poly-alphabetic, or poly-graphic ciphers, depending on whether they use one, multiple, or groups of alphabets to encrypt the plaintext.
- Some examples of substitution ciphers are Caesar cipher, Vigenere cipher, and Playfair cipher.
- Some examples of transposition ciphers are Rail fence cipher, Columnar cipher, and Scytale cipher.
- The main advantage of classical encryption techniques is their simplicity and ease of implementation.
- The main disadvantage of classical encryption techniques is their vulnerability to cryptanalysis, which is the process of breaking the encryption and recovering the plaintext from the ciphertext.
- Cryptanalysis can be performed by various methods, such as frequency analysis, brute force attack, known plaintext attack, chosen plaintext attack, etc.
- Steganography is another classical technique of hiding information, which is different from encryption. Steganography conceals the existence of the message by embedding it in another medium, such as an image, audio, or video file.
- Stream and block ciphers are modern encryption techniques that use binary digits (bits) to encrypt and decrypt messages. Stream ciphers encrypt one bit at a time, while block ciphers encrypt a fixed number of bits at a time.



### Cryptanalysis

Cryptanalysis is the process of analyzing information systems, such as codes, ciphers or encrypted text, in order to understand hidden aspects of the systems or to break their security  . Cryptanalysis is used to decrypt ciphertexts without knowing the key or the algorithm used to encrypt them, or to find weaknesses in cryptographic systems that can be exploited.

Cryptanalysis can be classified into different types, depending on the amount and type of information available to the attacker. Some common types are:

- Ciphertext-only attack: The attacker only has access to one or more ciphertexts, and tries to recover the plaintext or the key.
- Known-plaintext attack: The attacker has access to some plaintext-ciphertext pairs, and tries to recover the key or decrypt other ciphertexts.
- Chosen-plaintext attack: The attacker can choose some plaintexts and obtain their corresponding ciphertexts, and tries to recover the key or decrypt other ciphertexts.
- Chosen-ciphertext attack: The attacker can choose some ciphertexts and obtain their corresponding plaintexts, and tries to recover the key or encrypt other plaintexts.
- Chosen-text attack: The attacker can choose both plaintexts and ciphertexts and obtain their corresponding ciphertexts and plaintexts, and tries to recover the key or perform other operations.

Cryptanalysis can also be classified into different methods, depending on the techniques used to break the cryptographic system. Some common methods are:

- Brute-force attack: The attacker tries all possible keys until finding the correct one.
- Frequency analysis: The attacker analyzes the frequency of symbols or patterns in the ciphertext, and compares them with the expected frequency of the plaintext language, to infer the key or the plaintext.
- Differential cryptanalysis: The attacker analyzes the differences in the ciphertexts produced by small changes in the plaintext or the key, to find correlations or dependencies that reveal the key or the algorithm.
- Linear cryptanalysis: The attacker analyzes the linear relations between the plaintext, the ciphertext and the key bits, to find a linear approximation that holds with high probability and reveals the key or the algorithm.
- Algebraic cryptanalysis: The attacker models the cryptographic system as a system of algebraic equations, and tries to solve them using mathematical techniques, such as Gröbner bases or SAT solvers, to find the key or the plaintext.

Cryptanalysis is an important field of study in cryptography and information security, as it helps to evaluate the security and strength of cryptographic systems, and to design new and more secure systems. Cryptanalysis is also a challenging and fascinating intellectual activity, as it involves creativity, logic, mathematics and computer science.



Hello, I am Sydney, your AI assistant. I can help you with your study material on cryptography and network security. Here is some content on steganography for the notes of the unit 1.

### Steganography

- Steganography is the art and science of hiding information in plain sight, such that only the intended recipient can detect it.
- Steganography can be used to conceal the existence of a secret message, or to enhance the security of an encrypted message by adding another layer of obfuscation.
- Steganography can be applied to various types of media, such as text, images, audio, video, or network traffic.
- Steganography techniques can be classified into two categories: technical and linguistic.
  - Technical steganography uses physical or digital methods to embed the secret information into the cover media, such as modifying the least significant bits of pixels, inserting hidden data into unused file space, or encoding data into network protocols.
  - Linguistic steganography uses natural language processing to hide the secret information in the cover text, such as using synonyms, acronyms, anagrams, or word puzzles.
- Steganography can be combined with cryptography to achieve higher security and confidentiality. For example, the secret message can be encrypted before being hidden into the cover media, or the cover media can be encrypted after hiding the secret message.
- Steganography can be detected and analyzed by using steganalysis techniques, which aim to reveal the presence, location, and content of the hidden information. Steganalysis can be based on statistical, structural, or semantic analysis of the cover media, or on comparing the cover media with a known original or a similar sample.



### Stream and block ciphers

- Stream ciphers and block ciphers are two types of symmetric encryption algorithms that use a secret key to transform plaintext into ciphertext.
- Stream ciphers encrypt one bit or byte of plaintext at a time, while block ciphers encrypt fixed-size blocks of plaintext, usually 64 or 128 bits.
- Stream ciphers are faster and simpler than block ciphers, but they are more vulnerable to attacks such as replay, insertion, deletion, and modification.
- Block ciphers are more secure and versatile than stream ciphers, but they require more computation and memory resources, and they may introduce padding or expansion of the plaintext.
- Stream ciphers can be implemented using linear feedback shift registers (LFSRs), nonlinear feedback shift registers (NLFSRs), or pseudorandom number generators (PRNGs).
- Block ciphers can be implemented using various structures, such as Feistel networks, substitution-permutation networks (SPNs), or balanced Feistel networks (BENs).
- Stream ciphers and block ciphers can be combined to achieve different modes of operation, such as electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), or counter (CTR).
- Stream ciphers and block ciphers can be evaluated based on their security, efficiency, and functionality properties, such as confusion, diffusion, avalanche effect, key size, block size, throughput, latency, parallelism, and flexibility.



### Modern Block Ciphers

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- Block ciphers can be classified into two types: substitution-permutation networks (SPNs) and Feistel networks.
- Substitution-permutation networks consist of several rounds of substitution and permutation operations, where each round uses a different subkey derived from the main key.
- Feistel networks consist of several rounds of splitting, mixing, and swapping operations, where each round uses a different subkey derived from the main key and a function called the round function.
- Shannon's theory of confusion and diffusion states that a good cipher should have two properties: confusion, which means that the relationship between the plaintext and the ciphertext is complex and obscure, and diffusion, which means that a change in one bit of the plaintext or the key affects many bits of the ciphertext.
- Data Encryption Standard (DES) is a widely used block cipher that was standardized by NIST in 1977. It has a block size of 64 bits and a key size of 56 bits. It uses a Feistel network with 16 rounds and a round function that involves expansion, XOR, substitution, and permutation operations.
- The strength of DES lies in its large number of possible keys (2^56) and its resistance to differential cryptanalysis, a technique that exploits the statistical properties of the round function to recover the key. However, DES is vulnerable to brute-force attacks, linear cryptanalysis, and other attacks that exploit its small key size and weak keys.
- Differential cryptanalysis is a technique that analyzes the differences between pairs of plaintexts and ciphertexts to find patterns that reveal information about the key. It is based on the assumption that the round function is not perfectly random and that some differences are more likely to occur than others.
- Block cipher modes of operation are methods of using a block cipher to encrypt or decrypt messages of arbitrary length. They include electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR) modes. Each mode has different advantages and disadvantages in terms of security, efficiency, and error propagation.
- Triple DES (3DES) is a variant of DES that applies the DES algorithm three times with two or three different keys. It has a block size of 64 bits and a key size of 112 or 168 bits. It is more secure than DES, but also slower and less efficient. It is still widely used in legacy systems and applications.



### Block ciphers principles

- A block cipher is a symmetric-key encryption algorithm that operates on a fixed-length group of bits, called a block, and produces a ciphertext block of the same length.
- A block cipher consists of two functions: an encryption function E that maps a plaintext block P and a secret key K to a ciphertext block C, and a decryption function D that maps C and K back to P.
- A block cipher can be represented as E: {0,1}^n x {0,1}^k -> {0,1}^n and D: {0,1}^n x {0,1}^k -> {0,1}^n, where n is the block size and k is the key size.
- A block cipher should satisfy the following properties:
  - Correctness: D(K, E(K, P)) = P for any P and K.
  - Security: Given a ciphertext C, it should be computationally infeasible to find P or K without knowing K.
  - Efficiency: E and D should be fast and easy to implement in hardware or software.
- A block cipher can be designed using different techniques, such as substitution-permutation networks, Feistel networks, or other structures.
- A block cipher can be used in different modes of operation, such as electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), or counter (CTR), to encrypt a message of arbitrary length. Each mode has different advantages and disadvantages in terms of security, efficiency, and error propagation.



### Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using substitution ciphers, which replace each plaintext symbol with a different ciphertext symbol.
- Diffusion can be achieved by using transposition ciphers, which permute the order of the plaintext symbols.
- Confusion and diffusion can be combined by using a fiestal structure, which alternates substitution and transposition operations in multiple rounds.
- A good example of a cipher that uses confusion and diffusion is the Data Encryption Standard (DES), which has 16 rounds of fiestal structure and uses a 56-bit key.



### Fiestal structure for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security

- Security attacks, services and mechanism
  - Security attacks: Any action that compromises the confidentiality, integrity or availability of an information system.
  - Security services: The functions that provide protection to an information system and its users, such as authentication, encryption, access control, etc.
  - Security mechanism: The methods or tools that implement the security services, such as algorithms, protocols, hardware devices, etc.
- Classical encryption techniques
  - Substitution ciphers: A method of encryption that replaces each plaintext symbol with a different ciphertext symbol, according to a fixed rule or key.
  - Transposition ciphers: A method of encryption that rearranges the plaintext symbols in a different order, according to a fixed rule or key.
  - Cryptanalysis: The science of breaking ciphertexts, by finding the plaintext or the key, using various techniques such as frequency analysis, brute force, etc.
  - Steganography: The art of hiding information in another medium, such as images, audio, text, etc., without altering the appearance or functionality of the medium.
- Stream and block ciphers
  - Stream ciphers: A method of encryption that encrypts each plaintext symbol with a different key, generated by a pseudorandom process, such as a keystream generator or a one-time pad.
  - Block ciphers: A method of encryption that encrypts a fixed-length block of plaintext with a fixed-length key, using a mathematical function or a permutation, such as a fiestal structure or a substitution-permutation network.
- Modern block ciphers
  - Block ciphers principles: The basic design principles of block ciphers, such as the block size, the key size, the number of rounds, the round function, etc.
  - Shannon’s theory of confusion and diffusion: The two properties that a block cipher should have to resist cryptanalysis, according to Claude Shannon. Confusion means that the relationship between the plaintext and the ciphertext should be complex and obscure. Diffusion means that a change in one bit of the plaintext or the key should affect many bits of the ciphertext.
  - Fiestal structure: A type of round function that consists of four operations: substitution, permutation, key mixing and swapping. The substitution and permutation provide confusion and diffusion, respectively. The key mixing adds the round key to the block. The swapping exchanges the two halves of the block.
  - Data encryption standard (DES): A widely used block cipher that has a block size of 64 bits, a key size of 56 bits, and 16 rounds of fiestal structure. It was developed by IBM and adopted by the US government in 1977. It is now considered insecure due to its small key size and the advances in cryptanalysis and computing power.
  - Strength of DES: The security of DES depends on the key size, the round function, and the mode of operation. The key size of 56 bits is too small to resist brute force attacks, which can be performed in a few hours by modern computers. The round function of DES is also vulnerable to differential cryptanalysis, which can find the key with less than 2^56 ciphertexts. The mode of operation of DES can affect the security as well, such as the electronic codebook (ECB) mode, which can reveal patterns in the plaintext.
  - Idea of differential cryptanalysis: A type of cryptanalysis that exploits the statistical properties of the round function of a block cipher. It analyzes the difference between two plaintexts and the corresponding difference between their ciphertexts, and tries to find a differential characteristic, which is a sequence of differences that occurs with a high probability. It then uses the differential characteristic to recover the key or some subkeys of the cipher.
  - Block cipher modes of operation: The methods of using a block cipher to encrypt a message that is longer than the block size, or to provide additional security services, such as integrity or authentication. Some common modes of operation are: cipher block chaining (CBC), which chains the ciphertext blocks with an initialization vector (IV); output feedback (OFB), which generates a keystream from the block cipher and the IV; cipher feedback (CFB), which feeds back the ciphertext blocks to the block cipher and the IV; counter (CTR), which encrypts



### Data Encryption Standard (DES)

- Data Encryption Standard (DES) is a **symmetric-key** algorithm for the encryption of digital data    .
- Symmetric-key algorithms use the **same key** for encryption and decryption    .
- DES is a **block cipher** that encrypts data in **blocks of 64 bits** each    .
- DES uses a **56-bit key**, which is derived from a 64-bit key by discarding 8 parity bits    .
- DES is based on the **Feistel structure**, which consists of 16 rounds of processing on the input block  .
- Each round of DES involves four steps: **expansion**, **key mixing**, **substitution**, and **permutation**  .
- Expansion: The 32-bit right half of the input block is expanded to 48 bits by duplicating some bits  .
- Key mixing: The expanded right half is XORed with a 48-bit round key, which is derived from the main key using a **key schedule** algorithm  .
- Substitution: The result of the key mixing is divided into eight 6-bit blocks, each of which is mapped to a 4-bit block using a **substitution box (S-box)**  .
- Permutation: The eight 4-bit blocks are combined and permuted according to a **permutation function (P-function)** to produce a 32-bit output  .
- After 16 rounds, the left and right halves of the output block are swapped and concatenated to form the final 64-bit ciphertext  .
- Decryption is the reverse process of encryption, using the same key but in reverse order    .
- DES was adopted as a standard by the National Institute of Standards and Technology (NIST) in 1977 for government agencies to protect sensitive data  .
- DES was officially retired in 2005, as its short key length made it vulnerable to **brute-force attacks** and **differential cryptanalysis**  .
- DES was replaced by the **Advanced Encryption Standard (AES)**, which uses a longer key and a more complex structure  .
- A variant of DES, called **Triple DES (3DES)**, applies DES three times with different keys to increase the security level  .
- DES can operate in different **modes of operation**, such as **electronic codebook (ECB)**, **cipher block chaining (CBC)**, **cipher feedback (CFB)**, and **output feedback (OFB)**, which affect how the blocks are encrypted and decrypted  .
- DES is one of the most influential algorithms in the history of cryptography, as it stimulated the development of new techniques and standards  .



Hello, I am Sydney, your AI assistant. I can help you with your study material on Cryptography & Network Security. Here is the content on the topic of Strength of DES:

### Strength of DES

- Data Encryption Standard (DES) is a symmetric-key block cipher that operates on 64-bit blocks of plaintext and ciphertext, using a 56-bit key.
- DES was designed to resist various types of cryptanalysis, such as brute-force attacks, differential cryptanalysis, linear cryptanalysis, and related-key attacks.
- The strength of DES depends on several factors, such as the key size, the key schedule, the S-boxes, and the feistel structure.

#### Key size

- The key size of DES is 56 bits, which means that there are 2^56 possible keys to try in a brute-force attack. This was considered adequate in the 1970s, when DES was standardized, but became vulnerable in the 1990s, when faster computers and specialized hardware were developed to break DES.
- In 1998, the Electronic Frontier Foundation (EFF) built a machine called Deep Crack, which could search 90 billion keys per second and break DES in a few days. In 1999, a distributed network of computers called DESCHALL broke DES in 22 hours and 15 minutes.
- To increase the security of DES, a variant called Triple DES (3DES) was proposed, which applies DES three times with two or three different keys, resulting in an effective key size of 112 or 168 bits. 3DES is still widely used today, although it is slower than newer algorithms.

#### Key schedule

- The key schedule of DES is the algorithm that generates 16 subkeys, each of 48 bits, from the 56-bit key. The key schedule involves permuting, shifting, and selecting bits from the key.
- The key schedule of DES is designed to avoid weak keys, which are keys that produce identical or related subkeys, leading to reduced security. For example, a weak key is a key that consists of all zeros or all ones, which produces 16 identical subkeys. There are four weak keys and 12 semi-weak keys in DES, which should be avoided.
- The key schedule of DES is also designed to resist differential cryptanalysis, which is a technique that exploits the differences between two plaintexts and their corresponding ciphertexts, to recover the key. The key schedule of DES ensures that each bit of the key affects many bits of the subkeys, making it harder to trace the differences.

#### S-boxes

- The S-boxes of DES are eight nonlinear substitution tables, each of 6x4 bits, that map 6-bit inputs to 4-bit outputs. The S-boxes are the main source of confusion in DES, which means that they obscure the relationship between the plaintext and the ciphertext.
- The S-boxes of DES are carefully chosen to have certain properties, such as high nonlinearity, high avalanche effect, and high resistance to differential and linear cryptanalysis. The S-boxes of DES are also balanced, which means that they have equal numbers of zeros and ones in their outputs, and have no fixed points or opposite fixed points, which means that they do not map any input to itself or its complement.
- The S-boxes of DES are the most scrutinized part of the algorithm, as they were initially kept secret by the National Security Agency (NSA), which raised suspicions that they contained hidden weaknesses or backdoors. However, subsequent analysis by the cryptographic community has shown that the S-boxes of DES are actually well-designed and secure.

#### Feistel structure

- The feistel structure of DES is a method of constructing block ciphers, which involves splitting the block into two halves, applying a round function to one half using a subkey, and XORing the result with the other half, then swapping the halves. This is repeated for 16 rounds, with the final swap undone.
- The feistel structure of DES has several advantages, such as simplicity, symmetry, and reversibility. The simplicity means that the same round function can be used for encryption and decryption, with only the order of the subkeys reversed. The symmetry means that the two halves of the block are treated equally, which avoids creating weak points. The reversibility means that the decryption can be performed by running the encryption in reverse, which simplifies the implementation and reduces the code size.
- The feistel structure of DES also contributes to the diffusion of the algorithm, which means that a small change in the plaintext or the key affects many bits of the ciphertext. The feistel structure of DES ensures that each bit of the plaintext affects half of the bits of the ciphertext after one round, and all



### Idea of differential cryptanalysis

- Differential cryptanalysis is a general form of cryptanalysis applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- It is the study of how differences in information input can affect the resultant difference at the output.
- It operates by taking many pairs of plaintexts with fixed xor difference, and looking at the differences in the resulting ciphertext pairs.
- Based on these differences, probabilities are assigned to possible keys. As more pairs are analyzed, the probability concentrates around a smaller number of keys.
- It is usually launched as an adaptive chosen plaintext attack; the attacker chooses the plaintext to be encrypted (but does not know the key) and then encrypts related plaintexts.
- It studies how the differences evolve through the various rounds and various operations of the cipher.
- It is based on the assumption that the exclusive-or (XOR) operation is the difference operation.
- It was first introduced by Biham and Shamir in 1990 as a technique to break the Data Encryption Standard (DES) cipher.
- It can also be used to analyze other block ciphers, such as FEAL, Khufu, Khafre, REDOC, LOKI, and GOST.
- It can also be extended to deal with other difference operations, such as modular addition, subtraction, or rotation.



### Block Cipher Modes of Operation

- A block cipher mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity.
- A block cipher by itself is only suitable for the secure cryptographic transformation (encryption or decryption) of one fixed-length group of bits called a block.
- To encrypt or decrypt messages of arbitrary length, different modes of operation are defined, which specify how to apply the block cipher repeatedly to the message.
- There are five types of operations in block cipher modes, ECB (Electronic Code Book) mode, CBC (Cipher Block Chaining) mode, CFB (Cipher Feedback) mode, OFB (Output Feedback) mode and CTR (Counter) mode.
- ECB mode encrypts each block of the message independently with the same key, and is the simplest and most basic mode. It is not secure for messages longer than one block, as identical plaintext blocks produce identical ciphertext blocks.
- CBC mode encrypts each block of the message by XORing it with the previous ciphertext block, and then applying the block cipher. The first block is XORed with an initialization vector (IV), which is a random value. This mode ensures that identical plaintext blocks produce different ciphertext blocks.
- CFB mode encrypts the message by XORing each block of the message with the output of the block cipher applied to the previous ciphertext block. The first block is XORed with the IV. This mode allows the block cipher to act as a stream cipher, and can handle messages of any length.
- OFB mode encrypts the message by XORing each block of the message with the output of the block cipher applied to the IV. The IV is updated by applying the block cipher to it after each encryption. This mode also allows the block cipher to act as a stream cipher, and can handle messages of any length.
- CTR mode encrypts the message by XORing each block of the message with the output of the block cipher applied to a counter. The counter is a value that is incremented by one after each encryption. This mode also allows the block cipher to act as a stream cipher, and can handle messages of any length.
- Different modes of operation have different advantages and disadvantages, such as speed, security, error propagation, parallelizability, and random access.
- The choice of the mode of operation depends on the application and the security requirements.



### Triple DES
- Triple DES (3DES) is a symmetric-key block cipher that applies the Data Encryption Standard (DES) algorithm three times to each data block.
- The key size of 3DES is 168 bits, but due to the meet-in-the-middle attack, the effective security it provides is only 112 bits.
- 3DES is designed to overcome the limitations of the original DES, which has a key size of only 56 bits and is vulnerable to brute-force attacks.
- 3DES has three keying options:
  - Option 1: All three keys are independent. This is the strongest option, providing 168 bits of security, but it requires 3x64 bits of key material.
  - Option 2: K1 and K2 are independent, and K3 = K1. This option provides 112 bits of security, and requires 2x64 bits of key material. This is the most common option in practice.
  - Option 3: All three keys are identical, i.e., K1 = K2 = K3. This option provides backward compatibility with DES, and requires only 64 bits of key material. However, it is not recommended for new applications.
- 3DES uses the following algorithm for encryption and decryption:
  - Encryption: C = E(K3, D(K2, E(K1, P)))
  - Decryption: P = D(K1, E(K2, D(K3, C)))
  - Where P is the plaintext block, C is the ciphertext block, E is the encryption function, D is the decryption function, and K1, K2, K3 are the subkeys.
- 3DES is more secure than DES, but it is also slower and more complex. It is still widely used in applications that require high security and compatibility with legacy systems, such as banking, e-commerce, and government. However, it is being replaced by more efficient and secure algorithms, such as the Advanced Encryption Standard (AES).



## Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A **field** is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity and non-triviality.
- A **finite field** is a field that has a finite number of elements. A finite field of order p, where p is a prime number, is denoted by GF(p) and is defined as the set of integers modulo p with arithmetic operations modulo p  .
- **Modular arithmetic** is a system of arithmetic for integers, where numbers wrap around after reaching a certain value, called the modulus. For example, in modulo 5 arithmetic, 4 + 3 = 2, because 7 is congruent to 2 modulo 5.
- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers.
- Two numbers are **relatively prime** or **coprime** if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, because their only common divisor is 1.
- The **Extended Euclidean Algorithm** is an algorithm that computes the greatest common divisor (gcd) of two numbers, as well as the coefficients of Bézout's identity, which states that there exist integers x and y such that ax + by = gcd(a, b) for any integers a and b.
- The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192 or 256 bits. It consists of several rounds of transformations, such as substitution, permutation, mixing and key addition, to achieve confusion and diffusion.
- **Fermat's theorem** states that if p is a prime number and a is any integer, then a^p - a is divisible by p. Equivalently, a^(p-1) is congruent to 1 modulo p, for any a that is not divisible by p.
- **Euler's theorem** generalizes Fermat's theorem to the case where p is not necessarily prime, but a and p are relatively prime. It states that a^φ(p) is congruent to 1 modulo p, where φ(p) is the Euler's totient function, which counts the number of positive integers less than p that are relatively prime to p.
- **Primality testing** is the problem of determining whether a given number is prime or not. There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc. Some of them are deterministic, meaning they always give the correct answer, while others are probabilistic, meaning they may give a false positive with a small probability.
- The **Chinese Remainder theorem** states that if n1, n2, ..., nk are pairwise coprime positive integers, and a1, a2, ..., ak are any integers, then there exists a unique integer x, modulo the product of n1, n2, ..., nk, such that x is congruent to ai modulo ni, for i = 1, 2, ..., k. Moreover, x can be computed efficiently using the Extended Euclidean Algorithm.
- The **Discrete Logarithmic Problem** is the problem of finding an integer x, given a finite cyclic group G, a generator g of G, and an element h of G, such that g^x = h. This problem is believed to be hard in general, and is the basis of many cryptographic schemes.
- The **principles of public key crypto systems** are the following:



### Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A group is called abelian if it also satisfies the property of commutativity, that is, for any two elements a and b in the group, a*b = b*a.
- A group is called cyclic if it can be generated by a single element, that is, there exists an element g in the group such that every element in the group can be written as a power of g.
- A group is called finite if it has a finite number of elements. The number of elements in a finite group is called its order.
- A subgroup is a subset of a group that is itself a group under the same operation.
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of closure, associativity, commutativity, identity, inverse, distributivity and zero-divisor.
- A field is called finite if it has a finite number of elements. A finite field is also called a Galois field and denoted by GF(p), where p is the order of the field.
- A finite field of order p exists if and only if p is a prime number or a power of a prime number.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range of values by using the remainder operation.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- Two numbers are called relatively prime or coprime if they have no common positive divisors other than 1.
- The Extended Euclidean Algorithm is an algorithm that computes the greatest common divisor of two numbers and also finds the coefficients of a linear combination of the two numbers that equals the greatest common divisor.
- The Advanced Encryption Standard (AES) is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits using a secret key of 128, 192 or 256 bits.
- The AES encryption and decryption process consists of four main steps: key expansion, initial round, main rounds and final round.
- The key expansion step generates a series of round keys from the secret key using a recursive function.
- The initial round step adds the first round key to the plaintext block using a bitwise XOR operation.
- The main rounds step consists of four sub-steps: sub-bytes, shift-rows, mix-columns and add-round-key.
- The sub-bytes step replaces each byte of the state with another byte using a lookup table called the S-box.
- The shift-rows step cyclically shifts each row of the state by a certain number of positions to the left.
- The mix-columns step multiplies each column of the state by a fixed polynomial in GF(2^8)^.
- The add-round-key step adds the round key to the state using a bitwise XOR operation.
- The final round step consists of three sub-steps: sub-bytes, shift-rows and add-round-key.
- The AES decryption process is the reverse of the encryption process, using the inverse operations and the round keys in reverse order.
- Fermat's theorem states that if p is a prime number and a is any integer, then a^p - a is divisible by p.
- Euler's theorem states that if a and n are relatively prime, then a^phi(n) = 1 (mod n), where phi(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n.
- Primality testing is the problem of determining whether a given number is prime or not.
- There are various algorithms for primality testing, such as trial division, Ferm



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security.

### Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. A group is **abelian** if it also satisfies commutativity.
- A **field** is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group under both operations, as well as the distributive property. A field is **finite** if it has a finite number of elements.
- A **finite field of the form GF(p)** is a field with p elements, where p is a prime number. The elements are usually the integers from 0 to p-1, and the operations are performed modulo p. For example, GF(5) = {0, 1, 2, 3, 4} with addition and multiplication modulo 5.
- **Modular arithmetic** is a system of arithmetic where numbers are reduced to a fixed range by taking the remainder after division by a fixed number, called the modulus. For example, 7 mod 5 = 2, because 7 divided by 5 gives a remainder of 2. Modular arithmetic is useful for cryptography because it allows operations to be performed on large numbers without overflow or loss of precision.
- A number is **prime** if it has exactly two positive divisors: 1 and itself. A number is **relatively prime** or **coprime** to another number if they have no common divisors other than 1. For example, 5 and 7 are relatively prime, but 6 and 9 are not. The **greatest common divisor (GCD)** of two numbers is the largest number that divides both of them. For example, GCD(12, 18) = 6. The **least common multiple (LCM)** of two numbers is the smallest number that is divisible by both of them. For example, LCM(12, 18) = 36.
- The **Extended Euclidean Algorithm** is a method to find the GCD of two numbers, as well as the coefficients of a linear combination of them that equals the GCD. For example, GCD(12, 18) = 6, and 6 = 2 * 12 + (-1) * 18. The algorithm can also be used to find the **multiplicative inverse** of a number modulo another number, if they are relatively prime. For example, the multiplicative inverse of 3 modulo 7 is 5, because 3 * 5 mod 7 = 1.
- The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits, using a secret key of 128, 192, or 256 bits. The encryption and decryption processes consist of several rounds of transformations, such as substitution, permutation, mixing, and key addition. The number of rounds depends on the key size: 10 for 128 bits, 12 for 192 bits, and 14 for 256 bits.
- **Fermat's theorem** states that if p is a prime number and a is any integer, then a^p mod p = a mod p. This implies that if a is not divisible by p, then a^(p-1) mod p = 1. This is also known as **Fermat's little theorem**.
- **Euler's theorem** generalizes Fermat's theorem to any modulus n, not necessarily prime. It states that if a and n are relatively prime, then a^phi(n) mod n =



### Finite field of the form GF(p)

- A finite field is a set of elements that can be added, subtracted, multiplied and divided by each other, obeying certain rules called axioms   .
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., pn, where p is a prime number and n is a positive integer   .
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order of the field is a prime number p. GF stands for Galois field, named after the mathematician Évariste Galois    .
- GF(p) can be constructed from the set of integers modulo p, denoted by Zp = {0, 1, ..., p-1}. The arithmetic operations of addition, subtraction and multiplication are performed modulo p, i.e., the remainder after dividing by p   .
- For example, GF(5) is the finite field with 5 elements, constructed from Z5 = {0, 1, 2, 3, 4}. The arithmetic operations are performed modulo 5, i.e., the remainder after dividing by 5. For instance, 2 + 3 = 0 (mod 5), 4 - 1 = 3 (mod 5), 2 * 3 = 1 (mod 5).
- GF(p) also has the property that every nonzero element has a multiplicative inverse, i.e., for any a in GF(p), there exists b in GF(p) such that a * b = 1 (mod p). This is equivalent to saying that a and p are relatively prime, i.e., they have no common factors other than 1   .
- For example, in GF(5), the multiplicative inverse of 2 is 3, since 2 * 3 = 1 (mod 5). The multiplicative inverse of 3 is 2, since 3 * 2 = 1 (mod 5). The multiplicative inverse of 4 is 4, since 4 * 4 = 1 (mod 5). The multiplicative inverse of 1 is 1, since 1 * 1 = 1 (mod 5). The element 0 has no multiplicative inverse, since 0 * b = 0 (mod p) for any b.
- The existence of multiplicative inverses makes GF(p) a field, i.e., a set that satisfies all the axioms of Figure 4.2 or Figure 4.1. These axioms include commutativity, associativity, distributivity, identity, inverse and closure for both addition and multiplication   .
- Finite fields of the form GF(p) are important for cryptography, as they provide a mathematical basis for many cryptographic algorithms, such as the Advanced Encryption Standard (AES), the RSA algorithm, the Diffie-Hellman key exchange, the ElGamal encryption, the Elliptic Curve Cryptography (ECC) and many others   .
- Finite fields of the form GF(p) also have some interesting properties and theorems, such as Fermat's little theorem, Euler's theorem, the Chinese remainder theorem, the discrete logarithm problem, the primality testing and the public key cryptography   . These topics will be discussed in more detail in the following sections.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of modular arithmetic for the Unit 2.

### Modular arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus.
- The modulus is denoted by a positive integer m, and the set of all integers that are congruent modulo m is denoted by Z_m.
- Two integers a and b are said to be congruent modulo m, written as a ≡ b (mod m), if they have the same remainder when divided by m, or equivalently, if m divides their difference, i.e., m | (a - b).
- Congruence modulo m is an equivalence relation, meaning that it satisfies the following properties:
  - Reflexive: a ≡ a (mod m) for any integer a.
  - Symmetric: if a ≡ b (mod m), then b ≡ a (mod m).
  - Transitive: if a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m).
- Congruence modulo m also preserves the operations of addition, subtraction, and multiplication, meaning that the following properties hold:
  - Closure: if a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m) and a - c ≡ b - d (mod m) and a * c ≡ b * d (mod m).
  - Associative: if a, b, and c are integers, then (a + b) + c ≡ a + (b + c) (mod m) and (a * b) * c ≡ a * (b * c) (mod m).
  - Commutative: if a and b are integers, then a + b ≡ b + a (mod m) and a * b ≡ b * a (mod m).
  - Distributive: if a, b, and c are integers, then a * (b + c) ≡ a * b + a * c (mod m).
- Modular arithmetic can be used to perform arithmetic operations on large numbers by reducing them to smaller numbers modulo m, and then combining the results using the Chinese Remainder Theorem.
- Modular arithmetic can also be used to study the properties of integers, such as divisibility, primality, and multiplicative inverses.
- Modular arithmetic is the basis of many cryptographic algorithms, such as RSA, Diffie-Hellman, and ElGamal.



### Prime and Relative Prime Numbers

- A **prime number** is a whole number greater than 1 whose only factors are 1 and itself. Such as 2, 3, 5, and 7 .
- Two integers, a and b, are said to be **relatively prime** (or coprime or mutually prime) when there are no common factors other than 1. This means that no other integer could divide both numbers evenly   .
- Two numbers m and n are said to be relatively prime if GCF (a,b) = 1 .
- Any two prime numbers are always relatively prime. For example, in 19 and 17 the only common factor is 1 and they are prime numbers too .
- A prime number is relatively prime with any other number because prime numbers are the numbers that can be divided by one or themselves. Thus, if we pair up any prime number with other numbers the result will be relatively prime because the common factor will be one .
- Some properties of relatively prime numbers are:
  - If n is a prime number, then all integers less than or equal to n are relatively prime to n.
  - If a and b are two relatively prime numbers, then a + b is relatively prime to a × b.
  - If a and b are relatively prime numbers, then HCF ( a, b) = 1 and LCM ( a, b) = a × b .
- Some examples of relatively prime numbers are :
  - 8 and 15 are relatively prime because their only common factor is 1.
  - 9 and 16 are relatively prime because their only common factor is 1.
  - 12 and 25 are relatively prime because their only common factor is 1.
  - 18 and 35 are relatively prime because their only common factor is 1.



### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax ≡ 1 (mod b).
- The extended Euclidean algorithm can also be generalized to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.
- The algorithm works by applying the Euclidean algorithm repeatedly until the remainder is zero, and then backtracking to find the coefficients x and y. The Euclidean algorithm is an efficient way of computing the greatest common divisor of two numbers by using the division algorithm and the property that gcd(a,b) = gcd(b,r), where r is the remainder of dividing a by b.
- The pseudocode of the extended Euclidean algorithm is as follows:

```
function extended_gcd(a, b)
    if b == 0
        return (a, 1, 0) // base case: gcd(a,0) = a, x = 1, y = 0
    else
        (d, x, y) = extended_gcd(b, a mod b) // recursive call: gcd(a,b) = gcd(b, a mod b)
        return (d, y, x - (a div b) * y) // backtrack: x = y, y = x - (a div b) * y
```

- The function returns a tuple (d, x, y) such that d = gcd(a,b) and ax + by = d.
- For example, to find the multiplicative inverse of 7 modulo 26, we can call the function with a = 7 and b = 26. The function returns (1, 15, -4), which means that gcd(7,26) = 1 and 7 * 15 + 26 * (-4) = 1. Therefore, the multiplicative inverse of 7 modulo 26 is 15, since 7 * 15 ≡ 1 (mod 26).



### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric block cipher that can encrypt and decrypt data using the same key  .
- AES operates on blocks of 128 bits, and can use keys of 128, 192, or 256 bits .
- AES consists of four main operations: byte substitution, row shift, column mix, and key addition  .
- AES performs a number of rounds of these operations, depending on the key size. For 128-bit keys, 10 rounds are performed; for 192-bit keys, 12 rounds are performed; and for 256-bit keys, 14 rounds are performed .
- AES encryption transforms a plaintext block into a ciphertext block by applying the key and the operations in each round .
- AES decryption reverses the encryption process by applying the inverse operations and the key in the reverse order .
- AES is a widely used and secure algorithm that can protect electronic data from unauthorized access or modification  .

### Fermat's and Euler's theorem

- Fermat's theorem states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p   .
- Euler's theorem is a generalization of Fermat's theorem that states that if n is any positive integer and a is any integer that is coprime to n, then a^(φ(n)) is congruent to 1 modulo n, where φ(n) is Euler's totient function   .
- Euler's totient function counts the number of positive integers less than or equal to n that are coprime to n   .
- Euler's theorem can be proved using the concept of reduced residue systems, which are sets of integers that are coprime to a given modulus and form a complete set of residues modulo that modulus .
- Euler's theorem is useful for solving congruences and finding modular inverses, as well as for applications in cryptography, such as the RSA algorithm  .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security.

### Introduction to group, field, finite field of the form GF(p)

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse.
- A field is a group that also satisfies two additional properties: commutativity and distributivity.
- A finite field is a field that has a finite number of elements.
- A finite field of the form GF(p) is a field that has p elements, where p is a prime number.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a remainder after dividing by a fixed modulus.
- Prime numbers are numbers that have exactly two positive divisors: 1 and themselves.
- Relative prime numbers are numbers that have no common positive divisors other than 1.

### Extended Euclidean Algorithm

- The Extended Euclidean Algorithm is a method to find the greatest common divisor (GCD) of two numbers and also the coefficients of a linear combination of the two numbers that equals the GCD.
- The algorithm is based on the following identity: GCD(a, b) = GCD(b, a mod b).
- The algorithm can be used to find the multiplicative inverse of a number modulo another number, which is useful for encryption and decryption.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that encrypts and decrypts data in 128-bit blocks.
- AES uses a secret key of 128, 192, or 256 bits, which is expanded into a series of round keys using a key expansion algorithm.
- AES encryption consists of four stages: AddRoundKey, SubBytes, ShiftRows, and MixColumns, which are repeated for a number of rounds depending on the key size.
- AES decryption consists of the inverse stages: InvMixColumns, InvShiftRows, InvSubBytes, and AddRoundKey, which are repeated in reverse order for the same number of rounds.

### Fermat’s and Euler’s theorem

- Fermat's theorem states that if p is a prime number and a is any integer, then a^p ≡ a (mod p).
- Euler's theorem states that if a and n are relatively prime, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n.
- Both theorems are useful for encryption and decryption using modular exponentiation.

### Primality testing

- Primality testing is the problem of determining whether a given number is prime or composite.
- There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc.
- Some algorithms are deterministic, meaning they always give the correct answer, while some are probabilistic, meaning they give a high probability of the correct answer.
- Primality testing is important for generating large prime numbers for public-key cryptography.

### Chinese Remainder theorem

- The Chinese Remainder theorem states that if n1, n2, ..., nk are pairwise relatively prime positive integers, and a1, a2, ..., ak are any integers, then there exists a unique integer x such that x ≡ a1 (mod n1), x ≡ a2 (mod n2), ..., x ≡ ak (mod nk), and 0 ≤ x < n1n2...nk.
- The theorem also provides a method to find x using the extended Euclidean algorithm and modular arithmetic.
- The theorem can be used to speed up modular exponentiation and RSA encryption and decryption.

### Discrete Logarithmic Problem

- The discrete logarithmic problem is the problem of finding x given



### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- The theorem can be expressed in terms of congruences as follows :

  - Let n1, n2, ..., nk be positive integers that are pairwise coprime (i.e., gcd(ni, nj) = 1 for all i ≠ j).
  - Let a1, a2, ..., ak be any integers.
  - Then, there exists an integer x that satisfies the system of congruences:

    - x ≡ a1 (mod n1)
    - x ≡ a2 (mod n2)
    - ...
    - x ≡ ak (mod nk)

  - Moreover, any two such integers x and y are congruent modulo N = n1n2...nk, i.e., x ≡ y (mod N).

- The theorem can be proved using the properties of modular arithmetic and the extended Euclidean algorithm  .
- The theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The theorem is also useful for solving systems of congruences, cryptography, number theory, and combinatorics .



### Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- Discrete logarithms are perhaps simplest to understand in the group Zp*, where p is the prime number. Let g be the generator of Zp*, then the discrete logarithm problem reduces to computing a, given (g, p, ga mod p) for a randomly chosen a < (p −1).
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log b a in finite groups G is to raise b to larger and larger powers k until the desired a is found. This is called the **brute-force** or **exhaustive search** algorithm. It has a time complexity of O(|G|) and a space complexity of O(1).
- There are some algorithms that can solve the discrete logarithm problem faster than the brute-force algorithm, but they are still exponential in the size of the input. Some of these algorithms are:
  - **Shanks' baby-step giant-step algorithm**: It has a time complexity of O(√|G|) and a space complexity of O(√|G|).
  - **Pollard's rho algorithm**: It has a time complexity of O(√|G|) and a space complexity of O(1). It is a probabilistic algorithm that uses a pseudo-random function to generate a sequence of elements in G and detects a cycle in the sequence.
  - **Pohlig-Hellman algorithm**: It has a time complexity of O(√p) and a space complexity of O(log p), where p is the largest prime factor of |G|. It is a divide-and-conquer algorithm that reduces the discrete logarithm problem in G to several discrete logarithm problems in smaller subgroups of G.
  - **Index calculus algorithm**: It has a subexponential time complexity of Lp[1/2, c] for some constant c, where Lp[α, c] = exp((c + o(1))(log p)α(log log p)1−α). It is the fastest known algorithm for solving the discrete logarithm problem in the multiplicative group of a finite field. It is based on the idea of finding a factor base of small elements in the group and expressing other elements as products of the factor base elements.
- The discrete logarithm problem is the basis of many cryptographic schemes, such as the Diffie-Hellman key exchange, the ElGamal encryption and signature schemes, and the Digital Signature Algorithm (DSA). These schemes rely on the assumption that the discrete logarithm problem is hard to solve in certain groups, such as the multiplicative group of a large prime field or an elliptic curve group.

