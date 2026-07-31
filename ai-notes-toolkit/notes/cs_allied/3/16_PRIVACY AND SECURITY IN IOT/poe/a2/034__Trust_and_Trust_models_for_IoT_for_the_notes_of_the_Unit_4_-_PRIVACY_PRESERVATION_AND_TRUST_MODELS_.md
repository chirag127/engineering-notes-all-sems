 Here is the content in markdown format:

### Trust and Trust models for IoT

- **Direct trust**: Devices trust each other directly based on pre-shared keys or certificates. Scalability is a challenge as number of devices increase.
- **Web of trust**: Devices get endorsed by other trusted devices and build trust recursively. Scalability is better but vulnerability to malicious devices is higher.
- **Third party trust**: Trust is established through a third party certificate authority or cloud service. Scalability is good but single point of failure exists.
- **Reputation based trust**: Devices build trust based on other's experience of interactions with a device. Effective against selfish but not malicious devices. Vulnerable to Sybil attacks.
- **Policy based trust**: Fine grained access control policies specify trust between devices. Flexible but complex to implement and manage.
- **Blockchain based trust**: A blockchain is used to establish an immutable ledger of interactions between devices to build trust. Scalable and resilient but incurs overhead.

The choice of a trust model depends on the specific use case requirements such as scalability, resilience against attacks, complexity of implementation, etc. Hybrid models combining multiple schemes are also possible and can potentially achieve a good balance of properties. Establishing and maintaining trust is critical for the secure and reliable operation of IoT systems.

How's this? I have written the content in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.