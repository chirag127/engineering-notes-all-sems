### TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented transport layer protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that packet losses are mostly due to network congestion and reacts by reducing its sending rate to avoid further losses and alleviate congestion.
- However, in wireless networks, packet losses can also occur due to other factors such as bit errors, fading, handoffs, and mobility, which are not related to congestion.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce its sending rate when wireless losses occur, resulting in poor performance and low network utilization.
- Therefore, it is essential to have mechanisms that can improve TCP's performance in wireless networks and enable efficient integration of wireless networks with the Internet.
- There are two main approaches to improve TCP performance over wireless networks: (1) hide non-congestion losses from the TCP sender, and (2) adapt the TCP sender to realize that some losses are not due to congestion.
- The first approach can be implemented by using either TCP-aware or TCP-unaware reliable link layer protocols, or by using split connection schemes with separate wireline and wireless TCP connections.
- The second approach can be implemented by using selective acknowledgments or explicit loss notification schemes that inform the TCP sender about the cause and location of losses.
- Each approach has its own advantages and disadvantages in terms of complexity, ease of deployment, and performance in different scenarios.
- Some of the challenges and issues that need to be considered when designing and evaluating TCP over wireless mechanisms are: scalability, fairness, compatibility, security, and energy efficiency.