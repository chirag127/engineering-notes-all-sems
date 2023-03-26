 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Comparison of methods for concurrency control

1. Locking:
- Exclusive lock: Only one transaction can access the data at a time. Prevents dirty reads but can lead to deadlocks and low concurrency.
- Shared lock: Multiple transactions can read the data simultaneously but only one transaction can write to the data at a time. Prevents dirty reads but allows higher concurrency than exclusive locks.

2. Time stamp ordering: Each transaction is assigned a unique time stamp. Transactions are committed in the order of their time stamps to ensure serializability. The system clock must be synchronized for this method to work accurately.

3. Optimistic concurrency control: Transactions proceed without acquiring locks, validating or aborting at the end if a conflict is detected. This method has higher concurrency but may result in more aborts and wasted work. Conflicts can be detected using time stamps or versions.

4. Validation: Read operations do not block writes but writes verify that the read data has not been modified by another transaction before committing. This is a Hybrid of locking and time stamp ordering methods and can avoid some problems of the two methods.

The method chosen for a system depends on the requirements such as performance, number of conflicts and complexity. No one method is ideal for all situations. A combination of methods is sometimes used to gain the advantages of multiple approaches.

How's that? I have written the points in a formal tone with no emojis or external links as instructed. Let me know if you would like me to modify or expand the answer.