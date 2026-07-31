### Event and signals

- An event is something that happens during the execution of a system that triggers a change in the state or behavior of an object .
- Events can be external or internal .
  - External events are those that pass between the system and its actors (users or other systems).
  - Internal events are those that pass among the objects that live within the system.
- There are four kinds of events  :
  - Signals: A signal is an object that is dispatched (thrown) asynchronously by one object and then received (caught) by another . A signal event is the event of sending or receiving a signal. A signal can carry data as its attributes. A signal does not imply a response from the receiver. A signal is represented by a dashed arrow with a filled triangle as the arrowhead .
  - Calls: A call is an invocation of an operation on another object . A call event is the event of invoking or executing an operation. A call can also carry data as its parameters. A call implies a response from the receiver, which means that the sender waits for the operation to complete before resuming its own execution . A call is represented by a solid arrow with an open triangle as the arrowhead .
  - Time: A time event is the event of reaching a specific point in time or a specific duration of time . A time event can be used to model timeouts, delays, or periodic occurrences. A time event is represented by a stopwatch icon .
  - Change: A change event is the event of a change in the state or value of an object or a variable . A change event can be used to model triggers, guards, or conditions. A change event is represented by a hexagon with a lightning bolt icon .
- Events and signals are important for modeling the dynamic behavior of a system and its objects, as they capture the interactions and communications among them . Events and signals can be used to specify the sequence, timing, and conditions of the messages exchanged in a system . Events and signals can also be used to specify the state transitions and actions of an object in response to different stimuli .