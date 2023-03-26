 Here are the notes on Digital Signatures for the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT:

### Digital Signatures

- A digital signature is a mathematical scheme for demonstrating the authenticity of a digital message or document.
- A valid digital signature gives a recipient reason to believe that the message was created by a known sender, and that it was not altered in transit.
- Digital signatures are commonly used for software distribution, financial transactions, and in other cases where it is important to detect forgery or tampering.

How Digital Signatures work:

1. The sender uses a private key to generate a digital signature for the message. This signature is a short digest of the message that is unique to the sender.
2. The sender transmits the digital signature along with the message to the recipient.
3. The recipient uses the sender's public key to verify the digital signature. If the signature is valid, the recipient can be sure that the message came from the sender and was not altered.
4. Only the sender's private key could have created the digital signature. The public key can verify it but cannot generate it. This provides authentication and non-repudiation.

Benefits of Digital Signatures:

- Authentication - Confirms that the message was signed by the genuine sender
- Non-Repudiation - The sender cannot deny sending the message later
- Integrity - Ensures that the message was not altered in transit
- Non-interference - Only the sender and recipient are involved, no third party is required to verify the signature

Thus, digital signatures provide authentication, non-repudiation and integrity for electronic messages and documents. They play an important role in ensuring security for IoT communications and transactions.