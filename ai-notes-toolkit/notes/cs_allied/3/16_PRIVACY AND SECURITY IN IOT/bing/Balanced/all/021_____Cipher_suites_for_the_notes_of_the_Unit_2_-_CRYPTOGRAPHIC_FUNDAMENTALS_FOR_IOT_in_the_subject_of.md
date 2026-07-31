### Cipher suites

- A cipher suite is a set of cryptographic algorithms that are used to secure the communication between two parties in a network.
- A cipher suite consists of four components: a key exchange algorithm, a bulk encryption algorithm, a message authentication code (MAC) algorithm, and a pseudorandom function (PRF).
- The key exchange algorithm is used to establish a shared secret key between the communicating parties, which is then used to encrypt and decrypt the data.
- The bulk encryption algorithm is used to encrypt and decrypt the data using the shared secret key.
- The MAC algorithm is used to verify the integrity and authenticity of the data, by generating and checking a tag that is appended to the data.
- The PRF is used to derive additional keys and nonces from the shared secret key, using a hash function and a secret input.
- A cipher suite is usually denoted by a string of the form `KEX_WITH_ENC_MAC_PRF`, where `KEX` is the key exchange algorithm, `ENC` is the bulk encryption algorithm, `MAC` is the MAC algorithm, and `PRF` is the PRF.
- For example, `ECDHE_RSA_WITH_AES_128_GCM_SHA256` is a cipher suite that uses Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) as the key exchange algorithm, RSA as the digital signature algorithm, AES-128 in Galois/Counter Mode (GCM) as the bulk encryption algorithm, SHA-256 as the MAC algorithm, and SHA-256 as the PRF.
- Cipher suites are negotiated between the communicating parties during the handshake protocol, where they exchange their supported cipher suites and agree on the most preferred one.
- The choice of a cipher suite depends on various factors, such as the security level, the performance, the compatibility, and the regulatory requirements of the communication.
- Some of the common cipher suites used in IoT are:

  - `TLS_PSK_WITH_AES_128_CCM_8`: This cipher suite uses Pre-Shared Key (PSK) as the key exchange algorithm, AES-128 in Counter with CBC-MAC (CCM) mode as the bulk encryption and MAC algorithm, and SHA-256 as the PRF. It is suitable for resource-constrained IoT devices that have a pre-established secret key with the server.
  - `TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`: This cipher suite uses ECDHE as the key exchange algorithm, ECDSA as the digital signature algorithm, AES-128 in CCM mode as the bulk encryption and MAC algorithm, and SHA-256 as the PRF. It is suitable for IoT devices that support elliptic curve cryptography and want to achieve forward secrecy and mutual authentication.
  - `TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256`: This cipher suite uses ECDHE as the key exchange algorithm, PSK as the authentication algorithm, AES-128 in Cipher Block Chaining (CBC) mode as the bulk encryption algorithm, SHA-256 as the MAC algorithm, and SHA-256 as the PRF. It is suitable for IoT devices that want to combine the benefits of PSK and ECDHE, such as low computational cost and forward secrecy.