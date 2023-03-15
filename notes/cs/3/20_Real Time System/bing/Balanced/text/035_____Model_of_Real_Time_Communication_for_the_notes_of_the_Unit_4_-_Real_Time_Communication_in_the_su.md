### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, chat messages, online games, etc.
- Real time communication requires a network that can support the quality of service (QoS) parameters such as throughput, delay and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay among different messages.
- Real time communication can be classified into two types: hard real time and soft real time .
- Hard real time communication has strict deadlines and guarantees that the messages will be delivered within the specified time limit.
- Soft real time communication has relaxed deadlines and allows some degree of delay or loss of messages.
- A model of real time communication consists of the following components :
  - Sources and destinations: the end users of the communication system that generate and consume messages.
  - Hosts: the devices that host the sources and destinations and provide network interfaces.
  - Network: the medium that connects the hosts and enables data transmission.
  - Input and output queues: the buffers that store the incoming and outgoing messages at each host.
  - Input and output buffers: the memory areas that allocate space for the input and output queues.
  - Traffic model: the characterization of the messages in terms of inter-packet spacing, message length and reception deadline.
  - Scheduling algorithm: the method that determines the order of sending and receiving messages at each host.