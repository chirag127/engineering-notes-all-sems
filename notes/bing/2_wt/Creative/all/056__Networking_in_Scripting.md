### Networking in Scripting

- Networking in scripting is the process of using code, concepts based on the software development lifecycle, and other tools to make networks perform actions.
- Scripting lets you automate various network administration tasks, such as those that are performed every day or even several times a day.
- Scripting in network administration offers significant advantages. It allows you to:
  - Save time —Scripts can carry out complex tasks and be invoked automatically, without the intervention of the network administrator, so the admin can concentrate on other tasks while the script runs.
  - Increase accuracy —Scripts can reduce human errors and ensure consistency in network configuration and management.
  - Enhance security —Scripts can enforce security policies and monitor network activity for potential threats.
  - Improve scalability —Scripts can adapt to changing network conditions and requirements, and handle multiple devices and platforms.
- Scripting languages are high-level languages that are interpreted rather than compiled, which means they are easier to write, debug, and modify than low-level languages.
- Some examples of scripting languages that are commonly used for networking are:
  - Python —A versatile, powerful, and popular language that has many libraries and modules for networking, such as socket, requests, scapy, paramiko, etc .
  - PowerShell —A Windows-based language that can interact with various network components and protocols, such as Active Directory, DNS, DHCP, TCP/IP, etc .
  - Bash —A UNIX-based language that can execute commands and scripts on remote servers and devices, and manipulate files and data over the network .
- A basic example of networking in scripting is making HTTP requests to a web server using Python. The following code snippet shows how to use the requests module to send a GET request to a URL and print the response status code and content:

```python
import requests
url = "https://www.example.com"
response = requests.get(url)
print(response.status_code)
print(response.text)
```

- Some mnemonics and learning tricks for networking in scripting are:
  - Remember the OSI model layers using the phrase "Please Do Not Throw Sausage Pizza Away", which stands for Physical, Data Link, Network, Transport, Session, Presentation, and Application.
  - Remember the TCP/IP model layers using the acronym "NITA", which stands for Network Interface, Internet, Transport, and Application.
  - Remember the common port numbers for some network protocols using the following associations:
    - 20 and 21 for FTP (File Transfer Protocol), which sounds like "to FTP"
    - 22 for SSH (Secure Shell), which sounds like "to SSH"
    - 23 for Telnet, which sounds like "tell net"
    - 25 for SMTP (Simple Mail Transfer Protocol), which sounds like "send mail to 5 people"
    - 53 for DNS (Domain Name System), which sounds like "D is 5, N is 3"
    - 80 for HTTP (Hypertext Transfer Protocol), which sounds like "ate 0"
    - 443 for HTTPS (Hypertext Transfer Protocol Secure), which sounds like "for secure"