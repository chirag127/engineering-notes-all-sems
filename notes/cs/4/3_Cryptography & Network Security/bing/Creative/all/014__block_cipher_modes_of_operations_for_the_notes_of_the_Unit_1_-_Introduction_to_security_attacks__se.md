### Block cipher modes of operation

A block cipher mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity. A block cipher by itself is only suitable for the secure cryptographic transformation (encryption or decryption) of one fixed-length group of bits called a block. A mode of operation describes how to repeatedly apply a cipher's single-block operation to securely transform amounts of data larger than a block. Most modes require a unique binary sequence, often called an initialization vector (IV), for each encryption operation. The IV has to be non-repeating and, for some modes, random as well. The initialization vector is used to ensure distinct ciphertexts are produced even when the same plaintext is encrypted multiple times independently with the same key.

There are several modes of operation for a block cipher, each with different advantages and disadvantages. Some of the most common modes are:

- Electronic Code Book (ECB) – This is the simplest mode of operation, where each block of plaintext is encrypted independently with the same key. The output is a sequence of blocks of ciphertext. This mode is fast and parallelizable, but it is not secure against cryptanalysis, as identical plaintext blocks will produce identical ciphertext blocks, revealing patterns and repetitions in the data. This mode also does not support data integrity or authentication.

- Cipher Block Chaining (CBC) – This mode improves the security of ECB by using the previous ciphertext block as an IV for the next encryption. The first block is encrypted with a random IV. The output is a sequence of blocks of ciphertext. This mode prevents identical plaintext blocks from producing identical ciphertext blocks, and also provides some data integrity protection. However, this mode is not parallelizable for encryption, as each block depends on the previous one. It also does not provide authentication.

- Cipher Feedback (CFB) – This mode converts a block cipher into a stream cipher, where each plaintext bit is encrypted with a keystream bit generated from the previous ciphertext block. The first block is encrypted with a random IV. The output is a sequence of bits of ciphertext. This mode allows encryption and decryption of data of any size, and also provides some data integrity protection. However, this mode is not parallelizable for encryption, and it is sensitive to bit errors, as a single bit error in the ciphertext will propagate to the rest of the decryption.

- Output Feedback (OFB) – This mode is similar to CFB, but it uses the encrypted output as the IV for the next encryption, instead of the actual ciphertext. The first block is encrypted with a random IV. The output is a sequence of bits of ciphertext. This mode also converts a block cipher into a stream cipher, and allows encryption and decryption of data of any size. However, this mode does not provide any data integrity or authentication, and it is vulnerable to replay attacks, as the same keystream can be used to encrypt different plaintexts.

- Counter (CTR) – This mode also converts a block cipher into a stream cipher, but it uses a counter as the IV for each encryption. The counter is incremented for each block, and encrypted with the same key. The output is a sequence of bits of ciphertext. This mode allows encryption and decryption of data of any size, and it is parallelizable for both encryption and decryption. However, this mode also does not provide any data integrity or authentication, and it requires a unique and unpredictable counter for each encryption, otherwise the security is compromised.

- XTS – This mode is designed for encrypting data on storage devices, where the data is organized in units of a fixed size, such as sectors. This mode uses two keys, one for encrypting the data blocks, and one for encrypting the sector numbers. The output is a sequence of blocks of ciphertext. This mode provides confidentiality and some data integrity protection, but it does not provide authentication. It also does not prevent data manipulation, such as swapping or copying sectors.

Some mnemonics and learning tricks for the block cipher modes of operation are:

- ECB: Easy but Crappy Block mode
- CBC: Cipher Blocks Chained together
- CFB: Cipher Feedback from previous block
- OFB: Output Feedback from encryption
- CTR: Counter mode with incrementing IV
- XTS: eXtended Tweaked Sector mode

Some examples of block cipher modes of operation in ASCII diagrams are:

- ECB:

```
Key    Key    Key    Key
 |      |      |      |
 v      v      v      v
+------+ +------+ +------+ +------+
|Plain1| |Plain2| |Plain3| |Plain4|
+------+ +------+ +------+ +------