 Here is the formal content written in markdown format without any emojis or external links:

### Experiment 8.1 - Echo client and echo server.

1. Aim: To write a TCP echo client and echo server to understand the client-server model.
2. Theory: A client-server model consists of two programs - a client program that initiates a request for a service, and a server program that receives the request and performs the service. The echo client sends a message to the echo server, which echoes back the same message to the client. This demonstrates a simple client-server interaction.
3. Procedure:
    1. Write a TCP echo server program that binds to a port and listens for client connections. When a client connects, it receives data from the client and echoes back the same data.
    2. Write a TCP echo client program that connects to the echo server, sends a message and displays the echoed response from the server.
4. Observations: The client and server programs are run, the client sends a message to the server which echoes back the same message. This shows a successful client-server interaction. The message echoed back can be seen on the client side.
5. Conclusion: The experiment demonstrates a basic client-server model using TCP sockets where the client sends a request (message) to the server which processes the request (echoes back the message) and sends back a response to the client.