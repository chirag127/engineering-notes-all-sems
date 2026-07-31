### DNS revisited for the notes of the Unit 5 - Internet Infrastructure in the subject of COMPUTER SYSTEM SECURITY

DNS or Domain Name System is a vital component of the internet infrastructure. It is responsible for translating domain names into IP addresses, making it possible for users to access websites and other internet services. In this section, we will revisit the concept of DNS and its importance in computer system security.

Here are some key points to keep in mind:

- DNS is a distributed database system that maps domain names to IP addresses. It is hierarchical in nature, with the root domain at the top.
- DNS operates on two main protocols - UDP and TCP. UDP is used for queries, while TCP is used for zone transfers and large queries.
- DNS queries can be either recursive or iterative. In a recursive query, the client asks the DNS server to provide the final answer. In an iterative query, the DNS server provides the best possible answer it has, and the client makes subsequent queries until it gets the final answer.
- DNS can be vulnerable to various types of attacks, including DNS spoofing, DNS cache poisoning, and DNS amplification attacks.
- DNSSEC (DNS Security Extensions) is a set of security protocols that can be used to secure DNS. It provides data integrity, authentication, and confidentiality for DNS queries and responses.
- DNS over HTTPS (DoH) is a protocol that encrypts DNS queries and responses using HTTPS. It provides additional security and privacy for DNS queries.
- DNS over TLS (DoT) is another protocol that encrypts DNS queries and responses using TLS. It is similar to DoH but operates at the transport layer instead of the application layer.

In conclusion, DNS is a critical component of the internet infrastructure that plays a vital role in computer system security. It is vulnerable to various types of attacks, but there are security protocols like DNSSEC, DoH, and DoT that can be used to secure it. As a computer system security professional, it is essential to have a solid understanding of DNS and its security implications.