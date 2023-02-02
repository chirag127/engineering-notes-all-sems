### block cipher modes of operations for the notes of the Unit 1 - Introduction of security attacks, services and mechanism in the subject of Cryptography & Network Security
Block cipher modes of operation are methods used to encrypt data in fixed-size blocks using a block cipher algorithm.
1. ECB (Electronic Codebook Mode): simplest mode, each block encrypted separately, vulnerable to pattern recognition.
2. CBC (Cipher Block Chaining Mode): each block XORed with previous ciphertext, randomizes plaintext.
3. CFB (Cipher Feedback Mode): encrypts a stream of data, operates on small parts of plaintext.
4. OFB (Output Feedback Mode): encrypts a stream of data, operates on ciphertext.
5. CTR (Counter Mode): encrypts a stream of data, uses a counter for unique ciphertext.
6. XTS (XEX-based Tweaked Codebook Mode): encrypts disk data, uses two keys and block cipher.
