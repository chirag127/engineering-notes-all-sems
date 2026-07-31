# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Objective
The objective of this experiment is to understand and implement two data link layer protocols for reliable and sequential delivery of data frames: stop and wait protocol and sliding window protocol.

## Theory
- Stop and wait protocol is a simple protocol that allows the sender to send one data frame at a time and wait for the acknowledgment from the receiver before sending the next frame. The sender uses a single bit to indicate the sequence number of the frame (0 or 1) and the receiver sends back the same bit as acknowledgment. The sender and the receiver use a half-duplex link, which means that they cannot send and receive data simultaneously. The efficiency of this protocol is low, as the sender has to wait for a round trip time (RTT) between sending and receiving the acknowledgment. The efficiency is given by:

  Efficiency = Tt / (Tt + 2Tp)

  where Tt is the transmission time of a frame and Tp is the propagation time of a frame.

- Sliding window protocol is a more efficient protocol that allows the sender to send multiple frames at a time without waiting for the acknowledgment. The sender and the receiver use a window size to indicate how many frames can be sent or received at a time. The window size can vary from 1 to the maximum sequence number. The sender and the receiver use a full-duplex link, which means that they can send and receive data simultaneously. There are two variants of sliding window protocol: go-back-N ARQ and selective repeat ARQ.

  - Go-back-N ARQ is a sliding window protocol with a fixed window size of 1 for the receiver and a variable window size of wt for the sender. The sender can send up to wt frames at a time and the receiver can only accept the frames in order. If the receiver receives a frame out of order, it discards the frame and sends a negative acknowledgment (NAK) to the sender. The sender then retransmits all the frames from the last acknowledged frame to the current frame. The efficiency of this protocol is given by:

    Efficiency = wt / (1 + 2a)

    where a is the ratio of propagation time to transmission time (a = Tp / Tt).

  - Selective repeat ARQ is a sliding window protocol with a variable window size of wr for the receiver and a variable window size of wt for the sender. The sender can send up to wt frames at a time and the receiver can accept the frames in any order. If the receiver receives a frame out of order, it buffers the frame and sends a positive acknowledgment (ACK) to the sender. The sender then retransmits only the frames that are lost or corrupted. The efficiency of this protocol is given by:

    Efficiency = 1 - p

    where p is the probability of frame loss or corruption.