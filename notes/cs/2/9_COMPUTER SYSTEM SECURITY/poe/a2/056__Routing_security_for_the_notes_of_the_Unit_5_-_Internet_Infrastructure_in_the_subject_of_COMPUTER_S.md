 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Routing security for the notes of the Unit 5 - Internet Infrastructure in the subject of COMPUTER SYSTEM SECURITY

1. Route filtering: Filtering routes to avoid malicious routes and prevent route hijacking. Some methods are:
- Filtering based on prefix list: Only allow specific prefixes/subnets to be routed.
- Filtering based on AS path: Only accept routes that have a valid AS path.
- Filtering based on community attribute: Accept routes with specific community attributes only.

2. Route authentication: Use cryptographic methods to authenticate route origins. Some methods are:
- Secure Border Gateway Protocol (S-BGP): Uses certificates and digital signatures to authenticate routes.
- Resource Public Key Infrastructure (RPKI): Uses cryptographically signed certificates/objects to verify route origins and validate IP allocation.

3. Route leak protection: Prevent the leaking of routes to illegitimate networks. Methods include:
- Max-prefix filtering: Limit the number of routes an ISP can advertise.
- Specific route leaking protection configurations.

The above points cover key methods to provide routing security and protect against route hijacking, unauthorized route leaks, and other threats to routing infrastructure. Appropriate configuration of routing security methods is important to ensure a robust routing system.