 Here are the notes on causal order for Unit 1 - Characterization of Distributed Systems in a formal tone:

### Causal Order

1. Messages in a distributed system may be delivered out of order. Causal order ensures that messages are delivered in the same order as they were sent.
2. If event A causes event B, then B cannot happen before A in causal order.
3. Causal order is necessary to maintain correctness in a distributed system. For example, if a bank transfer is initiated after a deposit, the transfer cannot complete before the deposit.
4. Causal order can be ensured in a distributed system by:
- Including sequence numbers with messages
- Including information about the events that a message is dependent on (e.g. include identifiers of previous messages that the current message is responding to)
- Tracking the happens-before relationship between events to infer causal dependencies

The above notes cover the key points on causal order to formalize the understanding of distributed system characterization. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.