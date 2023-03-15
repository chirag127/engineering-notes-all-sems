 Here is the formal content on the given topic:

### Process-to-process delivery in transport layer

1. The transport layer provides process-to-process delivery of the entire message. It receives messages from the upper layers, splits the messages into segments and reassembles them at the destination.
2. Each segment includes a sequencing number so that the transport layer protocol can reassemble the segments in the correct order at the destination.
3. The transport layer provides an interface between the upper layers and the network layer. It masks the network layer from the upper layers. The transport layer handles segmenting and reassembling the message.
4. The transport layer also controls the flow of segments, including detection of missing and duplicate segments. It provides mechanisms to ensure all segments arrive and are in the correct sequence.
5. Two protocols that provide process-to-process delivery in the transport layer are:
    - Transmission Control Protocol (TCP) which provides a reliable, in-order delivery of bytes.
    - User Datagram Protocol (UDP) which provides fast delivery of unordered messages with no error correction.

The above points cover the key aspects of process-to-process delivery in the transport layer. The transport layer ensures the complete and correct delivery of the messages passed from the upper layers by handling segmentation, reassembly, sequence control and flow control.