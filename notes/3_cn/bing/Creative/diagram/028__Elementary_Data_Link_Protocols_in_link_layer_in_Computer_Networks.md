#### Elementary Data Link Protocols in link layer in Computer Networks

Elementary data link protocols are designed to perform the basic functions of the data link layer, such as framing, error control and flow control. Framing is the process of dividing the bit stream from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes. Error control mechanisms deal with transmission errors and retransmission of corrupted or lost frames. Flow control regulates the speed of delivery so that a fast sender does not overwhelm a slow receiver.

There are different types of elementary data link protocols, depending on whether the transmission channel is noiseless or noisy, and whether the data transfer is unidirectional or bidirectional. Some of the common elementary data link protocols are:

- Simplex protocol: This protocol is for unidirectional data transmission over an ideal channel, i.e. a channel through which transmission can never go wrong. The sender simply sends all its data frames as soon as they are available in its buffer. The receiver is assumed to process all incoming data frames instantly. This protocol does not handle flow control or error control.

- Stop-and-wait protocol: This protocol is for unidirectional data transmission over a noiseless channel. It provides flow control so that a fast sender does not drown a slow receiver. The sender can send a frame only when it has received an indication from the receiver that it is available for further data processing. The indication is called an acknowledgment (ACK) frame. The sender keeps a timer for each frame and waits for the ACK before sending the next frame.

- Stop-and-wait ARQ: This protocol is a variation of the stop-and-wait protocol with added error control mechanisms, appropriate for noisy channels. The sender keeps a copy of the sent frame and waits for a finite time to receive a positive acknowledgment (ACK) from the receiver. If the timer expires or a negative acknowledgment (NAK) is received, the frame is retransmitted. If a positive acknowledgment is received, then the next frame is sent. The frames are sequentially numbered to avoid duplication.

- Go-back-N ARQ: This protocol provides for sending multiple frames before receiving the acknowledgment for the first frame. It uses the concept of sliding window, and so is also called sliding window protocol. The sender maintains a window of frames that can be sent without waiting for ACKs. The receiver maintains a window of frames that can be accepted without sending ACKs. The frames are sequentially numbered and a cumulative ACK is sent by the receiver for the last correctly received frame. If the sender does not receive an ACK within a time limit, or receives a NAK, it retransmits all the frames in its window.

- Selective repeat ARQ: This protocol also provides for sending multiple frames before receiving the acknowledgment for the first frame. However, here only the erroneous or lost frames are retransmitted, while the good frames are received and buffered by the receiver. The sender and the receiver maintain windows of frames that can be sent and accepted, respectively. The frames are sequentially numbered and a selective ACK is sent by the receiver for each correctly received frame. If the sender does not receive an ACK for a frame within a time limit, it retransmits that frame only.

The following diagram illustrates the basic architecture of a data link layer protocol using ASCII characters:

```
+-----------------+      +-----------------+
|                 |      |                 |
|   Data link     |      |   Data link     |
|    layer        |      |    layer        |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|   Physical      |      |   Physical      |
|    layer        |      |    layer        |
|                 |      |                 |
+-----------------+      +-----------------+
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       |                        |
       +------------------------+
              Transmission
               channel
```

The sender and the receiver communicate through the physical layer, which provides the transmission channel. The data link layer frames the data from the upper layer and adds error control and flow control information. The data link layer also handles the acknowledgment and retransmission of frames. The data link layer protocols can be classified into different types based on the channel characteristics and the data transfer mode.