# IP security

- IP security (IPSec) is a suite of protocols and algorithms for securing data transmitted over the internet or any public network.
- IPSec provides data authentication, integrity, and confidentiality by encrypting, decrypting, and authenticating IP packets.
- IPSec operates at the IP layer, which means it can secure traffic for all applications, without requiring any modifications to the applications .
- IPSec consists of two main components: Security Associations (SAs) and Security Protocols.
  - SAs are logical connections that define the security parameters for a communication session, such as the encryption algorithm, the authentication algorithm, the key, and the mode.
  - Security Protocols are the mechanisms that implement the security functions of IPSec, such as Authentication Header (AH) and Encapsulating Security Payload (ESP).
    - AH provides data authentication and integrity, but not confidentiality, by adding a header to the IP packet that contains a message authentication code (MAC) computed from the packet and a shared secret key.
    - ESP provides data confidentiality, authentication, and integrity, by encrypting the payload of the IP packet and adding a header and a trailer that contain a MAC and other information.
- IPSec can operate in two modes: transport mode and tunnel mode.
  - Transport mode is used for end-to-end communication, where the original IP header is preserved and only the payload is encrypted and/or authenticated.
  - Tunnel mode is used for gateway-to-gateway communication, where the entire IP packet is encrypted and/or authenticated and encapsulated in a new IP packet with a new header.