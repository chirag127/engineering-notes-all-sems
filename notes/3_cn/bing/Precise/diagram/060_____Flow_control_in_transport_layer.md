### Flow control in transport layer

Flow control is a mechanism used in the transport layer of the TCP/IP model to manage the rate of data transmission between two nodes. It is necessary to prevent a fast sender from transmitting more data than can be supported by the receiving data buffer, causing a buffer overrun. This can also be used to improve efficiency by reducing buffer underrun.

The transport layer provides a flow control mechanism between the adjacent layers of the TCP/IP model. TCP also prevents data loss due to a fast sender and slow receiver by imposing some flow control techniques .

Flow control in the transport layer ensures the delivery of the message globally, as the two points of connection over this protocol are logically connected. Whereas in the data-link layer, the concern is to deliver the message locally, as the two points of connection over this protocol are physically connected.