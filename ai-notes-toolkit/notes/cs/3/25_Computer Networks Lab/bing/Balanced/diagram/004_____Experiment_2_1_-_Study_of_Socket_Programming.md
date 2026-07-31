### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, configuring, connecting, sending and receiving data through sockets using a programming language, such as C, Python, or Java.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, remote control, etc.
- Socket programming can be classified into two types: stream sockets and datagram sockets.
  - Stream sockets use TCP as the transport protocol and provide reliable, ordered, and error-free data transmission. Stream sockets are suitable for applications that require a continuous flow of data, such as web browsing, email, etc.
  - Datagram sockets use UDP as the transport protocol and provide fast, unordered, and unreliable data transmission. Datagram sockets are suitable for applications that require low latency, such as video streaming, online gaming, etc.
- Socket programming can be done using different APIs, such as BSD sockets, Winsock, Java sockets, etc. Each API provides a set of functions or methods to create, manipulate, and use sockets.
- Socket programming can be done using different models, such as blocking, non-blocking, multiplexing, asynchronous, etc. Each model defines how the program handles the input and output operations on sockets.
  - Blocking model: The program waits for the socket operation to complete before proceeding to the next statement. This model is simple but inefficient, as the program cannot perform other tasks while waiting for the socket operation.
  - Non-blocking model: The program does not wait for the socket operation to complete and proceeds to the next statement. This model is efficient but complex, as the program has to check the status of the socket operation and handle errors or exceptions.
  - Multiplexing model: The program uses a single thread or process to monitor multiple sockets and perform the appropriate socket operation when an event occurs. This model is efficient and scalable, as the program can handle multiple sockets without creating multiple threads or processes.
  - Asynchronous model: The program registers a callback function or handler to be executed when a socket operation is completed. This model is efficient and simple, as the program does not have to wait or check the status of the socket operation.