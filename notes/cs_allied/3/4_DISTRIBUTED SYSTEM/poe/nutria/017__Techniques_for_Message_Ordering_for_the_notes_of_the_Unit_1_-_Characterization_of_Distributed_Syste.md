
### Techniques for Message Ordering

1. Total Order: All messages sent by all processes are totally ordered.
2. Causal Order: Messages sent by a process are causally ordered, i.e., messages sent by a process are totally ordered but messages sent by different processes may be partially ordered.
3. FIFO Order: Messages sent by a process are FIFO ordered, i.e., messages sent by a process are totally ordered and messages sent by different processes are causally ordered.
4. Local Order: Messages sent by a process are locally ordered, i.e., messages sent by a process are totally ordered and messages sent by different processes may be partially ordered.
5. Eventual Order: Messages sent by a process are eventually ordered, i.e., messages sent by a process are totally ordered but messages sent by different processes may be partially ordered.