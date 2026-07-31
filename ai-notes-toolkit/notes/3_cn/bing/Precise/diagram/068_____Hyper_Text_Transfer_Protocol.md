### Hyper Text Transfer Protocol

Hyper Text Transfer Protocol (HTTP) is an application layer protocol used for transmitting data over the internet. It is a request-response protocol between a client and a server. Here is an ASCII diagram that illustrates the basic flow of HTTP:

```
    +--------+                                   +--------+
    |        |                                   |        |
    | Client |                                   | Server |
    |        |                                   |        |
    +----+---+                                   +---+----+
         |                                           |
         | 1. Request (GET /index.html HTTP/1.1)     |
         |------------------------------------------>|
         |                                           |
         | 2. Response (HTTP/1.1 200 OK)             |
         |<------------------------------------------|
         |                                           |
         | 3. Response body (HTML, CSS, JS, etc.)    |
         |<------------------------------------------|
         |                                           |
    +----+---+                                   +---+----+
    |        |                                   |        |
    | Client |                                   | Server |
    |        |                                   |        |
    +--------+                                   +--------+
```

In this diagram, the client sends an HTTP request to the server, asking for the `index.html` page. The server responds with an HTTP response, indicating that the request was successful (`200 OK`). The server then sends the response body, which contains the requested data (in this case, the HTML, CSS, and JS files for the `index.html` page). The client receives the response and can then render the page for the user to view.
