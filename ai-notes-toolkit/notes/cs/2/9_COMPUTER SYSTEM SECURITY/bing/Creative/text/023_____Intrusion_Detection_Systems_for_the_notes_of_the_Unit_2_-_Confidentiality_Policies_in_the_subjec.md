### Intrusion Detection Systems

- An intrusion detection system (IDS) is a device or software application that monitors a network or systems for malicious activity or policy violations.
- An IDS can send alerts to IT and security teams when it detects any security risks and threats, such as unauthorized access, malware, denial-of-service attacks, or data breaches.
- An IDS can be classified into two main types: network-based IDS (NIDS) and host-based IDS (HIDS).
  - A NIDS monitors the traffic on a network segment or a device and analyzes the packets for any signs of intrusion.
  - A HIDS monitors the activity on a specific host, such as a server or a workstation, and analyzes the system logs, files, processes, and network connections for any signs of intrusion.
- An IDS can also be classified into two main categories: signature-based IDS and anomaly-based IDS.
  - A signature-based IDS compares the network or system activity with a database of known attack patterns or signatures and generates an alert if a match is found.
  - An anomaly-based IDS establishes a baseline of normal network or system behavior and generates an alert if it detects any deviation from the baseline.
- An IDS can be combined with an intrusion prevention system (IPS) to form an intrusion detection and prevention system (IDPS).
  - An IPS is an extension of an IDS that can not only detect but also block or prevent malicious activity or policy violations.
  - An IPS can operate in two modes: inline mode and promiscuous mode.
    - In inline mode, the IPS is placed between the network and the protected system and can directly stop or modify the traffic that violates the security policy.
    - In promiscuous mode, the IPS is placed outside the network and can only send alerts or commands to other devices to stop or modify the traffic that violates the security policy.
- An IDPS can provide several benefits, such as improving the security posture, enhancing the visibility, reducing the response time, and complying with the regulations.
- An IDPS can also face some challenges, such as generating false positives, requiring constant updates, consuming resources, and raising privacy issues.
- Some examples of IDPS products are Cisco Firepower, Fortinet FortiGate, IBM QRadar, McAfee Network Security Platform, and Snort.