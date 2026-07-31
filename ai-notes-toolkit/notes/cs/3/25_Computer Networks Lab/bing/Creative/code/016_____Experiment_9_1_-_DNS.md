Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Experiment 9.1 - DNS.

```markdown
# Experiment 9.1 - DNS

## Objective
- To understand the basic concepts and functions of the Domain Name System (DNS).
- To learn how to use the nslookup and dig commands to query DNS servers.
- To observe the DNS resolution process and caching mechanism.

## Theory
- DNS is a distributed database that maps domain names to IP addresses and other information.
- DNS uses a hierarchical structure of name servers, each responsible for a zone of the domain name space.
- DNS uses a client-server model, where a DNS client (resolver) sends queries to a DNS server and receives responses.
- DNS uses two types of queries: iterative and recursive. In an iterative query, the DNS server returns the best answer it can, or a referral to another server. In a recursive query, the DNS server queries other servers on behalf of the client until it finds the answer or an error.
- DNS uses a caching mechanism to reduce the network traffic and improve the performance. A DNS server can store the results of previous queries in its cache and use them to answer future queries.

## Procedure
- To query a DNS server using nslookup, type `nslookup <domain name> <DNS server>` in the command prompt. For example, `nslookup www.google.com 8.8.8.8` queries the domain name www.google.com using the DNS server 8.8.8.8 (Google Public DNS).
- To query a DNS server using dig, type `dig <domain name> @<DNS server>` in the command prompt. For example, `dig www.google.com @8.8.8.8` queries the domain name www.google.com using the DNS server 8.8.8.8 (Google Public DNS).
- To observe the DNS resolution process, use the `+trace` option with dig. For example, `dig www.google.com +trace` traces the path of the query from the root servers to the authoritative servers for the domain name www.google.com.
- To observe the DNS caching mechanism, use the `+noall +answer` option with dig. For example, `dig www.google.com +noall +answer` shows only the answer section of the response. Repeat the same query after a few seconds and compare the TTL (time to live) values. The TTL value indicates how long the record can be cached by the DNS server. A lower TTL value means the record is closer to expiration.

## Questions
- What is the difference between a domain name and an IP address?
- What are the advantages of using DNS over using IP addresses directly?
- What are the main components of DNS and how do they interact with each other?
- What are the types of DNS records and what information do they contain?
- What are the steps involved in resolving a domain name to an IP address?
- How does DNS caching improve the efficiency and performance of DNS?
- How can you flush the DNS cache of your system?
```