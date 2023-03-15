Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of order of relations for the notes of the unit 1 - set theory in the subject of discrete structures and theory of logic.

### Order of relations

- A relation R on a set A is called an **order relation** or a **partial order** if it satisfies the following properties for all x, y, and z in A:
  - **Reflexivity**: xRx
  - **Antisymmetry**: if xRy and yRx, then x = y
  - **Transitivity**: if xRy and yRz, then xRz
- An order relation is also called a **partial order** because it may not compare every pair of elements in A. For example, the relation of "divides" on the set of positive integers is a partial order, but it does not compare 2 and 3, since neither 2 divides 3 nor 3 divides 2.
- A set A with a partial order R is called a **partially ordered set** or a **poset**, denoted by (A, R).
- A partial order R on a set A is called a **total order** or a **linear order** if it also satisfies the following property for all x and y in A:
  - **Comparability**: either xRy or yRx
- A total order is also called a **linear order** because it arranges the elements of A in a linear sequence, such as the usual order of numbers or alphabets. For example, the relation of "less than or equal to" on the set of real numbers is a total order.
- A set A with a total order R is called a **totally ordered set** or a **chain**, denoted by (A, R).
- A subset B of a poset (A, R) is called a **chain** if (B, R) is a totally ordered set. For example, the set {1, 2, 4, 8} is a chain in the poset of positive integers with the relation of "divides".
- A subset B of a poset (A, R) is called an **antichain** if no two distinct elements of B are comparable by R. For example, the set {2, 3, 5, 7} is an antichain in the poset of positive integers with the relation of "divides".
- A relation R on a set A is called a **strict partial order** if it satisfies the following properties for all x, y, and z in A:
  - **Irreflexivity**: not xRx
  - **Asymmetry**: if xRy, then not yRx
  - **Transitivity**: if xRy and yRz, then xRz
- A strict partial order is a partial order without reflexivity and antisymmetry. For example, the relation of "less than" on the set of real numbers is a strict partial order.
- A relation R on a set A is called a **strict total order** or a **linear order** if it is a strict partial order and it also satisfies the following property for all x and y in A:
  - **Comparability**: either xRy or yRx
- A strict total order is a total order without reflexivity and antisymmetry. For example, the relation of "less than" on the set of real numbers is a strict total order.