Protocols are a set of rules that govern the communication and exchange of data over the internet. The web is a massive network of webpages, programs, and files that are accessible via URLs. The web uses various protocols on top of the internet protocols, such as TCP/IP, DNS, HTTP, and TLS.

The following diagram illustrates the basic architecture of a web communication using these protocols:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Browser     |    |     Server      |    |     DNS         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       | 1. Enter URL         |                      |
       |----------------------|----------------------|
       |                      |                      |
       |                      | 2. Resolve domain    |
       |                      | name to IP address   |
       |                      |<---------------------|
       |                      |                      |
       |                      | 3. Establish TCP     |
       |                      | connection           |
       |<-------------------->|                      |
       |                      |                      |
       | 4. Send HTTP request |                      |
       |--------------------->|                      |
       |                      |                      |
       |                      | 5. Process request   |
       |                      | and send HTTP        |
       |                      | response             |
       |<-------------------->|                      |
       |                      |                      |
       | 6. Render webpage    |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
```

Note: The diagram is simplified and does not show all the details of the protocols. For example, TLS is used to encrypt the HTTP communication and DNS may involve multiple servers to resolve a domain name. Also, the browser may use other protocols such as FTP or SMTP to access other resources or services on the web.