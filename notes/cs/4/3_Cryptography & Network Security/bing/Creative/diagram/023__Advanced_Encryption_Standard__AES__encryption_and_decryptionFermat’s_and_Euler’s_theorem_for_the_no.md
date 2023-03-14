The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt data using the same key. The key can have a length of 128, 192, or 256 bits, and the data is processed in blocks of 128 bits. The AES algorithm consists of four main steps: byte substitution, row shift, column mix, and key addition. These steps are repeated for a number of rounds, depending on the key length. The encryption and decryption processes are similar, except that the key addition step uses the inverse key schedule and the column mix step is skipped in the last round.

The following diagram illustrates the basic architecture of the AES encryption and decryption process using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Plain Text     |    |  Cipher Text    |    |  Plain Text     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Key Expansion  |    |  Key Expansion  |    |  Key Expansion  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Add Round Key  |    |  Add Round Key  |    |  Add Round Key  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Sub Bytes      |    |  Inv Sub Bytes  |    |  Sub Bytes      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Shift Rows     |    |  Inv Shift Rows |    |  Shift Rows     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Mix Columns    |    |  Inv Mix Columns|    |  Mix Columns    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Add Round Key  |    |  Add Round Key  |    |  Add Round Key  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         V