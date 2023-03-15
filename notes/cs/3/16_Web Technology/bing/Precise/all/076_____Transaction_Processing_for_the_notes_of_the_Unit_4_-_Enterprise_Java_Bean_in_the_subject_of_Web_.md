# Transaction Processing

Transaction processing is an essential part of Enterprise Java Beans (EJB) and is covered in Unit 4 of the Web Technology course. Here are some key points to remember:

1. Transaction processing refers to the handling of multiple transactions in a reliable and efficient manner.
2. Transactions are a series of operations that must be completed as a whole. If any part of the transaction fails, the entire transaction must be rolled back.
3. EJBs support transaction processing through the use of container-managed transactions (CMT) and bean-managed transactions (BMT).
4. CMT allows the EJB container to automatically manage transactions on behalf of the bean.
5. BMT allows the bean to explicitly manage its own transactions.
6. EJBs can use the Java Transaction API (JTA) to manage transactions.
7. Transactions can have different levels of isolation, which determines how data is shared between transactions.
8. Transactions can also have different levels of propagation, which determines how transactions are nested within one another.

These are some of the key points to remember when studying transaction processing in the context of EJBs and Web Technology. It is important to understand the concepts and mechanisms behind transaction processing in order to effectively use EJBs in web applications.