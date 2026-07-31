# Transaction System

A transaction system is a system that processes and records the daily transactions of a business or an organization. A transaction is a single unit of work or logic that involves one or more operations on a database. A transaction system ensures that the transactions are performed in a consistent, reliable, and atomic way, meaning that either all the operations in a transaction are completed successfully or none of them are.

Some examples of transaction systems are:

- CRM (Customer Relationship Management) system: This system manages the interactions and relationships with the customers of a business. It stores information such as customer profiles, contact details, purchase history, feedback, etc. A transaction in this system could be adding a new customer, updating a customer's information, or deleting a customer.
- HRM (Human Resources Management) system: This system manages the employees and their activities in an organization. It stores information such as employee profiles, payroll, benefits, performance, etc. A transaction in this system could be hiring a new employee, updating an employee's salary, or terminating an employee.
- ERP (Enterprise Resource Planning) system: This system integrates and coordinates the various functions and processes of an organization. It stores information such as inventory, production, sales, accounting, etc. A transaction in this system could be ordering a new product, updating the inventory, or generating an invoice.

A transaction system uses a database management system (DBMS) to store and manipulate the data in the database. A DBMS is a software tool that enables users to access and interact with the underlying data in the database. A DBMS provides features such as data security, data integrity, data backup, data recovery, data concurrency, etc. A DBMS also supports transaction management, which is the process of controlling and monitoring the transactions in the database. Transaction management ensures that the transactions follow the ACID properties, which are:

- Atomicity: A transaction is either fully completed or fully aborted. There is no partial execution of a transaction.
- Consistency: A transaction preserves the consistency of the database. It does not violate any integrity constraints or business rules.
- Isolation: A transaction is isolated from other concurrent transactions. It does not interfere with or affect the results of other transactions.
- Durability: A transaction is permanently recorded in the database. It is not lost or undone due to system failures or errors.

To achieve the ACID properties, a transaction system uses techniques such as locking, logging, checkpointing, recovery, etc. These techniques ensure that the transactions are executed correctly and reliably, and that the database is always in a consistent state.