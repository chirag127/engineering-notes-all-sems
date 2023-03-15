# World Wide Web and Hyper Text Transfer Protocol

- The World Wide Web (WWW) is a system of interlinked hypertext documents that can be accessed via the Internet using a web browser.
- A hypertext document is a text that contains links to other texts or resources, such as images, videos, or audio files.
- The links in a hypertext document are called hyperlinks, and they allow users to navigate from one document to another.
- The WWW was invented by Tim Berners-Lee and his team at CERN in 1989-1991, as a way to share information among researchers.
- The WWW is based on three main technologies: Uniform Resource Identifiers (URIs), HyperText Markup Language (HTML), and HyperText Transfer Protocol (HTTP).
- A URI is a string of characters that identifies a resource on the web, such as a webpage, an image, or a file.
- A URI consists of two parts: a scheme and a path. For example, in the URI `http://example.com/index.html`, the scheme is `http` and the path is `/index.html`.
- A scheme specifies the protocol or method used to access the resource, such as `http`, `https`, `ftp`, `mailto`, etc.
- A path specifies the location or name of the resource on the server, such as `/index.html`, `/images/logo.png`, etc.
- HTML is a markup language that defines the structure and content of a webpage.
- HTML uses tags to enclose different elements of a webpage, such as headings, paragraphs, lists, tables, images, links, etc.
- HTML also uses attributes to provide additional information about the elements, such as their size, color, alignment, etc.
- For example, the following HTML code defines a simple webpage with a title, a heading, and a paragraph:

```html
<html>
<head>
<title>Example Webpage</title>
</head>
<body>
<h1>Welcome to Example Webpage</h1>
<p>This is a paragraph of text.</p>
</body>
</html>
```

- HTTP is an application layer protocol that defines how web browsers and web servers communicate over the Internet.
- HTTP is based on a client-server model, where a web browser is a client that requests a resource from a web server that hosts the resource.
- HTTP uses a request-response cycle, where a client sends a request message to a server, and the server sends back a response message to the client.
- A request message consists of a request line, a header section, and an optional body section.
- A request line specifies the method, the URI, and the version of HTTP used by the client.
- A method indicates the action that the client wants to perform on the resource, such as `GET`, `POST`, `PUT`, `DELETE`, etc.
- A header section contains additional information about the request, such as the host name, the user agent, the content type, etc.
- A body section contains the data that the client wants to send to the server, such as form inputs, files, etc.
- For example, the following request message asks the server to send the webpage `/index.html` using HTTP version 1.1:

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
```

- A response message consists of a status line, a header section, and an optional body section.
- A status line specifies the version of HTTP used by the server, the status code, and the status message.
- A status code indicates the result of the request, such as `200` (OK), `404` (Not Found), `500` (Internal Server Error), etc.
- A status message provides a short description of the status code, such as `OK`, `Not Found`, `Internal Server Error`, etc.
- A header section contains additional information about the response, such as the content type, the content length, the date, etc.
- A body section contains the data that the server wants to send to the client, such as the webpage, the image, the file, etc.
- For example, the following response message sends the webpage `/index.html