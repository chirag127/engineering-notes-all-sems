Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application. It gives developers more control over what gets encrypted and who gets the keys for decryption. It also improves privacy and access control by using end-to-end encryption and key management policies .

A possible diagram for cryptography in application layer is:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Encryption    |    |   Encryption    |    |   Encryption    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Transport     |    |   Transport     |    |   Transport     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
                 |                    |
       +-----------------+    +-----------------+
       |                 |    |                 |
       |   Physical      |    |   Physical      |
       |                 |    |                 |
       +-----------------+    +-----------------+
       |                 |    |                 |
       |   Network       |    |   Network       |
       |                 |    |                 |
       +-----------------+    +-----------------+
       |                 |    |                 |
       |   Transport     |    |   Transport     |
       |                 |    |                 |
       +-----------------+    +-----------------+
       |                 |    |                 |
       |   Encryption    |    |   Encryption    |
       |                 |    |                 |
       +-----------------+    +-----------------+
       |                 |    |                 |
       |   Application   |    |   Application   |
       |                 |    |                 |
       +-----------------+    +-----------------+
```

The diagram shows how data is encrypted and decrypted at the application layer, before and after being transmitted over the network. The encryption and decryption keys are managed by the applications or the users themselves, not by the lower layers of the network stack. This ensures that only the intended recipients can access the data, even if the network or the transport layer is compromised. The encryption and decryption algorithms can be chosen by the developers or the users, depending on their security and performance requirements. The encryption and decryption processes can also be integrated with the application logic, such as authentication, authorization, and data validation.