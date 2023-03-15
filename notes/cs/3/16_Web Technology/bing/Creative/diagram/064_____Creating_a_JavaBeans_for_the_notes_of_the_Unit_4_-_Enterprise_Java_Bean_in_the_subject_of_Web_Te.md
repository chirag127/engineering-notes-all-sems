### Creating a JavaBeans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- JavaBeans is a technology developed by Sun Microsystems and released in 1996, as part of JDK 1.1.
- JavaBeans are classes that encapsulate one or more objects into a single standardized object (the bean).
- JavaBeans are reusable software components that can be easily developed and assembled to create sophisticated applications.
- JavaBeans have the following features :
  - Properties: attributes that define the state or appearance of a bean.
  - Methods: operations that a bean can perform or that can be invoked by other beans or applications.
  - Events: notifications that a bean can send or receive when something of interest happens.
  - Persistence: the ability to save and restore the state of a bean to and from a persistent storage.
- To create a JavaBeans class, the following conventions must be followed :
  - The class must have a public default constructor (no-argument constructor).
  - The class must implement the java.io.Serializable interface or its subinterface.
  - The class must follow the JavaBeans naming conventions for properties, methods and events.
  - The class may optionally implement the java.beans.Customizer interface to provide a custom GUI for editing the bean's properties.
  - The class may optionally provide a BeanInfo class that describes the bean's properties, methods, events and other information.