Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers. This application layer encryption approach increases security by reducing the number of potential attack vectors. Application-layer encryption, or shift-left cryptography, means giving developers more control over what gets encrypted and who gets the keys for decryption. End-to-end encryption is an increasingly popular type of application-layer cryptography. This type of encryption lets organizations enforce access control using key management as well as policy.

### Cryptography in application layer

The following diagram illustrates the basic architecture of a cryptography in application layer:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Application  |    |   Application  |    |   Application  |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Encryption   |    |   Encryption   |    |   Encryption   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|     Data       |    |     Data       |    |     Data       |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Storage     |    |    Storage     |    |    Storage     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

Each application has its own encryption layer that encrypts and decrypts the data before storing or retrieving it from the storage layer. The encryption layer can use symmetric or asymmetric encryption algorithms, depending on the use case and the security requirements. The encryption keys are managed by the application or by a separate key management service. The encryption layer can also implement policies to control who can access the data and under what conditions. The encryption layer can also provide integrity and authenticity checks to ensure the data is not tampered or forged. The encryption layer can also support end-to-end encryption, where the data is encrypted by the sender and decrypted by the receiver, without any intermediate decryption by the application or the storage layer. This ensures that only the intended parties can access the data, even if the application or the storage layer is compromised.