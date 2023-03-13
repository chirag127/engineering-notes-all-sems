#### Elementary Data Link Protocols in link layer in Computer Networks

- Protocols in the data link layer are designed to perform the basic functions of framing, error control and flow control.
- Framing is the process of dividing bit-streams from the physical layer into data frames whose size ranges from a few hundred to a few thousand bytes.
- Error control is the process of detecting and correcting errors that may occur during transmission or reception of data frames.
- Flow control is the process of regulating the rate of data transmission between the sender and the receiver to avoid congestion or buffer overflow.
- Elementary data link layer protocols are the simplest protocols that can be used for data transmission over a single link.
- Elementary data link layer protocols are divided into three categories, as given below:

  - Protocol 1: Unrestricted simplex protocol
  - Protocol 2: Simplex stop and wait protocol
  - Protocol 3: Simplex protocol for noisy channels.

- Let us discuss each protocol one by one.

##### Protocol 1: Unrestricted simplex protocol

- This protocol is used for one-way data transmission over a noiseless channel.
- The sender continuously sends data frames without waiting for any acknowledgment from the receiver.
- The receiver simply accepts and processes the incoming data frames.
- There is no error or flow control in this protocol.
- This protocol is suitable for applications where data loss is not critical, such as streaming audio or video.
- A possible mnemonic for this protocol is: **U**nrestricted **S**implex **P**rotocol = **U**nlimited **S**ending **P**ermission.

##### Protocol 2: Simplex stop and wait protocol

- This protocol is used for one-way data transmission over a noisy channel.
- The sender sends one data frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment after receiving and processing a data frame.
- If the sender does not receive an acknowledgment within a specified time, it assumes that the frame or the acknowledgment was lost and retransmits the frame.
- This protocol provides error control but not flow control.
- This protocol is suitable for applications where data loss is not acceptable, such as file transfer or email.
- A possible mnemonic for this protocol is: **S**implex **S**top and **W**ait **P**rotocol = **S**end **S**ingle **W**ait **P**atiently.

##### Protocol 3: Simplex protocol for noisy channels

- This protocol is an improvement over protocol 2 that can handle the problem of duplicate frames.
- The sender and the receiver use sequence numbers to identify each data frame and acknowledgment.
- The sender sends one data frame with a sequence number and waits for an acknowledgment with the same sequence number before sending the next frame.
- The receiver sends an acknowledgment with the sequence number of the last correctly received frame.
- If the sender receives an acknowledgment with a different sequence number, it assumes that the frame or the acknowledgment was lost or duplicated and retransmits the frame with the same sequence number.
- This protocol provides error control but not flow control.
- This protocol is suitable for applications where data loss and duplication are not acceptable, such as database transactions or online banking.
- A possible mnemonic for this protocol is: **S**implex **P**rotocol for **N**oisy **C**hannels = **S**end **P**roper **N**umber **C**heck.