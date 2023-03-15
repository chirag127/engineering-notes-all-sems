 Here is the formal content on the given topic in Markdown format:

### Window management in transport layer

1. Window size - The amount of data that can be sent before an acknowledgement is received. This is done to improve efficiency and throughput. Eg: If window size is 64 KB, sender can send 64 KB of data before waiting for acknowledgement.
2. Sliding window - Window size 'slides' over the data as acknowledgements are received. This helps in continuous transmission of data. eg: If first 64 KB is sent and acknowledgement received, next 64 KB is sent. This 'slides' the window over data.
3. Window full - If acknowledgements are not received in time, window gets full and sender stops sending data. This avoids overflow and congestion.
4. Advertised window - Receiver advertises its available buffer space as window size to inform sender how much data it can accommodate. This helps sender send data accordingly and avoid overflow at receiver.

The above points cover the key aspects of window management in transport layer which controls the amount of data in transit and improves throughput. Window size, sliding window, window full situation and advertised window are the main concepts in this method of efficient data transmission.