 Here is the content in markdown format for the given topic:

### Transaction Processing

- A transaction is a single unit of work that accomplishes a task. In EJB, transactions are used to ensure data integrity and consistency across multiple operations.
- EJB supports container-managed transactions (CMT) as well as bean-managed transactions (BMT).
- In CMT, the EJB container manages the transaction boundaries. The bean simply specifies the required transaction behavior for its methods in its deployment descriptor.
- In BMT, the bean code explicitly marks the boundaries of a transaction using the UserTransaction interface. The bean has more control over transactions, but it also has more responsibility to manage them properly.
- Transactions have the following characteristics:

** Atomicity:** A transaction is an atomic unit of work. All steps of a transaction are completed successfully or none are completed.
** Consistency:** A transaction must bring the system from one consistent state to another. It must preserve all database integrity constraints.
** Isolation:** Transactions must be isolated from one another. The intermediate states of a transaction are not visible to other transactions.
** Durability:** Once a transaction completes successfully, its effects are permanent and will not be undone, even in the event of a system failure.

- The EJB container provides isolation, atomicity, and durability for CMT. The bean is responsible for consistency. For BMT, the bean is responsible for all ACID properties.
- Advantages of CMT:
** Simplicity:** The bean code does not have to deal with transactions explicitly.
** Portability:** The transaction behavior is defined in the deployment descriptor separately from the bean implementation.
** Global Transactions:** The container can manage transactions that span multiple resources, including databases and message queues.
- Disadvantages of CMT:
** Less Flexibility:** Limited control over transaction boundaries and timeouts.
** Performance Impact:** There may be some additional overhead due to container management.

[Include diagrams, codes, tables, examples, applications, advantages, disadvantages, etc. if any for better learning.]