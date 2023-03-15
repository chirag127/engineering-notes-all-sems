### DNS revisited

- DNS (Domain Name System) is a distributed database that maps domain names to IP addresses and other information.
- DNS is essential for the functioning of the Internet, as it allows users to access websites and services by using human-readable names instead of numerical addresses.
- DNS is also vulnerable to various attacks, such as spoofing, cache poisoning, denial of service, and hijacking, that can compromise the security and availability of the Internet.
- DNS security can be improved by implementing several measures, such as:

  - DNSSEC (Domain Name System Security Extensions): a suite of extensions that add cryptographic signatures to DNS records, allowing DNS responses to be validated for authenticity and integrity .
  - DNS resolvers: the servers that perform DNS queries on behalf of clients. DNS resolvers should be configured to use secure protocols, such as TLS or HTTPS, to communicate with authoritative servers and other resolvers .
  - DNS firewall: a device or software that monitors and filters DNS traffic based on predefined rules, such as blocking malicious domains or allowing only authorized queries .
  - DNS monitoring and auditing: a process of collecting and analyzing DNS data, such as logs, queries, responses, and anomalies, to detect and respond to potential threats or incidents .