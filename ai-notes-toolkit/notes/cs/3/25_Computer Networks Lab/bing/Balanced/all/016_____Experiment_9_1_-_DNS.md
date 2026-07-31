# Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.72.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email delivery, load balancing, and security.

The main components of DNS are:

- DNS servers: These are computers that store and provide DNS records, which are mappings between domain names and IP addresses. There are different types of DNS servers, such as authoritative servers, recursive servers, and caching servers.
- DNS clients: These are devices that request DNS records from DNS servers. For example, a web browser is a DNS client that asks for the IP address of a website before connecting to it.
- DNS records: These are data entries that contain information about a domain name and its corresponding IP address. There are different types of DNS records, such as A records, CNAME records, MX records, and NS records.
- DNS zones: These are logical partitions of the DNS namespace, which is the entire set of domain names and their IP addresses. Each DNS zone is managed by one or more authoritative servers, which are responsible for providing the DNS records for the domain names in that zone.
- DNS queries: These are messages that DNS clients send to DNS servers to request DNS records. There are different types of DNS queries, such as iterative queries, recursive queries, and non-recursive queries.
- DNS responses: These are messages that DNS servers send to DNS clients to provide DNS records. There are different types of DNS responses, such as positive responses, negative responses, and referral responses.

The basic steps of DNS resolution are:

- A DNS client sends a DNS query to a DNS server, asking for the IP address of a domain name.
- The DNS server checks its local cache and zone files to see if it has the DNS record for the domain name. If it does, it sends a positive response to the DNS client with the IP address. If it does not, it sends a referral response to the DNS client with the IP address of another DNS server that may have the DNS record.
- The DNS client repeats the process with the next DNS server until it receives a positive response or a negative response, which indicates that the domain name does not exist or has no IP address.
- The DNS client uses the IP address to connect to the website or perform other actions.