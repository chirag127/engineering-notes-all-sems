#### URL in Networking

A URL (Uniform Resource Locator) is a type of Uniform Resource Identifier (URI) that provides a way to access information from remote computers, such as a web server or cloud storage. It contains various elements, such as:

- A network communication protocol, which indicates the method for retrieving the resource. For example, HTTP, HTTPS, FTP, MAILTO, etc.
- An authority, which includes the domain name and optionally the port number of the server. For example, www.example.com:80.
- A path, which specifies the location of the resource within the server. For example, /en-US/docs/Learn/.
- A query, which provides additional information or parameters for the resource. For example, ?q=URL.
- A fragment, which identifies a specific part of the resource. For example, #Syntax.

A URL is often colloquially referred to as a web address, or simply an address, since web pages are the most common resources that users employ URLs to find. However, URLs can also be used for other types of resources, such as files, images, emails, databases, etc.

A URL is composed of different parts, some mandatory and others optional. The most important parts are highlighted on the URL below (details are provided in the following sections):

`protocol://domain:port/path?query#fragment`

Here are some examples of URLs:

- https://developer.mozilla.org
- https://developer.mozilla.org/en-US/docs/Learn/
- https://developer.mozilla.org/en-US/search?q=URL
- ftp://ftp.example.com/file.txt
- mailto:user@example.com
- jdbc:mysql://localhost:3306/database