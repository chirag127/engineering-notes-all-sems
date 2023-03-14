A URL (Uniform Resource Locator) is a type of Uniform Resource Identifier (URI) that specifies the location and the mechanism for accessing a resource on a computer network, such as the World Wide Web. A URL consists of different parts, some mandatory and some optional, separated by special characters. The most common parts are:

- Scheme: This indicates the protocol to use for requesting the resource, such as HTTP, HTTPS, FTP, MAILTO, etc. The scheme is followed by a colon and two slashes (://).
- Authority: This includes the domain name and the port number of the server that hosts the resource. The domain name can be a registered name (such as www.example.com) or an IP address (such as 192.168.0.1). The port number is optional and defaults to the standard port for the scheme (such as 80 for HTTP). The authority is preceded by two slashes (//) and followed by a slash (/).
- Path: This specifies the location of the resource within the server, such as a file or a directory. The path is a sequence of segments separated by slashes (/). The path can be absolute (starting from the root directory) or relative (starting from the current directory).
- Query: This is an optional part that provides additional information to the server for processing the request, such as parameters, filters, or keywords. The query is preceded by a question mark (?) and consists of a series of key-value pairs separated by ampersands (&).
- Fragment: This is another optional part that identifies a specific part of the resource, such as a section, a paragraph, or an element. The fragment is preceded by a hash sign (#) and can be used by the browser to scroll to the corresponding part of the document.

The following diagram illustrates the basic structure of a URL:

```
  scheme  authority       path        query   fragment
    |   __________|_______   |   _______|____   |
    |  /                  \  |  /          \  |  |
    | |                    | | |            | |  |
  http://www.example.com:80/index.html?lang=en#intro
  \______________________________/\________/ \___/
             |                      |         |
          origin                  path     fragment
```

The origin of a URL is the combination of the scheme, the authority, and the default port (if any). The origin is used to determine the same-origin policy for security purposes. Two URLs have the same origin if they have the same scheme, authority, and port. For example, the following URLs have the same origin:

```
http://www.example.com/index.html
http://www.example.com/about.html
http://www.example.com:80/contact.html
```

But the following URLs have different origins:

```
https://www.example.com/index.html (different scheme)
http://www.example.net/index.html (different domain)
http://www.example.com:8080/index.html (different port)
```