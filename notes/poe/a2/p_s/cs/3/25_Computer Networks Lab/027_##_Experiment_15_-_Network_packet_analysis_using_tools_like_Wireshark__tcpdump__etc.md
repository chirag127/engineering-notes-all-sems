 Here is the content in markdown format for the given topic:

## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc.

1. Introduction
- Wireshark and tcpdump are popular network packet analysis tools used to capture and analyze network traffic.
- They provide a graphical and command-line interface respectively to analyze the captured packets and understand the conversation between different network devices, protocols used, etc.
- This experiment involves using these tools to capture and analyze network traffic to understand the network packets and protocols in action.

2. Pre-requisites
- Wireshark should be installed on the system to capture and analyze packets. Tcpdump comes pre-installed on most Linux systems.
- The system should be connected to a network to capture live network traffic. Else, sample capture files can be used for analysis.

3. Capturing packets
- For Wireshark, select the network interface to capture packets from and start the capture.
- For tcpdump, run the command `tcpdump -i <interface> -w capture.pcap` to capture packets to a file.
- Capture packets for a significant time period to get a good amount of data for analysis.

4. Analyzing packets
- In Wireshark, the captured packets can be analyzed by exploring the details under Capture Options, inspecting individual packets, understanding protocols, etc.
- In tcpdump, the capture file can be analyzed using Wireshark or other tools to understand the packets and protocols.
- Analyze the packets to understand the conversation between devices, protocols used, packet headers, payloads, etc. This helps in understanding the network traffic and troubleshooting network issues.

5. Advantages and applications
- Packet analysis tools provide a deep insight into the network traffic and are useful for network administrators, security analysts, etc.
- They are used to monitor networks, troubleshoot issues, analyze attacks, understand bandwidth usage, and for various other network-related tasks.
- Though powerful, these tools require technical knowledge to analyze the captures and understand the network packets and protocols.