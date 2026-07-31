# Fuzzy set theory and operations

## Fuzzy set theory

- Fuzzy set theory is a branch of mathematics that deals with sets whose elements have degrees of membership.
- Fuzzy sets are a generalization of crisp sets, which are sets whose elements have binary membership (either 0 or 1).
- Fuzzy sets allow for the representation of uncertainty, vagueness, and imprecision in real-world problems.
- Fuzzy sets are denoted with a tilde sign on top of the normal set notation, such as $\tilde{A}$.
- A fuzzy set $\tilde{A}$ is defined by a membership function $\mu_{\tilde{A}}$ that assigns a degree of membership to each element in the universe of discourse $U$.
- The membership function $\mu_{\tilde{A}}$ can take any value between 0 and 1, where 0 means no membership and 1 means full membership.
- A fuzzy set can be represented graphically by a plot of the membership function versus the elements of the universe.

## Fuzzy set operations

- Fuzzy set operations are a generalization of crisp set operations for fuzzy sets.
- There are different ways to define fuzzy set operations, but the most widely used ones are called standard fuzzy set operations.
- The standard fuzzy set operations are fuzzy complements, fuzzy intersections, and fuzzy unions.
- Fuzzy complements are defined by applying the negation operator to the membership function of a fuzzy set.
- Fuzzy intersections are defined by applying the minimum operator to the membership functions of two or more fuzzy sets.
- Fuzzy unions are defined by applying the maximum operator to the membership functions of two or more fuzzy sets.
- Fuzzy set operations can be represented graphically by plotting the membership functions of the resulting fuzzy sets versus the elements of the universe.

## Examples of fuzzy set operations

- Let $U = \{1, 2, 3, 4, 5\}$ be the universe of discourse and let $\tilde{A}$ and $\tilde{B}$ be two fuzzy sets defined by the following membership functions:

| x | $\mu_{\tilde{A}}(x)$ | $\mu_{\tilde{B}}(x)$ |
|---|---------------------|---------------------|
| 1 | 0.2                 | 0.8                 |
| 2 | 0.4                 | 0.6                 |
| 3 | 0.6                 | 0.4                 |
| 4 | 0.8                 | 0.2                 |
| 5 | 1.0                 | 0.0                 |

- The fuzzy complement of $\tilde{A}$ is denoted by $\tilde{A}^c$ and is defined by:

| x | $\mu_{\tilde{A}^c}(x)$ |
|---|------------------------|
| 1 | 0.8                    |
| 2 | 0.6                    |
| 3 | 0.4                    |
| 4 | 0.2                    |
| 5 | 0.0                    |

- The fuzzy intersection of $\tilde{A}$ and $\tilde{B}$ is denoted by $\tilde{A} \cap \tilde{B}$ and is defined by:

| x | $\mu_{\tilde{A} \cap \tilde{B}}(x)$ |
|---|-------------------------------------|
| 1 | 0.2                                 |
| 2 | 0.4                                 |
| 3 | 0.4                                 |
| 4 | 0.2                                 |
| 5 | 0.0                                 |

- The fuzzy union of $\tilde{A}$ and $\tilde{B}$ is denoted by $\tilde{A} \cup \tilde{B}$ and is defined by:

| x | $\mu_{\tilde{A} \cup \tilde{B}}(x)$ |
|---|-------------------------------------|
| 1 | 0.8                                 |
| 2 | 0.6                                 |
| 3 | 0.6                                 |
| 4 | 0.8                                 |
| 5 | 1.0                                 |

- The following