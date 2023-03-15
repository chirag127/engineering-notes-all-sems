### Point-to-point networks in network layer

A point-to-point network is a network topology that consists of two nodes connected by a single link. The link can be a physical cable, a wireless connection, or a logical tunnel. Point-to-point networks are often used to connect two routers or two hosts over a wide area network (WAN).

One of the common protocols used in point-to-point networks is the Point-to-Point Protocol (PPP). PPP is a data link layer protocol that encapsulates multiprotocol data into frames for transmission over the link. PPP also provides features such as authentication, encryption, and compression. PPP can be used over various types of links, such as serial, Ethernet, or ATM.

The basic structure of a PPP frame is as follows:

```
+----------+----------+----------+----------+----------+
| Flag     | Address  | Control  | Protocol | Data     |
| (1 byte) | (1 byte) | (1 byte) | (2 bytes)| (variable)|
+----------+----------+----------+----------+----------+
| FCS      | Flag     |
| (2 bytes)| (1 byte) |
+----------+----------+
```

The flag field marks the beginning and end of a frame with the value 0x7E. The address field is usually set to 0xFF, which means broadcast. The control field is usually set to 0x03, which means unnumbered information. The protocol field identifies the type of data carried in the frame, such as IP, IPv6, or LCP. The data field contains the encapsulated data, which can be variable in length. The FCS field is a checksum that detects errors in the frame.

PPP also uses the Link Control Protocol (LCP) to establish, configure, and test the link. LCP uses special frames called LCP packets, which have the protocol field set to 0xC021. LCP packets can perform various functions, such as negotiating options, exchanging authentication information, or signaling errors. LCP packets have the following format:

```
+----------+----------+----------+----------+----------+
| Code     | Identifier| Length  | Data     |
| (1 byte) | (1 byte)  | (2 bytes)| (variable)|
+----------+----------+----------+----------+
```

The code field specifies the type of LCP packet, such as configure-request, configure-ack, or terminate-request. The identifier field is a number that matches the request and the response. The length field indicates the total length of the packet, including the header. The data field contains the information specific to the code, such as options or authentication data.