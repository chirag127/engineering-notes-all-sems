# Introduction to browser isolation

Browser isolation is a cybersecurity model that aims to physically isolate an internet user's browsing activity (and the associated cyber risks) away from their local networks and infrastructure. Browser isolation can help protect computers from malware, phishing, ransomware, and other web-based threats by preventing malicious code from reaching the endpoint device.

There are different types of browser isolation, depending on where the isolation occurs and how the web content is delivered to the user. Some of the common types are:

- **Remote browser isolation**: This type of browser isolation loads webpages and executes any associated JavaScript code on a cloud server, far away from the user's device. The server then sends a safe representation of the web content to the user's browser, such as an image or a video stream. This way, the user can interact with the web content without exposing their device to any potential harm.
- **On-premise browser isolation**: This type of browser isolation does the same thing as remote browser isolation, but on a server that an organization manages internally. This may offer more control and customization over the isolation environment, but also requires more resources and maintenance.
- **Client-side browser isolation**: This type of browser isolation uses virtualization or containerization technology to isolate the user's web browsing activity away from the rest of the device. The user's browser runs inside a sandbox or a virtual machine that is separate from the operating system and the local network. Any malicious code that may be encountered during browsing is confined within the isolated environment and cannot affect the device or the network .
- **Hardware-based browser isolation**: This type of browser isolation leverages hardware features to create a secure boundary between the user's browser and the rest of the device. For example, Microsoft Edge supports browser isolation using Application Guard, which uses the Windows hypervisor to create a virtualized container for the browser. This container is isolated from the host operating system, the local network, and the internet, and can only access a limited set of resources. Any malicious code that may be encountered during browsing is discarded when the container is closed .

Browser isolation can offer several benefits for cybersecurity, such as:

- Reducing the attack surface for web-based threats by preventing malicious code from reaching the endpoint device or the network.
- Enhancing the user experience by allowing the user to access any web content without compromising security or performance.
- Simplifying the security management by reducing the need for complex web filtering, whitelisting, or blacklisting policies.
- Complementing other security solutions by adding an extra layer of protection for web browsing activity.