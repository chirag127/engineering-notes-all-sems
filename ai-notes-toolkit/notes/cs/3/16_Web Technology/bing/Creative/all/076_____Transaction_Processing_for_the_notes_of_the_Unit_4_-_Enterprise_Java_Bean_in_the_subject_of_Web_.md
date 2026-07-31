# Transaction Processing for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- Transaction processing is the execution of a series of operations on a set of data in a reliable, consistent, and atomic manner.
- A transaction is a logical unit of work that either completes entirely or has no effect at all.
- Transactions are important for ensuring data integrity and consistency in distributed applications.
- Enterprise Java Beans (EJB) is a technology that supports distributed transactional component-based applications written in Java.
- EJB provides two types of transaction management: container-managed and bean-managed.
- In container-managed transactions, the EJB container sets the boundaries of the transactions and controls the transaction propagation.
- In bean-managed transactions, the EJB code explicitly marks the transaction boundaries and uses the Java Transaction API (JTA) to interact with the transaction manager .
- EJB supports flat transactions, which are independent of other transactions in the system and cannot be nested.
- EJB transactions can be configured with different attributes that specify the transaction behavior of the EJB methods.
- EJB transactions can also use annotations from the EJB spec to declare the transaction attributes and demarcate the transaction boundaries.

: https://docs.oracle.com/cd/E19229-01/819-1644/detrans.html
: https://www.researchgate.net/publication/2365544_Advanced_Transactions_in_Enterprise_JavaBeans
: https://www.baeldung.com/java-transactions
: https://stackify.com/enterprise-java-beans/