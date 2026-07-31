### Digital Signatures

- A digital signature is a mathematical scheme for verifying the authenticity and integrity of digital messages or documents.
- A digital signature is backed by a digital certificate, which provides proof of the identity of the sender.
- A digital signature consists of two components: a signing algorithm and a verification algorithm.
- The signing algorithm uses a private key to generate a signature for a given message, while the verification algorithm uses a public key to verify the signature for the same message.
- The public key and the private key are mathematically related, but the private key cannot be derived from the public key.
- The public key and the digital certificate are usually distributed to the recipients or made available in a public repository, while the private key is kept secret by the sender.
- A digital signature provides the following benefits :
  - It ensures that the message was created by a known sender (authenticity).
  - It ensures that the message was not altered in transit or after signing (integrity).
  - It prevents the sender from denying having sent the message (non-repudiation).
- A digital signature can be used for various purposes, such as signing contracts, invoices, emails, software, firmware, etc  .
- A digital signature can be implemented using various algorithms, such as RSA, DSA, ECDSA, etc.
- A digital signature is different from an electronic signature, which is a broader term that refers to any method of signing a digital document, such as typing a name, drawing a signature, scanning a handwritten signature, etc. An electronic signature may or may not be backed by a digital certificate or a cryptographic scheme.