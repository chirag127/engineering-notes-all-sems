### Triple DES

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block. 
- It is officially called the Triple Data Encryption Algorithm (TDEA or Triple DEA). 
- It was designed to increase the key size of DES, which has 56 bits and is vulnerable to brute-force attacks. 
- Triple DES can use two or three different keys, resulting in 112 or 168 bits of security respectively. 
- However, due to some attacks, the effective security of Triple DES is less than the key size. For example, a 112-bit key can be broken with 2^32 known plaintexts and 2^113 operations. 
- Triple DES has been deprecated by NIST in 2017 for new applications and will be disallowed for all applications by the end of 2023.  
- It has been replaced by the more secure and efficient AES algorithm. 
- Triple DES can operate in different modes, such as ECB, CBC, CFB, OFB, and CTR, which affect how the data blocks are encrypted and decrypted.  
- Triple DES uses a Feistel structure, which consists of 16 rounds of substitution and permutation operations, followed by a final swap of the left and right halves.  
- Triple DES applies this structure three times, with either the same key (EEE mode) or different keys (EDE mode) for encryption and decryption.