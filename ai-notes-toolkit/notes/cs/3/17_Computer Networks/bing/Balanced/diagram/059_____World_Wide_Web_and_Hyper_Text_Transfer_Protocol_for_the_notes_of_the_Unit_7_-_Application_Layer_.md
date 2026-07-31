Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of World Wide Web and Hyper Text Transfer Protocol for the Unit 7 - Application Layer in the subject of Computer Networks.

### World Wide Web and Hyper Text Transfer Protocol

- The World Wide Web (WWW) is a system of interlinked hypertext documents that can be accessed via the Internet using a web browser.
- A hypertext document is a text file that contains links to other documents or resources, such as images, videos, audio, etc.
- The links are usually highlighted or underlined in the document, and can be clicked or tapped to navigate to the linked resource.
- The WWW was invented by Tim Berners-Lee and his team at CERN in 1989-1991, as a way to share information among researchers across the world.
- The WWW is based on three main components: Uniform Resource Identifiers (URIs), HyperText Markup Language (HTML), and HyperText Transfer Protocol (HTTP).

- Uniform Resource Identifiers (URIs) are strings of characters that identify and locate a resource on the Internet, such as a webpage, an image, a video, etc.
- A URI consists of two parts: a scheme and a path. The scheme indicates the protocol or method used to access the resource, such as http, https, ftp, mailto, etc. The path specifies the location or name of the resource, such as www.example.com, /index.html, /images/logo.png, etc.
- A URI can also include optional components, such as a user name, a password, a port number, a query string, and a fragment identifier.
- For example, the URI https://www.example.com:8080/index.html?name=Sydney#section1 has the following components:

  - Scheme: https
  - User name: none
  - Password: none
  - Host: www.example.com
  - Port: 8080
  - Path: /index.html
  - Query: name=Sydney
  - Fragment: section1

- HyperText Markup Language (HTML) is a standard language for creating and formatting hypertext documents that can be displayed by web browsers.
- HTML uses tags or elements to mark up the structure and content of a document, such as headings, paragraphs, lists, tables, images, links, etc.
- HTML also uses attributes to provide additional information or modify the appearance or behavior of an element, such as the source, the size, the color, the alignment, the style, etc.
- For example, the HTML code for a simple webpage with a title, a heading, and a link is:

```html
<html>
<head>
  <title>My Webpage</title>
</head>
<body>
  <h1>Welcome to my webpage</h1>
  <p>This is a paragraph with a <a href="https://www.bing.com">link</a> to Bing.</p>
</body>
</html>
```

- HyperText Transfer Protocol (HTTP) is the foundation of the WWW, and is used to load webpages using hypertext links.
- HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack, such as TCP/IP.
- HTTP follows a client-server model, where a web browser is a client that requests a resource from a web server that hosts the resource.
- HTTP uses a request-response cycle, where the client sends an HTTP request message to the server, and the server responds with an HTTP response message that contains the requested resource or an error code.
- HTTP request and response messages have a similar structure, consisting of three parts: a start line, a header, and a body.
- The start line indicates the type, the method, the URI, and the version of the message, such as GET /index.html HTTP/1.1 for a request, or HTTP/1.1 200 OK for a response.
- The header contains key-value pairs that provide additional information or parameters about the message, such as the host, the content type, the content length, the date, the cookie, etc.
- The body contains the actual data or content of the message, such as the HTML code, the image data, the video data, etc.
- For example, a typical HTTP request and response cycle for loading a webpage is:

```text
Client: GET /index.html HTTP/1.1
Host: www.example.com

Server: HTTP/1.1 200 OK

```
