### Cipher suites for the notes of the Unit 2 - CRYPTOGRAPHIC FUNDAMENTALS FOR IOT in the subject of PRIVACY AND SECURITY IN IOT

- Cipher suites are collections of algorithms that can work together to perform the handshake and the encryption/decryption that follows.
- Cipher suites provide a set of algorithms and protocols required to secure communications between clients and servers.
- The agreed cipher suite is a combination of four components:
  - Key exchange algorithm, such as RSA, DH, ECDH, DHE, ECDHE, or PSK
  - Authentication/Digital Signature Algorithm, such as RSA, ECDSA, or DSA
  - Bulk encryption algorithm, such as AES, CHACHA20, Camellia, or ARIA
  - Message Authentication Code algorithm, such as SHA-256, and POLY1305
- Cipher suites are negotiated between the client and the server at the beginning of the TLS connection, based on the supported and preferred cipher suites of each party .
- Cipher suites are identified by a standard name, such as TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, which indicates the key exchange, authentication, encryption, and MAC algorithms used.
- Cipher suites for IoT devices should be chosen based on the security, performance, and compatibility requirements of the application  .
- Some examples of IoT platforms and their supported or recommended cipher suites are  :
  - Azure IoT Hub: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
  - Azure IoT Device Provisioning Service: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P384 (legacy)
  - AWS IoT Core: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384