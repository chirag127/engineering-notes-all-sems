# Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relational database .
- A domain defines the **data type**, **format**, and **constraints** of an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- For example, the domain of Marital Status can have the values {Married, Single, Divorced}, and the domain of Shift can have the values {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- A domain can be **simple** or **composite**, depending on whether it is composed of one or more subdomains.
- For example, the domain of Address can be a composite domain consisting of subdomains for Street, City, State, and Zip Code.
- A domain can be **scalar** or **nonscalar**, depending on whether it can hold only one value or a collection of values.
- For example, the domain of Phone Number can be a nonscalar domain that can hold multiple phone numbers for a person.
- A domain can be **user-defined** or **system-defined**, depending on whether it is created by the user or the database system.
- For example, the domain of Date can be a system-defined domain that has a predefined format and range.
- A domain can be **named** or **unnamed**, depending on whether it has a specific name or not.
- For example, the domain of Marital Status can be a named domain, while the domain of {1, 2, 3} can be an unnamed domain.
- A domain can be **shared** or **local**, depending on whether it is used by more than one attribute or not.
- For example, the domain of Employee ID can be a shared domain that is used by multiple attributes in different relations, while the domain of Salary can be a local domain that is used by only one attribute in one relation.