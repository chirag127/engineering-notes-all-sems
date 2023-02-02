### Authentication header for the notes of the Unit 7 - IP Security in the subject of Cryptography & Network Security
The Authentication Header (AH) is a protocol for providing data integrity and authentication for IP datagrams. It is used in conjunction with the Internet Protocol Security (IPSec) suite of protocols. The AH protects the entire IP datagram, including both the header and payload, against tampering and replay attacks.

The AH operates at the IP layer and is transparent to higher-layer protocols such as TCP and UDP. The AH provides a mechanism for verifying the authenticity of the source of an IP datagram and its contents.

The AH uses a keyed hash function to generate a message authentication code (MAC) that is appended to the IP datagram. The MAC is generated using a shared secret key that is established between the communicating parties. The recipient of the datagram can use the key to verify the integrity of the datagram and its source.

The AH provides protection against tampering with the IP header fields, such as source and destination addresses, and the payload. It does not provide confidentiality for the IP datagram, as the contents of the datagram are still visible to attackers.

In summary, the Authentication Header is a key component of IPSec, providing data integrity and authentication for IP datagrams.
