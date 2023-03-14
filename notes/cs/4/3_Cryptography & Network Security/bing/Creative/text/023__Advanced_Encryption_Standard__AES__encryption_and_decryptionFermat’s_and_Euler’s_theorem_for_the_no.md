### Advanced Encryption Standard (AES) encryption and decryption

- The Advanced Encryption Standard (AES) is a **symmetric block cipher** that can be used to protect electronic data  .
- A symmetric block cipher means that the same **secret key** is used to both encrypt and decrypt the data, and that the data is processed in fixed-size blocks (128 bits in AES).
- AES was adopted as a **FIPS-approved** cryptographic algorithm by the U.S. government in 2001, after a public competition and evaluation process .
- AES can use cryptographic keys of **128, 192, or 256 bits** to encrypt and decrypt data  .
- AES encryption and decryption involves **several rounds** of substitution, transposition, and mixing operations, which are controlled by the key .
- The number of rounds depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys .
- Each round consists of four steps: **SubBytes**, **ShiftRows**, **MixColumns**, and **AddRoundKey** .
- SubBytes is a **non-linear substitution** of each byte in the state (the intermediate result of the encryption or decryption) using a lookup table called the S-box .
- ShiftRows is a **cyclic shift** of each row in the state to the left by a certain number of positions .
- MixColumns is a **linear transformation** that mixes the bytes in each column of the state using a matrix multiplication .
- AddRoundKey is a **bitwise XOR** of the state and the round key (derived from the secret key using a key expansion algorithm) .
- The final round omits the MixColumns step .
- AES decryption is the **inverse** of AES encryption, using the same key but in reverse order .
- AES decryption also involves four steps: **InvSubBytes**, **InvShiftRows**, **InvMixColumns**, and **AddRoundKey** .
- InvSubBytes is the inverse of SubBytes, using a different lookup table called the inverse S-box .
- InvShiftRows is the inverse of ShiftRows, shifting each row to the right instead of the left .
- InvMixColumns is the inverse of MixColumns, using a different matrix for the multiplication .
- AddRoundKey is the same as in encryption, but using the round keys in reverse order .
- AES is considered to be a **secure** and **efficient** algorithm for encryption and decryption, and is widely used in various applications and protocols .

: What Is the Advanced Encryption Standard (AES)? | U.S. News
: FIPS 197, Advanced Encryption Standard | CSRC - NIST
: Advanced Encryption Standard (AES) | NIST