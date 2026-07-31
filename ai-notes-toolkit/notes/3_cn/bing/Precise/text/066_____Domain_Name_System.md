### Domain Name System

- The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network.
- It associates various information with domain names assigned to each of the participating entities.
- Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols.
- By providing a worldwide, distributed directory service, the Domain Name System is an essential component of the functionality of the Internet.
- The Domain Name System is maintained by a distributed database system, which uses the client-server model.
- The nodes of this database are the name servers.
- Each domain has at least one authoritative DNS server that publishes information about that domain and the name servers of any domains subordinate to it.
- The top of the hierarchy is served by the root name servers, the servers to query when looking up (resolving) a top-level domain name.
- The DNS resolver, the client side of the DNS client-server model, is responsible for initiating and sequencing the queries that ultimately lead to a full resolution of the resources sought, e.g., translation of a domain name into an IP address.
- The DNS resolver is usually integrated into the operating system, and can be configured by the user or system administrator to use a particular DNS server or set of servers, or to use the default servers provided by the Internet Service Provider (ISP).
- DNS messages are transported over the User Datagram Protocol (UDP) or the Transmission Control Protocol (TCP), depending on the size of the message and the reliability requirements.
- DNS messages are limited to 512 bytes when transported over UDP, but can be larger when transported over TCP.
- DNS messages consist of a header and four sections: the question section, the answer section, the authority section, and the additional section.
- The header contains information about the message, including the type of message (query or response), the number of questions, answers, authority records, and additional records, and various flags and codes.
- The question section contains the domain name and type of record being queried.
- The answer section contains the resource records that answer the query.
- The authority section contains the resource records that provide information about the authoritative name servers for the domain being queried.
- The additional section contains additional resource records that may be helpful in resolving the query, such as the IP addresses of the name servers listed in the authority section.