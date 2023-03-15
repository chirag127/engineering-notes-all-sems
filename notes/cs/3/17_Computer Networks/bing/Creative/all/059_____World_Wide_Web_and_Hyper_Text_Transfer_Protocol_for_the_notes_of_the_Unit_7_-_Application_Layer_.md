# World Wide Web and Hyper Text Transfer Protocol

- The World Wide Web (WWW) is a system of interlinked hypertext documents that can be accessed via the Internet using a web browser.
- A hypertext document is a text file that contains links to other documents or resources, such as images, videos, or audio files.
- The links in a hypertext document are called hyperlinks, and they allow users to navigate from one document to another by clicking on them.
- The WWW was invented by Tim Berners-Lee and his team at CERN in 1989-1991, as a way to share information among researchers across the world.
- The WWW is based on three main technologies: Uniform Resource Identifiers (URIs), HyperText Markup Language (HTML), and HyperText Transfer Protocol (HTTP).

- The HyperText Transfer Protocol (HTTP) is the foundation of the WWW, and is used to load webpages using hypertext links.
- HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack.
- HTTP defines a set of rules and methods for communication between a client and a server, such as how to request and send data, how to handle errors, and how to negotiate formats and encodings.
- A client is a device or program that initiates a request for a resource, such as a web browser. A server is a device or program that responds to a request and provides the requested resource, such as a web server.
- A resource is any piece of information that can be identified by a URI, such as a webpage, an image, a video, or a file.
- A URI is a string of characters that uniquely identifies a resource on the Internet, such as https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:web-protocols/a/the-world-wide-web
- A URI consists of two parts: a scheme and a path. The scheme indicates the protocol to be used to access the resource, such as http, https, ftp, or mailto. The path specifies the location of the resource on the server, such as /computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:web-protocols/a/the-world-wide-web
- HTTP uses a request-response model, where a client sends a request message to a server, and the server sends back a response message to the client.
- A request message consists of three parts: a request line, a header, and a body. The request line contains the method, the URI, and the version of HTTP. The header contains additional information about the request, such as the host name, the user agent, the content type, and the cookies. The body contains the actual data to be sent to the server, such as form data or file uploads.
- A response message consists of three parts: a status line, a header, and a body. The status line contains the version of HTTP, the status code, and the status message. The status code indicates the outcome of the request, such as 200 OK, 404 Not Found, or 500 Internal Server Error. The status message provides a human-readable explanation of the status code. The header contains additional information about the response, such as the content type, the content length, the server name, and the cookies. The body contains the actual data to be sent to the client, such as HTML, images, videos, or files.
- HTTP supports several methods for different types of requests, such as GET, POST, PUT, DELETE, HEAD, and OPTIONS. The most common methods are GET and POST.
- GET is used to request a resource from the server, such as a webpage or an image. The request parameters are encoded in the URI, and the response body contains the requested resource.
- POST is used to send data to the server, such as form data or file uploads. The request parameters are encoded in the body, and the response body contains the result of the data processing by the server.
- HTTP is a stateless protocol, which means that each request and response are independent and do not remember any previous interactions. To maintain state information across multiple requests and responses, HTTP uses cookies.
- A cookie is a small piece of data that is stored by the client and sent to the server with each request. The server can use cookies to identify and