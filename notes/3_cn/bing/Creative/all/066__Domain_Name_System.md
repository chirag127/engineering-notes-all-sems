### Domain Name System

- The Domain Name System (DNS) is a hierarchical and distributed naming system for computers, services, and other resources in the Internet or other Internet Protocol (IP) networks.
- DNS is the main index of the internet that directs traffic for queries across the web.
- DNS maps the name people use to locate a website to the IP address that a computer uses to locate that website.
- DNS makes it possible for browsers, apps, and servers to load internet resources.
- DNS is very similar to a phone book that contains all the public domains and their corresponding IP addresses.
- DNS is composed of four types of servers: DNS recursor, root nameserver, TLD nameserver, and authoritative nameserver.
- DNS recursor is a server that receives queries from clients and makes additional requests to resolve them.
- Root nameserver is the first step in translating a hostname into an IP address. It serves as a reference to other more specific locations.
- TLD nameserver is the server that hosts the last portion of a hostname (e.g., .com, .org, .net).
- Authoritative nameserver is the final stop in the query. It has access to the requested record and returns the IP address for the requested hostname.
- The process of DNS resolution involves the following steps:
  - A client sends a query to a DNS recursor for a hostname (e.g., www.example.com).
  - The DNS recursor contacts a root nameserver for the top-level domain (TLD) of the hostname (e.g., .com).
  - The root nameserver returns a list of TLD nameservers for the requested TLD.
  - The DNS recursor contacts one of the TLD nameservers for the second-level domain (SLD) of the hostname (e.g., example).
  - The TLD nameserver returns a list of authoritative nameservers for the requested SLD.
  - The DNS recursor contacts one of the authoritative nameservers for the full hostname (e.g., www.example.com).
  - The authoritative nameserver returns the IP address for the requested hostname.
  - The DNS recursor caches the IP address and returns it to the client.
  - The client can now communicate with the server at the IP address.

- A mnemonic to remember the four types of DNS servers is: **R**ecursor, **R**oot, **T**LD, **A**uthoritative, or **RRTA**.
- A mnemonic to remember the order of DNS resolution is: **C**lient, **R**ecursor, **R**oot, **T**LD, **A**uthoritative, or **CRRTA**.
- An example of a DNS resolution for www.example.com is shown below:

```
Client: 192.168.1.100
DNS Recursor: 8.8.8.8
Root Nameserver: 198.41.0.4
TLD Nameserver: 192.5.6.30
Authoritative Nameserver: 93.184.216.34
Server: 93.184.216.34

Client -> DNS Recursor: What is the IP address of www.example.com?
DNS Recursor -> Root Nameserver: What are the TLD nameservers for .com?
Root Nameserver -> DNS Recursor: Here are the TLD nameservers for .com: 192.5.6.30, 192.33.14.30, ...
DNS Recursor -> TLD Nameserver: What are the authoritative nameservers for example.com?
TLD Nameserver -> DNS Recursor: Here are the authoritative nameservers for example.com: 93.184.216.34, 93.184.216.35, ...