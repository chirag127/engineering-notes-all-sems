### Triple DES

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block .
- It is a simple method of increasing the key size of DES to protect against brute-force attacks, without the need to design a new block cipher algorithm.
- The key size of 3DES is 168 bits, but due to the meet-in-the-middle attack, the effective security it provides is only 112 bits.
- 3DES uses the DES cipher three times in one of the following modes :
  - Encrypt-Decrypt-Encrypt (EDE): The first key is used to encrypt the plaintext, the second key is used to decrypt the intermediate ciphertext, and the third key is used to encrypt the final ciphertext.
  - Encrypt-Encrypt-Encrypt (EEE): The first key is used to encrypt the plaintext, the second key is used to encrypt the intermediate ciphertext, and the third key is used to encrypt the final ciphertext.
- 3DES can use either two keys (K1 and K2) or three keys (K1, K2, and K3) for encryption and decryption :
  - If two keys are used, then K1=K3 for EDE mode and K2=K3 for EEE mode.
  - If three keys are used, then K1, K2, and K3 are all different.
- 3DES is more secure than DES, but it is also slower and more complex .
- 3DES is being phased out by more modern and efficient block ciphers, such as AES .