### Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relation .
- A domain defines the **data type** and the **constraints** for an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- For example, the domain of Marital Status can be {Married, Single, Divorced}, the domain of Shift can be {Mon, Tue, Wed, Thu, Fri, Sat, Sun}, and the domain of Salary can be any positive integer number .
- A domain can be **named** or **unnamed**. A named domain has a unique identifier that can be referenced by multiple attributes in different relations. An unnamed domain is defined by the attribute itself and cannot be shared by other attributes.
- A domain can be **simple** or **composite**. A simple domain consists of a single data type, such as integer, string, or date. A composite domain consists of multiple data types, such as address or phone number.
- A domain can be **scalar** or **nonscalar**. A scalar domain has a single value for each attribute, such as name or age. A nonscalar domain has a collection of values for each attribute, such as hobbies or skills.