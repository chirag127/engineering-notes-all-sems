### IP security

IP security (IPsec) is a suite of protocols and algorithms for securing data transmitted over the internet or any public network. It provides data authentication, integrity, and confidentiality. It also defines the encrypted, decrypted and authenticated packets.

Some features of IP security are:

- It allows individual users or organizations to secure traffic for all applications, without having to make any modifications to the applications .
- It operates at the IP layer, which means it can protect any IP-based application, such as web, email, file transfer, etc.
- It uses security associations (SAs), which are the building blocks of secure communications. SAs are agreements between two or more parties on how to secure the data exchange. SAs include parameters such as encryption algorithm, authentication algorithm, key length, mode of operation, etc .
- It supports two modes of operation: transport mode and tunnel mode. Transport mode encrypts and authenticates only the payload of the IP packet, leaving the IP header intact. Tunnel mode encrypts and authenticates the entire IP packet, and encapsulates it in a new IP header. Transport mode is suitable for end-to-end communications, while tunnel mode is suitable for gateway-to-gateway communications .
- It uses two main protocols: Authentication Header (AH) and Encapsulating Security Payload (ESP). AH provides data authentication and integrity, but not confidentiality. ESP provides data authentication, integrity, and confidentiality. AH and ESP can be used separately or together, depending on the security requirements .