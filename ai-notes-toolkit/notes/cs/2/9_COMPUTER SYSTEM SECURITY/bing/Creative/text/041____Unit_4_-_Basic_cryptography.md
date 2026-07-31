## Unit 4 - Basic cryptography

Cryptography is the art of securing information by turning plaintext into ciphertext. Plaintext is the original message that can be understood by anyone, while ciphertext is the encrypted message that can only be understood by the intended recipient. Cryptography uses mathematical concepts and algorithms to transform messages in ways that are hard to decipher.

Some of the objectives of cryptography are:

- Confidentiality: ensuring that only the authorized parties can access the information.
- Integrity: ensuring that the information is not altered or corrupted during transmission or storage.
- Non-repudiation: ensuring that the sender or the receiver cannot deny their involvement in the communication.
- Authentication: ensuring that the parties involved in the communication are who they claim to be.

Some of the basic types of cryptography are:

- Symmetric-key cryptography: using the same key for both encryption and decryption. The key must be shared securely between the sender and the receiver. Examples of symmetric-key algorithms are AES, DES, and RC4.
- Asymmetric-key cryptography: using different keys for encryption and decryption. The sender uses the public key of the receiver to encrypt the message, and the receiver uses their own private key to decrypt it. The public key can be shared openly, while the private key must be kept secret. Examples of asymmetric-key algorithms are RSA, ECC, and ElGamal.
- Hashing: using a one-way function to map any input to a fixed-length output, called a hash or a digest. The hash cannot be reversed to obtain the original input, and it is unique for each input. Hashing is used to verify the integrity of the information, as any change in the input will result in a different hash. Examples of hashing algorithms are SHA, MD5, and BLAKE.

Some of the applications of cryptography are:

- Digital signatures: using asymmetric-key cryptography and hashing to sign a message with the sender's private key and verify it with the sender's public key. Digital signatures provide non-repudiation and authentication for the message.
- Time stamping: using a trusted third party to record the time and date of a message or a document. Time stamping provides proof of existence and proof of order for the message or the document.
- Electronic money transactions: using cryptography to secure the transfer of funds between parties. Electronic money transactions provide confidentiality, integrity, non-repudiation, and authentication for the payment.
- Cryptocurrency: using cryptography to create and manage a decentralized digital currency that is not controlled by any central authority. Cryptocurrency uses cryptographic techniques such as hashing, digital signatures, and proof-of-work to ensure the validity and security of the transactions and the currency. Examples of cryptocurrencies are Bitcoin, Ethereum, and Dogecoin.