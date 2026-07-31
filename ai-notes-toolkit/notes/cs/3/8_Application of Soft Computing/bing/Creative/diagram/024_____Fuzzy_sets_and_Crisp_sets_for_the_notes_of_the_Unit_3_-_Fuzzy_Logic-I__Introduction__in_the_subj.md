### Fuzzy sets and Crisp sets

- Fuzzy sets and Crisp sets are two different set theories that deal with the representation of uncertainty and vagueness in data and information.
- A **crisp set** is a set that has a clear and precise boundary, and its elements either belong or do not belong to the set. A crisp set follows the binary logic of true or false, 1 or 0, yes or no. For example, the set of even numbers is a crisp set, as any number is either even or not.
- A **fuzzy set** is a set that has an indeterminate and gradual boundary, and its elements have a degree of membership to the set that ranges from 0 to 1. A fuzzy set follows the infinite-valued logic of possibility and probability, where the truth value of a statement can be any real number between 0 and 1. For example, the set of tall people is a fuzzy set, as the concept of tallness is subjective and relative, and different people may have different opinions on how tall someone is.
- The main difference between fuzzy sets and crisp sets is that fuzzy sets allow for partial and ambiguous membership, while crisp sets require complete and definite membership. Fuzzy sets can capture the nuances and variations of natural language and human perception, while crisp sets can only represent precise and objective facts.
- Fuzzy sets are denoted by a membership function that assigns a degree of membership to each element in the universe of discourse. The membership function can be any mathematical function that satisfies the following properties:
  - It is defined for every element in the universe of discourse.
  - It takes values between 0 and 1, inclusive.
  - It is non-negative and non-decreasing.
- Crisp sets are denoted by a characteristic function that assigns a binary value to each element in the universe of discourse. The characteristic function can be any mathematical function that satisfies the following properties:
  - It is defined for every element in the universe of discourse.
  - It takes values of either 0 or 1, exclusive.
  - It is non-negative and non-decreasing.
- Fuzzy sets generalize crisp sets, as the characteristic functions of crisp sets are special cases of the membership functions of fuzzy sets, if the latter only takes values 0 or 1.
- Fuzzy sets and crisp sets can be represented graphically by using diagrams that show the elements in the universe of discourse and their degrees or values of membership. A common type of diagram is the **fuzzy set diagram**, which uses a horizontal axis to represent the elements and a vertical axis to represent the degrees of membership. The membership function is plotted as a curve that connects the points corresponding to the degrees of membership of each element. A crisp set can be represented by a fuzzy set diagram with a step function that jumps from 0 to 1 at the boundary of the set.
- Another type of diagram is the **Venn diagram**, which uses circles or other shapes to represent the sets and their intersections. The elements in the universe of discourse are placed inside or outside the shapes depending on their membership to the sets. A fuzzy set can be represented by a Venn diagram with a fuzzy boundary that indicates the degrees of membership of the elements. A crisp set can be represented by a Venn diagram with a sharp boundary that separates the elements into two groups.

Here are some examples of fuzzy sets and crisp sets and their diagrams:

- The set of positive numbers is a crisp set, as any number is either positive or not. Its characteristic function is:

  - C(x) = 1, if x > 0
  - C(x) = 0, otherwise

  Its fuzzy set diagram is:

  ![fuzzy set diagram of positive numbers](https://i.imgur.com/5c5l9tK.png)

  Its Venn diagram is:

  ![Venn diagram of positive numbers](https://i.imgur.com/8fZ4w1F.png)

- The set of young people is a fuzzy set, as the concept of youth is subjective and relative. Its membership function can be:

  - M(x) = 1, if x <= 18
  - M(x) = (30 - x) / 12, if 18 < x < 30
  - M(x) = 0, if x >= 30

  Its fuzzy set diagram is:

  ![fuzzy set diagram of young people](https://i.imgur.com/9y0bZw7.png)

  Its Venn diagram is:

  ![Venn diagram of young people