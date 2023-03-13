The Domain Name System (DNS) is a service that translates domain names into IP addresses. Domain names are human-readable names that identify websites or other resources on the internet, such as google.com or wikipedia.org. IP addresses are numerical identifiers that computers use to communicate with each other over the network, such as 142.250.64.78 or 208.80.154.224.

DNS works by using a hierarchical and distributed database of domain names and IP addresses, organized into zones. Each zone corresponds to a domain or a subdomain, and contains records that map names to IP addresses or other types of data. For example, the zone for google.com contains records that map www.google.com to 142.250.64.78, mail.google.com to 142.250.64.101, and so on.

DNS also uses a network of servers that store and query the DNS database. These servers are called name servers, and they can be classified into different types according to their role and function. The main types of name servers are:

- Root name servers: These are the authoritative servers for the root zone, which is the top-level zone of the DNS hierarchy. The root zone contains records that point to the name servers for the top-level domains (TLDs), such as .com, .org, .net, and so on. There are 13 root name servers in the world, identified by letters from A to M, and they are distributed across various locations and organizations.
- TLD name servers: These are the authoritative servers for the TLD zones, such as .com, .org, .net, and so on. They contain records that point to the name servers for the second-level domains (SLDs), such as google.com, wikipedia.org, amazon.com, and so on.
- SLD name servers: These are the authoritative servers for the SLD zones, such as google.com, wikipedia.org, amazon.com, and so on. They contain records that point to the name servers for the subdomains or the hostnames, such as www.google.com, en.wikipedia.org, www.amazon.com, and so on. They also contain records that map the hostnames to the IP addresses or other types of data, such as mail servers, name servers, or text records.
- Recursive name servers: These are the servers that receive DNS queries from clients, such as web browsers or applications, and resolve them by contacting the authoritative name servers in the DNS hierarchy. They can also cache the results of the queries to improve the performance and reduce the load on the authoritative name servers. Recursive name servers are usually provided by internet service providers (ISPs), network administrators, or public DNS services, such as Google Public DNS or Cloudflare DNS.

The following diagram illustrates the basic architecture of a DNS system using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Root name      |       |  TLD name       |       |  SLD name       |
|  server         |       |  server         |       |  server         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |
                                     |