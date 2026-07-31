### Event and signals

- An event is something that happens and triggers a change in the state of an object or a system .
- Events can be external or internal .
  - External events are those that pass between the system and its actors (users or other systems).
  - Internal events are those that pass among the objects that live within the system.
- There are four kinds of events  :
  - Signals: A signal is an object that is dispatched (thrown) asynchronously by one object and then received (caught) by another . A signal event is the event of sending or receiving a signal. A signal can carry data and can be used to notify another object about a change in state or a request for action. A signal is visualized as a dashed arrow with a filled arrowhead in a sequence diagram .
  - Calls: A call is an invocation of an operation on another object . A call event is the event of invoking or executing an operation. A call is synchronous, which means that the sender object waits for the receiver object to complete the operation and return control to the sender . A call is visualized as a solid arrow with a filled arrowhead in a sequence diagram .
  - Time: A time event is the event of reaching a specific point in time or a specific duration of time . A time event can be used to model timeouts, delays, or periodic occurrences. A time event is visualized as a dashed arrow with a clock symbol in a sequence diagram .
  - Change: A change event is the event of a change in the value or state of an attribute, a variable, or a condition . A change event can be used to model transitions, guards, or triggers in a state machine diagram. A change event is visualized as a dashed arrow with a pentagon symbol in a state machine diagram .