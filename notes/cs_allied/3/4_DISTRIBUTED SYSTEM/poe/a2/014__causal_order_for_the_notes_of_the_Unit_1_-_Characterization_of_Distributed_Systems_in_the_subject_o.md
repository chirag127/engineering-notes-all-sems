 Here are the notes on causal order for Unit 1 - Characterization of Distributed Systems in markdown format:

### Causal Order

* Events in a distributed system occur in causal order if the happens-before relationship is acyclic.
* The happens-before relationship is the transitive closure of the following relation:
** Event a happens before event b if a is the sending of a message and b is the receipt of that message.
** Event a happens before event b if a is the writing of a variable by one process and b is the subsequent reading of that variable by another process.
* Causal order ensures that events are processed in an order consistent with the actual causal relationships between events.
* Total order is a special case of causal order where the happens-before relationship is total (any two events are comparable).
* Causal order is necessary for the correct operation of distributed systems since it ensures that events are processed in an order consistent with the actual causal relationships between events. Total order is not always needed and can reduce performance.

The notes are written in a formal tone with points and without any emojis or external links as per the given instructions. The content is written in markdown format inside the header for the given topic from the specified subject. Please let me know if you would like me to modify or expand the notes.