### Transport Layer Security (TLS)

- Transport Layer Security (TLS) is a cryptographic protocol that provides privacy and data security for communications over the Internet .
- TLS operates on top of the Transport Layer of the TCP/IP model, and can be used by various applications such as web browsers, email, instant messaging, and voice over IP .
- The main goals of TLS are to:
  - Encrypt the data exchanged between two parties, such as a client and a server, to prevent eavesdropping and tampering .
  - Authenticate the identity of the parties, such as using certificates and digital signatures, to prevent impersonation and spoofing .
  - Ensure the integrity of the data, such as using message authentication codes and hashes, to detect any modification or corruption .
- The basic steps of TLS are as follows  :
  - The client initiates a connection to the server and sends a list of supported TLS versions, cipher suites, and extensions.
  - The server responds with its chosen TLS version, cipher suite, and extensions, and sends its certificate and public key.
  - The client verifies the server's certificate and public key, and optionally sends its own certificate and public key if requested by the server.
  - The client and the server use a key exchange algorithm, such as Diffie-Hellman or RSA, to generate a shared secret key, called the pre-master secret.
  - The client and the server use the pre-master secret and some random values to derive the master secret, which is used to generate the session keys for encryption and authentication.
  - The client and the server exchange messages to confirm that they have successfully computed the same session keys, and then switch to the encrypted mode.
  - The client and the server exchange application data, such as HTTP requests and responses, using the session keys to encrypt and authenticate each message.
  - The client and the server exchange messages to close the connection and delete the session keys.
- TLS supports various cipher suites, which are combinations of encryption, authentication, and key exchange algorithms, such as AES, SHA, and ECDHE .
- TLS also supports various extensions, which are optional features that enhance the functionality or performance of the protocol, such as Server Name Indication, Session Resumption, and Application-Layer Protocol Negotiation .
- TLS is the successor of Secure Sockets Layer (SSL), which is an older and less secure version of the protocol. The current version of TLS is 1.3, which was published in 2018 and introduced several improvements, such as removing obsolete cipher suites, reducing the number of round trips, and encrypting more handshake messages  .