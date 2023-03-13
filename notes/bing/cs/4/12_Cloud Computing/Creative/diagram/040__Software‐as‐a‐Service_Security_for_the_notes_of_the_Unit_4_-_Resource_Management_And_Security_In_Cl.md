Software‐as‐a‐Service (SaaS) is a business model that provides access to applications over the internet or cloud. SaaS implies a subscription-based and centrally-hosted model of software licensing and deployment . SaaS security is the practice of protecting the data and applications that are hosted by a third-party provider on a remote server. SaaS security requires a shared responsibility model between the provider and the customer, as well as a security architecture that connects with the overall enterprise security approach .

The following diagram illustrates the basic architecture of a SaaS security model using ASCII characters:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   SaaS Provider |      |   SaaS Customer |      |   SaaS User     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Application    |      |  Subscription   |      |  Authentication |
|  Security       |      |  Management     |      |  and Access     |
|                 |      |                 |      |  Control        |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Identity and   |      |  Cloud Access   |      |  Data Security  |
|  Access         |      |  Security       |      |  and Privacy    |
|  Management     |      |  Broker (CASB)  |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Infrastructure |      |  Enterprise     |      |  Endpoint       |
|  Security       |      |  Security       |      |  Security       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Cloud Service  |<---->|  Internet       |<---->|  Device         |
|  Provider (CSP) |      |                 |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```