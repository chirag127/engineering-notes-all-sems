# Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.74.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email delivery, load balancing, and security.

The main components of DNS are:

- DNS servers: These are computers that store and update the mappings between domain names and IP addresses. There are different types of DNS servers, such as root servers, authoritative servers, and recursive servers.
- DNS resolvers: These are programs that run on the user's device and query DNS servers to find the IP address of a domain name. The resolver may cache the results of previous queries to speed up the process.
- DNS records: These are data entries that store the information about a domain name and its IP address. There are different types of DNS records, such as A records, CNAME records, MX records, and NS records.

The process of resolving a domain name to an IP address involves the following steps:

- The user types a domain name in the browser, such as www.example.com.
- The browser sends a DNS query to the resolver, asking for the IP address of www.example.com.
- The resolver checks its cache to see if it already has the answer. If not, it sends a query to a root server, which is one of the 13 servers that manage the top-level domains, such as .com, .org, .net, etc.
- The root server responds with a referral to an authoritative server for the .com domain, which is responsible for managing the subdomains under .com, such as example.com, google.com, etc.
- The resolver sends a query to the authoritative server for the .com domain, asking for the IP address of www.example.com.
- The authoritative server responds with a referral to another authoritative server for the example.com domain, which is responsible for managing the subdomains under example.com, such as www.example.com, mail.example.com, etc.
- The resolver sends a query to the authoritative server for the example.com domain, asking for the IP address of www.example.com.
- The authoritative server responds with the IP address of www.example.com, which is stored in an A record.
- The resolver returns the IP address of www.example.com to the browser, and caches the result for future use.
- The browser uses the IP address of www.example.com to establish a connection with the web server and request the web page.