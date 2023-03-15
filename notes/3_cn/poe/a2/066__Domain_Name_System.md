 Here is the formal content on Domain Name System in markdown format with points:

### Domain Name System

1. DNS is a distributed database that maintains the mapping between domain names and IP addresses. It translates the domain names to IP addresses so that the browsers can load the requested websites.
2. The DNS database is distributed across multiple servers for fault tolerance and better performance. These servers are located in a hierarchical structure with the root servers at the top, followed by top-level domain servers, second-level domain servers and so on.
3. When a user enters a domain name in the browser, the request is first sent to the local DNS server. If the local DNS server does not have the mapping for the domain name in its database, it sends a query to the next upper level server and so on until the root server is reached. The mapping is then sent back to the local DNS server which sends the IP address to the user's system.
4. The distributed and hierarchical nature of DNS ensures that the system is fault tolerant and the domain name to IP address mapping is efficiently obtained even for large networks and a huge number of domain names. The DNS system is a critical Internet infrastructure service.
5. The most commonly used protocols for DNS are DNS Query and DNS Zone Transfer (AXFR/IXFR) protocols. BIND is a very popular open source implementation of DNS servers.

The content is written formally as a study material without any feelings or friendliness. No emojis are included and all the content is written myself without any external links. The points are structured in a way to learn and read about Domain Name System for exams. Please let me know if you would like me to modify or expand the content.