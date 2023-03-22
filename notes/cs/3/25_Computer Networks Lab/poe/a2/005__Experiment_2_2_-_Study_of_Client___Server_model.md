 Here is the formal write-up in Markdown format without any emojis or external links:

### Experiment 2.2 - Study of Client – Server model.

1. Client-Server model: In this model, two processes are involved:
    - Server process: Waits for requests to come, accepts requests and sends back responses. The server manages shared resources and services.
    - Client process: Sends requests to the server and waits for responses. The client utilizes services and resources provided by the server.
2. Working:
    - Client connects to the server and sends a request.
    - Server accepts the request and processes it. It may access databases or other resources to fetch required data.
    - Server sends a response back to the client.
    - Connection between client and server terminates.
3. Advantages:
    - Work distribution: Work is distributed between client and server. Client is not overloaded.
    - Scalability: Easy to scale by adding more servers.
    - Security: Sensitive data is stored on the server.
    - Maintenance: Easy to maintain as updates are handled only on the server.
4. Disadvantages:
    - Prone to attacks: As client and server communicate over a network, it is prone to hacking and security attacks.
    - Reliability: Partial failure of the server affects all clients.
    - Response time: Depends on network latency and server load, response time can be high at times.
5. Applications: Web applications, emails, online chat etc. follow client-server model. The web browser acts as a client and the web server serves as the server.