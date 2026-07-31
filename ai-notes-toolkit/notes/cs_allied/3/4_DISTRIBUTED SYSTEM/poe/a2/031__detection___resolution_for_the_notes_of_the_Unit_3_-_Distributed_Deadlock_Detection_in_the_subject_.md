 Here is the formal content in Markdown format without any emojis or external links for the topic - Detection & Resolution for Distributed Deadlock Detection:

### Detection & Resolution for Distributed Deadlock Detection

1. Deadlock Detection:
- Centralized approach: Elect a coordinator which maintains the global state and checks for deadlock.
- Distributed approach: Each process detects local deadlock and informs the coordinator. The coordinator determines if it is a global deadlock.
- Time-out based approach: Each process waits for a fixed time period for requests to be granted. If it times out, it aborts one of its transactions.

2. Deadlock Prevention:
- Limit number of resources a process can hold.
- Require processes to request resources in a specific order.
- Require resources to be allocated in a specific order.

3. Deadlock Avoidance:
- Each process estimates future resource needs before requesting resources. If it is possible that deadlock may occur if request is granted, then it delays the request.
- The allocation is allowed only if it is proved that no deadlock will occur due to the allocation.

4. Deadlock Recovery:
- Abort one or more processes to break the deadlock.
- Backtrack by rolling back processes to a safe state and then reschedule resources.
- The process that has used least resources or has the shortest expected processing time can be chosen for abortion.

The content covers the key points on the ways to detect, prevent and resolve distributed deadlocks. The points are written concisely in the list format as instructed. The tone is formal and no emoji or external links are included. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.