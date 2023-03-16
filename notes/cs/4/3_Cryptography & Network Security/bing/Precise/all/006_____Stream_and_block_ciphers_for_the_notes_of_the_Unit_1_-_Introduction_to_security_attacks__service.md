# Stream and Block Ciphers

Stream and block ciphers are two types of symmetric key encryption techniques. Symmetric key encryption is a method of encryption where the same key is used for both encryption and decryption of the data.

## Stream Ciphers

A stream cipher is a type of symmetric key encryption where the plaintext is combined with a pseudorandom cipher bit stream, typically by an exclusive-or (XOR) operation. In a stream cipher, each plaintext digit is encrypted one at a time with the corresponding digit of the keystream, to give a digit of the ciphertext stream.

Stream ciphers can be classified into two types: synchronous and self-synchronizing. In a synchronous stream cipher, the keystream is generated independently of the plaintext and ciphertext messages. In a self-synchronizing stream cipher, the keystream is generated based on the previous N ciphertext digits.

## Block Ciphers

A block cipher is a type of symmetric key encryption where the plaintext is divided into blocks of fixed length and each block is encrypted separately. The most common block size is 64 bits, but other block sizes are also used, such as 128 bits.

Block ciphers can be classified into two types: substitution-permutation network (SPN) and Feistel network. In an SPN, the plaintext is divided into blocks and each block is passed through several rounds of substitution and permutation operations. In a Feistel network, the plaintext is divided into two halves and each half is passed through several rounds of substitution and permutation operations, with the two halves being swapped after each round.

Block ciphers can be used in several modes of operation, such as electronic codebook (ECB), cipher block chaining (CBC), cipher feedback (CFB), output feedback (OFB), and counter (CTR). Each mode of operation has its own advantages and disadvantages, and the choice of mode depends on the specific requirements of the application.