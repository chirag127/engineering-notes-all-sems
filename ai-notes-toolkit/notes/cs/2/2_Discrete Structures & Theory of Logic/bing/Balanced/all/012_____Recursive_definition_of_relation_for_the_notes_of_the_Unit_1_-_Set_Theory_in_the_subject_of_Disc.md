# Recursive definition of relation

A relation is a set of ordered pairs that satisfies some property. A recursive definition of a relation is a way of specifying a relation by giving a rule that generates the next element of the relation from the previous ones. A recursive definition consists of two parts:

- A **base case** that specifies one or more initial elements of the relation.
- A **recursive step** that specifies how to obtain new elements of the relation from the existing ones.

For example, consider the relation R on the set of natural numbers N, defined as follows:

- (0,0) ∈ R (base case)
- If (x,y) ∈ R, then (x+1,y+1) ∈ R and (x+2,y) ∈ R (recursive step)

This relation can be visualized as a tree, where each node represents an ordered pair in R, and each edge represents an application of the recursive step:

![tree](https://i.stack.imgur.com/7Yy0m.png)

Some properties of recursive definitions of relations are:

- A recursive definition may not generate all the elements of a relation, but only a subset of it. For example, the recursive definition above does not generate the pair (1,0), even though it belongs to the relation R.
- A recursive definition may generate the same element more than once, but this does not affect the relation. For example, the recursive definition above generates the pair (2,1) twice, but this does not change the fact that (2,1) ∈ R.
- A recursive definition may not terminate, meaning that there is no finite way of listing all the elements of the relation. For example, the recursive definition above does not terminate, because there is always a way to generate a new element from an existing one.