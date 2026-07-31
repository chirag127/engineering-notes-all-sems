### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, instant messaging, live streaming, online gaming, etc.
- In the model of real time communication, end users of the message application systems are sources and destinations residing in different hosts.
- The network interface of each host contains input queue and output queue. Two buffer areas called input/output buffer are allocated to input and output queue to store queuing information.
- In real time traffic model, each message (Mi) can be characterized by tuples of inter-packet spacing (Pi), message length (ei), reception deadline (Di) as below:

  Mi = (pi, ei, Di)

- This traffic model is called peak rate model in real time communication.
- The performance of real time communication can be measured by throughput, delay and jitter .
- Throughput is the rate of successful message delivery over a communication channel.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay of received messages.
- The goal of real time communication is to achieve high throughput, low delay and low jitter.