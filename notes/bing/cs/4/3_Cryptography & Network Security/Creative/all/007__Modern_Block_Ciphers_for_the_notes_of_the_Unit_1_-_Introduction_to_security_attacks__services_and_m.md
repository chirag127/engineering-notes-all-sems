### Modern Block Ciphers

- A modern block cipher is a cipher which encrypts m-bit block of plaintext and decrypts m-bit block of ciphertext .
- For encryption or decryption, modern block cipher facilitate a K bit key and the decryption algorithm should be inverse of encryption algorithms and for both encryption and decryption similar key is used.
- Most modern block ciphers are designed to encrypt data in fixed-size blocks of either 64 or 128 bits.
- Modern block ciphers are based on the design of an iterated product cipher, which means that they apply a basic encryption function repeatedly to the plaintext, using a different subkey for each iteration.
- The basic encryption function is called a round function, and the subkeys are derived from the main key by a process called key schedule.
- The number of rounds depends on the security level and the block size of the cipher. For example, DES has 16 rounds, AES has 10, 12, or 14 rounds depending on the key size.
- Modern block ciphers can operate in different modes of operation, which determine how the blocks are chained together and how the initialization vector (IV) is used.
- The most common modes of operation are:

  - Electronic codebook (ECB) mode: ECB mode is used to electronically code messages as their plaintext form. It is the simplest of all block cipher modes, but also the least secure. It encrypts each block of plaintext independently with the same key, which means that identical blocks of plaintext will produce identical blocks of ciphertext. This can reveal patterns and repetitions in the data, making it vulnerable to cryptanalysis.
  - Cipher block chaining (CBC) mode: CBC mode is a method of encrypting data that ensures each block of ciphertext depends on all the previous blocks of plaintext. It uses an IV to randomize the first block of ciphertext, and then XORs each subsequent block of plaintext with the previous block of ciphertext before encrypting it. This way, any change in the plaintext will propagate through the ciphertext, and identical blocks of plaintext will produce different blocks of ciphertext.
  - Cipher feedback (CFB) mode: CFB mode is a method of encrypting data that makes a block cipher into a self-synchronizing stream cipher. It uses an IV to generate the first block of keystream, and then XORs it with the first block of plaintext to produce the first block of ciphertext. The ciphertext is then fed back into the cipher to generate the next block of keystream, and so on. This way, the ciphertext is always the same size as the plaintext, and any bit error in the ciphertext will only affect the corresponding bit of plaintext.
  - Output feedback (OFB) mode: OFB mode is a method of encrypting data that makes a block cipher into a synchronous stream cipher. It uses an IV to generate the first block of keystream, and then XORs it with the first block of plaintext to produce the first block of ciphertext. The keystream is then fed back into the cipher to generate the next block of keystream, and so on. This way, the ciphertext is always the same size as the plaintext, and any bit error in the ciphertext will not affect the plaintext at all.
  - Counter (CTR) mode: CTR mode is a method of encrypting data that makes a block cipher into a stream cipher. It uses a counter, which is a value that is incremented for each block of plaintext, and encrypts it with the key to generate a block of keystream. The keystream is then XORed with the block of plaintext to produce the block of ciphertext. This way, the ciphertext is always the same size as the plaintext, and any bit error in the ciphertext will only affect the corresponding bit of plaintext. CTR mode has the advantage of being parallelizable, meaning that multiple blocks of plaintext can be encrypted or decrypted at the same time.

- Some mnemonics and learning tricks for modern block ciphers are:

  - To remember the difference between ECB and CBC modes, think of ECB as "Easy to Crack Blocks" and CBC as "Chaining Blocks Carefully".
  - To remember the difference between CFB and OFB modes, think of CFB as "Ciphertext Feedback" and OFB as "Output Feedback".
  - To remember the difference between CFB and CTR modes, think of CFB as "Cipher Feedback" and CTR as "Counter".
  - To remember the difference