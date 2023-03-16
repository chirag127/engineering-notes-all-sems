### Advanced Encryption Standard (AES) encryption and decryption

Advanced Encryption Standard (AES) is a symmetric block cipher that encrypts and decrypts data in blocks of 128 bits. It uses a fixed block size of 128 bits and a key size of 128, 192, or 256 bits. The number of rounds in the AES algorithm depends on the key size, with 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.

The AES algorithm consists of four main stages: SubBytes, ShiftRows, MixColumns, and AddRoundKey. These stages are repeated for each round of the algorithm.

1. **SubBytes**: This stage applies a non-linear substitution to each byte of the block, using a substitution table called the S-box.
2. **ShiftRows**: This stage cyclically shifts the rows of the block by different offsets.
3. **MixColumns**: This stage mixes the columns of the block, combining the four bytes in each column.
4. **AddRoundKey**: This stage adds the round key to the block, using bitwise XOR.

The encryption process begins with an initial AddRoundKey stage, followed by the four main stages repeated for the appropriate number of rounds, and ends with a final round that consists of SubBytes, ShiftRows, and AddRoundKey stages.

Decryption is the reverse process of encryption. It uses the same key and algorithm, but in reverse order. The decryption process begins with an initial AddRoundKey stage, followed by the four main stages repeated for the appropriate number of rounds, and ends with a final round that consists of InvShiftRows, InvSubBytes, and AddRoundKey stages.

AES is a widely used encryption standard, adopted by the U.S. government and used in various applications, including secure communications, data storage, and online transactions. It is considered to be a secure encryption algorithm, with no known practical attacks against it.