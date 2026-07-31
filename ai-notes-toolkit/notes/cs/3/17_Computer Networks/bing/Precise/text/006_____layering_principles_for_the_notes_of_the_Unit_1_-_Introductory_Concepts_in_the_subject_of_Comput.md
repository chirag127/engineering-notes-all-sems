### Layering Principles

1. **Layering** is a design principle that divides a complex system into smaller, more manageable parts, called layers.
2. Each layer provides a specific set of services to the layer above it, and relies on the services provided by the layer below it.
3. The **OSI model** is an example of a layered architecture, with seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.
4. The **TCP/IP model** is another example of a layered architecture, with four layers: Link, Internet, Transport, and Application.
5. Layering allows for **modularity**, where each layer can be developed and updated independently of the others.
6. Layering also allows for **interoperability**, where different implementations of the same layer can communicate with each other.
7. However, layering can also introduce **overhead**, as each layer adds its own processing and data to the overall system.
8. The **encapsulation** process involves adding a header to the data at each layer, with the header containing information specific to that layer's protocol.
9. The **decapsulation** process involves removing the header at each layer, and using the information in the header to determine how to process the data.
10. The **peer-to-peer communication** between the same layers on different devices is achieved through the use of protocols, which define the rules and formats for exchanging data.
