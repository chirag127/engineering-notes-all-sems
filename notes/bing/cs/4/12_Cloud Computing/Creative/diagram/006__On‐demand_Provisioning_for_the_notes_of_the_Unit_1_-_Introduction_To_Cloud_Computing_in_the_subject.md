On-demand provisioning is a feature of cloud computing that allows customers to obtain cloud resources on runtime, according to their fluctuating demands . This reduces the cost and complexity of managing cloud resources, and enables customers to access cloud services through an online control panel .

The following diagram illustrates the basic architecture of on-demand provisioning in cloud computing using ASCII characters:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Cloud Service  |       |  Cloud Service  |       |  Cloud Service  |
|  Provider (CSP) |       |  Provider (CSP) |       |  Provider (CSP) |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Cloud Service  |       |  Cloud Service  |       |  Cloud Service  |
|  Consumer (CSC) |       |  Consumer (CSC) |       |  Consumer (CSC) |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Online Control |       |  Online Control |       |  Online Control |
|     Panel       |       |     Panel       |       |     Panel       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows three cloud service providers (CSPs) and three cloud service consumers (CSCs). Each CSC can access an online control panel to request cloud resources from any CSP on demand. The CSPs can dynamically allocate and deallocate cloud resources to the CSCs based on their requests and availability. This way, the CSCs can obtain the cloud resources they need, when they need them, without having to pay for or manage excess resources. This is the essence of on-demand provisioning in cloud computing.