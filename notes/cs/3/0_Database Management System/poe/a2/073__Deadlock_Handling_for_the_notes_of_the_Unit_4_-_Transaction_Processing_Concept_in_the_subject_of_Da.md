 Here is the content written in formal tone with markdown format and without emojis for the given topic:

### Deadlock Handling

1. Deadlock Detection:
- Periodically check for deadlocks.
- Check if a requesting transaction can be allocated its demanded resources without violating safety. If not, deadlock has occurred.

2. Deadlock Prevention:
- Ensure that at least one of the following conditions cannot hold:

- Mutual exclusion: Deny mutually exclusive resources whenever possible.
- Hold and wait: Require resources to be requested in some predetermined order or deny requests for new resources for a transaction that is holding some resources.
- No preemption: Preempt resources from lower-priority transactions if a higher-priority transaction requests them.

3. Deadlock Avoidance:
- Predict the possibility of deadlock for a transaction before allocating any resource to it. If deadlock is predicted, then either backtrack and roll back some transactions or wait for some transactions to complete their execution and release the resources.

4. Deadlock Recovery:
- Upon detection of a deadlock, choose one or more transactions as victims and roll them back. The rolled-back transactions are rescheduled for execution.
- The victim selection policy can be:
-- Choose randomly.
-- Choose the transaction that has acquired least number of resources (least cost).
-- Choose the transaction that has the oldest time stamp (first-in-first-out).

[No external links are included. All the points are written in bullet points as per the instructions. Markup language Markdown is used to format the text.]