Triple DES is a symmetric-key block cipher that applies the DES algorithm three times to each data block, using either two or three different keys. It was developed to increase the security of DES, which has a relatively small key size of 56 bits. Triple DES has a key size of either 112 or 168 bits, depending on the number of keys used.

The following diagram illustrates the basic architecture of Triple DES, using three keys K1, K2, and K3. The data block is first encrypted with K1, then decrypted with K2, and finally encrypted again with K3. The output is the ciphertext. To decrypt, the process is reversed: the ciphertext is decrypted with K3, encrypted with K2, and decrypted with K1. The output is the original plaintext.

```
+-----+     +-----+     +-----+
| K1  |     | K2  |     | K3  |
+-----+     +-----+     +-----+
   |           |           |
   |           |           |
   v           v           v
+-----+     +-----+     +-----+
| DES |     | DES |     | DES |
| ENC |     | DEC |     | ENC |
+-----+     +-----+     +-----+
   |           |           |
   |           |           |
   v           v           v
+-----+     +-----+     +-----+
|     |     |     |     |     |
| P   |---->| C1  |---->| C2  |----> C
|     |     |     |     |     |
+-----+     +-----+     +-----+
```

To decrypt:

```
+-----+     +-----+     +-----+
| K3  |     | K2  |     | K1  |
+-----+     +-----+     +-----+
   |           |           |
   |           |           |
   v           v           v
+-----+     +-----+     +-----+
| DES |     | DES |     | DES |
| DEC |     | ENC |     | DEC |
+-----+     +-----+     +-----+
   |           |           |
   |           |           |
   v           v           v
+-----+     +-----+     +-----+
|     |     |     |     |     |
| C   |---->| C2  |---->| C1  |----> P
|     |     |     |     |     |
+-----+     +-----+     +-----+
```