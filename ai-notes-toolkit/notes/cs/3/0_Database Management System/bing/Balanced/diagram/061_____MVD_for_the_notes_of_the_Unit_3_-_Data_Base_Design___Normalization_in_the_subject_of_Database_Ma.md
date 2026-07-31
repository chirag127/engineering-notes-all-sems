### MVD for the notes of the Unit 3 - Data Base Design & Normalization in the subject of Database Management System

- MVD stands for **Multivalued Dependency**.
- It is a type of **constraint** between two sets of attributes in a relation.
- It means that for a single value of one attribute, multiple values of another attribute exist.
- For example, if a person has multiple hobbies and works on multiple projects, then there is a MVD between the person and the hobbies, and between the person and the projects.
- We write it as `A --> --> B`, which means A is multivalued dependent on B.
- MVD plays a role in the **4NF** database normalization.
- 4NF is a normal form that requires a relation to be in **BCNF** and have no MVDs.
- BCNF is a normal form that requires a relation to be in **3NF** and have no **partial dependencies** or **transitive dependencies**.
- 3NF is a normal form that requires a relation to be in **2NF** and have no transitive dependencies.
- 2NF is a normal form that requires a relation to be in **1NF** and have no partial dependencies.
- 1NF is a normal form that requires a relation to have only **atomic values** and no **repeating groups**.
- The purpose of normalization is to **reduce redundancy**, **maintain consistency**, and **save space** in a database.
- To normalize a relation, we need to find the **closure** of a set of **functional dependencies** and/or MVDs.
- A functional dependency is a constraint that says that the value of one attribute determines the value of another attribute.
- The closure of a set of dependencies is the set of all dependencies that can be derived from the given set using some rules.
- To find the closure of a set of dependencies, we can use the following algorithm:

```
Input: A set of attributes R and a set of dependencies F
Output: The closure of F, denoted by F+
Steps:
1. Initialize F+ to F
2. Repeat until F+ does not change
  a. If A --> B and B --> C are in F+, then add A --> C to F+
  b. If A --> B and A --> C are in F+, then add A --> BC to F+
  c. If A --> BC and A --> D are in F+, then add A --> BCD to F+
  d. If A --> B is in F+ and A is a subset of R, then add R --> B to F+
3. Return F+
```

- To decompose a relation into 4NF, we can use the following algorithm:

```
Input: A relation R and a set of dependencies F
Output: A set of relations in 4NF
Steps:
1. Find the closure of F, denoted by F+
2. Find a minimal cover of F+, denoted by G
3. For each dependency A --> B in G, create a relation with attributes AB
4. If none of the relations created in step 3 contains a candidate key of R, then create a relation with any candidate key of R
5. Return the set of relations created in steps 3 and 4
```

- A minimal cover of a set of dependencies is a set of dependencies that is equivalent to the original set, but has no redundant dependencies, no redundant attributes, and no extraneous attributes.
- A candidate key of a relation is a set of attributes that can uniquely identify each tuple in the relation.