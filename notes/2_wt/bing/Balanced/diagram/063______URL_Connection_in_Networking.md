A URL connection in networking is a way of communicating with a resource on the Internet using a URL (Uniform Resource Locator). A URL is a unique identifier that specifies the protocol, domain name, path, port, reference point, and query parameters of a resource. For example, https://www.example.com:8080/index.html#section1?name=John is a URL that uses the HTTPS protocol, the domain name www.example.com, the port 8080, the path /index.html, the reference point #section1, and the query parameter name=John.

A URL connection can be established by using the URL object's openConnection method, which returns a URLConnection object or one of its protocol-specific subclasses, such as HttpURLConnection. A URLConnection object allows you to read from and write to the resource, as well as access its metadata, such as content type, content length, and last modified date.

The following diagram shows a simplified example of a URL connection in networking:

```
+-----------------+       +-----------------+       +-----------------+
| Java program    |       | Web server      |       | Resource        |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | URL object  | |       | | HTTP daemon | |       | | index.html | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|       |         |       |       |         |       |       |         |
|       | openConnection()|       |         |       |       |         |
|       |---------------->|       |         |       |       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       |         |       |       |         |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | URLConnection| |       | | HTTP request| |       | | Content    | |
| | object      | |       | | object      | |       | | metadata   | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|       |         |       |       |         |       |       |         |
|       | connect()|       |       |         |       |       |         |
|       |---------------->|       |         |       |       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       | GET /index.html |       |         |
|       |         |       |       |---------------->|       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       | 200 OK  |       |       |         |
|       |         |       |       |<-----------------|       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       | Content |       |       |         |
|       |         |       |       |<-----------------|       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       |         |       |       |         |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | InputStream | |       | | HTTP response| |       | | Content    | |
| | object      | |       | | object      | |       | | data       | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|       |         |       |       |         |       |       |         |
|       | read()  |       |       |         |       |       |         |
|       |<----------------|       |         |       |       |         |
|       |         |       |       |         |       |       |         |
|       |         |       |       |         |       |       |         |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | OutputStream| |       | | HTTP request| |       | | Content    | |
| | object      | |       | | object      | |       | | data       | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|       |         |

```
