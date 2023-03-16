### Digital signature

A digital signature is a mathematical scheme to verify the authenticity of digital documents or messages. A digital signature uses a digital certificate from a trust service provider (TSP), such as a certificate authority (CA), to authenticate a signer's identity. The digital certificate demonstrates proof of signing by binding the digital certificate associated with each signature to the document using encryption .

A digital signature has the following properties:

- **Authentication**: It confirms the identity of the sender or signer of the document or message.
- **Integrity**: It ensures that the document or message has not been altered or tampered with after signing.
- **Non-repudiation**: It prevents the sender or signer from denying or disputing the validity of the document or message.

A digital signature is created by applying a hash function to the document or message, which produces a unique value called a hash or digest. The hash is then encrypted with the private key of the signer, which is known only to the signer. The encrypted hash is the digital signature, which is attached to the document or message. The recipient of the document or message can verify the digital signature by decrypting it with the public key of the signer, which is available from the TSP. The decrypted hash is then compared with the hash of the document or message, which is computed by applying the same hash function. If the hashes match, the digital signature is valid and the document or message is authentic and intact .

A digital signature is different from an electronic signature, which is a broader term that refers to any electronic data that carries the intent of a signature. An electronic signature can be a scanned image of a handwritten signature, a typed name, a click of a button, or a biometric identifier. An electronic signature does not necessarily provide the same level of security and legal validity as a digital signature.

A digital signature is governed by various laws and regulations, depending on the jurisdiction and the context of use. In the United States, the Electronic Signatures in Global and National Commerce (ESIGN) Act in 2000 legislated that electronic signatures, including digital signatures, are legal in every state and U.S. territory where federal law applies. Where federal law does not apply, most U.S. states have adopted the Uniform Electronic Transactions Act (UETA), which Congress passed in 1999. Both ESIGN and UETA establish the legal equivalence of electronic signatures and handwritten signatures, and provide guidelines for their use and acceptance .

In India, the Information Technology Act, 2000, governs the use of cyberspace and the protection of digital information. The Act defines a digital signature as "authentication of any electronic record by a subscriber by means of an electronic method or procedure in accordance with the provisions of section 3". Section 3 specifies the use of asymmetric cryptosystem and hash function for creating and verifying digital signatures. The Act also provides legal recognition to digital signatures and electronic records, and prescribes the duties and responsibilities of the TSPs and the signers .

A digital signature is an important tool for ensuring the security and legality of digital transactions and communications. It can be used for various purposes, such as:

- Signing contracts, agreements, invoices, receipts, and other documents electronically.
- Securing online banking, e-commerce, and e-government services.
- Protecting email messages and attachments from unauthorized access and modification.
- Verifying the authenticity and integrity of software downloads and updates.
- Certifying the identity and authority of online users and entities.