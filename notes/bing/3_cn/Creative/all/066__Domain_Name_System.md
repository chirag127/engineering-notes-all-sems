### Domain Name System

- The Domain Name System (DNS) is a hierarchical and distributed naming system for computers, services, and other resources in the Internet or other Internet Protocol (IP) networks.
- DNS is the main index of the internet that directs traffic for queries across the web. It maps the name people use to locate a website to the IP address that a computer uses to locate that website.
- DNS is an internet service that translates the domain name into IP addresses. For example, the domain name `google.com` is translated to the IP address `142.250.72.238`.
- DNS works by using a network of servers called DNS servers. When a user requests a domain name, the request first goes to a DNS server. The DNS server then looks up the domain name in its database and returns the corresponding IP address to the user. If the DNS server does not have the domain name in its database, it forwards the request to another DNS server until the IP address is found or the request fails.
- DNS has a hierarchical structure, which means that there are different levels of DNS servers. The top level is the root DNS servers, which store the information about the top-level domains (TLDs), such as `.com`, `.org`, `.net`, etc. The second level is the authoritative DNS servers, which store the information about the specific domains within each TLD, such as `google.com`, `okta.com`, `cloudflare.com`, etc. The third level is the local DNS servers, which are usually provided by the internet service providers (ISPs) or the organizations, and cache the information from the authoritative DNS servers for faster access.
- DNS uses a protocol called DNS resolution to find the IP address of a domain name. DNS resolution involves sending a query message from the user to the DNS server, and receiving a response message from the DNS server to the user. The query message contains the domain name that the user wants to resolve, and the response message contains the IP address of the domain name or an error code if the resolution fails.
- DNS resolution can be iterative or recursive. In iterative resolution, the DNS server returns the best answer it has, or a referral to another DNS server that may have the answer. The user then sends the query to the referred DNS server and repeats the process until the IP address is found or the query fails. In recursive resolution, the DNS server does the work of contacting other DNS servers on behalf of the user, and returns the final answer or an error to the user. Recursive resolution is faster and more convenient for the user, but it puts more load on the DNS server.
- DNS has many benefits, such as:
  - It makes the internet more user-friendly, as people can use easy-to-remember domain names instead of complex IP addresses.
  - It enables the scalability and flexibility of the internet, as domain names can be changed or moved to different IP addresses without affecting the users.
  - It supports the security and reliability of the internet, as DNS servers can implement various mechanisms to prevent or mitigate attacks, such as DNS spoofing, DNS hijacking, DNS cache poisoning, etc.
- DNS also has some challenges, such as:
  - It can be vulnerable to various attacks, as malicious actors can exploit the weaknesses of the DNS protocol or the DNS servers to redirect or block the users from accessing the legitimate websites.
  - It can be affected by various factors, such as network congestion, server overload, configuration errors, etc., which can cause delays or failures in the DNS resolution process.
  - It can be inconsistent or outdated, as DNS servers may have different or old information about the domain names and their IP addresses, which can lead to errors or conflicts in the DNS resolution process.

- A possible mnemonic to remember the steps of DNS resolution is:

  - **D**omain name requested by user
  - **N**ame server queried by user
  - **S**erver responds with IP address or referral
  - **R**epeat until IP address found or query fails
  - **E**nd of resolution process
  - **S**uccess or error returned to user
  - **O**utput displayed to user
  - **L**ocal cache updated by user

- A possible learning trick to understand the hierarchical structure of DNS is to compare it to a family tree, where:

  - The root DNS servers are the ancestors, who know the information about the main branches of the family (TLDs).
  - The authoritative DNS servers are the parents, who know the information about their