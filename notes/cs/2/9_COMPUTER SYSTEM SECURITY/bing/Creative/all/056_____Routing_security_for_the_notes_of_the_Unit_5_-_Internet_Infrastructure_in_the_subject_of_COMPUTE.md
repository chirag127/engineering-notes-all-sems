# Routing Security

Routing security is the protection of the Internet's routing system from errors and attacks that can compromise its availability, integrity, and confidentiality. Routing security is important for the Internet infrastructure, as it ensures that data packets are delivered to their intended destinations without being intercepted, modified, or dropped by malicious actors.

Some of the topics that are covered in routing security are:

- Routing protocols: These are the rules and algorithms that routers use to exchange information about the network topology and the best paths to reach different destinations. Routing protocols can be classified into two types: interior gateway protocols (IGPs) and exterior gateway protocols (EGPs). IGPs are used within a single network or domain, such as RIP, EIGRP, or OSPF. EGPs are used to connect different networks or domains, such as BGP.
- Routing attacks: These are the malicious actions that aim to disrupt, manipulate, or hijack the routing process. Routing attacks can be classified into two types: passive attacks and active attacks. Passive attacks involve eavesdropping on the routing messages or traffic, while active attacks involve injecting, modifying, or deleting routing messages or traffic. Some examples of routing attacks are:

  - Route spoofing: This is when an attacker advertises false or misleading routing information to other routers, causing them to forward packets to the wrong destination or to a black hole.
  - Route hijacking: This is when an attacker redirects traffic intended for a legitimate destination to a malicious one, either by modifying the routing tables of other routers or by intercepting the packets in transit.
  - Route poisoning: This is when an attacker injects invalid or unreachable routes into the routing system, causing network congestion, loops, or partitions.
  - Route flapping: This is when an attacker causes frequent changes in the routing information, causing instability and inefficiency in the routing system.
- Routing security solutions: These are the techniques and mechanisms that aim to prevent, detect, or mitigate routing attacks. Routing security solutions can be classified into two types: cryptographic solutions and non-cryptographic solutions. Cryptographic solutions involve using encryption, authentication, or digital signatures to secure the routing messages or traffic, while non-cryptographic solutions involve using filtering, monitoring, or auditing to verify the routing messages or traffic. Some examples of routing security solutions are:

  - Routing protocol security extensions: These are the modifications or additions to the routing protocols that enhance their security features, such as RIPv2, EIGRP, OSPFv3, or BGPsec.
  - Routing policy specification language (RPSL): This is a language that allows network operators to define and enforce routing policies, such as who can advertise or receive routes, what routes can be accepted or rejected, or how routes can be modified or prioritized.
  - Resource public key infrastructure (RPKI): This is a framework that allows network operators to use public key cryptography to certify the ownership and validity of IP addresses and AS numbers, and to verify the origin and path of BGP announcements.
  - Secure inter-domain routing (SIDR): This is a working group of the Internet Engineering Task Force (IETF) that develops standards and best practices for securing the inter-domain routing system, such as RPKI, BGPsec, or BGP origin validation.