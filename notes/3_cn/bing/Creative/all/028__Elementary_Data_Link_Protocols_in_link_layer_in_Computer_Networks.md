#### Elementary Data Link Protocols in link layer in Computer Networks

- Data link layer protocols are designed to perform the basic functions of the data link layer, such as framing, error control and flow control.
- Framing is the process of dividing the bit stream from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control mechanisms deal with transmission errors and retransmission of corrupted or lost frames.
- Flow control regulates the speed of delivery so that a fast sender does not overwhelm a slow receiver.
- Data link protocols can be broadly divided into two categories, depending on whether the transmission channel is noiseless or noisy.
- Noiseless channels are ideal channels that do not introduce any errors or losses in the transmission.
- Noisy channels are realistic channels that may cause errors or losses in the transmission due to noise, interference or congestion.
- The following are some of the elementary data link protocols for noiseless and noisy channels:

  - Simplex protocol: This is a hypothetical protocol designed for unidirectional data transmission over a noiseless channel. It has distinct procedures for sender and receiver. The sender simply sends all its data available onto the channel as soon as they are available in its buffer. The receiver is assumed to process all incoming data instantly. It does not handle flow control or error control.
  - Stop-and-wait protocol: This is a protocol for unidirectional data transmission over a noiseless channel. It provides flow control but not error control. The sender can send a frame only when it has received an indication from the receiver that it is available for further data processing. The receiver sends an acknowledgement (ACK) to the sender after processing each frame. The sender waits for the ACK before sending the next frame.
  - Stop-and-wait ARQ (Automatic Repeat reQuest): This is a protocol for unidirectional data transmission over a noisy channel. It provides both flow control and error control. The sender keeps a copy of the sent frame and starts a timer after sending it. The receiver sends an ACK or a negative acknowledgement (NAK) to the sender after receiving each frame. The sender retransmits the frame if the timer expires or a NAK is received. The sender sends the next frame only after receiving an ACK.
  - Go-back-N ARQ: This is a protocol for bidirectional data transmission over a noisy channel. It provides both flow control and error control. It uses the concept of sliding window, and so is also called sliding window protocol. The sender can send multiple frames before receiving the ACK for the first frame. The frames are sequentially numbered and a finite number of frames are sent. The receiver sends an ACK for the last correctly received frame. If the sender does not receive an ACK within a time period, or receives a NAK, it retransmits all frames starting from the last ACKed frame. The receiver discards any out-of-order frames.
  - Selective repeat ARQ: This is a protocol for bidirectional data transmission over a noisy channel. It provides both flow control and error control. It also uses the concept of sliding window. The sender can send multiple frames before receiving the ACK for the first frame. The frames are sequentially numbered and a finite number of frames are sent. The receiver sends an ACK for each correctly received frame. If the sender does not receive an ACK within a time period, or receives a NAK, it retransmits only the erroneous or lost frames. The receiver buffers any out-of-order frames and delivers them in sequence to the upper layer.

- The following table summarizes the characteristics of the elementary data link protocols:

| Protocol | Channel | Direction | Flow control | Error control | Window size |
|----------|---------|-----------|--------------|---------------|-------------|
| Simplex | Noiseless | Unidirectional | No | No | 1 |
| Stop-and-wait | Noiseless | Unidirectional | Yes | No | 1 |
| Stop-and-wait ARQ | Noisy | Unidirectional | Yes | Yes | 1 |
| Go-back-N ARQ | Noisy | Bidirectional | Yes | Yes | N |
| Selective repeat ARQ | Noisy | Bidirectional | Yes | Yes | N |

- The following are some of the mnemonics and learning tricks for the elementary data link protocols:

  - Simplex protocol: Simplex means one-way, so the sender sends and the receiver receives without any feedback.
  - Stop-and-wait protocol: Stop-and-wait means the sender stops and waits for the receiver's ACK before sending the next frame.
  - Stop-and-wait ARQ: ARQ