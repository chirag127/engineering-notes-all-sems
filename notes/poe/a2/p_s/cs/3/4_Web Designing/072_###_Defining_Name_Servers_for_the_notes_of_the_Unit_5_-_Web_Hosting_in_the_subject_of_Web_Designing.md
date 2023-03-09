 Here is the content in markdown format for the given topic:

### Defining Name Servers for the notes of the Unit 5 - Web Hosting in the subject of Web Designing

- Name servers are servers that contain records of domain names and their corresponding IP addresses. They are responsible for translating domain names to IP addresses.
- When a user enters a domain name in the browser, the request is first sent to the local DNS resolver which then queries the name servers to fetch the IP address for that domain name. The IP address is then sent back to the local DNS resolver which forwards it to the browser. The browser then uses the IP address to fetch the contents from the web server.
- There are mainly two types of name servers -

1. Primary name server - It contains the original resource records for a domain. The primary name server is responsible for managing the data for the domain and distributing it to the secondary name servers.
2. Secondary name server - It obtains its data from the primary name server via a zone transfer. The primary purpose of a secondary name server is to share the load of the primary name server and provide redundancy. If the primary name server goes down, the secondary name server can still resolve domain names to IP addresses and serve the requests.

- Some of the popular name servers are - Bind, Microsoft DNS, OpenDNS, Google Public DNS, etc.
- For a domain, it is recommended to configure at least two name servers - a primary and a secondary. This ensures high availability in case one of the name servers goes down. The name servers can be hosted by the domain registrar, the web hosting provider or can be set up independently.
- That's all for the key points to cover under the topic of defining name servers for the given notes. Please let me know if you would like me to elaborate on any of the points or add more details.