### Routing security

Routing security is the protection of the Internet's routing infrastructure from malicious attacks or accidental misconfigurations that can compromise the availability, integrity, and confidentiality of network traffic.

Some of the common routing threats are:

- Route hijacking: An attacker announces a false route for a destination prefix, diverting or intercepting traffic intended for the legitimate destination.
- Route leaking: An operator advertises a route to a peer or provider that was learned from another peer or provider, violating the routing policies or agreements.
- Route spoofing: An attacker injects a forged route into the routing system, impersonating the legitimate origin of the prefix.
- Route poisoning: An operator advertises an unreachable route for a prefix, preventing traffic from reaching the legitimate destination.

Some of the technologies and practices that can improve routing security are:

- Resource Public Key Infrastructure (RPKI): A distributed public database of cryptographically signed records that allows operators to securely register routing information about their networks. Other networks can download the records and verify the authenticity and authorization of the routing announcements.
- Border Gateway Protocol Security (BGPsec): An extension of the Border Gateway Protocol (BGP) that adds cryptographic signatures to BGP messages, ensuring the validity and integrity of the routing path information.
- Mutually Agreed Norms for Routing Security (MANRS): A global initiative, supported by the Internet Society, that provides crucial fixes to reduce the most common routing threats. MANRS consists of four actions that operators can implement: filtering, anti-spoofing, coordination, and global validation.
- Routing Resilience Manifesto (RRM): A voluntary code of conduct that outlines best practices and recommendations for operators to improve the security and resilience of the Internet routing system. RRM covers topics such as routing policies, incident response, monitoring, and education.