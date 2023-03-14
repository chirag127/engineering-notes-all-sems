Hello, I am Sydney, your AI assistant. I can help you with drawing diagrams in ASCII format. 

The following diagram illustrates the emergence of MSA from SOA:

```
+-----------------+     +-----------------+     +-----------------+
| Monolithic      |     | SOA             |     | MSA             |
| Architecture    |     | Architecture    |     | Architecture    |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Application | |     | | Service 1   | |     | | Service 1   | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Database    | |     | | Service 2   | |     | | Service 2   | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Middleware  | |     | | Service 3   | |     | | Service 3   | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Single unit of  |     | Coarse-grained |     | Fine-grained   |
| deployment      |     | services       |     | services       |
|                 |     |                 |     |                 |
| High coupling   |     | Loose coupling |     | Loose coupling |
| and cohesion    |     | and cohesion   |     | and cohesion   |
|                 |     |                 |     |                 |
| Centralized     |     | Centralized    |     | Decentralized  |
| governance      |     | governance     |     | governance     |
|                 |     |                 |     |                 |
| Shared database |     | Shared database|     | Database per   |
|                 |     |                 |     | service        |
|                 |     |                 |     |                 |
| Difficult to    |     | Easier to      |     | Easier to      |
| scale and       |     | scale and      |     | scale and      |
| maintain        |     | maintain       |     | maintain       |
|                 |     |                 |     |                 |
| Low resilience  |     | Moderate       |     | High resilience|
|                 |     | resilience     |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows how MSA emerged from SOA by breaking down the services into smaller and more independent units that can be deployed, scaled, and maintained separately. MSA also introduced decentralized governance and database per service to reduce the dependencies and increase the resilience of the services. MSA is a subset of SOA that applies the same principles of service-orientation, but adds more constraints to ensure the autonomy and reliability of each service.