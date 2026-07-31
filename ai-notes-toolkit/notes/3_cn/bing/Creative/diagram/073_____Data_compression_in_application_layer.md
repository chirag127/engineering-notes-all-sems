Data compression is the function of presentation layer in OSI reference model. Compression is often used to maximize the use of bandwidth across a network or to optimize disk space when saving data. Data compression allows to reduce the number of bits that needs to be transmitted on the network. Data compression can be performed by various algorithms, such as Huffman coding, run-length encoding, Lempel-Ziv-Welch (LZW) algorithm, etc.

### Data compression in application layer

The application layer is the topmost layer of the OSI model, which provides the user interface and support for services like email, file transfer, web browsing, etc. The application layer also identifies constraints at the application level such as those associated with authentication, privacy, quality of service, networking devices, and data syntax. The application layer helps us to identify communication partners, and synchronizing communication. The application layer can use data compression to reduce the size of the data before sending it to the lower layers.

A possible ASCII diagram for data compression in application layer is:

```
+-----------------+   +-----------------+   +-----------------+
| Application     |   | Application     |   | Application     |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
| +-------------+ |   | +-------------+ |   | +-------------+ |
| | Compression | |   | | Compression | |   | | Compression | |
| | Algorithm   | |   | | Algorithm   | |   | | Algorithm   | |
| +-------------+ |   | +-------------+ |   | +-------------+ |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Presentation    |   | Presentation    |   | Presentation    |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Session         |   | Session         |   | Session         |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Transport       |   | Transport       |   | Transport       |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Network         |   | Network         |   | Network         |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Data Link       |   | Data Link       |   | Data Link       |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Physical        |   | Physical        |   | Physical        |
| Layer           |   | Layer           |   | Layer           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+

    Sender               Intermediate              Receiver
    Device                Device(s)                Device
```