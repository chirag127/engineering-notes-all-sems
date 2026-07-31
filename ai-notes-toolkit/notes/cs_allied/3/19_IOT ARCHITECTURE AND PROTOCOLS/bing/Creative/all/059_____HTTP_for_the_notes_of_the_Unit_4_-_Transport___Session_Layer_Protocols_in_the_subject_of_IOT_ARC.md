# HTTP

HTTP stands for **Hypertext Transfer Protocol**. It is an **application layer protocol** in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is used for transmitting **hypermedia documents**, such as HTML, between web browsers and web servers.

Some key points about HTTP are:

- HTTP is a **stateless** protocol, which means that each request and response pair is independent and does not remember any previous interaction.
- HTTP uses **TCP** as the underlying and reliable transport layer protocol. TCP establishes a connection between the client and the server, and ensures that the data is delivered in order and without errors.
- HTTP follows a **request-response** model, where the client sends a request message to the server, and the server sends back a response message to the client. The request and response messages have a similar structure, consisting of a **start-line**, **headers**, and an optional **body**.
- HTTP defines a set of **methods** that indicate the action to be performed on the requested resource. Some common methods are **GET**, **POST**, **PUT**, **DELETE**, **HEAD**, and **OPTIONS**.
- HTTP defines a set of **status codes** that indicate the result of the request. Some common status codes are **200 OK**, **404 Not Found**, **301 Moved Permanently**, **500 Internal Server Error**, and **403 Forbidden**.
- HTTP supports **multiple versions**, such as HTTP/1.0, HTTP/1.1, and HTTP/2. Each version introduces new features and improvements, such as persistent connections, pipelining, compression, multiplexing, and encryption.
- HTTP can be extended by adding new **headers**, **methods**, **status codes**, and **media types**. For example, HTTP/1.1 introduced the **Host** header, which allows multiple domains to share the same IP address. HTTP/2 introduced the **:method**, **:path**, and **:authority** pseudo-headers, which replace the start-line of the request message.
- HTTP can be used for other purposes than web browsing, such as **APIs**, **web services**, **webhooks**, and **IoT**. For example, HTTP can be used to send and receive data from sensors, actuators, and other devices connected to the Internet.
- HTTP can be combined with other protocols, such as **HTTPS**, **WebSocket**, and **HTTP/3**. HTTPS is a secure version of HTTP that uses **TLS** to encrypt the communication between the client and the server. WebSocket is a protocol that enables **bidirectional** and **real-time** communication between the client and the server. HTTP/3 is a new version of HTTP that uses **QUIC** as the transport layer protocol, which is faster and more reliable than TCP.