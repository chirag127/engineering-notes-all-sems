# Certificates for the notes of the Unit 4 - Basic cryptography in the subject of COMPUTER SYSTEM SECURITY

- In cryptography, a **certificate** is an electronic document that proves the ownership or validity of a public key .
- A public key is a cryptographic key that can be used by anyone to encrypt or verify data, while the corresponding private key is kept secret by the owner.
- A certificate contains information about the public key, the identity of its owner (called the **subject**), and the digital signature of an entity that has verified the certificate's contents (called the **issuer**) .
- The issuer is usually a trusted third party, such as a certificate authority (CA), that can vouch for the authenticity of the subject and the public key.
- A certificate can be used for various purposes, such as:
  - Proving the identity of a server or a client in a secure communication protocol, such as SSL/TLS or HTTPS .
  - Verifying the integrity and origin of a code or a document, such as a software update or a digital signature .
  - Encrypting data for a specific recipient, such as an email or a file .
- A certificate has a limited validity period, after which it expires and needs to be renewed or replaced.
- A certificate can also be revoked by the issuer or the subject if it is compromised or no longer needed.
- A certificate can be stored in various formats, such as PEM, DER, or PKCS#12, depending on the application and the platform.
- A certificate can be viewed or managed by using various tools, such as OpenSSL, certutil, or certmgr.