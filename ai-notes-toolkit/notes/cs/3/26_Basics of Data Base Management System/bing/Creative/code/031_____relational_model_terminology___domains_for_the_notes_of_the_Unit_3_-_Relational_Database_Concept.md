### Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relational database .
- A domain defines the **data type**, **format**, and **constraints** of an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- A domain is **independent** of any relation that uses it, meaning that the same domain can be used by different attributes in different relations .
- A domain is **named**, meaning that it has a unique identifier that distinguishes it from other domains .

Some examples of domains are:

- The domain of **Marital Status** has a set of possibilities: Married, Single, Divorced.
- The domain of **Shift** has the set of all possible days: {Mon, Tue, Wed…}.
- The domain of **Age** has the range of all positive integers.
- The domain of **Email** has the format of a valid email address.

Domains are important for the relational model because they:

- Ensure **data integrity**, meaning that the data stored in the database are valid and consistent .
- Facilitate **data manipulation**, meaning that the data can be easily queried, updated, and deleted using the relational algebra and SQL .
- Support **data abstraction**, meaning that the data are represented at a logical level without depending on the physical implementation .