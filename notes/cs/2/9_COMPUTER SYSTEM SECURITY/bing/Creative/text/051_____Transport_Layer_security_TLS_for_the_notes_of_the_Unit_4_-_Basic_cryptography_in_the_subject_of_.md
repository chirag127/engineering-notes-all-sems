### Transport Layer Security (TLS)

- Transport Layer Security (TLS) is a cryptographic protocol that provides privacy and data security for communications over the Internet .
- TLS operates on top of the TCP/IP transport layer and adds encryption, authentication, and integrity protection to the data transmitted.
- TLS uses both symmetric encryption and public key encryption to establish a secure session between two parties, such as a web browser and a web server .
- The main steps of the TLS protocol are :
  - Handshake: The two parties negotiate the protocol version, cipher suite, and key exchange method, and authenticate each other using digital certificates or other means.
  - Key exchange: The two parties generate and exchange cryptographic keys to be used for symmetric encryption of the data.
  - Data transfer: The two parties encrypt and decrypt the data using the agreed symmetric key and append a message authentication code (MAC) to detect any tampering.
  - Connection termination: The two parties close the secure session and optionally resume it later with a shorter handshake.
- TLS supports various cryptographic algorithms and parameters, which are grouped into cipher suites. A cipher suite specifies the key exchange method, the encryption algorithm, the MAC algorithm, and the pseudorandom function (PRF) used in the TLS protocol .
- TLS also supports various extensions that add functionality or improve performance, such as server name indication (SNI), session resumption, application layer protocol negotiation (ALPN), and encrypted server name indication (ESNI) .
- TLS is the successor of the Secure Sockets Layer (SSL) protocol, which is now deprecated and insecure. The current version of TLS is 1.3, which was published in 2018 and introduced several improvements, such as faster handshake, stronger encryption, and more secure key exchange  .