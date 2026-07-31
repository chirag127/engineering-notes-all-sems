### Synchronous & asynchronous communication

Synchronous and asynchronous communication are two modes of communication that are used in computer organization and architecture. They differ in the timing, coordination, and feedback of the communication process.

#### Synchronous communication

- Synchronous communication is a mode of communication where the sender and the receiver are in sync, meaning they communicate in real time and expect an immediate response.
- Synchronous communication is simpler in design but carries the risk of spreading failures across services. To mitigate that risk, the architect must implement sophisticated service discovery and application load balancing among microservices.
- Synchronous communication is suitable for scenarios where the sender and the receiver need to exchange information quickly and frequently, such as interactive applications, online gaming, video conferencing, etc.
- Examples of synchronous communication methods are phone calls, video calls, live chats, etc.

#### Asynchronous communication

- Asynchronous communication is a mode of communication where the sender and the receiver are not in sync, meaning they communicate over a period of time and do not expect an immediate response.
- Asynchronous communication is more complex in design but offers more flexibility and scalability. It allows the sender and the receiver to communicate independently and asynchronously, without blocking each other or waiting for each other.
- Asynchronous communication is suitable for scenarios where the sender and the receiver do not need to exchange information urgently or frequently, such as email, social media, file sharing, etc.
- Examples of asynchronous communication methods are email, text messages, voice messages, etc.

#### Comparison

- Synchronous communication is faster, more interactive, and more engaging, but also more demanding, more prone to errors, and more dependent on network availability and latency.
- Asynchronous communication is slower, less interactive, and less engaging, but also more convenient, more reliable, and more independent of network conditions and availability.
- Synchronous and asynchronous communication have different advantages and disadvantages, and the choice of which mode to use depends on the context, the purpose, and the preference of the communication parties.