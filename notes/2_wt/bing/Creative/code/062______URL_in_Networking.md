#### URL in Networking

A URL (Uniform Resource Locator) is a string that identifies a resource on the Internet. A URL has a specific format that consists of several components:

- A scheme that indicates the protocol to use, such as `http`, `https`, `ftp`, `mailto`, etc.
- A colon (`:`) followed by two slashes (`//`) that separate the scheme from the rest of the URL.
- A hostname that identifies the domain name or IP address of the server that hosts the resource, such as `www.example.com` or `192.168.1.1`.
- An optional port number that specifies the port to use for the connection, such as `:80` for HTTP or `:443` for HTTPS. If the port number is omitted, the default port for the scheme is used.
- An optional path that specifies the location of the resource on the server, such as `/index.html` or `/images/logo.png`. The path may contain slashes (`/`) to separate different segments, and may also contain parameters or queries that start with a question mark (`?`) and are separated by ampersands (`&`).
- An optional fragment that starts with a hash (`#`) and identifies a specific part of the resource, such as `#section1` or `#top`. The fragment is usually used to scroll to a certain position on a web page.

Here is an example of a URL and its components:

```
https://www.example.com:443/path/to/resource?param1=value1&param2=value2#fragment
```

- The scheme is `https`, which indicates that the resource is accessed using the Hypertext Transfer Protocol Secure (HTTPS).
- The hostname is `www.example.com`, which identifies the domain name of the server that hosts the resource.
- The port number is `443`, which is the default port for HTTPS.
- The path is `/path/to/resource`, which specifies the location of the resource on the server.
- The query is `?param1=value1&param2=value2`, which contains two parameters: `param1` with the value `value1` and `param2` with the value `value2`.
- The fragment is `#fragment`, which identifies a specific part of the resource.