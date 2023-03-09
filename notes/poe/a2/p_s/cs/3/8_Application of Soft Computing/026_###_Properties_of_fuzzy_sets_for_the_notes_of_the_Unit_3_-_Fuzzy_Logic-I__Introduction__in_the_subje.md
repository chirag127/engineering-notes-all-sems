 Here is the content in markdown format for the topic ### Properties of fuzzy sets for the notes of the Unit 3 - Fuzzy Logic-I (Introduction) in the subject of Application of Soft Computing:

### Properties of fuzzy sets:

1. Membership grade: In fuzzy sets, each element has a grade of membership ranging between 0 and 1. The membership grade represents the degree to which an element belongs to the set.
2. Non-empty: A fuzzy set contains at least one element with a membership grade greater than 0.
3. Normal: The sum of the membership grades of all elements of a fuzzy set is equal to 1.
$$ \sum_{x{\epsilon} X} \mu_A(x) = 1 $$
Where $\mu_A(x)$ is the membership function of fuzzy set $A$.
4. Convex: The line segment joining any two points in the membership function of a fuzzy set must lie inside or on the boundary of the membership function.
5. Bounded: Membership functions have a finite range and are bounded above by 1.
$$0 \le \mu_A(x) \le 1 \qquad \forall x \in X$$

Advantages:
- Allows intermediate degrees of membership rather than binary sets (either 0 or 1).
- Mimics human thought processes which are often ambiguous and uncertain rather than precise.
- Used in applications like control systems, pattern recognition, decision making, etc. to handle imprecise or uncertain information.

Disadvantages:
- Increased computational complexity compared to binary sets.
- Difficult to determine appropriate membership functions for a problem.
- Prone to subjectivity as membership functions are designed based on experience and intuition.

[Detailed diagrams, examples and applications can be added here if required.]