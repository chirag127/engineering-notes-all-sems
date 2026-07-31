# Synchronous and Asynchronous Communication

Synchronous and asynchronous communication are two modes of communication that are used in computer organization and architecture. They differ in the timing and coordination of the data transfer between the sender and the receiver.

## Synchronous Communication

- Synchronous communication is a mode of communication where the sender and the receiver are synchronized in time and exchange data at a fixed rate.
- Synchronous communication requires a common clock signal between the sender and the receiver to coordinate the data transfer.
- Synchronous communication is simpler in design but carries the risk of spreading failures across services. To mitigate that risk, the architect must implement sophisticated service discovery and application load balancing among microservices.
- Synchronous communication is suitable for real-time applications that require low latency and high reliability, such as video conferencing, online gaming, and live streaming.
- Examples of synchronous communication are phone calls, video calls, face-to-face meetings, and synchronous serial communication protocols such as SPI and I2C.

## Asynchronous Communication

- Asynchronous communication is a mode of communication where the sender and the receiver are not synchronized in time and exchange data at variable rates.
- Asynchronous communication does not require a common clock signal between the sender and the receiver, but uses start and stop bits to indicate the beginning and the end of a data frame.
- Asynchronous communication trades architectural simplicity and data consistency for scalability, resilience, and flexibility. It allows the sender and the receiver to operate independently and handle data at their own pace.
- Asynchronous communication is suitable for non-real-time applications that require high throughput and low coupling, such as email, chat, and asynchronous serial communication protocols such as UART and USB.
- Examples of asynchronous communication are email, text messages, social media posts, and blog comments.