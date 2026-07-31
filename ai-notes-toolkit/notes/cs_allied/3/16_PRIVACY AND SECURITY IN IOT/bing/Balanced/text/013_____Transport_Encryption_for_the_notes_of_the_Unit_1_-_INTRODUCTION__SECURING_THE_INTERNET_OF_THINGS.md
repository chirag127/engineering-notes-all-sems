### Transport Encryption for the notes of the Unit 1 - INTRODUCTION: SECURING THE INTERNET OF THINGS in the subject of PRIVACY AND SECURITY IN IOT

- Transport encryption is the process of protecting data while it is being transmitted over a network, such as the internet.
- Transport encryption is important for IoT devices because they often communicate sensitive or personal information, such as sensor readings, device status, user commands, etc.
- Transport encryption can prevent unauthorized parties from intercepting, modifying, or tampering with the data in transit, thus ensuring its confidentiality, integrity, and authenticity.
- Transport encryption can also prevent replay attacks, where an attacker captures and retransmits a valid message to cause undesired effects, such as turning on a device, changing its settings, etc.
- Transport encryption can be achieved by using cryptographic protocols, such as Transport Layer Security (TLS), which is the standard protocol for securing web traffic.
- TLS works by establishing a secure connection between two parties, such as an IoT device and a cloud service, using a handshake process that involves exchanging certificates, keys, and ciphers.
- TLS then encrypts and decrypts the data using symmetric encryption, such as AES, and verifies its integrity using message authentication codes, such as HMAC.
- TLS also supports mutual authentication, where both parties verify each other's identity using certificates, which are digital documents that contain public keys and other information, such as issuer, expiration date, etc.
- Certificates are issued and signed by trusted authorities, such as Certificate Authorities (CAs), which are entities that vouch for the validity of the certificates.
- IoT devices need to have certificates installed on them, either by the manufacturer, the user, or the cloud service provider, in order to use TLS for transport encryption.
- IoT devices also need to have a secure storage for the certificates and keys, such as a hardware security module (HSM), which is a physical device that protects the cryptographic material from unauthorized access or tampering.
- IoT devices should use the latest version of TLS, which is TLS 1.3, as it offers improved security and performance over previous versions, such as TLS 1.2 or SSL.
- IoT devices should also use strong ciphers and algorithms, such as AES-256 and SHA-256, and avoid weak or deprecated ones, such as RC4 and MD5.
- IoT devices should also use certificate pinning, which is a technique that allows them to verify the identity of a specific server or service, rather than trusting any certificate issued by a CA.
- Certificate pinning can prevent man-in-the-middle attacks, where an attacker intercepts and modifies the traffic between the IoT device and the cloud service, by using a fake or compromised certificate.
- Certificate pinning can be implemented by hardcoding the expected certificate or its fingerprint in the IoT device's firmware, or by using a public key infrastructure (PKI), which is a system that manages the creation, distribution, and revocation of certificates and keys.