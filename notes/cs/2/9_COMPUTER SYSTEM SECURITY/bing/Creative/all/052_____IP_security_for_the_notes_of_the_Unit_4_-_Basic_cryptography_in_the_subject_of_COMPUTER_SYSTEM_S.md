# IP security

IP security (IPsec) is a suite of protocols and algorithms for securing data transmitted over the internet or any public network. It provides security at the IP layer through authentication and encryption of IP network packets .

## Features of IPsec

- IPsec can secure traffic for all applications, without having to make any modifications to the applications.
- IPsec can encrypt application layer data, provide security for routers sending routing data across the public internet, provide authentication without encryption, and protect network data from replay attacks.
- IPsec can operate in two modes: transport mode and tunnel mode. In transport mode, only the payload of the IP packet is encrypted or authenticated. In tunnel mode, the entire IP packet is encrypted or authenticated, and then encapsulated in a new IP packet .
- IPsec can use two protocols: Authentication Header (AH) and Encapsulating Security Payload (ESP). AH provides data integrity and authentication, but not encryption. ESP provides data integrity, authentication, and encryption .

## Components of IPsec

- IPsec consists of the following components :

  - Security Association (SA): A set of parameters that defines how IPsec should secure a communication session between two hosts. An SA includes the mode, the protocol, the encryption and authentication algorithms, the keys, and the lifetime of the SA.
  - Security Parameter Index (SPI): A 32-bit identifier that uniquely identifies an SA. The SPI is carried in the AH or ESP header of the IPsec packet.
  - Key Management Protocol: A protocol that establishes and maintains the SAs and the keys. The most common key management protocol for IPsec is the Internet Key Exchange (IKE), which consists of two phases: IKE Phase 1 and IKE Phase 2.
  - IPsec Policy: A set of rules that determines which traffic should be secured by IPsec and how. The IPsec policy can be configured manually or dynamically by IKE.

## Process of IPsec

- The process of IPsec can be summarized as follows:

  - Host recognition: The IPsec process begins when a host system recognizes that a packet needs protection and should be processed by IPsec.
  - Negotiation, or IKE Phase 1: In the second step, the hosts use IPsec to negotiate the set of policies they will use for the communication session. This step establishes an IKE SA, which is a secure channel for exchanging keys and other information.
  - IPsec circuit, or IKE Phase 2: In the third step, the hosts use the IKE SA to establish one or more IPsec SAs, which are used to secure the actual data packets. This step also generates the keys for encryption and authentication.
  - Data transfer: In the fourth step, the hosts use the IPsec SAs to encrypt, authenticate, and optionally compress the data packets. The packets are then sent over the network with the AH or ESP header, depending on the protocol used.
  - Termination: In the final step, the IPsec SAs are terminated when they expire or when the communication session ends. The keys and the policies are also deleted.