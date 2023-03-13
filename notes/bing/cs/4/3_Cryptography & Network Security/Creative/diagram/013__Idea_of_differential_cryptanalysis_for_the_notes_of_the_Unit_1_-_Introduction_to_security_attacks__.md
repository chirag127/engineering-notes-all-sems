Differential cryptanalysis is a technique that exploits the relationship between the differences in the input plaintexts and the differences in the output ciphertexts of a block cipher. It can be used to recover the secret key of a cipher by analyzing a large number of plaintext-ciphertext pairs with a fixed difference.

The following diagram illustrates the basic idea of differential cryptanalysis using a simple example of a 4-bit block cipher with 2 rounds and a 4-bit key for each round. The diagram shows how a pair of plaintexts with a fixed difference of 0011 (denoted by ΔP) is encrypted using the same key, and how the difference in the ciphertexts (denoted by ΔC) is computed. The diagram also shows how the difference in the ciphertexts can be used to guess the last round key by applying the inverse of the last round function to both ciphertexts and comparing the differences in the intermediate values.

```
+----------------+    +----------------+    +----------------+
| Plaintext P1   |    | Plaintext P2   |    | Difference ΔP  |
+----------------+    +----------------+    +----------------+
| 0101           |    | 0110           |    | 0011           |
+----------------+    +----------------+    +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+    +----------------+    +----------------+
| Round 1        |    | Round 1        |    | Round 1        |
+----------------+    +----------------+    +----------------+
| F(P1, K1)      |    | F(P2, K1)      |    | F(ΔP, K1)      |
+----------------+    +----------------+    +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+    +----------------+    +----------------+
| Round 2        |    | Round 2        |    | Round 2        |
+----------------+    +----------------+    +----------------+
| F(P1', K2)     |    | F(P2', K2)     |    | F(ΔP', K2)     |
+----------------+    +----------------+    +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+    +----------------+    +----------------+
| Ciphertext C1  |    | Ciphertext C2  |    | Difference ΔC  |
+----------------+    +----------------+    +----------------+
| 1100           |    | 1010           |    | 0110           |
+----------------+    +----------------+    +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+    +----------------+    +----------------+
| Inverse Round 2|    | Inverse Round 2|    | Inverse Round 2|
+----------------+    +----------------+    +----------------+
| F-1(C1, K2)    |    | F-1(C2, K2)    |    | F-1(ΔC, K2)    |
+----------------+    +----------------+    +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+    +----------------+    +----------------+
| Guess K2       |    | Guess K2       |    | Guess K2       |
+----------------+    +----------------+    +----------------+
| ΔP1' = ΔC1'    |    | ΔP2' = ΔC2'    |    | ΔP' = ΔC'      |
+----------------+    +----------------+    +----------------+
```

The function F is the round function of the cipher, which takes a 4-bit input and a 4-bit key and produces a 4-bit output. The function F-1 is the inverse of F, which takes a 4-bit output and a 4-bit key and produces a 4-bit input. The notation P1', P2', ΔP', C1', C2', ΔC', ΔP1', ΔP2', ΔC1', and ΔC2' denotes the intermediate values after applying F or F-1 to the corresponding inputs or outputs.

The goal of differential