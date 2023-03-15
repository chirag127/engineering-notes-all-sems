# Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

## Objective
The objective of this experiment is to learn how to capture, analyze, and interpret network packets using various tools such as Wireshark, tcpdump, etc.

## Theory
- A network packet is a unit of data that is transmitted over a network. It consists of a header and a payload. The header contains information such as the source and destination addresses, the protocol type, the length, and the checksum. The payload contains the actual data being sent.
- Network packet analysis is the process of examining the network packets to understand the network traffic, troubleshoot problems, identify security threats, optimize performance, etc.
- Network packet analysis tools are software applications that can capture, filter, decode, and display network packets. Some of the common tools are:
  - Wireshark: A free and open-source graphical user interface (GUI) tool that supports many protocols and features. It can capture packets from live or offline sources, apply filters, display statistics, export data, etc. 
  - tcpdump: A command-line tool that can capture and print network packets. It can also save packets to a file for later analysis. It supports many filters and options. 
  - Colasoft Capsa: A commercial GUI tool that can capture and analyze network packets in real-time. It can also monitor and diagnose network issues, generate reports, etc. 
  - Paessler PRTG: A commercial network monitoring tool that can capture and analyze network packets. It can also classify network traffic, measure bandwidth, alert on issues, etc. 
  - Arkime: A free and open-source web-based tool that can capture and index network packets. It can also search, visualize, and export data, etc. 

## Procedure
The procedure for network packet analysis using tools like Wireshark, tcpdump, etc. may vary depending on the tool, the platform, the network interface, the capture filter, the display filter, the analysis task, etc. However, a general procedure can be outlined as follows:

1. Install and launch the network packet analysis tool of your choice on your system.
2. Select the network interface from which you want to capture packets. You may need to configure the interface settings, such as the promiscuous mode, the snap length, the buffer size, etc.
3. Optionally, apply a capture filter to limit the packets that are captured based on certain criteria, such as the protocol, the port, the address, etc. For example, `tcp port 80` will capture only TCP packets with port 80 as the source or destination.
4. Start the packet capture and observe the packets that are displayed on the tool. You may need to stop the capture manually or set a capture duration or size limit.
5. Optionally, apply a display filter to limit the packets that are displayed based on certain criteria, such as the protocol, the field, the value, etc. For example, `http.request.method == "GET"` will display only HTTP packets with the GET method.
6. Select a packet that you want to analyze and view its details. You may need to expand the packet header and payload sections, decode the packet data, follow the packet stream, etc.
7. Repeat steps 5 and 6 for other packets that you want to analyze.
8. Optionally, save the captured packets to a file for later analysis or export the packet data to another format, such as CSV, XML, JSON, etc.
9. Optionally, generate statistics, graphs, reports, etc. based on the captured packets or the analysis results.