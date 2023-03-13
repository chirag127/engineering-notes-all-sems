## Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES

- Security attacks, services and mechanisms
  - Security attack: Any action that compromises the security of information owned by an organization .
  - Security service: A service that enhances the security of data processing systems and information transfers . Examples are confidentiality, integrity, authentication, non-repudiation, access control, availability .
  - Security mechanism: A mechanism that is designed to detect, prevent or recover from a security attack . Examples are encryption, digital signature, firewall, intrusion detection system, backup .
  - The OSI security architecture provides a systematic framework for defining security attacks, mechanisms, and services .
  - Security attacks are classified as either passive or active .
    - Passive attack: An attack that does not affect the normal functioning of the system, but only attempts to eavesdrop or monitor the communication . Examples are traffic analysis, release of message contents .
    - Active attack: An attack that alters or disrupts the normal functioning of the system, by modifying, deleting, inserting, or replaying data . Examples are masquerade, modification of messages, denial of service, replay .
  - Security services are classified according to the OSI model layers .
    - Application layer: Provides security services to end users and applications . Examples are secure email, secure web browsing, secure electronic transactions .
    - Presentation layer: Provides security services to the data representation and syntax . Examples are data compression, data encryption, data conversion .
    - Session layer: Provides security services to the communication session between hosts . Examples are session authentication, session encryption, session management .
    - Transport layer: Provides security services to the end-to-end data transmission . Examples are transport authentication, transport encryption, transport reliability .
    - Network layer: Provides security services to the network layer packets . Examples are network authentication, network encryption, network routing .
    - Data link layer: Provides security services to the data link layer frames . Examples are frame authentication, frame encryption, frame error control .
    - Physical layer: Provides security services to the physical layer signals . Examples are signal authentication, signal encryption, signal interference .
  - Security mechanisms are classified as either specific or pervasive .
    - Specific mechanism: A mechanism that is applied to a specific service or protocol . Examples are encryption algorithm, digital signature algorithm, hash function .
    - Pervasive mechanism: A mechanism that is applied to the entire system or network . Examples are security audit, security recovery, security policy .

- Classical encryption techniques
  - Encryption: The process of transforming plaintext (original message) into ciphertext (encrypted message) using a secret key and an encryption algorithm .
  - Decryption: The process of transforming ciphertext (encrypted message) into plaintext (original message) using a secret key and a decryption algorithm .
  - Cryptography: The study of encryption and decryption techniques .
  - Cryptanalysis: The study of breaking encryption and decryption techniques .
  -