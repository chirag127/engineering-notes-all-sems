The OSI reference model in Computer Networks is a conceptual framework that describes how information from a software application in one computer moves through a physical medium to the software application in another computer. It consists of seven layers, each with its own function and protocols. The layers are:

- Application Layer: This layer interacts with the user and provides services such as web browsing, email, file transfer, etc.
- Presentation Layer: This layer formats and encrypts the data for the application layer and handles issues such as data compression, character encoding, etc.
- Session Layer: This layer establishes, maintains, and terminates the communication sessions between the applications.
- Transport Layer: This layer provides reliable and efficient data transfer between the end systems and handles issues such as flow control, error control, segmentation, etc.
- Network Layer: This layer provides routing and forwarding of data packets across different networks and handles issues such as addressing, congestion control, etc.
- Data Link Layer: This layer provides error-free transmission of data frames over the physical layer and handles issues such as framing, addressing, error detection, etc.
- Physical Layer: This layer transmits the individual bits over the physical medium and handles issues such as signaling, modulation, synchronization, etc.

The following diagram illustrates the basic architecture of the OSI reference model in Computer Networks using ASCII art:

```
+----------------+ +----------------+ +----------------+
| Application    | | Application    | | Application    |
+----------------+ +----------------+ +----------------+
| Presentation   | | Presentation   | | Presentation   |
+----------------+ +----------------+ +----------------+
| Session        | | Session        | | Session        |
+----------------+ +----------------+ +----------------+
| Transport      | | Transport      | | Transport      |
+----------------+ +----------------+ +----------------+
| Network        | | Network        | | Network        |
+----------------+ +----------------+ +----------------+
| Data Link      | | Data Link      | | Data Link      |
+----------------+ +----------------+ +----------------+
| Physical       | | Physical       | | Physical       |
+----------------+ +----------------+ +----------------+
    | | | | | | |     | | | | | | |     | | | | | | |
    v v v v v v v     v v v v v v v     v v v v v v v
+----------------+ +----------------+ +----------------+
| Physical Medium| | Physical Medium| | Physical Medium|
+----------------+ +----------------+ +----------------+
```