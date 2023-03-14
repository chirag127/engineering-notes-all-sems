The following is a detailed ASCII diagram for Virtualization Structures for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing.

The diagram illustrates the basic architecture of a service-oriented system, where service consumers interact with service providers through service intermediaries. The service intermediaries are responsible for abstracting the physical location and implementation details of the service providers, as well as providing additional functionalities such as routing, security, and monitoring. The service providers are self-contained units of software functionality that can be accessed remotely and updated independently. The service consumers are applications or components that invoke the services provided by the service providers.

The diagram uses the following symbols:

- [C] represents a service consumer
- [I] represents a service intermediary
- [P] represents a service provider
- --> represents a service invocation or request
- <-- represents a service response or result
- | represents a network boundary

The diagram is as follows:

```
[C] --> [I] | [P]
    <--     |
```

This means that the service consumer sends a service request to the service intermediary, which then forwards it to the service provider across a network boundary. The service provider then sends back a service result to the service intermediary, which then returns it to the service consumer.

The diagram can be extended to show multiple service consumers, service intermediaries, and service providers, as well as different patterns of service virtualization, such as service selection, service aggregation, and service transformation. For example, the following diagram shows a service selection pattern, where the service intermediary chooses the appropriate service provider based on the context of the service request:

```
[C] --> [I] | [P1]
    <--     |
          | [P2]
          | [P3]
```

This means that the service consumer sends a service request to the service intermediary, which then selects one of the three service providers based on some criteria, such as the service level, the availability, or the location. The service intermediary then forwards the service request to the selected service provider and returns the service result to the service consumer.