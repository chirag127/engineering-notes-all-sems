# Relational Model Terminology – Domains

- A **domain** is the set of all possible values that an attribute can have in a relation .
- A domain defines the **data type** and the **constraints** for an attribute .
- A domain is **atomic**, meaning that each value in the domain is indivisible as far as the relational model is concerned .
- A domain is also **homogeneous**, meaning that all the values in the domain have the same data type and constraints.
- A domain can be **named** or **unnamed**. A named domain has a unique identifier that can be referenced by multiple attributes. An unnamed domain is defined by the attribute itself.
- A domain can be **simple** or **composite**. A simple domain has only one component, such as integer or string. A composite domain has multiple components, such as date or address.
- A domain can be **scalar** or **nonscalar**. A scalar domain has a single value, such as number or boolean. A nonscalar domain has a collection of values, such as array or set.

## Examples of domains

- The domain of **StudentID** is the set of all possible student identification numbers, such as {123456, 234567, 345678, ...}. It is a simple, scalar, and named domain with an integer data type and a uniqueness constraint.
- The domain of **Name** is the set of all possible names, such as {"Alice", "Bob", "Charlie", ...}. It is a simple, scalar, and unnamed domain with a string data type and a length constraint.
- The domain of **DOB** is the set of all possible dates of birth, such as {01/01/2000, 02/02/2001, 03/03/2002, ...}. It is a composite, scalar, and unnamed domain with a date data type and a range constraint.
- The domain of **Courses** is the set of all possible courses that a student can enroll in, such as {"CS101", "CS102", "CS103", ...}. It is a simple, nonscalar, and unnamed domain with a string data type and a cardinality constraint.