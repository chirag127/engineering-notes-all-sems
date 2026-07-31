### Active database systems

- An active database system is a database system that includes an **event-driven architecture** that can respond automatically to events that occur inside or outside the database .
- An event is a change of state or a condition that is detected by the database system or an external agent.
- A typical active database system uses **ECA rules** (Event-Condition-Action rules) to specify the actions to be performed in response to events .
- An ECA rule has the form: **ON event IF condition DO action**.
- The event part specifies the event or a combination of events that trigger the rule.
- The condition part specifies a predicate that must be satisfied for the rule to be executed.
- The action part specifies the operation or a sequence of operations that are performed by the rule.
- Active database systems can be used for various purposes, such as security monitoring, alerting, statistics gathering, authorization, workflow management, data integration, and constraint enforcement .
- Active database systems are challenging to design, implement, and maintain, because of the complexity and unpredictability of the interactions among rules, events, and data .
- Some examples of active database systems are Oracle, IBM DB2, and Microsoft SQL Server.