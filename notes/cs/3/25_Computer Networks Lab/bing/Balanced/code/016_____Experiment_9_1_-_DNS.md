### Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.74.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email routing, load balancing, and security.

DNS works by using a hierarchical structure of servers, called name servers, that store and distribute information about domain names and IP addresses. There are four types of name servers:

- Root servers: These are the top-level servers that know the addresses of all the authoritative servers for the top-level domains, such as .com, .org, .net, etc.
- Top-level domain (TLD) servers: These are the servers that know the addresses of all the authoritative servers for the second-level domains, such as google.com, wikipedia.org, amazon.net, etc.
- Authoritative servers: These are the servers that know the exact IP address of a specific domain name, such as www.google.com, en.wikipedia.org, www.amazon.net, etc.
- Recursive servers: These are the servers that act as intermediaries between users and other name servers. They cache the results of previous queries and forward the queries to the appropriate name servers if they do not have the answer.

When a user wants to access a website using a domain name, the following steps occur:

- The user's browser sends a DNS query to a recursive server, asking for the IP address of the domain name.
- The recursive server checks its cache to see if it has the answer. If not, it sends a query to a root server, asking for the address of the TLD server for the domain name.
- The root server responds with the address of the TLD server and the recursive server sends a query to the TLD server, asking for the address of the authoritative server for the domain name.
- The TLD server responds with the address of the authoritative server and the recursive server sends a query to the authoritative server, asking for the IP address of the domain name.
- The authoritative server responds with the IP address of the domain name and the recursive server sends the answer back to the user's browser.
- The user's browser uses the IP address to establish a connection with the website and request the web page.

The following diagram illustrates the DNS resolution process:

```
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | Root           |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      | DNS query              |                        |
      |----------------------->|                        |
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | TLD            |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | Authoritative  |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      | DNS response          |                        |
      |<----------------------|                        |
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |