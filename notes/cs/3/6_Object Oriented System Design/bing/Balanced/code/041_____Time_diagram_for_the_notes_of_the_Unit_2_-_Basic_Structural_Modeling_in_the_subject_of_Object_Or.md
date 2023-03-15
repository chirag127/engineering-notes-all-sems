### Time diagram for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

- Object Oriented System Design is a process of defining the architecture, modules, interfaces, and data for a system that uses objects and classes to model the real-world entities and their relationships.
- Basic Structural Modeling is a part of Object Oriented System Design that focuses on the static structure of the system, such as the classes, attributes, methods, and associations that represent the system's entities and their interactions.
- A time diagram is a type of UML diagram that shows the behavior of individual objects and interactions of objects along a linear time axis. It can be used to model the timing constraints and performance requirements of a system.
- A time diagram consists of the following elements:
  - Lifelines: vertical dashed lines that represent the existence of an object over time. They can have a name and a type, such as `:Customer` or `c:Customer`.
  - States: horizontal rectangles that show the state or condition of an object at a certain time interval. They can have a name, such as `active` or `idle`.
  - Events: points or ticks on the lifelines that indicate when something happens to or by an object, such as sending or receiving a message, changing state, or creating or destroying an object.
  - Messages: horizontal arrows that show the communication between objects. They can have a name, such as `request()` or `response()`, and a sequence number, such as `1` or `1.1`.
  - Constraints: expressions that specify the temporal relationships between events or states, such as `t1 < t2` or `t3 - t4 = 5s`.
  - Duration: a value or a range that specifies the length of time that an event or a state lasts, such as `10s` or `[5s..15s]`.
- An example of a time diagram is shown below:

```
@startuml
participant ":Customer" as c
participant ":ATM" as a
participant ":Bank" as b

c -> a: 1. insertCard()
activate a
a -> c: 2. requestPIN()
activate c
c -> a: 3. enterPIN()
deactivate c
a -> b: 4. validatePIN()
activate b
b -> a: 5. PINresult()
deactivate b
a -> c: 6. displayMenu()
activate c
c -> a: 7. selectWithdrawal()
deactivate c
a -> b: 8. checkBalance()
activate b
b -> a: 9. balanceResult()
deactivate b
a -> c: 10. requestAmount()
activate c
c -> a: 11. enterAmount()
deactivate c
a -> b: 12. withdrawMoney()
activate b
b -> a: 13. withdrawalResult()
deactivate b
a -> c: 14. dispenseCash()
activate a
a -> c: 15. ejectCard()
deactivate a
@enduml
```

![time diagram example](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLd1EBLBGjLDmpCbCJbMmKiX8pSd9vL0gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL2gNafCJYp9vL