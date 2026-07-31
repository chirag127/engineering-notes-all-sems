# DNS revisited

- DNS stands for Domain Name System, which is a distributed database that maps domain names to IP addresses and other information.
- DNS is essential for the functioning of the Internet, as it allows users to access websites and services by using human-readable names instead of numerical addresses.
- DNS also supports other applications, such as email, VoIP, and peer-to-peer networking, by providing name resolution and service discovery.
- DNS is based on a hierarchical structure of domains, which are divided into zones. Each zone is managed by one or more authoritative name servers, which store the records for the domain and its subdomains.
- DNS uses a client-server model, where a DNS client (also called a resolver) sends queries to a DNS server (also called a name server) to obtain the information it needs.
- DNS queries and responses are transmitted over UDP or TCP, using port 53. DNS messages have a standard format, consisting of a header, a question section, an answer section, an authority section, and an additional section.
- DNS queries can be either recursive or iterative. A recursive query asks the name server to provide the final answer or an error, while an iterative query asks the name server to provide the best answer it can or a referral to another name server.
- DNS caching is a technique that improves the performance and efficiency of DNS by storing the results of previous queries in a local memory. DNS caching reduces the network traffic and the load on the name servers, and speeds up the name resolution process for the clients.
- DNS security is a major challenge, as DNS is vulnerable to various attacks, such as spoofing, cache poisoning, denial of service, and amplification. These attacks can compromise the integrity, availability, and confidentiality of DNS data and services, and affect the security of the entire Internet.
- DNS security can be enhanced by applying various measures, such as:

  - Securing the DNS infrastructure, by using firewalls, intrusion detection systems, access control lists, and encryption.
  - Securing the DNS transactions, by using DNS Security Extensions (DNSSEC), which add digital signatures to the DNS records and messages, and allow the clients to verify the authenticity and integrity of the DNS data.
  - Securing the DNS clients, by using DNS over HTTPS (DoH) or DNS over TLS (DoT), which encrypt the DNS queries and responses between the clients and the servers, and prevent eavesdropping and tampering by third parties.