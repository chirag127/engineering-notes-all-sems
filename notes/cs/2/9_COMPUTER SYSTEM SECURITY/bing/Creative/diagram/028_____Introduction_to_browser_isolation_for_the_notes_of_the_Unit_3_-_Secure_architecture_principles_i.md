### Introduction to browser isolation

Browser isolation is a cybersecurity model that aims to physically isolate an internet user's browsing activity (and the associated cyber risks) away from their local networks and infrastructure. Browser isolation can help protect computers from malware, phishing, ransomware, and other web-based threats by preventing malicious code from reaching the endpoint device.

There are different types of browser isolation, such as:

- Remote browser isolation: This type of browser isolation loads webpages and executes any associated JavaScript code on a cloud server, far away from the user's device. The user only sees a rendered image or video of the webpage, which is delivered through a secure channel. This way, any malicious code is contained on the remote server and cannot harm the user's device or network.
- On-premise browser isolation: This type of browser isolation does the same thing as remote browser isolation, but on a server that an organization manages internally. This may offer more control and customization over the isolation environment, but also requires more resources and maintenance.
- Client-side browser isolation: This type of browser isolation uses virtualization or containerization technology to isolate the web browsing activity away from the endpoint device. The browser runs in a sandbox or a virtual machine, which acts as a buffer between the web and the device. Any malicious code is trapped inside the sandbox or the virtual machine and cannot access the device's files or resources .

Browser isolation can offer several benefits, such as:

- Enhanced security: Browser isolation can reduce the attack surface for web-based threats and prevent malware from compromising the device or the network. It can also protect the user's identity and credentials from phishing and other forms of social engineering.
- Improved performance: Browser isolation can improve the speed and responsiveness of web browsing, as the browser does not have to process or render complex web content on the device. It can also save bandwidth and storage space, as the browser does not have to download or cache web content on the device.
- Simplified management: Browser isolation can simplify the administration and maintenance of web security policies and updates, as the browser isolation environment can be centrally managed and controlled. It can also reduce the need for endpoint security software and patches, as the browser isolation environment can handle most of the web security functions.

One example of browser isolation technology is Microsoft Defender Application Guard, which is a feature of Microsoft Edge that uses hardware-based isolation to protect the device from web-based threats. It can run untrusted websites and files in an isolated container, which is separated from the device by using Hyper-V virtualization technology. It can also integrate with Microsoft Defender SmartScreen and Microsoft Defender for Endpoint to provide additional layers of protection .

The following diagram illustrates how browser isolation works using Microsoft Defender Application Guard:

![Diagram of browser isolation using Microsoft Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-application-guard/media/application-guard-overview.png)

Source: https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-application-guard/overview-app-guard

: https://en.wikipedia.org/wiki/Browser_isolation
: https://www.mcafee.com/content/enterprise/en-us/security-awareness/cloud/what-is-browser-isolation.html
: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-video-security-application-guard
: https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/
: https://learn.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-application-guard/install-md-app-guard