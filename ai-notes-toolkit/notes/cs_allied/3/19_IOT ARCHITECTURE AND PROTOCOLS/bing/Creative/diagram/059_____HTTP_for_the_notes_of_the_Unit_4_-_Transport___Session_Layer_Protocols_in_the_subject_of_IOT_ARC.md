### HTTP

HTTP stands for **Hypertext Transfer Protocol**. It is an **application layer protocol** in the Internet protocol suite model for distributed, collaborative, hypermedia information systems. It is used for transmitting **hypermedia documents**, such as HTML, between web browsers and web servers.

Some key points about HTTP are:

- HTTP is a **stateless** protocol, which means that each request and response pair is independent and does not remember any previous interaction.
- HTTP uses **TCP** as the underlying and reliable transport layer protocol. TCP establishes a connection between the client and the server, and ensures that the data is delivered in order and without errors.
- HTTP follows a **request-response** model, where the client sends a request message to the server, and the server sends back a response message to the client. The request and response messages have a similar structure, consisting of a **start-line**, **headers**, and an optional **body**.
- HTTP defines a set of **methods** that indicate the action to be performed on the requested resource. Some common methods are **GET**, **POST**, **PUT**, **DELETE**, **HEAD**, and **OPTIONS**.
- HTTP defines a set of **status codes** that indicate the outcome of the request. Some common status codes are **200 OK**, **404 Not Found**, **301 Moved Permanently**, **500 Internal Server Error**, and **403 Forbidden**.
- HTTP supports **multiple media types**, which are identified by the **Content-Type** header in the message. Some common media types are **text/html**, **image/jpeg**, **application/json**, and **multipart/form-data**.
- HTTP supports **compression**, **caching**, **authentication**, **redirection**, **cookies**, and **encryption** through various headers and mechanisms.

Some similar or related protocols to HTTP are:

- **Gopher**: a content delivery protocol that was displaced by HTTP in the early 1990s.
- **SPDY**: an alternative to HTTP developed at Google, superseded by HTTP/2.
- **HTTP/2**: an improved version of HTTP that supports multiplexing, compression, prioritization, and server push.
- **Gemini**: a Gopher-inspired protocol that mandates privacy-related features and minimalism.

: HTTP - Wikipedia
: HTTP | MDN - Mozilla