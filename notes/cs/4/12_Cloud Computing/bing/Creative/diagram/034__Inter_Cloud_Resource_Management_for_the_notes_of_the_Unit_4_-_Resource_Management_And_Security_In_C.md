Inter Cloud Resource Management is a concept that refers to the coordination and sharing of resources among different cloud service providers. It aims to overcome the limitations of single clouds, such as resource scarcity, vendor lock-in, geographic constraints, and service availability. Inter Cloud Resource Management can be achieved through different types of inter-cloud architectures, such as federation clouds, multi-clouds, and cloud brokers. The following diagram illustrates the basic architecture of a federation cloud, where several cloud service providers voluntarily link their cloud infrastructures together to exchange resources.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Cloud Service  |     |  Cloud Service  |     |  Cloud Service  |
|  Provider 1     |     |  Provider 2     |     |  Provider 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Cloud          |     |  Cloud          |     |  Cloud          |
|  Infrastructure |     |  Infrastructure |     |  Infrastructure |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Resource       |     |  Resource       |     |  Resource       |
|  Management     |     |  Management     |     |  Management     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Federation     |     |  Federation     |     |  Federation     |
|  Agent          |     |  Agent          |     |  Agent          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
                           |
                           |
                           v
                  +-----------------+
                  |                 |
                  |  Federation     |
                  |  Manager        |
                  |                 |
                  +-----------------+
```

The federation manager is a central entity that coordinates the resource allocation and utilization among the federation members. The federation agent is a local entity that communicates with the federation manager and the resource management system of each cloud service provider. The resource management system is responsible for managing the resources within each cloud infrastructure, such as computing, storage, and network resources. The cloud service provider offers various services to the end users, such as software as a service, platform as a service, or infrastructure as a service. The federation cloud enables the cloud service providers to dynamically scale their resources, improve their service quality, and reduce their operational costs .