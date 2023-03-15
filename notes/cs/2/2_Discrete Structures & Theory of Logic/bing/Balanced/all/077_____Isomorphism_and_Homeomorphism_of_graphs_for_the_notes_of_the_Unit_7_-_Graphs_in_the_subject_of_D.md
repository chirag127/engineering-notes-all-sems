# Isomorphism and Homeomorphism of graphs

## Isomorphism

- Two graphs G and H are **isomorphic** (denoted by G ≅ H) if they have the same number of vertices connected in the same way.
- Formally, an **isomorphism** between graphs G and H is a **bijection** (one-to-one and onto) f: V(G) → V(H) such that for any two vertices u and v in G, (u, v) is an edge in G if and only if (f(u), f(v)) is an edge in H .
- An isomorphism preserves both **edges and non-edges** of a graph .
- An isomorphism also preserves the **degree** of each vertex, the **number of components** of the graph, the **cycle structure** of the graph, and any other graph property that depends only on the abstract structure of the graph.
- Checking for isomorphism between two graphs is a **computationally hard** problem, as there is no known efficient algorithm to do so.

## Homeomorphism

- Two graphs G and H are **homeomorphic** if there is a graph isomorphism from some **subdivision** of G to some subdivision of H.
- A **subdivision** of a graph is obtained by replacing each edge with a path of one or more edges, without introducing new vertices of degree 2.
- A **homeomorphism** between graphs G and H is a **mapping** f: V(G) → V(H) such that for any two vertices u and v in G, (u, v) is an edge in G if and only if there is a **path** from f(u) to f(v) in H.
- A homeomorphism preserves only **edges** of a graph, but not necessarily non-edges .
- A homeomorphism also preserves the **connectedness** of a graph, but not necessarily the degree of each vertex, the number of components, or the cycle structure.
- Checking for homeomorphism between two graphs is a **computationally easy** problem, as there is a known efficient algorithm to do so.