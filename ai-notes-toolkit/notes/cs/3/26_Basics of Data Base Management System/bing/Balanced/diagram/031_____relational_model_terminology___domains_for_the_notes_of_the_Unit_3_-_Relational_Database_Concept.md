### Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relation  .
- A domain is defined by a **name**, a **data type**, and a set of **constraints** that limit the values that can belong to the domain .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- A domain is also **homogeneous**, meaning that all the values in the domain have the same data type and conform to the same constraints.
- A domain can be **simple** or **composite**, depending on whether it is composed of one or more subdomains.
- A domain can be **scalar** or **nonscalar**, depending on whether it can be decomposed into smaller components.
- A domain can be **user-defined** or **system-defined**, depending on whether it is created by the user or by the database management system.
- A domain can be **shared** or **local**, depending on whether it is used by more than one attribute or relation in the database schema.

#### Examples of domains

- The domain of **Marital Status** has a set of possible values: Married, Single, Divorced.
- The domain of **Shift** has the set of all possible days: {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- The domain of **Age** has a data type of integer and a constraint that the value must be between 0 and 150.
- The domain of **Email** has a data type of string and a constraint that the value must contain the @ symbol.
- The domain of **Address** is a composite domain that consists of subdomains for street, city, state, and zip code.
- The domain of **Image** is a nonscalar domain that can be decomposed into pixels, colors, and formats.
- The domain of **Boolean** is a system-defined domain that has only two possible values: true or false.
- The domain of **EmployeeID** is a local domain that is used only by the attribute EmployeeID in the relation Employee.