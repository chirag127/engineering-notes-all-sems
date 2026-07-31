# Browser isolation

Browser isolation is a cybersecurity model that aims to physically isolate an internet user's browsing activity (and the associated cyber risks) away from their local networks and infrastructure. It is based on the principle of least privilege, which grants the minimum level of access and permissions necessary for a task.

Some of the benefits of browser isolation are:

- It reduces the attack surface for web-based threats, such as phishing, malware, ransomware, and zero-day exploits.
- It protects the endpoint device and the network from malicious or compromised websites and web content.
- It enhances the user experience by allowing access to any website without compromising security or performance.
- It simplifies the management and maintenance of security policies and updates.

Some of the types of browser isolation are:

- Remote browser isolation: This type of browser isolation loads webpages and executes any associated JavaScript code on a cloud server, far away from the endpoint device and the network. The user only sees a safe rendering of the webpage on their browser, which is delivered as pixels or vector graphics. This type of browser isolation can be implemented as a cloud service or as an on-premise solution.
- Client-side browser isolation: This type of browser isolation uses a sandbox or a virtual machine on the endpoint device to isolate the web browsing activity from the rest of the system. The user interacts with the isolated browser as they would with a normal browser, but any malicious web content is contained within the sandbox or the virtual machine. This type of browser isolation requires more resources and maintenance on the endpoint device.
- Hardware-based browser isolation: This type of browser isolation leverages the hardware capabilities of the endpoint device to create a secure and isolated environment for web browsing. For example, Microsoft Edge supports browser isolation using Microsoft Defender Application Guard, which uses the virtualization-based security features of Windows 10 to create a container for the browser. The user can switch between the normal browser and the isolated browser as needed, and any malicious web content is deleted when the container is closed. This type of browser isolation requires compatible hardware and software on the endpoint device.