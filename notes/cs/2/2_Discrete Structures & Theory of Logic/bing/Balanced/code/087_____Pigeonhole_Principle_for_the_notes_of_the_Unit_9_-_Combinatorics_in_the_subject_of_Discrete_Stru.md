# Pigeonhole Principle

- The pigeonhole principle is a basic concept in combinatorics that states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.
- The principle can be used to prove the existence of certain outcomes without explicitly finding them, by showing that there are more possibilities than cases.
- The principle can also be generalized to different scenarios, such as when the items or containers have different properties, or when the items are distributed unevenly.
- Some examples of the pigeonhole principle are:

  - If you have 10 pigeons and 9 holes, then at least one hole has more than one pigeon.
  - If you have 20 socks of two colors in a drawer, then you need to pull only three socks to get a matching pair.
  - If you have 16 pigeons in 5 holes, then some hole has at least 4 pigeons.
  - If you have 10 points within a unit equilateral triangle, then there exists two points with distance at most 1/3 apart.
  - If you have 13 cards from a standard deck, then you have at least two cards of the same suit.

- The pigeonhole principle can be formally stated as follows:

  - Let A and B be finite sets, and let f : A -> B be a function. If |A| > |B|, then f is not injective, i.e., there exist distinct elements x, y in A such that f(x) = f(y).
  - Equivalently, if f : A -> B is injective, then |A| <= |B|.
  - In other words, if there are more items than containers, then some container has more than one item. If every container has at most one item, then there are at least as many containers as items.