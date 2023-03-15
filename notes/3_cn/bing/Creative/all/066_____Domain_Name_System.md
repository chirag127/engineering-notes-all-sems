### Domain Name System

- The Domain Name System (DNS) is a hierarchical and distributed naming system for computers, services, and other resources in the Internet or other Internet Protocol (IP) networks.
- DNS is the main index of the internet that directs traffic for queries across the web. It maps the name people use to locate a website to the IP address that a computer uses to locate that website.
- DNS is an internet service that translates the domain name into IP addresses. For example, the domain name `google.com` is translated to the IP address `142.250.64.78`.
- DNS works by using a network of servers called DNS servers. Each DNS server stores a part of the DNS database, called a zone, that contains information about a set of domain names and their corresponding IP addresses.
- When a user requests a domain name, such as `google.com`, the user's device contacts a DNS server, usually provided by the user's internet service provider (ISP). This DNS server is called a recursive resolver, because it recursively queries other DNS servers to find the answer.
- The recursive resolver first checks its own cache to see if it already knows the IP address for the domain name. If not, it sends a query to a root server, which is one of the 13 servers that store information about the top-level domains (TLDs), such as `.com`, `.org`, `.net`, etc.
- The root server responds with a referral to the authoritative server for the TLD, such as `.com`. The recursive resolver then sends a query to the authoritative server, which responds with a referral to the authoritative server for the second-level domain, such as `google.com`.
- The recursive resolver then sends a query to the authoritative server for the second-level domain, which responds with the IP address for the domain name. The recursive resolver then caches the answer and returns it to the user's device.
- The user's device then uses the IP address to communicate with the web server that hosts the website for the domain name.

A possible mnemonic to remember the steps of DNS resolution is:

**C**ache **R**oot **A**uthoritative **I**P

- **C**heck the cache of the recursive resolver
- **R**equest the root server for the TLD
- **A**sk the authoritative server for the second-level domain
- **I**dentify the IP address for the domain name

A possible ASCII diagram to illustrate the DNS resolution process is:

```
User's device -> Recursive resolver -> Root server -> TLD server -> SLD server -> Web server
               |<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-|
               |                                                                           |
               |----------------------> IP address of google.com ------------------------->|
```

Some advantages of DNS are:

- It makes it easier for users to access websites by using human-readable names instead of numerical addresses
- It allows websites to change their IP addresses without affecting the users, as long as the DNS records are updated
- It provides a distributed and fault-tolerant system that can handle millions of queries per day
- It supports load balancing and redundancy by allowing multiple IP addresses to be associated with a single domain name

Some disadvantages of DNS are:

- It can be vulnerable to attacks, such as DNS spoofing, DNS hijacking, DNS cache poisoning, etc., that can redirect users to malicious websites or servers
- It can be affected by network congestion, server failures, or configuration errors, that can cause delays or errors in resolving domain names
- It can be subject to censorship or filtering by governments or ISPs, that can block or restrict access to certain domain names or websites

Some examples of applications that use DNS are:

- Web browsers, such as Chrome, Firefox, Safari, etc., that use DNS to load web pages from web servers
- Email clients, such as Outlook, Gmail, Yahoo, etc., that use DNS to send and receive emails from mail servers
- Online games, such as Fortnite, Minecraft, Call of Duty, etc., that use DNS to connect players to game servers
- Streaming services, such as Netflix, YouTube, Spotify, etc., that use DNS to deliver content from media servers
- Cloud services, such as AWS, Azure, Google Cloud, etc., that use DNS to provide various services and resources to customers