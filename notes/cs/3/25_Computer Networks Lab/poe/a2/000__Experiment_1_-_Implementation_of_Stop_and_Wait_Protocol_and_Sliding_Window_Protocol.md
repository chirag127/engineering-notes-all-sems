 Here is the content in markdown format without any external links or emojis:

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol.

### Stop and Wait Protocol:

- Sender sends one frame, waits for acknowledgement and sends next frame only after receiving acknowledgement for previous frame.
- Throughput is low due to waiting for acknowledgement after every frame.
- Simple to implement.
- Prone to large delays.

### Steps:

1. Sender sends one frame to receiver.
2. Receiver sends acknowledgement for the received frame.
3. Sender sends next frame only after receiving acknowledgement.
4. Repeats steps 2 and 3 until all frames are sent.

### Sliding Window Protocol:

- Sender can send multiple frames without waiting for acknowledgement. This window slides as acknowledgements arrive.
- Throughput is high as multiple frames are in transit.
- Complex to implement.
- Handling of lost or corrupted frames is required.

### Steps:

1. Sender sends multiple frames within a window to receiver.
2. Receiver sends acknowledgements for frames received.
3. Sender slides window as acknowledgements arrive and can send more frames.
4. Repeats steps 2 and 3 until all frames are sent.

The content is written in formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the content in any way.