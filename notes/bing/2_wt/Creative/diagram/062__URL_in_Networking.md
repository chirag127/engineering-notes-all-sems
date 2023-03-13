A URL (Uniform Resource Locator) is a type of Uniform Resource Identifier (URI) that provides a way to access information from remote computers, such as a web server and cloud storage. It contains various elements, such as the network communication protocol, a subdomain, a domain name, and its extension. A URL is often colloquially referred to as a web address, or simply an address, since web pages are the most common resources that users employ URLs to find.

The following diagram illustrates the basic structure of a URL in networking:

```
+-------------------------+-------------------------+-------------------------+
|        Protocol         |        Authority       |          Path           |
+-------------------------+-------------------------+-------------------------+
|                         |                         |                         |
|  https://               |  www.example.com:8080  |  /path/to/resource.html |
|                         |                         |                         |
+-------------------------+-------------------------+-------------------------+
|                         |                         |                         |
|  Protocol scheme        |  Hostname and port     |  Resource location      |
|                         |                         |                         |
+-------------------------+-------------------------+-------------------------+
```

The protocol scheme indicates the network communication protocol used to access the resource, such as HTTP, HTTPS, FTP, etc. The authority consists of the hostname and the port number, separated by a colon. The hostname is the domain name of the server that hosts the resource, such as www.example.com. The port number is the numerical identifier of the network port used by the server to communicate with clients, such as 8080. The path specifies the location of the resource on the server, such as /path/to/resource.html. The path may also include query parameters and fragment identifiers, which provide additional information to the server or the client about the resource.