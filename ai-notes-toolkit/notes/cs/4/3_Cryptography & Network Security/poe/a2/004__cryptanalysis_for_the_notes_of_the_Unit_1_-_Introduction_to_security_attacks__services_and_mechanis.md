 Here are the notes on the given topic in the requested format:

### Cryptanalysis

- Cryptanalysis is the study of methods of obtaining the meaning of encrypted information, without access to the secret information that is normally required to do so.
- Cryptanalysts look for weaknesses in the implementation or algorithm that can be exploited to recover the secret key or plain text.
- The two types of cryptanalysis are ciphertext-only cryptanalysis and known-plaintext cryptanalysis.

### Classical Encryption Techniques

- Substitution ciphers: Replace each letter of the plain text with another letter or symbol. Eg. Caesar cipher. Can be easily cracked using frequency analysis.
- Transposition ciphers: Rearrange the position of letters in the plain text. Eg. Rail fence cipher. Can be cracked using anagramming techniques.

### Modern Block Ciphers

- Block ciphers encrypt data in blocks of fixed size. Eg. DES, AES.
- Shannon's theory of confusion and diffusion: A secure block cipher should have confusion (making the relationship between the key and the ciphertext complex) and diffusion (spreading the influence of one plaintext symbol over many ciphertext symbols).
- Feistel structure: A common structure used in block ciphers. Uses repeated application of encryption and decryption functions.
- Data Encryption Standard (DES): A 64-bit block cipher with a 56-bit key. Considered insecure due to small key size.
- Strength of DES: Can be cracked in less than a day. Vulnerable to related-key attacks and brute-force attacks.
- Idea of differential cryptanalysis: Studies how differences in plain text can affect the resultant differences in the ciphertext. Can be used to break block ciphers.
- Block cipher modes of operation: Different ways of using a block cipher to encrypt data of arbitrary length. Eg. ECB, CBC, CFB, OFB, CTR modes.
- Triple DES: A variant of DES that applies DES three times to each block and increases the key size to 112/168 bits. More secure than DES.