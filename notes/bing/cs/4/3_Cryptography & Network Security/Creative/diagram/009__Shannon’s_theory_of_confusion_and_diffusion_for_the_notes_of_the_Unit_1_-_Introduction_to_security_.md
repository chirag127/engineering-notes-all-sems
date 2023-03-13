According to Wikipedia, confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography. These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis.

Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible; diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.

A possible diagram to illustrate Shannon's theory of confusion and diffusion is as follows:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Plaintext    |    |   Ciphertext   |    |   Plaintext    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Key 1        |    |   Key 2        |    |   Key 1        |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Confusion    |    |   Confusion    |    |   Confusion    |
|   Function     |    |   Function     |    |   Function     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Diffusion    |    |   Diffusion    |    |   Diffusion    |
|   Function     |    |   Function     |    |   Function     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        v                     v                     v
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Ciphertext   |    |   Plaintext    |    |   Ciphertext   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The diagram shows how the plaintext is transformed into ciphertext by applying a confusion function and a diffusion function with the help of two keys. The confusion function makes the ciphertext depend on the key in a complex way, while the diffusion function spreads the influence of each plaintext bit over many ciphertext bits. The same process is reversed to decrypt the ciphertext back into plaintext. The diagram is based on the idea of a Feistel cipher, which is a common structure for block ciphers.