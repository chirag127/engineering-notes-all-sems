### Relational Model Terminology – Domains

- A domain is the set of all possible values that an attribute can have in a relation  .
- A domain is defined by a name, a data type, and a set of constraints .
- A domain is atomic, meaning that each value in the domain is indivisible as far as the relational model is concerned  .
- A domain can be shared by multiple attributes in different relations, as long as they have the same name, data type, and constraints .
- A domain can be simple or composite, depending on whether it is composed of one or more subdomains.
- A domain can be scalar or nonscalar, depending on whether it can be decomposed into smaller components.

Some examples of domains are:

- The domain of Marital Status has a set of possibilities: Married, Single, Divorced .
- The domain of Shift has the set of all possible days: {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.
- The domain of Phone Number has a data type of string and a constraint of 10 digits.
- The domain of Address has a composite structure of subdomains: Street, City, State, Zip Code.
- The domain of Image has a nonscalar structure of pixels and colors.