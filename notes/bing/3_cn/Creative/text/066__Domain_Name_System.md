### Domain Name System

- The Domain Name System (DNS) is a service that translates domain names into Internet Protocol (IP) addresses. Domain names are the human-readable names of websites, such as google.com or wikipedia.org. IP addresses are the numerical identifiers of computers or devices on the internet, such as 142.250.64.78 or 198.35.26.96.
- DNS works like a phone book that contains all the public domains and their corresponding IP addresses. When a user types a domain name in a web browser or an app, the request is sent to a DNS server, which looks up the domain name and returns the matching IP address. The browser or app then connects to the IP address and loads the website or resource.
- DNS is a hierarchical and distributed system that consists of various components and levels. The main components of DNS are:

  - **Root servers**: These are the servers that store the information about the top-level domains (TLDs), such as .com, .org, .net, etc. There are 13 root servers in the world, each with multiple copies and locations for redundancy and performance.
  - **TLD servers**: These are the servers that store the information about the second-level domains (SLDs), such as google.com, wikipedia.org, etc. Each TLD server is responsible for a specific TLD or a group of TLDs.
  - **Authoritative servers**: These are the servers that store the information about the subdomains and records of a specific SLD, such as mail.google.com, en.wikipedia.org, etc. Each authoritative server is managed by the owner or administrator of the SLD.
  - **Recursive servers**: These are the servers that act as intermediaries between the user and the DNS system. They receive the user's query and perform a series of requests to the root, TLD, and authoritative servers until they find the answer. They also cache the results for future queries to improve efficiency and speed.
  - **Resolver**: This is the software component that runs on the user's device and initiates the DNS query. It communicates with the recursive server and returns the IP address to the browser or app.

- DNS uses various types of records to store different kinds of information. Some of the common record types are:

  - **A record**: This is the most basic type of record that maps a domain name to an IPv4 address, such as google.com -> 142.250.64.78.
  - **AAAA record**: This is similar to an A record, but maps a domain name to an IPv6 address, such as google.com -> 2607:f8b0:4006:80a::200e.
  - **CNAME record**: This is a type of record that maps a domain name to another domain name, such as mail.google.com -> googlemail.l.google.com. This is useful for creating aliases or redirecting traffic.
  - **MX record**: This is a type of record that specifies the mail server that handles the email for a domain name, such as google.com -> aspmx.l.google.com. This is useful for sending and receiving email.
  - **NS record**: This is a type of record that specifies the authoritative server that is responsible for a domain name, such as google.com -> ns1.google.com. This is useful for delegating authority and maintaining consistency.
  - **TXT record**: This is a type of record that stores arbitrary text information for a domain name, such as google.com -> "v=spf1 include:_spf.google.com ~all". This is useful for verifying ownership, providing security, or adding metadata.