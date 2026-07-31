# Triple DES

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block .
- It is a simple method of increasing the key size of DES to protect against brute-force attacks, without the need to design a new block cipher algorithm.
- The key size of 3DES is 168 bits, but due to the meet-in-the-middle attack, the effective security it provides is only 112 bits.
- 3DES uses the DES cipher three times in one of the following modes :
  - Encrypt-Decrypt-Encrypt (EDE): The first key is used to encrypt the data, the second key is used to decrypt the data, and the third key is used to encrypt the data again.
  - Encrypt-Encrypt-Encrypt (EEE): The first key is used to encrypt the data, the second key is used to encrypt the data again, and the third key is used to encrypt the data once more.
- 3DES can use either two keys (K1 and K2) or three keys (K1, K2, and K3) for encryption and decryption :
  - Two-key 3DES: The same key (K1) is used for the first and third encryption/decryption, and a different key (K2) is used for the second encryption/decryption. The key size is 112 bits.
  - Three-key 3DES: Three different keys (K1, K2, and K3) are used for each encryption/decryption. The key size is 168 bits.
- 3DES is more secure than DES, but it is also slower and more complex .
- 3DES is being phased out by newer and more efficient encryption algorithms, such as AES .