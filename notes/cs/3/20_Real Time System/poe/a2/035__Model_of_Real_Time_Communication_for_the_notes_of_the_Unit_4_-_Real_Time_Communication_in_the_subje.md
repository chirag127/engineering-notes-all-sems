 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### Model of Real Time Communication for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System

1. Sender-Receiver Model: This is the basic model of communication where a sender encodes a message and sends it via a medium to the receiver who decodes and understands the message. This model is inadequate for real-time communication as there is no feedback or acknowledgment of the message being received.

2. Two-way Communication Model: This model incorporates feedback where the receiver sends an acknowledgement or response back to the sender. This makes communication more effective but still does not capture the real-time nature of the exchange.

3. Dialog Model: This model accounts for multiple rounds of communication between the sender and receiver leading to a back and forth exchange. It allows for clarifications and makes communication more robust compared to one-way communication. However, there are no strict timeliness requirements in this model.

4. Real-Time Dialog Model: This model places timeliness requirements on the communication between the sender and receiver. The responses need to be delivered within specific time constraints making the communication truly real-time and enabling applications such as emergency response systems. The time taken needs to be predicable and minimally interfered with for real-time dialog to be effective.

This notes aims to highlight the key models of communication and how the real-time dialog model enables real-time communication systems by incorporating timeliness requirements. The real-time nature makes these systems useful for critical applications while also introducing system design challenges to meet the low latency needs.