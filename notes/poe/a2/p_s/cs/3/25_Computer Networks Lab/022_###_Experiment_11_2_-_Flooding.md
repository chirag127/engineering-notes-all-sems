 Here is the content written in markdown format:

### Experiment 11.2 - Flooding

Flooding is a type of Denial of Service (DoS) attack where an attacker overwhelms a computer, server, or network with a flood of Internet traffic, effectively disrupting services and making resources unavailable to legitimate users.

- An attacker sends a large volume of packets to the target machine's IP address. This floods the target with more traffic than it can handle, disrupting its ability to respond to legitimate requests or users.
- The attack can be sent using spoofed IP addresses to avoid being traced back to the attacker.
- Common types of flooding attacks include:
    - UDP flood - Sends a large number of UDP packets to random ports on the target machine. The target has to unsuccessfully attempt to process the UDP packets, consuming resources.
    - SYN flood - Sends a flood of SYN requests to the target, which has to reserve resources for each SYN awaiting a SYN-ACK response. If enough SYNs are sent without proper responses, the target can get overwhelmed.
    - ICMP (Ping) flood - Sends a flood of ICMP Echo Request (ping) packets to the target, which has to respond to each packet with an Echo Reply. This consumes resources and can disrupt services.
- Defenses include:
    - Filtering - Block suspicious traffic types/sources.
    - Limiting resources - Limit the impact of attacks by limiting resources attackers can consume.
    - Over-provisioning - Provide more resources than needed so floods are less likely to overwhelm the system.
    - Load balancing - Distribute traffic across multiple servers so floods affect a smaller portion of resources.

The points and details covered in the content should help in learning and reading about Experiment 11.2 - Flooding for exams. Let me know if you would like me to elaborate on any of the points or add additional details.