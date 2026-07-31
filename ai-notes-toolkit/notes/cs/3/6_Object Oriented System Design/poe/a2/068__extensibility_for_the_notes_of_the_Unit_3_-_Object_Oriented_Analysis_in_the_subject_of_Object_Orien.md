 Here are the notes on extensibility for Unit 3 - Object Oriented Analysis in Object Oriented System Design:

### Extensibility

1. Open for Extension: The system should be designed in a way that it can be easily extended to incorporate new requirements or capabilities. This makes the system future-proof and adaptable to changes.
2. Closed for Modification: The existing code should be protected from modifications whenever new capabilities are added. This can be achieved using techniques like inheritance, interfaces, polymorphism, etc. so that the core system logic remains untouched.
3. Plugins/Extensions: The system can provide well-defined plugin architectures or APIs using which external extensions or plugins can be built to add new capabilities. This avoids modifying the core system and keeps it extensible.
4. Configuration over Code Changes: Wherever possible, new capabilities should be added via configuration changes rather than code changes. This makes the system easy to extend without in-depth technical knowledge.
5. Minimal Coupling: The system components should be loosely coupled so that new additions do not impact existing components. This can be achieved using separation of concerns, well-defined interfaces, dependency inversion, etc.
6. Graceful Degradation: If an extension is not supported by some system components, the system should degrade gracefully instead of failing abruptly. This makes the system robust and resilient to changes.

The above points cover some key characteristics and techniques to design an extensible system that can accommodate new requirements and capabilities without major code changes to the core system logic. Applying object-oriented principles and following a modular, loosely coupled architecture helps in building extensible systems.