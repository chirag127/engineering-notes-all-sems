### DNS revisited

- Domain Name System (DNS) is a protocol that translates human-readable domain names into numerical IP addresses that identify the location of the web servers or other network resources.
- DNS is a critical component of the internet infrastructure, as it enables users to access websites and applications without memorizing IP addresses.
- DNS is also a potential target for cyber attacks, as malicious actors can exploit its vulnerabilities to redirect users to fake or malicious websites, intercept or modify DNS traffic, or deny access to legitimate websites.
- DNS security aims to protect the integrity and authenticity of DNS data and prevent unauthorized access or manipulation of DNS services.
- DNS security can be achieved by implementing various measures, such as:

  - DNS Security Extensions (DNSSEC): a suite of extensions that add digital signatures to DNS records, allowing DNS responses to be validated by the recipients. DNSSEC provides origin authority, data integrity, and authenticated denial of existence.
  - DNS over HTTPS (DoH): a protocol that encrypts DNS queries and responses using HTTPS, preventing eavesdropping or tampering by third parties. DoH also enhances user privacy by hiding DNS traffic from network operators or ISPs.
  - DNS over TLS (DoT): a protocol that encrypts DNS queries and responses using TLS, similar to DoH, but using a dedicated port (853) instead of the standard HTTPS port (443).
  - DNS filtering: a technique that blocks or redirects DNS queries or responses based on predefined rules or policies, such as blacklists or whitelists. DNS filtering can be used to prevent access to malicious or unwanted websites, or to enforce content filtering or parental control.
  - DNS firewall: a device or software that monitors and controls DNS traffic, detecting and blocking malicious or anomalous DNS queries or responses, such as DNS amplification or DNS tunneling attacks.
  - DNS monitoring and analysis: a process that collects and analyzes DNS data, such as logs, statistics, or traffic patterns, to identify and respond to DNS threats, anomalies, or incidents, or to optimize DNS performance and availability.

- DNS security requires a holistic and risk-based approach, as different DNS components, such as authoritative servers, recursive resolvers, or end-user devices, may face different threats and require different security measures .
- DNS security also requires coordination and collaboration among various stakeholders, such as domain owners, DNS service providers, network operators, ISPs, or end-users, as DNS is a distributed and hierarchical system that relies on the trust and cooperation of multiple parties .