Fault tolerance is a property of a distributed system that helps it to continue working when some of its components fail. For a system to have this property, many separate issues are involved, such as:

- Fault confinement: preventing the propagation of errors from one component to another
- Fault detection: identifying the presence and location of faults in the system
- Fault masking: hiding the effects of faults from the users or other components
- Retry: repeating a failed operation or request
- Diagnosis: determining the cause and nature of faults
- Reconfiguration: changing the structure or configuration of the system to cope with faults
- Recovery: restoring the system to a consistent and correct state after a fault
- Restart: restarting a failed component or the whole system
- Repair: fixing or replacing a faulty component
- Reintegration: reintegrating a repaired component into the system

The following diagram illustrates the basic architecture of a fault tolerant distributed system using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Component 1    |----|  Component 2    |----|  Component 3    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Fault Tolerant |----|  Fault Tolerant |----|  Fault Tolerant |
|  Middleware     |    |  Middleware     |    |  Middleware     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  User           |----|  User           |----|  User           |
|  Application    |    |  Application    |    |  Application    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows three components of a distributed system, each connected to a fault tolerant middleware layer that provides the services and mechanisms for dealing with faults. The middleware layer is also connected to the user applications that use the distributed system. The middleware layer can perform functions such as:

- Monitoring the health and status of the components
- Detecting and reporting faults to the components and the users
- Masking faults by providing alternative or degraded services
- Retrying failed operations or requests
- Diagnosing faults and initiating repair actions
- Reconfiguring the system by adding, removing, or replacing components
- Recovering the system state from checkpoints or backups
- Restarting failed components or the whole system
- Reintegrating repaired components into the system

The diagram is a simplified representation of a fault tolerant distributed system. In reality, there can be more components, more middleware layers, more connections, and more types of faults and issues. The design and implementation of a fault tolerant distributed system is a complex and challenging task that requires careful analysis, testing, and evaluation.