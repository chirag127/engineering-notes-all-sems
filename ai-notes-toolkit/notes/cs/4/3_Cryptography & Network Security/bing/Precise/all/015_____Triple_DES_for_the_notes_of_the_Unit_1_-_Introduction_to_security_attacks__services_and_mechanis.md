# Triple DES

Triple DES (3DES) is a symmetric key block cipher that applies the Data Encryption Standard (DES) algorithm three times to each data block. It was developed to provide a more secure alternative to the original DES algorithm, which was found to be vulnerable to brute-force attacks.

1. Triple DES uses a "key bundle" that consists of three DES keys, K1, K2 and K3, each of 56 bits (excluding parity bits).
2. The encryption algorithm is: ciphertext = EK3(DK2(EK1(plaintext)))
3. The decryption algorithm is: plaintext = DK1(EK2(DK3(ciphertext)))
4. Triple DES can also be used with two keys, where K1 and K3 are the same. In this case, the encryption algorithm becomes: ciphertext = EK1(DK2(EK1(plaintext)))
5. Triple DES is considered to be significantly more secure than DES, due to its longer key length.
6. However, it is also slower than DES, due to the need to apply the algorithm three times.
7. Triple DES has been widely adopted in various applications, including financial transactions and secure communications.
8. Despite its improved security over DES, Triple DES is still considered to be vulnerable to certain attacks, and its use is being phased out in favor of more secure algorithms such as AES.
