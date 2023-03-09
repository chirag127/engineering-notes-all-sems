 Here is the content in markdown format for the topic ### Experiment 9.1 - DNS:

### Experiment 9.1 - DNS

Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or any resource connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates domain names meaningful to humans into the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols.

- DNS is organized in a tree-like structure, with each branch representing a subdivision of the domain namespace.
- The root domain contains the top-level domains (TLDs) like .com, .net, .org, etc. These TLDs further contain second-level domains like example.com and third-level domains like subdomain.example.com and so on.
- DNS resolves domain names to IP addresses using DNS servers that maintain databases of domain name registrations.
- When a user enters a domain name into a browser, the request is sent to a DNS server which looks up the IP address associated with that domain name and returns it to the user.
- This allows accessing websites, sending emails, etc using domain names which are easy to remember rather than the numeric IP addresses.
- The DNS system is crucial for the functioning of the Internet and most internal networks as it provides the foundation for all online services and communications.

Advantages:
- Easy to remember domain names
- Decentralized and distributed system
- Scalable to large networks

Disadvantages:
- Vulnerable to attacks like DNS spoofing, cache poisoning, DDoS, etc.
- Single point of failure if DNS servers go down
- Additional latency in name resolution

[Include diagrams, examples, codes, etc here if required]