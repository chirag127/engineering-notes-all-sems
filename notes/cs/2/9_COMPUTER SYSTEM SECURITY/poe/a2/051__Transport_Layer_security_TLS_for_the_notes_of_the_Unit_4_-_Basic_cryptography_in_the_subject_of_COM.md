 Here is the content in markdown format without any emojis or external links:

### Transport Layer Security (TLS)

- TLS is a protocol that provides security and data integrity for communications over networks such as the Internet. It sits on top of a reliable transport layer protocol (like TCP), underneath application-level protocols (like HTTP or SMTP).
- TLS uses X.509 certificates and hence asymmetric cryptography to authenticate the server and/or client and establish a symmetric session key, which is then used to encrypt application data flowing over the connection using a symmetric cipher like AES.
- The TLS handshake involves the following steps:
  - The client sends a ClientHello message containing the highest TLS version it supports, a random number, and a list of cipher suites it supports.
  - The server responds with a ServerHello containing the selected TLS version, random number, and cipher suite. It also sends its certificate.
  - The client verifies the server's certificate and sends a ClientKeyExchange message containing a premaster secret encrypted with the server's public key.
  - Using the premaster secret, both sides generate the master secret and use it to derive encryption/decryption keys and MAC keys for the connection.
  - The client sends a ChangeCipherSpec message indicating that subsequent data will be encrypted, followed by a Finished message that is encrypted and signed with the derived keys.
  - The server verifies the client Finished message and replies with its own ChangeCipherSpec and Finished messages.
  - Application data can now be sent over the encrypted TLS connection.
- TLS 1.3 simplified the handshake, removed insecure/weak cipher suites, and uses authenticated encryption with associated data (AEAD) ciphers to provide confidentiality and integrity in a single step.