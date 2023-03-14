Hyper Text Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes. HTTP follows a classical client-server model, with a client opening a connection to make a request, then waiting until it receives a response. HTTP is a stateless protocol, meaning that the server does not keep any data (state) between two requests. 

The following diagram illustrates the basic architecture of HTTP:

```
    +--------+                                 +-----------+
    |        |---------(1) HTTP Request------>|           |
    |        |                                 |           |
    |        |<--------(2) HTTP Response------|           |
    |        |                                 |           |
    | Client |                                 |   Server  |
    |        |---------(3) HTTP Request------>|           |
    |        |                                 |           |
    |        |<--------(4) HTTP Response------|           |
    |        |                                 |           |
    +--------+                                 +-----------+
```

The steps are:

1. The client initiates a TCP connection to the server and sends an HTTP request message, which consists of a request line, header fields, and an optional message body.
2. The server accepts the TCP connection and sends back an HTTP response message, which consists of a status line, header fields, and an optional message body.
3. The client may send another HTTP request message using the same TCP connection, or close the connection and open a new one for a new request.
4. The server may send another HTTP response message using the same TCP connection, or close the connection and wait for a new one from another client.