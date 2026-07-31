#### Services in networks architecture in Computer Networks

- Services in networks architecture are the **functions** or **operations** that each layer of the network model provides to the layer above it or below it.
- Services are **abstract** and **independent** of the implementation details of the layer that provides them or the layer that uses them.
- Services are **defined** by a set of **primitives** or **commands** that specify the **type**, **parameters**, and **results** of the service.
- Services are **invoked** by the **service user** (the layer above) and **performed** by the **service provider** (the layer below) through the **service access point** (SAP), which is a logical point of interaction between the layers.
- Services can be **classified** into two types: **connection-oriented** and **connectionless**.
  - Connection-oriented services require the establishment of a **logical connection** between the service user and the service provider before any data can be exchanged. The connection is **terminated** after the data transfer is complete. Connection-oriented services provide **reliable**, **ordered**, and **error-free** delivery of data, but they also incur **overhead** and **delay** for connection setup and teardown.
  - Connectionless services do not require any connection establishment or termination. The service user can send data to the service provider at any time, without any prior agreement. Connectionless services provide **fast** and **efficient** delivery of data, but they do not guarantee **reliability**, **order**, or **error-correction**.
- Examples of services in networks architecture are:
  - **DHCP** (Dynamic Host Configuration Protocol): A service that assigns IP addresses and other network configuration parameters to hosts dynamically.
  - **DNS** (Domain Name System): A service that maps domain names to IP addresses and vice versa.
  - **FTP** (File Transfer Protocol): A service that allows users to transfer files between hosts over a network.
  - **HTTP** (Hypertext Transfer Protocol): A service that allows users to access web pages and other resources over a network.
  - **SMTP** (Simple Mail Transfer Protocol): A service that allows users to send and receive email messages over a network.