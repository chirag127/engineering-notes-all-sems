 Here is the content in Markdown format:

### Software Version Control

- Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.
- Version control allows you to revert a file or project to a previous version, revert the entire project to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more.
- Using a VCS also generally means that if you screw things up or lose files, you can easily recover. In addition, you get all this for very little overhead.
- Some popular version control systems are:
    - Git - Distributed VCS, free and open source, fast, scalable
    - Mercurial - Distributed VCS, free and open source
    - Subversion - Centralized VCS, free and open source
- Advantages:
    - Backup and Recovery
    - Track Changes
    - Collaboration
    - Parallel Development
- Disadvantages:
    - Steep Learning Curve
    - Reliance on tool
- Applications: Software Development, Website Development, Document Changes Tracking, etc.

[Detailed diagrams and examples can be added if required]

### Process-to-process delivery in transport layer

- The transport layer provides process-to-process delivery of the entire message.
- It ensures that the whole message arrives unmodified, in the right order, and without errors or duplications.
- Two protocols operate at the transport layer:
    - Transmission Control Protocol (TCP) - Provides reliable, ordered, and error-checked delivery of transmitted data.
    - User Datagram Protocol (UDP) - Provides fast but unreliable datagram service.
- TCP provides reliability through:
    - Sequence numbers - Numbers packets to ensure they are delivered in correct order. Out-of-order packets are buffered until missing packets arrive.
    - Acknowledgements - Receiver sends ACK to confirm correct packet reception. Sender retransmits if ACK is not received.
    - Checksums - Detect data corruption. Damaged packets are discarded and retransmitted.
- UDP provides fast but unreliable data delivery. No ordering, error-checking or congestion control. Used for real-time traffic where speed is more important than reliability (e.g. video streaming).
- Advantages of TCP: Reliability, Ordering, Congestion Control. Disadvantage: Slow.
- Advantages of UDP: Fast. Disadvantages: Unreliable, No ordering or congestion control.

[Diagrams and examples of TCP and UDP can be added if required]